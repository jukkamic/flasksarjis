#!/bin/bash

# Run the Docker container
docker run -d --name=sarjis --network=sarjisnet --network-alias=sarjis_backend ecr-sarjis-repo:latest
