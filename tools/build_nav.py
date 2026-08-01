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

# Части книги. Пятнадцать разделов подряд — это список, а не книга: читатель не видит,
# зачем он сейчас читает именно это и что будет уметь через сто страниц. Части задают
# сюжет: язык -> ядро -> представления -> доказательства -> инженерия -> сборка -> обобщение.
# Порядок разделов внутри части = порядок каталогов, менять его надо через renumber_section.
PARTS: list[dict] = [
    {
        "title": "Перед началом",
        "sections": ["00-start"],
        "lead": "Как устроена книга, как её читать, чтобы знание осталось, и что вообще "
                "спрашивают на собеседовании MLE. Двадцать минут здесь экономят недели дальше.",
    },
    {
        "title": "Часть I. Язык",
        "sections": ["01-math"],
        "lead": "Всё, что дальше, формулируется на языке линейной алгебры, вероятности "
                "и оптимизации. Здесь мы берём из математики ровно тот минимум, который "
                "реально используется в работе и на собеседовании, — и берём его с выводами, "
                "чтобы потом не пришлось верить формулам на слово.",
        "after": "вы читаете формулу функции потерь и видите в ней смысл, а не набор значков.",
    },
    {
        "title": "Часть II. Ядро",
        "sections": ["02-classic-ml"],
        "lead": "Здесь живёт профессия. Что значит «модель обучилась», почему это вообще "
                "работает на новых данных, чем измерять качество и на чём измерять, "
                "как устроены линейные модели, деревья и бустинг — и как всё это ломается. "
                "Порядок внутри части не случаен: сначала чем мерить, потом на чём мерить, "
                "и только потом модели.",
        "after": "вы решаете табличную задачу целиком: от постановки до честной оценки — "
                 "и понимаете, где именно у вас утечка.",
    },
    {
        "title": "Часть III. Представления",
        "sections": ["03-deep-learning", "04-nlp", "05-llm"],
        "lead": "Классический ML требует, чтобы признаки составил человек. Как только данные "
                "перестают быть таблицей — текст, последовательность, картинка, — это "
                "перестаёт работать, и признаки приходится учить. Отсюда одна сквозная линия "
                "на три раздела: **представление** — от эмбеддинга слова до механизма внимания "
                "и большой языковой модели. Это не три разные темы, а одна, разобранная "
                "с нарастающей сложностью.",
        "after": "вы понимаете, откуда в модели берутся векторы, почему внимание вытеснило "
                 "рекуррентность и что именно происходит внутри LLM на каждом шаге.",
    },
    {
        "title": "Часть IV. Доказательства",
        "sections": ["06-ab-testing"],
        "lead": "Офлайн-метрика выросла. Значит ли это, что стало лучше? Почти всегда нет — "
                "и это самая дорогая ошибка в отрасли. Часть отвечает на вопрос, как доказать "
                "пользу изменения на живых пользователях и не обмануть себя по дороге. "
                "Она стоит здесь, а не в конце, потому что дальше без неё нельзя: выкатка, "
                "рекомендации и проектная секция все опираются на умение измерять эффект.",
        "after": "вы проектируете эксперимент, считаете его размер и объясняете, почему "
                 "нельзя подглядывать.",
    },
    {
        "title": "Часть V. Инженерия",
        "sections": ["07-mlops", "08-big-data", "09-monitoring"],
        "lead": "Модель, которая живёт в ноутбуке, не приносит пользы. Здесь она доезжает "
                "до пользователя и начинает жить: воспроизводимость, признаки, сервинг, "
                "данные в масштабе, наблюдаемость и то, что происходит с качеством через "
                "полгода после выката.",
        "after": "вы отвечаете не только «какая модель», но и «как она попадёт в прод, "
                 "сколько будет стоить и как вы узнаете, что она сломалась».",
    },
    {
        "title": "Часть VI. Первая полная система",
        "sections": ["10-recsys"],
        "lead": "Рекомендации — самый полный домен в ML: здесь одновременно нужны метрики "
                "и валидация из части II, эмбеддинги и трансформеры из части III, "
                "A/B из части IV и весь прод из части V. Поэтому раздел стоит именно тут: "
                "раньше его читать нечем. Это первая сборка всего, что вы знаете, "
                "в одну работающую систему.",
        "after": "вы проектируете рекомендательную систему целиком — от кандидатов "
                 "до онлайн-оценки — и знаете, где она деградирует.",
    },
    {
        "title": "Часть VII. Обобщение",
        "sections": ["11-system-design"],
        "lead": "То же самое, но на любом домене. Каркас ответа на проектной секции "
                "и семь полных разборов: лента, поиск, антифрод, RAG-ассистент, "
                "realtime-персонализация, отток, реклама.",
        "after": "вы проходите секцию ML System Design и ведёте проектное обсуждение "
                 "на работе.",
    },
    {
        "title": "Тренажёр",
        "sections": ["12-coding"],
        "lead": "Не глава в очереди, а зал, куда заходят по мере надобности. "
                "Если голова понимает, а руки не пишут — вам сюда, и можно в любой момент.",
    },
    {
        "title": "Приложения",
        "sections": ["13-optional", "14-career"],
        "lead": "Смежные модальности для не-профильного инженера и то, что происходит "
                "вокруг найма и роста.",
    },
]


