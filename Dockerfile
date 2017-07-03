FROM java:alpine
MAINTAINER Eflamm OLLIVIER <eflamm.ollivier@hotmail.fr>

ARG minecraft_home=/opt/minecraft-server

## copy the minecraft server files
COPY minecraft-server/ ${minecraft_home}/
## copy the starting script
COPY start.sh ${minecraft_home}/
## could have put in the same directory, but it's preferable to separate

VOLUME ${minecraft_home}/world
VOLUME ${minecraft_home}/logs

WORKDIR ${minecraft_home}

## use ENTRYPOINT to CMD, to read the script flag
ENTRYPOINT ["/opt/minecraft-server/start.sh"]