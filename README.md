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
