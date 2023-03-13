#!/bin/bash

aws ecr get-login-password | docker login --username AWS --password-stdin 634129605042.dkr.ecr.eu-west-1.amazonaws.com