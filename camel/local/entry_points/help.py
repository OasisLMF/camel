"""
This file defines the cml-repo command.
"""
from termcolor import colored

from camel.storage.components.profile import Profile


def repo() -> None:
    """
    Prints out the available commands for the repo command.

    :return: None
    """
    Profile.print_out_profiles()
    print("\navailable commands:")
    print(colored("cml-repo-add => adds an local repo config to the current profile", 'yellow'))
    print(colored("cml-repo-update => updates a python env from a local repo", 'yellow'))
    print(colored("cml-repo-delete => deletes an local repo config to the current profile", 'yellow'))
    print(colored("cml-repo-get => gets all the locaL repos that can be updated", 'yellow'))
