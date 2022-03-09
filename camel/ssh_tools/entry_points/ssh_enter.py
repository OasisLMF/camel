import argparse

from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile
from typing import Dict, Union
from subprocess import Popen


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True)
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = SshConfig(config_path=profile.configs_path + "/ssh_config.yml")

    ssh_profile: Dict[str, Union[str, bool]] = config[args.name]

    if ssh_profile["vpn"] is True:
        print("spinning up VPN")

    key_name = ssh_profile["key"]
    username = ssh_profile["username"]

    key_path = profile.keys_path + f"/{key_name}"

    ssh_process = Popen(f"ssh ", shell=True)
