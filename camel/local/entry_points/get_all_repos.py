"""
This file defines the entry point for the cml-repo-get command.
"""
from camel.local.components.local_repo_config import LocalRepoConfig
from camel.storage.components.profile import Profile


def main() -> None:
    """
    Gets all the available SSH configs for the profile.

    Returns: None
    """
    profile = Profile.get_cached_profile()

    config = LocalRepoConfig(config_path=profile.configs_path + "/repo_config.yml")
    print("available local repos:")

    for key in config.keys():
        print(key)
