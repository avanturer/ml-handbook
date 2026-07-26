"""Метрики с нуля.

Задание: реализуйте функции так, чтобы прошли тесты из `code/tests/test_metrics.py`.
Пользоваться sklearn внутри реализаций нельзя — только numpy.

Норматив по времени (для подготовки к live-coding):
    confusion_counts     — 5 минут
    precision_recall_f1  — 5 минут
    roc_auc              — 15 минут   ← классическая задача с собеседования
    average_precision    — 15 минут
    ndcg_at_k            — 15 минут

Теория: docs/02-classic-ml/04-metrics.md и docs/06-recsys/02-metrics-offline.md
"""

from __future__ import annotations

import numpy as np


def confusion_counts(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[int, int, int, int]:
    """Возвращает (tp, fp, fn, tn) для бинарных меток и бинарных предсказаний.

    Подсказка: всё считается через булевы маски и .sum(), без единого цикла.
    """
    raise NotImplementedError("Реализуйте confusion_counts")


def precision_recall_f1(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[float, float, float]:
    """Точность, полнота и F1 для положительного класса.

    Внимание на краевые случаи: если предсказаний положительного класса нет,
    precision не определена — верните 0.0, а не NaN (и подумайте, почему
    в проде это может быть плохим решением).
    """
    raise NotImplementedError("Реализуйте precision_recall_f1")


def roc_auc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    """ROC-AUC без построения самой кривой.

    Ключевая идея: ROC-AUC равен вероятности того, что случайный положительный объект
    получит больший скор, чем случайный отрицательный. Отсюда следует связь со
    статистикой Манна-Уитни:

        AUC = (R_pos - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)

    где R_pos — сумма рангов положительных объектов при сортировке по скору
    по возрастанию, n_pos и n_neg — числа положительных и отрицательных объектов.

    Совпадающие скоры должны получать СРЕДНИЙ ранг — иначе результат разъедется
    с sklearn на данных с повторами. Это самая частая ошибка в этой задаче.
    """
    raise NotImplementedError("Реализуйте roc_auc")


def average_precision(y_true: np.ndarray, y_score: np.ndarray) -> float:
    """Average Precision — площадь под PR-кривой, считаемая как сумма по позициям.

        AP = sum_k (R_k - R_{k-1}) * P_k

    где P_k и R_k — precision и recall на отсечке k при сортировке по убыванию скора.
    """
    raise NotImplementedError("Реализуйте average_precision")


def dcg_at_k(relevances: np.ndarray, k: int) -> float:
    """DCG@k при бинарной или градуированной релевантности.

        DCG@k = sum_{i=1..k} (2^rel_i - 1) / log2(i + 1)

    `relevances` уже упорядочены так, как их выдала модель.
    """
    raise NotImplementedError("Реализуйте dcg_at_k")


def ndcg_at_k(relevances: np.ndarray, k: int) -> float:
    """NDCG@k = DCG@k / IDCG@k, где IDCG — DCG идеального порядка.

    Краевой случай: если идеальный DCG равен нулю (релевантных объектов нет),
    верните 0.0.
    """
    raise NotImplementedError("Реализуйте ndcg_at_k")
