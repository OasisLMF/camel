"""
This file defines the main display entry point for the cml command telling the user the available options.
"""
from termcolor import colored

from camel.interface.components.tent_logo import print_tent_image
from camel.interface.components.oasis_logo import print_logo_image
from camel.basecamp.components.mapper import Mapper


def main() -> None:
    """
    Prints out the Camel and OASIS logos, the current profile, the available profiles, and the available options.

    :returns: None
    """
    print_tent_image()
    print_logo_image()
    print(f"the current base camp is: {Mapper().camp_name}")
    print("\navailable commands:")
    print(colored(f"cb-project => manages the running projects in the current camp", 'yellow'))
    print(colored(f"cb-user => manages the users in the current camp", 'yellow'))
    print(colored(f"cb-create => creates a new basecamp in the current working directory", 'yellow'))
