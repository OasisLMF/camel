import argparse
import os

from camel.storage.components.profile import Profile


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=False)
    args = args_parser.parse_args()

    print(f"switching to profile: {args.name}")
    new_profile = Profile(name=args.name)
    if not os.path.isdir(new_profile.profile_base_path):
        raise ValueError(f"profile with the name {new_profile.name} does not exist")
    new_profile.delete_profile()
    print("profile deleted")
