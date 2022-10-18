from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.model_runs.mdk_test_model_run import MdkTestModelRunStep


class TestMdkTestModelRunStep(TestCase):

    @patch("camel.terra.steps.model_runs.mdk_test_model_run.MdkTestModelRunStep._scan_input_params")
    @patch("camel.terra.steps.model_runs.mdk_test_model_run.os.path.dirname")
    @patch("camel.terra.steps.model_runs.mdk_test_model_run.RunScriptOnServerStep")
    def setUp(self, mock_script_run_step, mock_dirname, mock__scan_input_params) -> None:
        mock_dirname.return_value = "test_dir"
        self.test = MdkTestModelRunStep(input_params={}, terraform_data={})
        self.mock_script_run_step = mock_script_run_step

    def tearDown(self) -> None:
        pass

    @patch("camel.terra.steps.model_runs.mdk_test_model_run.MdkTestModelRunStep._scan_input_params")
    @patch("camel.terra.steps.model_runs.mdk_test_model_run.os.path.dirname")
    @patch("camel.terra.steps.model_runs.mdk_test_model_run.RunScriptOnServerStep")
    def test___init__(self, mock_script_run_step, mock_dirname, mock__scan_input_params):
        mock_dirname.return_value = "test_dir"
        test = MdkTestModelRunStep(input_params={}, terraform_data={})
        mock_script_run_step.assert_called_once_with(input_params={},
                                                     terraform_data={"script_name": "run_mdk_test_1"},
                                                     location="test_dir/server_scripts/")
        mock__scan_input_params.assert_called_once_with(input_params={})
        self.assertEqual(mock_script_run_step.return_value, test.run_on_server_step)

    def test__scan_input_params(self):
        input_params = {
            "git_branch": "one",
            "parent_dir": "two",
            "expected_md5": "three"
        }

        with self.assertRaises(ValueError) as error:
            self.test._scan_input_params(input_params=input_params)
        self.assertEqual(str(error.exception), "the following keys are not found: ['test_dir', 'run_dir']")

        input_params["test_dir"] = "four"
        input_params["run_dir"] = "five"
        self.test._scan_input_params(input_params=input_params)

    def test_run(self):
        self.test.run()
        self.mock_script_run_step.return_value.run.assert_called_once_with()


if __name__ == "__main__":
    main()
