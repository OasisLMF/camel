"""
This file tests the mapping of data in the base camp.
"""
from unittest import main, TestCase
from unittest.mock import patch, MagicMock, PropertyMock

from camel.basecamp.components.mapper import Mapper


class MapperTest(TestCase):

    def setUp(self) -> None:
        self.test = Mapper()

    def tearDown(self) -> None:
        pass

    @patch("camel.basecamp.components.mapper.Mapper.in_camp", new_callable=PropertyMock)
    @patch("camel.basecamp.components.mapper.os.getcwd")
    def test_available_projects(self, mock_getcwd, mock_in_camp):
        mock_getcwd.return_value = "."
        mock_in_camp.return_value = True

        self.assertEqual(["two", "three", "one"], self.test.available_projects)

        mock_in_camp.return_value = False
        self.assertEqual([], self.test.available_projects)

    @patch("camel.basecamp.components.mapper.Mapper.in_camp", new_callable=PropertyMock)
    @patch("camel.basecamp.components.mapper.os.getcwd")
    def test_available_users(self, mock_getcwd, mock_in_camp):
        mock_getcwd.return_value = "."
        mock_in_camp.return_value = True

        self.assertEqual(["five", "four", "six"], self.test.available_users)

        mock_in_camp.return_value = False
        self.assertEqual([], self.test.available_users)

    def test_camp_name(self):
        self.assertEqual("test_name", self.test.camp_name)


if __name__ == "__main__":
    main()
