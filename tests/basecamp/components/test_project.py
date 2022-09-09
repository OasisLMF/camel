"""
This file tests the object that manages the data around a project.
"""
import json
import os
from unittest import main, TestCase
from unittest.mock import patch
import pathlib

from camel.basecamp.components.project import Project, Status


class ProjectTest(TestCase):

    def setUp(self) -> None:
        self.file_path: str = str(pathlib.Path(__file__).resolve().parent) + "/projects"
        self.name = "four"
        self.expected_data = {
            'NAME': 'test model',
            'STATUS': 'running',
            'CREATED_BY': 'four',
            'LAST_INTERACTED_BY': 'five',
        }
        self.test = Project(name=self.name, file_path=self.file_path)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(self.name, self.test.name)
        self.assertEqual(self.file_path, self.test.file_path)
        self.assertEqual(self.expected_data, self.test.data)

    def test_write(self):
        self.test.name = "test"
        self.test.write()

        with open(f"{self.file_path}/test.json", "r") as file:
            data = json.loads(file.read())

        self.assertEqual(self.test.data, data)
        os.remove(f"{self.file_path}/test.json")

    def test_update_status(self):
        self.test.update_status(status=Status.DESTROYING)
        self.expected_data["STATUS"] = "destroying"
        self.assertEqual(self.expected_data, self.test.data)

    @patch("camel.basecamp.components.project.datetime")
    def test_update_last_interacted_by(self, mock_now):
        mock_now.now.return_value = "NOW"
        expected_outcome = {
            'NAME': 'test model',
            'STATUS': 'running',
            'CREATED_BY': 'four',
            'LAST_INTERACTED_BY': 'maxwellflitton',
            'LAST_INTERACTED': 'NOW'
        }
        self.test.update_last_interacted_by(user_name="maxwellflitton")
        self.assertEqual(expected_outcome, self.test.data)

    def test_schema(self):
        self.expected_data["LAST_INTERACTED"] = "undefined"
        self.assertEqual(self.expected_data, self.test.schema)

    def test_schema_from_empty_folder(self):
        test = Project(name="five", file_path=self.file_path)
        expected_empty_schema = {
            'NAME': 'undefined',
            'STATUS': 'undefined',
            'CREATED_BY': 'undefined',
            'LAST_INTERACTED_BY': 'undefined',
            'LAST_INTERACTED': 'undefined'
        }
        self.assertEqual(expected_empty_schema, test.schema)

    def test_last_interacted_by(self):
        self.test.data["LAST_INTERACTED_BY"] = "test"
        self.assertEqual("test", self.test.last_interacted_by)

    def test_read(self):
        self.assertEqual(self.expected_data, self.test.data)


if __name__ == "__main__":
    main()
