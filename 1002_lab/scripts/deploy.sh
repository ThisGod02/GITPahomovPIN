#!/bin/bash
set -e
ENVIRONMENT="${1:-staging}"
echo "Деплой окружения: $ENVIRONMENT"
docker build -t todo-api:latest .
echo "Образ собран. Публикация в Registry и rollout на $ENVIRONMENT."
