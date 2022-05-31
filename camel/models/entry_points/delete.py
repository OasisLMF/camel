"""
This file defines the function around the entry point cml-model-delete.
"""
import argparse
import shutil
from pathlib import Path


def main() -> None:
    """
    Deletes a model.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="name of the model being deleted")
    args = args_parser.parse_args()

    model_directory = str(Path(__file__).parent.absolute()).replace(
        "models/entry_points", f"terra/terra_builds/model_runs/{args.name}"
    )
    shutil.rmtree(model_directory)
