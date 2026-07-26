#!/usr/bin/env python3
"""Сборка сводного списка источников из блоков «Что читать дальше».

Каждая глава заканчивается аннотированным списком источников. Этот скрипт собирает их
в один файл `resources/reading-list.md`, сгруппированный по разделам хендбука, — чтобы
можно было окинуть взглядом всю библиографию и понять, что читать после какой главы.

Запуск:
    python tools/build_bibliography.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "resources" / "reading-list.md"

H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
# Блок источников: от заголовка «Что читать дальше» до навигационного футера или конца файла
SOURCES_RE = re.compile(
    r"^##\s*(?:\d+\.\s*)?(?:Что читать дальше|Источники|Материалы).*?$(.*?)(?=^---\s*$|\Z)",
    re.MULTILINE | re.DOTALL,
)
ITEM_RE = re.compile(r"^-\s+(.+?)(?=\n-\s|\n\n|\Z)", re.MULTILINE | re.DOTALL)

SECTION_TITLES = {
    "00-start": "Старт",
    "01-math": "Математика",
    "02-classic-ml": "Классический ML",
    "03-deep-learning": "Deep Learning",
    "04-nlp": "NLP",
    "05-llm": "LLM",
    "06-recsys": "Рекомендательные системы",
    "07-mlops": "Выкатка в прод / MLOps",
    "08-big-data": "Big Data",
    "09-monitoring": "Мониторинг",
    "10-ab-testing": "A/B-тесты",
    "11-system-design": "ML System Design",
    "12-coding": "Практика кода",
    "13-optional": "CV, звук, мультимодальность",
    "14-career": "Карьера",
}


REL_LINK_RE = re.compile(r"\]\((?!https?://|#)([^)]+)\)")


def normalize(item: str) -> str:
    """Схлопывает переносы строк внутри одного пункта списка."""
    return re.sub(r"\s*\n\s*", " ", item).strip()


def rewrite_relative_links(item: str, chapter_path: Path) -> str:
    """Переписывает относительные ссылки так, чтобы они работали из `resources/`.

    В главе ссылка вида `02-tracks.md` относительна каталогу главы; в сводном файле
    она обязана указывать на `../docs/00-start/02-tracks.md`.
    """

    def repl(match: re.Match[str]) -> str:
        target = match.group(1)
        file_part, sep, anchor = target.partition("#")
        if not file_part:
            return match.group(0)
        resolved = (chapter_path.parent / file_part).resolve()
        try:
            rel = resolved.relative_to(ROOT)
        except ValueError:
            return match.group(0)          # ссылка ведёт наружу репозитория — не трогаем
        return f"](../{rel.as_posix()}{sep}{anchor})"

    return REL_LINK_RE.sub(repl, item)


def is_bibliography_item(item: str) -> bool:
    """Отсекает навигационные пункты: нас интересуют внешние источники и книги."""
    has_external = "http://" in item or "https://" in item
    looks_like_book = item.lstrip().startswith("**")     # «**Автор. «Название»**» без ссылки
    return has_external or looks_like_book


def collect() -> dict[str, list[tuple[str, str, list[str]]]]:
    """раздел -> [(заголовок главы, имя файла, список источников)]"""
    result: dict[str, list[tuple[str, str, list[str]]]] = defaultdict(list)
    for section in sorted(DOCS.iterdir()):
        if not section.is_dir() or section.name not in SECTION_TITLES:
            continue
        for path in sorted(section.glob("*.md")):
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            h1 = H1_RE.search(text)
            block = SOURCES_RE.search(text)
            if not (h1 and block):
                continue
            items = [normalize(i) for i in ITEM_RE.findall(block.group(1))]
            items = [i for i in items if len(i) > 20 and is_bibliography_item(i)]
            items = [rewrite_relative_links(i, path) for i in items]
            if items:
                result[section.name].append((h1.group(1).strip(), path.name, items))
    return result


def main() -> int:
    data = collect()
    if not data:
        print("Блоки источников не найдены.")
        return 1

    total_items = sum(len(items) for chapters in data.values() for _, _, items in chapters)
    lines = [
        "# Сводный список источников",
        "",
        "> Собран автоматически из блоков «Что читать дальше» всех глав "
        "(`python tools/build_bibliography.py`).",
        "> Это не список «прочитать всё» — это карта: у каждого источника указано, "
        "зачем его читать и после какой главы.",
        "",
        f"**Источников:** {total_items} · **глав с библиографией:** "
        f"{sum(len(v) for v in data.values())}",
        "",
        "## Как этим пользоваться",
        "",
        "Читать источники до соответствующей главы обычно бесполезно: оригинальные статьи "
        "написаны для тех, кто уже знает контекст. Правильный порядок — глава, потом задачи, "
        "потом первоисточник. Тогда статья читается за полчаса вместо вечера, а в голове "
        "остаётся не пересказ, а понимание, чем работа отличается от предшественников.",
        "",
        "---",
        "",
    ]

    for slug, chapters in data.items():
        lines += [f"## {SECTION_TITLES[slug]}", ""]
        for title, filename, items in chapters:
            lines += [f"### [{title}](../docs/{slug}/{filename})", ""]
            lines += [f"- {item}" for item in items]
            lines.append("")

    lines += ["---", "", "🏠 [Оглавление хендбука](../docs/index.md)", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Записано: {OUT.relative_to(ROOT)} — {total_items} источников "
          f"из {sum(len(v) for v in data.values())} глав.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
