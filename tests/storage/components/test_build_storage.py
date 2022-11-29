from unittest import main, TestCase
from unittest.mock import patch, MagicMock

from camel.storage.components.build_storage import BuildStorage
import json


class TestBuildStorage(TestCase):

    def setUp(self) -> None:
        self.test = BuildStorage()
        self.file_path = "./data.json"

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        test = BuildStorage()
        self.assertEqual(None, test.s3_path)
        self.assertEqual(None, test._data)

        test = BuildStorage(s3_path="some/path")
        self.assertEqual("some/path", test.s3_path)
        self.assertEqual(None, test._data)

    def test__read_local(self):
        print(json.dumps({}))

    def test__write_local(self):
        self.test._write_local()

    @patch("camel.storage.components.build_storage.dirname")
    def test_file_path(self, mock_dirname) -> None:
        mock_dirname.return_value = "camel/storage/components"
        self.assertEqual("camel/storage/components/builds.json", self.test.file_path)


if __name__ == "__main__":
    main()
