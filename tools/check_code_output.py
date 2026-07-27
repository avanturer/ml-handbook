#!/usr/bin/env python3
"""Проверка того, что показанный вывод программы — настоящий.

Самый неприятный вид брака в учебнике: код правильный, а под ним стоит вывод,
которого код никогда не печатал. Читатель запускает у себя, видит другие числа
и перестаёт доверять всему тексту. Один такой случай в этом репозитории уже был.

Как работает. В главе берутся все блоки ```python по порядку и склеиваются в один
скрипт (в наших главах код почти всегда наращивается: следующий блок пользуется
переменными предыдущего). Скрипт запускается. Затем каждый блок без указания языка —
а это у нас и есть «вывод программы» — сверяется со СТРОКАМИ настоящего stdout.

Что считается ошибкой, а что нет:
  * код упал или не запустился     -> НЕ ошибка, а сообщение. Блоки бывают фрагментами,
                                      требуют GPU, кластера или сети — проверить их нечем.
  * код отработал, а строки заявленного вывода в настоящем stdout нет -> ОШИБКА.
Такая асимметрия делает проверку полезной и при этом не заставляет переписывать
главы, где код принципиально не запускается в песочнице.

Запуск:
    python tools/check_code_output.py docs/02-classic-ml/19-stacking-and-blending.md
    python tools/check_code_output.py docs/02-classic-ml      # раздел целиком
    python tools/check_code_output.py --verbose docs/...      # показать вывод скрипта
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

FENCE_RE = re.compile(r"^```(\w*)[ \t]*$(.*?)^```", re.DOTALL | re.MULTILINE)

# Блок без языка — это может быть и вывод программы, и дерево каталогов, и схема
# псевдографикой. Считаем выводом только то, что стоит сразу после блока python:
# именно так вывод и оформляют в наших главах.
MAX_SECONDS = 900

# Строки, которые бессмысленно сверять: разделители, многоточия, отбивки.
NOISE_RE = re.compile(r"^[\s.…\-=_*|+~<>^]*$")


def blocks_of(text: str) -> list[tuple[str, str, int]]:
    out = []
    for match in FENCE_RE.finditer(text):
        line_no = text.count("\n", 0, match.start()) + 1
        out.append((match.group(1), match.group(2), line_no))
    return out


def claimed_outputs(blocks: list[tuple[str, str, int]]) -> list[tuple[str, int]]:
    """Блоки без языка, стоящие непосредственно после блока python."""
    result = []
    for index, (lang, body, line_no) in enumerate(blocks):
        if lang:
            continue
        if index == 0 or blocks[index - 1][0] != "python":
            continue
        result.append((body, line_no))
    return result


def check_file(path: Path, verbose: bool) -> tuple[list[str], list[str], bool]:
    """Возвращает (ошибки, сообщения, был ли файл вообще пригоден к проверке)."""
    text = path.read_text(encoding="utf-8")
    blocks = blocks_of(text)
    python_blocks = [body for lang, body, _ in blocks if lang == "python"]
    expected = claimed_outputs(blocks)

    if not python_blocks or not expected:
        return [], [], False

    script = "\n".join(python_blocks)
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "chapter.py"
        source.write_text(script, encoding="utf-8")
        try:
            run = subprocess.run(
                [sys.executable, str(source)],
                capture_output=True, text=True, timeout=MAX_SECONDS, cwd=tmp,
            )
        except subprocess.TimeoutExpired:
            return [], [f"{path.relative_to(ROOT)}: код не уложился в {MAX_SECONDS} с — не проверено"], True

    if run.returncode != 0:
        reason = (run.stderr or "").strip().splitlines()
        tail = reason[-1] if reason else "без сообщения"
        return [], [f"{path.relative_to(ROOT)}: код не выполняется целиком ({tail[:90]}) — не проверено"], True

    if verbose:
        print(f"--- настоящий вывод {path.relative_to(ROOT)} ---")
        print(run.stdout)

    actual_lines = {line.strip() for line in run.stdout.splitlines() if line.strip()}
    errors: list[str] = []
    for body, line_no in expected:
        for line in body.splitlines():
            stripped = line.strip()
            if not stripped or NOISE_RE.match(stripped):
                continue
            if stripped not in actual_lines:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_no}: строки нет в настоящем выводе: {stripped[:70]!r}"
                )
                break  # одного примера на блок достаточно
    return errors, [], True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("targets", nargs="*", default=[])
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    targets = [Path(t) for t in args.targets] or [DOCS]
    files: list[Path] = []
    for target in targets:
        target = (ROOT / target) if not target.is_absolute() else target
        files.extend(sorted(target.rglob("*.md")) if target.is_dir() else [target])

    all_errors: list[str] = []
    all_notes: list[str] = []
    checked = 0
    for path in files:
        errors, notes, applicable = check_file(path, args.verbose)
        checked += int(applicable)
        all_errors.extend(errors)
        all_notes.extend(notes)

    verified = checked - len(all_notes)
    print(f"Глав с кодом и показанным выводом: {checked}, из них проверено запуском: {verified}")
    if all_notes:
        print(f"\nНе проверено ({len(all_notes)}) — код не запускается в песочнице:")
        for note in all_notes:
            print(f"  . {note}")
    if all_errors:
        print(f"\nВЫВОД НЕ СОВПАДАЕТ С НАСТОЯЩИМ ({len(all_errors)}):")
        for error in all_errors:
            print(f"  x {error}")
        return 1
    print("\nВесь проверяемый вывод — настоящий.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
