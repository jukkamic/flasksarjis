#!/bin/bash

# Build the Docker image
docker build -t 634129605042.dkr.ecr.eu-west-1.amazonaws.com/ecr-sarjis-repo
docker push 634129605042.dkr.ecr.eu-west-1.amazonaws.com/ecr-sarjis-repo:latest