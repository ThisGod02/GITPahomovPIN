#!/usr/bin/env python3
"""Генерация тестовых LFS-ассетов (logo.png, banner.jpg-заглушка)."""
import base64
from pathlib import Path
HERE = Path(__file__).parent
PNG_1PX = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
data = base64.b64decode(PNG_1PX)
(HERE / "logo.png").write_bytes(data)
(HERE / "banner.jpg").write_bytes(data)
print("assets written:", sorted(p.name for p in HERE.iterdir()))
