from os.path import join, dirname, realpath, exists
from typing import Optional
import json


class BuildStorage:

    def __init__(self, s3_path: Optional[str] = None) -> None:
        self.s3_path: str = s3_path
        self._data: Optional[dict] = None

    # check the build log for the state

    def _read_local(self) -> dict:
        if exists(self.file_path) is False:
            return {}
        with open(self.file_path, "r") as file:
            data = json.loads(file.read())
        return data

    def _write_local(self) -> None:
        data = self.data
        with open(self.file_path, "w") as file:
            json.dump(data, file)
            # file.write(json.dumps(self.data))

    def _read_s3(self) -> dict:
        pass

    def _write_s3(self) -> None:
        pass

    def write(self) -> None:
        if self.s3_path is None:
            self._write_local()
        else:
            self._write_s3()

    @property
    def file_path(self) -> str:
        if self.s3_path is None:
            return join(dirname(realpath(__file__)), "builds.json")
        return self.s3_path

    @property
    def data(self) -> dict:
        if self._data is None:
            if self.s3_path is None:
                self._data = self._read_s3()
            self._data = self._read_local()
        return self._data
