"""
This file defines the class that handles overwriting data variables in a terraform file that usually cannot be
overwritten.
"""
import json
from typing import Optional
import os


class VariableEditor:
    """
    This class is responsible for overwriting variables in the main.tf file that usually cannot be overwritten.

    Attributes:
        data_directory (str): the path to the directory to where the main.tf and variables.json files are housed
    """
    def __init__(self, data_directory: str) -> None:
        """
        The constructor for the VariableEditor class.

        Args:
            data_directory: (str) the path to the directory to where the main.tf and variables.json files are housed
        """
        self.data_directory: str = data_directory + "/"
        self.cache_path: str = self.data_directory + "cache.txt"
        self.main_path: str = self.data_directory + "main.tf"
        self._overwrite_data: Optional[dict] = None
        self._main_data: Optional[str] = None

    @property
    def overwrite_data(self) -> dict:
        if self._overwrite_data is None:
            with open(self.data_directory + "variables.json", "r") as file:
                self._overwrite_data = json.loads(file.read())
        return self._overwrite_data

    @property
    def main_data(self) -> str:
        if self._main_data is None:
            with open(self.main_path, "r") as file:
                self._main_data = file.read()
        return self._main_data

    def write_main_data(self) -> None:
        """
        Writes the self.main_data to the main.tf file in the self.data_directory.

        Returns: None
        """
        with open(self.main_path, "w") as file:
            file.write(self.main_data)

    def overwrite_variable(self, key: str, variable: str) -> None:
        """
        Overwrites a variable in self.main_data.

        Args:
            key: (str) the name of the variable in the variables.json that is going to be overwritten.
            variable: (str) the new value of the variable that is being overwritten

        Returns: None
        """
        main_data = self.main_data
        variable_value = self.overwrite_data.get(key)

        if variable_value is None:
            raise ValueError(
                f"{key} key is not supported for overwriting a terra build as it "
                f"is not found in the variables.json keys"
            )

        self._main_data = main_data.replace(variable_value, variable)

    def wipe_cache(self) -> None:
        """
        Wipes the data of the cache so all data has to be loaded from the

        Returns: None
        """
        self._overwrite_data = None
        self._main_data = None

    def cache_main(self) -> None:
        """
        Caches the main.tf as cache.txt.

        Returns: None
        """
        os.rename(self.main_path, self.cache_path)

    def load_main(self) -> None:
        """
        Loads data from cache.txt and saves it as main.tf (existing main.tf is overwritten)

        Returns: None
        """
        if os.path.exists(self.main_path):
            os.remove(self.main_path)
        os.rename(self.cache_path, self.main_path)
