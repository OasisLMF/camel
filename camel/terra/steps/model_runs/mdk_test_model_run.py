"""
This file defines the run MDK model test step which runs on the model server.
"""
import os

from camel.terra.steps.base import Step
from camel.terra.steps.run_script_on_server import RunScriptOnServerStep


class MdkTestModelRunStep(Step):
    """
    This class is responsible for running an MDK test for a model on the model server.

    Attributes:
        run_on_server_step (RunScriptOnServerStep): the step class that runs a python script on a model server.
    """
    EXPECTED_PARAMS = ["git_branch", "parent_dir", "test_dir", "run_dir", "expected_md5"]

    def __init__(self, input_params: dict, terraform_data: dict) -> None:
        """
        The constructor for the MdkTestModelRunStep class.

        Args:
            input_params: (dict) the params that are going to be
            terraform_data:
        """
        input_params["script_name"] = "run_mdk_test_1"
        self._scan_input_params(input_params=input_params["variables"], expected_params=self.EXPECTED_PARAMS)
        self.run_on_server_step = RunScriptOnServerStep(
            input_params=input_params,
            terraform_data=terraform_data,
            location=str(os.path.dirname(__file__)) + "/server_scripts/",
        )

    def run(self) -> None:
        self.run_on_server_step.run()
