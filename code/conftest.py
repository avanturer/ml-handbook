"""Настройка путей для тренажёра.

Позволяет тестам импортировать `exercises.*` независимо от того, откуда запущен pytest.

Дополнительно: если выставить переменную окружения `HANDBOOK_CHECK_SOLUTIONS=1`,
тесты будут прогоняться против эталонных решений из `solutions/`. Это нужно,
чтобы убедиться, что падает именно ваша реализация, а не сам тест:

    HANDBOOK_CHECK_SOLUTIONS=1 pytest code/tests -q     # всё должно быть зелёным
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

if os.environ.get("HANDBOOK_CHECK_SOLUTIONS") == "1":
    import solutions

    sys.modules["exercises"] = solutions
    for _module in ("metrics", "models", "attention"):
        sys.modules[f"exercises.{_module}"] = importlib.import_module(f"solutions.{_module}")
