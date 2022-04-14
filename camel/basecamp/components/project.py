from enum import Enum

from camel.basecamp.components.storage_descriptor import DataStorageDescriptor


class Status(Enum):
    DESTROYED = "destroyed"
    DESTROYING = "destroying"
    CREATING = "creating"
    RUNNING = "running"
    UNDEFINED = "undefined"


class Project:

    DATA = DataStorageDescriptor()

    def __init__(self, name: str, file_path: str) -> None:
        self.name: str = name
        self.file_path: str = file_path
        self.data: dict = self.DATA

    def write(self) -> None:
        self.DATA = self.data

    def update_status(self, status: Status) -> None:
        self.data["STATUS"] = status.value

    @property
    def schema(self) -> dict:
        return {
            "NAME": self.data.get("NAME", "undefined"),
            "STATUS": self.data.get("STATUS", Status.UNDEFINED.value),
            "CREATED_BY": self.data.get("CREATED_BY", "undefined"),
            "LAST_INTERACTED_BY": self.data.get("LAST_INTERACTED_BY", "undefined")
        }
