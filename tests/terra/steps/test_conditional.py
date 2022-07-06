"""
This file tests the Variable displaying how the object can be used in code on the last test case.
"""
from unittest import main, TestCase
from unittest.mock import MagicMock

from camel.terra.steps.conditional import ConditionalStep, Operator, Variable


class ConditionalStepVariableTest(TestCase):

    def setUp(self) -> None:
        self.mock_step = MagicMock()
        self.mock_step.__str__.return_value = "test"
        self.variable = Variable(name="test")
        self.test = ConditionalStep(operator="==", variable=self.variable, value="test", step=self.mock_step)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(Operator("=="), self.test.operator)
        self.assertEqual(self.mock_step, self.test.step)
        self.assertEqual(self.variable, self.test.variable)
        self.assertEqual("test", self.test.value)

    def test_result(self):
        self.assertEqual(True, self.test.result)
        self.test.value = "should fail"
        self.assertEqual(False, self.test.result)

    def test_run(self):
        self.test.run()
        self.mock_step.run.assert_called_once_with()

        self.test.value = "testing"
        self.test.run()
        self.mock_step.run.assert_called_once_with()


if __name__ == "__main__":
    main()
