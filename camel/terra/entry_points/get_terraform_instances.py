"""
This file defines the entry point for getting terraform instances currently on AWS.
"""
# import argparse

from camel.terra.components.live_ec2 import LiveEc2InstanceList
from camel.storage.components.profile_storage import LocalProfileVariablesStorage


def main() -> None:
    """
    The main function for the get_terraform_instances.py script.
    """
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--aws_access_key", action="store", type=str, required=False, help="the AWS access key")
    # parser.add_argument("--aws_secret_key", action="store", type=str, required=False, help="the AWS secret key")
    #
    # args = parser.parse_args()
    LocalProfileVariablesStorage()
    raw_data: dict = LiveEc2InstanceList.get_raw_data_from_aws(region="eu-west-2")
    # instances: List[LiveEc2] = LiveEc2InstanceList(raw_data).get_instances_by_tag(key="Terraform", value="True")
    for instance in LiveEc2InstanceList(raw_data).instances:
        print(instance)
