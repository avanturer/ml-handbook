#!/usr/bin/env python3
"""Проверка покрытия: закрывает ли хендбук известные точки провала на собеседованиях.

Список составлен из research-дампов (`.handbook/GAPS-CHECKLIST.md`) — это концепции,
на которых кандидаты сыпятся чаще всего. Правило простое: если тема названа в списке,
в соответствующей главе должен быть текст, отвечающий на неё.

Проверка грубая — по ключевым словам. Она не доказывает, что тема раскрыта хорошо,
но надёжно ловит случай «темы нет вообще».

Запуск:
    python tools/check_coverage.py
    python tools/check_coverage.py --verbose   # показать и закрытые пункты
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# (тема, где искать, паттерны — достаточно одного совпадения)
COVERAGE: list[tuple[str, str, list[str]]] = [
    # --- метрики и классический ML ---
    ("ROC-AUC как ранговая статистика", "02-classic-ml/04-metrics.md",
     [r"Манна[-\s]?Уитни", r"вероятност\w+ (?:смысл|интерпретаци)"]),
    ("Почему ROC-AUC обманывает при дисбалансе", "02-classic-ml/04-metrics.md",
     [r"дисбаланс", r"PR-AUC"]),
    ("Выбор порога через матрицу стоимостей", "02-classic-ml/04-metrics.md",
     [r"матриц\w+ стоимост", r"стоимост\w+ ошиб"]),
    ("Bias-variance как разложение с выводом", "02-classic-ml/01-learning-theory.md",
     [r"разложени\w+ (?:на )?смещени", r"bias[-\s]?variance"]),
    ("Почему L1 зануляет (геометрия или субградиент)", "02-classic-ml/02-linear-models.md",
     [r"субградиент", r"мягк\w+ порог", r"soft[-\s]?threshold"]),
    ("Ridge как MAP с гауссовым априором", "02-classic-ml/02-linear-models.md",
     [r"MAP", r"априорн"]),
    ("Почему в логрег не MSE", "02-classic-ml/03-logistic-regression.md",
     [r"невыпукл", r"затухани\w+ градиент"]),
    ("Ordered boosting и target statistics в CatBoost", "02-classic-ml/08-boosting-in-practice.md",
     [r"ordered (?:boosting|target)", r"prediction shift"]),
    ("GOSS и EFB в LightGBM", "02-classic-ml/08-boosting-in-practice.md",
     [r"GOSS", r"EFB"]),
    ("Каталог утечек данных", "02-classic-ml/13-validation-and-leakage.md",
     [r"утечк", r"leakage"]),
    ("Target encoding и out-of-fold", "02-classic-ml/14-feature-engineering.md",
     [r"out[-\s]?of[-\s]?fold", r"target encoding"]),
    ("SMOTE и почему он часто вредит", "02-classic-ml/12-imbalance-and-calibration.md",
     [r"SMOTE"]),
    ("Калибровка: Платт и изотоническая", "02-classic-ml/12-imbalance-and-calibration.md",
     [r"[Ии]зотоническ", r"Платт"]),

    # --- deep learning ---
    ("Почему делим на sqrt(d_k)", "03-deep-learning/04-attention-and-transformer.md",
     [r"\\sqrt\{d_k\}", r"дисперси\w+ логит"]),
    ("Pre-LN против post-LN", "03-deep-learning/04-attention-and-transformer.md",
     [r"pre-LN", r"post-LN"]),
    ("Bias correction в Adam", "03-deep-learning/02-training-dynamics.md",
     [r"bias correction", r"коррекци\w+ смещени"]),
    ("Xavier и He: вывод через дисперсию", "03-deep-learning/02-training-dynamics.md",
     [r"Xavier", r"He"]),
    ("Почему LayerNorm, а не BatchNorm", "03-deep-learning/02-training-dynamics.md",
     [r"LayerNorm", r"BatchNorm"]),

    # --- LLM ---
    ("Размер KV-кэша и как его считать", "05-llm/05-inference-and-serving.md",
     [r"KV-кэш", r"KV cache"]),
    ("Prefill compute-bound, decode memory-bound", "05-llm/05-inference-and-serving.md",
     [r"memory-bound", r"compute-bound"]),
    ("LoRA: ранг, alpha, куда вешать", "05-llm/04-peft-and-quantization.md",
     [r"LoRA", r"ранг"]),
    ("Вывод DPO из RLHF с KL", "05-llm/03-sft-and-alignment.md",
     [r"DPO"]),
    ("Chinchilla: ~20 токенов на параметр", "05-llm/02-pretraining-and-scaling.md",
     [r"Chinchilla"]),

    # --- recsys ---
    ("Почему «просто SVD» не работает на пропусках", "06-recsys/03-collaborative-filtering.md",
     [r"пропуск", r"заполнени\w+ нул"]),
    ("Вывод шага ALS для implicit", "06-recsys/04-implicit-feedback.md",
     [r"ALS", r"confidence"]),
    ("Вывод функции потерь BPR", "06-recsys/04-implicit-feedback.md",
     [r"BPR"]),
    ("LambdaRank: градиент через ΔNDCG", "06-recsys/07-learning-to-rank.md",
     [r"Lambda(?:Rank|MART)", r"NDCG"]),
    ("Позиционный биас и IPS", "06-recsys/07-learning-to-rank.md",
     [r"позиционн\w+ биас", r"IPS", r"propensity"]),
    ("Почему офлайн-метрики расходятся с онлайном", "06-recsys/02-metrics-offline.md",
     [r"офлайн", r"онлайн"]),
    ("Semantic IDs и генеративный ретривал", "06-recsys/11-llm-recsys.md",
     [r"semantic ID", r"TIGER", r"генеративн\w+ ретривал"]),
    ("Петля обратной связи и вырождение выдачи", "06-recsys/12-cold-start-and-bias.md",
     [r"петл\w+ обратной связи", r"feedback loop"]),

    # --- прод и мониторинг ---
    ("Point-in-time correctness", "07-mlops/03-data-and-feature-store.md",
     [r"point[-\s]?in[-\s]?time"]),
    ("Train/serve skew", "07-mlops/03-data-and-feature-store.md",
     [r"skew"]),
    ("Shadow, canary, blue-green", "07-mlops/08-deployment-strategies.md",
     [r"shadow", r"canary|канареечн"]),
    ("Почему смотрят p99, а не среднее", "07-mlops/09-inference-optimization.md",
     [r"p99"]),
    ("PSI и его пороги", "09-monitoring/03-drift-detection.md",
     [r"PSI"]),
    ("Разница ковариативного сдвига и концепт-дрифта", "09-monitoring/03-drift-detection.md",
     [r"концепт[-\s]?дрифт", r"ковариативн"]),
    ("Мониторинг без разметки: прокси-метрики", "09-monitoring/04-model-degradation.md",
     [r"прокси", r"отложенн\w+ разметк"]),

    # --- A/B ---
    ("MDE и вывод размера выборки", "10-ab-testing/01-experiment-design.md",
     [r"MDE", r"размер выборки"]),
    ("Ratio-метрики и дельта-метод", "10-ab-testing/02-statistical-criteria.md",
     [r"дельта[-\s]?метод", r"ratio[-\s]?метрик"]),
    ("Чем p-value НЕ является", "01-math/03-statistics.md",
     [r"НЕ является|не является"]),
    ("CUPED: вывод и требование к ковариате", "10-ab-testing/03-variance-reduction.md",
     [r"CUPED"]),
    ("Подглядывание и инфляция FPR", "10-ab-testing/04-pitfalls.md",
     [r"подглядыван", r"peeking"]),
    ("SRM и проверка хи-квадрат", "10-ab-testing/04-pitfalls.md",
     [r"SRM"]),
    ("Множественные сравнения: Bonferroni и FDR", "10-ab-testing/04-pitfalls.md",
     [r"Bonferroni", r"FDR|Benjamini"]),
    ("Парадокс Симпсона с механизмом", "10-ab-testing/04-pitfalls.md",
     [r"Симпсон"]),
    ("Switchback и сетевые эффекты", "10-ab-testing/05-complex-designs.md",
     [r"switchback|свитчбэк", r"сетев\w+ эффект"]),
    ("Что на самом деле проверяет Манн — Уитни", "10-ab-testing/02-statistical-criteria.md",
     [r"Манн\w*\s*[—-]\s*Уитни", r"Mann\s*[—-]?\s*Whitney"]),
    ("Тест Уэлча как разумный дефолт", "10-ab-testing/02-statistical-criteria.md",
     [r"Уэлч"]),
    ("Тяжёлые хвосты: винзоризация и бутстрап", "10-ab-testing/02-statistical-criteria.md",
     [r"винзориз", r"тяж\w+ хвост"]),
    ("Novelty и primacy: как детектировать", "10-ab-testing/04-pitfalls.md",
     [r"новизн", r"novelty"]),
    ("Guardrail-метрики и решение при их просадке", "10-ab-testing/01-experiment-design.md",
     [r"guardrail|гардрейл"]),
    ("Выбросы фильтруются по предэкспериментальному периоду", "10-ab-testing/04-pitfalls.md",
     [r"выброс"]),

    # --- system design и код ---
    ("Каркас ответа: уточнения до модели", "11-system-design/01-framework.md",
     [r"уточн"]),
    ("Бюджет латентности по стадиям", "11-system-design/01-framework.md",
     [r"бюджет латентност"]),
    ("Обязательный неML-бейзлайн", "11-system-design/01-framework.md",
     [r"бейзлайн"]),
    ("ROC-AUC с нуля через ранги", "12-coding/03-ml-from-scratch.md",
     [r"ROC-AUC", r"ранг"]),
    ("GIL и выбор конкурентности", "12-coding/01-python-for-mle.md",
     [r"GIL"]),
    ("Оконные функции", "08-big-data/02-sql-for-mle.md",
     [r"ROW_NUMBER|оконн\w+ функц"]),
    ("Перекос данных в Spark и salting", "08-big-data/04-spark-tuning.md",
     [r"salting|солен", r"перекос|skew"]),
    ("Гарантии доставки Kafka", "08-big-data/05-streaming.md",
     [r"exactly[-\s]?once", r"at[-\s]?least[-\s]?once"]),
    ("Идемпотентность задач Airflow", "08-big-data/06-orchestration.md",
     [r"идемпотент"]),

    # --- пробелы, найденные прочёсом внешних программ (.handbook/sweep/GAPS.md) ---
    # Каждая из этих тем всплыла в 2-6 независимых прочёсах и до ревизии
    # не встречалась в хендбуке ни разу. Держим их проверяемыми, чтобы не отъехали обратно.
    ("Стекинг: out-of-fold как единственный корректный источник мета-признаков",
     "02-classic-ml/19-stacking-and-blending.md",
     [r"out[-\s]?of[-\s]?fold"]),
    ("Блендинг и чем он отличается от стекинга",
     "02-classic-ml/19-stacking-and-blending.md",
     [r"блендинг"]),
    ("Разбор ошибок: ceiling analysis", "02-classic-ml/20-error-analysis.md",
     [r"ceiling|потолок|сквозн\w+ точност"]),
    ("Разбор ошибок: сегментный анализ и поиск слабых подгрупп",
     "02-classic-ml/20-error-analysis.md",
     [r"сегмент"]),
    ("Разбор ошибок: кривые обучения как ответ «данные или модель»",
     "02-classic-ml/20-error-analysis.md",
     [r"кривы\w+ обучени|learning_curve"]),
    ("RL: MDP и уравнение Беллмана", "03-deep-learning/07-rl-foundations.md",
     [r"MDP|марковск\w+ процесс"]),
    ("RL: Q-learning", "03-deep-learning/07-rl-foundations.md",
     [r"Q-learning|Q-обучени"]),
    ("RL: policy gradient, baseline и advantage",
     "03-deep-learning/07-rl-foundations.md",
     [r"REINFORCE", r"advantage|преимуществ"]),
    ("RL: PPO и clipped surrogate", "03-deep-learning/07-rl-foundations.md",
     [r"PPO"]),
    ("Генеративные: ELBO и reparametrization trick",
     "03-deep-learning/08-generative-models.md",
     [r"ELBO", r"reparametriz|репараметриз"]),
    ("Генеративные: VQ-VAE и straight-through",
     "03-deep-learning/08-generative-models.md",
     [r"VQ-VAE"]),
    ("Генеративные: диффузия, DDPM и classifier-free guidance",
     "03-deep-learning/08-generative-models.md",
     [r"DDPM|диффуз"]),
    ("Разметка: согласованность аннотаторов", "07-mlops/11-data-and-labeling.md",
     [r"каппа|Коэн|Криппендорф"]),
    ("Разметка: агрегация меток и Dawid-Skene", "07-mlops/11-data-and-labeling.md",
     [r"Dawid|Дэвид|Давид"]),
    ("Разметка: активное обучение и когда оно окупается",
     "07-mlops/11-data-and-labeling.md",
     [r"активн\w+ обучени|active learning"]),
    ("Разметка: поиск ошибочных меток", "07-mlops/11-data-and-labeling.md",
     [r"confident learning|ошибочн\w+ мет"]),
    ("Безопасность: состязательные примеры и переносимость",
     "07-mlops/12-ml-security.md",
     [r"состязательн|adversarial"]),
    ("Безопасность: отравление обучающей выборки", "07-mlops/12-ml-security.md",
     [r"отравлени|poisoning"]),
    ("Безопасность: membership inference и дифференциальная приватность",
     "07-mlops/12-ml-security.md",
     [r"membership inference"]),
    ("Справедливость: групповые критерии", "09-monitoring/08-fairness.md",
     [r"equalized odds|demographic parity"]),
    ("Справедливость: доказанная несовместимость критериев",
     "09-monitoring/08-fairness.md",
     [r"невозможност|несовместим"]),
    ("Платформа экспериментов: слои и ортогональность",
     "10-ab-testing/07-experiment-platform.md",
     [r"сло[йя]|layer"]),
    ("Платформа экспериментов: counterfactual logging",
     "10-ab-testing/07-experiment-platform.md",
     [r"counterfactual|контрфакт"]),
    ("Триггерный анализ", "10-ab-testing/03-variance-reduction.md",
     [r"триггерн\w+ (?:популяц|анализ|метрик)"]),
    ("Байесовский A/B", "10-ab-testing/02-statistical-criteria.md",
     [r"байесовск"]),
    ("HPO: Hyperband и Successive Halving",
     "02-classic-ml/08-boosting-in-practice.md",
     [r"Hyperband|Successive Halving|ASHA"]),
    ("Устройство GPU: roofline и арифметическая интенсивность",
     "03-deep-learning/06-scaling-and-efficiency.md",
     [r"roofline|арифметическ\w+ интенсивност"]),
    ("KV-кэш как инфраструктура: маршрутизация и оффлоад",
     "05-llm/05-inference-and-serving.md",
     [r"KV-aware|оффлоад|offload"]),
    ("Test-time compute как ось масштабирования",
     "05-llm/06-prompting-and-structured-output.md",
     [r"test-time|вычислени\w+ на инференс"]),
    ("Агенты: context engineering и память как подсистема",
     "05-llm/08-agents-and-tools.md",
     [r"context engineering|инженери\w+ контекст"]),
    ("Дизайн-док как артефакт", "11-system-design/01-framework.md",
     [r"дизайн-док"]),
    ("«А нужен ли здесь ML»", "07-mlops/01-ml-lifecycle.md",
     [r"нужен ли.{0,20}ML|эвристик"]),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    missing_chapter, not_covered, covered = [], [], []

    for topic, rel_path, patterns in COVERAGE:
        path = DOCS / rel_path
        if not path.exists():
            missing_chapter.append((topic, rel_path))
            continue
        text = path.read_text(encoding="utf-8")
        if any(re.search(p, text, re.IGNORECASE) for p in patterns):
            covered.append((topic, rel_path))
        else:
            not_covered.append((topic, rel_path))

    print(f"Проверено тем: {len(COVERAGE)}")
    print(f"  закрыто:            {len(covered)}")
    print(f"  не найдено в главе: {len(not_covered)}")
    print(f"  главы ещё нет:      {len(missing_chapter)}")

    if args.verbose and covered:
        print("\nЗакрытые темы:")
        for topic, rel in covered:
            print(f"  + {topic}  [{rel}]")

    if missing_chapter:
        print("\nГлавы ещё не написаны:")
        for topic, rel in missing_chapter:
            print(f"  . {topic}  [{rel}]")

    if not_covered:
        print("\nТЕМА НЕ НАЙДЕНА В ГЛАВЕ (требует внимания):")
        for topic, rel in not_covered:
            print(f"  x {topic}  [{rel}]")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
