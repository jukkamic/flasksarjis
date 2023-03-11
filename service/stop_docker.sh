#!/bin/bash

docker ps -q --filter ancestor="ecr-sarjis-repo" | xargs docker stop