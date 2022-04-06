from camel.terra.steps.base import Step


class PrintoutStep(Step):

    def __init__(self, string: str) -> None:
        self.string: str = string

    def run(self) -> None:
        print(self.string)