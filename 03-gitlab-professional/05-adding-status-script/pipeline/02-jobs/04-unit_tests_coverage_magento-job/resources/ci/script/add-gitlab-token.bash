#!/bin/bash

# We need to install dependencies only for Docker
[[ ! -e /.dockerenv ]] && exit 0

while [ "$1" != "" ]; do
    sed -i "s#git@git.smile.fr:#https://gitlab-ci-token:${CI_JOB_TOKEN}@git.smile.fr/#" "$1"
    shift
done
