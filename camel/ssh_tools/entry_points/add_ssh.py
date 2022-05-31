"""
This file defines the entry point for cml-ssh-add.
"""
import argparse

from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile


def main() -> None:
    """
    Adds an SSH config to the profile.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args_parser.add_argument('--ip', action='store', type=str, required=True,
                             help="the ip address of the server the SSH is for")
    args_parser.add_argument('--vpn', action='store', type=bool, required=True,
                             help="if the SSH requires VPN or not")
    args_parser.add_argument('--key', action='store', type=str, required=True,
                             help="the name of the key being used for the SSH (including extension)")
    args_parser.add_argument('--username', action='store', type=str, required=True,
                             help="the username of the SSH for the server")
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = SshConfig(config_path=profile.configs_path + "/ssh_config.yml")

    config.add_ssh_config(name=args.name, ip_address=args.ip,
                          vpn=args.vpn, key=args.key, username=args.username)
    config.write()
