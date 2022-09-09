"""
This file defines a basic function a prints out the Ten logo for display to the terminal.
"""
from termcolor import colored

IMAGE = """                                                                                                                      
                                **                            
                               ****                             
                              *******                          
                            **********                         
                          *************                        
                     ******   ***********                   
                ,*****      **************                
           ,*****          *** *************  ,                
             ****         ***  **************                 
               ***,      **    ***************                 
                ****   ***     *****************            
                 **** ***      ******************             
               *********       ********************         
              *********        *********************              
             *********         **********************.          
"""


def print_tent_image() -> None:
    """
    Prints out the Tent logo to the terminal in red.

    :returns: None
    """
    print(colored(IMAGE, 'red'))
