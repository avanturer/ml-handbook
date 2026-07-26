#!/usr/bin/env python3
"""Сводка по объёму и наполнению хендбука.

Считает не только страницы, но и то, что определяет ценность: сколько в тексте
разобранных вопросов, выведенных формул, исполняемого кода и схем.

Запуск: python tools/stats.py   (или `make stats`)
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

CODE_FENCE = "```"


def main() -> int:
    chapters = [p for p in DOCS.rglob("*.md") if p.name != "index.md"]
    if not chapters:
        print("Главы не найдены.")
        return 1

    total_bytes = 0
    words = 0
    callouts = 0          # 💬 «На собеседовании»
    questions = 0         # <details> в «Проверь себя»
    formulas = 0          # блочные формулы $$
    code_blocks = 0       # ```python
    diagrams = 0          # ```mermaid
    pitfalls = 0          # блоки «Подводные камни»
    level_marks = 0       # 🌱 / 🧠 врезки уровня

    for path in chapters:
        text = path.read_text(encoding="utf-8")
        total_bytes += len(text.encode("utf-8"))
        words += len(text.split())
        callouts += text.count("💬")
        questions += text.count("<details>")
        formulas += len(re.findall(r"^\$\$", text, re.MULTILINE))
        code_blocks += len(re.findall(rf"^{CODE_FENCE}python", text, re.MULTILINE))
        diagrams += len(re.findall(rf"^{CODE_FENCE}mermaid", text, re.MULTILINE))
        pitfalls += len(re.findall(r"^##\s*.*Подводные камни", text, re.MULTILINE))
        level_marks += text.count("🌱") + text.count("🧠")

    by_section: dict[str, int] = {}
    for path in chapters:
        section = path.parent.name
        by_section[section] = by_section.get(section, 0) + 1

    print(f"Глав:                    {len(chapters)}")
    print(f"Объём текста:            {total_bytes / 1_048_576:.1f} МБ, ~{words // 1000}k слов")
    print(f"Врезок «на собеседовании»: {callouts}")
    print(f"Вопросов с разбором:     {questions}")
    print(f"Блочных формул:          {formulas}")
    print(f"Блоков кода на Python:   {code_blocks}")
    print(f"Схем mermaid:            {diagrams}")
    print(f"Разделов «подводные камни»: {pitfalls}")
    print(f"Врезок уровня 🌱/🧠:      {level_marks}")
    print("\nПо разделам:")
    for section in sorted(by_section):
        print(f"  {section}: {by_section[section]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
