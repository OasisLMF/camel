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
    print(colored(f"cml-ssh-add => adds an ssh config to the current profile", 'yellow'))
    print(colored(f"cml-ssh-delete => deletes an ssh config", 'yellow'))
    print(colored(f"cml-ssh-get => lists all ssh configs", 'yellow'))
    print(colored(f"cml-ssh-enter => connects to the server in the SSH config selected", 'yellow'))
    print(colored(f"\ncml-key-add => adds a key file for the current profile", 'yellow'))
    print(colored(f"cml-key-delete => deletes a key file for the current profile", 'yellow'))
