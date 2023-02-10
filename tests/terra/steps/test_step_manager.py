from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps import StepManager, Variable


class TestStepManager(TestCase):

    def setUp(self) -> None:
        self.terraform_data = {

        }
        self.config = {
            "ONE": "one",
            "TWO": 2,
            "location": "some_location"
        }
        self.step_data = {
            "name": "placeholder",
            "script_name": "some_script",
            "script_location": "some_dir_location",
            "variables": self.config,
            "statement": "some_statement",
            "command": "some command"
        }
        self.file_path = "some_path"
        self.test = StepManager(terraform_data={}, file_path=self.file_path, config=self.config)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(self.terraform_data, self.test.terraform_data)
        self.assertEqual(self.config, self.test.config)
        self.assertEqual(self.file_path, self.test.file_path)

    def test_translate_dictionary(self):
        outcome = self.test.translate_dictionary(config=self.config)

        self.assertEqual("one", outcome["ONE"].value)
        self.assertEqual(2, outcome["TWO"].value)
        self.assertEqual(Variable, type(outcome["ONE"]))
        self.assertEqual(Variable, type(outcome["TWO"]))

    @patch("camel.terra.steps.get_generic_model")
    @patch("camel.terra.steps.RunCommandOnServerStep")
    @patch("camel.terra.steps.DestroyBuild")
    @patch("camel.terra.steps.PrintoutStep")
    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test__get_step_run_script(self, mock_run_script_on_server, mock_print, mock_destroy, mock_run_command,
                       mock_get_generic_model):
        outcome = self.test._get_step(step_data=self.step_data)
        self.assertEqual(None, outcome)

        self.step_data["name"] = "run_script"
        outcome = self.test._get_step(step_data=self.step_data)
        self.assertEqual(mock_run_script_on_server.return_value, outcome)
        mock_run_script_on_server.assert_called_once_with(
            input_params=self.step_data,
            terraform_data=self.terraform_data,
            location="some_path/some_location"
        )

    @patch("camel.terra.steps.get_generic_model")
    @patch("camel.terra.steps.RunCommandOnServerStep")
    @patch("camel.terra.steps.DestroyBuild")
    @patch("camel.terra.steps.PrintoutStep")
    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test__get_step_run_local_script(self, mock_run_script_on_server, mock_print, mock_destroy, mock_run_command,
                       mock_get_generic_model):
        self.step_data["name"] = "run_local_script"
        outcome = self.test._get_step(step_data=self.step_data)
        self.assertEqual(mock_run_script_on_server.return_value, outcome)
        mock_run_script_on_server.assert_called_once_with(
            input_params=self.step_data,
            terraform_data=self.terraform_data,
            location="some_dir_location/"
        )

    @patch("camel.terra.steps.get_generic_model")
    @patch("camel.terra.steps.RunCommandOnServerStep")
    @patch("camel.terra.steps.DestroyBuild")
    @patch("camel.terra.steps.PrintoutStep")
    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test__get_step_print(self, mock_run_script_on_server, mock_print, mock_destroy, mock_run_command,
                          mock_get_generic_model):
          self.step_data["name"] = "print"
          self.step_data["variables"]["location"] = "some_location"
          outcome = self.test._get_step(step_data=self.step_data)
          self.assertEqual(mock_print.return_value, outcome)
          mock_print.assert_called_once_with(string="some_statement")

    @patch("camel.terra.steps.get_generic_model")
    @patch("camel.terra.steps.RunCommandOnServerStep")
    @patch("camel.terra.steps.DestroyBuild")
    @patch("camel.terra.steps.PrintoutStep")
    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test__get_step_run_server_command(self, mock_run_script_on_server, mock_print, mock_destroy, mock_run_command,
                            mock_get_generic_model):
            self.step_data["name"] = "run_server_command"
            outcome = self.test._get_step(step_data=self.step_data)
            self.assertEqual(mock_run_command.return_value, outcome)
            mock_run_command.assert_called_once_with(terraform_data=self.test.terraform_data,
                                                     command="some command",
                                                     environment_variables={})

    @patch("camel.terra.steps.get_generic_model")
    @patch("camel.terra.steps.RunCommandOnServerStep")
    @patch("camel.terra.steps.DestroyBuild")
    @patch("camel.terra.steps.PrintoutStep")
    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test__get_step_test_model(self, mock_run_script_on_server, mock_print, mock_destroy, mock_run_command,
                            mock_get_generic_model):
            self.step_data["name"] = "test_model"
            outcome = self.test._get_step(step_data=self.step_data)
            self.assertEqual(mock_get_generic_model.return_value, outcome)
            mock_get_generic_model.assert_called_once_with(model_type="test_model",
                                                           input_params=self.step_data,
                                                           terraform_data=self.terraform_data)

    @patch("camel.terra.steps.get_generic_model")
    @patch("camel.terra.steps.RunCommandOnServerStep")
    @patch("camel.terra.steps.DestroyBuild")
    @patch("camel.terra.steps.PrintoutStep")
    @patch("camel.terra.steps.RunScriptOnServerStep")
    def test__get_step_destroy_build(self, mock_run_script_on_server, mock_print, mock_destroy, mock_run_command,
                            mock_get_generic_model):
            self.step_data["name"] = "destroy_build"
            outcome = self.test._get_step(step_data=self.step_data)
            self.assertEqual(mock_destroy.return_value, outcome)
            mock_destroy.assert_called_once_with(config=self.config, file_path=self.file_path)

    @patch("camel.terra.steps.Variable")
    @patch("camel.terra.steps.ConditionalStep")
    @patch("camel.terra.steps.StepManager._get_step")
    def test_process_step(self, mock__get_step, mock_conditional_step, mock_variable):
        self.step_data["name"] = "conditional"
        self.step_data["operator"] = "=="
        self.step_data["variable"] = "some_variable"
        self.step_data["value"] = "some_value"
        self.step_data["step_data"] = self.config

        self.test.process_step(step_data=self.step_data)

        mock__get_step.assert_called_once_with(step_data=self.config)
        mock_conditional_step.assert_called_once_with(operator="==",
                                                      variable=mock_variable.return_value,
                                                      value="some_value",
                                                      step=mock__get_step.return_value)
        mock_variable.assert_called_once_with(name="some_variable")
        mock__get_step.return_value.run_assert_called_once_with()

        mock__get_step.reset_mock()

        self.step_data["name"] = "print"
        self.test.process_step(step_data=self.step_data)

        mock__get_step.assert_called_once_with(step_data=self.step_data)
        mock__get_step.return_value.run_assert_called_once_with()


if __name__ == "__main__":
    main()
