"""
This file contains the BuildsAccessAdapter class to accessing and updating builds.
"""
from typing import Optional, List

from camel.storage.components.build_record import BuildRecord, Status
from camel.storage.components.build_storage import BuildStorage


class BuildsAccessAdapter:
    """
    This class is responsible for accessing the builds and their statuses.

    Attributes:
        storage (BuildStorage): The storage handle for the builds.
    """
    def __init__(self, s3_path: Optional[str] = None) -> None:
        """
        The constructor for the BuildsAccessAdapter class.

        Args:
            s3_path: The path to the s3 bucket where the builds are stored.
        """
        self.storage: BuildStorage = BuildStorage(s3_path=s3_path)

    def get_build(self, state_path: str) -> Optional[BuildRecord]:
        """
        Gets a build by its state_path.

        Args:
            state_path: The state_path of the build.

        Returns: The build with the given state_path.
        """
        try:
            return self.storage.get_build(state_path=state_path)
        except FileNotFoundError:
            return None

    def get_builds(self) -> List[BuildRecord]:
        """
        Gets all the builds in the build storage.

        Returns: A list of all the builds in the build storage.
        """
        data = self.storage.data
        return [BuildRecord.from_dict(data=build) for build in data.values()]

    def add_new_build(self, state_path: str, ip_address: str, build_name: str) -> None:
        """
        Adds a new build to the build storage.

        Args:
            state_path: the state_path of the build to add.
            ip_address: the ip_address of the build to add.
            build_name: the build_name of the build to add.

        Returns: None
        """
        build: Optional[BuildRecord] = self.get_build(state_path=state_path)

        if build is not None:
            print(f"Build with state_path {state_path} already exists will be overwriting")

        self.storage.insert_build(state_path=state_path, ip_address=ip_address,
                                  build_name=build_name, status=Status.RUNNING)

    def update_build(self, state_path: str, status: Status) -> None:
        """
        Updates the status of a build.

        Args:
            state_path: the state_path of the build to update.
            status: the status to update the build to.

        Returns: None
        """
        build: Optional[BuildRecord] = self.storage.get_build(state_path=state_path)

        build.status = status
        self.storage.insert_build(state_path=state_path, ip_address=build.ip_address,
                                  build_name=build.build_name, status=build.status)
