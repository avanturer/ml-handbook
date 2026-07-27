#!/usr/bin/env python3
"""Делает внутренние ссылки вида «см. §7» кликабельными.

В длинной главе ссылка «см. §7» заставляет читателя скроллить и искать раздел глазами.
Скрипт превращает её в якорную ссылку на соответствующий заголовок той же главы.

Что НЕ трогаем, чтобы не сломать разметку:
  * `§N` внутри блоков и строчек кода — там markdown-ссылка не отрендерится;
  * `§N` внутри уже существующей ссылки `[...](...)` — вложенные ссылки ломают парсер;
  * `§N` внутри заголовка — якорь на самого себя бессмыслен;
  * `§N` со ссылкой на другую главу («§4 предыдущей главы») — номер относится к чужому файлу;
  * `§N`, для которого в этой главе нет раздела с таким номером.

Запуск:
    python tools/link_sections.py --dry-run   # показать, что изменится
    python tools/link_sections.py             # применить
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Нумерованные заголовки: «## 7. Название», «### 12.3 Название».
HEADING_NUM_RE = re.compile(r"^(#{2,4})\s+(\d+(?:\.\d+)*)\.?\s+(.+?)\s*$", re.MULTILINE)
ANY_HEADING_RE = re.compile(r"^#{1,6}\s+.*$", re.MULTILINE)
FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.DOTALL | re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")
SECTION_REF_RE = re.compile(r"§(\d+(?:\.\d+)*)")
# «§4 предыдущей главы», «§13 главы 05», «§9 прошлой главы», «§11 [главы 05](...)» —
# номер относится к ДРУГОМУ файлу, и якорь на свой раздел здесь был бы враньём.
# Ровно на этом первая версия скрипта ошиблась пять раз: она требовала слово «глав»
# сразу за номером и не видела ни «прошлой главы», ни «главы» внутри ссылки.
# Поэтому смотрим на окно после номера и допускаем в нём вводные слова и открывающую скобку.
CROSS_CHAPTER_RE = re.compile(
    r"[\s,]*(?:\[\s*)?"
    r"(?:предыдущ\w*|прошл\w*|следующ\w*|соседн\w*|перв\w*|той\s+же)?[\s,]*"
    r"глав\w*"
)
# «§3 этой главы» — это как раз ссылка на себя, её линковать НУЖНО.
SELF_CHAPTER_RE = re.compile(r"[\s,]*(?:этой|настоящей|данной)\s+глав")


def slugify(heading: str) -> str:
    """Якорь GitHub: нижний регистр, пунктуация удаляется, каждый пробел -> дефис."""
    text = re.sub(r"[`*]", "", heading).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def protected_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for pattern in (FENCE_RE, INLINE_CODE_RE, MD_LINK_RE, ANY_HEADING_RE):
        spans.extend((m.start(), m.end()) for m in pattern.finditer(text))
    return spans


def section_anchors(text: str) -> dict[str, str]:
    anchors: dict[str, str] = {}
    for _, number, title in HEADING_NUM_RE.findall(text):
        # Заголовок целиком — именно из него GitHub строит якорь.
        anchors.setdefault(number, slugify(f"{number}. {title}"))
    return anchors


def process(text: str) -> tuple[str, int, list[str]]:
    anchors = section_anchors(text)
    if not anchors:
        return text, 0, []
    spans = protected_spans(text)
    skipped: list[str] = []
    out: list[str] = []
    cursor = 0
    replaced = 0

    for match in SECTION_REF_RE.finditer(text):
        start, end = match.span()
        if any(a <= start < b for a, b in spans):
            continue
        tail = text[end:end + 40]
        if not SELF_CHAPTER_RE.match(tail) and CROSS_CHAPTER_RE.match(tail):
            skipped.append(f"{match.group(0)} (ссылка на другую главу)")
            continue
        number = match.group(1)
        if number not in anchors:
            skipped.append(f"{match.group(0)} (нет такого раздела)")
            continue
        out.append(text[cursor:start])
        out.append(f"[§{number}](#{anchors[number]})")
        cursor = end
        replaced += 1

    out.append(text[cursor:])
    return "".join(out), replaced, skipped


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv
    total = 0
    touched = 0
    all_skipped: list[str] = []

    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "§" not in text:
            continue
        new_text, count, skipped = process(text)
        all_skipped.extend(f"{path.relative_to(ROOT)}: {s}" for s in skipped)
        if count:
            total += count
            touched += 1
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
            print(f"{path.relative_to(ROOT)}: {count}")

    print(f"\nФайлов затронуто: {touched}, ссылок сделано кликабельными: {total}")
    if all_skipped:
        print(f"\nПропущено осознанно ({len(all_skipped)}):")
        for s in all_skipped:
            print(f"  - {s}")
    if dry_run:
        print("\n(сухой прогон, файлы не изменены)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
