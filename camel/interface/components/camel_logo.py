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


def print_camel_image():
    print(colored(IMAGE, 'red'))
