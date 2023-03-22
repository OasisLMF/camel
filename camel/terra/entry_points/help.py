"""
This file defines the entry point for the cml-terra command printing out all of the available terra commands.
"""
from termcolor import colored

from camel.storage.components.profile import Profile


def main() -> None:
    try:
        current_profile = Profile.get_cached_profile().name
        print(f"\ncurrent profile: {current_profile}")
    except FileNotFoundError:
        print("\ncurrent profile: None")
    print("\navailable profiles:")
    for profile in Profile.get_profiles():
        print(profile)
    print("\navailable commands:")
    print(colored("cml-terra-apply => builds a terraform build based on the config file passed", 'yellow'))
    print(colored("cml-terra-destroy => destroys the terraform build in the config file", 'yellow'))
    print(colored("cml-terra-install => installs the terraform software to be used", 'yellow'))
    print(colored("cml-terra-all => gets all the automatically supported models and builds", 'yellow'))
    print(colored("cml-terra-get => gets all the running EC2 instances for a specific region", 'yellow'))
