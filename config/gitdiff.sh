#!/bin/sh

# Script to compare local git repository with remote. 
# Insert a cd into this script to a local repostiry.


git fetch
UPSTREAM=${1:-'@{u}'}
LOCAL=$(sudo git rev-parse @)
REMOTE=$(sudo git rev-parse "remotes/origin/master")
BASE=$(sudo git merge-base @ "master")

if [ $LOCAL = $REMOTE ]; then
    echo "Local is up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "Local is out-of-date."
    echo "Pulling from remote."
#    git pull
else
    echo "Diverged"
fi
