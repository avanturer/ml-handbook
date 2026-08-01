#!/usr/bin/env python3
"""Проверка того, что хендбук читается подряд.

Каждая глава объявляет в шапке строку «Предварительно нужно» со ссылками на главы,
без которых её читать рано. Если книга построена правильно, все эти ссылки ведут
НАЗАД: к моменту, когда читатель дошёл до главы, всё нужное он уже прочитал.

Ссылка вперёд означает одно из двух, и оба стоит знать:
  * главы стоят не в том порядке — тогда порядок надо менять;
  * зависимость на самом деле не обязательная, а «полезно заглянуть» — тогда её
    надо убрать из «Предварительно нужно», иначе читатель послушно уйдёт вперёд
    и потеряет линию.

Заодно считаем «сирот»: главы, на которые никто не ссылается ни как на предпосылку,
ни из текста других глав. Сирота — признак того, что кусок не встроен в книгу,
а лежит рядом.

Запуск:
    python tools/check_order.py
    python tools/check_order.py --graph   # вывести граф зависимостей
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

PREREQ_RE = re.compile(r"^\*\*Предварительно нужно:\*\*(.+)$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+\.md)(?:#[^)]*)?\)")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def reading_order() -> list[Path]:
    """Канонический порядок чтения: разделы по номеру, главы внутри по номеру."""
    chapters: list[Path] = []
    for section in sorted(p for p in DOCS.iterdir() if p.is_dir()):
        chapters.extend(sorted(p for p in section.glob("*.md") if p.name != "index.md"))
    return chapters


def title_of(path: Path) -> str:
    match = TITLE_RE.search(path.read_text(encoding="utf-8"))
    return match.group(1).strip() if match else path.stem


def main(argv: list[str]) -> int:
    order = reading_order()
    position = {path: i for i, path in enumerate(order)}

    forward: list[str] = []
    broken: list[str] = []
    referenced: set[Path] = set()
    graph: list[tuple[str, list[str]]] = []

    for path in order:
        text = path.read_text(encoding="utf-8")
        match = PREREQ_RE.search(text)
        prereqs: list[str] = []
        if match:
            for target in LINK_RE.findall(match.group(1)):
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    broken.append(f"{path.relative_to(DOCS)}: битая предпосылка {target}")
                    continue
                prereqs.append(resolved.relative_to(DOCS).as_posix())
                referenced.add(resolved)
                if position.get(resolved, -1) > position[path]:
                    forward.append(
                        f"{path.relative_to(DOCS)} требует того, что идёт ПОЗЖЕ: "
                        f"{resolved.relative_to(DOCS)}"
                    )
        graph.append((path.relative_to(DOCS).as_posix(), prereqs))

    # Ссылки из текста — для поиска сирот учитываем их тоже.
    linked_anywhere: set[Path] = set()
    for path in order:
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            resolved = (path.parent / target).resolve()
            if resolved.exists() and resolved != path:
                linked_anywhere.add(resolved)

    orphans = [p for p in order if p not in linked_anywhere and p.parent.name != "00-start"]

    if "--graph" in argv:
        for name, prereqs in graph:
            print(f"{name}")
            for prereq in prereqs:
                print(f"    <- {prereq}")

    print(f"Глав в порядке чтения: {len(order)}")
    print(f"  с объявленными предпосылками: {sum(1 for _, p in graph if p)}")
    print(f"  ссылок-предпосылок всего:     {sum(len(p) for _, p in graph)}")

    if broken:
        print(f"\nБитые предпосылки ({len(broken)}):")
        for item in broken:
            print(f"  x {item}")
    if forward:
        print(f"\nПРЕДПОСЫЛКА ВПЕРЁД ({len(forward)}) — книга не читается подряд:")
        for item in forward:
            print(f"  x {item}")
    if orphans:
        print(f"\nНа эти главы не ссылается никто ({len(orphans)}):")
        for path in orphans:
            print(f"  . {path.relative_to(DOCS)} — {title_of(path)}")

    if broken or forward:
        return 1
    print("\nПорядок согласован: всё нужное идёт раньше.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
