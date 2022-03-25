import argparse
import os
import shutil

from camel.storage.components.profile import Profile


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="name the config is going to be stored under")

    args = args_parser.parse_args()

    print(f"exporting config: {args.name}")

    profile = Profile.get_cached_profile()

    config_base_path = f"{profile.terra_builds_path}/{args.name}.yml"

    if not os.path.isdir(config_base_path):
        raise ValueError(f"terraform config with the name {args.name} does not exist")

    shutil.copyfile(config_base_path, f"{os.getcwd()}/{args.name}.yml")
    print("config exported")
