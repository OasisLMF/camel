"""
This file defines the entry point for the cb-create command.
"""
from camel.basecamp.components.mapper import Mapper
import argparse


def main() -> None:
    """
    Creates a new basecamp in the current working directory.

    Returns: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--name', action='store', type=str, required=True,
                               help="name of the basecamp being created")
    args = config_parser.parse_args()
    mapper = Mapper()
    if mapper.in_camp is False:
        print(f"creating basecamp called: {args.name}")
        mapper.create(name=args.name)
        print(f"basecamp called: {args.name} created")
