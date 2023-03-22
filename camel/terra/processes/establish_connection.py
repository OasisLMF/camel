"""
This file defines the process of establishing a connection to a server. At this point in time, the process is
just a function but it may be refactored in the future.
"""
import time
from typing import List

from gerund.commands.terminal_command import TerminalCommand


def establish_connection(ip_address: str) -> None:
    """
    Loops through SSH connections until the SSH connection is accepted.

    Args:
        ip_address: (str) the IP address of the server being connecting to

    Returns: None
    """
    connection = TerminalCommand(command="echo 'connection achieved'", ip_address=ip_address)

    connected = False
    while connected is False:
        print(f"establishing connection to: {ip_address}")
        established: List[str] = connection.wait(capture_output=True)
        established_str: str = " ".join(established).lower()

        if "refused" not in established_str:
            print("connection established")
            break
        print("connection refused trying again")
        time.sleep(3)
