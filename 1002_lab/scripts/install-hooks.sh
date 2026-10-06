#!/bin/bash
set -e
pip install pre-commit
pre-commit install
echo "pre-commit хуки установлены"
