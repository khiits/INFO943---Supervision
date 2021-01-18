# Projet IoT 

## Généralités
Le  but  de  ce  projet  est  de  mettre  en  place  un  système  de  monitoring  d’infrastructure virtualisé  sous  docker.  Vous  pouvez  voir  un  example  d’un  
tel  système  de  monitoring  sur solarwind   (https://www.solarwinds.com/server-application-monitor/use-cases/docker-monitoring).
Pour ceci nous divisons le projet en plusieurs parties.

## Partie 1 - Docker

L’objectif de cette partie est prendre en main docker et de déployer une cinquantaine  de  container  docker  divers  (container  wordpress,  nginx,  postgres-SQL, machine  ubuntu,  etc..)  
On  pourra  utiliser  l’API  python  de  docker  (voir https://docker-py.readthedocs.io/en/stable/) pour executer de façon centralisé les containers dockers.

## Partie 2 - Monitoring

L’objectif   de   cette   partie   est   de   récupérer   les   données   de performances  des  machines  virtuelles  docker.  Docker  offre  divers  moyens  de  récupérer les  paramètres  de  performances  docker. 
Nous  verrons  ici  la  commande  stats  ainsi  que l’API rest permettant d’accéder aux mesures de performances.

## Partie 3 - MQTT

L’objectif  de  cette  partie  est  de  mettre  en  place  un  service  de  broker MQTT  sous  Mosquitto.
Nous  développerons  dans  ce  cadre  deux  broker  Mosquitto.  Un premier sera sur une raspberry pi et un second à l’intérieur d’un container docker.

## Partie 4 - Base de donné

Un premier utilisateur du flux de données envoyé dans MQTT est  une  base  de  données.  Le  but  de  cette  partie  est  la  mise  en  place  de  la  Base  de données. Dans ce cadre nous déploierons deux types de base de données.
Une base de données  MySQL  et  une  base  de  données  NoSQL  REDIS. Ces  deux  bases  seront déployés dans des composants dockers.

## Partie 5 - Base de donné

visualisation des performances- l’objectif de cette partie est de développer sous angular  un  tableau  de  bord  permettant  de  visualiser  les  performances  des  containers docker observé.

Test
