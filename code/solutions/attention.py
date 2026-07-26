"""Эталонная реализация внимания на numpy.

Открывайте только после собственной попытки.
"""

from __future__ import annotations

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x_max = np.max(x, axis=axis, keepdims=True)
    # если вся строка -inf (полностью замаскированная позиция), максимум тоже -inf;
    # заменяем его на 0, иначе получим -inf - (-inf) = nan
    x_max = np.where(np.isfinite(x_max), x_max, 0.0)
    exps = np.exp(x - x_max)
    denom = np.sum(exps, axis=axis, keepdims=True)
    safe_denom = np.where(denom > 0, denom, 1.0)
    return np.where(denom > 0, exps / safe_denom, 0.0)


def scaled_dot_product_attention(
    q: np.ndarray,
    k: np.ndarray,
    v: np.ndarray,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    q = np.asarray(q, dtype=float)
    k = np.asarray(k, dtype=float)
    v = np.asarray(v, dtype=float)

    d_k = q.shape[-1]
    # деление на sqrt(d_k) удерживает дисперсию логитов около единицы:
    # Var(q·k) = d_k при независимых компонентах с единичной дисперсией
    scores = np.matmul(q, np.swapaxes(k, -1, -2)) / np.sqrt(d_k)

    if mask is not None:
        # маскируем ЛОГИТЫ до softmax: обнуление весов после него сломало бы нормировку
        scores = np.where(mask, -np.inf, scores)

    weights = softmax(scores, axis=-1)
    return np.matmul(weights, v), weights


def causal_mask(n: int) -> np.ndarray:
    return np.triu(np.ones((n, n), dtype=bool), k=1)


def multi_head_attention(
    x: np.ndarray,
    w_q: np.ndarray,
    w_k: np.ndarray,
    w_v: np.ndarray,
    w_o: np.ndarray,
    n_heads: int,
    causal: bool = False,
) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    batch, n, d_model = x.shape
    if d_model % n_heads != 0:
        raise ValueError("d_model должно делиться на число голов")
    d_head = d_model // n_heads

    def to_heads(t: np.ndarray) -> np.ndarray:
        # (B, n, d_model) -> (B, n, h, d_head) -> (B, h, n, d_head)
        return t.reshape(batch, n, n_heads, d_head).transpose(0, 2, 1, 3)

    q = to_heads(x @ w_q)
    k = to_heads(x @ w_k)
    v = to_heads(x @ w_v)

    mask = causal_mask(n) if causal else None
    out, _ = scaled_dot_product_attention(q, k, v, mask)

    # обратно: (B, h, n, d_head) -> (B, n, h, d_head) -> (B, n, d_model)
    out = out.transpose(0, 2, 1, 3).reshape(batch, n, d_model)
    return out @ w_o
