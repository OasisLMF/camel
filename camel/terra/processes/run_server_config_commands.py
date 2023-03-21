"""
This file defines the function that runs the terraform commands to build the model server. Processes are currently just
functions, but they could be refactored in the future.
"""
from gerund.commands.bash_script import BashScript
from gerund.components.variable import Variable

from camel.terra.components.server_build_bash_generator import ServerBuildBashGenerator
from camel.terra.processes.run_build_script import run_build_script


def run_server_config_commands(ip_address: str, config: dict) -> None:
    """
    Runs the bash script on the model server to setup the model run.

    Args:
        ip_address: (str) the IP address of the model server where the model is being run on
        config: (dict) the config data around the build

    Returns: None
    """
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
    run_build_script(command=command)
