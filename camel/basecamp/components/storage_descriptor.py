import json
import os


class DataStorageDescriptor:

    @staticmethod
    def file_path(obj) -> str:
        return obj.file_path + f"/{obj.name}.json"

    @staticmethod
    def _write(data: dict, file_path: str) -> None:
        with open(file_path, "w") as file:
            file.write(json.dumps(data))

    def __get__(self, obj, owner) -> dict:
        file_path: str = DataStorageDescriptor.file_path(obj=obj)

        if os.path.isfile(path=file_path) is False:
            self._write(data={}, file_path=file_path)

        with open(DataStorageDescriptor.file_path(obj=obj), "r") as file:
            data = json.loads(file.read())
        return data

    def __set__(self, obj, value: dict) -> None:
        self._write(data=value, file_path=DataStorageDescriptor.file_path(obj=obj))
