"""
This file defines the class around installing a package on a machine.
"""
import time
from typing import Optional

from gerund.commands.terminal_command import TerminalCommand


class InstallCommand:
    """
    This class is responsible for installing a package on a machine.

    Attributes:
        package (str): the package to be installed
        ip_address (Optional[str]): the ip address of the machine to install the package on
    """
    OK_STATUS: str = "Status: install ok installed"

    def __init__(self, package: str, ip_address: Optional[str] = None) -> None:
        """
        The constructor for the InstallCommand class.

        :param package: (str) the package to be installed
        :param ip_address: (Optional[str]) the ip address of the machine to install the package on
        """
        self.package: str = package
        self.ip_address: Optional[str] = ip_address

    def _check_outcome(self) -> bool:
        """
        Checks the outcome of the command to see if the package is installed.

        :return: (bool) True if the package is installed, False otherwise
        """
        command = TerminalCommand(command=f"dpkg -s {self.package} | grep Status", ip_address=self.ip_address)
        outcome = command.wait(capture_output=True)

        if len(outcome) == 0:
            return False
        if outcome[0] == self.OK_STATUS:
            return True
        return False

    def install_package(self) -> bool:
        """
        Installs the package on the machine.

        :return: (bool) True if the package is installed, False otherwise
        """
        if self._check_outcome() is True:
            print(f"Package {self.package} is already installed. Skipping installation.")
            return True
        command = TerminalCommand(command=f"sudo apt-get install {self.package} -y", ip_address=self.ip_address)

        counter = 5
        while counter > 0:
            print(f"Installing package {self.package}.")
            command.wait()
            if self._check_outcome() is True:
                print(f"Package {self.package} installed successfully.")
                return True
            print(f"Package {self.package} failed to install. Retrying in 3 seconds.")
            counter -= 1
            time.sleep(3)
        return False
