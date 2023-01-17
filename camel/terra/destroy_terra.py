"""
This script defines the entry point for terra-destroy.
"""
import argparse
import os
from pathlib import Path
from subprocess import Popen
from typing import Any, Dict

import boto3
from gerund.components.variable import Variable

from camel.basecamp.projects.adapters.terra_apply import TerraApplyProjectAdapter
from camel.storage.components.profile_storage import LocalProfileVariablesStorage
from camel.terra.config_loader import ConfigEngine
from camel.terra_configs.components.config_mapper import TerraConfigMapper


def _delete_tf_state_file(config: dict) -> None:
    """
    Deletes the state from s3.

    Args:
        config: (dict) the config for the build being destroyed

    Returns: None
    """
    backend_config: Dict[str, str] = config["build_state"]
    backend_bucket: str = Variable(backend_config["bucket"]).value
    backend_key: str = Variable(backend_config["key"]).value
    backend_region: str = Variable(backend_config["region"]).value

    build_variables: Dict[str, str] = config["build_variables"]
    aws_access_key: str = Variable(build_variables["aws_access_key"]).value
    aws_secret_access_key: str = Variable(build_variables["aws_secret_access_key"]).value

    client = boto3.client('s3', aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=backend_region)
    client.delete_object(Bucket=backend_bucket, Key=backend_key)


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


def _get_init_config(config: dict) -> str:
    """
    Extracts the backend terraform config command from the config file.

    Args:
        config: (dict) the config file loaded for the model run

    Returns: (str) the backend terraform config command
    """
    backend_config = config["build_state"]
    backend_bucket = backend_config["bucket"]
    backend_key = backend_config["key"]
    backend_region = backend_config["region"]

    backend_config_bucket = f' -backend-config="bucket={backend_bucket}"'
    backend_config_key = f' -backend-config="key={backend_key}"'
    backend_config_region = f' -backend-config="region={backend_region}"'

    return f'terraform init -reconfigure {backend_config_bucket} {backend_config_key} {backend_config_region}'


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

    if args.config_name != "none":
        print(f"destroying existing config: {args.config_name}")
        config_map = TerraConfigMapper.get_cached_profile()
        config_path: str = config_map.terra_builds_path + f"/{args.config_name}.yml"
    else:
        config_path: str = str(os.getcwd()) + f"/{args.config_path}"

    file_path: str = str(Path(__file__).parent) + "/terra_builds"

    config = ConfigEngine(config_path=config_path)
    project_adapter = TerraApplyProjectAdapter(config=config)

    command_buffer = [f'cd {file_path}/{config["location"]} ', '&& ', 'terraform destroy ']
    variables = config["build_variables"]
    variables["state_tag"] = config["model_variables"].get("state_s3_key")

    for key in variables:
        current_value = _extract_variable(key=key, lookup_dict=variables, label="terraform variables")
        command_buffer.append(f'-var="{key}={current_value}" ')
    command_buffer.append("-auto-approve")

    command = "".join(command_buffer)

    if project_adapter.continue_building is True:

        config_command: str = _get_init_config(config=config)

        project_adapter.destroy_build()
        init_terraform = Popen(f'cd {file_path}/{config["location"]} && {config_command}', shell=True)
        init_terraform.wait()
        run_terraform = Popen(command, shell=True)
        run_terraform.wait()
        project_adapter.declare_destroyed()
        _delete_tf_state_file(config=config)
