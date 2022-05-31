"""
This file defines the class and manages the data around local repo configs.
"""
import os

import yaml


class LocalRepoConfig(dict):
    """
    This class is responsible for loading the config data and managing it.
    Attributes:
        config_path (str): the path to the yml file to be loaded
    """
    def __init__(self, config_path: str) -> None:
        """
        The constructor for the LocalRepoConfig class.

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
        """
        Writes the data of the config to the yml file in the self.config_path.

        :return: None
        """
        placeholder = {}
        for key in self.keys():
            placeholder[key] = self[key]
        with open(self.config_path, "w") as file:
            yaml.dump(placeholder, file, default_flow_style=False)

    def add_repo_config(self, name: str, local_path: str) -> None:
        """
        Adds an SSH configuration to the config file.

        Args:
            name: (str) the name of the SSH config that is going to be referenced
            local_path: (str) local path to the repo being updated

        Returns: None
        """
        self[name] = {
            "local_path": local_path
        }
