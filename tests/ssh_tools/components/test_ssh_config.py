"""
This file tests the management of ssh configs
"""
from unittest import main, TestCase
from unittest.mock import patch, MagicMock, PropertyMock

from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile


class SshConfigTest(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        profile = Profile(name="maxwell")
        test = SshConfig(config_path=profile.configs_path + "ssh_config.yml")
        print(test)


if __name__ == "__main__":
    main()
