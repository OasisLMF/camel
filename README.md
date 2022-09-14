# camel
Camel is a command line tool that automates processes for developers in our organisation. The have this tool in order 
to not only automate processes, but it reduces errors. I also acts as a sort of self documentation. Keeping 
documentation on processes up to date can be tiring. You need to get the process working and then it's all too 
tempting to move onto the next feature or start using it instead of updating the documentation. This documentation 
lag can be completely cut with well-structured code that performs our processes. Someone can instantly see the most 
uptodate process we use by just looking at the code that executes this process. However, before we use it we have 
to work with profiles. 

## Profiles 
Profiles is what camel is built on. Each profile houses configs for the processes that we execute. You cannot 
do anything unless you have a profile and your current profile has to be pointed to a valid profile. This is why every 
help section has a list of available profiles and the current profile that camel is pointing to. Running the 
```cml``` command gives us the following printout:

```commandline
❯ cml

                     ,,__
           ..  ..   / o._)                   .---.
          /--'/--\  \-'||        .----.    .'     '.
         /        \_/ / |      .'      '..'         '-.
       .'\  \__\  __.'.'     .'          “-._
         )\ |  )\ |      _.'
        // \ // \
       ||_  \|_  \_
       '--' '--'' '--' 


                                                                                
      ############      %####%%#%%%%%       /%%%%%%%%%%%%%%%%      %%%%%%%%%%%% 
   ####          #### ###/         .%%%    #%%             %%%   %%%            
  ###              ####/             .%%%   %%%             %%    %%#           
 ###                ###               #%%    /%%%%%%        %%     %%%%%%(      
 /##                ###                #%          %%%%%    %%          ,%%%%%  
  ###              ####%               ##             %%%   %%              %%% 
   .###(        /###. ####         %#  ##%            %%%   %%#             %%% 
      ############       ###########    ########%%%%%%%      *%%%%%%%%%%%%%%%  


current profile: maxwell

available profiles:
maxwell
terraform-dev

available commands:
cml-profile => manages the profile
cml-ssh => manages ssh configurations
cml-terra => manages terraform builds
cml-repo => manages local repo operations

```
Now that we have looked at the main interface we can access what is supported in profiles by running the 
```cml-profile``` command giving us the printout below:
```commandline
❯ cml-profile

current profile: maxwell

available profiles:
maxwell
terraform-dev

available commands:
cml-profile-create => creates a new profile
cml-profile-switch => switches the current profile to a new one
cml-profile-delete => deletes a profile wiping all data associated with the profile
```
This is the last level of general help commands. Once you are one level off the main help menu all commands listed 
will execute a process and will sometimes require arguments. We can access help on how to run these commands with the 
```-h``` argument. For instance, we can see what arguments are required for the ```cml-profile-create``` command 
by running ```cml-profile-create -h``` which will give out the following printout:
```commandline
❯ cml-profile-create -h
usage: cml-profile-create [-h] --name NAME

optional arguments:
  -h, --help   show this help message and exit
  --name NAME  the name of the profile being created
```
Here we can see that we need to provide a name under the argument ```--name```. With this help approach whenever 
new processes are added or updated, a user will be able to see what is needed instead of asking around for documentation
or seeing if there are changes in release notes, you can just directly look at what commands are available right now. 
This also enables us to version our processes. For instance, we can keep running old processes in some pipelines or 
servers by merely having an older version of camel running. A user can instantly get to grips with what is available
and how its done by merely routing through the version being used.

## Exporting profiles 
In the future we hope to support export and importing of profiles. This will enable us to transfer configs, files, and 
data under a certain profile to another user onboarding and standardising processes. 

## Terraform 
Camel supports terraform. The most recent commands available can be seen by running the ```cml-terra``` command.
However, what is not covered and needs further explanation is the config files for terra builds. Later on we will 
work on storing these config files in the profile storage just like the SSH configs. For now, we just need to point to 
terraform configs for running builds. A example of a terraform config file takes the form below:

