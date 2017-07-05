## Supported tags and respective ``` Dockerfile ``` links  
 - ``` latest ``` [(Dockerfile)] [DockerfileLatest]

## Quick references

- **Where to get help:**
- **Where to file issues:**
[https://github.com/aveltan/dockraft/issues] [DockraftIssues]
- **Maintained by:**
[aveltan]
- **Published image artifact details:**
- **Image updates:**
- **Source of this description:**
[https://github.com/aveltan/dockraft] [Dockraft]
- **Supported Docker versions:**
 

# Dockraft

Launch a Minecraft server in a docker container. You can pass argument to the ``` docker run ``` command to configure the server before start. The available arguments 
are specified in the section below.

## How to use this image

### Start the Minecraft server

```
$ docker run -P  aveltan/dockraft --eula=true
```

#### Example :
``` 
$ docker run -ti --name minecraft-server -p 25565:25565 aveltan/dockraft -w 069a79f4-44e9-4726-a5be-fca90e38aaf5:notch -o 069a79f4-44e9-4726-a5be-fca90e38aaf5:notch:4 
--whitelist=true --onlinemode=true -g survival -d hard --eula=true
```

## Backing up data

## Image variants



[DockerfileLatest]: <https://github.com/aveltan/dockraft/blob/master/Dockerfile>
[aveltan]: <https://github.com/aveltan>
[Dockraft]: <https://github.com/aveltan/dockraft>
[DockraftIssues]: <https://github.com/aveltan/dockraft/issues>
