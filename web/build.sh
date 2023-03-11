#!/bin/bash

docker build -t sarjis-web:latest .
docker tag sarjis-web:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/sarjis-web:latest

