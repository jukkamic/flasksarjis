#!/bin/bash

# Run the Docker container
docker rm sarjis
docker run -itd --name=sarjis --network=sarjisnet --network-alias=sarjis_backend sarjis-service:latest
