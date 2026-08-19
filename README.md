# personal Whatsapp bot

ensure u have docker,python installed 

# install

1-clone the repo 
2-inside the repo folder run "docker compose -up -d"
3-wait for the containers to finish initialization

# Container ports
n8n:5678 
evo-api:8080
evo-api-manager-8080/manager # to connect ur whatsapp number via evo api 

# notes

import the json file inside n8n workflow 
fill any missing api keys 
ensure that the webhook url is the same in both evo api and n8n (replace localhost with host.docker.internal)

