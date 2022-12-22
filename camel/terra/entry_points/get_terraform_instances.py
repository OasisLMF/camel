"""
This file defines the entry point for getting terraform instances currently on AWS.
"""
import argparse

from camel.terra.components.live_ec2 import LiveEc2InstanceList


def main() -> None:
    """
    The main function for the get_terraform_instances.py script.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", action="store", type=str, required=False,
                        help="the region to get the instances from")

    args = parser.parse_args()
    raw_data: dict = LiveEc2InstanceList.get_raw_data_from_aws(region=args.region)

    for instance in LiveEc2InstanceList(raw_data).instances:
        if instance.tf_state is not None:
            print(instance)
        # print(instance)
