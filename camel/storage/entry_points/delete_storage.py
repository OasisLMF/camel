import argparse

from camel.storage.components.profile_storage import LocalProfileVariablesStorage


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the value being stored")

    args = args_parser.parse_args()

    storage = LocalProfileVariablesStorage()
    storage.delete_value(name=args.name)
    print(f"{args.name} deleted")
