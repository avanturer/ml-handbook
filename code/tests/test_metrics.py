"""Тесты к code/exercises/metrics.py.

Запуск:  pytest code/tests/test_metrics.py -v
Пока функции не реализованы, тесты падают с NotImplementedError — это нормально.
"""

from __future__ import annotations

import numpy as np
import pytest

from exercises.metrics import (
    average_precision,
    confusion_counts,
    dcg_at_k,
    ndcg_at_k,
    precision_recall_f1,
    roc_auc,
)

sklearn_metrics = pytest.importorskip("sklearn.metrics")


def test_confusion_counts_basic():
    y_true = np.array([1, 1, 0, 0, 1])
    y_pred = np.array([1, 0, 0, 1, 1])
    assert confusion_counts(y_true, y_pred) == (2, 1, 1, 1)


def test_precision_recall_f1_matches_sklearn():
    rng = np.random.default_rng(0)
    y_true = rng.integers(0, 2, size=500)
    y_pred = rng.integers(0, 2, size=500)
    precision, recall, f1 = precision_recall_f1(y_true, y_pred)
    assert precision == pytest.approx(sklearn_metrics.precision_score(y_true, y_pred), abs=1e-9)
    assert recall == pytest.approx(sklearn_metrics.recall_score(y_true, y_pred), abs=1e-9)
    assert f1 == pytest.approx(sklearn_metrics.f1_score(y_true, y_pred), abs=1e-9)


def test_precision_no_positive_predictions():
    """Краевой случай: модель не предсказала ни одного положительного."""
    y_true = np.array([1, 0, 1])
    y_pred = np.array([0, 0, 0])
    precision, recall, f1 = precision_recall_f1(y_true, y_pred)
    assert precision == 0.0 and recall == 0.0 and f1 == 0.0


def test_roc_auc_perfect_and_random():
    y_true = np.array([0, 0, 1, 1])
    assert roc_auc(y_true, np.array([0.1, 0.2, 0.8, 0.9])) == pytest.approx(1.0)
    assert roc_auc(y_true, np.array([0.9, 0.8, 0.2, 0.1])) == pytest.approx(0.0)


def test_roc_auc_matches_sklearn():
    rng = np.random.default_rng(42)
    y_true = rng.integers(0, 2, size=2000)
    y_score = rng.normal(size=2000) + y_true * 0.7
    assert roc_auc(y_true, y_score) == pytest.approx(
        sklearn_metrics.roc_auc_score(y_true, y_score), abs=1e-9
    )


def test_roc_auc_with_ties():
    """Совпадающие скоры должны получать средний ранг — самая частая ошибка."""
    y_true = np.array([0, 1, 0, 1, 1, 0])
    y_score = np.array([0.5, 0.5, 0.5, 0.9, 0.1, 0.5])
    assert roc_auc(y_true, y_score) == pytest.approx(
        sklearn_metrics.roc_auc_score(y_true, y_score), abs=1e-9
    )


def test_average_precision_matches_sklearn():
    rng = np.random.default_rng(7)
    y_true = (rng.random(1000) < 0.15).astype(int)   # дисбаланс, как в жизни
    y_score = rng.random(1000) + y_true * 0.4
    assert average_precision(y_true, y_score) == pytest.approx(
        sklearn_metrics.average_precision_score(y_true, y_score), abs=1e-6
    )


def test_dcg_known_value():
    """Проверка на числах, которые можно пересчитать в уме."""
    relevances = np.array([1, 0, 1])
    expected = 1 / np.log2(2) + 0 / np.log2(3) + 1 / np.log2(4)
    assert dcg_at_k(relevances, 3) == pytest.approx(expected)


def test_ndcg_perfect_order_is_one():
    relevances = np.array([3, 2, 1, 0])
    assert ndcg_at_k(relevances, 4) == pytest.approx(1.0)


def test_ndcg_no_relevant_items():
    assert ndcg_at_k(np.array([0, 0, 0]), 3) == 0.0


def test_ndcg_worse_order_is_lower():
    good = ndcg_at_k(np.array([3, 2, 1, 0]), 4)
    bad = ndcg_at_k(np.array([0, 1, 2, 3]), 4)
    assert bad < good
