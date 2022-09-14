from unittest import main, TestCase

from camel.terra.steps.run_command_on_server import RunCommandOnServerStep
from gerund.components.variable_map import VariableMap, Singleton


class TestRunCommandOnServerStep(TestCase):

    def setUp(self) -> None:
        self.variable_map = VariableMap()

    def tearDown(self) -> None:
        Singleton._instances = {}

    def test___init__(self):
        pass



if __name__ == "__main__":
    main()
