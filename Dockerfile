FROM java:alpine
MAINTAINER aveltan <aveltan@protonmail.com>

ENV minecraft_home=/opt/minecraft

RUN apk update && apk add python3 ca-certificates && update-ca-certificates

## copy the minecraft server files
COPY minecraft-server/ ${minecraft_home}/minecraft-server
## copy the starting script
COPY start.py ${minecraft_home}/

VOLUME ${minecraft_home}/minecraft-server/world
VOLUME ${minecraft_home}/minecraft-server/logs

EXPOSE 25565

WORKDIR ${minecraft_home}

## use ENTRYPOINT to CMD, to read the script flag
## TODO use the ARG for the path instead of hard coding it
ENTRYPOINT ["python3", "/opt/minecraft/start.py"]
