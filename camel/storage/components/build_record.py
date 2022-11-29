"""
This file defines the class for the build record.
"""
from enum import Enum
from datetime import datetime
from typing import Optional


class Status(Enum):
    """
    This class defines the status of a build.
    """
    SUCCESS = "success"
    FAILURE = "failure"
    RUNNING = "running"
    DESTROYED = "destroyed"


class BuildRecord:
    """
    This class is responsible for managing the data for a build.

    Attributes:
        state_path: (str) the path to the Terraform state file for the build
        ip_address: (str) the IP address of the server that the build is running on
        build_name: (str) the name of the build
        status: (Status) the status of the build
        time_stamp: (Optional[str]) the timestamp of the last interaction
    """
    def __init__(self, state_path: str, ip_address: str, build_name: str, status: Status) -> None:
        """
        The constructor for the BuildRecord class.

        Args:
            state_path: the path to the Terraform state file for the build
            ip_address: the IP address of the server that the build is running on
            build_name: the name of the build
            status: the status of the build
        """
        self.state_path: str = state_path
        self.ip_address: str = ip_address
        self.build_name: str = build_name
        self.status: Status = status
        self.time_stamp: Optional[str] = None

    def to_dict(self) -> dict:
        """
        Converts the BuildRecord to a dictionary, use this function to write to file.

        Returns: the dictionary representation of the BuildRecord
        """
        return {
            "state_path": self.state_path,
            "ip_address": self.ip_address,
            "build_name": self.build_name,
            "status": self.status.value,
            "time_stamp": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }

    def __str__(self):
        return f"BuildRecord => \nstate_path: {self.state_path} " \
               f"\nip_address: {self.ip_address} " \
               f"\nbuild_name: {self.build_name} " \
               f"\nstatus: {self.status} " \
               f"\ntime_stamp: {self.time_stamp}"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_dict(data: dict) -> "BuildRecord":
        """
        Converts a dictionary to a BuildRecord.

        Args:
            data: the dictionary to be converted

        Returns: the BuildRecord representation of the dictionary
        """
        record = BuildRecord(
            state_path=data["state_path"],
            ip_address=data["ip_address"],
            build_name=data["build_name"],
            status=Status(data["status"])
        )
        record.time_stamp = data.get("time_stamp", str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return record
