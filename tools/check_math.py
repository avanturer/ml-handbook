#!/usr/bin/env python3
"""Поиск формул, которые GitHub не отрендерит.

GitHub умеет `$...$` и `$$...$$`, но у него есть узкие места, на которых формула молча
превращается в сырой LaTeX. Проверяем именно их:

1. **Инлайновая формула, разорванная переносом строки.** GitHub требует, чтобы `$...$`
   умещалась в одну строку. Это самая частая и самая незаметная поломка: в исходнике
   всё выглядит правильно, а на странице читатель видит `\\sigma^2 = p(1-p)`.
2. **Непарные `$` внутри абзаца** — обычно следствие пункта 1, но бывает и опечаткой.
3. **`\\\\` внутри `$$` без окружения** aligned/array/cases — переносить строку негде.
4. **Неэкранированная `|` внутри формулы в таблице** — разрывает ячейку.
   (Экранированная `\\|` — не ошибка: она рендерится как двойная черта нормы.)

Запуск: python tools/check_math.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

PROTECTED_RE = re.compile(
    r"(^```.*?^```)|(`[^`\n]*`)|(\$\$.*?\$\$)",
    re.DOTALL | re.MULTILINE,
)
BLOCK_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
ENVIRONMENT_RE = re.compile(
    r"\\(?:begin\{(?:aligned|align|array|cases|matrix|split|gather|"
    r"bmatrix|pmatrix|vmatrix|Bmatrix|smallmatrix)|substack\{)"
)


def mask_protected(text: str) -> str:
    """Затирает пробелами код и блочную математику, сохраняя нумерацию строк."""
    def blank(match: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", match.group(0))
    return PROTECTED_RE.sub(blank, text)


def paragraphs(text: str):
    """Отдаёт (номер первой строки, текст абзаца). Абзацы разделены пустой строкой."""
    line_no = 1
    for block in re.split(r"\n[ \t]*\n", text):
        yield line_no, block
        line_no += block.count("\n") + 2


def check_file(path: Path) -> list[tuple[int, str]]:
    raw = path.read_text(encoding="utf-8")
    masked = mask_protected(raw)
    problems: list[tuple[int, str]] = []

    # 1-2. Разорванные формулы и непарные `$` — ищем по абзацам
    for start_line, block in paragraphs(masked):
        dollars = [m.start() for m in re.finditer(r"(?<!\\)\$", block)]
        if not dollars:
            continue
        if len(dollars) % 2 == 1:
            snippet = " ".join(block.split())[:70]
            problems.append((start_line, f"непарный `$` в абзаце: {snippet}"))
            continue
        for open_pos, close_pos in zip(dollars[::2], dollars[1::2]):
            body = block[open_pos + 1:close_pos]
            if "\n" in body:
                snippet = " ".join(body.split())[:60]
                problems.append((
                    start_line + block.count("\n", 0, open_pos),
                    f"формула разорвана переносом строки: ${snippet}$",
                ))

    # 3. Перенос внутри $$ без окружения
    for match in BLOCK_MATH_RE.finditer(raw):
        body = match.group(1)
        if "\\\\" in body and not ENVIRONMENT_RE.search(body):
            problems.append((raw.count("\n", 0, match.start()) + 1,
                             r"`\\` внутри $$ без \begin{aligned}/{array}/{cases}"))

    # 4. Неэкранированная `|` внутри формулы в строке таблицы
    for lineno, line in enumerate(masked.split("\n"), start=1):
        if not line.lstrip().startswith("|"):
            continue
        for match in re.finditer(r"(?<!\\)\$([^$]+?)(?<!\\)\$", line):
            body = match.group(1)
            if re.search(r"(?<!\\)\|", body):
                problems.append((lineno, f"неэкранированная `|` в формуле в таблице: {match.group(0)[:50]}"))

    return problems


def main() -> int:
    total = files = 0
    for path in sorted(DOCS.rglob("*.md")):
        problems = check_file(path)
        if not problems:
            continue
        files += 1
        print(f"\n{path.relative_to(ROOT)}")
        for lineno, message in problems[:10]:
            print(f"  {lineno}: {message}")
        if len(problems) > 10:
            print(f"  … и ещё {len(problems) - 10}")
        total += len(problems)

    if total:
        print(f"\nФайлов с проблемами: {files}, проблем всего: {total}")
        return 1
    print("Проблем с рендерингом формул не найдено.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
