"""
This file tests the object that manages the data around a project
"""
import json
import os
from unittest import main, TestCase
from unittest.mock import patch
import pathlib

from camel.basecamp.components.user import User


class UserTest(TestCase):

    def setUp(self) -> None:
        self.file_path = str(pathlib.Path(__file__).resolve().parent) + "/users/"
        self.expected_data = {
            'NAME': 'test name',
        }
        self.test = User(name="two", file_path=self.file_path)

    def tearDown(self) -> None:
        pass

    def test_read(self):
        self.assertEqual(self.expected_data, self.test.data)

    def test_write(self):
        self.test.name = "test"
        self.test.write()

        with open(f"{self.file_path}/test.json", "r") as file:
            data = json.loads(file.read())

        self.assertEqual(self.test.data, data)
        os.remove(f"{self.file_path}/test.json")

    def test_schema(self):
        self.assertEqual(self.expected_data, self.test.schema)

    def test_schema_from_empty_folder(self):
        test = User(name="one", file_path=self.file_path)
        expected_empty_schema = {
            'NAME': 'undefined'
        }
        self.assertEqual(expected_empty_schema, test.schema)

    @patch("camel.basecamp.components.user.Popen")
    def test_get_cached_username(self, mock_p_open):
        mock_p_open.return_value.communicate.return_value = [b"one two three\nfour five@test six"]
        outcome = User.get_cached_username()

        self.assertEqual("five@test", outcome)


if __name__ == "__main__":
    main()
