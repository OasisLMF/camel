"""
This script defines the entry point for terra-apply. This file takes a functional approach however, we do not want to
just litter the file with loads of functions. If a theme of functionality can be found we should package it as a
module or object and abstract it out of the file. The aim of this file is to define the flow of running a terra-apply
command. Examples of code being packaged as objects and abstracted out is:

- components/variable.py
- components/variable_map.py
- steps/run_script_on_server.py
"""
import argparse
import json
import os
from pathlib import Path
from subprocess import Popen
from typing import Optional

from camel.basecamp.projects.adapters.terra_apply import TerraApplyProjectAdapter
from camel.terra.adapters.edit_state_position import EditStatePositionAdapter
from camel.terra.components.server_build_bash_generator import ServerBuildBashGenerator
from camel.terra.components.variable import Variable
from camel.terra.components.variable_map import VariableMap
from camel.terra.config_loader import ConfigEngine
from camel.terra.steps import StepManager
from camel.terra_configs.components.config_mapper import TerraConfigMapper


def write_server_build_bash_file(file_path: str, oasis_version: Optional[str]) -> None:
    """
    Writes a server build bash script for the terraform build.

    Args:
        file_path: (str) path to the build including the name of the script being written
        oasis_version: (Optional[str]) the version of aosis you want installed is None will be latest version

    Returns: None
    """
    bash_file = ServerBuildBashGenerator()
    bash_file.generate_script(oasislmf_version=oasis_version)
    bash_file.write_script(file_path=file_path)


def _run_terraform_build_commands(file_path: str, config: dict, output_path: str) -> None:
    """
    Builds the command for running a terraform build and runs it.

    Args:
        file_path: (str) the path to where the terraform files are for the terraform build
        config: (dict) variables to be inserted into the terraform build
        output_path: (str) the path to where the output of the terraform is done

    Returns: None
    """
    build_path: str = config["location"]
    oasis_version: Optional[str] = config.get("oasis_version")
    server_build_bash_script_path: str = f"{file_path}/{build_path}/server_build.sh"
    command_buffer = [f'cd {file_path}/{build_path} ', '&& ', 'terraform apply -auto-approve']
    variables = config["variables"]

    write_server_build_bash_file(file_path=server_build_bash_script_path, oasis_version=oasis_version)

    for key in variables:
        current_value = Variable(name=variables[key])
        command_buffer.append(f'-var="{key}={current_value}" ')

    new_state_key = variables.get("STATE_S3_KEY")
    edit_state = EditStatePositionAdapter(build_path=f"{file_path}/{build_path}")

    if new_state_key is not None:
        edit_state.update_state(s3_key=new_state_key)

    command = "".join(command_buffer)

    init_terraform = Popen(f'cd {file_path}/{build_path} && terraform init -reconfigure', shell=True)
    init_terraform.wait()
    run_terraform = Popen(command, shell=True)
    run_terraform.wait()

    output_terra = Popen(f'cd {file_path}/{build_path} && terraform output -json > {output_path}', shell=True)
    output_terra.wait()

    if new_state_key is not None:
        edit_state.revert_main_back_to_initial_state()


def main() -> None:
    """
    Loads the data from the terra_config.yml config file in the current directory and run a terraform apply command.

    :return: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--config_path', action='store', type=str, required=False, default="terra_config.yml",
                               help="the path the config yml file that defines the terraform build (default: terra_config.yml)")
    config_parser.add_argument('--config_name', action='store', type=str, required=False, default="none",
                               help="the name of the existing terraform config file")
    args = config_parser.parse_args()

    # gets the existing config if the --config_name is supplied
    if args.config_name != "none":
        print(f"running existing config: {args.config_name}")
        config_map = TerraConfigMapper.get_cached_profile()
        config_path: str = config_map.terra_builds_path + f"/{args.config_name}.yml"
    else:
        config_path: str = str(os.getcwd()) + f"/{args.config_path}"

    # defines the file path of where all the terraform builds are defined in the pip package
    file_path: str = str(Path(__file__).parent) + "/terra_builds"

    # load and extract the data from the terra build config file
    config = ConfigEngine(config_path=config_path)
    project_adapter = TerraApplyProjectAdapter(config=config)

    if project_adapter.continue_building is True:
        project_adapter.start_build()
        local_vars = config.get("local_vars", [])
        variable_map = VariableMap()

        for local_var in local_vars:
            variable_map[local_var["name"]] = local_var

        _run_terraform_build_commands(file_path=file_path, config=config,
                                      output_path=project_adapter.terraform_data_path)

        with open(project_adapter.terraform_data_path, "r") as file:
            terraform_data = json.loads(file.read())

        step_manager = StepManager(terraform_data=terraform_data, file_path=file_path, config=config)

        if config.steps is not None:
            for step in config.steps:
                step_manager.process_step(step_data=step)

        project_adapter.finish_build()
