"""Тесты к code/exercises/attention.py.

Запуск:  pytest code/tests/test_attention.py -v
"""

from __future__ import annotations

import numpy as np
import pytest

from exercises.attention import (
    causal_mask,
    multi_head_attention,
    scaled_dot_product_attention,
    softmax,
)


def test_softmax_sums_to_one():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(4, 7, 11))
    p = softmax(x, axis=-1)
    assert np.allclose(p.sum(axis=-1), 1.0)
    assert np.all(p >= 0.0)


def test_softmax_is_stable_on_large_values():
    x = np.array([[1000.0, 1001.0, 1002.0]])
    p = softmax(x)
    assert np.all(np.isfinite(p))
    assert p.sum() == pytest.approx(1.0)
    # ответ не должен зависеть от сдвига аргумента на константу
    assert np.allclose(p, softmax(x - 1000.0))


def test_softmax_shift_invariance():
    rng = np.random.default_rng(1)
    x = rng.normal(size=(3, 5))
    assert np.allclose(softmax(x), softmax(x + 100.0))


def test_attention_shapes():
    rng = np.random.default_rng(2)
    q = rng.normal(size=(2, 6, 8))
    k = rng.normal(size=(2, 10, 8))
    v = rng.normal(size=(2, 10, 16))
    out, weights = scaled_dot_product_attention(q, k, v)
    assert out.shape == (2, 6, 16)
    assert weights.shape == (2, 6, 10)
    assert np.allclose(weights.sum(axis=-1), 1.0)


def test_attention_is_scaled_by_sqrt_dk():
    """Без деления на sqrt(d_k) веса при большом d_k выродятся в one-hot."""
    rng = np.random.default_rng(3)
    d_k = 256
    q = rng.normal(size=(1, 4, d_k))
    k = rng.normal(size=(1, 4, d_k))
    v = rng.normal(size=(1, 4, 4))
    _, weights = scaled_dot_product_attention(q, k, v)
    # при корректном масштабировании распределение остаётся не вырожденным
    assert weights.max() < 0.99


def test_attention_picks_matching_key():
    """Если запрос совпадает с одним из ключей, вес на нём должен доминировать."""
    k = np.array([[[10.0, 0.0], [0.0, 10.0]]])       # (1, 2, 2)
    v = np.array([[[1.0, 0.0], [0.0, 1.0]]])         # (1, 2, 2)
    q = np.array([[[10.0, 0.0]]])                    # (1, 1, 2) — совпадает с первым ключом
    out, weights = scaled_dot_product_attention(q, k, v)
    assert weights[0, 0, 0] > 0.99
    assert np.allclose(out[0, 0], [1.0, 0.0], atol=1e-2)


def test_causal_mask_shape_and_content():
    m = causal_mask(4)
    assert m.shape == (4, 4)
    assert m.dtype == bool
    assert not m[2, 0] and not m[2, 2]   # смотреть назад и на себя можно
    assert m[0, 1] and m[2, 3]           # смотреть вперёд нельзя


def test_causal_attention_ignores_future():
    rng = np.random.default_rng(4)
    n = 6
    q = rng.normal(size=(1, n, 8))
    k = rng.normal(size=(1, n, 8))
    v = rng.normal(size=(1, n, 8))
    _, weights = scaled_dot_product_attention(q, k, v, mask=causal_mask(n))
    upper = np.triu(np.ones((n, n), dtype=bool), k=1)
    assert np.allclose(weights[0][upper], 0.0)
    assert np.allclose(weights.sum(axis=-1), 1.0)


def _identity_weights(d: int) -> np.ndarray:
    return np.eye(d)


def test_mha_shapes():
    rng = np.random.default_rng(5)
    B, n, d, h = 2, 7, 16, 4
    x = rng.normal(size=(B, n, d))
    ws = [rng.normal(scale=0.1, size=(d, d)) for _ in range(4)]
    out = multi_head_attention(x, *ws, n_heads=h)
    assert out.shape == (B, n, d)


def test_mha_single_head_matches_plain_attention():
    rng = np.random.default_rng(6)
    B, n, d = 1, 5, 8
    x = rng.normal(size=(B, n, d))
    eye = _identity_weights(d)

    out_mha = multi_head_attention(x, eye, eye, eye, eye, n_heads=1)
    out_plain, _ = scaled_dot_product_attention(x, x, x)
    assert np.allclose(out_mha, out_plain, atol=1e-10)


def test_mha_causal_does_not_leak_future():
    """Изменение последнего токена не должно влиять на выходы предыдущих позиций."""
    rng = np.random.default_rng(7)
    B, n, d, h = 1, 6, 16, 4
    x = rng.normal(size=(B, n, d))
    ws = [rng.normal(scale=0.1, size=(d, d)) for _ in range(4)]

    out_a = multi_head_attention(x, *ws, n_heads=h, causal=True)
    x_modified = x.copy()
    x_modified[0, -1] += 100.0
    out_b = multi_head_attention(x_modified, *ws, n_heads=h, causal=True)

    assert np.allclose(out_a[0, :-1], out_b[0, :-1], atol=1e-8)


def test_mha_permutation_equivariance_without_causal():
    """Без маски и без позиционных кодировок attention эквивариантен к перестановке."""
    rng = np.random.default_rng(8)
    B, n, d, h = 1, 5, 16, 2
    x = rng.normal(size=(B, n, d))
    ws = [rng.normal(scale=0.1, size=(d, d)) for _ in range(4)]
    perm = np.array([2, 0, 4, 1, 3])

    out = multi_head_attention(x, *ws, n_heads=h)
    out_perm = multi_head_attention(x[:, perm], *ws, n_heads=h)
    assert np.allclose(out[:, perm], out_perm, atol=1e-10)