```commandline
location: model_runs/BGEQ
oasis_version: "1.26"
variables:
    aws_access_key: "=>aws_access_key"
    aws_secret_access_key: "=>aws_secret_access_key"
    subnet_id: some_subnet_id
    server_security_group: some_security_group_id
local_vars:
    - name: output
      path: "/home/ubuntu/"
      ip_address: true
steps:
    - name: run_server_command
      command: echo 'export OASIS_UI_VERSION="1.11.3"' >> ~/.bashrc && echo 'export OASIS_WORKER_VERSION="1.26.2"' >> ~/.bashrc && echo 'export OASIS_PLATFORM_VERSION="1.26.2"' >>~/.bashrc
    - name: run_script
      script_name: run_model
      variables:
              key: "=>aws_access_key"
              secret_key: "=>aws_secret_access_key"
    - name: conditional
      operator: "=="
      variable: ">>output"
      value: "FINISHED"
      step_data:
              name: print
              statement: "the process is finished"
    - name: run_server_command
      command: 'cd {=>directory} && echo "{>>output}"'
    - name: conditional
      operator: "=="
      variable: ">>output"
      value: "FINISHED"
      step_data:
              name: destroy_build
```
What we first need to note is the ```location``` field. This is the location of the build in the camel repo. The 
base path of the ```location``` is [here](https://github.com/OasisLMF/camel/tree/main/camel/terra/terra_builds). Your
path that the ```location``` field has to point to is a path leading to the ```main.tf``` file of that build. 
To demonstrate this, we can revisit our location definition below:
```commandline
location: model_runs/BGEQ
```
This will tell camel to look for a ```main.tf``` file 
[here](https://github.com/OasisLMF/camel/tree/main/camel/terra/terra_builds/model_runs/pariswindstorm). We can now 
move onto the next field which is ```variables```. This is merely a dictionary of variables passed into the terraform 
build. Continuing our Paris Windstorm model example, we can look a what variables are needed in the 
```variables.tf``` file in the build as seen 
[here](https://github.com/OasisLMF/camel/blob/main/camel/terra/terra_builds/model_runs/pariswindstorm/variables.tf). 
It must be noted here that we are working on passing in keys in different ways as they are needed for all builds. Also, 
they keys are noted as secrets so they will not show up in the terraform logs. With this covered, we can now move onto 
the final section which is ```steps```. This field is a list. They have a ```name``` field which is the name of the 
step that is suppoorted. If you want to see what steps are available they can be seen 
[here](https://github.com/OasisLMF/camel/blob/3136fcfddd4e33eb44124706080aedcc35a344b8/camel/terra/steps/__init__.py#L59)
Our example config file runs a python script on a server that has been created. The ```run_model``` script is a 
python script in the terraform build that we are running which can be found 
[here](https://github.com/OasisLMF/camel/blob/main/camel/terra/terra_builds/model_runs/pariswindstorm/run_model.py).
More steps will be added in time. 

We also must state that ```oasis_version``` is optional. If you do not supply a version the latest version will be used
as default. The ```oasis_version``` is the version of ```oasislmf``` from pypi.

When it comes to our ```run_server_command``` step this is running a command on the recently created server. We
can see that right now we are exporting a range of global environment variables into the server. We should work on
creating an environment variable step to organise the variables better.

## Creating a model 
Camel now supports model templates. To create a model template carry out the following command: 
```bash
cml-model-build --name <NAME_OF_MODEL>
```
This will produce a template folder will all the files needed to build a model that will run on a server created by 
terraform. All files are annotated and the example ```config.yml``` in the package. Once you have altered the files 
to enable your model to run, you will have to load it into your camel package with the following command:
```bash
cml-model-load --name <NAME_OF_MODEL>
```
This loads the model package into the camel package so it can be referenced in model builds. You will also be asked if 
you want to add the config in the model package. If you put in ```y``` to this answer it will be loaded into our 
```tconfig```. 

## AWS authentication 
We are looking into handling profiles and aws authentication using the following guide:
https://blog.gruntwork.io/authenticating-to-aws-with-the-credentials-file-d16c0fbcbf9e


