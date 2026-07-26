#!/usr/bin/env python3
"""Сверка содержимого `docs/` с манифестом `.handbook/STRUCTURE.md`.

Манифест — единственный источник правды о составе хендбука: на него завязаны навигация,
перелинковка между главами и распределение работы между авторами. Расхождение означает
либо недописанную главу, либо файл, появившийся мимо плана.

Запуск: python tools/check_manifest.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".handbook" / "STRUCTURE.md"
DOCS = ROOT / "docs"

PATH_RE = re.compile(r"`(docs/\d\d-[^`]+\.md)`")


def main() -> int:
    if not MANIFEST.exists():
        print(f"Манифест не найден: {MANIFEST}")
        return 1

    planned = sorted(set(PATH_RE.findall(MANIFEST.read_text(encoding="utf-8"))))
    present = {
        p.relative_to(ROOT).as_posix()
        for p in DOCS.rglob("*.md")
        if p.name != "index.md"
    }

    missing = sorted(set(planned) - present)
    unplanned = sorted(present - set(planned))

    print(f"В манифесте: {len(planned)} | на диске: {len(present)}")

    if missing:
        print(f"\nНЕ НАПИСАНО ({len(missing)}):")
        for path in missing:
            print(f"  - {path}")

    if unplanned:
        print(f"\nЕсть на диске, но нет в манифесте ({len(unplanned)}):")
        for path in unplanned:
            print(f"  + {path}")

    if not missing and not unplanned:
        print("\nСостав совпадает с манифестом полностью.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
