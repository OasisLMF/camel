# Steps
When we run a model we run a series steps. Below are the steps that are currently supported:

## Run Script step
This is where we run a Python script on the server that we have just spun up for the model.

Below is an example of how we run a script in our config file:
```yaml
steps:
  - name: run_script
    script_name: run_model
    env_vars:
      OASIS_WORKER_VERSION: "1.26.3"
      OASIS_UI_VERSION: "1.11.3"
      OASIS_PLATFORM_VERSION: "1.26.3"
    variables:
      git_branch: "develop"
      key: "=>aws_access_key"
      secret_key: "=>aws_secret_access_key"
```
Above we can see that we have a step called `run_script` and we are running a script called `run_model`. 
We are also passing in some environment variables and some variables that we have defined in our config file.

This step would translate to the following command:
```bash
export OASIS_WORKER_VERSION=1.26.3
export OASIS_UI_VERSION=1.11.3
export OASIS_PLATFORM_VERSION=1.26.3

python camel/terra/terra_builds/run_model.py --git_branch develop --key <aws_access_key> --secret_key <aws_secret_access_key>
```
The location is fixed to the `camel/terra/terra_builds` directory. If we want to run a script in a different directory 
we can use the `run_local_script` step.

## Run Local Script step
This is exactly the same as the `run_script` step but it allows us to run a script in a different directory with
the following example in our config file:
```yaml
steps:
  - name: run_local_script
    script_name: run_model
    script_location: some/other/directory
    env_vars:
      OASIS_WORKER_VERSION: "1.26.3"
      OASIS_UI_VERSION: "1.11.3"
      OASIS_PLATFORM_VERSION: "1.26.3"
    variables:
      git_branch: "develop"
      key: "=>aws_access_key"
      secret_key: "=>aws_secret_access_key"
```
This step would translate to the following command:
```bash
export OASIS_WORKER_VERSION=1.26.3
export OASIS_UI_VERSION=1.11.3
export OASIS_PLATFORM_VERSION=1.26.3

python some/other/directory/run_model.py --git_branch develop --key <aws_access_key> --secret_key <aws_secret_access_key>
```

## Print step
This is a step that allows us to print out a message to the console. This can be local or on the server.
This has the following example in our config file:
```yaml
steps:
  - name: print
    statement: "Hello World"
  - name: print
    statement: "=>finished"
  - name: print
    statement: ">>finished"
```
This gives us three steps. The first step will print out `Hello World` to the console. The second step will print out
what variable is in the local storage for the profile under the key `finished`. The third step will print out what
is stored on the server in the file `finished.txt`.

## Destroy build step
This step will destroy the server that has been built. This can be achieved by the following example in our config file:
```yaml
steps:
  - name: destroy_build
```

## Run server command step
Here we can run a command on the server that we have just spun up for the model. This can be achieved by the following
example in our config file:
```yaml
steps:
  - name: run_server_command
    command: "ls -la"
    env_vars:
      OASIS_WORKER_VERSION: "1.26.3"
      OASIS_UI_VERSION: "1.11.3"
      OASIS_PLATFORM_VERSION: "1.26.3"
```
This will give us the following command:
```bash
ssh -o StrictHostKeyChecking=no -i /Users/username/.ssh/id_rsa ubuntu@<server_ip> 'export OASIS_WORKER_VERSION=1.26.3 && export OASIS_UI_VERSION=1.11.3 && export OASIS_PLATFORM_VERSION=1.26.3 && ls -la'
```
The environment variables are set before the command is run. The IP address of the server is the server that we have
built for the model.

## Conditional step
This step allows us to run a step if a condition is met. This can be achieved by the following example in our config file:
```yaml
steps:
  - name: conditional
    operator: ==
    variable: '>>output'
    value: FINISHED
    step_data:
      name: print
      statement: the process is finished
```
This checks the ```output.txt``` file on the server and checks if the value is equal to ```FINISHED```. If it is then
we print out the statement ```the process is finished```. We also support the not equal to operator ```!=```. We
have used the ```print``` step as an example but we can use any step that we want.

## Test model step
This is where we test a model script. These are specific scripts that have been purposefully written to 
test a model in a generic way. This means that we can pass in a number of variables to test any generic model.
These scripts are held in the ```camel/terra/steps/model_runs/server_scripts``` directory. We can run a test model
step by the following example in our config file:
```yaml
steps:
  - name: some_test_model
    env_vars:
      OASIS_WORKER_VERSION: "1.26.3"
      OASIS_UI_VERSION: "1.11.3"
      OASIS_PLATFORM_VERSION: "1.26.3"
    script_name: run_api_test_1
    variables:
      git_branch: "develop"
      parent_dir: "/home/ubuntu/some_provider"
      test_dir: "/home/ubuntu/some_provider/example/tests/test_1"
      expected_md5: "/home/ubuntu/some_provider/example/expected/1-26-3/expected.md5"
      worker_name: "example_worker"
      worker_dockerfile: "/home/ubuntu/some_provider/docker/Dockerfile.some_provider_example_worker"
      docker_compose_platform: "/home/ubuntu/some_provider/docker/docker-compose.yml"
      docker_compose_worker: "/home/ubuntu/some_provider/docker/docker-compose_example.yml"
      docker_compose_ui: "/home/ubuntu/some_provider/docker/docker-compose_ui.yml"
```
Here we can see that we are running a script called `run_api_test_1.py`. We can also see that we have called our 
step ```some_test_model```. If our step name contains ```test_model``` then the step will look for scripts
in the ```camel/terra/steps/model_runs/server_scripts``` directory. If we do not have all of the variables that
are required for the script then the step will refuse to run. If you want to run custom model tests that are not
supported then it is best to either crease on or use the local script step.
