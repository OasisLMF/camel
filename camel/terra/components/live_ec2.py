"""
This file contains the class that represents the live ec2 instances that are currently on AWS.
"""
from datetime import datetime
from typing import Optional, List

import boto3
from botocore.config import Config
from gerund.components.variable import Variable
from camel.storage.components.profile_storage import LocalProfileVariablesStorage


class LiveEc2:
    """
    This class is used to house live data from AWS EC2.

    Attributes:
        ami_launch_index (int): The AMI launch index, which can be used to find this instance in the launch group.
        image_id (str): The ID of the AMI used to launch the instance.
        instance_id (str): The ID of the instance.
        instance_type (str): The instance type.
        key_name (str): The name of the key pair, if this instance was launched with an associated key pair.
        launch_time (str): The time the instance was launched.
        monitoring (dict): The monitoring for the instance.
        placement (dict): The location where the instance launched, if applicable.
        private_dns_name (str): The private DNS hostname name assigned to the instance. This DNS hostname can only be
        used inside the Amazon EC2 network. This element remains empty until the instance enters a running state.
        private_ip_address (str): The private IPv4 address assigned to the instance.
        product_codes (list): Any product codes associated with the AMI used to launch the instance.
        public_dns_name (str): The public DNS name assigned to the instance. This name is not available until the
        instance enters the running state. For EC2-VPC, this name is only available if you've enabled DNS hostnames for
        your VPC.
        state (dict): The current state of the instance.
        state_transition_reason (str): The reason for the most recent state transition. This might be an empty string.
        subnet_id (str): The ID of the subnet in which the instance is running.
        vpc_id (str): The ID of the VPC in which the instance is running.
        architecture (str): The architecture of the image.
        block_device_mappings (list): Any block device mapping entries for the instance.
        client_token (str): The idempotency token you provided when you launched the instance, if applicable.
        ebs_optimized (bool): Indicates whether the instance is optimized for Amazon EBS I/O.
        ena_support (bool): Indicates whether enhanced networking with ENA is enabled.
        hypervisor (str): The hypervisor type of the instance.
        network_interfaces (list): The network interfaces for the instance.
        root_device_name (str): The device name of the root device volume (for example, /dev/sda1 or /dev/xvda).
        root_device_type (str): The root device type used by the AMI. The AMI can use an EBS volume or an instance
        store volume.
        security_groups (list): [EC2-VPC] The security groups for the instance.
        source_dest_check (bool): Indicates whether source/destination checking is enabled.
        tags (list): Any tags assigned to the instance.
        virtualization_type (str): The virtualization type of the instance.
        cpu_options (dict): The CPU options for the instance.
        capacity_reservation_specification (dict): The Capacity Reservation targeting option.
        hibernation_options (dict): Indicates whether an instance is enabled for hibernation.
        metadata_options (dict): The metadata options for the instance.
        public_ip_address (str): The public IPv4 address, if applicable, from which the instance can be accessed.
    """
    def __init__(self, data: dict) -> None:
        """
        The constructor for LiveEc2 class.

        Args:
            data: The data to be used to create the object.
        """
        self._raw_data: Optional[dict] = data
        self.ami_launch_index: Optional[int] = data.get("AmiLaunchIndex")
        self.image_id: Optional[str] = data.get("ImageId")
        self.instance_id: Optional[str] = data.get("InstanceId")
        self.instance_type: Optional[str] = data.get("InstanceType")
        self.key_name: Optional[str] = data.get("KeyName")
        self.launch_time: Optional[str] = data.get("LaunchTime")
        self.monitoring: Optional[dict] = data.get("Monitoring")
        self.placement: Optional[dict] = data.get("Placement")
        self.private_dns_name: Optional[str] = data.get("PrivateDnsName")
        self.private_ip_address: Optional[str] = data.get("PrivateIpAddress")
        self.product_codes: Optional[list] = data.get("ProductCodes")
        self.public_dns_name: Optional[str] = data.get("PublicDnsName")
        self.state: Optional[dict] = data.get("State")
        self.state_transition_reason: Optional[str] = data.get("StateTransitionReason")
        self.subnet_id: Optional[str] = data.get("SubnetId")
        self.vpc_id: Optional[str] = data.get("VpcId")
        self.architecture: Optional[str] = data.get("Architecture")
        self.block_device_mappings: Optional[list] = data.get("BlockDeviceMappings")
        self.client_token: Optional[str] = data.get("ClientToken")
        self.ebs_optimized: Optional[bool] = data.get("EbsOptimized")
        self.ena_support: Optional[bool] = data.get("EnaSupport")
        self.hypervisor: Optional[str] = data.get("Hypervisor")
        self.network_interfaces: Optional[list] = data.get("NetworkInterfaces")
        self.root_device_name: Optional[str] = data.get("RootDeviceName")
        self.root_device_type: Optional[str] = data.get("RootDeviceType")
        self.security_groups: Optional[list] = data.get("SecurityGroups")
        self.source_dest_check: Optional[bool] = data.get("SourceDestCheck")
        self._tags: Optional[list] = data.get("Tags", [])
        self.virtualization_type: Optional[str] = data.get("VirtualizationType")
        self.cpu_options: Optional[dict] = data.get("CpuOptions")
        self.capacity_reservation_specification: Optional[dict] = data.get("CapacityReservationSpecification")
        self.hibernation_options: Optional[dict] = data.get("HibernationOptions")
        self.metadata_options: Optional[dict] = data.get("MetadataOptions")
        self.public_ip_address: Optional[str] = data.get("PublicIpAddress")

    def __str__(self) -> str:
        """
        The string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return f"{self.public_ip_address} ({self.instance_id}) - {self.instance_type} - {self.launch_time} - {self.state}"

    def __repr__(self) -> str:
        """
        The string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return f"{self.public_ip_address} ({self.instance_id}) - {self.instance_type} - {self.launch_time} - {self.state}"

    @property
    def tags(self) -> List["LiveEc2Tag"]:
        """
        The tags for the instance.

        Returns:
            The tags for the instance.
        """
        return [LiveEc2Tag(tag) for tag in self._tags]

    @property
    def current_running_code(self) -> Optional[int]:
        """
        Returns the current running code of the instance.

        Returns:
            The current running code of the instance.
        """
        return self.state.get("Code")

    @property
    def current_running_state(self) -> str:
        """
        Returns the current running state of the instance.

        Returns:
            The current running state of the instance.
        """
        return self.state.get("Name", "")

    @property
    def launch_time_as_datetime(self) -> Optional[datetime]:
        """
        Returns the launch time of the instance as a datetime object.

        Returns:
            The launch time of the instance as a datetime object.
        """
        return datetime.strptime(self.launch_time, "%Y-%m-%dT%H:%M:%S.%fZ")


