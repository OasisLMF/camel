from unittest import main, TestCase
from unittest.mock import patch

from gerund.components.variable_map import VariableMap, Singleton

from camel.terra.steps.run_command_on_server import RunCommandOnServerStep


class TestRunCommandOnServerStep(TestCase):

    def setUp(self) -> None:
        self.variable_map = VariableMap()
        self.terraform_data = {
            "ONE": "1",
            "TWO": "two"
        }
        self.terra_data = {
            "main_server_ip": {
                "value": ["123456"]
            }
        }
        self.environment_variables = {
            "THREE": "three",
            "FOUR": "4"
        }
        self.command = "python test.py"
        self.test = RunCommandOnServerStep(terraform_data=self.terra_data,
                                           command=self.command,
                                           environment_variables=self.environment_variables)

    def tearDown(self) -> None:
        Singleton._instances = {}

    def test___init__(self):
        self.assertEqual("123456", self.test.server_ip)
        self.assertEqual(self.environment_variables, self.test.environment_variables)
        self.assertEqual(self.command, self.test.command)

    @patch("camel.terra.steps.run_command_on_server.TerminalCommand")
    def test_run(self, mock_terminal_command):
        self.test.run()
        mock_terminal_command.assert_called_once_with(command='cd /home/ubuntu/ && python test.py',
                                                      environment_variables=self.environment_variables,
                                                      ip_address="123456")


if __name__ == "__main__":
    main()
