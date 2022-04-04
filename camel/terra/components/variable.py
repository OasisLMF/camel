"""
This file defines the Variable class in order to manage variables from configs and the environment.
"""
from subprocess import Popen, PIPE
from typing import Optional

from camel.storage.components.profile_storage import LocalProfileVariablesStorage
from camel.terra.components.variable_map import VariableMap


class Variable:
    """
    This class is responsible for taking in a variable, working out if it is a raw variable or a pointer to a variable
    defined in the config file to be collected from the environment or a stored variable in the profile, retrieving
    the value, and presenting it.

    Attributes:
         path (Optional[str]): the path where the variable can be accessed
         name (str): the name of the variable
         ip_address (Optional[str]): where the variable is stored if not local
    """
    def __init__(self, name: str) -> None:
        """
        The constructor for the Variable class.

        :param name: (str) the name of the variable
        """
        self.path: Optional[str] = None
        self.name: str = name
        self.ip_address: Optional[str] = None

    def _extract_variable_from_local_storage(self) -> str:
        """
        Extracts the variable value from a stored variable in the profile.

        :return: (str) the variable value
        """
        local_storage = LocalProfileVariablesStorage()
        current_value = local_storage.get(self.name[2:])

        if current_value is None:
            raise ValueError(f"{self.name[2:]} not found in profile storage")
        return current_value

    def _extract_value_from_config_vars(self) -> str:
        """
        Extracts the variable value from a file whether it's local or on a server.

        :return: (str) the variable value
        """
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
