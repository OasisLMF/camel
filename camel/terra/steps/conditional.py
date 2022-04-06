from enum import Enum

from camel.terra.steps.base import Step
from camel.terra.components.variable import Variable


class Operator(Enum):
    EQUALS = "=="


class ConditionalStep(Step):

    def __init__(self, operator: str, variable: Variable, value: str,  step: Step) -> None:
        self.operator: Operator = Operator(operator)
        self.step: Step = step
        self.variable: Variable = variable
        self.value: str = value

    def run(self) -> None:
        if self.result is True:
            self.step.run()

    @property
    def result(self) -> bool:
        if self.operator == Operator.EQUALS:
            if str(self.variable) == self.value:
                return True
        return False
