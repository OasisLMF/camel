import argparse

from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True)
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = SshConfig(config_path=profile.configs_path + "/ssh_config.yml")
    del config[args.name]
    config.write()
