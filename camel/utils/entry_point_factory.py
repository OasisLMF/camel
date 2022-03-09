from typing import List, Tuple


def entry_point_factory(module: str, commands: List[Tuple[str, str]]) -> List[str]:
    # command example => ("one", "script_one") => cml-interface-one=interface.entry_points.script_one:main
    buffer = []
    for i in commands:
        command, script = i
        new_command = f"cml-{module}-{command}={module}.entry_points.{script}:main"
        buffer.append(new_command)

    buffer.append(f"cml-{module}={module}.entry_points.help:main")
    return buffer
