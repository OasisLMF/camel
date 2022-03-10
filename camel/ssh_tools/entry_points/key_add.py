import argparse
from subprocess import Popen

from camel.storage.components.profile import Profile


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--key', action='store', type=str, required=True,
                             help="the path to the key being added")
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    file_name = args.key.split("/")[-1]
    key_name = file_name.split(".")[0]

    print(f"adding key: {key_name}")

    key_path = profile.keys_path + f"/{file_name}"

    copy_process = Popen(f"cp {args.key} {key_path}", shell=True)
    copy_process.wait()

    change_permissions = Popen(f"chmod 600 {key_path}", shell=True)
    change_permissions.wait()
    print(f"key {key_name} added, this key has to be referred to for SSH")
