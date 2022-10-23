"""
This file defines the factory that gets generic model runs
"""
from camel.terra.steps.base import Step
from camel.terra.steps.model_runs.api_test_model_run import ApiTestModelRunStep
from camel.terra.steps.model_runs.mdk_test_model_run import MdkTestModelRunStep


def get_generic_model(model_type: str, input_params: dict, terraform_data: dict) -> Step:
    """
    Gets a generic model based on the model type selected.

    Args:
        model_type: (str) the type of generic model to be run as a step
        input_params: (dict) the parameters directly from the step being read
        terraform_data: (dict) the data produced from the terraform build once it is completed

    Returns: (Step) the generic model to be run
    """
    if model_type == "mdk_test_model":
        return MdkTestModelRunStep(input_params=input_params, terraform_data=terraform_data)
    elif model_type == "api_test_model":
        return ApiTestModelRunStep(input_params=input_params, terraform_data=terraform_data)
    raise ValueError(f"{model_type} generic model type is not supported")
