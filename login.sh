#!/bin/bash

dos2unix bin/environments.conf
# Read configuration into an associative array
declare -A CONFIG
# IFS is the 'internal field separator'. In this case, your file uses '='
IFS="="
while read -r key value
do
    if [ -n $value ]; then
        CONFIG[$key]=$value
    else
        CONFIG[$key]=$value
    fi
done < bin/environments.conf
unset IFS

aws ecr get-login-password | docker login --username AWS --password-stdin ${CONFIG['AWS_ID']}.dkr.ecr.${CONFIG['AWS_REGION']}.amazonaws.com