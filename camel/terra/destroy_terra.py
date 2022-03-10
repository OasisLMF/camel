"""
This script defines the entry point for terra-destroy.
"""
import argparse
import os
from pathlib import Path
from subprocess import Popen

from camel.terra.config_loader import ConfigEngine


def main() -> None:
    """
    Loads the data from the terra_config.yml config file in the current directory and run a terraform apply command.

    :return: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--config_path', action='store', type=str, required=False, default="terra_config.yml")
    args = config_parser.parse_args()

    config_path: str = str(os.getcwd()) + f"/{args.config_path}"
    file_path: str = str(Path(__file__).parent) + "/terra_builds"

    config = ConfigEngine(config_path=config_path)

    command_buffer = [f'cd {file_path}/{config["location"]} ', '&& ', 'terraform destroy ']
    variables = config["variables"]

    for key in variables:
        command_buffer.append(f'-var="{key}={variables[key]}" ')

    command = "".join(command_buffer)

    init_terraform = Popen(f'cd {file_path}/{config["location"]} && terraform init', shell=True)
    init_terraform.wait()
    run_terraform = Popen(command, shell=True)
    run_terraform.wait()
