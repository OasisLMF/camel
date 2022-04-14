"""
This file defines the object that manages the user around base camp.
"""
from camel.basecamp.components.storage_descriptor import DataStorageDescriptor
from subprocess import Popen, PIPE
from uuid import uuid4


class User:

    DATA = DataStorageDescriptor()

    def __init__(self, name: str, file_path: str) -> None:
        self.name: str = name
        self.file_path: str = file_path
        self.data: dict = self.DATA

    def write(self) -> None:
        self.DATA = self.data

    @property
    def schema(self) -> dict:
        return {
            "NAME": self.data.get("NAME", "undefined")
        }

    @staticmethod
    def get_cached_username() -> str:
        get_ids = Popen("ssh-add -L", shell=True, stdout=PIPE)
        get_ids.wait()
        communication_buffer = get_ids.communicate()[0].decode().split("\n")

        user_found = False
        cached_id = None

        for command in communication_buffer:
            if "@" in command:
                inner_buffer = command.split(" ")
                for id_ref in inner_buffer:
                    if "@" in id_ref:
                        cached_id = id_ref
                        user_found = True
                        break
                if user_found is True:
                    break

        if cached_id is None:
            print("WARNING: github SSH key not found so either you have not added it to ssh-add or you have not forwarded it")
            temp_id = str(uuid4())
            print(f"your temp id is {temp_id}")
            return temp_id
        return cached_id

    @staticmethod
    def from_cache(file_path: str) -> "User":
        user_name = User.get_cached_username()
        return User(name=user_name, file_path=file_path)

