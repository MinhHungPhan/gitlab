#!/bin/bash

# The token correction is needed in CI
if [ -z "${CI}" ]; then
    exit 0
fi

while [ "$1" != "" ]; do
    sed -i "s#\(git\|https.*\)@\(git\.smile\.fr\)\(:\|/\)#https://gitlab-ci-token:${CI_JOB_TOKEN}@\2/#" "$1"
    shift
done
