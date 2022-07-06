"""
Docstring  -- This file creates enums for our step_names that are supported  //
"""
from enum import Enum


class StepNameEnum(Enum):
    RUN_SCRIPT = "run_script"
    PRINT = "print"
    DESTROY_BUILD = "destroy_build"
    CONDITIONAL = "conditional"
