"""
This file defines the step that executes another step based on a conditional comparison of variables.
"""
from enum import Enum

from gerund.components.variable import Variable

from camel.terra.steps.base import Step


class Operator(Enum):
    """
    This Enum defines the type of comparisons supported.
    """
    EQUALS = "=="
    NOT_EQUALS = "!="


class ConditionalStep(Step):
    """
    This class is responsible for checking a condition and running a step if that condition is met.

    Attributes:
        operator: (str) the type of operator that is being referenced when comparing variable and value
        variable:(Variable) the variable that is being referenced
        value: (str) the value that the variable is going to be compared against
        step: (Step) the step that is going to be executed if the condition is met
    """

    def __init__(self, operator: str, variable: Variable, value: str, step: Step) -> None:
        """
        The constructor for the ConditionalStep.

        Args:
            operator: (str) the type of operator that is being referenced when comparing variable and value
            variable:(Variable) the variable that is being referenced
            value: (str) the value that the variable is going to be compared against
            step: (Step) the step that is going to be executed if the condition is met
        """
        self.operator: Operator = Operator(operator)
        self.step: Step = step
        self.variable: Variable = variable
        self.value: str = value

    def run(self) -> None:
        """
        Runs the self.step if the condition is met.

        Returns: None
        """
        if self.result is True:
            self.step.run()

    @property
    def result(self) -> bool:
        if self.operator == Operator.EQUALS:
            if str(self.variable) == self.value:
                return True
        elif self.operator == Operator.NOT_EQUALS:
            if str(self.variable) != self.value:
                return True
        return False
