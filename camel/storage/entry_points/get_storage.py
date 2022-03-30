from camel.storage.components.profile_storage import LocalProfileVariablesStorage


def main():
    storage = LocalProfileVariablesStorage()

    for key in storage.keys():
        print(f"{key}: {storage[key]}")
