"""
Defines the entry point for the cml-tconfig-get command.
"""
from camel.terra_configs.components.config_mapper import TerraConfigMapper


def main() -> None:
    """
    Gets all the terraform configs associated with the current profile and prints them out.

    :return: None
    """
    print("the following terraform configs are available:")

    profile = TerraConfigMapper.get_cached_profile()

    for config in profile.get_configs():
        print(config.split("/")[-1])
