import os
from unittest import main, TestCase
from unittest.mock import patch

from camel.terra.config_loader import ConfigEngine


class TestConfigEngine(TestCase):

    @patch("camel.terra.config_loader.ConfigEngine._read")
    def setUp(self, mock__read) -> None:
        self.path = f"{os.path.dirname(os.path.abspath(__file__))}/config.yml"
        self.test = ConfigEngine(config_path=self.path)
        self.data = {
            'location': 'model_runs/BGEQ',
            'oasis_version': '1.26',
            'variables': {
                'aws_access_key': '=>aws_access_key',
                'aws_secret_access_key': '=>aws_secret_access_key',
                'subnet_id': 'some_subnet_id',
                'server_security_group': 'some_security_group_id'
            },
            'local_vars': [
                {'name': 'output', 'path': '/home/ubuntu/', 'ip_address': True}
            ],
            'steps': [
                {
                    'name': 'run_server_command',
                    'command': 'echo \'export OASIS_UI_VERSION="1.11.3"\' >> ~/.bashrc && echo \'export'
                               ' OASIS_WORKER_VERSION="1.26.2"\' >> ~/.bashrc && echo \'export '
                               'OASIS_PLATFORM_VERSION="1.26.2"\' >>~/.bashrc'
                },
                {
                    'name': 'run_script',
                    'script_name': 'run_model',
                    'variables': {
                        'key': '=>aws_access_key',
                        'secret_key': '=>aws_secret_access_key'
                    }
                },
                {
                    'name': 'conditional',
                    'operator': '==',
                    'variable': '>>output',
                    'value': 'FINISHED',
                    'step_data': {
                        'name': 'print',
                        'statement': 'the process is finished'
                    }
                },
                {
                    'name': 'run_server_command',
                    'command': 'cd {=>directory} && echo "{>>output}"'
                },
                {
                    'name': 'conditional',
                    'operator': '==',
                    'variable': '>>output',
                    'value': 'FINISHED',
                    'step_data': {
                        'name': 'destroy_build'
                    }
                }
            ]
        }

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual({}, self.test)
        self.assertEqual(self.path, self.test.config_path)
        self.assertEqual(None, self.test.location)

    def test__read(self):
        test = ConfigEngine(config_path=self.path)
        self.assertEqual(self.data, test)

    def test_steps(self):
        test = ConfigEngine(config_path=self.path)
        self.assertEqual(self.data["steps"], test.steps)


if __name__ == "__main__":
    main()
