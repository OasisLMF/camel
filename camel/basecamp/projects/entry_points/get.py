"""
This file defines the functions that get the data around a single project and the entry point for `cb-project-get`
command.
"""
import argparse
from typing import Optional

from camel.basecamp.components.mapper import Mapper
from camel.basecamp.components.project import Project


def get(name: str) -> Optional[Project]:
    """
    Gets the data for a project.

    Args:
        name: (str) the name of the project being called

    Returns: (Optional[Project]) the data concerning the project being called
    """
    mapper: Mapper = Mapper()

    if mapper.in_camp is True and name in mapper.available_projects:
        existing_project = Project(name=name, file_path=mapper.projects_path)
        return existing_project
    return None


def main() -> None:
    """
    The entry point that gets the data for the project.

    Returns: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--name', action='store', type=str, required=True,
                               help="name of the project being created")
    args = config_parser.parse_args()
    project = get(name=args.name)
    if project is None:
        print(dict())
    else:
        print(project.schema)


def api() -> None:
    pass
