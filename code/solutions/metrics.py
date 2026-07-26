"""Эталонные реализации метрик.

Открывайте ТОЛЬКО после того, как написали свою версию: сравнение своего решения
с чужим — полезно, чтение чужого вместо своего — нет.
"""

from __future__ import annotations

import numpy as np


def confusion_counts(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[int, int, int, int]:
    y_true = np.asarray(y_true).astype(bool)
    y_pred = np.asarray(y_pred).astype(bool)
    tp = int(np.sum(y_true & y_pred))
    fp = int(np.sum(~y_true & y_pred))
    fn = int(np.sum(y_true & ~y_pred))
    tn = int(np.sum(~y_true & ~y_pred))
    return tp, fp, fn, tn


def precision_recall_f1(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[float, float, float]:
    tp, fp, fn, _ = confusion_counts(y_true, y_pred)
    # 0.0 при неопределённости — та же конвенция, что у sklearn с zero_division=0.
    # В проде так делать опасно: «precision = 0» и «precision не определена» —
    # разные состояния, и алерт на них должен быть разный.
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    denom = precision + recall
    f1 = 2 * precision * recall / denom if denom > 0 else 0.0
    return precision, recall, f1


def roc_auc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    """AUC через статистику Манна-Уитни: считаем ранги, а не строим кривую."""
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score, dtype=float)

    n_pos = int(np.sum(y_true == 1))
    n_neg = int(np.sum(y_true == 0))
    if n_pos == 0 or n_neg == 0:
        return float("nan")   # AUC не определён, если есть только один класс

    order = np.argsort(y_score, kind="mergesort")
    sorted_scores = y_score[order]
    ranks = np.empty(len(y_score), dtype=float)

    # средние ранги внутри групп одинаковых скоров: без этого результат
    # разъедется со sklearn на данных с повторами
    i, n = 0, len(sorted_scores)
    while i < n:
        j = i
        while j + 1 < n and sorted_scores[j + 1] == sorted_scores[i]:
            j += 1
        ranks[order[i : j + 1]] = (i + j) / 2.0 + 1.0
        i = j + 1

    rank_sum_pos = ranks[y_true == 1].sum()
    return float((rank_sum_pos - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg))


def average_precision(y_true: np.ndarray, y_score: np.ndarray) -> float:
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score, dtype=float)

    n_pos = int(np.sum(y_true == 1))
    if n_pos == 0:
        return 0.0

    order = np.argsort(-y_score, kind="mergesort")
    y_sorted = y_true[order]
    scores_sorted = y_score[order]

    tp = np.cumsum(y_sorted)
    k = np.arange(1, len(y_sorted) + 1)
    precision = tp / k
    recall = tp / n_pos

    # точки отсечки берём только там, где скор меняется: внутри группы
    # одинаковых скоров порядок произволен, и промежуточные точки не имеют смысла
    distinct = np.r_[np.diff(scores_sorted) != 0, True]
    precision_d = precision[distinct]
    recall_d = recall[distinct]
    recall_prev = np.r_[0.0, recall_d[:-1]]
    return float(np.sum((recall_d - recall_prev) * precision_d))


def dcg_at_k(relevances: np.ndarray, k: int) -> float:
    rel = np.asarray(relevances, dtype=float)[:k]
    if rel.size == 0:
        return 0.0
    discounts = np.log2(np.arange(2, rel.size + 2))
    return float(np.sum((np.power(2.0, rel) - 1.0) / discounts))


def ndcg_at_k(relevances: np.ndarray, k: int) -> float:
    rel = np.asarray(relevances, dtype=float)
    ideal = np.sort(rel)[::-1]
    idcg = dcg_at_k(ideal, k)
    if idcg == 0.0:
        return 0.0
    return float(dcg_at_k(rel, k) / idcg)
