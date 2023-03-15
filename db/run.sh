#!/bin/bash

PARAMS="-t"

if [[ $# -gt 0 && $1 == "d" ]]
then
  PARAMS="-td"
fi

docker run $PARAMS --network=sarjisnet --network-alias=database sarjis-db:latest

