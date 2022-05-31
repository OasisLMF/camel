"""
This file defines the object that manages the status and paths for a base camp.
"""
import glob
import json
import os
from subprocess import Popen
from typing import Optional, List


class Mapper:
    """
    This object is responsible for mapping out the current position of the user and the paths for the data in the
    basecamp.
    """
    def __init__(self) -> None:
        """
        The constructor Mapper object.
        """
        self.current_path: str = os.getcwd()

    def _create_venv(self) -> None:
        """
        Creates the venv for the basecamp.

        Returns: None
        """
        create_venv = Popen(f"cd {self.current_path} && python3 -m venv venv", shell=True)
        create_venv.wait()

        command_buffer = [
            f"cd {self.current_path}/ && ",
            f"source venv/bin/activate && ",
            f"pip install git+https://github.com/OasisLMF/camel"
        ]
        command = "".join(command_buffer)
        install_camel = Popen(command, shell=True)
        install_camel.wait()

    def create(self, name: str) -> bool:
        """
        Creates a new basecamp infrastructure if not in a basecamp.

        Args:
            name: (str) the name of the basecamp being created

        Returns: (bool) True if created False if not
        """
        if self.in_camp is False:
            os.mkdir(self.projects_path)
            os.mkdir(self.configs_path)
            os.mkdir(self.users_path)
            os.mkdir(self.data_path)
            # self._create_venv()
            with open(self.camp_charter_path, "w") as file:
                data = {"NAME": name}
                json.dump(data, file)
            # TODO => api.py writing isn't defined yet
            return True
        return False

    @property
    def projects_path(self) -> str:
        return self.current_path + "/projects/"

    @property
    def configs_path(self) -> str:
        return self.current_path + "/configs/"

    @property
    def users_path(self) -> str:
        return self.current_path + "/users/"

    @property
    def data_path(self) -> str:
        return self.current_path + "/data/"

    @property
    def api_path(self) -> str:
        return self.current_path + "/api.py"

    @property
    def camp_charter_path(self) -> str:
        return self.current_path + "/camp_charter.json"

    @property
    def in_camp(self) -> bool:
        if os.path.isfile(self.camp_charter_path) is False:
            return False
        return True

    @property
    def camp_name(self) -> Optional[str]:
        if self.in_camp is True:
            with open(self.camp_charter_path, "r") as file:
                charter_data = json.loads(file.read())
                return charter_data["NAME"]
        return None

    @property
    def available_projects(self) -> List[str]:
        if self.in_camp is True:
            return [x.replace(".json", "").split("/")[-1] for x in glob.glob(self.projects_path + "*.json")]
        return []

    @property
    def available_users(self) -> List[str]:
        if self.in_camp is True:
            return [x.replace(".json", "").split("/")[-1] for x in glob.glob(self.users_path + "*.json")]
        return []

    @property
    def available_configs(self) -> List[str]:
        if self.in_camp is True:
            return [x.replace(".yml", "").split("/")[-1] for x in glob.glob(self.configs_path + "*.yml")]
        return []
