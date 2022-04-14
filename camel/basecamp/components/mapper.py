import glob
import json
import os
from typing import Optional, List


class Mapper:

    def __init__(self) -> None:
        self.current_path: str = os.getcwd()

    def create(self, name: str) -> bool:
        if self.in_camp is False:
            os.mkdir(self.projects_path)
            os.mkdir(self.configs_path)
            os.mkdir(self.users_path)
            with open(self.camp_charter_path, "w") as file:
                data = json.dumps({"NAME": name})
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
    def api_path(self) -> str:
        return self.current_path + "/api.py"

    @property
    def camp_charter_path(self) -> str:
        return self.current_path + "/.camp_charter.json"

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
