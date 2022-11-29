import json
import os
from unittest import main, TestCase
from unittest.mock import patch

from camel.storage.components.build_storage import BuildStorage, Status


class TestBuildStorage(TestCase):

    def setUp(self) -> None:
        self.test = BuildStorage()
        self.file_path = "./data.json"
        self.data = {
            "some/path": {
                "ip_address": "some_ip",
                "build_name": "some_name",
                "status": Status.RUNNING.value
            }
        }

    def tearDown(self) -> None:
        if os.path.exists(self.test.file_path):
            os.remove(self.test.file_path)

    def test___init__(self) -> None:
        test = BuildStorage()
        self.assertEqual(None, test.s3_path)
        self.assertEqual(None, test._data)

        test = BuildStorage(s3_path="some/path")
        self.assertEqual("some/path", test.s3_path)
        self.assertEqual(None, test._data)

    def test__read_local(self):
        self.assertEqual({}, self.test._read_local())
        with open(self.test.file_path, "w") as file:
            json.dump(self.data, file)
        self.assertEqual(self.data, self.test._read_local())

    def test__write_local(self):
        self.test._write_local()
        self.assertEqual(True, os.path.exists(self.test.file_path))

    @patch("camel.storage.components.build_storage.dirname")
    def test_file_path(self, mock_dirname) -> None:
        mock_dirname.return_value = "camel/storage/components"
        self.assertEqual("camel/storage/components/builds.json", self.test.file_path)

    def test__read_s3(self):
        with self.assertRaises(NotImplementedError):
            self.test._read_s3()

    def test__write_s3(self):
        with self.assertRaises(NotImplementedError):
            self.test._write_s3()

    @patch("camel.storage.components.build_storage.BuildStorage._write_local")
    @patch("camel.storage.components.build_storage.BuildStorage._write_s3")
    def test_write(self, mock_write_s3, mock_write_local) -> None:
        self.test.write()
        mock_write_local.assert_called_once()

        self.test.s3_path = "some/path"
        self.test.write()
        mock_write_s3.assert_called_once()

    def test_get_build(self):
        self.test._data = {"some/path": {
                "state_path": "some/path",
                "ip_address": "some_ip",
                "build_name": "some_name",
                "status": Status.RUNNING.value
            }
        }
        build = self.test.get_build("some/path")
        self.assertEqual("some/path", build.state_path)
        self.assertEqual("some_ip", build.ip_address)
        self.assertEqual("some_name", build.build_name)
        self.assertEqual(Status.RUNNING, build.status)

        with self.assertRaises(FileNotFoundError):
            self.test.get_build("some/other/path")

    @patch("camel.storage.components.build_record.datetime")
    def test_insert_build(self, mock_datetime):
        mock_datetime.now.return_value.strftime.return_value = "some_time"
        self.test.insert_build(state_path="some/path", ip_address="some_ip",
                               build_name="some_name", status=Status.RUNNING)

        self.assertEqual({'some/path': {
                                  'state_path': 'some/path',
                                  'ip_address': 'some_ip',
                                  'build_name': 'some_name',
                                  'status': 'running',
                                  'time_stamp': 'some_time'
                              }
        }, self.test.data)

    @patch("camel.storage.components.build_storage.dirname")
    def test_file_path(self, mock_dirname):
        mock_dirname.return_value = "camel/storage/components"
        self.assertEqual("camel/storage/components/builds.json", self.test.file_path)

        self.test.s3_path = "some/path/builds.json"
        self.assertEqual("some/path/builds.json", self.test.file_path)


if __name__ == "__main__":
    main()
