from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.run_command_on_server import RunCommandOnServerStep
from gerund.components.variable_map import VariableMap, Singleton


class TestRunCommandOnServerStep(TestCase):

    def setUp(self) -> None:
        self.variable_map = VariableMap()
        self.terraform_data = {
            "ONE": "1",
            "TWO": "two",
            "main_server_ip": {
                "value": ["123456"]
            }
        }
        self.environment_variables = {
            "THREE": "three",
            "FOUR": "4"
        }
        self.command = "python test.py"
        self.test = RunCommandOnServerStep(terraform_data=self.terraform_data,
                                           command=self.command,
                                           environment_variables=self.environment_variables)

    def tearDown(self) -> None:
        Singleton._instances = {}

    def test___init__(self):
        self.assertEqual("123456", self.test.server_ip)
        self.assertEqual(self.environment_variables, self.test.environment_variables)
        self.assertEqual(self.command, self.test.command)

    def test_run(self):
        self.test.run()


if __name__ == "__main__":
    main()
