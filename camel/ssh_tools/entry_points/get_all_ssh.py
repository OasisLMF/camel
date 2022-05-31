"""
This file defines the entry point for the cml-ssh-get command.
"""
from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile


def main() -> None:
    """
    Gets all the available SSH configs for the profile.

    Returns: None
    """
    profile = Profile.get_cached_profile()

    config = SshConfig(config_path=profile.configs_path + "/ssh_config.yml")
    print("available ssh configs:")

    for key in config.keys():
        print(key)
