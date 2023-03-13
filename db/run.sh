#!/bin/bash

docker run -itd --network=sarjisnet --network-alias=database sarjis-db:latest

