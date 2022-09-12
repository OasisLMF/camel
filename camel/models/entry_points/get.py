"""
This file defines the function around the entry point cml-model-get.
"""
from glob import glob
from pathlib import Path


def main() -> None:
    """
    Prints all the available models.

    Returns: None
    """
    model_directory = str(Path(__file__).parent.absolute()).replace(
        "models/entry_points", "terra/terra_builds/model_runs/"
    )

    print("available models:")
    for model in [x.split("/")[-2] for x in glob(f"{model_directory}/*/", recursive=True)]:
        if model != "__pycache__":
            print(model)
