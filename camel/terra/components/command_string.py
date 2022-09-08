"""
This file defines the class that processes a command string with variables if needed
"""
import re
from typing import List

from camel.terra.components.variable import Variable


class CommandString:
    """
    This class is responsible for handling a command string and processing variables inside it.

    Attributes:
        command (str): the command that is going to be processed
        command_processed (bool): if True the command will not get processed again as the command is already updated.
    """
    def __init__(self, command: str) -> None:
        """
        The constructor for the CommandString class.

        Args:
            command: (str) the command that is going to be processed
        """
        self.command: str = command
        self.command_processed: bool = False

    def _extract_variables(self) -> List[str]:
        """
        Extracts the variables from the self.command attribute.

        Returns: (List[str]) the list of variables that were inserted into the command
        """
        without_parens = re.sub('\(.+?\)', '', self.command)
        return re.findall('{(.+?)}', without_parens)

    def _replace_with_variable(self, variable_string: str) -> None:
        """
        Updates the command with the value of the special variable.

        Args:
            variable_string: (str) the name of the variable where we are going to get the value for

        Returns: None
        """
        input_var = str(Variable(name=variable_string))
        input_var_placeholder = "{" + variable_string + "}"
        self.command = self.command.replace(input_var_placeholder, input_var)

    def process_command(self) -> None:
        """
        Processes the whole self.command updating all special variables in the command with their values.

        Returns: None
        """
        if self.command_processed is False:
            variables = self._extract_variables()
            for variable in variables:
                self._replace_with_variable(variable_string=variable)
            self.command_processed = True

    def __str__(self):
        self.process_command()
        return self.command

    def __repr__(self):
        self.process_command()
        return self.command
