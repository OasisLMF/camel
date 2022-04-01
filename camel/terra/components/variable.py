from typing import Optional, Any
from subprocess import Popen, PIPE

from camel.storage.components.profile_storage import LocalProfileVariablesStorage
from camel.terra.components.variable_map import VariableMap


class Variable:

    def __init__(self, name: str) -> None:
        self.path: Optional[str] = None
        self.name: str = name
        self.ip_address: Optional[str] = None

    def _extract_variable_from_local_storage(self) -> str:
        local_storage = LocalProfileVariablesStorage()
        current_value = local_storage.get(self.name[2:])

        if current_value is None:
            raise ValueError(f"{current_value[2:]} not found in profile storage")
        return current_value

    def _extract_value_from_config_vars(self) -> str:
        variable_map = VariableMap()
        variable_data = variable_map[self.name[2:]]

        self.path = variable_data["path"]
        self.ip_address = variable_data.get("ip_address")

        if self.ip_address is None:
            with open(f"{self.path}/{self.name[2:]}.txt", "r") as file:
                value = file.read()
            return value

        ssh_value_process = Popen(f"ssh -A ubuntu@{variable_map.ip_address} 'cat {self.path}/{self.name[2:]}.txt'", stdout=PIPE, shell=True)
        ssh_value_process.wait()
        return ssh_value_process.communicate()[0].decode().replace("\n", "")

    def __str__(self):
        return self.value

    @property
    def value(self) -> str:
        if isinstance(self.name, str) and self.name[:2] == "=>":
            return self._extract_variable_from_local_storage()
        elif isinstance(self.name, str) and self.name[:2] == ">>":
            return self._extract_value_from_config_vars()
        return self.name
