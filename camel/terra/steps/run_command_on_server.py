"""
This file defines the step that runs a command on another server.
"""
from subprocess import Popen

from camel.terra.steps.base import Step
from gerund.commands.terminal_command import TerminalCommand
from gerund.components.variable_map import VariableMap


class RunCommandOnServerStep(Step):
    """
    This class is responsible for defining the step that copies a python script onto a server and then runs that
    script on the server that has been created in the terraform build.

    Attributes:
        server_ip (str): the IP address of the server running the script
        command (str): the command that is going to be run on the server
    """
    def __init__(self, terraform_data: dict, command: str, environment_variables: dict) -> None:
        """
        The constructor for the RunCommandOnServerStep class.

        Args:
            terraform_data: (dict) the data produced from the terraform build once it is completed
            command: (str) the command that is going to be run on the server
        """
        self.server_ip: str = terraform_data["main_server_ip"]["value"][0]
        self.environment_variables: dict = environment_variables
        self.command: str = command

    def run(self) -> None:
        """
        Runs the step which consists of adding new server ip to known hosts, then running the self.command on the
        server that is SSHed into.

        Returns: None
        """
        # VariableMap().ip_address = self.server_ip
        # add_to_known_hosts = Popen(f'ssh-keyscan -H "{self.server_ip}" >> ~/.ssh/known_hosts', shell=True)
        # add_to_known_hosts.wait()

        command = f"cd /home/ubuntu/ && {self.command}"
        terminal_command = TerminalCommand(command=command,
                                           environment_variables=self.environment_variables,
                                           ip_address=self.server_ip)
        terminal_command.wait()
