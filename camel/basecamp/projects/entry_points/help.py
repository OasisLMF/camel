"""
This file defines the main display entry point for the cb-project command telling the user the available options.
"""
from termcolor import colored

from camel.interface.components.oasis_logo import print_logo_image
from camel.basecamp.components.mapper import Mapper


def main() -> None:
    """
    Prints out the available options.

    :returns: None
    """
    camp_name = Mapper().camp_name
    print_logo_image()
    print(f"the current base camp is: {camp_name}")
    print("\navailable commands:")
    print(colored(f"cb-project-create => creates a new project in the {camp_name} basecamp", 'yellow'))
    print(colored(f"cb-project-update => updates the status of a project in the {camp_name} basecamp", 'yellow'))
    print(colored(f"cb-project-get => gets a specific project in the {camp_name} basecamp", 'yellow'))
    print(colored(f"cb-project-all => gets all the projects in the {camp_name} basecamp", 'yellow'))
