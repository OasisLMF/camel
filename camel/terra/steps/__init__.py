"""
This file defines the step manager for managing steps in a terraform run.
"""
from typing import Optional

from gerund.components.command_string import CommandString
from gerund.components.variable import Variable

from camel.terra.steps.base import Step
from camel.terra.steps.conditional import ConditionalStep
from camel.terra.steps.destroy_build import DestroyBuild
from camel.terra.steps.model_runs import get_generic_model
from camel.terra.steps.printout import PrintoutStep
from camel.terra.steps.run_command_on_server import RunCommandOnServerStep
from camel.terra.steps.run_script_on_server import RunScriptOnServerStep


class StepManager:
    """
    This class is responsible for managing the execution of steps.

    Attributes:
        terraform_data: (dict) data loaded from the output file from the terraform build
        file_path: (str) the path to where the terraform files are for the terraform build
        config: (dict) variables to be inserted into the terraform build
    """
    def __init__(self, terraform_data: dict, file_path: str, config: dict) -> None:
        """
        The constructor for the StepManager class.

        Args:
            terraform_data: (dict) data loaded from the output file from the terraform build
            file_path: (str) the path to where the terraform files are for the terraform build
            config: (dict) variables to be inserted into the terraform build
        """
        self.terraform_data: dict = terraform_data
        self.file_path: str = file_path
        self.config: dict = config

    @staticmethod
    def translate_dictionary(config: dict) -> dict:
        """
        Converts all values in a dictionary into Variable objects.

        Args:
            config: (dict) the dictionary to be processed

        Returns: (dict) the inputted dictionary that has all the values to be a Variable
        """
        for key in config.keys():
            config[key] = Variable(name=config[key])
        return config

    def _get_step(self, step_data: dict) -> Optional[Step]:
        """
        Gets the step and constructs it.

        Args:
            step_data: (dict) data needed to construct the step

        Returns: (Optional[Step]) the constructed step if it is supported
        """
        step_name = step_data["name"]
        step_process: Optional[Step] = None

        if step_name == "run_script":
            step_data["script_name"] = Variable(name=step_data["script_name"])
            step_data["variables"] = StepManager.translate_dictionary(config=step_data.get("variables", {}))
            step_process = RunScriptOnServerStep(input_params=step_data,
                                                 terraform_data=self.terraform_data,
                                                 location=f'{self.file_path}/{self.config["location"]}')
        elif step_name == "print":
            step_process = PrintoutStep(string=step_data["statement"])
        elif step_name == "destroy_build":
            step_process = DestroyBuild(config=self.config, file_path=self.file_path)
        elif step_name == "run_server_command":
            command_string = CommandString(command=step_data["command"])
            environment_variables: dict = step_data.get("env_vars", {})
            step_process = RunCommandOnServerStep(terraform_data=self.terraform_data,
                                                  command=str(command_string),
                                                  environment_variables=environment_variables)
        elif "test_model" in step_name:
            step_data["variables"] = StepManager.translate_dictionary(config=step_data.get("variables", {}))
            step_process = get_generic_model(model_type=step_name, input_params=step_data,
                                             terraform_data=self.terraform_data)
        return step_process

    def process_step(self, step_data: dict) -> None:
        """
        Processes a step based on the data by constructing it and then running it.

        Args:
            step_data: (dict) data needed to construct the step

        Returns: None
        """
        step_name = step_data["name"]

        if step_name == "conditional":

            inner_step_data = step_data["step_data"]
            inner_step = self._get_step(step_data=inner_step_data)
            step_process = ConditionalStep(operator=step_data["operator"],
                                           variable=Variable(name=step_data["variable"]),
                                           value=step_data["value"],
                                           step=inner_step)

        else:
            step_process = self._get_step(step_data=step_data)

        if step_process is not None:
            step_process.run()