class LiveEc2Tag:
    """
    This class is used to house live data from AWS EC2 for a tag.

    Attributes:
        key (str): The key of the tag.
        value (str): The value of the tag.
    """
    def __init__(self, data: dict) -> None:
        """
        The constructor for LiveEc2Tag class.

        Args:
            data: The data to be used to create the object.
        """
        self._raw_data: Optional[dict] = data
        self.key: Optional[str] = data.get("Key")
        self.value: Optional[str] = data.get("Value")


class LiveEc2InstanceList:
    """
    This class is used to house live data from AWS EC2 for a list of instances.

    Attributes:
        reservations (list): The list of reservations.
        instances (List["LiveEc2"]): The list of instances.
    """
    def __init__(self, data: dict) -> None:
        """
        The constructor for LiveEc2InstanceList class.

        Args:
            data: The data to be used to create the object.
        """
        self._raw_data: Optional[dict] = data
        self.reservations: Optional[list] = data.get("Reservations", [])
        self.instances: List["LiveEc2"] = [LiveEc2(instance) for reservation in self.reservations for instance in reservation.get("Instances", [])]

    def get_instances_by_tag(self, key: str, value: str) -> List["LiveEc2"]:
        """
        Returns a list of instances that have the given tag.

        Args:
            key: The key of the tag.
            value: The value of the tag.

        Returns:
            A list of instances that have the given tag.
        """
        return [instance for instance in self.instances if any(tag.key == key and tag.value == value for tag in instance.tags)]

    @staticmethod
    def get_raw_data_from_aws(region: str) -> dict:
        """
        Returns the raw data from AWS.

        Args:
            region: The region to get the data from.

        Returns:
            The raw data from AWS.
        """
        LocalProfileVariablesStorage()
        # my_config = Config(
        #     region_name=region,
        #     signature_version='v4',
        #     retries={
        #         'max_attempts': 10,
        #         'mode': 'standard'
        #     }
        # )
        ec2 = boto3.client('ec2',
                           aws_access_key_id=str(Variable(name="=>aws_access_key")),
                           aws_secret_access_key=str(Variable(name="=>aws_secret_access_key")),
                           region_name=region
                           )
        return ec2.describe_instances()
