"""
This file defines the class around managing config variables for a terra build.
"""
import argparse
from enum import Enum
from typing import Optional, List

import yaml


class LocationEnum(Enum):
    EU_WEST_ONE = "eu_west_1"


class ConfigEngine(dict):
    """
    This class is responsible for loading the config data and managing it.

    Attributes:
        config_path (str): the path to the yml file to be loaded
        location (Optional[LocationEnum]): the location of where the build is happening (currently has no effect)
    """
    def __init__(self, config_path: str) -> None:
        """
        The constructor for the ConfigEngine class.

        :param config_path: (str) the default path to the config file
        """
        super().__init__({})
        self.config_path: str = config_path
        # self._establish_path()
        self.location: Optional[LocationEnum] = None
        self._read()
        # self._establish_location()

    def _establish_path(self) -> None:
        """
        Updates the self.config_path based on the arguments parsed into the program.

        :return: None
        """
        config_parser = argparse.ArgumentParser()
        config_parser.add_argument('--config_path', action='store', type=str, required=False, default=self.config_path)
        args = config_parser.parse_args()
        self.config_path = args.config_path

    def _read(self) -> None:
        """
        Reads the config file based off the self.config_path file. File needs to be in yml.

        :return: None
        """
        my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
        my_parser.add_argument("path", help="the path to the config file")

        with open(self.config_path) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            self.update(data)

    def _establish_location(self) -> None:
        self.location = LocationEnum(self["location"])

    @property
    def steps(self) -> Optional[List[dict]]:
        return self.get("steps")
