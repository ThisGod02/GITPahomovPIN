#!/bin/bash
# Установка хуков из каталога .githooks в .git/hooks
set -e
HOOK_DIR="$(git rev-parse --show-toplevel)/.githooks"
TARGET_DIR="$(git rev-parse --git-dir)/hooks"
cp "$HOOK_DIR"/pre-commit "$HOOK_DIR"/commit-msg "$HOOK_DIR"/pre-push "$TARGET_DIR"/
chmod +x "$TARGET_DIR"/pre-commit "$TARGET_DIR"/commit-msg "$TARGET_DIR"/pre-push
echo "Хуки установлены в $TARGET_DIR"
