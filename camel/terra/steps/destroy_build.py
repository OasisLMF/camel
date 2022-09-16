"""
This file defines the step that destroys the terraform build.
"""
from subprocess import Popen

from gerund.components.variable import Variable

from camel.terra.steps.base import Step


class DestroyBuild(Step):
    """
    This class is responsible for destroying a terraform build in a step process.

    Attributes:
        config: (dict) the terraform configuration for parameters for destroying the build
        file_path: (str) the path to the terraform build files
    """
    def __init__(self, config: dict, file_path: str) -> None:
        """
        The constructor for the DestroyBuild class.

        Args:
            config: (dict) the terraform configuration for parameters for destroying the build
            file_path: (str) the path to the terraform build files
        """
        self.config: dict = config
        self.file_path: str = file_path

    def run(self) -> None:
        """
        Destroys the terraform build.

        Returns: None
        """
        command_buffer = [f'cd {self.file_path}/{self.config["location"]} ', '&& ', 'terraform destroy ']
        variables = self.config["variables"]

        for key in variables:
            current_value = Variable(name=variables[key])
            command_buffer.append(f'-var="{key}={current_value}" ')

        command = "".join(command_buffer)

        init_terraform = Popen(f'cd {self.file_path}/{self.config["location"]} && terraform init', shell=True)
        init_terraform.wait()
        run_terraform = Popen(command, shell=True)
        run_terraform.wait()
