"""
This script defines the entry point for terra-apply.
"""
import argparse
import json
import os
from pathlib import Path
from subprocess import Popen

from camel.terra.config_loader import ConfigEngine
from camel.terra_configs.components.config_mapper import TerraConfigMapper

from camel.terra.steps.run_script_on_server import RunScriptOnServer


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

    command_buffer = [f'cd {file_path}/{config["location"]} ', '&& ', 'terraform apply ']
    variables = config["variables"]

    for key in variables:
        command_buffer.append(f'-var="{key}={variables[key]}" ')

    command = "".join(command_buffer)

    init_terraform = Popen(f'cd {file_path}/{config["location"]} && terraform init -reconfigure', shell=True)
    init_terraform.wait()
    run_terraform = Popen(command, shell=True)
    run_terraform.wait()

    output_path: str = str(os.getcwd()) + "/build_output.json"

    output_terra = Popen(f'cd {file_path}/{config["location"]} && terraform output -json > {output_path}', shell=True)
    output_terra.wait()

    with open(output_path, "r") as file:
        terraform_data = json.loads(file.read())

    if config.steps is not None:
        for step in config.steps:
            if step["name"] == "run_script":
                step_process = RunScriptOnServer(input_params=step,
                                                 terraform_data=terraform_data,
                                                 location=f'{file_path}/{config["location"]}')
                step_process.run()
