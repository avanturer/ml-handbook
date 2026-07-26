#!/usr/bin/env python3
"""Проверка внешних ссылок хендбука.

Выдуманная ссылка в учебнике хуже отсутствующей: читатель теряет доверие ко всему тексту.
Скрипт собирает все http(s)-ссылки из `docs/` и проверяет, что они отвечают.

Запуск:
    python tools/check_links.py              # проверить все
    python tools/check_links.py --only arxiv # только ссылки, содержащие подстроку

Замечания:
  * используется HEAD, при отказе — GET (часть сайтов не поддерживает HEAD);
  * 403 от сайтов с защитой от ботов помечается отдельно и не считается ошибкой;
  * проверка идёт в несколько потоков, но с ограничением, чтобы не долбить arxiv.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
LINK_RE = re.compile(r"\]\((https?://[^)\s]+)\)")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ml-handbook-link-check/1.0)",
    "Accept": "*/*",
}
TIMEOUT = 20
# 403/429 обычно означают защиту от ботов, а не отсутствие страницы
SOFT_FAIL_CODES = {403, 429, 405}


def collect_links() -> dict[str, list[str]]:
    """url -> список файлов, где он встречается."""
    links: dict[str, list[str]] = defaultdict(list)
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for url in LINK_RE.findall(text):
            links[url.rstrip(".,;")].append(str(path.relative_to(ROOT)))
    return links


def probe(url: str) -> tuple[str, int | None, str]:
    """Возвращает (url, http-код или None, пояснение)."""
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=HEADERS, method=method)
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return url, response.status, "ok"
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (405, 403, 501):
                continue          # попробуем GET
            return url, exc.code, exc.reason or ""
        except urllib.error.URLError as exc:
            return url, None, f"сеть: {exc.reason}"
        except Exception as exc:  # noqa: BLE001 - сообщаем любую неожиданную проблему
            return url, None, f"{type(exc).__name__}: {exc}"
    return url, None, "не удалось проверить"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default="", help="проверять только ссылки с этой подстрокой")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    links = collect_links()
    urls = [u for u in sorted(links) if args.only in u]
    if not urls:
        print("Ссылок для проверки не найдено.")
        return 0

    print(f"Проверяю {len(urls)} уникальных ссылок...")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(probe, urls))

    broken, soft = [], []
    for url, code, note in results:
        if code is not None and 200 <= code < 400:
            continue
        entry = (url, code, note, links[url])
        (soft if code in SOFT_FAIL_CODES else broken).append(entry)

    if soft:
        print(f"\nОтвет с защитой от ботов ({len(soft)}) — проверьте вручную при желании:")
        for url, code, _, files in soft:
            print(f"  ? [{code}] {url}  ({files[0]})")

    if broken:
        print(f"\nБИТЫЕ ССЫЛКИ ({len(broken)}):")
        for url, code, note, files in broken:
            print(f"  x [{code or '-'}] {url}")
            print(f"      {note}")
            for f in dict.fromkeys(files):
                print(f"      в: {f}")
        return 1

    print(f"\nВсе {len(urls)} ссылок отвечают.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
