"""
This file defines the entry point for cml-repo-add.
"""
import argparse

from camel.local.components.local_repo_config import LocalRepoConfig
from camel.storage.components.profile import Profile


def main() -> None:
    """
    Adds a local repo config to the profile.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args_parser.add_argument('--path', action='store', type=str, required=True,
                             help="the absolute path to the repo being stashed")
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = LocalRepoConfig(config_path=profile.configs_path + "/repo_config.yml")

    config.add_repo_config(name=args.name, local_path=args.path)
    config.write()
