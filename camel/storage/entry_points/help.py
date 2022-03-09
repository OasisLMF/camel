from camel.storage.components.profile import Profile
from termcolor import colored


def profile():
    try:
        current_profile = Profile.get_cached_profile().name
        print(f"\ncurrent profile: {current_profile}")
    except:
        print("\ncurrent profile: None")
    print("\navailable profiles:")
    for profile in Profile.get_profiles():
        print(profile)
    print("\navailable commands:")
    print(colored(f"cml-profile-create => creates a new profile: args: --name: the name of the file involved", 'yellow'))
    print(colored(f"cml-profile-switch => creates a new profile: args: --name: the name of the file involved", 'yellow'))
    print(colored(f"cml-profile-delete => creates a new profile: args: --name: the name of the file involved", 'yellow'))
