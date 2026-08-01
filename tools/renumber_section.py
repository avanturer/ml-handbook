#!/usr/bin/env python3
"""Перенумерация разделов хендбука с переписыванием всех ссылок.

Порядок папок — это и есть порядок чтения книги, поэтому менять его приходится
целиком: каталог, все относительные ссылки в главах, манифест, навигация, README,
инструменты. Руками это не делается без ошибок, поэтому делается здесь.

Работает как обмен или переименование по карте старое -> новое. Обмен безопасен:
переименование идёт через временные имена, поэтому пересечения не мешают.

Запуск:
    python tools/renumber_section.py --dry-run 06-recsys=10-recsys 10-ab-testing=06-ab-testing
    python tools/renumber_section.py 06-recsys=10-recsys 10-ab-testing=06-ab-testing
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Где искать упоминания. node_modules и .git не трогаем.
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".sh", ".txt", ".cfg", ".ini"}
SKIP_DIRS = {".git", "node_modules", "site", "__pycache__", ".pytest_cache"}


def text_files() -> list[Path]:
    out = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        out.append(path)
    return out


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv
    pairs = [a for a in argv[1:] if "=" in a]
    if not pairs:
        print("нужны пары вида старое=новое, например 06-recsys=10-recsys")
        return 2

    mapping = dict(p.split("=", 1) for p in pairs)
    for old in mapping:
        if not (DOCS / old).is_dir():
            print(f"нет такого раздела: docs/{old}")
            return 2

    print("Переименование:")
    for old, new in mapping.items():
        print(f"  docs/{old} -> docs/{new}")

    # 1. Текст. Обмен делаем за один проход через плейсхолдеры, иначе первый
    #    replace затрёт то, что нужно второму (06 -> 10, а потом 10 -> 06 обратно).
    placeholders = {old: f"\x00SECT{i}\x00" for i, old in enumerate(mapping)}
    touched = 0
    for path in text_files():
        original = path.read_text(encoding="utf-8")
        text = original
        for old, ph in placeholders.items():
            text = text.replace(old, ph)
        for old, ph in placeholders.items():
            text = text.replace(ph, mapping[old])
        if text != original:
            touched += 1
            if not dry_run:
                path.write_text(text, encoding="utf-8")

    print(f"\nФайлов с упоминаниями: {touched}")

    # 2. Каталоги. Через временное имя — на случай обмена.
    if not dry_run:
        temp = {}
        for old in mapping:
            tmp_name = f"__tmp__{old}"
            (DOCS / old).rename(DOCS / tmp_name)
            temp[tmp_name] = mapping[old]
        for tmp_name, new in temp.items():
            (DOCS / tmp_name).rename(DOCS / new)
        print("Каталоги переименованы.")
        # git заметит переименование сам, но подскажем ему явным add
        subprocess.run(["git", "add", "-A", "docs"], cwd=ROOT, check=False,
                       capture_output=True)
    else:
        print("(сухой прогон, ничего не изменено)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
