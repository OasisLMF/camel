"""
This file defines the entry point for the cml-tconfig-delete command
"""
import argparse
import os

from camel.storage.components.profile import Profile


def main() -> None:
    """
    Deletes a terraform config file associated with the current profile.

    :return: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the terraform config to be deleted")

    args = args_parser.parse_args()

    print(f"deleting config: {args.name}")

    profile = Profile.get_cached_profile()

    config_base_path = f"{profile.terra_builds_path}/{args.name}.yml"

    if not os.path.exists(config_base_path):
        raise ValueError(f"terraform config with the name {args.name} does not exist")

    os.remove(config_base_path)
    print("config deleted")
