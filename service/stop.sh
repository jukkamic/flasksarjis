#!/bin/bash

docker ps -aq --filter name="sarjis" | xargs docker rm

docker ps -aq --filter ancestor="sarjis-service:latest" | xargs docker rm
