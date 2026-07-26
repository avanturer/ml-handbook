"""Эталонные реализации моделей.

Открывайте только после собственной попытки.
"""

from __future__ import annotations

import numpy as np


class LinearRegressionGD:
    def __init__(self, lr: float = 0.05, n_steps: int = 2000):
        self.lr = lr
        self.n_steps = n_steps
        self.w: np.ndarray | None = None
        self.b: float = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegressionGD":
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0
        for _ in range(self.n_steps):
            residual = X @ self.w + self.b - y          # (n,)
            self.w -= self.lr * (2.0 / n) * (X.T @ residual)
            self.b -= self.lr * (2.0 / n) * residual.sum()
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.asarray(X, dtype=float) @ self.w + self.b


class LogisticRegressionGD:
    def __init__(self, lr: float = 0.1, n_steps: int = 3000, l2: float = 0.0):
        self.lr = lr
        self.n_steps = n_steps
        self.l2 = l2
        self.w: np.ndarray | None = None
        self.b: float = 0.0

    @staticmethod
    def _sigmoid(z: np.ndarray) -> np.ndarray:
        z = np.asarray(z, dtype=float)
        out = np.empty_like(z)
        pos = z >= 0
        neg = ~pos
        out[pos] = 1.0 / (1.0 + np.exp(-z[pos]))
        # для отрицательных считаем через exp(z), иначе exp(-z) переполняется
        exp_z = np.exp(z[neg])
        out[neg] = exp_z / (1.0 + exp_z)
        return out

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LogisticRegressionGD":
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0
        for _ in range(self.n_steps):
            p = self._sigmoid(X @ self.w + self.b)
            diff = p - y                                 # градиент log-loss по логиту
            self.w -= self.lr * (X.T @ diff / n + self.l2 * self.w)
            self.b -= self.lr * diff.mean()              # свободный член не регуляризуем
        return self

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self._sigmoid(np.asarray(X, dtype=float) @ self.w + self.b)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        return (self.predict_proba(X) >= threshold).astype(int)


class KMeans:
    def __init__(self, n_clusters: int = 3, max_iter: int = 300, random_state: int = 0):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.centers_: np.ndarray | None = None
        self.labels_: np.ndarray | None = None
        self.inertia_: float = float("inf")

    @staticmethod
    def _sq_dists(X: np.ndarray, centers: np.ndarray) -> np.ndarray:
        """Матрица квадратов расстояний (n, k) без циклов."""
        return np.sum((X[:, None, :] - centers[None, :, :]) ** 2, axis=2)

    def _init_plusplus(self, X: np.ndarray, rng: np.random.Generator) -> np.ndarray:
        n = len(X)
        centers = np.empty((self.n_clusters, X.shape[1]), dtype=float)
        centers[0] = X[rng.integers(n)]
        closest = np.sum((X - centers[0]) ** 2, axis=1)
        for j in range(1, self.n_clusters):
            total = closest.sum()
            if total <= 0:                    # все точки совпали с центрами
                centers[j] = X[rng.integers(n)]
            else:
                centers[j] = X[rng.choice(n, p=closest / total)]
            closest = np.minimum(closest, np.sum((X - centers[j]) ** 2, axis=1))
        return centers

    def fit(self, X: np.ndarray) -> "KMeans":
        X = np.asarray(X, dtype=float)
        rng = np.random.default_rng(self.random_state)
        centers = self._init_plusplus(X, rng)

        labels = np.full(len(X), -1)
        for _ in range(self.max_iter):
            new_labels = np.argmin(self._sq_dists(X, centers), axis=1)
            if np.array_equal(new_labels, labels):
                break                          # приписывания не изменились — сошлись
            labels = new_labels
            for j in range(self.n_clusters):
                mask = labels == j
                if mask.any():
                    centers[j] = X[mask].mean(axis=0)
                # пустой кластер оставляем на месте: перезапуск усложнил бы пример

        dists = self._sq_dists(X, centers)
        self.centers_ = centers
        self.labels_ = np.argmin(dists, axis=1)
        self.inertia_ = float(np.sum(np.min(dists, axis=1)))
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.argmin(self._sq_dists(np.asarray(X, dtype=float), self.centers_), axis=1)


class KNNClassifier:
    def __init__(self, k: int = 5):
        self.k = k
        self.X_train: np.ndarray | None = None
        self.y_train: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "KNNClassifier":
        self.X_train = np.asarray(X, dtype=float)
        self.y_train = np.asarray(y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X, dtype=float)
        # ||a - b||^2 = ||a||^2 - 2 a·b + ||b||^2 — раскрытие скобок даёт
        # одно матричное умножение вместо двойного цикла
        dists = (
            np.sum(X ** 2, axis=1)[:, None]
            - 2.0 * (X @ self.X_train.T)
            + np.sum(self.X_train ** 2, axis=1)[None, :]
        )
        # argpartition дешевле полной сортировки: нам нужны k ближайших, а не их порядок
        neighbor_idx = np.argpartition(dists, kth=self.k - 1, axis=1)[:, : self.k]
        neighbor_labels = self.y_train[neighbor_idx]

        preds = np.empty(len(X), dtype=self.y_train.dtype)
        for i in range(len(X)):
            values, counts = np.unique(neighbor_labels[i], return_counts=True)
            preds[i] = values[np.argmax(counts)]
        return preds
