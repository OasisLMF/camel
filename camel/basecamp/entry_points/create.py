from camel.basecamp.components.mapper import Mapper
import argparse


def main() -> None:
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--name', action='store', type=str, required=True,
                               help="name of the basecamp being created")
    args = config_parser.parse_args()
    mapper = Mapper()
    if mapper.in_camp is False:
        mapper.create(name=args.name)
