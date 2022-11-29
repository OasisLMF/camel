from unittest import main, TestCase
from unittest.mock import patch, MagicMock

from camel.storage.adapters.builds_access import BuildsAccessAdapter
from camel.storage.components.build_record import BuildRecord
from camel.storage.components.build_storage import BuildStorage, Status


class TestBuildsAccessAdapter(TestCase):

    def setUp(self) -> None:
        self.test = BuildsAccessAdapter()
        self.file_path = "./data.json"
        self.data = {
            "some/path": {
                "state_path": "some/path",
                "ip_address": "some_ip",
                "build_name": "some_name",
                "status": Status.RUNNING.value,
                "time_stamp": MagicMock()
            },
            "some/path2": {
                "state_path": "some/path2",
                "ip_address": "some_ip_2",
                "build_name": "some_name_2",
                "status": Status.DESTROYED.value,
                "time_stamp": MagicMock()
            },
            "some/path3": {
                "state_path": "some/path3",
                "ip_address": "some_ip_3",
                "build_name": "some_name_3",
                "status": Status.SUCCESS.value,
                "time_stamp": MagicMock()
            }
        }
        self.structured_data = [
            BuildRecord(
                state_path="some/path",
                ip_address="some_ip",
                build_name="some_name",
                status=Status.RUNNING
            ),
            BuildRecord(
                state_path="some/path2",
                ip_address="some_ip_2",
                build_name="some_name_2",
                status=Status.DESTROYED
            ),
            BuildRecord(
                state_path="some/path3",
                ip_address="some_ip_3",
                build_name="some_name_3",
                status=Status.SUCCESS
            )
        ]

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        self.assertEqual(type(BuildStorage()), type(self.test.storage))

    @patch("camel.storage.adapters.builds_access.BuildStorage.get_build")
    def test_get_build(self, mock_get_build) -> None:
        self.assertEqual(mock_get_build.return_value, self.test.get_build(state_path="some/path"))
        mock_get_build.assert_called_once_with(state_path="some/path")

    def test_get_builds(self):
        mock_storage = MagicMock()
        mock_storage.data = self.data
        self.test.storage = mock_storage
        test_data = self.test.get_builds()

        for i in range(0, len(test_data)):
            self.assertEqual(self.structured_data[i].state_path, test_data[i].state_path)
            self.assertEqual(self.structured_data[i].ip_address, test_data[i].ip_address)
            self.assertEqual(self.structured_data[i].build_name, test_data[i].build_name)
            self.assertEqual(self.structured_data[i].status, test_data[i].status)

    @patch("camel.storage.adapters.builds_access.BuildStorage.write")
    def test_add_new_build(self, mock_write):
        self.test.storage._data = self.data
        self.test.add_new_build(
            state_path="some/path4",
            ip_address="some_ip_4",
            build_name="some_name_4"
        )
        self.assertEqual(4, len(self.test.storage.data))
        self.assertEqual("some/path4", self.test.storage.data["some/path4"]["state_path"])
        self.assertEqual("some_ip_4", self.test.storage.data["some/path4"]["ip_address"])
        self.assertEqual("some_name_4", self.test.storage.data["some/path4"]["build_name"])
        self.assertEqual(Status.RUNNING.value, self.test.storage.data["some/path4"]["status"])
        mock_write.assert_called_once_with()

    @patch("camel.storage.adapters.builds_access.BuildStorage.write")
    def test_update_build(self, mock_write):
        self.test.storage._data = self.data

        with self.assertRaises(FileNotFoundError) as context:
            self.test.update_build(
                state_path="some/path4",
                status=Status.SUCCESS
            )
        self.assertTrue("state some/path4 is not stored in the builds" in str(context.exception))

        self.test.update_build(
            state_path="some/path",
            status=Status.SUCCESS
        )
        self.assertEqual(Status.SUCCESS.value, self.test.storage.data["some/path"]["status"])
        mock_write.assert_called_once_with()


if __name__ == "__main__":
    main()
