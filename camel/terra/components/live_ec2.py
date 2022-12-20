from datetime import datetime
from typing import Optional, List

data = {
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-07783674",
                    "InstanceId": "i-083939aeda6bf549c",
                    "InstanceType": "t2.micro",
                    "KeyName": "OpenVPNServer",
                    "LaunchTime": "2022-11-16T11:18:10.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-1-10.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.1.10",
                    "ProductCodes": [
                        {
                            "ProductCodeId": "f2ew2wrz425a1jagnifd02u5t",
                            "ProductCodeType": "marketplace"
                        }
                    ],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-b5eaa8c3",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2016-11-14T17:04:01.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-4458dbc2"
                            }
                        }
                    ],
                    "ClientToken": "GdqPJ1479143040420",
                    "EbsOptimized": False,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2016-11-14T17:04:00.000Z",
                                "AttachmentId": "eni-attach-464971f9",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Public SG",
                                    "GroupId": "sg-5b8c273d"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:41:0f:62:4f:4d",
                            "NetworkInterfaceId": "eni-72a0f03d",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-1-10.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.1.10",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-1-10.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.1.10"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b5eaa8c3",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Public SG",
                            "GroupId": "sg-5b8c273d"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "OpenVPNServer"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-05c32f6a7ee1411e5"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-7abd0209",
                    "InstanceId": "i-04b0eda2df56f64e0",
                    "InstanceType": "t2.micro",
                    "KeyName": "SFTP",
                    "LaunchTime": "2021-12-22T13:20:48.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-1-52.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.1.52",
                    "ProductCodes": [
                        {
                            "ProductCodeId": "aw0evgkw8e5c1q413zgy5pjce",
                            "ProductCodeType": "marketplace"
                        }
                    ],
                    "PublicDnsName": "ec2-34-250-5-35.eu-west-1.compute.amazonaws.com",
                    "PublicIpAddress": "34.250.5.35",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-b5eaa8c3",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2020-03-11T14:01:03.000Z",
                                "DeleteOnTermination": False,
                                "Status": "attached",
                                "VolumeId": "vol-0df71592219489b94"
                            }
                        }
                    ],
                    "ClientToken": "HeOYX1485519963650",
                    "EbsOptimized": False,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Association": {
                                "IpOwnerId": "713007925222",
                                "PublicDnsName": "ec2-34-250-5-35.eu-west-1.compute.amazonaws.com",
                                "PublicIp": "34.250.5.35"
                            },
                            "Attachment": {
                                "AttachTime": "2017-01-27T12:26:04.000Z",
                                "AttachmentId": "eni-attach-ed069488",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "SFTP",
                                    "GroupId": "sg-a41c43c2"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:96:20:7b:95:cf",
                            "NetworkInterfaceId": "eni-ad8a54ec",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-1-52.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.1.52",
                            "PrivateIpAddresses": [
                                {
                                    "Association": {
                                        "IpOwnerId": "713007925222",
                                        "PublicDnsName": "ec2-34-250-5-35.eu-west-1.compute.amazonaws.com",
                                        "PublicIp": "34.250.5.35"
                                    },
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-1-52.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.1.52"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b5eaa8c3",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "SFTP",
                            "GroupId": "sg-a41c43c2"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "SFTP"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0a8bd09f414307d0c"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-760aaa0f",
                    "InstanceId": "i-01c5784f5a7f87afa",
                    "InstanceType": "r5.xlarge",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-03-10T14:30:03.000Z",
                    "Monitoring": {
                        "State": "enabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-15.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.15",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-12-14 09:27:38 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2018-03-02T09:26:18.000Z",
                                "DeleteOnTermination": False,
                                "Status": "attached",
                                "VolumeId": "vol-0378ccd34f004c5bd"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": True,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2017-11-15T16:31:56.000Z",
                                "AttachmentId": "eni-attach-2d8db4c1",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "oasis-jenkins--jenkins-master20171115163154523700000001",
                                    "GroupId": "sg-2e912155"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:31:db:fd:23:de",
                            "NetworkInterfaceId": "eni-54e2ff6a",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-15.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.15",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-15.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.15"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "oasis-jenkins--jenkins-master20171115163154523700000001",
                            "GroupId": "sg-2e912155"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Terraform",
                            "Value": "True"
                        },
                        {
                            "Key": "Environment",
                            "Value": ""
                        },
                        {
                            "Key": "Name",
                            "Value": "oasis-jenkins--jenkins-master-1 (BACKUP Before removal) "
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 2
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0942eed9d44b5d3bf"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-760aaa0f",
                    "InstanceId": "i-00502014b884eeaf6",
                    "InstanceType": "t2.micro",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2018-03-14T14:49:02.000Z",
                    "Monitoring": {
                        "State": "enabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-93.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.93",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2018-03-14 15:10:36 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2017-11-15T16:35:13.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0ed51125d70c6a964"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2017-11-15T16:35:11.000Z",
                                "AttachmentId": "eni-attach-2080b9cc",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "oasis-jenkins--jenkins-master20171115163154523700000001",
                                    "GroupId": "sg-2e912155"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:f7:60:b9:f3:d2",
                            "NetworkInterfaceId": "eni-f89b86c6",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-93.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.93",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-93.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.93"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "oasis-jenkins--jenkins-master20171115163154523700000001",
                            "GroupId": "sg-2e912155"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Environment",
                            "Value": ""
                        },
                        {
                            "Key": "Name",
                            "Value": "oasis-jenkins--jenkins-linux-slave-1"
                        },
                        {
                            "Key": "Terraform",
                            "Value": "True"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-05ba9075319901917"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-58d7e821",
                    "InstanceId": "i-016eec09b2ba24ad4",
                    "InstanceType": "t2.micro",
                    "KeyName": "oasis_sam",
                    "LaunchTime": "2018-11-02T12:48:52.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-1-100.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.1.100",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-12-14 09:29:00 GMT)",
                    "SubnetId": "subnet-b5eaa8c3",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2018-06-11T10:46:13.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-04a9a568d61e7befd"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2018-06-11T10:46:13.000Z",
                                "AttachmentId": "eni-attach-396da944",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "Jenkins_Proxy",
                                    "GroupId": "sg-9f045ae2"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:e2:29:f2:05:cc",
                            "NetworkInterfaceId": "eni-d93cfeed",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-1-100.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.1.100",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-1-100.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.1.100"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b5eaa8c3",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Jenkins_Proxy",
                            "GroupId": "sg-9f045ae2"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Proxy_Jenkins (BACKUP before removal) "
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-07394b9fc9a7b9e54"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-08d658f84a6d84a80",
                    "InstanceId": "i-0e811d0ddb9675fd7",
                    "InstanceType": "t2.large",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-06-15T09:10:39.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-1-201.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.1.201",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-99-80-10-98.eu-west-1.compute.amazonaws.com",
                    "PublicIpAddress": "99.80.10.98",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-06-17 11:34:15 GMT)",
                    "SubnetId": "subnet-b5eaa8c3",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2019-05-24T10:16:22.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-029732233ba53f188"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Association": {
                                "IpOwnerId": "713007925222",
                                "PublicDnsName": "ec2-99-80-10-98.eu-west-1.compute.amazonaws.com",
                                "PublicIp": "99.80.10.98"
                            },
                            "Attachment": {
                                "AttachTime": "2019-05-24T10:16:20.000Z",
                                "AttachmentId": "eni-attach-08ee7ad07875d71e0",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Public SG",
                                    "GroupId": "sg-5b8c273d"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:5d:72:4d:e6:e2",
                            "NetworkInterfaceId": "eni-0f06933100dd11e4f",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-1-201.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.1.201",
                            "PrivateIpAddresses": [
                                {
                                    "Association": {
                                        "IpOwnerId": "713007925222",
                                        "PublicDnsName": "ec2-99-80-10-98.eu-west-1.compute.amazonaws.com",
                                        "PublicIp": "99.80.10.98"
                                    },
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-1-201.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.1.201"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b5eaa8c3",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Public SG",
                            "GroupId": "sg-5b8c273d"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Mirai-Test-Server"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0edf6bfe638298fc6"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-035966e8adab4aaad",
                    "InstanceId": "i-0d35e73f74db6c802",
                    "InstanceType": "t2.micro",
                    "KeyName": "VPN-Server",
                    "LaunchTime": "2022-11-16T11:24:31.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-1-178.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.1.178",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-54-171-84-161.eu-west-1.compute.amazonaws.com",
                    "PublicIpAddress": "54.171.84.161",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-b5eaa8c3",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2020-02-26T16:40:19.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0b144b85dc0e5e6ba"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Association": {
                                "IpOwnerId": "713007925222",
                                "PublicDnsName": "ec2-54-171-84-161.eu-west-1.compute.amazonaws.com",
                                "PublicIp": "54.171.84.161"
                            },
                            "Attachment": {
                                "AttachTime": "2020-02-26T16:40:19.000Z",
                                "AttachmentId": "eni-attach-0185285bdaf21a73f",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Public SG",
                                    "GroupId": "sg-5b8c273d"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:12:e4:01:52:b6",
                            "NetworkInterfaceId": "eni-0fce4c8785cde0086",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-1-178.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.1.178",
                            "PrivateIpAddresses": [
                                {
                                    "Association": {
                                        "IpOwnerId": "713007925222",
                                        "PublicDnsName": "ec2-54-171-84-161.eu-west-1.compute.amazonaws.com",
                                        "PublicIp": "54.171.84.161"
                                    },
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-1-178.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.1.178"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b5eaa8c3",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Public SG",
                            "GroupId": "sg-5b8c273d"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "VPN-Server"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-06a67772fb658160e"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-0dc8d444ee2a42d8a",
                    "InstanceId": "i-037f051949b7c9d3f",
                    "InstanceType": "t2.micro",
                    "KeyName": "nginx",
                    "LaunchTime": "2021-01-24T22:42:48.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-1-108.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.1.108",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-52-31-239-95.eu-west-1.compute.amazonaws.com",
                    "PublicIpAddress": "52.31.239.95",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2021-03-01 10:08:39 GMT)",
                    "SubnetId": "subnet-b5eaa8c3",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2021-01-24T22:42:49.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0956b9f52e5ba9f89"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Association": {
                                "IpOwnerId": "713007925222",
                                "PublicDnsName": "ec2-52-31-239-95.eu-west-1.compute.amazonaws.com",
                                "PublicIp": "52.31.239.95"
                            },
                            "Attachment": {
                                "AttachTime": "2021-01-24T22:42:48.000Z",
                                "AttachmentId": "eni-attach-09dad49d7bf5aae10",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Public SG",
                                    "GroupId": "sg-5b8c273d"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:fb:3d:13:a8:1d",
                            "NetworkInterfaceId": "eni-0768baab2c34b7b9f",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-1-108.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.1.108",
                            "PrivateIpAddresses": [
                                {
                                    "Association": {
                                        "IpOwnerId": "713007925222",
                                        "PublicDnsName": "ec2-52-31-239-95.eu-west-1.compute.amazonaws.com",
                                        "PublicIp": "52.31.239.95"
                                    },
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-1-108.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.1.108"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b5eaa8c3",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Public SG",
                            "GroupId": "sg-5b8c273d"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Nginx"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0d7a776873d738e00"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-0e5657f6d3c3ea350",
                    "InstanceId": "i-0a41df18152bb6c01",
                    "InstanceType": "t2.large",
                    "KeyName": "nginx",
                    "LaunchTime": "2021-02-15T18:04:23.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-82.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.82",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2021-03-01 10:08:30 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2021-02-15T16:36:12.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0955defb13b63fdb5"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2021-02-15T16:36:10.000Z",
                                "AttachmentId": "eni-attach-0a82be970308f7dd2",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:a8:14:d0:a1:7d",
                            "NetworkInterfaceId": "eni-0f1d0e22f55dc9dce",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-82.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.82",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-82.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.82"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Nginx-ui"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0d19133b11cc7f451"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-08ca3fed11864d6bb",
                    "InstanceId": "i-0e0302637103069ad",
                    "InstanceType": "t2.medium",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-12-14T14:20:01.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-239.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.239",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-12-14 14:20:12 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-04-25T09:54:52.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-001c82fcdb499b223"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-04-25T09:54:51.000Z",
                                "AttachmentId": "eni-attach-05a89c516196a3203",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:96:e7:ac:b5:dd",
                            "NetworkInterfaceId": "eni-07eece9ecf99ca0b6",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-239.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.239",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-239.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.239"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "KamDev"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0a7948720adac62b4"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-08ca3fed11864d6bb",
                    "InstanceId": "i-0c69c693563acd89f",
                    "InstanceType": "t2.medium",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-06-17T10:47:32.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-130.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.130",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-06-17T10:47:33.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-01dea8b5436e42f35"
                            }
                        },
                        {
                            "DeviceName": "/dev/sdd",
                            "Ebs": {
                                "AttachTime": "2022-06-17T10:48:08.000Z",
                                "DeleteOnTermination": False,
                                "Status": "attached",
                                "VolumeId": "vol-0c97d735a4f9010ec"
                            }
                        }
                    ],
                    "ClientToken": "539E8AEB-E9D5-4095-ADDA-3D4483B3F663",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-06-17T10:47:32.000Z",
                                "AttachmentId": "eni-attach-0cab4720b7b698f1c",
                                "DeleteOnTermination": False,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:e5:fc:66:52:f7",
                            "NetworkInterfaceId": "eni-0f30bb47cd4b70696",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-130.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.130",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-130.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.130"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "New Mirai test server"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0cac9cedfca270398"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-08ca3fed11864d6bb",
                    "InstanceId": "i-0918a03d8a3c54d2f",
                    "InstanceType": "t2.small",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-11-18T18:45:44.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-56.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.56",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-02-23T11:02:55.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0cc2b99f297455b22"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-02-23T11:02:54.000Z",
                                "AttachmentId": "eni-attach-0618ecc3e3b49c58d",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:24:af:3a:38:1d",
                            "NetworkInterfaceId": "eni-07532c94d29a45741",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-56.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.56",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-56.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.56"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Camel"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-005bcfdeb36e11e65"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-0d2a4a5d69e46ea0b",
                    "InstanceId": "i-0bfb4f03bff03d9b2",
                    "InstanceType": "m4.16xlarge",
                    "KeyName": "Fathom-US",
                    "LaunchTime": "2022-11-16T10:03:01.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-87.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.87",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-11-16 11:41:55 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-08-08T09:28:39.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0e84509ce0e8fa3ea"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": True,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-08-08T09:28:38.000Z",
                                "AttachmentId": "eni-attach-0132d904bb324ed6d",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:80:38:e9:a9:79",
                            "NetworkInterfaceId": "eni-0f911596309086364",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-87.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.87",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-87.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.87"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Fathom -USFlood"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 32,
                        "ThreadsPerCore": 2
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0a36899423b7f3796"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-04e2e94de097d3986",
                    "InstanceId": "i-0e0633f1c49565f9e",
                    "InstanceType": "t2.large",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-10-31T11:24:26.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-224.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.224",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-10-31 17:02:24 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-10-27T15:15:23.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-00f00e6b1b834b896"
                            }
                        }
                    ],
                    "ClientToken": "969DF97B-DA04-46BB-AEE6-F0AF592EFB5E",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-10-27T15:15:22.000Z",
                                "AttachmentId": "eni-attach-01885f54538e5ad4c",
                                "DeleteOnTermination": False,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:1f:51:4d:43:81",
                            "NetworkInterfaceId": "eni-0f80bf0647cbcbe7f",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-224.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.224",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-224.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.224"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "combus alm"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0dc487543a35fe30c"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-096800910c1b781ba",
                    "InstanceId": "i-07828645608be1a1e",
                    "InstanceType": "t2.medium",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-12-20T10:35:22.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-116.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.116",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-11-16T11:57:55.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0d5bf6b611e91a74e"
                            }
                        }
                    ],
                    "ClientToken": "ffdb4d26-45b3-413d-852c-5dd45e45d89f",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-11-16T11:57:54.000Z",
                                "AttachmentId": "eni-attach-07b406be698077c93",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:41:a2:b9:8f:89",
                            "NetworkInterfaceId": "eni-0c1f218ceaa089492",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-116.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.116",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-116.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.116"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "ben_dev"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-00253267b7173761c"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-0b95c8042c84717b9",
                    "InstanceId": "i-01dfc51e68ad74ab5",
                    "InstanceType": "m4.4xlarge",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-12-12T11:57:22.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-157.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.157",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-12-12 16:56:17 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-12-07T11:18:53.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-066f01b41b379f633"
                            }
                        }
                    ],
                    "ClientToken": "D2ABA550-094D-424A-B30B-971714EFCC07",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-12-07T11:18:52.000Z",
                                "AttachmentId": "eni-attach-0cb14c5f303049766",
                                "DeleteOnTermination": False,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:87:7f:e3:95:83",
                            "NetworkInterfaceId": "eni-0a86d4197b888f0e8",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-157.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.157",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-157.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.157"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "jba ukfl camel run"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 8,
                        "ThreadsPerCore": 2
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0f5d5c14fa0bb3ee3"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-05e786af422f8082a",
                    "InstanceId": "i-0c424312ae1807cf4",
                    "InstanceType": "m4.4xlarge",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-12-14T17:13:46.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-140.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.140",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2022-12-15 03:05:01 GMT)",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-12-14T17:13:47.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-08ec1fa4c20f7a86c"
                            }
                        }
                    ],
                    "ClientToken": "a7d3eba9-4c81-4fe6-b016-8f734617a506",
                    "EbsOptimized": True,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-12-14T17:13:46.000Z",
                                "AttachmentId": "eni-attach-08285c1cba786283f",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:7b:c4:75:6e:63",
                            "NetworkInterfaceId": "eni-08791c4b905131f9c",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-140.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.140",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-140.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.140"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "aalcalc-test"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 8,
                        "ThreadsPerCore": 2
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-0424a006cf937a2f8"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-029cfca952b331b52",
                    "InstanceId": "i-0f19b5f52f9ac54f4",
                    "InstanceType": "t2.large",
                    "KeyName": "OasisProject",
                    "LaunchTime": "2022-12-19T14:42:18.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-1c",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-10-0-35.eu-west-1.compute.internal",
                    "PrivateIpAddress": "10.10.0.35",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-b4eaa8c2",
                    "VpcId": "vpc-da83f1be",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2022-12-19T14:42:19.000Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0fd693ec798fb1f77"
                            }
                        }
                    ],
                    "ClientToken": "7A08657D-F16E-47B8-B90A-3BE29673CA7D",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2022-12-19T14:42:18.000Z",
                                "AttachmentId": "eni-attach-02c969653adf9360a",
                                "DeleteOnTermination": False,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "Oasis Private SG",
                                    "GroupId": "sg-1d8c277b"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "06:75:54:f8:17:ff",
                            "NetworkInterfaceId": "eni-04aca9bc6507125ea",
                            "OwnerId": "713007925222",
                            "PrivateDnsName": "ip-10-10-0-35.eu-west-1.compute.internal",
                            "PrivateIpAddress": "10.10.0.35",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-10-0-35.eu-west-1.compute.internal",
                                    "PrivateIpAddress": "10.10.0.35"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-b4eaa8c2",
                            "VpcId": "vpc-da83f1be",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "Oasis Private SG",
                            "GroupId": "sg-1d8c277b"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "catrisks afeq camel run"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled"
                    }
                }
            ],
            "OwnerId": "713007925222",
            "ReservationId": "r-05bfb751c8ba6b157"
        }
    ]
}


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
        private_dns_name (str): The private DNS hostname name assigned to the instance. This DNS hostname can only be used inside the Amazon EC2 network. This element remains empty until the instance enters a running state.
        private_ip_address (str): The private IPv4 address assigned to the instance.
        product_codes (list): Any product codes associated with the AMI used to launch the instance.
        public_dns_name (str): The public DNS name assigned to the instance. This name is not available until the instance enters the running state. For EC2-VPC, this name is only available if you've enabled DNS hostnames for your VPC.
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
        root_device_type (str): The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.
        security_groups (list): [EC2-VPC] The security groups for the instance.
        source_dest_check (bool): Indicates whether source/destination checking is enabled.
        tags (list): Any tags assigned to the instance.
        virtualization_type (str): The virtualization type of the instance.
        cpu_options (dict): The CPU options for the instance.
        capacity_reservation_specification (dict): The Capacity Reservation targeting option.
        hibernation_options (dict): Indicates whether an instance is enabled for hibernation.
        metadata_options (dict): The metadata options for the instance.
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

    @property
    def tags(self) -> List["LiveEc2Tag"]:
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
    def get_raw_data_from_aws() -> dict:
        """
        Returns the raw data from AWS.

        Returns:
            The raw data from AWS.
        """
        return boto3.client("ec2").describe_instances()



if __name__ == "__main__":
    print(data.keys())
    for i in LiveEc2InstanceList(data).instances:
        for x in i.tags:
            print(x.key, x.value)

    outcome = LiveEc2InstanceList(data).get_instances_by_tag("Terraform", "True")
    print(outcome)
    # for i in data["Reservations"]:
    #     # reservations = i["reservations"]
    #     # print(i.keys())
    #     instances = i["Instances"]
    #     for j in instances:
    #         ec2_instance = LiveEc2(data=j)
    #         print(type(ec2_instance.launch_time_as_datetime))
