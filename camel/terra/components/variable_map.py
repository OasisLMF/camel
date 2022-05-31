from typing import Optional


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class VariableMap(dict, metaclass=Singleton):
    """
    This class is responsible to keeping track of all the variables to be referenced to throughout the program.

    Attributes:
        ip_address (Optional[str]): the latest IP address for remote variables
    """
    def __init__(self) -> None:
        """
        The constructor for the VariableMap class.
        """
        super().__init__({})
        self.ip_address: Optional[str] = None

    def load_data(self, mapped_variables: dict, ip_address: str) -> None:
        """
        Loads the variables and the latest IP address if a variable is remote.

        :param mapped_variables: (dict) the variables to be inserted into the map
        :param ip_address: (str) the latest IP address for remote variables
        :return: None
        """
        self.update(mapped_variables)
        self.ip_address = ip_address
