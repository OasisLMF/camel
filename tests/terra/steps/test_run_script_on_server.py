from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.run_script_on_server import RunScriptOnServerStep


class TestRunScriptOnServerStep(TestCase):

    @patch("camel.terra.steps.run_script_on_server.RunScriptOnServerStep._process_inputs")
    def setUp(self, mock__process_inputs) -> None:
        self.input_params = {
            "script_name": "test_script",
            "env_vars": {
                "ONE": "1",
                "TWO": "two",
                "THREE": "three"
            },
            "variables": {
                "git_branch": "master",
                "parent_dir": "/home/ubuntu/",
                "test_dir": "test_dir",
                "expected_md5": "123456",
                "worker_name": "worker",
                "worker_dockerfile": "worker_dockerfile",
                "docker_compose_platform": "docker_compose_platform",
                "docker_compose_worker": "docker_compose_worker",
                "docker_compose_ui": "docker_compose_ui"
            }
        }
        self.terraform_data = {
            "ONE": "1",
            "TWO": "two",
            "main_server_ip": {"value": ["123456"]}
        }
        self.location = "/home/ubuntu/"
        self.test = RunScriptOnServerStep(input_params=self.input_params,
                                          terraform_data=self.terraform_data,
                                          location=self.location)

    def tearDown(self) -> None:
        pass

    @patch("camel.terra.steps.run_script_on_server.RunScriptOnServerStep._process_inputs")
    def test___init__(self, mock__process_inputs):
        test = RunScriptOnServerStep(input_params=self.input_params,
                                     terraform_data=self.terraform_data,
                                     location=self.location)
        self.assertEqual(None, test.server_ip)
        self.assertEqual(None, test.script_name)
        self.assertEqual(self.location, test.location)
        self.assertEqual(None, test.parameters)
        self.assertEqual(None, test.environment_variables)

        mock__process_inputs.assert_called_once_with(input_data=self.input_params, terraform_dict=self.terraform_data)

    def test__process_inputs(self):
        self.test._process_inputs(input_data=self.input_params, terraform_dict=self.terraform_data)
        self.assertEqual("123456", self.test.server_ip)
        self.assertEqual("test_script", self.test.script_name)
        self.assertEqual(self.location, self.test.location)
        self.assertEqual(self.input_params["variables"], self.test.parameters)
        self.assertEqual(self.input_params["env_vars"], self.test.environment_variables)


if __name__ == "__main__":
    main()
