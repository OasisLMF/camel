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
    print(colored(f"cml-profile-create => creates a new profile", 'yellow'))
    print(colored(f"cml-profile-switch => switches the current profile to a new one", 'yellow'))
    print(colored(f"cml-profile-delete => deletes a profile wiping all data associated with the profile", 'yellow'))
