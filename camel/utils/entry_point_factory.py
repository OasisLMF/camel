from typing import List, Tuple


def entry_point_factory(module: str, commands: List[Tuple[str, str, str]], directory: str) -> List[str]:
    # command example => ("one", "script_one") => cml-interface-one=interface.entry_points.script_one:main
    buffer = []
    for i in commands:
        command, script, _ = i
        new_command = f"cml-{module}-{command}={directory}.entry_points.{script}:main"
        buffer.append(new_command)

    buffer.append(f"cml-{module}={directory}.entry_points.help:main")
    return buffer


def help_factory(module: str, commands: List[Tuple[str, str, str]]):
    buffer = []
    for i in commands:
        command, _, description = i
        new_command = f"cml-{module}-{command} => {description}"
        buffer.append(new_command)
    return buffer
