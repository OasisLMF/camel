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
    print(colored(f"cml-ssh-add => adds an ssh config to the current profile", 'yellow'))
    print(colored(f"cml-ssh-delete => deletes an ssh config", 'yellow'))
    print(colored(f"cml-ssh-get => lists all ssh configs", 'yellow'))
    print(colored(f"cml-ssh-enter => connects to the server in the SSH config selected", 'yellow'))
