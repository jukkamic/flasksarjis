#!/bin/bash

docker build -t sarjis-db:latest --build-arg postgres_password=secret .
docker tag sarjis-db:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/sarjis-db:latest
