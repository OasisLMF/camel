import argparse
from subprocess import Popen

from camel.ssh_tools.components.ssh_config import SshConfig
from camel.storage.components.profile import Profile


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True)
    args_parser.add_argument('--ip', action='store', type=str, required=True)
    args_parser.add_argument('--vpn', action='store', type=bool, required=False)
    args_parser.add_argument('--key', action='store', type=str, required=True)
    args_parser.add_argument('--username', action='store', type=str, required=True)
    args = args_parser.parse_args()

    profile = Profile.get_cached_profile()

    config = SshConfig(config_path=profile.configs_path + "/ssh_config.yml")

    key_name = args.key.split("/")[-1]

    key_path = profile.keys_path + f"/{key_name}"

    copy_process = Popen(f"cp {args.key} {key_path}", shell=True)
    copy_process.wait()

    change_permissions = Popen(f"chmod 600 {key_path}", shell=True)
    change_permissions.wait()

    config.add_ssh_config(name=args.name, ip_address=args.ip_address,
                          vpn=args.vpn, key=args.key, username=args.username)
    config.write()
