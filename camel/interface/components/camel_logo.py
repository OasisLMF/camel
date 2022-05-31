"""
This file defines a basic function a prints out the Camel logo for display to the terminal.
"""
from termcolor import colored


IMAGE = """
                     ,,__
           ..  ..   / o._)                   .---.
          /--'/--\  \-'||        .----.    .'     '.
         /        \_/ / |      .'      '..'         '-.
       .'\  \__\  __.'.'     .'          “-._
         )\ |  )\ |      _.'
        // \ // \\
       ||_  \|_  \_
       '--' '--'' '--' 
"""


def print_camel_image() -> None:
    """
    Prints out the Camel logo to the terminal in red.

    :returns: None
    """
    print(colored(IMAGE, 'red'))
