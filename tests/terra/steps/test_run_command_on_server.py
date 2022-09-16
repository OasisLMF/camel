from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.run_command_on_server import RunCommandOnServerStep
from gerund.components.variable_map import VariableMap, Singleton


class TestRunCommandOnServerStep(TestCase):

    def setUp(self) -> None:
        self.variable_map = VariableMap()
        self.terra_data = {
            "main_server_ip": {
                "value": ["123456"]
            }
        }
        self.env_var = {
            "ONE": "one",
            "TWO": "2",
            "THREE": "THREE"
        }
        self.command = "echo $ONE"
        self.test = RunCommandOnServerStep(terraform_data=self.terra_data,
                                           command=self.command,
                                           environment_variables=self.env_var)


    def tearDown(self) -> None:
        Singleton._instances = {}

    def test___init__(self):
        self.assertEqual("123456", self.test.server_ip)
        self.assertEqual(self.env_var, self.test.environment_variables)
        self.assertEqual(self.command, self.test.command)

    @patch("camel.terra.steps.run_command_on_server.Popen")
    @patch("camel.terra.steps.run_command_on_server.VariableMap")
    def test_run(self, mock_variable, mock_p_open):
        mock_variable.return_value.ip_address = "123456"
        self.test.run()
        print(mock_p_open.call_args_list[0][1])
        print(mock_p_open.call_args_list[0][0])


if __name__ == "__main__":
    main()
