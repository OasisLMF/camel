import os
from glob import glob
from pathlib import Path


class Profile:

    ROOT_PATH: str = str(Path.home()) + "./camel_storage/"

    def __init__(self, name: str) -> None:
        self.name: str = name

    def create_profile(self):
        os.mkdir(self.profile_base_path)
        os.mkdir(self.keys_path)
        os.mkdir(self.terra_builds_path)
        os.mkdir(self.process_flags_path)
        os.mkdir(self.configs_path)

    def delete_profile(self):
        pass

    def cache_profile_name(self) -> None:
        current_directory = str(os.path.dirname(os.path.realpath(__file__)))
        cache_directory = current_directory + "/profile_cache.txt"
        with open(cache_directory, "w") as file:
            file.write(self.name)

    @classmethod
    def get_cached_profile(cls):
        current_directory = str(os.path.dirname(os.path.realpath(__file__)))
        cache_directory = current_directory + "/profile_cache.txt"
        with open(cache_directory, "r") as file:
            name = file.read()
        return cls(name=name)

    @classmethod
    def create_storage(cls):
        if not os.path.isdir(Profile.ROOT_PATH):
            os.mkdir(Profile.ROOT_PATH)

    @classmethod
    def get_profiles(cls):
        return glob(Profile.ROOT_PATH + "/*/", recursive=True)

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


if __name__ == "__main__":
    outcome = Profile.get_cached_profile()
    print(outcome.name)
