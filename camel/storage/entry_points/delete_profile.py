"""
This file defines the entry point for the cml-profile-delete command.
"""
import argparse
import os

from camel.storage.components.profile import Profile


def main() -> None:
    """
    Deletes a profile from the camel storage with everything associated with the profile.

    :return: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the profile being deleted")
    args = args_parser.parse_args()

    print(f"deleting profile: {args.name}")
    new_profile = Profile(name=args.name)
    if not os.path.isdir(new_profile.profile_base_path):
        raise ValueError(f"profile with the name {new_profile.name} does not exist")
    new_profile.delete_profile()
    print("profile deleted")
