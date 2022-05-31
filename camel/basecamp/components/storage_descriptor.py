"""
This file defines the descriptor for storing and reading data for components in the basecamp.
"""
from typing import Any

import json
import os


class DataStorageDescriptor:
    """
    This class responsible for reading and writing data for components for the basecamp.
    """
    @staticmethod
    def file_path(obj: Any) -> str:
        """
        Creates a path for the file to be read and written.

        Args:
            obj: (Any) an object with a self.file_path and self.name

        Returns: (str) the path to the file being read or written
        """
        return obj.file_path + f"/{obj.name}.json"

    @staticmethod
    def _write(data: dict, file_path: str) -> None:
        """
        Writes data to a file.

        Args:
            data: (dict) the data to be written
            file_path: (str) the path to the file that the data will be written to

        Returns: None
        """
        with open(file_path, "w") as file:
            file.write(json.dumps(data))

    def __get__(self, obj, owner) -> dict:
        """
        Extracts the data from the file.

        Args:
            obj: (Any) the object calling the descriptor
            owner: (Any) the type owning the class of obj

        Returns: (dict) the data read from the file
        """
        file_path: str = DataStorageDescriptor.file_path(obj=obj)

        if os.path.isfile(path=file_path) is False:
            self._write(data={}, file_path=file_path)

        with open(DataStorageDescriptor.file_path(obj=obj), "r") as file:
            data = json.loads(file.read())
        return data

    def __set__(self, obj, value: dict) -> None:
        """
        Writes the data to the file.

        Args:
            obj: (Any) the object calling the descriptor
            value: (dict) the data being written to the file

        Returns: None
        """
        self._write(data=value, file_path=DataStorageDescriptor.file_path(obj=obj))
