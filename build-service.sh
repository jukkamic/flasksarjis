#!/bin/bash

# Build the Docker image
docker build -t sarjis-service:latest -f service/Dockerfile .

if [ "$1" == "az" ]; then
    echo "tag for azure"
    docker tag sarjis-service:latest sarjisregistry.azurecr.io/sarjis-service:latest
else
    echo "tag for aws"
    docker tag sarjis-service:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/sarjis-service:latest
fi


