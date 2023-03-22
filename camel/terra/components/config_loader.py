"""
This file defines the class around managing config variables for a terra build.
"""
from typing import Optional, List

import yaml


class ConfigEngine(dict):
    """
    This class is responsible for loading the config data and managing it.

    Attributes:
        config_path (str): the path to the yml file to be loaded
    """
    def __init__(self, config_path: str) -> None:
        """
        The constructor for the ConfigEngine class.

        :param config_path: (str) the default path to the config file
        """
        super().__init__({})
        self.config_path: str = config_path
        self._read()

    def _read(self) -> None:
        """
        Reads the config file based off the self.config_path file. File needs to be in yml.

        :return: None
        """
        with open(self.config_path) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            self.update(data)

    @property
    def steps(self) -> Optional[List[dict]]:
        return self.get("steps")
