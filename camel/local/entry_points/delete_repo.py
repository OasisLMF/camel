"""
This file defines the entry point for cml-repo-delete.
"""
import argparse

from camel.local.components.local_repo_config import LocalRepoConfig
from camel.storage.components.profile import Profile


def main() -> None:
    """
    Deletes a local repo config to the profile.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = LocalRepoConfig(config_path=profile.configs_path + "/repo_config.yml")
    del config[args.name]
    config.write()
