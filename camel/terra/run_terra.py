"""
This script defines the entry point for terra-apply.
"""
import argparse
import json
import os
from pathlib import Path
from subprocess import Popen
from typing import Any

from camel.terra.config_loader import ConfigEngine
from camel.terra_configs.components.config_mapper import TerraConfigMapper
from camel.storage.components.profile_storage import LocalProfileVariablesStorage

from camel.terra.steps.run_script_on_server import RunScriptOnServerStep


def _extract_variable(key: str, lookup_dict: dict, label: str) -> Any:
    current_value = lookup_dict.get(key)

    if current_value is None:
        raise ValueError(f"{key} not found in {label} config")

    if isinstance(current_value, str) and current_value[:2] == "=>":
        local_storage = LocalProfileVariablesStorage()
        current_value = local_storage.get(current_value[2:])

        if current_value is None:
            raise ValueError(f"{current_value[2:]} not found in profile storage")
    return current_value


def translate_dictionary(config: dict, label: str) -> dict:
    for key in config.keys():
        config[key] = _extract_variable(key=key, lookup_dict=config, label=label)
    return config


def _run_terraform_build_commands(file_path: str, config:dict) -> str:
    command_buffer = [f'cd {file_path}/{config["location"]} ', '&& ', 'terraform apply ']
    variables = config["variables"]

    for key in variables:
        current_value = _extract_variable(key=key, lookup_dict=variables, label="terraform variables")
        command_buffer.append(f'-var="{key}={current_value}" ')

    command = "".join(command_buffer)

    init_terraform = Popen(f'cd {file_path}/{config["location"]} && terraform init -reconfigure', shell=True)
    init_terraform.wait()
    run_terraform = Popen(command, shell=True)
    run_terraform.wait()

    output_path: str = str(os.getcwd()) + "/build_output.json"

    output_terra = Popen(f'cd {file_path}/{config["location"]} && terraform output -json > {output_path}', shell=True)
    output_terra.wait()
    return output_path


def main() -> None:
    """
    Loads the data from the terra_consfig.yml config file in the current directory and run a terraform apply command.

    :return: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--config_path', action='store', type=str, required=False, default="terra_config.yml",
                               help="the path the config yml file that defines the terraform build (default: terra_config.yml)")
    config_parser.add_argument('--config_name', action='store', type=str, required=False, default="none",
                               help="the name of the existing terraform config file")
    args = config_parser.parse_args()

    if args.config_name != "none":
        print(f"running existing config: {args.config_name}")
        config_map = TerraConfigMapper.get_cached_profile()
        config_path: str = config_map.terra_builds_path + f"/{args.config_name}.yml"
    else:
        config_path: str = str(os.getcwd()) + f"/{args.config_path}"

    file_path: str = str(Path(__file__).parent) + "/terra_builds"

    config = ConfigEngine(config_path=config_path)

    output_path = _run_terraform_build_commands(file_path=file_path, config=config)

    with open(output_path, "r") as file:
        terraform_data = json.loads(file.read())

    # TODO => build a process step function

    # TODO => build variable component (remote and local)

    # TODO => build if step with fields: left, right, condition(enum like ==, !=, >= etc) and then pass in step object to run
    if config.steps is not None:
        for step in config.steps:
            if step["name"] == "run_script":
                processed_step_params = translate_dictionary(config=step, label="step configuration for run script")
                step_process = RunScriptOnServerStep(input_params=processed_step_params,
                                                     terraform_data=terraform_data,
                                                     location=f'{file_path}/{config["location"]}')
                step_process.run()
