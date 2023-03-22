"""
This file defines the process that runs the terraform build commands on the model server. Processes are currently just
functions, but they could be refactored in the future.
"""
from subprocess import Popen

from gerund.components.variable import Variable

from camel.terra.utils import get_init_config


def run_terraform_build_commands(file_path: str, config: dict, output_path: str) -> None:
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

    variables["state_tag"] = config["build_state"]["key"]

    for key in variables:
        current_value = Variable(name=variables[key])
        command_buffer.append(f'-var="{key}={current_value}" ')
    command_buffer.append("-auto-approve")

    command = "".join(command_buffer)
    config_command: str = get_init_config(config=config)

    init_terraform = Popen(f'cd {file_path}/{build_path} && {config_command}', shell=True)
    init_terraform.wait()
    run_terraform = Popen(command, shell=True)
    run_terraform.wait()

    output_terra = Popen(f'cd {file_path}/{build_path} && terraform output -json > {output_path}', shell=True)
    output_terra.wait()
