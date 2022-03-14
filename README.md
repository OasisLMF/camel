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

