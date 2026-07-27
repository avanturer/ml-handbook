#!/usr/bin/env python3
"""Проверка того, что КАЖДАЯ формула действительно рендерится.

`check_math.py` ловит поломки разметки вокруг формулы (разрыв строки, доллар-валюта,
битая таблица). Здесь мы проверяем содержимое: скармливаем LaTeX тому самому движку,
которым GitHub рисует математику в markdown, — KaTeX. Если KaTeX бросает исключение,
на странице вместо формулы будет сырой LaTeX, и заметить это можно только глазами
на отрендеренной странице.

Типичное, что ловится: команда, которой в KaTeX нет (`\\mathds`, `\\bm`, `\\eqref`),
незакрытая скобка в длинном выводе, `\\begin{align}` без `ed`, `&` вне окружения.

Проверка ОПЦИОНАЛЬНАЯ: без установленного katex скрипт сообщает об этом и выходит с нулём.

Установка (один раз):
    npm install katex

Запуск:
    python tools/check_katex.py
    python tools/check_katex.py docs/05-llm
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
RENDERER = ROOT / "tools" / "katex_render.js"

# Код и блочная математика затираются отдельно, поэтому порядок важен.
FENCE_RE = re.compile(r"^```.*?^```", re.DOTALL | re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
BLOCK_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
INLINE_MATH_RE = re.compile(r"(?<![\\$])\$([^$\n]+?)(?<!\\)\$(?!\$)")


def blank(match: re.Match[str]) -> str:
    """Затирает найденное пробелами, сохраняя переводы строк и нумерацию."""
    return re.sub(r"[^\n]", " ", match.group(0))


def extract(path: Path) -> list[tuple[int, str, bool]]:
    """Возвращает [(номер строки, tex, блочная ли)] для одного файла."""
    raw = path.read_text(encoding="utf-8")
    found: list[tuple[int, str, bool]] = []

    without_code = INLINE_CODE_RE.sub(blank, FENCE_RE.sub(blank, raw))

    for match in BLOCK_MATH_RE.finditer(without_code):
        body = match.group(1).strip()
        if body:
            found.append((without_code.count("\n", 0, match.start()) + 1, body, True))

    # Строчные ищем уже без блочных, иначе `$$a$$` распадётся на пустые куски.
    without_block = BLOCK_MATH_RE.sub(blank, without_code)
    for match in INLINE_MATH_RE.finditer(without_block):
        body = match.group(1).strip()
        if body:
            found.append((without_block.count("\n", 0, match.start()) + 1, body, False))

    return found


def find_node() -> str | None:
    return shutil.which("node") or ("/opt/node22/bin/node"
                                    if Path("/opt/node22/bin/node").exists() else None)


def katex_dir() -> str | None:
    for base in (ROOT / "node_modules", Path.home() / "node_modules"):
        if (base / "katex").exists():
            return str(base)
    env = os.environ.get("KATEX_PATH")
    return env if env and Path(env, "katex").exists() else None


def main(argv: list[str]) -> int:
    node = find_node()
    base = katex_dir()
    if not node or not base:
        print("katex не найден — проверка формул рендерингом пропущена.")
        print("Чтобы включить её:  npm install katex")
        return 0

    targets = [Path(a) for a in argv[1:]] or [DOCS]
    files: list[Path] = []
    for target in targets:
        target = (ROOT / target) if not target.is_absolute() else target
        files.extend(sorted(target.rglob("*.md")) if target.is_dir() else [target])

    items: list[dict] = []
    index: dict[int, tuple[Path, int, str]] = {}
    for path in files:
        for lineno, tex, display in extract(path):
            item_id = len(items)
            items.append({"id": item_id, "tex": tex, "display": display})
            index[item_id] = (path, lineno, tex)

    if not items:
        print("Формул не найдено.")
        return 0

    env = dict(os.environ, KATEX_PATH=base)
    result = subprocess.run(
        [node, str(RENDERER)], input=json.dumps(items),
        capture_output=True, text=True, env=env, timeout=600,
    )
    if result.returncode != 0:
        print(f"Рендерер не отработал: {(result.stderr or '').strip()[:200]}")
        return 1

    failures = json.loads(result.stdout or "[]")
    print(f"Файлов: {len(files)}, формул проверено: {len(items)}")
    if failures:
        print(f"\nНе рендерятся ({len(failures)}):")
        for failure in failures:
            path, lineno, tex = index[failure["id"]]
            snippet = " ".join(tex.split())[:70]
            print(f"  x {path.relative_to(ROOT)}:{lineno}: {failure['error']}")
            print(f"      {snippet}")
        return 1
    print("Все формулы рендерятся.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
