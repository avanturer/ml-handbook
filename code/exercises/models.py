"""Модели с нуля.

Задание: реализуйте классы так, чтобы прошли тесты из `code/tests/test_models.py`.
Внутри реализаций разрешён только numpy.

Норматив по времени (для подготовки к live-coding):
    LinearRegressionGD    — 10 минут
    LogisticRegressionGD  — 15 минут
    KMeans                — 20 минут
    KNNClassifier         — 10 минут

Теория: docs/02-classic-ml/02-linear-models.md, 03-logistic-regression.md,
        10-clustering.md, 09-svm-knn-bayes.md
"""

from __future__ import annotations

import numpy as np


class LinearRegressionGD:
    """Линейная регрессия, обучаемая градиентным спуском.

    Минимизируем MSE:  L(w, b) = (1/n) * sum_i (x_i^T w + b - y_i)^2

    Градиенты:
        dL/dw = (2/n) * X^T (Xw + b - y)
        dL/db = (2/n) * sum(Xw + b - y)

    Подсказки:
      * не забудьте свободный член (intercept) — либо отдельной переменной,
        либо колонкой единиц в X; отдельной переменной честнее, потому что
        свободный член обычно не регуляризуют;
      * при слишком большом lr веса разойдутся в inf — это нормальное поведение,
        а не баг вашей реализации.
    """

    def __init__(self, lr: float = 0.05, n_steps: int = 2000):
        self.lr = lr
        self.n_steps = n_steps
        self.w: np.ndarray | None = None
        self.b: float = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegressionGD":
        raise NotImplementedError("Реализуйте LinearRegressionGD.fit")

    def predict(self, X: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Реализуйте LinearRegressionGD.predict")


class LogisticRegressionGD:
    """Логистическая регрессия с L2-регуляризацией.

    Функция потерь (log-loss + L2, свободный член не регуляризуется):

        L(w, b) = -(1/n) * sum_i [ y_i * log(p_i) + (1 - y_i) * log(1 - p_i) ]
                  + (l2 / 2) * ||w||^2,     где p_i = sigmoid(x_i^T w + b)

    Градиент по весам получается на удивление простым:

        dL/dw = (1/n) * X^T (p - y) + l2 * w
        dL/db = (1/n) * sum(p - y)

    Обязательно: устойчивая сигмоида. Наивная 1/(1+exp(-z)) переполняется
    при больших |z|; считайте отдельно для z >= 0 и z < 0.
    """

    def __init__(self, lr: float = 0.1, n_steps: int = 3000, l2: float = 0.0):
        self.lr = lr
        self.n_steps = n_steps
        self.l2 = l2
        self.w: np.ndarray | None = None
        self.b: float = 0.0

    @staticmethod
    def _sigmoid(z: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Реализуйте устойчивую сигмоиду")

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LogisticRegressionGD":
        raise NotImplementedError("Реализуйте LogisticRegressionGD.fit")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Возвращает вероятность положительного класса, форма (n,)."""
        raise NotImplementedError("Реализуйте LogisticRegressionGD.predict_proba")

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        raise NotImplementedError("Реализуйте LogisticRegressionGD.predict")


class KMeans:
    """Кластеризация K-средних с инициализацией k-means++.

    Алгоритм (координатный спуск по функционалу инерции):
      1. Инициализировать центры (k-means++ — см. подсказку ниже).
      2. Приписать каждый объект ближайшему центру.
      3. Пересчитать центры как средние своих кластеров.
      4. Повторять 2-3, пока приписывания меняются или пока не исчерпан лимит итераций.

    Инерция:  sum_i ||x_i - c_{a(i)}||^2, где a(i) — кластер объекта i.
    Она монотонно не возрастает — это удобный инвариант для самопроверки.

    k-means++: первый центр — случайный объект; каждый следующий выбирается
    случайно с вероятностью, пропорциональной квадрату расстояния до ближайшего
    из уже выбранных центров. Это резко снижает шанс плохого локального минимума.

    Подсказка по расстояниям: считайте матрицу (n, k) без циклов, через
    broadcasting: X[:, None, :] - centers[None, :, :].
    """

    def __init__(self, n_clusters: int = 3, max_iter: int = 300, random_state: int = 0):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.centers_: np.ndarray | None = None
        self.labels_: np.ndarray | None = None
        self.inertia_: float = float("inf")

    def fit(self, X: np.ndarray) -> "KMeans":
        raise NotImplementedError("Реализуйте KMeans.fit")

    def predict(self, X: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Реализуйте KMeans.predict")


class KNNClassifier:
    """Классификатор k ближайших соседей (евклидова метрика).

    Обучение здесь — просто запоминание выборки; вся работа в predict.

    Подсказка по производительности: наивный двойной цикл на 10 000 объектов
    будет считаться минутами. Векторизуйте расчёт попарных расстояний через
    тождество  ||a - b||^2 = ||a||^2 - 2 a^T b + ||b||^2  — это стандартный приём,
    и его любят спрашивать.
    """

    def __init__(self, k: int = 5):
        self.k = k
        self.X_train: np.ndarray | None = None
        self.y_train: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "KNNClassifier":
        raise NotImplementedError("Реализуйте KNNClassifier.fit")

    def predict(self, X: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Реализуйте KNNClassifier.predict")
