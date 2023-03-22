"""
This file defines the entry point for the terra-apply command.
"""
import argparse
import json
import time

from gerund.commands.terminal_command import TerminalCommand
from gerund.components.variable_map import VariableMap

from camel.storage.components.profile_storage import LocalProfileVariablesStorage
from camel.terra.components.config_loader import ConfigEngine
from camel.terra.processes.establish_connection import establish_connection
from camel.terra.processes.run_server_config_commands import run_server_config_commands
from camel.terra.processes.run_terraform_build_commands import run_terraform_build_commands
from camel.terra.steps import StepManager
from camel.terra.utils import extract_paths, OUTPUT_FILE_PATH


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

    config_map, config_path, file_path = extract_paths(config_name=args.config_name, config_path=args.config_path)

    # load and extract the data from the terra build config file
    config = ConfigEngine(config_path=config_path)

    local_vars = config.get("local_vars", [])
    variable_map = VariableMap()

    for local_var in local_vars:
        variable_map[local_var["name"]] = local_var

    run_terraform_build_commands(file_path=file_path, config=config,
                                 output_path=OUTPUT_FILE_PATH)

    with open(OUTPUT_FILE_PATH) as file:
        terraform_data = json.loads(file.read())

    # updates the local variables with the terraform outputs
    VariableMap().ip_address = terraform_data["main_server_ip"]["value"][0]

    # add IP address to ssh key
    add_to_known_hosts = TerminalCommand(f'ssh-keyscan -H "{VariableMap().ip_address}" >> ~/.ssh/known_hosts')
    add_to_known_hosts.wait()

    # block until connection to server is available
    establish_connection(ip_address=VariableMap().ip_address)

    run_server_config_commands(ip_address=VariableMap().ip_address,
                               config=config)

    time.sleep(10)

    step_manager = StepManager(terraform_data=terraform_data, file_path=file_path, config=config)

    if config.steps is not None:
        for step in config.steps:
            step_manager.process_step(step_data=step)
