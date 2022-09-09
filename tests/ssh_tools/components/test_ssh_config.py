"""
This file tests the management of ssh configs
"""
from unittest import main, TestCase
from unittest.mock import patch, MagicMock, PropertyMock

from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile


class SshConfigTest(TestCase):

    @patch("camel.ssh_tools.components.ssh_config.SshConfig.read")
    def setUp(self, _) -> None:
        self.profile = Profile(name="maxwell")
        self.path = self.profile.configs_path + "ssh_config.yml"
        self.test = SshConfig(config_path=self.path)

    def tearDown(self) -> None:
        pass

    @patch("camel.ssh_tools.components.ssh_config.SshConfig.read")
    def test___init__(self, mock_read):
        profile = Profile(name="maxwell")
        test = SshConfig(config_path=profile.configs_path + "ssh_config.yml")
        self.assertEqual(self.path, test.config_path)
        mock_read.assert_called_once_with()

    @patch("camel.ssh_tools.components.ssh_config.yaml.dump")
    @patch("camel.ssh_tools.components.ssh_config.open")
    def test_write(self, mock_open, mock_dump):
        test_dict = {
            "one": 1,
            "two": 2
        }
        self.test.update(test_dict)
        self.test.write()

        mock_open.assert_called_once_with(self.path, "w")
        mock_dump.assert_called_once_with(test_dict,
                                          mock_open.return_value.__enter__.return_value,
                                          default_flow_style=False)

    def test_add_ssh_config(self):
        expected_outcome = {
            'maxwell': {
                'ip_address': '1234',
                'vpn': True,
                'key': 'thekey.pem',
                'username': 'maxwellflitton'
            }
        }
        self.test.add_ssh_config(
            name="maxwell",
            ip_address="1234",
            vpn=True,
            key="thekey.pem",
            username="maxwellflitton"
        )
        self.assertEqual(expected_outcome, self.test)


if __name__ == "__main__":
    main()
