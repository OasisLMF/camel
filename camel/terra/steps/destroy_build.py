"""
This file defines the step that destroys the terraform build.
"""
from subprocess import Popen

from camel.terra.components.variable import Variable
from camel.terra.steps.base import Step


class DestroyBuild(Step):

    def __init__(self, config: dict, file_path: str) -> None:
        self.config: dict = config
        self.file_path: str = file_path

    def run(self) -> None:
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
