"""
This file defines the functions that get the data around getting all projects and the entry point for `cb-project-all`
command.
"""
from typing import List

from camel.basecamp.components.mapper import Mapper


def get_all() -> List[str]:
    """
    Gets the data for all projects.

    Returns: (List[str]) all the available projects
    """
    mapper: Mapper = Mapper()
    return mapper.available_projects


def main() -> None:
    """
    The entry point that gets the data for the available projects.

    Returns: None
    """
    projects = get_all()
    print("available projects:")

    for project in projects:
        print(project)


def api() -> None:
    pass
