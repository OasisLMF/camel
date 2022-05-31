"""
This file defines the file that updates the status of a project and the entry point for the `cb-project-update` command.
"""
import argparse

from camel.basecamp.components.mapper import Mapper
from camel.basecamp.components.project import Project, Status
from camel.basecamp.components.user import User


def update(name: str, status: Status) -> None:
    """
    Updates the status of a project.

    Args:
        name: (str) the name of the project being updated with
        status: (Status) the status that the project is going to be updated to

    Returns: None
    """
    mapper: Mapper = Mapper()

    if mapper.in_camp is True:
        user: User = User.from_cache(file_path=mapper.users_path)
        existing_project = Project(name=name, file_path=mapper.projects_path)
        existing_project.data["LAST_INTERACTED_BY"] = user.name
        existing_project.update_status(status=status)
        existing_project.write()
        user.write()


def main() -> None:
    """
    Entry point for `cb-project-update` command which updates the status of a project.

    Returns: None
    """
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--name', action='store', type=str, required=True,
                               help="name of the project being updated")
    config_parser.add_argument('--status', action='store', type=str, required=True,
                               help="status to update the project to")
    args = config_parser.parse_args()
    update(name=args.name, status=args.status)


def api() -> None:
    pass
