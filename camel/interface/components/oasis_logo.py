"""
This file defines a basic function a prints out the OASIS logo for display to the terminal.
"""
from termcolor import colored


IMAGE = """                                                            
      ############      %####%%#%%%%%       /%%%%%%%%%%%%%%%%      %%%%%%%%%%%% 
   ####          #### ###/         .%%%    #%%             %%%   %%%            
  ###              ####/             .%%%   %%%             %%    %%#           
 ###                ###               #%%    /%%%%%%        %%     %%%%%%(      
 /##                ###                #%          %%%%%    %%          ,%%%%%  
  ###              ####%               ##             %%%   %%              %%% 
   .###(        /###. ####         %#  ##%            %%%   %%#             %%% 
      ############       ###########    ########%%%%%%%      *%%%%%%%%%%%%%%%  
"""


def print_logo_image() -> None:
    """
    Prints out the Camel logo to the terminal in red.

    :returns: None
    """
    print(colored(IMAGE, 'red'))
