"""
Defines the object that maps the stashed terraform config files.
"""
import glob
from typing import List

from camel.storage.components.profile import Profile


class TerraConfigMapper(Profile):
    """
    This class inherits from the Profile class adding functionality for getting terraform config files.
    """
    def __init__(self, name: str) -> None:
        """
        The constructor for the TerraConfigMapper class.

        :param name: (str) the name of the profile being loaded
        """
        super().__init__(name=name)

    def get_configs(self) -> List[str]:
        """
        Gets all the names of the stashed terraform configs.

        :return: (List[str]) the names of all the stashed terraform config files
        """
        list_of_directories = glob.glob(f"{self.terra_builds_path}/*.yml")
        return [x.replace(".yml", "") for x in list_of_directories]
