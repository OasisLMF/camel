"""
This file defines the step that prints out a statement.
"""
from camel.terra.steps.base import Step


class PrintoutStep(Step):
    """
    This class is responsible for printing out a statement in the steps process.

    Attributes:
        string: (str) the string to be printed out
    """
    def __init__(self, string: str) -> None:
        """
        The constructor for the PrintoutStep class.

        Args:
            string: (str) the string to be printed out
        """
        self.string: str = string

    def run(self) -> None:
        """
        Prints out the self.string to the console.

        Returns: None
        """
        print(self.string)
