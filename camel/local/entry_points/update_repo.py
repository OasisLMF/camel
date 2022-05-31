"""
This file defines the entry point for cml-repo-update command.
"""
import argparse
from subprocess import Popen

from camel.local.components.local_repo_config import LocalRepoConfig
from camel.storage.components.profile import Profile


def main() -> None:
    """
    Updates a local python environment from a local repo config to the profile.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = LocalRepoConfig(config_path=profile.configs_path + "/repo_config.yml")

    local_repo_path = config[args.name]["local_path"]

    uninstall_process = Popen(f"pip uninstall {args.name} -y", shell=True)
    uninstall_process.wait()

    re_install_process = Popen(f"pip install {local_repo_path}", shell=True)
    re_install_process.wait()
