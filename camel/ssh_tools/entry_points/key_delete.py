"""
This file defines the entry point for the cml-key-add command.
"""
import argparse
from subprocess import Popen

from camel.storage.components.profile import Profile


def main() -> None:
    """
    Adds a key file for the profile.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--key', action='store', type=str, required=True,
                             help="the path to the key being added")
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    file_name = args.key.split("/")[-1]
    key_name = file_name.split(".")[0]

    print(f"deleting key: {key_name}")

    key_path = profile.keys_path + f"/{file_name}"

    change_permissions = Popen(f"rm -f {key_path}", shell=True)
    change_permissions.wait()

    delete_key = Popen(f"ssh-add -D {key_path}", shell=True)
    delete_key.wait()
    print(f"key {key_name} added, this key has to be referred to for SSH")
