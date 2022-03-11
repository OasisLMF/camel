"""
This file defines the cml-repo command.
"""
from termcolor import colored

from camel.storage.components.profile import Profile


def repo() -> None:
    Profile.print_out_profiles()
    print("\navailable commands:")
    print(colored(f"cml-repo-add => adds an local repo config to the current profile", 'yellow'))
    print(colored(f"cml-repo-update => updates a python env from a local repo", 'yellow'))
    print(colored(f"cml-repo-delete => deletes an local repo config to the current profile", 'yellow'))
