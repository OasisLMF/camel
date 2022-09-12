"""
This file defines the cml-ssh command.
"""
from termcolor import colored

from camel.storage.components.profile import Profile


def main() -> None:
    """
    Printouts the commands available for the ssh options.

    Returns: None
    """
    Profile.print_out_profiles()
    print("\navailable commands:")
    print(colored("cml-ssh-add => adds an ssh config to the current profile", 'yellow'))
    print(colored("cml-ssh-delete => deletes an ssh config", 'yellow'))
    print(colored("cml-ssh-get => lists all ssh configs", 'yellow'))
    print(colored("cml-ssh-enter => connects to the server in the SSH config selected", 'yellow'))
    print(colored("\ncml-key-add => adds a key file for the current profile", 'yellow'))
    print(colored("cml-key-delete => deletes a key file for the current profile", 'yellow'))
