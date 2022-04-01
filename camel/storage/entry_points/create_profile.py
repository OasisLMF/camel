"""
This file defines the entry point for cml-repo-create.
"""
import argparse
import os

from camel.storage.components.profile import Profile


def main() -> None:
    """
    Creates a repo to be referenced for updating code based off as long as the repo home directory has a setup.py
    file.

    :return: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the profile being created")
    args = args_parser.parse_args()

    print(f"creating profile with name: {args.name}")
    new_profile = Profile(name=args.name)
    if os.path.isdir(new_profile.profile_base_path):
        raise ValueError(f"profile with the name {new_profile.name} already exists")
    new_profile.create_profile()
    print("profile created")

