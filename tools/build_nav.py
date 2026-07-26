#!/usr/bin/env python3
"""Генерация навигации хендбука из реальных файлов.

Строит:
  * `docs/index.md`            — полное оглавление всех разделов и глав;
  * `docs/<раздел>/index.md`   — витрина раздела с картой глав;
  * блок `nav:` для `mkdocs.yml` (печатается в stdout, вставляется вручную).

Заголовок главы берётся из H1, краткое описание — из строки «> **Зачем эта глава.** …».
Так оглавление не расходится с содержимым: если главы нет, её не будет и в навигации.

Запуск:
    python tools/build_nav.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
PURPOSE_RE = re.compile(r">\s*\*\*Зачем эта глава\.\*\*\s*(.+?)(?:\n>\s*\n|\n\n)", re.DOTALL)
LEVEL_RE = re.compile(r"\*\*Уровень:\*\*\s*(.+)")

SECTION_TITLES = {
    "00-start": ("Старт", "Как пользоваться хендбуком, треки обучения и карта собеседования."),
    "01-math": ("Математика", "Линейная алгебра, вероятность, статистика и оптимизация — только то, что реально нужно инженеру."),
    "02-classic-ml": ("Классический ML", "Ядро профессии: от постановки задачи обучения до бустинга, валидации и работы с признаками."),
    "03-deep-learning": ("Deep Learning", "Как на самом деле обучается сеть — от вывода backprop до трансформера и масштабирования."),
    "04-nlp": ("NLP", "Текст как данные: токенизация, эмбеддинги, энкодеры, задачи и метрики, продакшен."),
    "05-llm": ("LLM", "Большие языковые модели: устройство, обучение, выравнивание, инференс, RAG, агенты и прод."),
    "06-recsys": ("Рекомендательные системы", "Классика и современность: от матричной факторизации до генеративного ретривала на LLM."),
    "07-mlops": ("Выкатка в прод / MLOps", "Путь модели от эксперимента до пользователей: упаковка, сервинг, CI/CD, стоимость."),
    "08-big-data": ("Big Data", "Данные в масштабе: форматы, SQL, Spark, стриминг, оркестрация, распределённое обучение."),
    "09-monitoring": ("Мониторинг", "Что происходит с моделью после выката и как узнать об этом раньше пользователей."),
    "10-ab-testing": ("A/B-тесты", "Как доказать, что изменение принесло пользу, и не обмануть себя по дороге."),
    "11-system-design": ("ML System Design", "Каркас ответа на проектную секцию и семь полных разборов реальных кейсов."),
    "12-coding": ("Практика кода", "Беглость руками: Python, NumPy, pandas, ML с нуля, алгоритмы, SQL, PyTorch, тесты."),
    "13-optional": ("CV, звук, мультимодальность", "Обзорно: необходимый минимум для не-профильного MLE."),
    "14-career": ("Карьера", "Процесс найма изнутри, поведенческая секция, рост и переговоры."),
}


@dataclass
class Chapter:
    path: Path
    number: str
    title: str
    purpose: str
    level: str

    @property
    def rel_from_docs(self) -> str:
        return self.path.relative_to(DOCS).as_posix()

    @property
    def filename(self) -> str:
        return self.path.name


def clean(text: str) -> str:
    """Схлопывает переносы и убирает markdown-разметку цитаты."""
    text = re.sub(r"\n>\s*", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def first_sentence(text: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return parts[0].strip() if parts else text.strip()


def parse_chapter(path: Path) -> Chapter | None:
    text = path.read_text(encoding="utf-8")
    h1 = H1_RE.search(text)
    if not h1:
        return None
    purpose_match = PURPOSE_RE.search(text)
    purpose = first_sentence(clean(purpose_match.group(1))) if purpose_match else ""
    level_match = LEVEL_RE.search(text)
    level = level_match.group(1).strip() if level_match else ""
    number = path.stem.split("-")[0]
    return Chapter(path=path, number=number, title=h1.group(1).strip(),
                   purpose=purpose, level=level)


def collect() -> dict[str, list[Chapter]]:
    sections: dict[str, list[Chapter]] = {}
    for section_dir in sorted(DOCS.iterdir()):
        if not section_dir.is_dir() or section_dir.name not in SECTION_TITLES:
            continue
        chapters = []
        for path in sorted(section_dir.glob("*.md")):
            if path.name == "index.md":
                continue
            chapter = parse_chapter(path)
            if chapter:
                chapters.append(chapter)
        if chapters:
            sections[section_dir.name] = chapters
    return sections


def write_section_index(slug: str, chapters: list[Chapter]) -> None:
    title, description = SECTION_TITLES[slug]
    lines = [
        f"# {title}",
        "",
        f"> {description}",
        "",
        f"**Глав в разделе:** {len(chapters)}",
        "",
        "## Карта раздела",
        "",
        "| # | Глава | Уровень | О чём |",
        "|---|---|---|---|",
    ]
    for chapter in chapters:
        purpose = chapter.purpose or "—"
        level = chapter.level or "—"
        lines.append(f"| {chapter.number} | [{chapter.title}]({chapter.filename}) | {level} | {purpose} |")
    lines += [
        "",
        "## Порядок чтения",
        "",
        "Главы упорядочены: каждая опирается на предыдущие. Если идёте не по порядку — "
        "смотрите строку «Предварительно нужно» в шапке главы.",
        "",
        "---",
        "",
        "🏠 [Оглавление хендбука](../index.md)",
        "",
    ]
    (DOCS / slug / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_root_index(sections: dict[str, list[Chapter]]) -> None:
    total = sum(len(v) for v in sections.values())
    lines = [
        "# Оглавление",
        "",
        "> Полная карта хендбука. Если вы здесь впервые — начните с "
        "[«Как пользоваться хендбуком»](00-start/01-how-to-use.md) "
        "и [треков обучения](00-start/02-tracks.md).",
        "",
        f"**Разделов:** {len(sections)} · **глав:** {total}",
        "",
        "---",
        "",
    ]
    for slug, chapters in sections.items():
        title, description = SECTION_TITLES[slug]
        number = slug.split("-")[0]
        lines += [
            f"## {number} · [{title}]({slug}/index.md)",
            "",
            description,
            "",
        ]
        for chapter in chapters:
            purpose = f" — {chapter.purpose}" if chapter.purpose else ""
            lines.append(f"- [{chapter.title}]({slug}/{chapter.filename}){purpose}")
        lines.append("")
    lines += [
        "---",
        "",
        "🏠 [К README репозитория](../README.md)",
        "",
    ]
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


NAV_START = "# >>> nav: сгенерировано tools/build_nav.py — не редактировать вручную"
NAV_END = "# <<< конец сгенерированной навигации"


def render_nav(sections: dict[str, list[Chapter]]) -> str:
    lines = [NAV_START, "nav:", "  - Оглавление: index.md"]
    for slug, chapters in sections.items():
        title, _ = SECTION_TITLES[slug]
        lines.append(f"  - {title}:")
        lines.append(f"      - {slug}/index.md")
        for chapter in chapters:
            # двоеточие в заголовке ломает YAML — заголовок берём в кавычки
            safe_title = chapter.title.replace('"', "'")
            lines.append(f'      - "{safe_title}": {slug}/{chapter.filename}')
    lines.append(NAV_END)
    return "\n".join(lines)


def write_mkdocs_nav(sections: dict[str, list[Chapter]]) -> None:
    """Вписывает блок nav в mkdocs.yml между маркерами, заменяя прежний."""
    path = ROOT / "mkdocs.yml"
    text = path.read_text(encoding="utf-8")
    nav = render_nav(sections)

    if NAV_START in text and NAV_END in text:
        start = text.index(NAV_START)
        end = text.index(NAV_END) + len(NAV_END)
        text = text[:start] + nav + text[end:]
    else:
        text = text.rstrip() + "\n\n" + nav + "\n"

    path.write_text(text, encoding="utf-8")
    print(f"mkdocs.yml: навигация обновлена ({len(sections)} разделов).")


def main() -> int:
    sections = collect()
    if not sections:
        print("Главы не найдены — нечего собирать.")
        return 1
    for slug, chapters in sections.items():
        write_section_index(slug, chapters)
    write_root_index(sections)
    write_mkdocs_nav(sections)
    total = sum(len(v) for v in sections.values())
    print(f"Собрано: {len(sections)} разделов, {total} глав.")
    for slug, chapters in sections.items():
        print(f"  {slug}: {len(chapters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
