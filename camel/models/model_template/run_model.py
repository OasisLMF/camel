"""
This script is an example of how to run a model on the server that is built using terraform.
"""
import argparse
import os
import time
from subprocess import Popen


if __name__ == "__main__":
    # collect the arguments needed to run
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--key', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args_parser.add_argument('--secret_key', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args = args_parser.parse_args()

    sleep_count = 2
    keep_waiting = True

    # loop until the FINISHED flag for the server_build.sh script has been written
    while keep_waiting is True:
        time.sleep(sleep_count)

        if os.path.exists("./output.txt") is True:
            keep_waiting = False
            break

    # add github to the known hosts as you will need to clone using a github SSH key
    add_key = Popen('ssh-keyscan -H "github.com" >> ~/.ssh/known_hosts ', shell=True)
    add_key.wait()

    # clones a github repo that houses a
    git_clone_command = Popen('git clone git@github.com:OasisLMF/some_model.git', shell=True)
    git_clone_command.wait()

    profile = "default"

    command_buffer = [
        'aws configure ',
        f'set aws_access_key_id "{args.key}" ',
        f'--profile {profile} ',
        f'&& aws configure set aws_secret_access_key "{args.secret_key}" ',
        f'--profile {profile}'
    ]

    aws_command = "".join(command_buffer)
    configure_aws_command = Popen(aws_command, shell=True)
    configure_aws_command.wait()

    # getting data from s3
    s3_command = "aws s3 cp --recursive s3://oasislmf-model-library-iki-bgwtcss1 /home/ubuntu/some_model_repo/some_model/"
    get_data = Popen(s3_command, shell=True)
    get_data.wait()

    # run the model you have cloned with the command below
    run_model = Popen("cd some_model_repo/some_model/ && oasislmf model run --config oasislmf.json", shell=True)
    run_model.wait()
