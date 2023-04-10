# -*- coding: utf-8 -*-
"""
           _.-'~~~~~~`-._
          /      ||      \
         /       ||       \
        |        ||        |
        | _______||_______ |
        |/ ----- \/ ----- \|
       /  (     )  (     )  \
      / \  ----- () -----  / \
     /   \      /||\      /   \
    /     \    /||||\    /     \
   /       \  /||||||\  /       \
  /_        \o========o/        _\
    `--...__|`-._  _.-'|__...--'
            |    `'    |
            

ENSENSIA Learning Packages (LP)

Foundation for Research and Technology Hellas (FORTH)
Institute of Chemical Engineering Sciences (ICE-HT)

© all rights reserved
@author: japostol

Do not distribute, reproduce, or expose this code

"""

def get_options ():
    OPTIONS = {
                'verbose'      : True,
                'to_server'    : True,
                'to_log_file'  : True
                }
    return OPTIONS


def communicate_title (message):
    print ('')
    print (message)
    print ('...')
    
def communicate_message (message):
    print (message)