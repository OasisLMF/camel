"""
This script defines the entry point for terra-destroy.
"""
import argparse
from subprocess import Popen
from typing import Any

from camel.storage.components.profile_storage import LocalProfileVariablesStorage
from camel.terra.components.config_loader import ConfigEngine
from camel.terra.utils import extract_paths, get_init_config
from camel.terra.processes.delete_tf_state_file import delete_tf_state_file


def _extract_variable(key: str, lookup_dict: dict, label: str) -> Any:
    # TODO => consider getting rid of this and having a standard Variable object instead
    current_value = lookup_dict.get(key)

    if current_value is None:
        raise ValueError(f"{key} not found in {label} config")

    if isinstance(current_value, str) and current_value[:2] == "=>":
        local_storage = LocalProfileVariablesStorage()
        current_value = local_storage.get(current_value[2:])

        if current_value is None:
            raise ValueError(f"{current_value[2:]} not found in profile storage")
    return current_value


def main() -> None:
    """
    Loads the data from the terra_config.yml config file in the current directory and run a terraform apply command.

    :return: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--config_path', action='store', type=str, required=False, default="terra_config.yml",
                               help="the path to the config yml file that defines the terraform build that is going"
                                    " to be destroyed (default: terra_config.yml)")
    config_parser.add_argument('--config_name', action='store', type=str, required=False, default="none",
                               help="the name of the existing terraform config file")

    args = config_parser.parse_args()

    config_map, config_path, file_path = extract_paths(config_name=args.config_name, config_path=args.config_path)

    config = ConfigEngine(config_path=config_path)

    command_buffer = [f'cd {file_path}/{config["location"]} ', '&& ', 'terraform destroy ']
    variables = config["build_variables"]
    variables["state_tag"] = config["model_variables"].get("state_s3_key")

    for key in variables:
        current_value = _extract_variable(key=key, lookup_dict=variables, label="terraform variables")
        command_buffer.append(f'-var="{key}={current_value}" ')
    command_buffer.append("-auto-approve")

    command = "".join(command_buffer)

    config_command: str = get_init_config(config=config)
    init_terraform = Popen(f'cd {file_path}/{config["location"]} && {config_command}', shell=True)
    init_terraform.wait()
    run_terraform = Popen(command, shell=True)
    run_terraform.wait()
    delete_tf_state_file(config=config)
