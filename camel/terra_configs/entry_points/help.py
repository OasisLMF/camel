"""
This file defines the entry point for the cml-tconfig command.
"""
from camel.storage.components.profile import Profile
from termcolor import colored


def main() -> None:
    """
    Prints out the available commands for the terraform configuration files.

    :return: None
    """
    Profile.print_out_profiles()
    print("\navailable commands:")
    print(colored("cml-tconfig-get => gets all the terraform configs available", 'yellow'))
    print(colored("cml-tconfig-import => imports a terraform config file to be saved", 'yellow'))
    print(colored("cml-tconfig-export => imports a terraform config file to the current location", 'yellow'))
    print(colored("cml-tconfig-delete => deletes a terraform config file to the current location", 'yellow'))
