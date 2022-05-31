"""
This file defines the entry point for the cml-storage-create command.
"""
import argparse

from camel.storage.components.profile_storage import LocalProfileVariablesStorage


def main() -> None:
    """
    Stores a value and key in the storage for the profile.

    :return: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the value being stored")
    args_parser.add_argument('--value', action='store', type=str, required=True,
                             help="the value being stored")

    args = args_parser.parse_args()

    storage = LocalProfileVariablesStorage()
    storage.add_variable(name=args.name, value=args.value)
    print(f"{args.name}: {args.value} stored")
