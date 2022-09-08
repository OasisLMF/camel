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

    # @patch("camel.basecamp.components.mapper.open")
    @patch("camel.basecamp.components.mapper.Mapper.in_camp", new_callable=PropertyMock)
    # @patch("camel.basecamp.components.mapper.os.mkdir")
    def test_create(self, mock_mkdir, mock_in_camp):
        self.test.current_path = self.current_path + "test_camp/"
        mock_in_camp.return_value = True
        self.assertEqual(False, self.test.create(name="test_camp"))
        

    @patch("camel.basecamp.components.mapper.Mapper.in_camp", new_callable=PropertyMock)
    def test_available_projects(self, mock_in_camp):
        mock_in_camp.return_value = True

        self.assertEqual(["five", "four", "six"], self.test.available_projects)

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
        self.assertEqual(["seven", "eight"], self.test.available_configs)

    def test_in_camp(self):
        self.assertEqual(True, self.test.in_camp)


if __name__ == "__main__":
    main()
