"""
This file performs tests for loading and saving the main.tf file in a terraform build when updating certain
variables.
"""
from unittest import TestCase, main
import os

from camel.terra.components.variable_editor import VariableEditor


class VariableEditorTest(TestCase):

    def setUp(self) -> None:
        self.meta_file_path = os.path.realpath(__file__).replace("test_variable_editor.py", "meta_data/")
        self.test = VariableEditor(data_directory=self.meta_file_path)

    def tearDown(self) -> None:
        pass

    def test_overwrite_and_write(self):
        # overwrite a variable in the main data
        self.test.overwrite_variable(key="state_location", variable="some_value")

        # switch the initial main.tf file to a cache.tf file
        self.test.cache_main()

        # write the new updated data to main.tf
        self.test.write_main_data()

        self.test.wipe_cache()

        # open the expected data file
        with open(self.meta_file_path + "expected_outcome.tf", "r") as file:
            expected_data = file.read()

        # check to see if the new written data is the same as the expected data
        self.assertEqual(expected_data, self.test.main_data)

        # clean up after test
        os.remove(self.meta_file_path + "main.tf")
        self.test.load_main()


if __name__ == "__main__":
    main()
