"""
This file defines the classes that manage the data around projects in basecamp.
"""
from enum import Enum

from camel.basecamp.components.storage_descriptor import DataStorageDescriptor


class Status(Enum):
    """
    This class is an Enum that defines the project statuses that are available.
    """
    DESTROYED = "destroyed"
    DESTROYING = "destroying"
    CREATING = "creating"
    RUNNING = "running"
    UNDEFINED = "undefined"


class Project:
    """
    This class is responsible for managing the data around a project.

    Attributes:
        name (str): the name of the project
        file_path (str): the path where the data file for the project is stored
        data (dict): the data around the project
    """
    DATA = DataStorageDescriptor()

    def __init__(self, name: str, file_path: str) -> None:
        """
        The constructor for the Project class.

        Args:
            name: (str) the name of the project
            file_path: (str) the path where the data file for the project is stored
        """
        self.name: str = name
        self.file_path: str = file_path
        self.data: dict = self.DATA

    def write(self) -> None:
        """
        Writes the data of the project to the file with the path (self.path + self.name).

        Returns: None
        """
        self.DATA = self.data

    def update_status(self, status: Status) -> None:
        """
        Updates the status of the project.

        Args:
            status: (Status) the status that the project is going to be updated to.

        Returns: None
        """
        self.data["STATUS"] = status.value

    @property
    def schema(self) -> dict:
        return {
            "NAME": self.data.get("NAME", "undefined"),
            "STATUS": self.data.get("STATUS", Status.UNDEFINED.value),
            "CREATED_BY": self.data.get("CREATED_BY", "undefined"),
            "LAST_INTERACTED_BY": self.data.get("LAST_INTERACTED_BY", "undefined")
        }
