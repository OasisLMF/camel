"""
This file defines the entry point for the cml-ssh-delete command.
"""
import argparse

from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile


def main() -> None:
    """
    Deletes an SSH config for a profile.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the SSH config to be deleted")
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = SshConfig(config_path=profile.configs_path + "/ssh_config.yml")
    del config[args.name]
    config.write()
