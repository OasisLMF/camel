from unittest import main, TestCase
from unittest.mock import patch, MagicMock

from camel.storage.components.build_record import BuildRecord, Status


class TestBuildRecord(TestCase):

    def setUp(self) -> None:
        self.test = BuildRecord(state_path="some/path", ip_address="some_ip",
                                build_name="some_name", status=Status.RUNNING)

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        self.assertEqual("some/path", self.test.state_path)
        self.assertEqual("some_ip", self.test.ip_address)
        self.assertEqual("some_name", self.test.build_name)
        self.assertEqual(Status.RUNNING, self.test.status)

    @patch("camel.storage.components.build_record.datetime")
    def test_to_dict(self, mock_datetime) -> None:
        datetime_mock = MagicMock()
        mock_datetime.now.return_value = datetime_mock
        self.assertEqual({
            "state_path": "some/path",
            "ip_address": "some_ip",
            "build_name": "some_name",
            "time_stamp": str(datetime_mock.strftime.return_value),
            "status": Status.RUNNING.value,
        }, self.test.to_dict())

    def test_from_dict(self) -> None:
        test = BuildRecord.from_dict({
            "state_path": "some/path",
            "ip_address": "some_ip",
            "build_name": "some_name",
            "status": Status.RUNNING.value,
            "time_stamp": "some_time_stamp"
        })
        self.assertEqual("some/path", test.state_path)
        self.assertEqual("some_ip", test.ip_address)
        self.assertEqual("some_name", test.build_name)
        self.assertEqual("some_time_stamp", test.time_stamp)
        self.assertEqual(Status.RUNNING, test.status)


if __name__ == "__main__":
    main()
