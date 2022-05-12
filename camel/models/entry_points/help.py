"""
Defines the help functions for the cml-model and cml-storage commands.
"""
from camel.storage.components.profile import Profile
from termcolor import colored


def main() -> None:
    Profile.print_out_profiles()
    print("\navailable commands:")
    print(colored(f"cml-model-build => builds a new model template to be run", 'yellow'))
    print(colored(f"cml-model-load => loads a model into the camel module", 'yellow'))
