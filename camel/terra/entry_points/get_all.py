"""
This file defines the entry point for cml-terra-all.
"""
from camel.terra.terra_builds import get_all_builds, get_all_models


def main() -> None:
    """
    Prints out all of the builds and models automcatically supported by camel.

    Returns: None
    """
    models = get_all_models()
    builds = get_all_builds()

    print("\nsupported terraform builds automatically supported by camel:")
    for build in builds:
        print(build)

    print("\nsupported terraform models automatically supported by camel:")
    for model in models:
        print(model)
