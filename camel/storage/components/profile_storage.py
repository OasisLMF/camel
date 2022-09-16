"""
This file defines the class and manages the data variables and their values for the profile.
"""
import os

import yaml
from gerund.components.local_variable_storage import LocalVariableStorage

from camel.storage.components.profile import Profile


class LocalProfileVariablesStorage(dict):
    """
    This class is responsible for loading the config data and managing it.

    Attributes:
        config_path (str): the path to the yml file to be loaded
        profile (Profile): the cached profile for loading and saving data
    """
    def __init__(self) -> None:
        """
        The constructor for the LocalRepoConfig class.
        """
        super().__init__({})
        self.profile = Profile.get_cached_profile()
        self.config_path: str = self.profile.configs_path + "/STORAGE_VARS123.yml"
        self.read()

    def _update_gerund(self) -> None:
        """
        Updates the gerund local storage so gerund variables can access the latest values.

        Returns: None
        """
        gerund_storage = LocalVariableStorage()
        gerund_storage.update(self)

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
        self._update_gerund()

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

    def add_variable(self, name, value) -> None:
        """
        Writes a value to the storage.

        Args:
            name: (str) the name of the variable being written
            value: (Any) the value being added (should be supported by yml)

        Returns: None
        """
        self[name] = value
        self.write()
        self._update_gerund()

    def delete_value(self, name) -> None:
        """
        Deletes a value from the storage

        Args:
            name: (str) the name of the value being deleted

        Returns: None
        """
        del self[name]
        self.write()
        self._update_gerund()
