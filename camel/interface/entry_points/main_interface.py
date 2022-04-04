"""
This file defines the main display entry point for the cml command telling the user the available options.
"""
from termcolor import colored

from camel.interface.components.camel_logo import print_camel_image
from camel.interface.components.oasis_logo import print_logo_image
from camel.storage.components.profile import Profile


def main()-> None:
    """
    Prints out the Camel and OASIS logos, the current profile, the available profiles, and the available options.

    :returns: None
    """
    print_camel_image()
    print_logo_image()
    Profile.print_out_profiles()
    print("\navailable commands:")
    print(colored(f"cml-profile => manages the profile", 'yellow'))
    print(colored(f"cml-storage => manages the storage of variables for a profile to be referenced in other processes", 'yellow'))
    print(colored(f"cml-ssh => manages ssh configurations", 'yellow'))
    print(colored(f"cml-terra => manages terraform builds", 'yellow'))
    print(colored(f"cml-repo => manages local repo operations", 'yellow'))
    print(colored(f"cml-tconfig => manages terraform build configs", 'yellow'))
