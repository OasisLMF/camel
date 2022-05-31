"""
This file defines the entry point for the cml-profile-export command.
"""
import argparse
import os
from subprocess import Popen

from camel.storage.components.profile import Profile


def main() -> None:
    """
    Exports a file to the current working directory that contains everything associated with the profile under the
    name of the profile.

    :return: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the profile being exported")
    args = args_parser.parse_args()

    print(f"exporting profile: {args.name}")
    new_profile = Profile(name=args.name)

    if not os.path.isdir(new_profile.profile_base_path):
        raise ValueError(f"profile with the name {new_profile.name} does not exist")

    source_folder = new_profile.profile_base_path
    destination_folder = f"{os.getcwd()}/{args.name}/"

    copy_process = Popen(f"cp -r {source_folder} {destination_folder}", shell=True)
    copy_process.wait()
    print("profile exported")
