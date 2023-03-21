"""
This file defines the process for deleting the terraform state file from s3. At this point the process is just a
function, it might be refactored later on.
"""
from typing import Dict

import boto3
from gerund.components.variable import Variable


def delete_tf_state_file(config: dict) -> None:
    """
    Deletes the state from s3.

    Args:
        config: (dict) the config for the build being destroyed

    Returns: None
    """
    backend_config: Dict[str, str] = config["build_state"]
    backend_bucket: str = Variable(backend_config["bucket"]).value
    backend_key: str = Variable(backend_config["key"]).value
    backend_region: str = Variable(backend_config["region"]).value

    build_variables: Dict[str, str] = config["build_variables"]
    aws_access_key: str = Variable(build_variables["aws_access_key"]).value
    aws_secret_access_key: str = Variable(build_variables["aws_secret_access_key"]).value

    client = boto3.client('s3', aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=backend_region)
    client.delete_object(Bucket=backend_bucket, Key=backend_key)
