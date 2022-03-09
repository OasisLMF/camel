from camel.interface.components.camel_logo import print_camel_image
from camel.interface.components.oasis_logo import print_logo_image
from camel.storage.components.profile import Profile
from termcolor import colored


def main():
    print_camel_image()
    print_logo_image()
    try:
        current_profile = Profile.get_cached_profile().name
        print(f"current profile: {current_profile}")
    except:
        print("current profile: None")
    print("available profiles:")
    for profile in Profile.get_profiles():
        print(profile)
    print("available commands:")
    print(colored(f"cml-profile => manages the profile", 'yellow'))
    print(colored(f"cml-ssh => manages ssh configurations", 'yellow'))
    print(colored(f"cml-terra => manages terraform builds", 'yellow'))
