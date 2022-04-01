"""
This file defines the class around managing data for a profile.
"""
import os
import shutil
from glob import glob
from pathlib import Path
from typing import List


class Profile:
    """
    This class is responsible for managing the data around a user profile.

    Attributes:
        name (str): the name of the profile
    """
    ROOT_PATH: str = str(Path.home()) + "/.camel_storage/"

    def __init__(self, name: str) -> None:
        """
        The constructor for the Profile class.

        Args:
            name: (str) the name of the profile being loaded
        """
        self.name: str = name

    def create_profile(self) -> None:
        """
        Creates the directories for a new profile.

        Returns: None
        """
        os.mkdir(self.profile_base_path)
        os.mkdir(self.keys_path)
        os.mkdir(self.terra_builds_path)
        os.mkdir(self.process_flags_path)
        os.mkdir(self.configs_path)

    def delete_profile(self) -> None:
        """
        Deletes all the data for a profile.

        Returns: None
        """
        shutil.rmtree(self.profile_base_path)

    def cache_profile_name(self) -> None:
        """
        Saves the name of the profile in a file called profile_cache.txt essentially caching the name of the profile.

        Returns: None
        """
        current_directory = str(os.path.dirname(os.path.realpath(__file__)))
        cache_directory = current_directory + "/profile_cache.txt"
        with open(cache_directory, "w") as file:
            file.write(self.name)

    @classmethod
    def get_cached_profile(cls):
        """
        Gets the profile from the cached name.

        Returns: self
        """
        current_directory = str(os.path.dirname(os.path.realpath(__file__)))
        cache_directory = current_directory + "/profile_cache.txt"
        with open(cache_directory, "r") as file:
            name = file.read()
        return cls(name=name)

    @classmethod
    def create_storage(cls) -> None:
        """
        Creates the directory for the profile.

        Returns: None
        """
        if not os.path.isdir(Profile.ROOT_PATH):
            os.mkdir(Profile.ROOT_PATH)

    @classmethod
    def get_profiles(cls) -> List[str]:
        """
        Gets a list of profiles that can be accessed.

        Returns: (List[str]) list of available profiles
        """
        return [x.split("/")[-2] for x in glob(Profile.ROOT_PATH + "/*/", recursive=True)]

    @property
    def profile_base_path(self) -> str:
        return self.ROOT_PATH + f"{self.name}/"

    @property
    def keys_path(self) -> str:
        return self.profile_base_path + "keys/"

    @property
    def terra_builds_path(self) -> str:
        return self.profile_base_path + "terra_builds/"

    @property
    def process_flags_path(self) -> str:
        return self.profile_base_path + "process_flags/"

    @property
    def configs_path(self) -> str:
        return self.profile_base_path + "configs/"

    @staticmethod
    def print_out_profiles() -> None:
        """
        Prints out the current active profile and the available profiles.  

        Returns: None
        """
        try:
            current_profile = Profile.get_cached_profile().name
            print(f"\ncurrent profile: {current_profile}")
        except:
            print("\ncurrent profile: None")
        print("\navailable profiles:")
        for profile in Profile.get_profiles():
            print(profile)
