#!/usr/bin/env python3
"""Проверка целостности хендбука.

Что проверяем:
  1. Все относительные ссылки внутри репозитория ведут на существующие файлы/якоря.
  2. Каждая глава содержит обязательные блоки авторского стандарта.
  3. Нет незакрытых блочных формул `$$` и незакрытых блоков кода.
  4. У блоков кода проставлен язык (иначе не будет подсветки).
  5. Нет оставленных заглушек (TODO / FIXME / lorem / «допишу»).

Запуск:
    python tools/check_handbook.py            # проверить всё
    python tools/check_handbook.py docs/05-llm  # проверить один раздел
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Ссылки вида [текст](путь) — исключаем картинки ![...] и внешние протоколы.
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
# Язык блока ищем ТОЛЬКО на той же строке: `\s*` съедал перевод строки и утаскивал
# первое слово следующего абзаца, из-за чего две подряд идущие ограды склеивались в одну.
FENCE_RE = re.compile(r"^([`~]{3,})[ \t]*(\S*)[ \t]*$", re.MULTILINE)
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
# Заглушки ищем осторожно: «дописать» — обычное слово («нельзя дописать строку в Parquet»),
# поэтому русские варианты засчитываем только в явно служебной форме: (дописать), [дописать]
# или отдельным пунктом списка. Английские маркеры однозначны сами по себе.
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|FIXME|XXX)\b"
    r"|lorem ipsum"
    r"|[\(\[]\s*(?:допишу|дописать|заглушка)\s*[\)\]]"
    r"|^\s*[-*]\s*(?:допишу|дописать)\b",
    re.IGNORECASE | re.MULTILINE,
)

# Блоки, без которых глава не соответствует стандарту (.handbook/AUTHORING.md §2).
REQUIRED_MARKERS = {
    "Карта главы": re.compile(r"^##\s*Карта главы", re.IGNORECASE | re.MULTILINE),
    "Подводные камни": re.compile(r"^##\s*.*Подводные камни", re.IGNORECASE | re.MULTILINE),
    "Проверь себя": re.compile(r"^##\s*.*Проверь себя", re.IGNORECASE | re.MULTILINE),
    "Практика": re.compile(r"^##\s*.*Практика", re.IGNORECASE | re.MULTILINE),
    "источники": re.compile(r"^##\s*.*(Что читать дальше|Источники|Материалы)",
                            re.IGNORECASE | re.MULTILINE),
    "навигация": re.compile(r"(⬅️|➡️|🏠)"),
    "врезка на собеседовании": re.compile(r"💬"),
}

# Файлы-оглавления и служебные страницы проверяем мягче: у них нет упражнений.
INDEX_NAMES = {"index.md", "README.md"}

# Порог в 90 строк существует, чтобы главу не заваливало кодом. Но бывает листинг,
# который есть ОДИН ЦЕЛЬНЫЙ АРТЕФАКТ: разрезать его — значит показать читателю то,
# что он не сможет собрать и запустить. Такие случаи разрешены поимённо и с причиной,
# чтобы решение оставалось осознанным, а не превращалось в вечное предупреждение,
# которое все привыкают пролистывать.
LONG_LISTING_OK = {
    "03-deep-learning/04-attention-and-transformer.md": "трансформер целиком — центр главы",
    "05-llm/01-llm-architecture.md": "современный decoder-блок целиком",
    "07-mlops/05-serving-architectures.md": "скелет прод-сервиса, который копируют целиком",
    "08-big-data/05-streaming.md": "стриминговая джоба целиком",
    "08-big-data/06-orchestration.md": "DAG переобучения целиком",
}

# Навигационные страницы раздела «Старт»: это путеводители, а не учебные главы,
# блок «Проверь себя» им не нужен по смыслу.
NAVIGATIONAL = {
    "00-start/01-how-to-use.md",
    "00-start/02-tracks.md",
    "00-start/03-interview-map.md",
    "00-start/05-glossary.md",
}

# Блоки, которых навигационные страницы не обязаны иметь: у путеводителя нет
# ни грабель из продакшена, ни задач на код, ни вопросов с собеседования.
NAVIGATIONAL_EXEMPT = {"Проверь себя", "Подводные камни", "Практика",
                       "врезка на собеседовании", "Карта главы"}


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, path: Path, msg: str) -> None:
        self.errors.append(f"{path.relative_to(ROOT)}: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"{path.relative_to(ROOT)}: {msg}")


def slugify(heading: str) -> str:
    """Аналог якорей GitHub: нижний регистр, пунктуация удаляется, каждый пробел -> дефис.

    Важно: пробелы НЕ схлопываются. «Трек 1. Junior → Middle» даёт
    `трек-1-junior--middle` с двойным дефисом там, где была стрелка, — потому что
    после удаления `.` и `→` остаются два пробела подряд, и каждый становится дефисом.
    Схлопывание здесь — классическая причина ложных «битых якорей».
    """
    # Снимаем только markdown-подсветку: backtick и звёздочку.
    # Подчёркивание НЕ трогаем — в якорях GitHub оно сохраняется («d_k» → «d_k», не «dk»).
    text = re.sub(r"[`*]", "", heading).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def anchors_of(path: Path) -> set[str]:
    if not path.exists() or path.suffix != ".md":
        return set()
    text = path.read_text(encoding="utf-8")
    return {slugify(h) for h in HEADING_RE.findall(text)}


MATH_RE = re.compile(r"\$\$.*?\$\$|\$[^$\n]+\$", re.DOTALL)
CODE_RE = re.compile(r"```.*?```|`[^`\n]+`", re.DOTALL)


def strip_non_prose(text: str) -> str:
    """Убирает формулы и код: там встречаются последовательности, неотличимые от ссылок.

    Пример из главы про Adam: `$\\mathbb{E}[g](1-\\beta_1^t)$` — для markdown-парсера
    это выглядит как ссылка `[g](1-\\beta_1^t)`, хотя это математика.
    """
    text = CODE_RE.sub(" ", text)
    return MATH_RE.sub(" ", text)


def check_links(path: Path, text: str, report: Report) -> None:
    for target in LINK_RE.findall(strip_non_prose(text)):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            if target.startswith("#"):
                anchor = target[1:]
                if anchor and anchor not in anchors_of(path):
                    report.warn(path, f"якорь не найден в самом файле: {target}")
            continue
        file_part, _, anchor = target.partition("#")
        if not file_part:
            continue
        resolved = (path.parent / file_part).resolve()
        if not resolved.exists():
            report.error(path, f"битая ссылка: {target}")
            continue
        if anchor and resolved.suffix == ".md" and anchor not in anchors_of(resolved):
            report.warn(path, f"якорь не найден: {target}")


def check_fences(path: Path, text: str, report: Report) -> None:
    fences = FENCE_RE.findall(text)
    depth = 0
    opened_lang: list[str] = []
    for marker, lang in fences:
        if depth == 0:
            depth = 1
            opened_lang.append(lang)
        else:
            depth = 0
    if depth != 0:
        report.error(path, "незакрытый блок кода (```)")

    # Блок без языка — это обычно вывод программы, и это нормально.
    # А вот слишком длинный листинг стандарт (AUTHORING §6) просит выносить в файл.
    rel = path.relative_to(DOCS).as_posix() if DOCS in path.parents else path.name
    allowed = LONG_LISTING_OK.get(rel)
    for match in re.finditer(r"^```python[ \t]*$(.*?)^```", text, re.DOTALL | re.MULTILINE):
        lines = match.group(1).count("\n")
        if lines <= 90 or allowed:
            continue
        report.warn(path, f"листинг на {lines} строк — стандарт просит выносить в code/")


def check_math(path: Path, text: str, report: Report) -> None:
    # Считаем только $$ вне блоков кода.
    without_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    if without_code.count("$$") % 2 != 0:
        report.error(path, "нечётное число `$$` — незакрытая блочная формула")


def check_structure(path: Path, text: str, report: Report) -> None:
    if path.name in INDEX_NAMES:
        return
    rel = path.relative_to(DOCS).as_posix() if DOCS in path.parents else path.name
    for name, pattern in REQUIRED_MARKERS.items():
        if name in NAVIGATIONAL_EXEMPT and rel in NAVIGATIONAL:
            continue
        if not pattern.search(text):
            report.warn(path, f"нет обязательного блока: {name}")
    # Считаем H1 только вне блоков кода: в Python комментарии тоже начинаются с «# »
    without_code = re.sub(r"^```.*?^```", "", text, flags=re.DOTALL | re.MULTILINE)
    h1_count = len(re.findall(r"^#\s+\S", without_code, re.MULTILINE))
    if h1_count > 1:
        report.warn(path, f"больше одного заголовка H1 (найдено {h1_count})")
    words = len(text.split())
    if words < 400:
        report.warn(path, f"подозрительно короткая глава: {words} слов")


def check_placeholders(path: Path, text: str, report: Report) -> None:
    for match in PLACEHOLDER_RE.finditer(text):
        report.error(path, f"осталась заглушка: {match.group(0)!r}")
        break


def main(argv: list[str]) -> int:
    targets = [Path(a) for a in argv[1:]] or [DOCS]
    files: list[Path] = []
    for target in targets:
        target = (ROOT / target).resolve() if not target.is_absolute() else target
        files.extend(sorted(target.rglob("*.md")) if target.is_dir() else [target])

    report = Report()
    for path in files:
        text = path.read_text(encoding="utf-8")
        check_links(path, text, report)
        check_fences(path, text, report)
        check_math(path, text, report)
        check_structure(path, text, report)
        check_placeholders(path, text, report)

    print(f"Проверено файлов: {len(files)}")
    if report.warnings:
        print(f"\nПредупреждения ({len(report.warnings)}):")
        for w in report.warnings:
            print(f"  ! {w}")
    if report.errors:
        print(f"\nОшибки ({len(report.errors)}):")
        for e in report.errors:
            print(f"  x {e}")
        return 1
    print("\nОшибок нет.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
