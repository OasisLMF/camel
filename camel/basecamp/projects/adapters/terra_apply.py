"""
This file defines the adapters for interacting with the terra-apply processes.
"""
from typing import Optional

from camel.basecamp.components.mapper import Mapper as BasecampMapper
from camel.basecamp.components.project import Project
from camel.basecamp.components.project import Status as ProjectStatus
from camel.basecamp.components.user import User as BasecampUser
from camel.basecamp.projects.entry_points.create import create as create_project
from camel.basecamp.projects.entry_points.get import get as get_project


class TerraApplyProjectAdapter:
    """
    This class is responsible for managing the interactions with a project and a terraform build.

    Attributes:
        config: (dict) the data for the terraform build
        basecamp_map: (BasecampMapper) the mapping object to navigate around the basecamp
        user: (Optional[BasecampUser]) the user running the terraform command (None if not in a basecamp)
        in_basecamp: (bool) True if in a basecamp, False if not
        project: (Optional[Project]) project object if in a basecamp, None if not
        continue_building: (bool) True if conditions are appropiate to continue the terraform build
                                  (see self._define_continue_building_project)
    """
    def __init__(self, config: dict) -> None:
        """
        The constructor for the TerraApplyProjectAdapter class.

        Args:
            config: (dict) the config data for the terra build being run
        """
        self.config: dict = config
        self.basecamp_map: BasecampMapper = BasecampMapper()
        self.user: Optional[BasecampUser] = None
        self.in_basecamp: bool = self.basecamp_map.in_camp
        self.project: Optional[Project] = None
        self.continue_building: bool = True
        self._define_continue_building_project()
        self._extract_project()

    def _define_continue_building_project(self) -> None:
        """
        Extracts the data from the basecamp and user. If this can be extracted then self.user is populated. If
        the user is in a basecamp this function checks the last interacted by. If the last interacted with name is
        different to the self.user the user is asked if they want to continue the build. If no then
        self.continue_building is set to False.

        Returns: None
        """
        if self.in_basecamp is True:
            self.user = BasecampUser.from_cache(file_path=self.basecamp_map.users_path)
            project_name = self.config["location"].replace("/", "_")
            print(f"we are in the basecamp {self.basecamp_map.camp_name}")
            project = get_project(name=project_name)

            # build a new project
            if project is None:
                print(f"{project_name} project is not present. Creating "
                      f"{project_name} project basecamp {self.basecamp_map.camp_name}")
                create_project(name=project_name)

            else:

                if self.user.name != project.last_interacted_by:
                    print(
                        f"WARNING! the last user to interact with the {project_name} project is {project.last_interacted_by}")
                    continue_input = input("continue build?[y/N]: ")
                    if continue_input == "y":
                        project.data["LAST_INTERACTED_BY"] = self.user.name
                        project.write()
                    else:
                        self.continue_building = False

    def _extract_project(self) -> None:
        """
        Populates the self.project if user is in a basecamp.

        Returns: None
        """
        if self.in_basecamp is True:
            project_name = self.config["location"].replace("/", "_")
            self.project = get_project(name=project_name)
        else:
            self.project = None

    def _update_status(self, status: ProjectStatus) -> None:
        """
        Updates the status of the project writing it to the project JSON file.

        Args:
            status: (ProjectStatus) the status to be updated

        Returns: None
        """
        if self.project is not None:
            self.project.update_status(status=status)
            self.project.update_last_interacted_by(user_name=self.user.name)
            self.project.write()

    def start_build(self) -> None:
        """
        Updates the status of the project to CREATING.

        Returns: None
        """
        self._update_status(status=ProjectStatus.CREATING)

    def finish_build(self) -> None:
        """
        Updates the status of the project to RUNNING.

        Returns: None
        """
        self._update_status(status=ProjectStatus.RUNNING)

    def destroy_build(self) -> None:
        """
        Updates the status of the project to DESTROYING.

        Returns: None
        """
        self._update_status(status=ProjectStatus.DESTROYING)

    def declare_destroyed(self) -> None:
        """
        Updates the status of the project to DESTROYED.

        Returns: None
        """
        self._update_status(status=ProjectStatus.DESTROYED)
