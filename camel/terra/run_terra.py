"""
This script defines the entry point for terra-apply.
"""
import os
from pathlib import Path
from subprocess import Popen
import argparse
import json

from camel.terra.config_loader import ConfigEngine


def _run_script_on_server(server_ip: str, script_name: str, location: str) -> None:
    # /home/ubuntu/
    copy_to_server = Popen(f"scp {location}/{script_name}.py ubuntu@{server_ip}:/home/ubuntu/{script_name}.py", shell=True)
    copy_to_server.wait()

    command = f"cd /home/ubuntu/ && python3 {script_name}.py"
    run_script = Popen(f"ssh ubuntu@{server_ip} '{command}'", shell=True)
    run_script.wait()


def main() -> None:
    """
    Loads the data from the terra_consfig.yml config file in the current directory and run a terraform apply command.

    :return: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--config_path', action='store', type=str, required=False, default="terra_config.yml")
    args = config_parser.parse_args()

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
                server_ip = terraform_data["main_server_ip"]["value"][0]
                script_name = step["script_name"]
                _run_script_on_server(server_ip=server_ip,
                                      script_name=script_name,
                                      location=f'{file_path}/{config["location"]}')
