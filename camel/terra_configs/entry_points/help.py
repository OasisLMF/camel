from camel.storage.components.profile import Profile
from termcolor import colored


def main():
    try:
        current_profile = Profile.get_cached_profile().name
        print(f"\ncurrent profile: {current_profile}")
    except:
        print("\ncurrent profile: None")
    print("\navailable profiles:")
    for profile in Profile.get_profiles():
        print(profile)
    print("\navailable commands:")
    print(colored(f"cml-tconfig-get => gets all the terraform configs available", 'yellow'))
    print(colored(f"cml-tconfig-import => imports a terraform config file to be saved", 'yellow'))
    print(colored(f"cml-tconfig-export => imports a terraform config file to the current location", 'yellow'))
    print(colored(f"cml-tconfig-delete => deletes a terraform config file to the current location", 'yellow'))
