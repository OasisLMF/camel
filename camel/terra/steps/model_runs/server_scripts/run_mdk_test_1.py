"""
This script is to be run on a model server to run a generic MDK test.
"""
import argparse
from subprocess import Popen


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--git_branch', action='store', type=str, required=True,
                             help="git branch to be used for test")
    args_parser.add_argument('--parent_dir', action='store', type=str, required=True,
                             help="the location of the git repo to run the tests on")
    args_parser.add_argument('--test_dir', action='store', type=str, required=True,
                             help="the location of the specific test dir")
    args_parser.add_argument('--run_dir', action='store', type=str, required=True,
                             help="the location of the run dir for the test")
    args_parser.add_argument('--expected_md5', action='store', type=str, required=True,
                             help="the location of the md5 file for teh expected results")
    args = args_parser.parse_args()

    # checkout required branch
    checkout_branch = Popen("cd {} && git checkout {}".format(args.parent_dir, args.git_branch), shell=True)
    checkout_branch.wait()

    # run the mdk process
    run_model = Popen(". ~/.profile && cd {} && oasislmf model run --config oasislmf.json -r {}".format(args.test_dir,
                                                                                                        args.run_dir),
                      shell=True)
    run_model.wait()

    # check md5sum
    output_dir = "{}/output".format(args.run_dir)
    md5sum_cmd = "cd {} && md5sum --check {} > check.md5".format(output_dir, args.expected_md5)
    md5sum_shell = Popen(md5sum_cmd, shell=True)
    md5sum_shell.wait()

    # print status
    with open("{}/check.md5".format(output_dir), "r") as check_file:
        contents = check_file.read()
        if "OK" not in contents:
            print("MD5 verification failed! The MDK run did not produce the expected results!")
        elif "FAILED" not in contents:
            print("The MDK run produced the expected results!")
        else:
            print("MD5 verification failed! The MDK run did not produce the expected results!")


if __name__ == "__main__":
    main()
