"""
This file defines the entry points for getting all the models and builds that are supported by camel.
"""
import os
from glob import glob
from typing import List


def get_all_models() -> List[str]:
    """
    Gets all the models supported for the terraform models.

    Returns: (List[str]) the models supported
    """
    parent_path = str(os.path.abspath(__file__)).replace("__init__.py", "")
    models = [x.split("/")[-2] for x in glob(parent_path + "/model_runs/*/", recursive=True)]
    buffer = []
    for model in models:
        if model != "__pycache__":
            buffer.append(model)
    return buffer


def get_all_builds() -> List[str]:
    """
    Gets all the builds supported.

    Returns: (List[str]) the builds supported
    """
    parent_path = str(os.path.abspath(__file__)).replace("__init__.py", "")
    builds = [x.split("/")[-2] for x in glob(parent_path + "/*/", recursive=True)]
    buffer = []
    for model in builds:
        if model not in ["model_runs", "__pycache__"]:
            buffer.append(model)
    return buffer
