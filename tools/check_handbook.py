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
FENCE_RE = re.compile(r"^([`~]{3,})\s*(\S*)", re.MULTILINE)
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"\b(TODO|FIXME|XXX|lorem ipsum|допишу|дописать)\b", re.IGNORECASE)

# Блоки, без которых глава не соответствует стандарту (.handbook/AUTHORING.md §2).
REQUIRED_MARKERS = {
    "Проверь себя": re.compile(r"##\s*.*Проверь себя", re.IGNORECASE),
    "источники": re.compile(r"##\s*.*(Что читать дальше|Источники|Материалы)", re.IGNORECASE),
    "навигация": re.compile(r"(⬅️|➡️|🏠)"),
}

# Файлы-оглавления и служебные страницы проверяем мягче: у них нет упражнений.
INDEX_NAMES = {"index.md", "README.md"}


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, path: Path, msg: str) -> None:
        self.errors.append(f"{path.relative_to(ROOT)}: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"{path.relative_to(ROOT)}: {msg}")


def slugify(heading: str) -> str:
    """Приблизительный аналог якорей GitHub: нижний регистр, пробелы -> дефисы."""
    text = re.sub(r"[`*_]", "", heading).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)


def anchors_of(path: Path) -> set[str]:
    if not path.exists() or path.suffix != ".md":
        return set()
    text = path.read_text(encoding="utf-8")
    return {slugify(h) for h in HEADING_RE.findall(text)}


def check_links(path: Path, text: str, report: Report) -> None:
    for target in LINK_RE.findall(text):
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
    for lang in opened_lang:
        if not lang:
            report.warn(path, "блок кода без указания языка — не будет подсветки")
            break


def check_math(path: Path, text: str, report: Report) -> None:
    # Считаем только $$ вне блоков кода.
    without_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    if without_code.count("$$") % 2 != 0:
        report.error(path, "нечётное число `$$` — незакрытая блочная формула")


def check_structure(path: Path, text: str, report: Report) -> None:
    if path.name in INDEX_NAMES:
        return
    for name, pattern in REQUIRED_MARKERS.items():
        if not pattern.search(text):
            report.warn(path, f"нет обязательного блока: {name}")
    if text.count("\n# ") + text.startswith("# ") > 1:
        report.warn(path, "больше одного заголовка H1")
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
