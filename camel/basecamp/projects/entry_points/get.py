import argparse

from camel.basecamp.components.mapper import Mapper
from camel.basecamp.components.project import Project


def get(name: str) -> dict:
    mapper: Mapper = Mapper()

    if mapper.in_camp is True:
        existing_project = Project(name=name, file_path=mapper.projects_path)
        return existing_project.schema
    return dict()


def main() -> None:
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--name', action='store', type=str, required=True,
                               help="name of the project being created")
    args = config_parser.parse_args()
    print(get(name=args.name))


def api() -> None:
    pass
