"""
This file tests the object that manages the data around a project.
"""
import json
import os
from unittest import main, TestCase

from camel.basecamp.components.project import Project, Status


class ProjectTest(TestCase):

    def setUp(self) -> None:
        self.file_path = "projects/"
        self.expected_data = {
            'NAME': 'test model',
            'STATUS': 'running',
            'CREATED_BY': 'four',
            'LAST_INTERACTED_BY': 'five',
        }
        self.test = Project(name="four", file_path=self.file_path)

    def tearDown(self) -> None:
        pass

    def test_read(self):
        self.assertEqual(self.expected_data, self.test.data)

    def test_write(self):
        self.test.name = "test"
        self.test.write()

        with open("projects/test.json", "r") as file:
            data = json.loads(file.read())

        self.assertEqual(self.test.data, data)
        os.remove("projects/test.json")

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

    def test_update_status(self):
        self.test.update_status(status=Status.DESTROYING)
        self.expected_data["STATUS"] = "destroying"
        self.assertEqual(self.expected_data, self.test.data)


if __name__ == "__main__":
    main()
