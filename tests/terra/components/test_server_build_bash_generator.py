from unittest import main, TestCase

from camel.terra.components.server_build_bash_generator import ServerBuildBashGenerator


class TestServerBuildBashGenerator(TestCase):

    def setUp(self) -> None:
        self.test = ServerBuildBashGenerator()

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual([], self.test)

    def test_write_line(self):
        self.test.write_line(line="this is the first line")
        self.test.write_line(line="this is the second line")

        expected_outcome = ['this is the first line\n', 'this is the second line\n']
        self.assertEqual(expected_outcome, self.test)

    def test_generate_script(self):
        self.test.generate_script(repository="test/repo", oasislmf_version="1.26",
                                  aws_key="AWS_KEY", aws_secret_key="AWS_SECRET_KEY")
        self.assertEqual("".join(self.test), str(self.test))

    def test_strip(self):
        expected_outcome = [
            'sudo apt-get update -y',
            'sudo apt-get install git -y',
            'sudo apt-get install vim -y',
            'sudo apt-get install tmux -y ',
            'sudo apt-get install ca-certificates -y',
            'sudo apt-get install curl -y',
            'sudo apt-get install gnupg -y',
            'sudo apt-get install lsb-release -y',
            'sudo apt-get install python3-venv -y',
            'sudo apt-get install python3-pip -y',
            'sudo apt-get install awscli -y',
            'aws configure set aws_access_key_id "AWS_KEY" --profile default',
            'aws configure set aws_secret_access_key "AWS_SECRET_KEY" --profile default',
            'curl -fsSL https://get.docker.com/ | sh',
            'sudo service docker restart',
            'sudo usermod -a -G docker ubuntu',
            'sudo chmod 666 /var/run/docker.sock',
            'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2'
            '/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose',
            'sudo chmod +x /usr/local/bin/docker-compose',
            'sudo chmod +x /usr/local/bin/docker',
            'cd /home/ubuntu', 'pip3 install oasislmf[extra]==1.26',
            'pip3 install git+https://github.com/OasisLMF/gerund',
            'ssh-keyscan -H "github.com" >> ~/.ssh/known_hosts',
            'git clone test/repo',
            'echo FINISHED > output.txt'
        ]

        self.test.generate_script(repository="test/repo", oasislmf_version="1.26",
                                  aws_key="AWS_KEY", aws_secret_key="AWS_SECRET_KEY")
        self.assertEqual(expected_outcome, self.test.stripped)


if __name__ == "__main__":
    main()
