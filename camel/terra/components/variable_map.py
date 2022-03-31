from typing import Optional


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class VariableMap(dict, metaclass=Singleton):

    def __init__(self) -> None:
        super().__init__({})
        self.ip_address: Optional[str] = None

    def load_data(self, mapped_variables: dict, ip_address: str) -> None:
        self.update(mapped_variables)
        self.ip_address = ip_address
