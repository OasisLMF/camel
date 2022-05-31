"""
This file defines the function around the entry point cml-model-load.
"""
import argparse
from os import getcwd
from pathlib import Path
from subprocess import Popen


def main() -> None:
    """
    Saves a model build into the pip module.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="name of the model package being loaded")
    args_parser.add_argument("--config", action='store', type=str, required=False,
                             default="N", help="'y' if you want to automatically load the config")
    args = args_parser.parse_args()

    target_path = str(Path(__file__).parent.absolute()).replace(
        "models/entry_points", f"terra/terra_builds/model_runs/{args.name}/"
    )
    build_path = str(getcwd()) + f"/{args.name}"

    # load the model project into the pip module
    if not Path(target_path).exists():
        print(f"loading the {args.name} model")
        copy_build = Popen(f"cp -r {build_path} {target_path}", shell=True)
        copy_build.wait()

        config_path = f"{build_path}/{args.name}_config.yml"
        if Path(config_path).exists():
            if args.config != "y":
                load_config = input(
                    f"{args.name}_config.yml file found do you want to load it into your tconfig? y/N: "
                )
            else:
                load_config = "y"

            if load_config == "y":
                print("loading to tconfig")
                command = f"cml-tconfig-import --name {args.name} --path {config_path}"
                import_command = Popen(command, shell=True)
                import_command.wait()
