"""
This file defines the entry point for cml-storage-get command.
"""
from camel.storage.components.profile_storage import LocalProfileVariablesStorage


def main() -> None:
    """
    Gets all the keys and values associated with the profile storage and prints it out.

    :return: None
    """
    storage = LocalProfileVariablesStorage()

    for key in storage.keys():
        print(f"{key}: {storage[key]}")
