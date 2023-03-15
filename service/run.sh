#!/bin/bash

# Run the Docker container
# docker rm sarjis

PARAMS="-t"

if [[ $# -gt 0 && $1 == "d" ]]
then
  PARAMS="-td"
fi

echo Running with $PARAMS
docker run $PARAMS --name=sarjis --network=sarjisnet --network-alias=sarjis_backend sarjis-service:latest

