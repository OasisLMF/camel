"""
This file defines the run MDK model test step which runs on the model server.
"""
import os

from camel.terra.steps.base import Step
from camel.terra.steps.run_script_on_server import RunScriptOnServerStep


class MdkTestModelRunStep(Step):
    """
    This class is responsible for running a MDK test for a model on the model server.

    Attributes:
        run_on_server_step (RunScriptOnServerStep): the step class that runs a python script on a model server.
    """
    def __init__(self, input_params: dict, terraform_data: dict) -> None:
        """
        The constructor for the MdkTestModelRunStep class.

        Args:
            input_params: (dict) the params that are going to be
            terraform_data:
        """
        terraform_data["script_name"] = "run_mdk_test_1"
        self._scan_input_params(input_params=input_params)
        self.run_on_server_step = RunScriptOnServerStep(
            input_params=input_params,
            terraform_data=terraform_data,
            location=str(os.path.dirname(__file__)) + "/server_scripts/"
        )

    @staticmethod
    def _scan_input_params(input_params: dict) -> None:
        """
        Scans the input parameters needed to run the MDK model test script.

        Args:
            input_params: (dict) the parameters that are going to be scanned

        Returns: None
        """
        expected_params = ["git_branch", "parent_dir", "test_dir", "run_dir", "expected_md5"]
        buffer = []

        for param in expected_params:
            if input_params.get(param) is None:
                buffer.append(param)

        if len(buffer) > 0:
            raise ValueError(f"the following keys are not found: {buffer}")

    def run(self) -> None:
        self.run_on_server_step.run()
