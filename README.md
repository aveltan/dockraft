## Supported tags and respective ``` Dockerfile ``` links  

 - ``` latest ``` [(Dockerfile)][DockerfileLatest]

## Quick references

- **Where to get help:**  
[the Docker Community Forums](https://forums.docker.com/), [the Docker Community 
Slack](https://blog.docker.com/2016/11/introducing-docker-community-directory-docker-community-slack/), or [Stack Overflow](https://stackoverflow.com/search?tab=newest&q=docker)
- **Where to file issues:**
[https://github.com/aveltan/dockraft/issues][DockraftIssues]
- **Maintained by:**
[aveltan]
- **Published image artifact details:**
- **Source of this description:**
[https://github.com/aveltan/dockraft][Dockraft]
- **Supported Docker versions:**
 

# Dockraft

Launch a Minecraft server in a docker container. You can pass argument to the ``` docker run ``` command to configure the server before start. The available arguments 
are specified in the section below.

## How to use this image

### Start the Minecraft server
This is how you can run the container :
```
$ docker run -P  aveltan/dockraft --eula=true
```
The ```-P``` option exposes the default port of the container, which is the port ```25565```.

By by passing the argument ```--eula``` the setting below to ```true```, you are indicating your agreement to Mojang's EULA (https://account.mojang.com/documents/minecraft_eula).

### Useful Docker arguments

The ```-p``` options exposes a specific container port and you can redirect to a host port to make it accessible from outside. It takes the format 
```<host_port>:<container_port>```. It gives you the possibility to run multiple servers using different ports on the host.

The ```--name``` option changes the name of the container, making it easier to find it later.  

The ```-d``` option runs the container in the background. As you cannot see the ```STDOUT``` output in the terminal, you can check it using the ```docker log``` command.

### Script arguments

You can find help by passing ```-h``` or ```--help``` to the script.
#### EULA

The ```--eula``` argument changes the value of the ```eula``` field in the ```eula.txt``` file. It means that you agree to the Mojang's [EULA]. You can pass ```true``` or 
```false```.

#### Server properties
The following arguments change the values in the ```server.properties``` file. For more informations you can check the official Minecrat wiki about 
[server.properties][MinecraftWikiServerProperties].
___
The ```--whitelist``` argument indicates whether or not you want to activate the white-list. If ```true```, only players registered in the ```whitelist.json``` wiill be able to 
connect to the server.  

The ```--onlinemode``` argument tells if the server will connect the players using the Minecraft's account database, if ```true```.

The ```pvp``` argument allows the players to kill each other if set to ```true```.

The ```-g``` or ```--gamemode``` arguments change the gamemode of the server, you have the choice between ```survival```, ```creative```, ```adventure``` or ```spectator```.

The ```-d```, ```--difficulty``` arguments change the difficulty of the server, you have the choice between ```peaceful```, ```easy```, ```normal``` or ```hard```.

#### White-list
The ```-w```, ```-p```, ```--player``` argument adds a new player to the ```whitelist.json``` file, it takes the form ```<uuid>:<name>```. You can determine a player **uuid** using 
the online tool on [mcuuid.net](https://mcuuid.net).

#### Ops
The ```-o```, ```--ops``` arguments add a new player to the ```ops.json``` file , it takes the form ```<uuid>:<name>:<permission_level>```. You can determine a player **uuid** using 
the online tool on [mcuuid.net](https://mcuuid.net).

#### Example :
``` 
$ docker run -d --name minecraft-server -p 12345:25565 aveltan/dockraft -w 069a79f4-44e9-4726-a5be-fca90e38aaf5:notch -o 069a79f4-44e9-4726-a5be-fca90e38aaf5:notch:4 
--whitelist=true --pvp=false --onlinemode=true -g survival -d hard --eula=true
```

## Backing up data

## Image variants



[DockerfileLatest]: <https://github.com/aveltan/dockraft/blob/master/Dockerfile>
[aveltan]: <https://github.com/aveltan>
[Dockraft]: <https://github.com/aveltan/dockraft>
[DockraftIssues]: <https://github.com/aveltan/dockraft/issues>
[EULA]: <https://account.mojang.com/documents/minecraft_eula>
[MinecraftWikiServerProperties]: <http://minecraft.gamepedia.com/Server.properties>
