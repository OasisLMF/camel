from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.components.install_command import InstallCommand


class TestInstallCommand(TestCase):

    def setUp(self) -> None:
        self.package = "awscli"
        self.ip_address = "12345"
        self.test = InstallCommand(package=self.package, ip_address=self.ip_address)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(self.package, self.test.package)
        self.assertEqual(self.ip_address, self.test.ip_address)

    @patch("camel.terra.components.install_command.TerminalCommand")
    def test__check_outcome(self, mock_terminal_command):
        mock_terminal_command.return_value.wait.return_value = []
        outcome = self.test._check_outcome()

        self.assertEqual(False, outcome)
        mock_terminal_command.assert_called_once_with(
            command=f"dpkg -s {self.package} | grep Status", ip_address=self.ip_address
        )

        mock_terminal_command.reset_mock()
        mock_terminal_command.return_value.wait.return_value = ["Status: install ok installed"]

        outcome = self.test._check_outcome()
        self.assertEqual(True, outcome)
        mock_terminal_command.assert_called_once_with(
            command=f"dpkg -s {self.package} | grep Status", ip_address=self.ip_address
        )

        mock_terminal_command.reset_mock()
        mock_terminal_command.return_value.wait.return_value = ["Status: error"]

        outcome = self.test._check_outcome()
        self.assertEqual(False, outcome)
        mock_terminal_command.assert_called_once_with(
            command=f"dpkg -s {self.package} | grep Status", ip_address=self.ip_address
        )

    @patch("camel.terra.components.install_command.print")
    @patch("camel.terra.components.install_command.TerminalCommand")
    @patch("camel.terra.components.install_command.time")
    @patch("camel.terra.components.install_command.InstallCommand._check_outcome")
    def test_install_package(self, mock_check_outcome, mock_time, mock_terminal_command, mock_print):
        mock_check_outcome.return_value = True
        outcome = self.test.install_package()

        self.assertEqual(True, outcome)
        mock_check_outcome.assert_called_once()
        mock_terminal_command.assert_not_called()
        mock_time.assert_not_called()
        mock_print.assert_called_once_with(f"Package {self.package} is already installed. Skipping installation.")

        mock_check_outcome.reset_mock()
        mock_terminal_command.reset_mock()
        mock_time.reset_mock()

        mock_terminal_command.return_value.wait.return_value = True
        mock_check_outcome.side_effect = [False, True]

        outcome = self.test.install_package()

        self.assertEqual(True, outcome)
        self.assertEqual(2, mock_check_outcome.call_count)
        mock_terminal_command.assert_called_once_with(
            command=f"sudo apt-get install {self.package} -y", ip_address=self.ip_address
        )

        mock_check_outcome.reset_mock()
        mock_terminal_command.reset_mock()
        mock_time.reset_mock()

        mock_check_outcome.side_effect = [False, False, True]

        outcome = self.test.install_package()

        self.assertEqual(True, outcome)
        self.assertEqual(3, mock_check_outcome.call_count)
        mock_terminal_command.assert_called_once_with(
            command=f"sudo apt-get install {self.package} -y", ip_address=self.ip_address
        )
        mock_time.sleep.assert_called_once_with(3)

        mock_check_outcome.reset_mock()
        mock_terminal_command.reset_mock()
        mock_time.reset_mock()

        mock_check_outcome.side_effect = [False, False, False, False, False, False]
        self.assertEqual(False, self.test.install_package())


if __name__ == "__main__":
    main()
