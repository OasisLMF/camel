from typing import List

from camel.terra.components.live_ec2 import LiveEc2InstanceList, LiveEc2


def main() -> None:
    """
    The main function for the get_terraform_instances.py script.
    """
    raw_data: dict = LiveEc2InstanceList.get_raw_data_from_aws(region="eu-west-2")
    instances: List[LiveEc2] = LiveEc2InstanceList(raw_data).get_instances_by_tag(key="Terraform", value="True")
    for instance in instances:
        print(instance)
