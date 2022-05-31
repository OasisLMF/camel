"""
This file defines the function that creates a project for basecamp and the entry point for the cb-project-create
command.
"""
import argparse

from camel.basecamp.components.mapper import Mapper
from camel.basecamp.components.project import Project, Status
from camel.basecamp.components.user import User


def create(name: str) -> None:
    """
    Creates a new basecamp project in the current basecamp.

    Args:
        name: (str) the name of the project being created

    Returns: None
    """
    mapper: Mapper = Mapper()

    if mapper.in_camp is True:
        user: User = User.from_cache(file_path=mapper.users_path)
        new_project = Project(name=name, file_path=mapper.projects_path)
        new_project.data["NAME"] = name
        new_project.data["CREATED_BY"] = user.name
        new_project.data["LAST_INTERACTED_BY"] = user.name
        new_project.update_status(status=Status.CREATING)
        new_project.write()
        user.write()


def main() -> None:
    """
    Creates a basecamp project in the current basecamp.

    Returns: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--name', action='store', type=str, required=True,
                               help="name of the project being created")
    args = config_parser.parse_args()
    create(name=args.name)


def api() -> None:
    pass
