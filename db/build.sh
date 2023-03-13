#!/bin/bash

docker build -t sarjis-db:latest --build-arg postgres_password=secret .

if [ "$1" == "az" ]; then
    echo "tag for azure"
    docker tag sarjis-db:latest sarjisregistry.azurecr.io/sarjis-db:latest
else
    echo "tag for aws"
    docker tag sarjis-db:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/sarjis-db:latest
fi

