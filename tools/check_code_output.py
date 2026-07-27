#!/usr/bin/env python3
"""Проверка того, что показанный вывод программы — настоящий.

Самый неприятный вид брака в учебнике: код правильный, а под ним стоит вывод,
которого код никогда не печатал. Читатель запускает у себя, видит другие числа
и перестаёт доверять всему тексту. Один такой случай в этом репозитории уже был.

Как работает. Блоки ```python главы выполняются по порядку в общем пространстве имён
(в наших главах код почти всегда наращивается: следующий блок пользуется переменными
предыдущего), каждый под своим `except` — чтобы один иллюстративный фрагмент вроде
`model = MyModel()` не ронял проверку всей главы. Вывод размечается по блокам,
и блоки без указания языка, ВПЛОТНУЮ следующие за кодом, сверяются с настоящим stdout
именно того блока, который их напечатал.

Слово «вплотную» здесь несёт всю нагрузку. Блок без языка — это не обязательно вывод:
им же оформлены разметка BIO, шаблон промпта, протокол ReAct и схемы псевдографикой.
Отличает их расстояние до кода: настоящий вывод стоит сразу под ним, максимум через
короткую подводку вроде «получаем:». Если между кодом и блоком целый абзац, заголовок
или врезка — блок относится не к коду, и сверять его не с чем.

Что считается ошибкой, а что нет:
  * блок кода упал                 -> НЕ ошибка, а сообщение. Блоки бывают фрагментами,
                                      требуют GPU, кластера или сети — проверить их нечем.
  * блок отработал, а заявленной строки в его выводе нет -> ОШИБКА.
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

# Маркеры, которыми скрипт размечает свой вывод по блокам.
RUN_MARK = "@@БЛОК-%d@@"
FAIL_MARK = "@@СБОЙ@@"
# Регулярку пишем явно, а не собираем из RUN_MARK: re.escape не экранирует «%»,
# и попытка подставить группу в экранированную строку молча не срабатывает —
# маркеры перестают находиться, а вывод выглядит так, будто код ничего не напечатал.
RUN_MARK_RE = re.compile(r"@@БЛОК-(\d+)@@")


def blocks_of(text: str) -> list[tuple[str, str, int, int, int]]:
    """(язык, тело, номер строки, начало, конец) для каждой ограды."""
    out = []
    for match in FENCE_RE.finditer(text):
        line_no = text.count("\n", 0, match.start()) + 1
        out.append((match.group(1), match.group(2), line_no, match.start(), match.end()))
    return out


# Между кодом и его выводом бывает максимум короткая подводка вроде «получаем:».
# Если между ними абзац текста, заголовок или врезка — значит, блок без языка
# относится не к коду, а к чему-то другому: это разметка BIO, шаблон промпта,
# протокол ReAct или схема псевдографикой. Такие блоки сверять не с чем.
MAX_GAP_CHARS = 220
GAP_BREAK_RE = re.compile(r"^\s*(#{1,6}\s|>\s|\||\d+\.\s|[-*]\s)", re.MULTILINE)


def claimed_outputs(text: str,
                    blocks: list[tuple[str, str, int, int, int]]) -> list[tuple[str, int, int]]:
    """Блоки без языка, вплотную следующие за блоком python.

    Отдаёт (тело, номер строки, порядковый номер блока python) — последнее нужно,
    чтобы сверять вывод именно с тем блоком, который его напечатал.
    """
    python_seen = 0
    result = []
    for index, (lang, body, line_no, start, _end) in enumerate(blocks):
        if lang == "python":
            python_seen += 1
        if lang or index == 0:
            continue
        prev_lang, _, _, _, prev_end = blocks[index - 1]
        if prev_lang != "python":
            continue
        gap = text[prev_end:start]
        if len(gap) > MAX_GAP_CHARS or GAP_BREAK_RE.search(gap):
            continue
        result.append((body, line_no, python_seen - 1))
    return result


def check_file(path: Path, verbose: bool) -> tuple[list[str], list[str], int]:
    """Возвращает (ошибки, сообщения, сколько блоков вывода нашлось в главе)."""
    text = path.read_text(encoding="utf-8")
    blocks = blocks_of(text)
    python_blocks = [body for lang, body, *_ in blocks if lang == "python"]
    expected = claimed_outputs(text, blocks)

    if not python_blocks or not expected:
        return [], [], 0

    # Блоки выполняются по одному в общем пространстве имён и каждый под своим except.
    # Иначе один иллюстративный фрагмент (`model = MyModel()`) роняет весь скрипт,
    # и глава целиком уходит в «не проверено» — хотя настоящий вывод в ней есть.
    script: list[str] = []
    for index, body in enumerate(python_blocks):
        script.append(f'print("{RUN_MARK % index}")')
        script.append(f"_src_{index} = {body!r}")
        script.append("try:")
        script.append(f"    exec(compile(_src_{index}, '<блок {index}>', 'exec'), globals())")
        script.append("except Exception as _e:")
        script.append(f'    print("{FAIL_MARK}", type(_e).__name__ + ": " + str(_e)[:90])')

    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "chapter.py"
        source.write_text("\n".join(script), encoding="utf-8")
        try:
            run = subprocess.run(
                [sys.executable, str(source)],
                capture_output=True, text=True, timeout=MAX_SECONDS, cwd=tmp,
            )
        except subprocess.TimeoutExpired:
            return [], [f"{path.relative_to(ROOT)}: код не уложился в {MAX_SECONDS} с — не проверено"], len(expected)

    if run.returncode != 0:
        reason = (run.stderr or "").strip().splitlines()
        tail = reason[-1] if reason else "без сообщения"
        return [], [f"{path.relative_to(ROOT)}: скрипт не запустился ({tail[:90]}) — не проверено"], len(expected)

    if verbose:
        print(f"--- настоящий вывод {path.relative_to(ROOT)} ---")
        print(run.stdout)

    # Разбираем вывод по блокам и запоминаем, какие из них упали.
    per_block: dict[int, list[str]] = {}
    broken: dict[int, str] = {}
    current = None
    for line in run.stdout.splitlines():
        marker = RUN_MARK_RE.fullmatch(line)
        if marker:
            current = int(marker.group(1))
            per_block[current] = []
            continue
        if current is None:
            continue
        if line.startswith(FAIL_MARK):
            broken[current] = line[len(FAIL_MARK):].strip()
        else:
            per_block[current].append(line)

    errors: list[str] = []
    notes: list[str] = []
    for body, line_no, block_index in expected:
        if block_index in broken:
            notes.append(f"{path.relative_to(ROOT)}:{line_no}: код блока не выполняется "
                         f"({broken[block_index]}) — не проверено")
            continue
        actual = {l.strip() for l in per_block.get(block_index, []) if l.strip()}
        for line in body.splitlines():
            stripped = line.strip()
            if not stripped or NOISE_RE.match(stripped):
                continue
            if stripped not in actual:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_no}: строки нет в настоящем выводе: {stripped[:70]!r}"
                )
                break  # одного примера на блок достаточно
    return errors, notes, len(expected)


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
    chapters = blocks_total = 0
    for path in files:
        errors, notes, found = check_file(path, args.verbose)
        if found:
            chapters += 1
            blocks_total += found
        all_errors.extend(errors)
        all_notes.extend(notes)

    verified = blocks_total - len(all_notes) - len(all_errors)
    print(f"Глав с кодом и показанным выводом: {chapters}; "
          f"блоков вывода: {blocks_total}, из них сверено с реальным запуском: {verified}")
    if all_notes:
        print(f"\nНе сверено ({len(all_notes)}) — этот код в песочнице не выполняется:")
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
