"""
This script configure the minecraft server's config files, and run the server.
"""
#!/usr/bin/env python
from subprocess import Popen, PIPE, STDOUT
import os
import argparse
import fileinput
import re
import json

## path to this script
__workdir__ = os.path.dirname(os.path.realpath(__file__))
__eula_file__ = __workdir__ + '/minecraft-server/eula.txt'
__server_properties_file__ = __workdir__ + '/minecraft-server/server.properties'
__ops_file__ = __workdir__ + '/minecraft-server/ops.json'
__whitelist_file__ = __workdir__ + '/minecraft-server/whitelist.json'

def search_and_replace(file_path, regex, new_line):
    """ Search for a pattern in the file, and replace with a new line """
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            print(re.sub(regex, new_line, line), end='')

def add_player(arg_file, arg_player, ops):
    """
    Append a player to an array of a json file,
    the player is composed of the uuid and the name separated by a :
    """
    file = open(arg_file, 'r+')
    player_list = json.load(file)
    split = re.split(':', arg_player)
    if ops:
        player = json.loads('{ "uuid":"'+split[0]+'","name":"'+split[1]+'","level":"'+split[2]+'"}')
    else:
        player = json.loads('{ "uuid" : "'+split[0]+'", "name" : "'+split[1]+'"}')
    player_list.append(player)
    file.seek(0) ## put the pointer at the beginning to overwrite
    file.write(json.dumps(player_list))
    file.close()

# #######################################################################
# ######################### server.properties ###########################
# #######################################################################

def set_difficulty(arg_value):
    """ Configure the value of the attribute "difficulty" in the file server.properties. """
    if arg_value:
        valid_arg = True
        if arg_value == 'peaceful':
            difficulty_int = '0'
        elif arg_value == 'easy':
            difficulty_int = '1'
        elif arg_value == 'normal':
            difficulty_int = '2'
        elif arg_value == 'hard':
            difficulty_int = '3'
        else:
            print('[ERROR] Invalid value for difficulty')
            valid_arg = False
        if valid_arg:
            search_and_replace(
                __server_properties_file__,
                r'difficulty=.*$',
                'difficulty='+difficulty_int
            )

def set_gamemode(arg_value):
    """ Configure the value of the attribute "gamemode" in the file server.properties. """
    if arg_value:
        valid_arg = True
        if arg_value == 'survival':
            gamemode_int = '0'
        elif arg_value == 'creative':
            gamemode_int = '1'
        elif arg_value == 'adventure':
            gamemode_int = '2'
        elif arg_value == 'spectator':
            gamemode_int = '3'
        else:
            print('[ERROR] Invalid value for gamemode')
            valid_arg = False
        if valid_arg:
            search_and_replace(
                __server_properties_file__,
                r'gamemode=.*$',
                'gamemode='+gamemode_int
            )

def set_pvp(arg_value):
    """ Configure the value of the attribute "pvp" in the file server.properties. """
    if arg_value:
        if (arg_value == 'true') or (arg_value == 'false'):
            search_and_replace(
                __server_properties_file__,
                r'pvp=.*$',
                'pvp='+arg_value
            )
        else:
            print('[ERROR] Invalid value for pvp')

def set_whitelist(arg_value):
    """ Configure the value of the attribute "white-list" in the file server.properties. """
    if arg_value:
        if (arg_value == 'true') or (arg_value == 'false'):
            search_and_replace(
                __server_properties_file__,
                r'white-list=.*$',
                'white-list='+arg_value
            )
        else:
            print('[ERROR] Invalid value for whitelist')

def set_server_port(arg_value):
    """ Configure the value of the attribute "server-port" in the file server.properties. """
    ## TODO specify an available range of ports
    if arg_value:
        is_int = False
        try:
            int(arg_value)
            is_int = True
        except ValueError:
            print('[ERROR] The server must be an integer')
        if is_int:
            search_and_replace(
                __server_properties_file__,
                r'server-port=.*$',
                'server-port='+arg_value
            )
        else:
            print('[ERROR] Invalid value for server port')

def set_online_mode(arg_value):
    """ Configure the value of the attribute "online-mode" in the file server.properties. """
    if arg_value:
        if (arg_value == 'true') or (arg_value == 'false'):
            search_and_replace(
                __server_properties_file__,
                r'online-mode=.*$',
                'online-mode='+arg_value
            )
        else:
            print('[ERROR] Invalid value for online mode')

# #######################################################################
# ############################### ops.json ##############################
# #######################################################################

def add_player_ops(arg_value):
    """ Add a player to the whitelist, the uuid and the name are to be specified """
    ## TODO check arg_value is valid
    if arg_value:
        add_player(__ops_file__, arg_value, True)

# #######################################################################
# ########################### whitelist.json ############################
# #######################################################################

def add_player_whitelist(arg_value):
    """ Add a player to the whitelist, the uuid and the name are to be specified """
    ## TODO check arg_value is valid
    if arg_value:
        add_player(__whitelist_file__, arg_value, False)

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
        if (arg_value == 'true') or (arg_value == 'false'):
            search_and_replace(__eula_file__, r'eula=.*$', 'eula='+arg_value)
        else:
            print('[ERROR] Invalid value for eula')

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
    '--pvp',
    default='true',
    help='set the pvp option of the server'
)
__parser__.add_argument(
    '--whitelist',
    default='false',
    help='set the whitelist option of the server'
)
__parser__.add_argument(
    '--port',
    default='25565',
    help='set the server-port of the server'
)
__parser__.add_argument(
    '--onlinemode',
    default='false',
    help='set the online-mode option of the server'
)

__parser__.add_argument(
    '-o', '--ops',
    help='add a player to the ops.json file, using the format [UUID]:[NAME]:[LEVEL]'
)
__parser__.add_argument(
    '-w', '-p', '--player',
    help='add a player to the whitelist.json file, , using the format [UUID]:[NAME]'
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
set_pvp(__args__.pvp)
set_whitelist(__args__.whitelist)
set_server_port(__args__.port)
set_online_mode(__args__.onlinemode)
add_player_ops(__args__.ops)
add_player_whitelist(__args__.player)

set_eula(__args__.eula)

# #######################################################################
# ########################## run the server #############################
# #######################################################################

def run():
    """ Start the minecraft server. """
    ## TODO add an argument to change the allocated memory 
    process = Popen(
        [
            "java", "-Xmx1024M", "-Xms1024M", "-jar",
            "minecraft-server.jar",
            "nogui"
        ],
        cwd=__workdir__ +"/minecraft-server/",
        stdout=PIPE,
        stderr=STDOUT
    )

    for log in process.stdout:
        print(log)

run()
