from enum import Enum
from typing import Optional

from camel.terra.steps.base import Step


class Operator(Enum):
    EQUALS = "=="


class ConditionalStep(Step):

    def __init__(self, operator: str, variable: str, value: str,  step: Step, ip_address: Optional[str] = None) -> None:
        self.operator: Operator = Operator(operator)
        self.step: Step = step
        self.variable: str = variable
        self.value: str = value
        self.ip_address: Optional[str] = ip_address

    def _process_inputs(self, input_data: dict, terraform_dict: dict) -> None:
        pass

    def run(self) -> None:
        pass
