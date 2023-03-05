#!/bin/bash

# Build the Docker image
docker build -t ecr-sarjis-repo:latest .
docker tag ecr-sarjis-repo:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/ecr-sarjis-repo:latest
