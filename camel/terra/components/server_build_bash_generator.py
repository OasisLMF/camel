"""
This file defines the class responsible for generating bash scripts for building servers.
"""
from typing import Optional, List


class ServerBuildBashGenerator(list):
    """
    This class is responsible for generating and writing bash scripts for building a model running server and
    writing the generated bash script to a file.
    """
    def __init__(self) -> None:
        """
        The constructor for the ServerBuildBashGenerator class.
        """
        super().__init__([])

    def generate_script(self, repository: str, aws_key: str, aws_secret_key: str,
                        oasislmf_version: Optional[str] = None, data_bucket: Optional[str] = None,
                        data_directory: Optional[str] = None) -> None:
        """
        Fills up the self with the lines needed to create a bash script.
        Notes:
            if you want to add parameters to the bash script in future pass them into this function and format the
            lines that you want with the parameters

        Args:
            repository: (str) the repository where the model is stored
            aws_key: (str) thr AWS access key to configure the server with the AWS client
            aws_secret_key: (str) thr AWS secret access key to configure the server with the AWS client
            oasislmf_version: (Optional[str]) the version of oasis you want installed is None will be latest version
            data_bucket: (Optional[str]) the s3 bucket that is where the model data is stored
            data_directory: (Optional[str]) the directory of where the data should be stored on the server

        Returns: None
        """
        if oasislmf_version is None:
            install_oasislmf_line = "pip3 install oasislmf[extra]"
        else:
            install_oasislmf_line = f"pip3 install oasislmf[extra]=={oasislmf_version}"

        if data_bucket is None:
            data_line = ""
        else:
            data_line = f"aws s3 sync s3://{data_bucket} {data_directory}"
        profile = "default"

        lines = [
            # "#!/bin/bash",
            "",
            # "sudo apt-get update -y",
            # "sudo apt-get install git -y",
            # "sudo apt-get install vim -y",
            # "sudo apt-get install tmux -y ",
            # "sudo apt-get install ca-certificates -y",
            # "sudo apt-get install curl -y",
            # "sudo apt-get install gnupg -y",
            # "sudo apt-get install lsb-release -y",
            # "sudo apt-get install python3-venv -y",
            # "sudo apt-get install python3-pip -y",
            # "sudo apt-get install awscli -y",
            "",
            f'aws configure set aws_access_key_id "{aws_key}" --profile {profile}',
            f'aws configure set aws_secret_access_key "{aws_secret_key}" --profile {profile}',
            "",
            "curl -fsSL https://get.docker.com/ | sh",
            "sudo service docker restart",
            "",
            "sudo usermod -a -G docker ubuntu",
            "",
            "sudo chmod 666 /var/run/docker.sock",
            "",
            'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose',
            "sudo chmod +x /usr/local/bin/docker-compose",
            "sudo chmod +x /usr/local/bin/docker",
            "",
            "cd /home/ubuntu",
            install_oasislmf_line,
            "pip3 install git+https://github.com/OasisLMF/gerund"
            "",
            "",
            'ssh-keyscan -H "github.com" >> ~/.ssh/known_hosts',
            "",
            f"git clone {repository}",
            "",
            data_line,
            "PATH=$PATH:~/.local/bin/",
            "echo FINISHED > output.txt"
        ]
        for line in lines:
            self.write_line(line=line)

    def write_line(self, line: str) -> None:
        """
        Writes a line to the bash script.
        Notes:
            do not add a new line delimiter at the end as this is already added in this function.

        Args:
            line: (str) line to be added to the bash script

        Returns: None
        """
        self.append(line + "\n")

    def write_script(self, file_path: str) -> None:
        """
        Writes entire content to a file.

        Args:
            file_path: (str) path of the file being written to

        Returns: None
        """
        with open(file_path, "w") as file:
            file.write(str(self))

    @property
    def stripped(self) -> List[str]:
        buffer = []
        for i in self[1:]:
            i = i.replace("\n", "")
            if i != "":
                buffer.append(i)
        return buffer

    def _format(self) -> str:
        return "".join(self)

    def __repr__(self):
        return self._format()

    def __str__(self):
        return self._format()
