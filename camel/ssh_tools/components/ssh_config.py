import os

import yaml


class SshConfig(dict):
    """
    This class is responsible for loading the config data and managing it.
    Attributes:
        config_path (str): the path to the yml file to be loaded
    """
    def __init__(self, config_path: str) -> None:
        """
        The constructor for the SshConfig class.

        :param config_path: (str) the default path to the config file
        """
        super().__init__({})
        self.config_path: str = config_path
        self.read()

    def read(self) -> None:
        """
        Reads the config file based off the self.config_path file. File needs to be in yml.
        :return: None
        """
        if os.path.exists(self.config_path) is False:
            self.write()

        with open(self.config_path, "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            self.update(data)

    def write(self) -> None:
        placeholder = {}
        for key in self.keys():
            placeholder[key] = self[key]
        with open(self.config_path, "w") as file:
            yaml.dump(placeholder, file, default_flow_style=False)

    def add_ssh_config(self, name: str, ip_address: str, vpn: bool, key: str, username: str) -> None:
        self[name] = {
            "ip_address": ip_address,
            "vpn": vpn,
            "key": key,
            "username": username
        }
