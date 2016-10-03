#!/bin/sh

# Build the container and pass the entire repo as context.
TAG="resource-allocator"
docker build -t $TAG .

STATUS=$?
if [ $STATUS -ne 0 ]; then
  echo Failed building the container!
  exit $STATUS
fi

# Run the container and give it a name so we can access it later.
docker run --rm $TAG hug -v