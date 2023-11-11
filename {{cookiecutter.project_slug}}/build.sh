#!/bin/sh

DOCKER_UTILS_TAG_EM=${DOCKER_UTILS_TAG_EM:-YES}

# Load functions
. "utils/funcs.sh"

# Load variables
GET_ENV_VARS ".env"

echo "Building via Compose $IMAGE_NAME - $IMAGE_VERSION"
BTP_IMAGE --image-name "$IMAGE_NAME" \
            --image-version "$IMAGE_VERSION" \
            --service "$SERVICE_NAME" \
            --compose

