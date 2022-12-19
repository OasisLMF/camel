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
import time
import sys
from pathlib import Path
from subprocess import Popen
from typing import List

from gerund.commands.bash_script import BashScript
from gerund.commands.terminal_command import TerminalCommand
from gerund.components.variable import Variable
from gerund.components.variable_map import VariableMap

from camel.basecamp.projects.adapters.terra_apply import TerraApplyProjectAdapter
from camel.storage.components.profile_storage import LocalProfileVariablesStorage
from camel.terra.adapters.edit_state_position import EditStatePositionAdapter
from camel.terra.components.server_build_bash_generator import ServerBuildBashGenerator
from camel.terra.config_loader import ConfigEngine
from camel.terra.steps import StepManager
from camel.terra_configs.components.config_mapper import TerraConfigMapper
from camel.storage.adapters.builds_access import BuildsAccessAdapter


def _run_build_script(command: BashScript) -> None:
    """
    Continuously loops until the server build bash script as run on the model server.

    Args:
        command: (BashScript) the build bash script to be run on the model server

    Returns: None
    """
    count: int = 0
    keep_going: bool = True
    variable_map = VariableMap()
    variable_map["output"] = {
        "path": "/home/ubuntu/",
        "ip_address": True
    }

    while keep_going is True:
        if count >= 5:
            sys.exit("model build script tried to run 5 times and failed, model server cannot run a model because"
                     "build script has note been executed")
        time.sleep(2)
        command.wait()
        outcome = str(Variable(name=">>output"))
        if outcome == "FINISHED":
            print("build script has run")
            break
        else:
            print("build script has not run retrying")
            command._path = None
            count += 1


def run_server_config_commands(ip_address: str, config: dict) -> None:
    """
    Runs the bash script on the model server to setup the model run.

    Args:
        ip_address: (str) the IP address of the model server where the model is being run on
        config: (dict) the config data around the build

    Returns: None
    """
    # build_path: str = config["location"]

    # obtaining the variables for a server build
    repository = Variable(config["model_variables"]["repository"]).value
    oasislmf_version = Variable(config["model_variables"]["oasislmf_version"]).value

    # getting optional s3 data
    data_bucket = config["model_variables"].get("data_bucket")
    data_directory = config["model_variables"].get("data_directory")

    if data_bucket is not None:
        data_bucket = Variable(data_bucket).value
    if data_directory is not None:
        data_directory = Variable(data_directory).value

    # getting the AWS credentials for the configuration of the model by getting s3 data
    aws_access_key = Variable(config["build_variables"]["aws_access_key"]).value
    aws_secret_access_key = Variable(config["build_variables"]["aws_secret_access_key"]).value

    # configuring the bash commands to install what's needed in the model server and get the data for the model
    server_build_commands = ServerBuildBashGenerator()
    server_build_commands.generate_script(repository=repository,
                                          aws_key=aws_access_key,
                                          aws_secret_key=aws_secret_access_key,
                                          oasislmf_version=oasislmf_version,
                                          data_bucket=data_bucket,
                                          data_directory=data_directory)
    # run the bash commands on the newly built model server
    command = BashScript(commands=server_build_commands.stripped, ip_address=ip_address)
    _run_build_script(command=command)
    # command.wait()


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
    command_buffer = [f'cd {file_path}/{build_path} ', '&& ', 'terraform apply ']
    variables = config["build_variables"]

    for key in variables:
        current_value = Variable(name=variables[key])
        command_buffer.append(f'-var="{key}={current_value}" ')
    command_buffer.append("-auto-approve")

    new_state_key = config["model_variables"].get("state_s3_key")
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


def _establish_connection(ip_address: str) -> None:
    """
    Loops through SSH connections until the SSH connection is accepted.

    Args:
        ip_address: (str) the IP address of the server being connecting to

    Returns: None
    """
    connection = TerminalCommand(command="echo 'connection achieved'", ip_address=ip_address)

    connected = False
    while connected is False:
        print(f"establishing connection to: {ip_address}")
        established: List[str] = connection.wait(capture_output=True)
        established_str: str = " ".join(established).lower()

        if "refused" not in established_str:
            print("connection established")
            break
        print("connection refused trying again")
        time.sleep(3)


def main() -> None:
    """
    Loads the data from the terra_config.yml config file in the current directory and run a terraform apply command.

    :return: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--config_path', action='store', type=str, required=False, default="terra_config.yml",
                               help="the path the config yml file that defines the terraform build "
                                    "(default: terra_config.yml)")
    config_parser.add_argument('--config_name', action='store', type=str, required=False, default="none",
                               help="the name of the existing terraform config file")
    args = config_parser.parse_args()
    LocalProfileVariablesStorage()

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

        # updates the local variables with the terraform outputs
        VariableMap().ip_address = terraform_data["main_server_ip"]["value"][0]
        builds_storage_adapter: BuildsAccessAdapter = BuildsAccessAdapter()
        builds_storage_adapter.add_new_build(state_path="~/camel_builds.json",
                                             ip_address=terraform_data["main_server_ip"]["value"][0],
                                             build_name="standard_model_run")
        # builds_storage_adapter.add_new_build(state_path=, ip_address=VariableMap().ip_address, build_name=)

        _establish_connection(ip_address=VariableMap().ip_address)

        add_to_known_hosts = TerminalCommand(f'ssh-keyscan -H "{VariableMap().ip_address}" >> ~/.ssh/known_hosts')
        add_to_known_hosts.wait()

        run_server_config_commands(ip_address=VariableMap().ip_address,
                                   config=config)

        time.sleep(10)

        step_manager = StepManager(terraform_data=terraform_data, file_path=file_path, config=config)

        if config.steps is not None:
            for step in config.steps:
                step_manager.process_step(step_data=step)

        project_adapter.finish_build()
