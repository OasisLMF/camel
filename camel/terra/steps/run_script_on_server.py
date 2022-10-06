"""
This file defines the step that runs a script on another server.
"""
from typing import Optional
from subprocess import Popen

from camel.terra.steps.base import Step
from gerund.components.variable_map import VariableMap
from gerund.commands.terminal_command import TerminalCommand


class RunScriptOnServerStep(Step):
    """
    This class is responsible for defining the step that copies a python script onto a server and then runs that
    script on the server that has been created in the terraform build.

    Attributes:
        server_ip (str): the IP address of the server running the script
        script_name (str): the name of the script that is going to be run on the server
        location (str): the location of where the terraform build is
        parameters (dict): parameters that will be passed into the script being run on the server
    """
    def __init__(self, input_params: dict, terraform_data: dict, location: str) -> None:
        """
        The constructor for the RunScriptOnServerStep class.

        Args:
            input_params: (dict) the parameters directly from the step being read
            terraform_data: (dict) the data produced from the terraform build once it is completed
            location: (str) the location of where the terraform build is
        """
        self.server_ip: Optional[str] = None
        self.script_name: Optional[str] = None
        self.location = location
        self.parameters: Optional[dict] = None
        self.environment_variables: Optional[dict] = None
        self._process_inputs(input_data=input_params, terraform_dict=terraform_data)

    def _process_inputs(self, input_data: dict, terraform_dict: dict) -> None:
        """
        Extracts the data needed from the terraform build and step parameters to run the step.

        Args:
            input_data: (dict) the parameters directly from the step being read
            terraform_dict: (dict) the data produced from the terraform build once it is completed

        Returns: None
        """
        self.server_ip = terraform_dict["main_server_ip"]["value"][0]
        self.script_name = input_data["script_name"]
        self.parameters = input_data.get("variables", {})
        self.environment_variables = input_data.get("env_vars", {})

    def run(self) -> None:
        """
        Runs the step which consists of adding new server ip to known hosts, copying the script to be run on the
        new server, and then running the script with the parameters specified.

        Returns: None
        """
        VariableMap().ip_address = self.server_ip
        add_to_known_hosts = Popen(f'ssh-keyscan -H "{self.server_ip}" >> ~/.ssh/known_hosts', shell=True)
        add_to_known_hosts.wait()

        copy_to_server = Popen(f"scp {self.location}/{self.script_name}.py ubuntu@{self.server_ip}:/home/ubuntu/{self.script_name}.py",
                               shell=True)
        copy_to_server.wait()

        command = f"cd /home/ubuntu/ && python3 {self.script_name}.py"
        buffer = list()
        buffer.append(command)

        for param_key in self.parameters.keys():
            buffer.append(f" --{param_key} {self.parameters[param_key]}")

        command = "".join(buffer)

        # run_script = TerminalCommand(command=command, environment_variables=self.environment_variables,
        #                              ip_address=self.server_ip)
        # run_script.wait()

        run_script = Popen(f"ssh -A -o StrictHostKeyChecking=no ubuntu@{self.server_ip} '{command}'", shell=True)
        run_script.wait()
