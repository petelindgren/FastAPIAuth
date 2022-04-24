#!/usr/bin/env bash
# Ref: https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

# If you want to remove All Unused or Dangling Images, Containers, Volumes and Networks
# docker system prune -a

# Remove All Docker Containers and Volumes"
CONTAINERS=$(docker ps -aq)
if [[ ! -z "$CONTAINERS" ]]
then
    echo "Remove Docker Containers and Volumes \$CONTAINERS"
    docker rm -vf ${CONTAINERS}
else
    echo "There are no Docker Containers to remove"
fi

# Remove All Docker Images
IMAGES=$(docker images -aq)
if [[ ! -z "$IMAGES" ]]
then
    echo "Remove Docker Images \$IMAGES"
    docker rmi -f ${IMAGES}
else
    echo "There are no Docker Images to remove"
fi

