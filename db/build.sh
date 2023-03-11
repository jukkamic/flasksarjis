#!/bin/bash

docker build -t sarjis-db:latest --build-arg postgres_password=secret .