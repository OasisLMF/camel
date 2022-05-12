"""
This file defines the function around the entry point cml-model-build.
"""
import argparse
from os import getcwd
from pathlib import Path
from subprocess import Popen

import yaml


class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


def _build_config(name: str, directory: str) -> None:
    """
    Writes a default config file to the new model package.

    Args:
        name: (str) the name of the model being deployed
        directory: (str) the directory of where the model is deployed

    Returns: None
    """
    body = {
        "location": f"model_runs/{name}",
        "variables": {
            "aws_access_key": "=>aws_access_key",
            "aws_secret_access_key": "=>aws_secret_access_key",
            "subnet_id": "some_subnet_id",
            "server_security_group": "some_security_group_id"
        },
        "local_vars": [
            {
                "name": "output",
                "path": "/home/ubuntu/",
                "ip_address": True
            }
        ],
        "steps": [
            {
                "name": "run_script",
                "script_name": "run_model",
                "variables": {
                    "key": "=>aws_access_key",
                    "secret_key": "=>aws_secret_access_key"
                }
            },
            {
                "name": "conditional",
                "operator": "==",
                "variable": ">>output",
                "value": "FINISHED",
                "step_data": {
                    "name": "print",
                    "statement": "the process is finished"
                }
            }
        ]
    }
    with open(f"{directory}/{name}_config.yml", 'w') as outfile:
        yaml.dump(body, outfile, default_flow_style=False, sort_keys=False, Dumper=MyDumper)


def main() -> None:
    """
    Copies a ready to go template for building a model.

    Returns: None
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--name', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args = args_parser.parse_args()

    template_path = str(Path(__file__).parent.absolute()).replace("entry_points", "model_template/")
    target_path = str(getcwd()) + f"/{args.name}"

    if not Path(target_path).exists():
        print(f"Unpacking template for the {args.name} model")
        copy_template = Popen(f"cp -r {template_path} {target_path}", shell=True)
        copy_template.wait()
        _build_config(name=args.name, directory=target_path)
        print(f"template for the {args.name} model has been unpacked")
    else:
        print(f"model build {args.name} already exists")
