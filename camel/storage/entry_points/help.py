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
    print(colored(f"cml-profile-export => exports a profile into the current directory", 'yellow'))
    print(colored(f"cml-profile-import => imports a profile from the current directory", 'yellow'))


def storage():
    try:
        current_profile = Profile.get_cached_profile().name
        print(f"\ncurrent profile: {current_profile}")
    except:
        print("\ncurrent profile: None")
    print("\navailable profiles:")
    for profile in Profile.get_profiles():
        print(profile)
    print("\navailable commands:")
    print(colored(f"cml-storage-create => stores a new variable for the local storage for the current profile", 'yellow'))
    print(colored(f"cml-storage-delete => deletes a variable in the storage for the current profile", 'yellow'))
    print(colored(f"cml-storage-get => gets all the stored variables for the current profile", 'yellow'))
