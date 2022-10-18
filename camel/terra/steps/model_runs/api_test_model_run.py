"""
This file defines the run API model test step which runs on the model server.
"""
import os

from camel.terra.steps.base import Step
from camel.terra.steps.run_script_on_server import RunScriptOnServerStep


class ApiTestModelRunStep(Step):
    """
    This class is responsible for running an API test for a model on the model server.

    Attributes:
        run_on_server_step (RunScriptOnServerStep): the step class that runs a python script on a model server.
    """
    EXPECTED_PARAMS = ["git_branch", "parent_dir", "test_dir", "expected_md5", "worker_name", "worker_dockerfile",
                       "docker_compose_platform", "docker_compose_worker", "docker_compose_ui"]

    def __init__(self, input_params: dict, terraform_data: dict) -> None:
        """
        The constructor for the ApiTestModelRunStep class.

        Args:
            input_params: (dict) the params that are going to be
            terraform_data:
        """
        terraform_data["script_name"] = "run_api_test_1"
        self._scan_input_params(input_params=input_params, expected_params=self.EXPECTED_PARAMS)
        self.run_on_server_step = RunScriptOnServerStep(
            input_params=input_params,
            terraform_data=terraform_data,
            location=str(os.path.dirname(__file__)) + "/server_scripts/"
        )

    def run(self) -> None:
        self.run_on_server_step.run()
