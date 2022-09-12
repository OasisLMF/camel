"""
Defines the help functions for the cml-model and cml-storage commands.
"""
from camel.storage.components.profile import Profile
from termcolor import colored


def main() -> None:
    Profile.print_out_profiles()
    print("\navailable commands:")
    print(colored("cml-model-build => builds a new model template to be run", 'yellow'))
    print(colored("cml-model-load => loads a model into the camel module", 'yellow'))
    print(colored("cml-model-get => prints out all the models available", 'yellow'))
    print(colored("cml-model-delete => deletes a model", 'yellow'))
