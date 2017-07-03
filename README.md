# Minecraft server deployed with Docker

#### Example

```sh
docker run -ti --name minecraft-server -p 25565:25565 minecraft-server -w f8b1c24a-8979-4061-a75c-e2e2c86f05fd:Capitaineflamm -o f8b1c24a-8979-4061-a75c-e2e2c86f05fd:Capitaineflamm:4 --whitelist=true --onlinemode=true -g survival -d hard --eula=true
```
