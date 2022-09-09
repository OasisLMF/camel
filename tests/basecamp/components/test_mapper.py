"""
This file tests the mapping of data in the base camp.
"""
import os.path
import pathlib
from unittest import main, TestCase
from unittest.mock import patch, PropertyMock
from subprocess import Popen

from camel.basecamp.components.mapper import Mapper


class MapperTest(TestCase):

    @patch("camel.basecamp.components.mapper.os.getcwd")
    def setUp(self, mock_getcwd) -> None:
        self.current_path: str = str(pathlib.Path(__file__).resolve().parent) + "/"
        mock_getcwd.return_value = self.current_path
        self.test = Mapper()

    def tearDown(self) -> None:
        pass

    def test__create_venv(self):
        # Warning the following test requires internet connection
        venv_path = self.current_path + f"/venv"
        self.test._create_venv()
        self.assertEqual(True, os.path.exists(venv_path))
        delete_process = Popen(f"cd {self.current_path} && rm -rf venv", shell=True)
        delete_process.wait()

    @patch("camel.basecamp.components.mapper.json")
    @patch("camel.basecamp.components.mapper.open")
    @patch("camel.basecamp.components.mapper.Mapper.in_camp", new_callable=PropertyMock)
    @patch("camel.basecamp.components.mapper.os.mkdir")
    def test_create(self, mock_mkdir, mock_in_camp, mock_open, mock_json):
        self.test.current_path = self.current_path + "test_camp/"
        mock_in_camp.return_value = True
        self.assertEqual(False, self.test.create(name="test_camp"))

        mock_in_camp.return_value = False
        self.assertEqual(True, self.test.create(name="test_camp"))
        self.assertEqual(4, len(mock_mkdir.call_args_list))
        mock_json.dump.assert_called_once_with({"NAME": "test_camp"}, mock_open.return_value.__enter__.return_value)

    def test_paths(self):
        self.assertEqual(self.current_path + "/projects/", self.test.projects_path)
        self.assertEqual(self.current_path + "/configs/", self.test.configs_path)
        self.assertEqual(self.current_path + "/users/", self.test.users_path)
        self.assertEqual(self.current_path + "/data/", self.test.data_path)
        self.assertEqual(self.current_path + "/api.py", self.test.api_path)
        self.assertEqual(self.current_path + "/camp_charter.json", self.test.camp_charter_path)

    @patch("camel.basecamp.components.mapper.Mapper.in_camp", new_callable=PropertyMock)
    def test_available_projects(self, mock_in_camp):
        mock_in_camp.return_value = True
        outcome = self.test.available_projects
        outcome.sort()
        self.assertEqual(["five", "four", "six"], outcome)

        mock_in_camp.return_value = False
        self.assertEqual([], self.test.available_projects)

    @patch("camel.basecamp.components.mapper.Mapper.in_camp", new_callable=PropertyMock)
    def test_available_users(self, mock_in_camp):
        mock_in_camp.return_value = True

        self.assertEqual(["one", "two"], self.test.available_users)

        mock_in_camp.return_value = False
        self.assertEqual([], self.test.available_users)

    def test_camp_name(self):
        self.assertEqual("test_camp", self.test.camp_name)

    def test_available_configs(self):
        outcome = self.test.available_configs
        outcome.sort()
        self.assertEqual(['eight', 'seven'], outcome)

    def test_in_camp(self):
        self.assertEqual(True, self.test.in_camp)


if __name__ == "__main__":
    main()
