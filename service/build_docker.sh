#!/bin/bash

# Build the Docker image
docker build -t sarjis-service:latest ..
docker tag sarjis-service:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/sarjis-service:latest

