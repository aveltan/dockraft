"""
This script configure the minecraft server's config files, and run the server.
"""
#!/usr/bin/env python
from subprocess import Popen, PIPE, STDOUT
import os
import argparse
import fileinput
import re

## path to this script
__workdir__ = os.path.dirname(os.path.realpath(__file__))
__eula_file__ = __workdir__ + '/minecraft-server/eula.txt'
__server_properties_file__ = __workdir__ + '/minecraft-server/server.properties'

def search_and_replace(file_path, regex, new_line):
    """ Search for a pattern in the file, and replace with a new line """
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            # line = re.sub(regex, new_line, line)
            # print(line.replace(regex, new_line), end='')
            print(re.sub(regex, new_line, line), end='')

# #######################################################################
# ######################### server.properties ###########################
# #######################################################################

def set_difficulty(arg_value):
    """ Configure the value of the attribute "difficulty" in the file server.properties. """
    if arg_value:
        if arg_value == 'peaceful':
            difficulty_int = '0'
        elif arg_value == 'easy':
            difficulty_int = '1'
        elif arg_value == 'normal':
            difficulty_int = '2'
        elif arg_value == 'hard':
            difficulty_int = '3'
        else:
            print('Invalid value for difficulty')
        search_and_replace(
            __server_properties_file__,
            r'difficulty=.*$',
            'difficulty='+difficulty_int
        )

def set_gamemode(arg_value):
    """ Configure the value of the attribute "gamemode" in the file server.properties. """
    if arg_value:
        if arg_value == 'survival':
            difficulty_int = '0'
        elif arg_value == 'creative':
            difficulty_int = '1'
        elif arg_value == 'adventure':
            difficulty_int = '2'
        elif arg_value == 'spectator':
            difficulty_int = '3'
        else:
            print('Invalid value for difficulty')
        search_and_replace(
            __server_properties_file__,
            r'gamemode=.*$',
            'gamemode='+difficulty_int
        )

# #######################################################################
# ############################### eula.txt ##############################
# #######################################################################

def set_eula(arg_value):
    """ Configure the value of the attribute "eula" in the file eula.txt. """
    if arg_value:
        if arg_value == 'true':
            print(
                "By passing 'true' to the --eula argument, "\
                "you're therefore accepting the Minecraft server's EULA."
            )
        else:
            print(
                "You haven't passed 'true' to the --eula argument,"\
                "meaning that you haven't agreed to the Minecraft server's EULA."
            )
        search_and_replace(__eula_file__, r'eula=.*$', 'eula='+arg_value)

# #######################################################################
# ########################## script arguments ###########################
# #######################################################################

__parser__ = argparse.ArgumentParser(description='Start a Minecraft server.')

# ######################### adding the arguments ########################

__parser__.add_argument(
    '-d', '--difficulty',
    default='normal',
    help='set the difficulty of the server'
)

__parser__.add_argument(
    '-g', '--gamemode',
    default='survival',
    help='set the gamemode of the server'
)

__parser__.add_argument(
    '--eula',
    action='store',
    default='false',
    help='by specifying True, the user accepts the Minecraft server\'s EULA.'
)

# ####################### run the configuration #########################

__args__ = __parser__.parse_args()

set_difficulty(__args__.difficulty)
set_gamemode(__args__.gamemode)

set_eula(__args__.eula)

# #######################################################################
# ########################## run the server #############################
# #######################################################################

def run():
    """ Start the minecraft server. """
    process = Popen(
        [
            "java", "-Xmx512M", "-Xms512M", "-jar",
            __workdir__ +"/minecraft-server/minecraft-server.jar",
            "nogui"
        ],
        stdout=PIPE,
        stderr=STDOUT
    )

    for log in process.stdout:
        print(log)
