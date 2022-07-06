import os
from unittest import main, TestCase
from unittest.mock import patch

import yaml

from camel.terra.steps import StepManager


META_PATH = file_path = str(os.path.realpath(__file__)).replace("test_step_manager.py", "meta_data/")


class TestStepManager(TestCase):

    def setUp(self) -> None:
        """
        Runs at the start of every test.

        Returns: None
        """
        with open(META_PATH + "test_config.yml", 'r') as stream:
            self.config = yaml.safe_load(stream)

        self.terraform_data = {

        }
        self.file_path = "some/file/path"
        self.test = StepManager(terraform_data=self.terraform_data, file_path=self.file_path, config=self.config)

    def tearDown(self) -> None:
        """
        Runs at the end of every test.

        Returns: None
        """
        pass

    def test___init__(self):
        self.assertEqual(self.config, self.test.config)
        self.assertEqual(self.terraform_data, self.test.terraform_data)
        self.assertEqual(self.file_path, self.test.file_path)

    def test_translate_dictionary(self):
        outcome = StepManager.translate_dictionary(config=self.config["variables"])

        self.assertEqual("=>aws_access_key", outcome["aws_access_key"].name)
        self.assertEqual("=>aws_secret_access_key", outcome["aws_secret_access_key"].name)
        self.assertEqual("some_subnet_id", outcome["subnet_id"].name)
        self.assertEqual("some_security_group_id", outcome["server_security_group"].name)

    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test__get_step(self, mock_run_script_on_server):
        step_process = self.test._get_step(step_data=self.config["steps"][0])
        self.assertEqual(mock_run_script_on_server.return_value, step_process)
        self.assertEqual(self.file_path + "/model_runs/BGEQ", mock_run_script_on_server.call_args_list[0][1]["location"])
        self.assertEqual("run_script", mock_run_script_on_server.call_args_list[0][1]["input_params"]["name"])

    @patch("camel.terra.steps.ConditionalStep.run")
    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test_process_step(self, mock_run_script_on_server, mock_conditional_step_run):
        self.test.process_step(step_data=self.config["steps"][0])
        mock_run_script_on_server.return_value.run.assert_called_once_with()

        # try and mock the ConditionalStep object and assert what the object is called with
        self.test.process_step(step_data=self.config["steps"][1])
        mock_conditional_step_run.assert_called_once_with()


if __name__ == "__main__":
    main()
