#!/usr/bin/env python3
"""Перестановка главы внутри раздела с переписыванием всех ссылок.

Номер главы — это её место в порядке чтения, поэтому переставить главу значит
переименовать файл, сдвинуть номера соседей и починить каждую ссылку во всём
репозитории. Руками это гарантированный источник битых ссылок.

Запуск:
    python tools/renumber_chapter.py --dry-run 02-classic-ml 13-validation-and-leakage 5
    python tools/renumber_chapter.py 02-classic-ml 13-validation-and-leakage 5

Третий аргумент — новый номер главы (позиция в разделе, начиная с 1).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".sh", ".txt"}
SKIP_DIRS = {".git", "node_modules", "site", "__pycache__", ".pytest_cache"}


def text_files() -> list[Path]:
    return [p for p in ROOT.rglob("*")
            if p.is_file() and p.suffix in TEXT_SUFFIXES
            and not any(part in SKIP_DIRS for part in p.parts)]


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    dry_run = "--dry-run" in argv
    if len(args) != 3:
        print("нужно: <раздел> <имя-главы-без-.md> <новый номер>")
        return 2
    section, stem, target_str = args
    target = int(target_str)

    section_dir = DOCS / section
    if not section_dir.is_dir():
        print(f"нет раздела docs/{section}")
        return 2

    chapters = sorted(p for p in section_dir.glob("*.md") if p.name != "index.md")
    names = [p.stem for p in chapters]
    if stem not in names:
        print(f"нет главы {stem} в {section}")
        return 2

    # Новый порядок: вынимаем главу и вставляем на нужную позицию.
    order = [n for n in names if n != stem]
    order.insert(target - 1, stem)

    # Считаем переименования: номер = позиция, хвост имени сохраняем.
    renames: dict[str, str] = {}
    for index, name in enumerate(order, start=1):
        slug = name.split("-", 1)[1]
        new_name = f"{index:02d}-{slug}"
        if new_name != name:
            renames[name] = new_name

    if not renames:
        print("нечего менять")
        return 0

    print("Переименование глав:")
    for old, new in renames.items():
        print(f"  {old}.md -> {new}.md")

    # Текст правим за один проход через плейсхолдеры: номера сдвигаются каскадом,
    # и последовательные replace затирали бы результат предыдущих.
    placeholders = {old: f"\x00CH{i}\x00" for i, old in enumerate(renames)}
    touched = 0
    for path in text_files():
        original = path.read_text(encoding="utf-8")
        text = original
        for old, ph in placeholders.items():
            text = text.replace(old, ph)
        for old, ph in placeholders.items():
            text = text.replace(ph, renames[old])
        if text != original:
            touched += 1
            if not dry_run:
                path.write_text(text, encoding="utf-8")
    print(f"\nФайлов с упоминаниями: {touched}")

    if dry_run:
        print("(сухой прогон, файлы не переименованы)")
        return 0

    tmp = {}
    for old, new in renames.items():
        tmp_name = f"__tmp__{old}"
        (section_dir / f"{old}.md").rename(section_dir / f"{tmp_name}.md")
        tmp[tmp_name] = new
    for tmp_name, new in tmp.items():
        (section_dir / f"{tmp_name}.md").rename(section_dir / f"{new}.md")
    print("Файлы переименованы.")
    subprocess.run(["git", "add", "-A", "docs"], cwd=ROOT, check=False, capture_output=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