def part_of(slug: str) -> dict | None:
    return next((p for p in PARTS if slug in p["sections"]), None)


SECTION_TITLES = {
    "00-start": ("Старт", "Как устроена книга, как её читать, что спрашивают на собеседовании и как учить, чтобы осталось."),
    "01-math": ("Математика", "Линейная алгебра, вероятность, статистика и оптимизация — только то, что реально нужно инженеру."),
    "02-classic-ml": ("Классический ML", "Ядро профессии: от постановки задачи обучения до бустинга, валидации и работы с признаками."),
    "03-deep-learning": ("Deep Learning", "Как на самом деле обучается сеть — от вывода backprop до трансформера и масштабирования."),
    "04-nlp": ("NLP", "Текст как данные: токенизация, эмбеддинги, энкодеры, задачи и метрики, продакшен."),
    "05-llm": ("LLM", "Большие языковые модели: устройство, обучение, выравнивание, инференс, RAG, агенты и прод."),
    "10-recsys": ("Рекомендательные системы", "Классика и современность: от матричной факторизации до генеративного ретривала на LLM."),
    "07-mlops": ("Выкатка в прод / MLOps", "Путь модели от эксперимента до пользователей: упаковка, сервинг, CI/CD, стоимость."),
    "08-big-data": ("Big Data", "Данные в масштабе: форматы, SQL, Spark, стриминг, оркестрация, распределённое обучение."),
    "09-monitoring": ("Мониторинг", "Что происходит с моделью после выката и как узнать об этом раньше пользователей."),
    "06-ab-testing": ("A/B-тесты", "Как доказать, что изменение принесло пользу, и не обмануть себя по дороге."),
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


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((?!https?://)[^)]+\)")


def clean(text: str) -> str:
    """Схлопывает переносы, убирает разметку цитаты и разворачивает внутренние ссылки.

    Ссылки разворачиваем в обычный текст намеренно: описание главы переезжает в оглавление
    и в витрину раздела, где относительный путь из исходной главы уже не разрешается.
    Проще снять ссылку, чем пересчитывать путь для каждого места назначения.
    """
    text = re.sub(r"\n>\s*", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = MD_LINK_RE.sub(r"\1", text)
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


def write_section_index(slug: str, chapters: list[Chapter],
                        sections: dict[str, list[Chapter]]) -> None:
    """Витрина раздела с соединительной тканью: откуда вы пришли и куда идёте.

    Голая таблица глав ничего не говорит о том, зачем читатель здесь оказался.
    Поэтому сверху — место раздела в книге и то, что к этому моменту уже освоено,
    снизу — переход к следующему разделу.
    """
    title, description = SECTION_TITLES[slug]
    part = part_of(slug)
    order = list(sections)
    index = order.index(slug)

    lines = [f"# {title}", "", f"> {description}", ""]

    if part:
        siblings = [s for s in part["sections"] if s in sections]
        place = (f"**{part['title']}**"
                 + (f", раздел {siblings.index(slug) + 1} из {len(siblings)}"
                    if len(siblings) > 1 else ""))
        lines += [f"{place} · глав в разделе: {len(chapters)}", ""]
        lines += [part["lead"], ""]
        if part.get("after"):
            lines += [f"**После этой части:** {part['after']}", ""]
    else:
        lines += [f"**Глав в разделе:** {len(chapters)}", ""]

    # Что читатель уже прошёл — не абстрактно, а конкретной ссылкой назад.
    if index > 0:
        prev_slug = order[index - 1]
        prev_title, _ = SECTION_TITLES[prev_slug]
        lines += [
            f"Перед этим разделом идёт **[{prev_title}]({relative_section(slug, prev_slug)})** — "
            f"если вы пришли сюда сразу, загляните в строку «Предварительно нужно» "
            f"в шапке первой главы.",
            "",
        ]

    lines += [
        "## Карта раздела",
        "",
        "| # | Глава | Уровень | О чём |",
        "|---|---|---|---|",
    ]
    for chapter in chapters:
        purpose = chapter.purpose or "—"
        level = chapter.level or "—"
        lines.append(f"| {chapter.number} | [{chapter.title}]({chapter.filename}) | {level} | {purpose} |")

    lines += ["", "---", ""]
    nav = []
    if index > 0:
        prev_slug = order[index - 1]
        nav.append(f"⬅️ [{SECTION_TITLES[prev_slug][0]}]({relative_section(slug, prev_slug)})")
    nav.append("🏠 [Оглавление книги](../index.md)")
    if index + 1 < len(order):
        next_slug = order[index + 1]
        nav.append(f"➡️ [{SECTION_TITLES[next_slug][0]}]({relative_section(slug, next_slug)})")
    lines += [" | ".join(nav), ""]

    (DOCS / slug / "index.md").write_text("\n".join(lines), encoding="utf-8")


def relative_section(source_slug: str, target_slug: str) -> str:
    return f"../{target_slug}/index.md"


def write_root_index(sections: dict[str, list[Chapter]]) -> None:
    """Оглавление как сюжет книги, а не как выгрузка ста двадцати пяти строк.

    Читатель должен с первого экрана понять, куда его ведут и зачем, поэтому части
    идут с рассказом «что даёт» и «что вы умеете после», а перечень глав — уже под ним.
    """
    total = sum(len(v) for v in sections.values())
    lines = [
        "# Оглавление",
        "",
        "> Это книга, а не сборник статей: части идут в том порядке, в котором их нужно "
        "читать, и каждая опирается на предыдущие. Пройдёте подряд — на выходе будете знать "
        "то, что спрашивают с middle+ MLE.",
        "",
        f"**Частей:** {len(PARTS)} · **разделов:** {len(sections)} · **глав:** {total}",
        "",
        "Первый раз здесь — [как пользоваться книгой](00-start/01-how-to-use.md). "
        "Если времени мало и нужен срез под конкретную задачу — "
        "[короткие маршруты](00-start/02-tracks.md).",
        "",
        "---",
        "",
    ]

    for part in PARTS:
        present = [s for s in part["sections"] if s in sections]
        if not present:
            continue
        chapters_in_part = sum(len(sections[s]) for s in present)
        lines += [
            f"## {part['title']}",
            "",
            f"{part['lead']}",
            "",
        ]
        if part.get("after"):
            lines += [f"**После этой части:** {part['after']}", ""]
        lines += [f"*Глав: {chapters_in_part}*", ""]

        for slug in present:
            title, description = SECTION_TITLES[slug]
            number = slug.split("-")[0]
            lines += [
                f"### {number} · [{title}]({slug}/index.md)",
                "",
                description,
                "",
            ]
            for chapter in sections[slug]:
                lines.append(f"- [{chapter.title}]({slug}/{chapter.filename})")
            lines.append("")
        lines.append("---")
        lines.append("")

    lines += [
        "🏠 [К README репозитория](../README.md)",
        "",
    ]
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


FOOTER_RE = re.compile(r"^(?:⬅️.*?\|\s*)?🏠 \[Оглавление\]\(\.\./index\.md\)(?:\s*\|\s*➡️.*)?$",
                       re.MULTILINE)


def write_footers(sections: dict[str, list[Chapter]]) -> None:
    """Проставляет стрелки «назад / оглавление / вперёд» по каноническому порядку.

    Подвал — это то, чем читатель пользуется, когда читает книгу подряд, и он же
    первым разъезжается при любой перестановке глав: после переноса главы стрелки
    начинают перепрыгивать через неё или вести назад через полкниги. Поэтому подвал
    не правится руками, а собирается из фактического порядка файлов.
    """
    flat: list[Chapter] = []
    for chapters in sections.values():
        flat.extend(chapters)

    changed = 0
    for index, chapter in enumerate(flat):
        parts = []
        if index > 0:
            prev = flat[index - 1]
            parts.append(f"⬅️ [{prev.title}]({relative_link(chapter, prev)})")
        parts.append("🏠 [Оглавление](../index.md)")
        if index + 1 < len(flat):
            nxt = flat[index + 1]
            parts.append(f"➡️ [{nxt.title}]({relative_link(chapter, nxt)})")
        footer = " | ".join(parts)

        text = chapter.path.read_text(encoding="utf-8")
        if not FOOTER_RE.search(text):
            continue
        new_text = FOOTER_RE.sub(lambda _m: footer, text, count=1)
        if new_text != text:
            chapter.path.write_text(new_text, encoding="utf-8")
            changed += 1
    print(f"Подвалы: пересобрано {changed} из {len(flat)}.")


def relative_link(source: Chapter, target: Chapter) -> str:
    """Ссылка из одной главы в другую: внутри раздела — имя файла, иначе через `../`."""
    if source.path.parent == target.path.parent:
        return target.filename
    return f"../{target.path.parent.name}/{target.filename}"


NAV_START = "# >>> nav: сгенерировано tools/build_nav.py — не редактировать вручную"
NAV_END = "# <<< конец сгенерированной навигации"


def render_nav(sections: dict[str, list[Chapter]]) -> str:
    """Навигация сайта повторяет части книги: боковое меню — это её содержание."""
    lines = [NAV_START, "nav:", "  - Оглавление: index.md"]
    for part in PARTS:
        present = [s for s in part["sections"] if s in sections]
        if not present:
            continue
        lines.append(f"  - {part['title']}:")
        for slug in present:
            title, _ = SECTION_TITLES[slug]
            lines.append(f"      - {title}:")
            lines.append(f"          - {slug}/index.md")
            for chapter in sections[slug]:
                safe_title = chapter.title.replace('"', "'")
                lines.append(f'          - "{safe_title}": {slug}/{chapter.filename}')
    lines.append(NAV_END)
    return "\n".join(lines)


def render_nav_flat(sections: dict[str, list[Chapter]]) -> str:
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


def update_readme_badges(sections: dict[str, list[Chapter]]) -> None:
    """Держит счётчики в шапке README в согласии с реальным числом файлов.

    Цифры в витрине — первое, что читатель может проверить. Если они врут,
    доверие к остальному тексту падает сразу, поэтому проставляем их автоматически.
    """
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    total = sum(len(v) for v in sections.values())

    text = re.sub(
        r'(<img alt="Разделов" src="https://img\.shields\.io/badge/разделов-)\d+',
        rf"\g<1>{len(sections)}",
        text,
    )
    text = re.sub(
        r'(<img alt="Глав" src="https://img\.shields\.io/badge/глав-)\d+',
        rf"\g<1>{total}",
        text,
    )

    # Счётчики в «Карте хендбука» тоже врут при добавлении главы, и заметить это
    # труднее, чем расхождение в шапке: там пятнадцать чисел, и глазами их не сверяют.
    # Проставляем каждое из числа реальных файлов раздела.
    fixed = 0

    def fix_section_count(match: re.Match[str]) -> str:
        nonlocal fixed
        head, slug, mid, claimed = (match.group(1), match.group(2),
                                    match.group(3), int(match.group(4)))
        if slug not in sections:
            return match.group(0)
        real = len(sections[slug])
        if real != claimed:
            fixed += 1
        return f"{head}{slug}{mid}{real}"

    # Карта в README перечисляет разделы ссылками вида [Название](docs/07-mlops/index.md) — 12.
    text = re.sub(
        r"(\]\(docs/)(\d\d-[a-z-]+)(/index\.md\) — )(\d+)",
        fix_section_count,
        text,
    )

    path.write_text(text, encoding="utf-8")
    note = f", исправлено счётчиков по разделам: {fixed}" if fixed else ""
    print(f"README: счётчики обновлены ({len(sections)} разделов, {total} глав){note}.")


def main() -> int:
    sections = collect()
    if not sections:
        print("Главы не найдены — нечего собирать.")
        return 1
    write_footers(sections)
    for slug, chapters in sections.items():
        write_section_index(slug, chapters, sections)
    write_root_index(sections)
    write_mkdocs_nav(sections)
    update_readme_badges(sections)
    total = sum(len(v) for v in sections.values())
    print(f"Собрано: {len(sections)} разделов, {total} глав.")
    for slug, chapters in sections.items():
        print(f"  {slug}: {len(chapters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
