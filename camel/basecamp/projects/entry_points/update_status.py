import argparse

from camel.basecamp.components.mapper import Mapper
from camel.basecamp.components.project import Project, Status
from camel.basecamp.components.user import User


def update(name: str, status: Status) -> None:
    mapper: Mapper = Mapper()

    if mapper.in_camp is True:
        user: User = User.from_cache(file_path=mapper.users_path)
        existing_project = Project(name=name, file_path=mapper.projects_path)
        existing_project.data["LAST_INTERACTED_BY"] = user.name
        existing_project.update_status(status=status)
        existing_project.write()
        user.write()


def main() -> None:
    config_parser = argparse.ArgumentParser()
    config_parser.add_argument('--name', action='store', type=str, required=True,
                               help="name of the project being updated")
    config_parser.add_argument('--status', action='store', type=str, required=True,
                               help="status to update the project to")
    args = config_parser.parse_args()
    update(name=args.name, status=args.status)


def api() -> None:
    pass
