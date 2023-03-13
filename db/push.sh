#!/bin/bash

if [ "$1" == "az" ]; then
    echo "push to azure"
    docker push sarjisregistry.azurecr.io/sarjis-db:latest
else
    echo "push to aws"
    docker push 634129605042.dkr.ecr.eu-west-1.amazonaws.com/sarjis-db:latest
fi


