"""
This file defines the process that runs the build script on the model server. Processes are currently just
functions, but they could be refactored in the future.
"""
import sys
import time

from gerund.commands.bash_script import BashScript
from gerund.components.variable import Variable
from gerund.components.variable_map import VariableMap


def run_build_script(command: BashScript) -> None:
    """
    Continuously loops until the server build bash script as run on the model server.

    Args:
        command: (BashScript) the build bash script to be run on the model server

    Returns: None
    """
    count: int = 0
    keep_going: bool = True
    variable_map = VariableMap()
    variable_map["output"] = {
        "path": "/home/ubuntu/",
        "ip_address": True
    }

    while keep_going is True:
        if count >= 5:
            sys.exit("model build script tried to run 5 times and failed, model server cannot run a model because"
                     "build script has note been executed")
        time.sleep(2)
        command.wait()
        outcome = str(Variable(name=">>output"))
        if outcome == "FINISHED":
            print("build script has run")
            break
        else:
            print("build script has not run retrying")
            command._path = None
            count += 1
