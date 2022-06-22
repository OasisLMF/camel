from camel.terra.components.variable_editor import VariableEditor
import os


class EditStatePositionAdapter:

    def __init__(self, build_path: str) -> None:
        self.build_path: str = build_path
        self.variable_editor = VariableEditor(data_directory=build_path)

    def update_state(self, s3_key: str) -> None:
        self.variable_editor.overwrite_variable(key="state_location", variable=s3_key)
        self.variable_editor.cache_main()
        self.variable_editor.write_main_data()

    def revert_main_back_to_initial_state(self) -> None:
        self.variable_editor.load_main()
