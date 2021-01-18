
# Docker

## Installation Docker Engine sur Ubuntu

lien : https://docs.docker.com/engine/install/ubuntu/?fbclid=IwAR1hwpqWHzFqkZEWxnGOnjVxcdn9uZMY6gI-kRAfPBRa1UsrdMgfrmbQM5w

```
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo docker run hello-world
```
