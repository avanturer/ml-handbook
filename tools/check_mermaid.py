#!/usr/bin/env python3
"""Проверка того, что каждая mermaid-диаграмма действительно рисуется.

Сломанная диаграмма на GitHub выглядит как красная плашка «Unable to render rich display»
на месте схемы. Глазами это не ловится: в исходнике блок выглядит правдоподобно.
Поэтому мы честно рендерим каждую схему через mermaid-cli и смотрим, получилось ли.

Проверка ОПЦИОНАЛЬНАЯ: если mermaid-cli не установлен, скрипт говорит об этом
и завершается успешно, чтобы не блокировать работу без Node.

Установка (один раз):
    npm install @mermaid-js/mermaid-cli

Запуск:
    python tools/check_mermaid.py
    python tools/check_mermaid.py docs/01-math
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

MERMAID_BLOCK_RE = re.compile(r"^```mermaid[ \t]*$(.*?)^```", re.DOTALL | re.MULTILINE)

# Где искать mmdc: локальная установка в репозитории, глобальная, скретч-каталог сессии.
MMDC_CANDIDATES = [
    ROOT / "node_modules" / ".bin" / "mmdc",
    Path.home() / "node_modules" / ".bin" / "mmdc",
]

# Puppeteer в этом окружении не умеет сам найти браузер: он ищет собственную
# загрузку, а здесь предустановлен Chromium от Playwright.
CHROME_CANDIDATES = [
    Path("/opt/pw-browsers/chromium-1194/chrome-linux/chrome"),
    Path("/opt/pw-browsers/chromium/chrome-linux/chrome"),
    Path("/usr/bin/chromium"),
    Path("/usr/bin/google-chrome"),
]


def find_mmdc() -> str | None:
    for candidate in MMDC_CANDIDATES:
        if candidate.exists():
            return str(candidate)
    env_path = os.environ.get("MMDC_PATH")
    if env_path and Path(env_path).exists():
        return env_path
    return shutil.which("mmdc")


def find_chrome() -> str | None:
    env_path = os.environ.get("PUPPETEER_EXECUTABLE_PATH")
    if env_path and Path(env_path).exists():
        return env_path
    for candidate in CHROME_CANDIDATES:
        if candidate.exists():
            return str(candidate)
    return None


def main(argv: list[str]) -> int:
    mmdc = find_mmdc()
    if not mmdc:
        print("mermaid-cli не найден — проверка схем пропущена.")
        print("Чтобы включить её:  npm install @mermaid-js/mermaid-cli")
        return 0

    targets = [Path(a) for a in argv[1:]] or [DOCS]
    files: list[Path] = []
    for target in targets:
        target = (ROOT / target) if not target.is_absolute() else target
        files.extend(sorted(target.rglob("*.md")) if target.is_dir() else [target])

    with_diagrams = [(p, MERMAID_BLOCK_RE.findall(p.read_text(encoding="utf-8")))
                     for p in files]
    with_diagrams = [(p, blocks) for p, blocks in with_diagrams if blocks]
    total = sum(len(blocks) for _, blocks in with_diagrams)
    if not total:
        print("Схем не найдено.")
        return 0

    env = dict(os.environ)
    chrome = find_chrome()
    if chrome:
        env["PUPPETEER_EXECUTABLE_PATH"] = chrome

    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        # Без --no-sandbox headless Chromium не стартует под root в контейнере.
        config = tmpdir / "puppeteer.json"
        config.write_text(json.dumps(
            {"args": ["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]}
        ), encoding="utf-8")

        for path, blocks in with_diagrams:
            # Рендерим схемы по одной: так ошибка привязывается к конкретному блоку,
            # а не ко всему файлу.
            for index, body in enumerate(blocks, start=1):
                src = tmpdir / "diagram.mmd"
                src.write_text(body.strip() + "\n", encoding="utf-8")
                out = tmpdir / "diagram.svg"
                out.unlink(missing_ok=True)
                result = subprocess.run(
                    [mmdc, "-p", str(config), "-i", str(src), "-o", str(out)],
                    capture_output=True, text=True, env=env, timeout=180,
                )
                if result.returncode != 0 or not out.exists():
                    reason = (result.stderr or result.stdout).strip().splitlines()
                    # Полезная строка обычно первая: сам текст ошибки парсера.
                    message = reason[0] if reason else "неизвестная ошибка"
                    failures.append(
                        f"{path.relative_to(ROOT)}: схема #{index} не рисуется — {message}"
                    )

    print(f"Файлов со схемами: {len(with_diagrams)}, схем всего: {total}")
    if failures:
        print(f"\nНе рисуются ({len(failures)}):")
        for f in failures:
            print(f"  x {f}")
        return 1
    print("Все схемы рисуются.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
