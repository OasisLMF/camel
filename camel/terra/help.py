"""
This file defines the entry point for the cml-terra command printing out all of the available terra commands.
"""
from camel.storage.components.profile import Profile
from termcolor import colored


def main() -> None:
    try:
        current_profile = Profile.get_cached_profile().name
        print(f"\ncurrent profile: {current_profile}")
    except:
        print("\ncurrent profile: None")
    print("\navailable profiles:")
    for profile in Profile.get_profiles():
        print(profile)
    print("\navailable commands:")
    print(colored(f"cml-terra-apply => builds a terraform build based on the config file passed", 'yellow'))
    print(colored(f"cml-terra-destroy => destroys the terraform build in the config file", 'yellow'))
    print(colored(f"cml-terra-install => installs the terraform software to be used", 'yellow'))
    print(colored(f"cml-terra-all => gets all the automatically supported models and builds", 'yellow'))
