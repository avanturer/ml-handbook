#!/usr/bin/env python3
"""Проверка того, что глоссарий не отстал от книги.

Глоссарий — единственная страница, куда читатель приходит с вопросом «что это слово
вообще значит». Если книга дописывается, а словарь нет, страница тихо перестаёт работать:
человек ищет `shuffle`, не находит и больше сюда не возвращается. Ровно это и случилось
однажды — словарь покрывал половину терминов, включая те, что встречаются в книге
сотни раз.

Как проверяем. Берём термины, которые книга реально использует часто, и смотрим, есть ли
они в глоссарии. Порог по частоте нужен, чтобы не требовать словарной статьи для каждого
слова, встретившегося дважды: в словарь идёт то, обо что читатель спотыкается регулярно.

Список кандидатов собирается автоматически из аббревиатур и англоязычных терминов в тексте
плюс из явного списка русских терминов ниже — автоматика русские слова с падежами
разбирает плохо, и честнее перечислить их руками, чем делать вид, что морфология решена.

Запуск:
    python tools/check_glossary.py
    python tools/check_glossary.py --list   # показать частоты кандидатов
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
GLOSSARY = DOCS / "00-start" / "06-glossary.md"

# Термин попадает в кандидаты, если встречается в книге не реже этого числа раз.
MIN_MENTIONS = 40

# Английские слова и аббревиатуры, которые терминами НЕ являются: служебные слова,
# части путей, названия языков разметки и прочий шум.
STOPWORDS = {
    "the", "and", "for", "not", "with", "from", "this", "that", "you", "все", "как",
    "true", "false", "none", "null", "int", "str", "def", "return", "import", "print",
    "http", "https", "com", "org", "github", "arxiv", "pdf", "html", "json", "yaml",
    "csv", "sql", "api", "cpu", "gpu", "ram", "ssd", "url", "uri", "utf", "ascii",
    "md", "py", "sh", "id", "ok", "vs", "etc", "eg", "ie", "ml", "ai", "it",
    # маркеры уровня и служебные куски путей, а не термины
    "middle", "junior", "senior", "ml-", "docs", "handbook", "index",
    # названия языков, библиотек и продуктов: это инструменты, а не понятия;
    # словарь объясняет, что такое shuffle, а не что такое PyTorch
    "python", "pytorch", "tensorflow", "numpy", "pandas", "sklearn", "scikit",
    "lightgbm", "catboost", "xgboost", "redis", "postgres", "postgresql", "docker",
    "kubernetes", "linux", "bash", "git", "jupyter", "optuna", "mlflow",
    # обломки составных терминов, которые сами по себе ничего не значат
    "rate", "score", "loss", "size", "time", "data", "model", "test", "train",
    "set", "step", "layer", "head", "batch", "top", "base", "case", "type",
}

# Русские термины, которые обязаны быть в словаре. Морфология: ищем по основе.
RUSSIAN_TERMS = [
    "бустинг", "бэггинг", "стекинг", "калибровк", "утечк", "кросс-валидац",
    "регуляризац", "эмбеддинг", "трансформер", "токенизац", "перплекси",
    "коллаборативн", "холодн", "дрифт", "идемпотентн", "партиц", "мощност",
    "бутстрап", "дельта-метод", "доверительн", "предсказательн",
    "разброс", "смещени", "переобучени", "дистилляц", "квантизац",
]


def prose_only(text: str) -> str:
    """Оставляет только прозу.

    Без этой чистки список кандидатов возглавляют `frac`, `cdot` и `summary`: команды LaTeX,
    имена из кода и HTML-теги встречаются чаще любого настоящего термина, и проверка
    превращается в шум. Термин попадает в словарь, если о него спотыкаются в ТЕКСТЕ.
    """
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)      # блоки кода
    text = re.sub(r"`[^`\n]+`", " ", text)                        # строчный код
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.DOTALL)     # блочные формулы
    text = re.sub(r"\$[^$\n]+\$", " ", text)                      # строчные формулы
    text = re.sub(r"</?[a-zA-Z][^>]*>", " ", text)                # html-теги
    text = re.sub(r"\]\([^)]*\)", " ", text)                      # адреса ссылок
    return text


def book_text() -> str:
    parts = []
    for path in DOCS.rglob("*.md"):
        if path.name == "index.md" or path == GLOSSARY:
            continue
        parts.append(prose_only(path.read_text(encoding="utf-8")))
    return "\n".join(parts)


def candidates(text: str) -> Counter:
    """Англоязычные термины и аббревиатуры, встречающиеся достаточно часто."""
    words = re.findall(r"\b[A-Za-z][A-Za-z0-9-]{1,24}\b", text)
    counts = Counter(w for w in words if w.lower() not in STOPWORDS and len(w) > 1)
    # Схлопываем регистр, оставляя самое частое написание.
    merged: Counter = Counter()
    best: dict[str, str] = {}
    for word, n in counts.items():
        key = word.lower()
        merged[key] += n
        if n > counts[best.get(key, word)]:
            best[key] = word
    return Counter({best.get(k, k): v for k, v in merged.items() if v >= MIN_MENTIONS})


def main(argv: list[str]) -> int:
    if not GLOSSARY.exists():
        print("глоссарий не найден")
        return 1
    gloss = GLOSSARY.read_text(encoding="utf-8").lower()
    text = book_text()

    english = candidates(text)
    missing_en = [(w, n) for w, n in english.most_common() if w.lower() not in gloss]

    missing_ru = []
    for stem in RUSSIAN_TERMS:
        n = len(re.findall(stem, text, re.IGNORECASE))
        if n and stem.lower() not in gloss:
            missing_ru.append((stem, n))

    if "--list" in argv:
        print("Кандидаты по частоте:")
        for word, n in english.most_common(60):
            mark = " " if word.lower() in gloss else "x"
            print(f"  {mark} {n:>5}  {word}")

    entries = len(re.findall(r"^\*\*", GLOSSARY.read_text(encoding="utf-8"), re.MULTILINE))
    print(f"Записей в глоссарии: {entries}")
    print(f"Кандидатов (упоминаний ≥ {MIN_MENTIONS}): {len(english) + len(RUSSIAN_TERMS)}")

    missing = missing_en + missing_ru
    if missing:
        print(f"\nНЕ НАЙДЕНО В ГЛОССАРИИ ({len(missing)}):")
        for word, n in sorted(missing, key=lambda x: -x[1])[:40]:
            print(f"  . {n:>5} упоминаний  {word}")
        if len(missing) > 40:
            print(f"  … и ещё {len(missing) - 40}")
        # По умолчанию это подсказка, а не приговор: список кандидатов собран
        # эвристикой, и часть слов терминами не является. Жёсткий режим — для CI,
        # когда список уже вычищен и любое новое отставание надо ловить.
        print("\nЭто список кандидатов, а не список ошибок: решает автор.")
        return 1 if "--strict" in sys.argv else 0

    print("\nГлоссарий покрывает все частые термины книги.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
