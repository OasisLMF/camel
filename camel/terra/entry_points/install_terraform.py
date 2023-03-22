"""
This script defines the entry point for terra-install.
"""
import subprocess
from pathlib import Path


def main() -> None:
    """
    Runs the installation script for terraform.

    :return: None
    """
    shell_directory: str = f"{str(Path(__file__).parent)}/scripts/install_terraform.sh"

    # change the permissions of the bash script that installs terraform
    change_permissions_process = subprocess.Popen(f"chmod +x {shell_directory}", shell=True)
    change_permissions_process.wait()

    # run the bash script that installs terraform
    subprocess.call(shell_directory)
