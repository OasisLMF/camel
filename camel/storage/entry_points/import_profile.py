"""
This file defines the entry point for the cml-profile-import command.
"""
import argparse
import os
from subprocess import Popen

from camel.storage.components.profile import Profile


def main() -> None:
    """
    Imports a file that holds all the data around a profile. The profile name is the name of the file.

    :return: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the profile being imported")
    args = args_parser.parse_args()

    print(f"exporting profile: {args.name}")
    new_profile = Profile(name=args.name)

    if os.path.isdir(new_profile.profile_base_path):
        raise ValueError(f"profile with the name {new_profile.name} already exists")

    source_folder = new_profile.profile_base_path
    destination_folder = f"{os.getcwd()}/{args.name}/"

    copy_process = Popen(f"cp -r {destination_folder} {source_folder}", shell=True)
    copy_process.wait()
    print("profile imported")
