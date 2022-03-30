from typing import Optional
from subprocess import Popen


class RunScriptOnServer:

    def __init__(self, input_params: dict, terraform_data: dict, location: str) -> None:
        self.server_ip: Optional[str] = None
        self.script_name: Optional[str] = None
        self.location = location
        self.parameters: Optional[dict] = None
        self._process_inputs(input_data=input_params, terraform_dict=terraform_data)

    def _process_inputs(self, input_data: dict, terraform_dict: dict):
        self.server_ip = terraform_dict["main_server_ip"]["value"][0]
        self.script_name = input_data["script_name"]
        self.parameters = input_data.get("variables", {})

    def run(self) -> None:
        add_to_known_hosts = Popen(f'ssh-keyscan -H "{self.server_ip}" >> ~/.ssh/known_hosts', shell=True)
        add_to_known_hosts.wait()

        copy_to_server = Popen(f"scp {self.location}/{self.script_name}.py ubuntu@{self.server_ip}:/home/ubuntu/{self.script_name}.py",
                               shell=True)
        copy_to_server.wait()

        command = f"cd /home/ubuntu/ && python3 {self.script_name}.py"
        buffer = list()
        buffer.append(command)

        for param_key in self.parameters.keys():
            buffer.append(f" --{param_key} {self.parameters[param_key]}")

        command = "".join(buffer)

        run_script = Popen(f"ssh -A -o StrictHostKeyChecking=no ubuntu@{self.server_ip} '{command}'", shell=True)
        run_script.wait()
