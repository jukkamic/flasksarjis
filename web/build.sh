#!/bin/bash

docker build -t sarjis-web:latest .

if [ "$1" == "az" ]; then
    echo "tag for azure"
    docker tag sarjis-web:latest sarjisregistry.azurecr.io/sarjis-web:latest
else
    echo "tag for aws"
    docker tag sarjis-web:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/sarjis-web:latest
fi

