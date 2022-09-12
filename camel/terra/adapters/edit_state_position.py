"""
This file defines the adapter that temporarily edits where the state is stored for the terraform build.
"""
from camel.terra.components.variable_editor import VariableEditor


class EditStatePositionAdapter:

    def __init__(self, build_path: str) -> None:
        """
        The constructor for the EditStatePositionAdapter class.

        Args:
            build_path: (str) the path to where the terraform files for the build are located
        """
        self.build_path: str = build_path
        self.variable_editor = VariableEditor(data_directory=build_path)

    def update_state(self, s3_key: str) -> None:
        """
        Overwrites the "state_location" key in the main.tf file for the build and caches the original main.tf to be
        reverted again.

        Args:
            s3_key: (str) the new variable for the state_location to over overwritten with

        Returns: None
        """
        self.variable_editor.overwrite_variable(key="state_location", variable=s3_key)
        self.variable_editor.cache_main()
        self.variable_editor.write_main_data()

    def revert_main_back_to_initial_state(self) -> None:
        """
        Reverts the main.tf in the build back to its original state.

        Returns: None
        """
        self.variable_editor.load_main()
