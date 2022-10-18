"""
This script is to be run on a model server to run a generic API test.
"""
import argparse
import os
from subprocess import Popen

env_vars = {
    "OASIS_WORKER_VERSION": os.getenv('OASIS_WORKER_VERSION'),
    "OASIS_PLATFORM_VERSION": os.getenv('OASIS_PLATFORM_VERSION'),
    "OASIS_UI_VERSION": os.getenv('OASIS_UI_VERSION')
}


def main():
    # arg parse
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--git_branch', action='store', type=str, required=True,
                             help="git branch to be used for test")
    args_parser.add_argument('--parent_dir', action='store', type=str, required=True,
                             help="the location of the git repo to run the tests on")
    args_parser.add_argument('--test_dir', action='store', type=str, required=True,
                             help="the location of the specific test dir")
    args_parser.add_argument('--expected_md5', action='store', type=str, required=True,
                             help="the location of the md5 file for the expected results")
    args_parser.add_argument('--worker_name', action='store', type=str, required=True,
                             help="the name of the worker container")
    args_parser.add_argument('--worker_dockerfile', action='store', type=str, required=True,
                             help="the name of the worker dockerfile")
    args_parser.add_argument('--docker_compose_platform', action='store', type=str, required=True,
                             help="the location of the docker compose for the platform")
    args_parser.add_argument('--docker_compose_worker', action='store', type=str, required=True,
                             help="the location of the docker compose for the worker")
    args_parser.add_argument('--docker_compose_ui', action='store', type=str, required=True,
                             help="the location of the docker compose for the ui")

    args = args_parser.parse_args()

    # checkout required branch
    checkout_branch = Popen("cd {} && git checkout {}".format(args.parent_dir, args.git_branch), shell=True)
    checkout_branch.wait()

    # Build docker-worker
    build_worker = Popen(
        "cd {} && docker build --build-arg OASIS_WORKER_VERSION=$OASIS_WORKER_VERSION -t {}:{} -f {} .".format(
            args.parent_dir, args.worker_name, env_vars["OASIS_WORKER_VERSION"], args.worker_dockerfile), shell=True)
    build_worker.wait()

    # set up docker network for shiny
    shiny_network = Popen("docker network create shiny-net", shell=True)
    shiny_network.wait()

    # run the docker-compose commands
    docker_compose = Popen("cd {} && docker-compose -f {} -f {} -f {} up -d".format(
        args.parent_dir, args.docker_compose_platform, args.docker_compose_worker, args.docker_compose_ui),
        shell=True)
    docker_compose.wait()

    # pull the oasis ui app docker image
    docker_ui = Popen("docker pull coreoasis/oasisui_app:{}".format(env_vars["OASIS_UI_VERSION"]), shell=True)
    docker_ui.wait()

    # run api client
    api_client = Popen(
        ". ~/.profile && cd {} && mkdir api_run && oasislmf api run --server-url http://0.0.0.0:8000 --config oasislmf.json -o api_run".format(args.test_dir),
        shell=True)
    api_client.wait()

    # Extract results from API
    untar_shell = Popen("cd {}/api_run && tar -xvf analysis_1_output.tar".format(args.test_dir), shell=True)
    untar_shell.wait()

    # check the md5sum
    output_dir = "{}/api_run/output".format(args.test_dir)
    md5sum_cmd = "cd {} && md5sum --check {} > check.md5".format(output_dir, args.expected_md5)
    md5sum_shell = Popen(md5sum_cmd, shell=True)
    md5sum_shell.wait()

    # print status
    with open("{}/check.md5".format(output_dir), "r") as check_file:
        contents = check_file.read()
        if "OK" not in contents:
            print("MD5 verification failed! The MDK run did not produced the expected results!")
        elif "FAILED" not in contents:
            print("The MDK run produced the expected results!")
        else:
            print("MD5 verification failed! The MDK run did not produced the expected results!")


if __name__ == "__main__":
    main()
