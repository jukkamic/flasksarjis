#!/bin/bash

docker run -d --network=sarjisnet --network-alias=database sarjis-db:latest

