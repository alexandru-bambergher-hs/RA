#!/bin/sh

TAG="resource-allocator"

# Stop the container and kill it after 3 seconds.
docker stop -t 3 $(docker ps -q -f ancestor=$TAG)