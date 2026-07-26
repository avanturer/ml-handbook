"""Тесты к code/exercises/models.py.

Запуск:  pytest code/tests/test_models.py -v
"""

from __future__ import annotations

import numpy as np
import pytest

from exercises.models import KMeans, KNNClassifier, LinearRegressionGD, LogisticRegressionGD


# --------------------------------------------------------------------------- линейная регрессия

def test_linear_regression_recovers_known_weights():
    """На данных без шума модель обязана восстановить истинные коэффициенты."""
    rng = np.random.default_rng(0)
    X = rng.normal(size=(500, 3))
    true_w, true_b = np.array([2.0, -1.0, 0.5]), 3.0
    y = X @ true_w + true_b

    model = LinearRegressionGD(lr=0.1, n_steps=5000).fit(X, y)
    assert np.allclose(model.w, true_w, atol=1e-2)
    assert model.b == pytest.approx(true_b, abs=1e-2)


def test_linear_regression_beats_mean_baseline():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(300, 5))
    y = X @ np.array([1.0, 0.0, -2.0, 0.5, 0.0]) + rng.normal(scale=0.3, size=300)

    model = LinearRegressionGD().fit(X, y)
    mse_model = np.mean((model.predict(X) - y) ** 2)
    mse_baseline = np.mean((y.mean() - y) ** 2)
    assert mse_model < 0.2 * mse_baseline


# ------------------------------------------------------------------------ логистическая регрессия

def test_sigmoid_is_numerically_stable():
    """Наивная реализация здесь даёт overflow и NaN."""
    z = np.array([-1000.0, -50.0, 0.0, 50.0, 1000.0])
    p = LogisticRegressionGD._sigmoid(z)
    assert np.all(np.isfinite(p))
    assert np.all((p >= 0.0) & (p <= 1.0))
    assert p[2] == pytest.approx(0.5)
    assert p[0] == pytest.approx(0.0, abs=1e-12)
    assert p[4] == pytest.approx(1.0, abs=1e-12)


def test_logistic_regression_separable_data():
    rng = np.random.default_rng(2)
    X = np.vstack([rng.normal(-2, 0.5, size=(200, 2)), rng.normal(2, 0.5, size=(200, 2))])
    y = np.array([0] * 200 + [1] * 200)

    model = LogisticRegressionGD(lr=0.5, n_steps=2000).fit(X, y)
    accuracy = (model.predict(X) == y).mean()
    assert accuracy > 0.98


def test_logistic_regression_probabilities_are_valid():
    rng = np.random.default_rng(3)
    X = rng.normal(size=(200, 4))
    y = (X[:, 0] + rng.normal(scale=0.5, size=200) > 0).astype(int)

    proba = LogisticRegressionGD().fit(X, y).predict_proba(X)
    assert proba.shape == (200,)
    assert np.all((proba >= 0.0) & (proba <= 1.0))


def test_l2_shrinks_weights():
    """Больше регуляризации — меньше норма весов. Инвариант, который легко проверить."""
    rng = np.random.default_rng(4)
    X = rng.normal(size=(300, 6))
    y = (X[:, 0] * 3 > 0).astype(int)

    weak = LogisticRegressionGD(l2=0.0, n_steps=1500).fit(X, y)
    strong = LogisticRegressionGD(l2=1.0, n_steps=1500).fit(X, y)
    assert np.linalg.norm(strong.w) < np.linalg.norm(weak.w)


# -------------------------------------------------------------------------------------- KMeans

def _three_blobs(seed: int = 0):
    rng = np.random.default_rng(seed)
    centers = np.array([[0.0, 0.0], [8.0, 8.0], [0.0, 8.0]])
    X = np.vstack([c + rng.normal(scale=0.4, size=(150, 2)) for c in centers])
    return X, centers


def test_kmeans_finds_well_separated_clusters():
    X, centers = _three_blobs()
    model = KMeans(n_clusters=3, random_state=0).fit(X)

    found = np.sort(model.centers_, axis=0)
    expected = np.sort(centers, axis=0)
    assert np.allclose(found, expected, atol=0.5)


def test_kmeans_inertia_decreases_with_more_clusters():
    X, _ = _three_blobs(seed=1)
    inertias = [KMeans(n_clusters=k, random_state=0).fit(X).inertia_ for k in (1, 2, 3, 5)]
    assert all(a > b for a, b in zip(inertias, inertias[1:]))


def test_kmeans_predict_matches_labels_on_train():
    X, _ = _three_blobs(seed=2)
    model = KMeans(n_clusters=3, random_state=0).fit(X)
    assert np.array_equal(model.predict(X), model.labels_)


# --------------------------------------------------------------------------------------- kNN

def test_knn_perfect_on_separable_data():
    rng = np.random.default_rng(5)
    X = np.vstack([rng.normal(-3, 0.4, size=(100, 2)), rng.normal(3, 0.4, size=(100, 2))])
    y = np.array([0] * 100 + [1] * 100)

    model = KNNClassifier(k=5).fit(X, y)
    assert (model.predict(X) == y).mean() > 0.99


def test_knn_k1_memorizes_training_set():
    """При k=1 предсказание на обучающей выборке обязано совпасть с метками."""
    rng = np.random.default_rng(6)
    X = rng.normal(size=(120, 3))
    y = rng.integers(0, 3, size=120)

    model = KNNClassifier(k=1).fit(X, y)
    assert np.array_equal(model.predict(X), y)


def test_knn_is_vectorized_enough():
    """Тест на скорость: наивный двойной цикл здесь не уложится."""
    import time

    rng = np.random.default_rng(7)
    X_train = rng.normal(size=(4000, 20))
    y_train = rng.integers(0, 2, size=4000)
    X_test = rng.normal(size=(2000, 20))

    model = KNNClassifier(k=10).fit(X_train, y_train)
    start = time.perf_counter()
    model.predict(X_test)
    assert time.perf_counter() - start < 5.0, "слишком медленно — векторизуйте расчёт расстояний"
