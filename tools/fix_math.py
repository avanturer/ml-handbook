#!/usr/bin/env python3
"""Починка формул, которые GitHub не рендерит.

Основная правка одна: **инлайновая формула, разорванная переносом строки**.
GitHub требует, чтобы `$...$` умещалась в одну строку, иначе читатель видит сырой LaTeX.
Переносы внутри такой формулы заменяются пробелом — строка становится длиннее,
и это осознанный размен: аккуратность исходника против работающего рендера.

Как ищем пары `$` безопасно: разбиваем текст на абзацы (пустая строка — граница),
внутри абзаца считаем `$` и спариваем их по порядку. Если число нечётное — абзац
пропускаем и сообщаем: значит, разметка сломана, и угадывать нельзя.
Блоки кода, инлайн-код и `$$...$$` не трогаем вовсе.

Вертикальную черту в таблицах скрипт НЕ трогает: `\\|` там уже экранирована и рендерится,
а редкие неэкранированные случаи правятся руками — замена вслепую портит нотацию.

Запуск:
    python tools/fix_math.py --dry-run
    python tools/fix_math.py
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

PROTECTED_RE = re.compile(
    r"(^```.*?^```)|(`[^`\n]*`)|(\$\$.*?\$\$)",
    re.DOTALL | re.MULTILINE,
)


def split_protected(text: str) -> list[tuple[str, bool]]:
    parts: list[tuple[str, bool]] = []
    pos = 0
    for match in PROTECTED_RE.finditer(text):
        if match.start() > pos:
            parts.append((text[pos:match.start()], False))
        parts.append((match.group(0), True))
        pos = match.end()
    if pos < len(text):
        parts.append((text[pos:], False))
    return parts


def join_in_paragraph(block: str) -> tuple[str, int, bool]:
    """Склеивает разорванные формулы внутри одного абзаца.

    Возвращает (новый текст, сколько склеено, был ли нечётным счёт `$`).
    """
    dollars = [m.start() for m in re.finditer(r"\$", block)]
    if not dollars:
        return block, 0, False
    if len(dollars) % 2 == 1:
        return block, 0, True

    out = []
    prev_end = 0
    joined = 0
    for open_pos, close_pos in zip(dollars[::2], dollars[1::2]):
        body = block[open_pos + 1:close_pos]
        out.append(block[prev_end:open_pos + 1])
        if "\n" in body:
            out.append(re.sub(r"[ \t]*\n[ \t]*", " ", body))
            joined += 1
        else:
            out.append(body)
        out.append("$")
        prev_end = close_pos + 1
    out.append(block[prev_end:])
    return "".join(out), joined, False


def process_chunk(chunk: str) -> tuple[str, int, int]:
    """Обрабатывает незащищённый фрагмент по абзацам."""
    pieces = re.split(r"(\n[ \t]*\n)", chunk)   # разделители сохраняем
    joined_total = odd_total = 0
    for i, piece in enumerate(pieces):
        if i % 2 == 1:                          # это разделитель абзацев
            continue
        fixed, joined, odd = join_in_paragraph(piece)
        pieces[i] = fixed
        joined_total += joined
        odd_total += int(odd)
    return "".join(pieces), joined_total, odd_total


def process(path: Path, dry_run: bool) -> tuple[int, int]:
    original = path.read_text(encoding="utf-8")
    rebuilt = []
    joined_total = odd_total = 0
    for chunk, protected in split_protected(original):
        if protected:
            rebuilt.append(chunk)
            continue
        fixed, joined, odd = process_chunk(chunk)
        rebuilt.append(fixed)
        joined_total += joined
        odd_total += odd
    text = "".join(rebuilt)

    if text != original and not dry_run:
        path.write_text(text, encoding="utf-8")
    return joined_total, odd_total


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    total_joined = total_odd = files = 0
    for path in sorted(DOCS.rglob("*.md")):
        joined, odd = process(path, args.dry_run)
        if joined or odd:
            files += 1
            note = f", пропущено абзацев с непарным `$`: {odd}" if odd else ""
            print(f"{path.relative_to(ROOT)}: склеено {joined}{note}")
            total_joined += joined
            total_odd += odd

    verb = "будет склеено" if args.dry_run else "склеено"
    print(f"\nФайлов: {files}. {verb} формул: {total_joined}.")
    if total_odd:
        print(f"Абзацев с непарным `$` (нужны руки): {total_odd}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
