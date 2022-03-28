import argparse
from subprocess import Popen
import os
import time


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--key', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args_parser.add_argument('--secret_key', action='store', type=str, required=True,
                             help="the name of the ssh key being added")
    args = args_parser.parse_args()

    sleep_count = 1
    keep_waiting = True

    while keep_waiting is True:
        time.sleep(sleep_count)
        sleep_count = sleep_count * 2

        if os.path.exists("./output.txt") is True:
            keep_waiting = False
            break

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


    s3_command = "aws s3 cp --recursive s3://oasislmf-model-library-iki-bgwtcss1 /home/ubuntu/BangladeshCyclone/BGWTCSS1/"
    get_data = Popen(s3_command, shell=True)
    get_data.wait()

    # aws configure
    # ws_access_key_id
    # "$AWS_ACCESS_KEY_ID" - -profile
    # profile_name_here & & aws
    # configure
    # set
    # aws_secret_access_key
    # "$AWS_SECRET_ACCESS_KEY" - -profile
    # profile_name_here & & aws
    # configure
    # set
    # region
    # "$AWS_REGION" - -profile
    # profile_name_here & & aws
    # configure
    # set
    # output
    # "json" - -profile
    # profile_name_here

    # get the data from s3

    run_model = Popen("cd BangladeshCyclone/tests/test-1 && oasislmf model run --config oasislmf_mdk.json", shell=True)
    run_model.wait()
