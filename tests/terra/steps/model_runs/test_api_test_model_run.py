from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.model_runs.api_test_model_run import ApiTestModelRunStep


class TestApiTestModelRunStep(TestCase):

    @patch("camel.terra.steps.model_runs.api_test_model_run.ApiTestModelRunStep._scan_input_params")
    @patch("camel.terra.steps.model_runs.api_test_model_run.os.path.dirname")
    @patch("camel.terra.steps.model_runs.api_test_model_run.RunScriptOnServerStep")
    def setUp(self, mock_script_run_step, mock_dirname, mock__scan_input_params) -> None:
        mock_dirname.return_value = "test_dir"
        self.test = ApiTestModelRunStep(input_params={"variables": {}}, terraform_data={})
        self.mock_script_run_step = mock_script_run_step

    def tearDown(self) -> None:
        pass

    @patch("camel.terra.steps.model_runs.api_test_model_run.ApiTestModelRunStep._scan_input_params")
    @patch("camel.terra.steps.model_runs.api_test_model_run.os.path.dirname")
    @patch("camel.terra.steps.model_runs.api_test_model_run.RunScriptOnServerStep")
    def test___init__(self, mock_script_run_step, mock_dirname, mock__scan_input_params):
        mock_dirname.return_value = "test_dir"
        test = ApiTestModelRunStep(input_params={"variables": {}}, terraform_data={})
        mock_script_run_step.assert_called_once_with(input_params={"variables": {}, "script_name": "run_api_test_1"},
                                                     terraform_data={},
                                                     location="test_dir/server_scripts/")
        mock__scan_input_params.assert_called_once_with(input_params={}, expected_params=self.test.EXPECTED_PARAMS)
        self.assertEqual(mock_script_run_step.return_value, test.run_on_server_step)

    def test__scan_input_params(self):
        input_params = {
            "git_branch": "one",
            "parent_dir": "two",
            "expected_md5": "three"
        }

        with self.assertRaises(ValueError) as error:
            self.test._scan_input_params(input_params=input_params, expected_params=self.test.EXPECTED_PARAMS)
        expected_error = "the following keys are not found: ['test_dir', 'worker_name', 'worker_dockerfile', " \
                         "'docker_compose_platform', 'docker_compose_worker', 'docker_compose_ui']"
        self.assertEqual(str(error.exception), expected_error)

        input_params["test_dir"] = "four"
        input_params["worker_name"] = "five"
        input_params["worker_dockerfile"] = "six"
        input_params["docker_compose_platform"] = "seven"
        input_params["docker_compose_worker"] = "eight"
        input_params["docker_compose_ui"] = "nine"
        self.test._scan_input_params(input_params=input_params, expected_params=self.test.EXPECTED_PARAMS)

    def test_run(self):
        self.test.run()
        self.mock_script_run_step.return_value.run.assert_called_once_with()


if __name__ == "__main__":
    main()
