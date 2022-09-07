"""
This file defines the class responsible for generating bash scripts for building servers.
"""
from typing import Optional


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

    def generate_script(self, oasislmf_version: Optional[str]) -> None:
        """
        Fills up the self with the lines needed to create a bash script.
        Notes:
            if you want to add parameters to the bash script in future pass them into this function and format the
            lines that you want with the parameters

        oasis_version: (Optional[str]) the version of aosis you want installed is None will be latest version

        Returns: None
        """
        if oasislmf_version is None:
            install_oasislmf_line = "pip3 install oasislmf[extra]"
        else:
            install_oasislmf_line = f"pip3 install oasislmf[extra]=={oasislmf_version}"

        lines = [
            "#!/bin/bash",
            "",
            "sudo apt-get update -y",
            "sudo apt-get install git -y",
            "sudo apt-get install vim -y",
            "sudo apt-get install tmux -y ",
            "sudo apt-get install ca-certificates -y",
            "sudo apt-get install curl -y",
            "sudo apt-get install gnupg -y",
            "sudo apt-get install lsb-release -y",
            "sudo apt install python3.8-venv -y",
            "sudo apt install python3-pip -y",
            "sudo apt install awscli -y",
            "",
            "curl -fsSL https://get.docker.com/ | sh",
            "sudo service docker restart",
            "",
            "sudo usermod -a -G docker ec2-user",
            "",
            'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose',
            "sudo chmod +x /usr/local/bin/docker-compose",
            "sudo chmod +x /usr/local/bin/docker",
            "",
            "cd /home/ubuntu",
            "PATH=$PATH:~/.local/bin",
            install_oasislmf_line,
            "pip3 install pyarrow",
            "pip3 install numba",
            "",
            "",
            "# sudo -u ubuntu git clone https://github.com/OasisLMF/BangladeshCyclone.git",
            "",
            "# aws s3 cp --recursive s3://oasislmf-model-library-iki-bgwtcss1 /home/ubuntu/BangladeshCyclone/BGWTCSS1/",
            'ssh-keyscan -H "github.com" >> ~/.ssh/known_hosts',
            "",
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

    def _format(self) -> str:
        return "".join(self)

    def __repr__(self):
        return self._format()

    def __str__(self):
        return self._format()
