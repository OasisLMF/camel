"""
This file contains the BuildsAccessAdapter class to accessing and updating build logs.
"""
import json
from os.path import join, dirname, realpath, exists
from typing import Optional

from camel.storage.components.build_record import BuildRecord, Status


class BuildStorage:
    """
    This class is responsible for storing the builds and their statuses.

    Attributes:
        s3_path (Optional[str]): The path to the s3 bucket where the builds are stored.
    """
    def __init__(self, s3_path: Optional[str] = None) -> None:
        """
        The constructor for the BuildStorage class.

        Args:
            s3_path: The path to the s3 bucket where the builds are stored.
        """
        self.s3_path: str = s3_path
        self._data: Optional[dict] = None

    def _read_local(self) -> dict:
        """
        Reads the builds from the local file.

        Returns: the builds from the local file.
        """
        if exists(self.file_path) is False:
            return {}
        with open(self.file_path, "r") as file:
            data = json.loads(file.read())
        return data

    def _write_local(self) -> None:
        """
        Writes the builds to the local file.

        Returns: None
        """
        data = self.data
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def _read_s3(self) -> dict:
        """
        Reads the builds from the s3 bucket.

        Warnings: This method is not implemented yet.

        Returns: the builds from the s3 bucket.
        """
        raise NotImplementedError("read s3 is not supported at the moment")

    def _write_s3(self) -> None:
        """
        Writes the builds to the s3 bucket.

        Warnings: This method is not implemented yet.

        Returns: None
        """
        raise NotImplementedError("write s3 is not supported at the moment")

    def write(self) -> None:
        """
        Writes the self.data to the storage.

        Returns: None
        """
        if self.s3_path is None:
            self._write_local()
        else:
            self._write_s3()

    def get_build(self, state_path: str) -> BuildRecord:
        """
        Gets the build with the given state_path.

        Args:
            state_path: the state_path of the build to get.

        Returns: the build with the given state_path.
        """
        data = self.data.get(state_path)
        if data is None:
            raise FileNotFoundError(f"state {state_path} is not stored in the builds")
        return BuildRecord.from_dict(data)

    def insert_build(self, state_path: str, ip_address: str, build_name: str, status: Status) -> None:
        """
        Inserts a build into the storage.

        Args:
            state_path: the state_path of the build to insert.
            ip_address: the ip_address of the build to insert.
            build_name: the build_name of the build to insert.
            status: the status of the build to insert.

        Returns: None
        """
        build_record = BuildRecord(state_path=state_path, ip_address=ip_address, build_name=build_name, status=status)
        self.data[state_path] = build_record.to_dict()
        self.write()

    @property
    def file_path(self) -> str:
        if self.s3_path is None:
            return join(dirname(realpath(__file__)), "builds.json")
        return self.s3_path

    @property
    def data(self) -> dict:
        if self._data is None:
            if self.s3_path is None:
                self._data = self._read_local()
            else:
                self._data = self._read_s3()
        return self._data
