"""
This file tests the Variable displaying how the object can be used in code on the last test case.
"""
from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.components.variable import Variable


class Test(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        test = Variable(name=">>test")

        self.assertEqual(None, test.path)
        self.assertEqual(">>test", test.name)
        self.assertEqual(None, test.ip_address)

    @patch("camel.terra.components.variable.LocalProfileVariablesStorage")
    def test__extract_variable_from_local_storage(self, mock_local_storage):
        mock_local_storage.return_value = {}
        mock_local_storage.return_value["test"] = "something"

        test = Variable(name=">>test")

        outcome = test._extract_variable_from_local_storage()

        self.assertEqual("something", outcome)

        del mock_local_storage.return_value["test"]

        with self.assertRaises(ValueError) as error:
            test._extract_variable_from_local_storage()

        self.assertEqual("test not found in profile storage", str(error.exception))

    @patch("camel.terra.components.variable.open")
    @patch("camel.terra.components.variable.Popen")
    @patch("camel.terra.components.variable.VariableMap")
    def test__extract_value_from_config_vars(self, mock_variable_map, mock_popen, mock_open):
        mock_variable_map.return_value = {}
        mock_variable_map.return_value["test"] = {
            "path": "/path/to/something"
        }
        mock_open.return_value.__enter__.return_value.read.return_value = "something"

        test = Variable(name="=>test")

        outcome = test._extract_value_from_config_vars()

        self.assertEqual("something", outcome)
        mock_open.assert_called_once_with('/path/to/something/test.txt', 'r')

        mock_variable_map.return_value["test"] = {
            "path": "/path/to/something",
            "ip_address": "0.0.0.0:500"
        }
        mock_popen.return_value.communicate.return_value[0].decode.return_value.replace.return_value = "something"
        outcome = test._extract_value_from_config_vars()

        self.assertEqual("something", outcome)
        mock_popen.assert_called_once_with("ssh -A ubuntu@0.0.0.0:500 'cat /path/to/something/test.txt'",
                                           stdout=-1, shell=True)

    @patch("camel.terra.components.variable.Variable._extract_value_from_config_vars")
    @patch("camel.terra.components.variable.Variable._extract_variable_from_local_storage")
    def test_value(self, mock_local_storage, mock_config_vars):
        mock_local_storage.return_value = "local"
        mock_config_vars.return_value = "config"

        test = Variable(name="=>test")
        self.assertEqual("local", test.value)

        test = Variable(name=">>test")
        self.assertEqual("config", test.value)

        test = Variable(name="another test")
        self.assertEqual("another test", test.value)

    @patch("camel.terra.components.variable.Variable._extract_value_from_config_vars")
    @patch("camel.terra.components.variable.Variable._extract_variable_from_local_storage")
    def test___str__(self, mock_local_storage, mock_config_vars):
        mock_local_storage.return_value = "local"
        mock_config_vars.return_value = "config"

        self.assertEqual("the value is: local", f"the value is: {Variable(name='=>test')}")
        self.assertEqual("the value is: config", f"the value is: {Variable(name='>>test')}")
        self.assertEqual("the value is: another test", f"the value is: {Variable(name='another test')}")


if __name__ == "__main__":
    main()
