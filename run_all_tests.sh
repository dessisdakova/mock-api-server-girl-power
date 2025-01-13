#!/bin/sh

# Build and run all containers using docker compose
docker-compose build
docker-compose up -d

# Execute all tests
docker exec tests-server poetry run pytest tests

# Shut down all containers
docker-compose down
