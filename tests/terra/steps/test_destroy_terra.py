"""
This file tests the step that destroys the terraform build.
"""
from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.steps.destroy_build import DestroyBuild


class DestroyBuildTest(TestCase):

    def setUp(self) -> None:
        self.config = {
            "variables": {
                "one": "1",
                "two": "two",
            },
            "location": "/another/location/"
        }
        self.file_path = "/path/to/something"
        self.test = DestroyBuild(config=self.config, file_path=self.file_path)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(self.config, self.test.config)
        self.assertEqual(self.file_path, self.test.file_path)

    @patch("camel.terra.steps.destroy_build.Popen")
    def test_run(self, mock_Popen):
        self.test.run()

        self.assertEqual(2, len(mock_Popen.call_args_list))
        self.assertEqual({"shell": True}, mock_Popen.call_args_list[0][1])
        self.assertEqual("cd /path/to/something//another/location/ && terraform init",
                         mock_Popen.call_args_list[0][0][0])

        self.assertEqual({"shell": True}, mock_Popen.call_args_list[1][1])
        self.assertEqual('cd /path/to/something//another/location/ && terraform destroy -var="one=1" -var="two=two" ',
                         mock_Popen.call_args_list[1][0][0])


if __name__ == "__main__":
    main()
