import glob
from typing import List

from camel.storage.components.profile import Profile


class TerraConfigMapper(Profile):

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def get_configs(self) -> List[str]:
        list_of_directories = glob.glob(f"{self.terra_builds_path}/*.yml")
        return [x.replace(".yml", "") for x in list_of_directories]
