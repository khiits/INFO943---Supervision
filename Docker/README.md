
# Docker

## Utilisation container

lien :
https://www.docker.com/blog/containerized-python-development-part-1/
https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211458-lancez-votre-premier-conteneur-en-local

## Commande de lancement des containers

```
docker build -t myimage .
docker images
docker run -d -p 5000:5000 myimage
docker ps
``
