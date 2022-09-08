from unittest import TestCase, main
from unittest.mock import patch

from camel.terra.components.command_string import CommandString


class TestCommandString(TestCase):

    def setUp(self) -> None:
        self.command = 'cd {>>DIRECTORY} && echo "{=>OUTCOME}"'
        self.test = CommandString(command=self.command)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(self.command, self.test.command)
        self.assertEqual(False, self.test.command_processed)

    def test__extract_variables(self):
        outcome = self.test._extract_variables()
        self.assertEqual(['>>DIRECTORY', '=>OUTCOME'], outcome)

        self.test.command = "cd one && echo 'two'"
        self.assertEqual([], self.test._extract_variables())

    @patch("camel.terra.components.command_string.Variable")
    def test__replace_with_variable(self, mock_variable):
        mock_variable.return_value = "test_server_outcome"
        self.test._replace_with_variable(variable_string='=>OUTCOME')

        self.assertEqual('cd {>>DIRECTORY} && echo "test_server_outcome"', self.test.command)
        mock_variable.assert_called_once_with(name='=>OUTCOME')

    @patch("camel.terra.components.command_string.Variable", side_effect=["one", "two"])
    def test__process_command(self, mock_variable):
        self.test.process_command()
        self.assertEqual('cd one && echo "two"', self.test.command)

        self.assertEqual({'name': '>>DIRECTORY'}, mock_variable.call_args_list[0][1])
        self.assertEqual({'name': '=>OUTCOME'}, mock_variable.call_args_list[1][1])

    @patch("camel.terra.components.command_string.Variable", side_effect=["one", "two"])
    def test_str(self, _):
        self.assertEqual('cd one && echo "two"', str(self.test))

        self.test.command = "cd two && echo 'one'"
        self.test.command_processed = False
        self.assertEqual("cd two && echo 'one'", str(self.test))


if __name__ == "__main__":
    main()
