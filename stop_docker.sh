#!/bin/bash

docker ps -aq --filter name="sarjis" | xargs docker rm

if [[ $# -gt 0 && $1 == "all" ]]
then
  docker ps -aq --filter ancestor="sarjis-db:latest" | xargs docker stop
  docker ps -aq --filter ancestor="sarjis-db:latest" | xargs docker rm
fi
docker ps -aq --filter ancestor="sarjis-service:latest" | xargs docker stop
docker ps -aq --filter ancestor="sarjis-service:latest" | xargs docker rm
docker ps -aq --filter ancestor="sarjis-web:latest" | xargs docker stop
docker ps -aq --filter ancestor="sarjis-web:latest" | xargs docker rm
