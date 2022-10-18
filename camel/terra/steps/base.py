"""
This file defines the base class for a step.
"""
from typing import List


class Step:
    """
    This class defines the base class for steps for the step manager. There is common function that can be used for
    multiple steps it can be housed here. We also use this for typing. We know that all steps have a run function.
    """
    @staticmethod
    def _scan_input_params(input_params: dict, expected_params: List[str]) -> None:
        """
        Scans the input parameters needed to run the MDK model test script.

        Args:
            input_params: (dict) the parameters that are going to be scanned
            expected_params: (List[str]) the expected params that the input params needs

        Returns: None
        """
        buffer = []

        for param in expected_params:
            if input_params.get(param) is None:
                buffer.append(param)

        if len(buffer) > 0:
            raise ValueError(f"the following keys are not found: {buffer}")

    def run(self) -> None:
        pass
