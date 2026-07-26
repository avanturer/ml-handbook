"""Внимание с нуля (numpy).

Задание: реализуйте функции так, чтобы прошли тесты из `code/tests/test_attention.py`.

Норматив по времени: softmax — 5 минут, scaled_dot_product_attention — 10 минут,
multi_head_attention — 20 минут. Это ровно та задача, которую дают на секции по DL.

Теория: docs/03-deep-learning/04-attention-and-transformer.md
"""

from __future__ import annotations

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Численно устойчивый softmax вдоль оси `axis`.

    Наивная формула exp(x) / sum(exp(x)) переполняется уже при x ~ 800.
    Приём: вычесть максимум по оси перед экспонентой — результат не меняется,
    потому что softmax инвариантен к сдвигу аргумента на константу.

    Отдельно продумайте случай, когда вся строка равна -inf (полностью
    замаскированная позиция): не должно получиться NaN.
    """
    raise NotImplementedError("Реализуйте softmax")


def scaled_dot_product_attention(
    q: np.ndarray,
    k: np.ndarray,
    v: np.ndarray,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V.

    Формы:
        q: (..., n_q, d_k)
        k: (..., n_k, d_k)
        v: (..., n_k, d_v)
        mask: (..., n_q, n_k) булев массив, True = ЗАПРЕЩЕНО смотреть

    Возвращает (output, attention_weights) с формами (..., n_q, d_v) и (..., n_q, n_k).

    Два обязательных момента:
      1. Делить на sqrt(d_k) — иначе при больших d_k softmax насыщается
         и градиент затухает (разбор — в главе про трансформер).
      2. Маскировать ЛОГИТЫ ДО softmax, а не веса после него. Если обнулить
         веса после softmax, они перестанут суммироваться в единицу.
    """
    raise NotImplementedError("Реализуйте scaled_dot_product_attention")


def causal_mask(n: int) -> np.ndarray:
    """Верхнетреугольная причинная маска (n, n): True там, куда смотреть нельзя.

    Позиция i имеет право видеть только позиции j <= i.
    """
    raise NotImplementedError("Реализуйте causal_mask")


def multi_head_attention(
    x: np.ndarray,
    w_q: np.ndarray,
    w_k: np.ndarray,
    w_v: np.ndarray,
    w_o: np.ndarray,
    n_heads: int,
    causal: bool = False,
) -> np.ndarray:
    """Многоголовое self-attention.

    Формы:
        x:   (B, n, d_model)
        w_q, w_k, w_v, w_o: (d_model, d_model)
        результат: (B, n, d_model)

    Порядок действий:
      1. Спроецировать x в q, k, v.
      2. Разрезать последнюю ось на головы: (B, n, d_model) -> (B, n, h, d_head)
         и переставить оси в (B, h, n, d_head).
      3. Применить scaled_dot_product_attention (с причинной маской, если causal).
      4. Склеить головы обратно и применить выходную проекцию w_o.

    Проверьте себя: при n_heads=1 результат обязан совпасть с одноголовым attention
    той же размерности — это первый тест, который стоит написать самому.
    """
    raise NotImplementedError("Реализуйте multi_head_attention")
