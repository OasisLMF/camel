"""
This file defines the class that gets meta data from pypi on the oasisLMF package (not used for now but can be handy)
Because class is not used there are no unit tests please build them if planning to use this class.
"""
from typing import Optional

import requests


class OasislmfMetaData(dict):

    def __init__(self, version_number: Optional[str]) -> None:
        super().__init__({})
        self._load(version=version_number)

    def _load(self, version: Optional[str]) -> None:
        """
        Loads the data from pypi to get the meta data from the hosted package and populates the class.

        Args:
            version: (Optional[str]) the version to be inspected (latest will be used if None)

        Returns: None
        """
        url: str = "https://pypi.org/pypi/oasislmf/json"
        if version is not None:
            url: str = f"fhttps://pypi.org/pypi/oasislmf/{version}/json"
        req = requests.get(url)
        self.update(req.json()["info"])

    @property
    def version_number(self) -> str:
        return self["version"]
