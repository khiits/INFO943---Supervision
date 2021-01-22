
# Docker
## Installation pas a pas

### Installation Ubuntu Groovy 20.10

lien d'installation : https://releases.ubuntu.com/20.10/

### Installation Docker Engine sur Ubuntu

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

### Installation de l'environnement de développement Python

lien : https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/

```
sudo apt update
sudo apt install python3-pip
```

### Installation de l'API - Docker SDK for Python

lien : https://docker-py.readthedocs.io/en/stable/

Dans l'environnement de développement Python :
```
pip install docker
import docker
client = docker.from_env()
```

Pour tester le bon fonctionnement : 
```
client.containers.run("ubuntu", "echo hello world")
```
## Utilisation container

lien :https://www.docker.com/blog/containerized-python-development-part-1/
https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211458-lancez-votre-premier-conteneur-en-local
