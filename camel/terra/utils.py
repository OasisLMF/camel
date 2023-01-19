"""
This file defines util functions for both terra apply and destroy.
"""
import os
from pathlib import Path
from typing import Tuple

from camel.terra_configs.components.config_mapper import TerraConfigMapper


OUTPUT_FILE_PATH: str = str(os.getcwd()) + "/build_output.json"


def extract_paths(config_name: str, config_path: str) -> Tuple[TerraConfigMapper, str, str]:
    """
    Extracts paths for the configs to enable the Terraform commands.

    Args:
        config_name: (str) the name of the name of the config being loaded
        config_path: (str) path to where the config file to be loaded is

    Returns: (Tuple[TerraConfigMapper, str, str]) config mapper for the profile, config path, file path of where
                                                  terraform builds are stored
    """
    config_map = TerraConfigMapper.get_cached_profile()
    if config_name != "none":
        print(f"using existing config: {config_name}")
        config_path: str = config_map.terra_builds_path + f"/{config_name}.yml"
    else:
        config_path: str = str(os.getcwd()) + f"/{config_path}"

    # defines the file path of where all the terraform builds are defined in the pip package
    file_path: str = str(Path(__file__).parent) + "/terra_builds"

    return config_map, config_path, file_path


def get_init_config(config: dict) -> str:
    """
    Extracts the backend terraform config command from the config file.

    Args:
        config: (dict) the config file loaded for the model run

    Returns: (str) the backend terraform config command
    """
    backend_config = config["build_state"]
    backend_bucket = backend_config["bucket"]
    backend_key = backend_config["key"]
    backend_region = backend_config["region"]

    backend_config_bucket = f' -backend-config="bucket={backend_bucket}"'
    backend_config_key = f' -backend-config="key={backend_key}"'
    backend_config_region = f' -backend-config="region={backend_region}"'

    return f'terraform init -reconfigure {backend_config_bucket} {backend_config_key} {backend_config_region}'
