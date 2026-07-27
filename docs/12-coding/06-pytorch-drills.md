# PyTorch: тренировка

> **Зачем эта глава.** На секции живого кодинга по DL просят не «объяснить трансформер»,
> а написать слой, собрать батч из последовательностей разной длины, починить NaN в лоссе
> или сказать, влезет ли модель в 24 ГБ. Здесь 13 задач ровно такого формата — с полными
> решениями, разбором «почему именно так» и той ошибкой, ради которой задачу дают.
> После главы вы сможете писать боевой обучающий цикл по памяти и диагностировать чужой.

**Уровень:** 🎯 middle → 🧠 middle+
**Предварительно нужно:** [PyTorch на практике](../03-deep-learning/05-pytorch-in-practice.md),
[Внимание и трансформер](../03-deep-learning/04-attention-and-transformer.md),
[Масштабирование обучения](../03-deep-learning/06-scaling-and-efficiency.md)
**Как проработать:** сначала решить самому, потом сверяться и запускать

> **О версиях.** Код написан под **PyTorch 2.4+** и Python 3.11. Где API менялся
> (`torch.cuda.amp` → `torch.amp`, `weights_only` в `torch.load`), это отмечено явно.
> Весь код запускается на CPU; блоки, требующие GPU, помечены и написаны так,
> чтобы деградировать на CPU без падения.

---

## Карта главы

- [1. Как устроена секция и общий скелет](#1-как-устроена-секция-и-общий-скелет)
- [2. Задача 1. Свой слой: RMSNorm](#2-задача-1-свой-слой-rmsnorm)
- [3. Задача 2. Dataset и collate_fn для переменной длины](#3-задача-2-dataset-и-collate_fn-для-переменной-длины)
- [4. Задача 3. Своя функция потерь: focal loss](#4-задача-3-своя-функция-потерь-focal-loss)
- [5. Задача 4. Attention с нуля](#5-задача-4-attention-с-нуля)
- [6. Задача 5. Сколько параметров и сколько памяти](#6-задача-5-сколько-параметров-и-сколько-памяти)
- [7. Задача 6. Отладить NaN в лоссе](#7-задача-6-отладить-nan-в-лоссе)
- [8. Задача 7. Найти утечку памяти](#8-задача-7-найти-утечку-памяти)
- [9. Задача 8. Ускорить обучающий цикл](#9-задача-8-ускорить-обучающий-цикл)
- [10. Задача 9. Градиентное накопление](#10-задача-9-градиентное-накопление)
- [11. Задача 10. Mixed precision](#11-задача-10-mixed-precision)
- [12. Задача 11. Воспроизводимость](#12-задача-11-воспроизводимость)
- [13. Задача 12. Early stopping и лучший чекпоинт](#13-задача-12-early-stopping-и-лучший-чекпоинт)
- [14. Задача 13. Собрать всё вместе](#14-задача-13-собрать-всё-вместе)
- [15. Подводные камни](#15-подводные-камни)
- [16. Проверь себя](#16-проверь-себя)
- [17. Практика](#17-практика)
- [18. Что читать дальше](#18-что-читать-дальше)

---

## 1. Как устроена секция и общий скелет

PyTorch-секция бывает двух форматов. **Первый**: «напишите X» — слой, лосс, коллатор,
attention. Проверяется, что вы пишете код руками, а не собираете из готовых кубиков.
**Второй**, и он опаснее: «вот код, он не работает / работает медленно / жрёт память —
почините». Проверяется опыт, который нельзя вычитать.

Что оценивают:

| Что оценивают | Как видно | Вес |
|---|---|---|
| **Понимание форм тензоров** | вы проговариваете `(B, L, D)` на каждом шаге | очень высокий |
| **Работа с autograd** | понимаете, где рвётся граф, что держит память, зачем `detach` | очень высокий |
| **Численная устойчивость** | пишете `binary_cross_entropy_with_logits`, а не `log(sigmoid(x))` | высокий |
| **Диагностика** | у вас есть протокол, а не «попробую уменьшить lr» | высокий |
| **Знание API** | помните сигнатуры `pad_sequence`, `GradScaler`, `clip_grad_norm_` | средний |
| **Производительность** | знаете, что `.item()` синхронизирует, а `num_workers=0` — узкое место | средний |

Скелет обучающего цикла, от которого мы будем отталкиваться. Держите его в мышечной памяти:

```python
model.train()
for batch in loader:
    batch = {k: v.to(device, non_blocking=True) for k, v in batch.items()}
    optimizer.zero_grad(set_to_none=True)   # обнулить ДО backward
    logits = model(batch["x"])
    loss = criterion(logits, batch["y"])
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()
    scheduler.step()                        # после optimizer.step(), не до
```

Пять строк, в каждой из которых есть чем ошибиться. Дальше — по задачам.

> 💬 **На собеседовании.** Спросят: «Что будет, если забыть `optimizer.zero_grad()`?»
> Хороший ответ: градиенты в `.grad` **накапливаются** между вызовами `backward()` — это
> сознательное решение авторов PyTorch, на котором построено градиентное накопление и
> обучение с несколькими лоссами. Без обнуления шаг оптимизатора будет делаться по сумме
> градиентов всех предыдущих батчей: направление превратится в мусор, эффективный learning
> rate вырастет линейно с числом шагов, обучение разойдётся или встанет. Симптом — лосс
> ведёт себя нормально первые десятки шагов и потом взрывается. Плохой ответ:
> «будет ошибка» — ошибки не будет, в этом и подвох.

---

## 2. Задача 1. Свой слой: RMSNorm

**Постановка.** Реализуйте `RMSNorm` — нормализацию, используемую в LLaMA и большинстве
современных LLM вместо `LayerNorm`. Формула:

$$
\mathrm{RMSNorm}(x)_j = \frac{x_j}{\sqrt{\frac{1}{d}\sum_{k=1}^{d} x_k^2 + \varepsilon}} \cdot g_j
$$

где $x \in \mathbb{R}^{d}$ — вектор признаков одного токена (последняя ось тензора),
$d$ — размерность этой оси, $x_j$ и $x_k$ — её компоненты, $g \in \mathbb{R}^{d}$ —
обучаемый вектор масштабов (по одному числу на канал), $\varepsilon > 0$ — малая константа
против деления на ноль, $j$ — индекс выходной компоненты.

От `LayerNorm` отличается тем, что **не вычитает среднее** и не имеет сдвига `bias`:
считается только среднеквадратичное значение. Это дешевле и на практике не хуже.

Требования: слой работает с тензорами любой формы `(..., d)`, параметры регистрируются
корректно, слой устойчив под `autocast`.

**Решение.**

```python
import torch
import torch.nn as nn


class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization (Zhang & Sennrich, 2019)."""

    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()          # ОБЯЗАТЕЛЬНО до присваивания параметров:
                                    # __setattr__ nn.Module ищет self._parameters, который
                                    # создаётся именно в super().__init__()
        self.eps = eps
        # Старт из единиц: слой на инициализации не искажает сигнал, только нормирует.
        # nn.Parameter автоматически попадает в model.parameters() и переезжает при .to(device)
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Считаем статистику в fp32: под autocast x приходит в fp16, где x**2 для значений
        # больше ~256 переполняется в inf, и вся нормализация даёт NaN. Это не паранойя,
        # а самая частая причина NaN в fp16-обучении трансформеров.
        in_dtype = x.dtype
        x_f32 = x.float()
        # rsqrt быстрее, чем 1/sqrt, и даёт на одну операцию меньше
        inv_rms = torch.rsqrt(x_f32.pow(2).mean(dim=-1, keepdim=True) + self.eps)
        normed = (x_f32 * inv_rms).to(in_dtype)
        return normed * self.weight

    def extra_repr(self) -> str:
        # Чтобы print(model) показывал размерность — мелочь, экономящая часы отладки
        return f"dim={self.weight.numel()}, eps={self.eps}"
```

**Проверка — обязательная часть ответа.** Не заявляйте, что слой готов, пока не показали тест:

```python
def test_rmsnorm():
    torch.manual_seed(0)
    layer = RMSNorm(8)
    x = torch.randn(2, 5, 8)                    # (B=2, L=5, D=8)

    out = layer(x)
    assert out.shape == x.shape, "форма должна сохраняться"

    # Эталон «в лоб» по определению — считаем независимо от реализации
    rms = x.pow(2).mean(dim=-1, keepdim=True).add(1e-6).sqrt()
    expected = x / rms * layer.weight
    assert torch.allclose(out, expected, atol=1e-5)

    # RMS выхода при weight=1 должен быть ≈ 1
    assert torch.allclose(out.pow(2).mean(-1).sqrt(), torch.ones(2, 5), atol=1e-3)

    # Параметр действительно зарегистрирован и получает градиент
    names = [n for n, _ in layer.named_parameters()]
    assert names == ["weight"], names
    out.sum().backward()
    assert layer.weight.grad is not None and torch.isfinite(layer.weight.grad).all()

    # Инвариантность к масштабу входа: RMSNorm(2x) == RMSNorm(x)
    assert torch.allclose(layer(x * 2.0), out, atol=1e-4)


test_rmsnorm()
```

**Объяснение.** Три вещи, которые проверяет эта задача.

**Регистрация параметров.** `nn.Parameter` — это `Tensor` с `requires_grad=True`, который
`nn.Module.__setattr__` перехватывает и кладёт в `self._parameters`. Отсюда следует всё
остальное: параметр попадает в `model.parameters()` (значит, его увидит оптимизатор),
в `state_dict()` (значит, он сохранится в чекпоинт) и переезжает на устройство при `.to(cuda)`.
Обычный тензор, присвоенный в `__init__`, ничего этого не делает.

**Параметр против буфера.** Если тензор нужен слою, но не обучается (маска, таблица частот,
позиционные коэффициенты RoPE), его регистрируют как **буфер**:

```python
self.register_buffer("causal_mask", torch.tril(torch.ones(L, L, dtype=torch.bool)))
self.register_buffer("running_mean", torch.zeros(dim))            # попадёт в state_dict
self.register_buffer("cos_cache", cos, persistent=False)          # НЕ попадёт в state_dict
```

Буфер переезжает вместе с моделью на GPU и (по умолчанию) сохраняется в чекпоинт,
но не получает градиентов и не виден оптимизатору. `persistent=False` — для вычислимых
кэшей, которые незачем таскать в файле весов.

**Вычисление в fp32.** Комментарий в коде не для красоты: `x.pow(2)` в fp16 переполняется
при `|x| > 256` (максимум fp16 около 65504), а активации в глубоких сетях легко доходят
до сотен. Штатные `nn.LayerNorm` и `nn.RMSNorm` внутри делают то же самое — поднимают
точность на время расчёта статистики.

> ⚠️ **Типичная ошибка.** Собрать подмодули в обычный список Python:
> ```python
> self.layers = [nn.Linear(d, d) for _ in range(6)]   # НЕВЕРНО
> ```
> Такие модули не попадут в `parameters()`, оптимизатор их не увидит, `.to(device)`
> их не перенесёт, `state_dict()` не сохранит. Модель будет обучаться, лосс будет падать
> (за счёт остальных слоёв) — и вы месяц не заметите. Правильно: `nn.ModuleList([...])`
> для списка, `nn.ModuleDict({...})` для словаря, `nn.Sequential(...)` для цепочки.
> То же самое для тензоров: список тензоров — `nn.ParameterList`.

**Родственные задачи на ту же тему**, которые встречаются вместо RMSNorm: SwiGLU-блок
FFN, LayerScale, Squeeze-and-Excitation, gated residual. Механика одна и та же.

---

## 3. Задача 2. Dataset и collate_fn для переменной длины

**Постановка.** Есть корпус текстов, уже токенизированных в списки id разной длины,
и метки классов. Напишите `Dataset` и `collate_fn`, которые собирают батч: паддинг
до максимума **в батче** (не в датасете), маска валидных позиций, метки. Дальше —
корректный masked mean pooling поверх выходов энкодера.

**Решение.**

```python
from dataclasses import dataclass
import torch
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence

PAD_ID = 0


class TokenizedTextDataset(Dataset):
    """Хранит уже токенизированные последовательности. Тяжёлую токенизацию делаем
    один раз заранее, а не в __getitem__: иначе она повторится на каждой эпохе."""

    def __init__(self, sequences: list[list[int]], labels: list[int], max_len: int = 512):
        assert len(sequences) == len(labels)
        self.sequences = sequences
        self.labels = labels
        self.max_len = max_len

    def __len__(self) -> int:
        return len(self.sequences)

    def __getitem__(self, idx: int) -> dict:
        # Обрезаем здесь, а не в collate: длина одного примера не должна зависеть от батча
        ids = self.sequences[idx][: self.max_len]
        return {
            # Тензоры создаём в __getitem__, чтобы работал pin_memory и передача в воркеры
            "ids": torch.tensor(ids, dtype=torch.long),
            "label": torch.tensor(self.labels[idx], dtype=torch.long),
        }


def collate_batch(batch: list[dict], pad_id: int = PAD_ID) -> dict:
    """Собирает список примеров разной длины в прямоугольный батч.

    Возвращает:
        ids     (B, L_max) — паддинг справа
        mask    (B, L_max) — True на валидных токенах
        lengths (B,)       — реальные длины, нужны для pack_padded_sequence и для метрик
        labels  (B,)
    """
    lengths = torch.tensor([len(item["ids"]) for item in batch], dtype=torch.long)
    ids = pad_sequence(
        [item["ids"] for item in batch],
        batch_first=True,          # (B, L), а не (L, B): почти везде удобнее
        padding_value=pad_id,
    )
    # Маска через сравнение с arange — векторно, без цикла по батчу
    max_len = ids.size(1)
    mask = torch.arange(max_len)[None, :] < lengths[:, None]   # (B, L_max), bool
    labels = torch.stack([item["label"] for item in batch])
    return {"ids": ids, "mask": mask, "lengths": lengths, "labels": labels}


def masked_mean_pool(hidden: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    """Среднее по времени с учётом паддинга.

    hidden: (B, L, D), mask: (B, L) bool -> (B, D)
    """
    m = mask.unsqueeze(-1).to(hidden.dtype)             # (B, L, 1)
    summed = (hidden * m).sum(dim=1)                    # (B, D) — паддинг занулён
    # clamp(min=1): защита от деления на ноль, если вдруг пришла пустая последовательность
    denom = m.sum(dim=1).clamp(min=1.0)                 # (B, 1)
    return summed / denom
```

Проверка:

```python
def test_collate():
    ds = TokenizedTextDataset([[5, 6, 7], [8], [9, 10]], [0, 1, 0])
    batch = collate_batch([ds[0], ds[1], ds[2]])

    assert batch["ids"].shape == (3, 3)
    assert batch["ids"][1].tolist() == [8, PAD_ID, PAD_ID]
    assert batch["mask"][1].tolist() == [True, False, False]
    assert batch["lengths"].tolist() == [3, 1, 2]

    # Ключевая проверка: паддинг не влияет на пулинг
    hidden = torch.randn(3, 3, 4)
    pooled = masked_mean_pool(hidden, batch["mask"])
    # для второго примера пулинг должен равняться первому вектору
    assert torch.allclose(pooled[1], hidden[1, 0], atol=1e-6)


test_collate()

loader = DataLoader(
    TokenizedTextDataset([[1, 2], [3], [4, 5, 6]] * 100, [0, 1, 0] * 100),
    batch_size=8,
    shuffle=True,
    collate_fn=collate_batch,   # без этого DataLoader попытается сложить тензоры разной длины
    num_workers=2,
    pin_memory=True,
    drop_last=True,             # последний неполный батч часто ломает BatchNorm и метрики
)
```

**Объяснение.**

**Зачем вообще `collate_fn`.** Дефолтный коллатор пытается сделать `torch.stack` по списку
тензоров — и падает с `RuntimeError: stack expects each tensor to be equal size`, как только
длины разные. `collate_fn` — точка, где вы решаете, как приводить примеры к общей форме.

**Паддинг до максимума в батче, а не в датасете.** Если паддить всё до 512, вы будете считать
attention по 512 позициям даже там, где реальных токенов 20 — а сложность attention
квадратична по длине. При сортировке по длине разница в скорости достигает 3–5 раз.

**Маска обязательна.** Без неё паддинг участвует в вычислениях: mean pooling разделит сумму
на `L_max` вместо реальной длины, attention будет смотреть на `<pad>`, а BatchNorm посчитает
статистику по мусору. Маска — не «хорошая практика», а условие корректности.

**Bucketing: батчи из похожих по длине примеров.** Следующий уровень оптимизации — не просто
паддить до максимума в батче, а формировать батчи так, чтобы максимум был маленьким:

```python
from torch.utils.data import Sampler
import random


class LengthBucketSampler(Sampler[list[int]]):
    """Группирует индексы по близкой длине, чтобы паддинга было меньше.
    Сохраняет случайность: перемешивает и внутри бакета, и порядок самих батчей."""

    def __init__(self, lengths: list[int], batch_size: int, bucket_mult: int = 50, seed: int = 0):
        self.lengths = lengths
        self.batch_size = batch_size
        self.pool_size = batch_size * bucket_mult   # окно, внутри которого сортируем
        self.rng = random.Random(seed)

    def __iter__(self):
        idx = list(range(len(self.lengths)))
        self.rng.shuffle(idx)                       # без этого порядок эпох будет одинаков
        batches = []
        for start in range(0, len(idx), self.pool_size):
            pool = sorted(idx[start:start + self.pool_size], key=lambda i: self.lengths[i])
            batches += [pool[i:i + self.batch_size] for i in range(0, len(pool), self.batch_size)]
        self.rng.shuffle(batches)                   # иначе все короткие батчи идут подряд
        return iter(batches)

    def __len__(self):
        return (len(self.lengths) + self.batch_size - 1) // self.batch_size


# использование: batch_sampler исключает batch_size/shuffle/drop_last
# loader = DataLoader(ds, batch_sampler=LengthBucketSampler(lens, 32), collate_fn=collate_batch)
```

Важная деталь: перемешивать нужно **дважды** — внутри пула и сам порядок батчей. Если этого
не сделать, батчи будут приходить по возрастанию длины, и градиентные шаги окажутся
скоррелированы с длиной текста, что заметно портит обучение.

> 💬 **На собеседовании.** Спросят: «Как обучать на последовательностях разной длины?»
> Хороший ответ: паддинг до максимума **внутри батча** плюс маска, которая пробрасывается
> во все операции, где паддинг может испортить результат (attention, пулинг, лосс);
> дополнительно — bucketing по длине, чтобы сократить долю паддинга, и `drop_last`
> для стабильности. Для RNN — `pack_padded_sequence`, который вообще не считает паддинг.
> Стоит упомянуть, что в лоссе паддинг убирается через `ignore_index` в
> `nn.CrossEntropyLoss(ignore_index=PAD_ID)`. Плохой ответ: «дополню нулями до 512» —
> дальше следует вопрос «а что будет с mean pooling?», и разговор заканчивается.

---

## 4. Задача 3. Своя функция потерь: focal loss

**Постановка.** Реализуйте binary focal loss для сильно несбалансированной задачи.
Формула из статьи Lin et al. «Focal Loss for Dense Object Detection» (2017):

$$
\mathrm{FL}(p_t) = -\alpha_t \,(1 - p_t)^{\gamma}\,\log(p_t)
$$

где $p_t$ — предсказанная вероятность **правильного** класса: $p_t = p$ при $y = 1$
и $p_t = 1 - p$ при $y = 0$, где $p = \sigma(z)$ — сигмоида от логита $z$, а $y \in \{0, 1\}$ —
метка; $\gamma \ge 0$ — параметр фокусировки (при $\gamma = 0$ формула вырождается
во взвешенную бинарную кросс-энтропию); $\alpha_t \in (0,1)$ — вес класса: $\alpha$ при
$y = 1$ и $1 - \alpha$ при $y = 0$.

Смысл множителя $(1 - p_t)^{\gamma}$: для примеров, которые модель уже уверенно угадала
($p_t \to 1$), он стремится к нулю и почти обнуляет их вклад в градиент. Обучение
концентрируется на трудных примерах. При дисбалансе 1:1000 подавляющее большинство лёгких
негативов перестаёт заглушать сигнал от редкого позитивного класса.

Требование: реализация должна быть **численно устойчивой** и работать под `autocast`.

**Решение.**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class BinaryFocalLoss(nn.Module):
    def __init__(self, alpha: float = 0.25, gamma: float = 2.0, reduction: str = "mean"):
        super().__init__()
        if reduction not in {"none", "mean", "sum"}:
            raise ValueError(f"unknown reduction: {reduction}")
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """logits: (N,) сырые логиты ДО сигмоиды. targets: (N,) значения 0.0/1.0."""
        targets = targets.to(logits.dtype)

        # -log(p_t) считаем через встроенную функцию: внутри log-sum-exp, поэтому
        # при |logit| = 30 нет ни log(0) = -inf, ни переполнения exp
        ce = F.binary_cross_entropy_with_logits(logits, targets, reduction="none")

        # p_t = p при y=1 и (1-p) при y=0. Эквивалентно exp(-ce), но так читаемее
        p = torch.sigmoid(logits)
        p_t = p * targets + (1.0 - p) * (1.0 - targets)

        # Модулирующий множитель. clamp защищает от (0)**gamma при дробном gamma
        focal_term = (1.0 - p_t).clamp(min=1e-8).pow(self.gamma)

        alpha_t = self.alpha * targets + (1.0 - self.alpha) * (1.0 - targets)

        loss = alpha_t * focal_term * ce

        if self.reduction == "mean":
            return loss.mean()
        if self.reduction == "sum":
            return loss.sum()
        return loss
```

Проверка — три независимых свойства:

```python
def test_focal_loss():
    torch.manual_seed(0)
    logits = torch.randn(1000)
    targets = (torch.rand(1000) > 0.5).float()

    # 1. gamma=0, alpha=0.5 -> ровно половина обычной BCE
    fl = BinaryFocalLoss(alpha=0.5, gamma=0.0, reduction="mean")
    bce = F.binary_cross_entropy_with_logits(logits, targets, reduction="mean")
    assert torch.allclose(fl(logits, targets), 0.5 * bce, atol=1e-6)

    # 2. Устойчивость на экстремальных логитах: наивная реализация здесь даёт inf/NaN
    extreme = torch.tensor([-50.0, 50.0, 0.0])
    y = torch.tensor([1.0, 0.0, 1.0])
    out = BinaryFocalLoss(reduction="none")(extreme, y)
    assert torch.isfinite(out).all(), out

    # 3. Фокусировка работает: лёгкий пример весит на порядки меньше трудного
    easy = BinaryFocalLoss(reduction="none")(torch.tensor([6.0]), torch.tensor([1.0]))
    hard = BinaryFocalLoss(reduction="none")(torch.tensor([0.0]), torch.tensor([1.0]))
    assert hard.item() > 100 * easy.item(), (hard.item(), easy.item())

    # 4. Градиент существует и конечен
    z = torch.randn(64, requires_grad=True)
    BinaryFocalLoss()(z, (torch.rand(64) > 0.5).float()).backward()
    assert torch.isfinite(z.grad).all()


test_focal_loss()
```

**Объяснение.**

**Почему логиты, а не вероятности.** Наивная реализация

```python
p = torch.sigmoid(logits)
loss = -alpha * (1 - p) ** gamma * torch.log(p)      # НЕУСТОЙЧИВО
```

даёт `log(0) = -inf` при `logits < -20` (сигмоида уходит в машинный ноль), а под fp16 —
уже при `logits < -12`. `binary_cross_entropy_with_logits` внутри использует тождество
$\log \sigma(z) = -\log(1 + e^{-z})$ с переносом знака (log-sum-exp trick) и остаётся конечной
при любых входах. Правило шире, чем focal loss: **любой лосс принимает логиты**.
Отсюда же `nn.CrossEntropyLoss` (сама делает log_softmax), а не `nn.NLLLoss(torch.log(softmax(x)))`.

**Почему `reduction="none"` внутри.** Мы должны умножить на веса **поэлементно** до усреднения.
Если сначала усреднить, домножать будет уже нечего.

**Про подбор $\alpha$ и $\gamma$.** В исходной статье лучшие значения — $\gamma = 2$,
$\alpha = 0.25$; для табличных задач с дисбалансом 1:100 и хуже обычно перебирают
$\gamma \in \{1, 2, 3\}$. Важно понимать, что $\alpha$ и $\gamma$ работают в **разные** стороны:
$\alpha$ поднимает вес редкого класса, а $\gamma$ давит лёгкие примеры, которых в редком классе
как раз мало, — поэтому при росте $\gamma$ оптимальная $\alpha$ обычно **снижается**.

**Что focal loss ломает.** Он смещает предсказанные вероятности: модель, обученная
с focal loss, плохо калибрована, и её выход нельзя интерпретировать как вероятность
без последующей калибровки. Если по вероятности принимается бизнес-решение (ожидаемая выручка,
порог по стоимости ошибки) — это существенно. См.
[дисбаланс и калибровка](../02-classic-ml/12-imbalance-and-calibration.md).

> ⚠️ **Типичная ошибка.** Подать в свой лосс уже прошедшие через сигмоиду вероятности,
> потому что «так понятнее». Обучение стартует нормально, а на 3-й эпохе, когда модель
> становится уверенной, лосс превращается в `inf` и следом в `NaN`. Диагностический признак:
> NaN появляется **не сразу**, а после того, как лосс заметно упал.

---

## 5. Задача 4. Attention с нуля

**Постановка.** Реализуйте scaled dot-product attention и multi-head attention без
использования `nn.MultiheadAttention` и `F.scaled_dot_product_attention`. Поддержите
causal-маску и маску паддинга. Сверьте результат со штатной реализацией.

**Формула.**

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}} + M\right)V
$$

где $Q \in \mathbb{R}^{L_q \times d_k}$ — матрица запросов (по строке на позицию),
$K \in \mathbb{R}^{L_k \times d_k}$ — матрица ключей, $V \in \mathbb{R}^{L_k \times d_v}$ —
матрица значений, $L_q$ и $L_k$ — длины последовательностей запросов и ключей,
$d_k$ — размерность головы для запросов/ключей, $d_v$ — для значений (обычно $d_v = d_k$),
$M \in \mathbb{R}^{L_q \times L_k}$ — аддитивная маска ($0$ там, где смотреть можно,
и $-\infty$ там, где нельзя), softmax применяется построчно.

**Про делитель $\sqrt{d_k}$.** Пусть компоненты $q$ и $k$ независимы, с нулевым средним
и единичной дисперсией. Тогда скалярное произведение $q^\top k = \sum_{i=1}^{d_k} q_i k_i$
имеет дисперсию $d_k$ (сумма $d_k$ независимых слагаемых с дисперсией 1) и стандартное
отклонение $\sqrt{d_k}$. При $d_k = 64$ это разброс порядка $\pm 8$ — softmax от таких
значений почти one-hot, градиент по всем позициям, кроме максимальной, экспоненциально мал.
Деление на $\sqrt{d_k}$ возвращает дисперсию к единице.

**Решение.**

```python
import math
import torch
import torch.nn as nn
import torch.nn.functional as F


def scaled_dot_product(
    q: torch.Tensor,           # (B, H, Lq, Dh)
    k: torch.Tensor,           # (B, H, Lk, Dh)
    v: torch.Tensor,           # (B, H, Lk, Dh)
    attn_mask: torch.Tensor | None = None,   # bool (..., Lq, Lk): True = смотреть можно
    dropout_p: float = 0.0,
    training: bool = True,
) -> tuple[torch.Tensor, torch.Tensor]:
    d_k = q.size(-1)
    # (B,H,Lq,Dh) @ (B,H,Dh,Lk) -> (B,H,Lq,Lk). Батчевый matmul по первым двум осям
    scores = q @ k.transpose(-2, -1) / math.sqrt(d_k)

    if attn_mask is not None:
        # Заполняем НЕ -inf, а минимальным конечным числом для этого dtype.
        # Причина: если какая-то строка замаскирована целиком (пустая последовательность
        # или паддинг-запрос), softmax от строки из -inf даёт NaN. С finfo.min получится
        # равномерное распределение — мусор, но не NaN, который убьёт всю модель.
        neg_inf = torch.finfo(scores.dtype).min
        scores = scores.masked_fill(~attn_mask, neg_inf)

    attn = scores.softmax(dim=-1)
    if dropout_p > 0.0:
        attn = F.dropout(attn, p=dropout_p, training=training)
    out = attn @ v                                     # (B,H,Lq,Dh)
    return out, attn


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, n_heads: int, dropout: float = 0.0, bias: bool = False):
        super().__init__()
        if d_model % n_heads != 0:
            raise ValueError(f"d_model={d_model} не делится на n_heads={n_heads}")
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.dropout = dropout

        # Одна матрица на Q, K, V вместо трёх: один GEMM вместо трёх — заметно быстрее
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=bias)
        self.proj = nn.Linear(d_model, d_model, bias=bias)

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        """(B, L, D) -> (B, H, L, Dh)"""
        b, l, _ = x.shape
        # view разбивает последнюю ось на (H, Dh); transpose выносит H вперёд,
        # чтобы matmul работал батчево по (B, H)
        return x.view(b, l, self.n_heads, self.d_head).transpose(1, 2)

    def _merge_heads(self, x: torch.Tensor) -> torch.Tensor:
        """(B, H, L, Dh) -> (B, L, D)"""
        b, h, l, dh = x.shape
        # contiguous обязателен: после transpose тензор не непрерывен, и view упадёт
        return x.transpose(1, 2).contiguous().view(b, l, h * dh)

    def forward(
        self,
        x: torch.Tensor,                          # (B, L, D)
        key_padding_mask: torch.Tensor | None = None,   # (B, L) bool: True = реальный токен
        is_causal: bool = False,
        need_weights: bool = False,
    ):
        b, l, _ = x.shape
        qkv = self.qkv(x)                                       # (B, L, 3D)
        q, k, v = qkv.chunk(3, dim=-1)                          # три (B, L, D)
        q, k, v = self._split_heads(q), self._split_heads(k), self._split_heads(v)

        mask = None
        if key_padding_mask is not None:
            # (B, L) -> (B, 1, 1, L): broadcast по головам и по позициям запроса
            mask = key_padding_mask[:, None, None, :]
        if is_causal:
            causal = torch.ones(l, l, dtype=torch.bool, device=x.device).tril()
            causal = causal[None, None, :, :]                   # (1, 1, L, L)
            mask = causal if mask is None else (mask & causal)

        out, attn = scaled_dot_product(q, k, v, mask, self.dropout, self.training)
        out = self.proj(self._merge_heads(out))                 # (B, L, D)
        return (out, attn) if need_weights else out
```

**Сверка со штатной реализацией — обязательный шаг:**

```python
def test_mha_matches_sdpa():
    torch.manual_seed(0)
    b, l, d, h = 2, 7, 32, 4
    mha = MultiHeadAttention(d, h, dropout=0.0).eval()
    x = torch.randn(b, l, d)

    # Наш forward
    ours = mha(x, is_causal=True)

    # Эталон: та же проекция, но attention считает torch
    qkv = mha.qkv(x).chunk(3, dim=-1)
    q, k, v = (t.view(b, l, h, d // h).transpose(1, 2) for t in qkv)
    ref = F.scaled_dot_product_attention(q, k, v, is_causal=True)
    ref = mha.proj(ref.transpose(1, 2).contiguous().view(b, l, d))

    assert torch.allclose(ours, ref, atol=1e-5), (ours - ref).abs().max()


def test_causal_no_leak():
    """Проверка каузальности «от противного»: изменение будущего токена не должно
    менять выход в прошлых позициях. Это ловит перепутанный tril/triu — самую
    частую ошибку в реализации маски."""
    torch.manual_seed(0)
    mha = MultiHeadAttention(16, 2).eval()
    x = torch.randn(1, 6, 16)
    y1 = mha(x, is_causal=True)

    x2 = x.clone()
    x2[0, -1] += 10.0                       # меняем ТОЛЬКО последний токен
    y2 = mha(x2, is_causal=True)

    assert torch.allclose(y1[0, :-1], y2[0, :-1], atol=1e-6), "утечка из будущего!"


test_mha_matches_sdpa()
test_causal_no_leak()
```

**Объяснение.**

**Проход по размерностям** — то, что просят проговорить вслух:

| Шаг | Форма | Комментарий |
|---|---|---|
| вход `x` | `(B, L, D)` | B — батч, L — длина, D — `d_model` |
| `qkv(x)` | `(B, L, 3D)` | одна линейная проекция |
| после `chunk` | 3 × `(B, L, D)` | |
| после `_split_heads` | `(B, H, L, Dh)` | `Dh = D / H` |
| `q @ k^T` | `(B, H, L, L)` | **квадрат по длине** — здесь и живёт O(L²) память |
| после `softmax @ v` | `(B, H, L, Dh)` | |
| после `_merge_heads` | `(B, L, D)` | |
| после `proj` | `(B, L, D)` | форма входа восстановлена |

Заметьте: общее число параметров MHA не зависит от числа голов — это `4·D²` (три проекции
в `qkv` плюс выходная). Головы «нарезают» одну и ту же размерность, а не добавляют её.

**Почему `contiguous()` перед `view`.** `transpose` не двигает данные в памяти, а меняет
только шаги (strides). `view` требует непрерывного размещения и падает с
`RuntimeError: view size is not compatible with input tensor's size and stride`.
Альтернатива без явного `contiguous` — `reshape`, который сам сделает копию при необходимости.

**Про маски — два разных типа.** В PyTorch путаница с масками — источник половины багов:

- **Булева маска**: `True` может означать «смотреть **можно**» (как у нас и как в
  `F.scaled_dot_product_attention`) или «позицию **надо скрыть**» (как `attn_mask`
  в `nn.MultiheadAttention` и как `src_key_padding_mask` в `nn.Transformer`).
  Соглашения противоположны — читайте документацию каждый раз.
- **Аддитивная маска** типа float: прибавляется к скорам, `0` и `-inf`.

Универсальный способ не ошибиться — написать `test_causal_no_leak` из примера выше.

**Про `-inf`.** Если строка маски полностью `False` (все ключи скрыты), `softmax` от строки
из `-inf` даёт `0/0 = NaN`, и NaN мгновенно расползётся по всей модели через `proj`
и residual. Использование `torch.finfo(dtype).min` вместо `-inf` превращает катастрофу
в безвредный мусор на позиции, которая всё равно замаскирована на выходе. Ситуация возникает
чаще, чем кажется: пустая последовательность в батче, causal-маска в комбинации с паддингом
в начале, скользящее окно attention на первых позициях.

**Когда писать своё, а когда брать `F.scaled_dot_product_attention`.** В проде — всегда
штатную: она диспатчится на FlashAttention или memory-efficient-реализацию и **не
материализует матрицу `(B, H, L, L)`**, что при `L = 4096` экономит десятки гигабайт.
Своя реализация нужна ровно в двух случаях: собеседование и нестандартная модификация
attention, которой в штатной нет.

> 💬 **На собеседовании.** Спросят: «Зачем делить на корень из `d_k`?» Хороший ответ —
> вывод через дисперсию: при независимых компонентах с единичной дисперсией скалярное
> произведение имеет дисперсию `d_k`, softmax от значений с разбросом `±√d_k` насыщается,
> градиент по немаксимальным позициям становится экспоненциально мал, и обучение
> останавливается. Деление возвращает дисперсию скоров к единице. Сильное дополнение:
> при инициализации это критично, а обученная модель может частично компенсировать масштаб
> нормой весов — но без нормировки она до этого просто не доучится.
> Плохой ответ: «для нормализации» без объяснения, что и зачем нормализуется.

---

## 6. Задача 5. Сколько параметров и сколько памяти

**Постановка.** Дана модель трансформера: $L$ слоёв, $d$ — размерность модели,
словарь $V$, максимальная длина контекста $s$. Посчитайте (а) число параметров
аналитически и кодом; (б) сколько GPU-памяти нужно для обучения с Adam в fp32;
(в) влезет ли обучение в 24 ГБ.

**Аналитический счёт параметров одного блока трансформера.**

Attention: четыре матрицы $d \times d$ (проекции $W_Q, W_K, W_V$ и выходная $W_O$) →
$4d^2$ параметров.

FFN со стандартным расширением в 4 раза: $d \times 4d$ и $4d \times d$ → $8d^2$.

Нормализации: две RMSNorm по $d$ параметров → $2d$ (пренебрежимо).

Итого на блок:

$$
P_{\text{block}} = 12 d^2 + 2d \approx 12 d^2
$$

где $d$ — размерность модели (`d_model`). Полная модель:

$$
P_{\text{total}} = V d + L \cdot 12 d^2 + (\text{голова } V d \text{, если веса не связаны})
$$

где $V$ — размер словаря, $L$ — число блоков, $Vd$ — таблица эмбеддингов токенов.
При weight tying (общие веса эмбеддинга и выходной головы) второе слагаемое исчезает.

Проверим на реальной модели: GPT-2 small имеет $L = 12$, $d = 768$, $V = 50257$.
$12 \cdot 12 \cdot 768^2 \approx 85$ млн плюс эмбеддинги $50257 \cdot 768 \approx 39$ млн
плюс позиционные $1024 \cdot 768 \approx 0.8$ млн — около 124 млн, что совпадает
с известной цифрой.

**Код, который надо уметь писать не задумываясь:**

```python
import torch
import torch.nn as nn


def count_parameters(model: nn.Module) -> dict:
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen = sum(p.numel() for p in model.parameters() if not p.requires_grad)
    buffers = sum(b.numel() for b in model.buffers())
    # element_size() — байт на элемент; для fp32 это 4, для bf16 — 2
    param_bytes = sum(p.numel() * p.element_size() for p in model.parameters())
    return {
        "trainable": trainable,
        "frozen": frozen,
        "buffers": buffers,
        "param_mb": param_bytes / 2**20,
    }


def parameters_by_module(model: nn.Module, top_k: int = 10) -> list[tuple[str, int]]:
    """Где именно живут параметры. Первое, что нужно смотреть при вопросе
    'почему модель такая большая' — обычно ответ 'эмбеддинги'."""
    rows = []
    for name, module in model.named_children():
        n = sum(p.numel() for p in module.parameters())
        rows.append((name, n))
    return sorted(rows, key=lambda r: -r[1])[:top_k]


class TinyTransformer(nn.Module):
    def __init__(self, vocab=50257, d=768, n_layers=12, n_heads=12, max_len=1024):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab, d)
        self.pos_emb = nn.Embedding(max_len, d)
        layer = nn.TransformerEncoderLayer(
            d_model=d, nhead=n_heads, dim_feedforward=4 * d,
            batch_first=True, norm_first=True,
        )
        self.blocks = nn.TransformerEncoder(layer, num_layers=n_layers)
        self.head = nn.Linear(d, vocab, bias=False)
        self.head.weight = self.tok_emb.weight       # weight tying: экономит V*d параметров

    def forward(self, ids):
        pos = torch.arange(ids.size(1), device=ids.device)
        h = self.tok_emb(ids) + self.pos_emb(pos)[None, :, :]
        return self.head(self.blocks(h))


model = TinyTransformer()
print(count_parameters(model))
print(parameters_by_module(model))
```

**Память при обучении.** Складывается из четырёх слагаемых:

$$
M_{\text{total}} = \underbrace{P \cdot b_w}_{\text{веса}} + \underbrace{P \cdot b_g}_{\text{градиенты}}
+ \underbrace{P \cdot b_o}_{\text{состояния оптимизатора}} + \underbrace{A}_{\text{активации}}
$$

где $P$ — число обучаемых параметров, $b_w$ — байт на вес, $b_g$ — байт на градиент,
$b_o$ — байт на параметр в состоянии оптимизатора, $A$ — память под активации,
сохранённые для обратного прохода.

Конкретные значения:

| Компонента | fp32 + Adam | AMP (bf16 автокаст) + Adam | SGD без momentum, fp32 |
|---|---|---|---|
| Веса $b_w$ | 4 Б | 4 Б (мастер-копия fp32) | 4 Б |
| Градиенты $b_g$ | 4 Б | 4 Б | 4 Б |
| Оптимизатор $b_o$ | 8 Б (`exp_avg` + `exp_avg_sq`) | 8 Б | 0 Б |
| **Итого на параметр** | **16 Б** | **16 Б** (+ временные bf16-копии) | **8 Б** |

Отсюда прикидка: **модель на 1 млрд параметров требует ~16 ГБ только под состояние
обучения**, без единой активации. Это цифра, которую стоит помнить наизусть.

Активации оцениваются грубо: для трансформера без gradient checkpointing порядок величины —

$$
A \sim c \cdot B \cdot s \cdot d \cdot L \cdot b_a
$$

где $B$ — размер батча, $s$ — длина последовательности, $d$ — размерность модели,
$L$ — число слоёв, $b_a$ — байт на элемент активации (2 при bf16), $c$ — константа порядка
10–20, зависящая от реализации (сколько промежуточных тензоров сохраняется). Отдельно
и опасно: матрица внимания $(B, H, s, s)$ — при $s = 4096$, $B = 8$, $H = 16$ это
$8 \cdot 16 \cdot 4096^2 \cdot 2 \approx 4.3$ ГБ **на слой**, если не используется
FlashAttention.

**Мерить надёжнее, чем считать.** Формулы дают порядок; точное число даёт эксперимент:

```python
def measure_peak_memory(model, batch, criterion, device="cuda"):
    """Пиковая память одного шага обучения. Запускать на 2-3 шагах:
    первый шаг всегда дороже из-за ленивой инициализации состояний Adam."""
    if not torch.cuda.is_available():
        return None
    model.to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=1e-4)

    for step in range(3):
        torch.cuda.reset_peak_memory_stats()
        x, y = batch[0].to(device), batch[1].to(device)
        opt.zero_grad(set_to_none=True)
        loss = criterion(model(x).flatten(0, 1), y.flatten())
        loss.backward()
        opt.step()
        torch.cuda.synchronize()          # без этого замер будет неполным: работа асинхронна
        print(
            f"step {step}: "
            f"peak allocated {torch.cuda.max_memory_allocated() / 2**30:.2f} GiB, "
            f"reserved {torch.cuda.max_memory_reserved() / 2**30:.2f} GiB"
        )
```

Разница между `allocated` и `reserved` — это фрагментация кэширующего аллокатора.
`reserved` — сколько PyTorch забрал у драйвера, `allocated` — сколько реально занято
тензорами. Если `reserved` сильно больше `allocated` и вы ловите OOM — проблема
во фрагментации, лечится `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
или выравниванием размеров батчей.

> 💬 **На собеседовании.** Спросят: «Модель на 7 млрд параметров — влезет обучение
> в одну A100 80 ГБ?» Хороший ответ: считаем — 7e9 × 16 байт (fp32-веса + градиенты +
> два момента Adam) ≈ 112 ГБ только под состояние, без активаций. Не влезет. Варианты:
> ZeRO-2/3 или FSDP с шардированием состояний по картам, 8-битный Adam (снижает
> 8 Б/параметр до 2 Б), LoRA (обучаем 0.1–1% параметров, состояние оптимизатора падает
> на два порядка), gradient checkpointing против активаций. Для инференса тех же 7 млрд
> в bf16 нужно ~14 ГБ весов плюс KV-cache — влезает свободно.
> Плохой ответ: «надо попробовать» без арифметики.

---

## 7. Задача 6. Отладить NaN в лоссе

**Постановка.** Обучение шло нормально, на шаге ~800 лосс стал `nan` и больше не восстановился.
Опишите протокол диагностики и почините.

Это самая частая задача формата «почините». Ждут **протокол**, а не догадку.

**Протокол из восьми шагов.**

**Шаг 0. Зафиксировать воспроизведение.** Поставьте seed, отключите shuffle, найдите
номер шага и сохраните батч, на котором всё ломается. Пока баг невоспроизводим, чинить нечего.

**Шаг 1. Проверить входные данные.** Самая частая причина — не в модели.

```python
def assert_finite(name: str, t: torch.Tensor) -> None:
    if not torch.isfinite(t).all():
        n_nan = torch.isnan(t).sum().item()
        n_inf = torch.isinf(t).sum().item()
        raise ValueError(
            f"{name}: {n_nan} NaN, {n_inf} inf из {t.numel()}; "
            f"min={t[torch.isfinite(t)].min() if torch.isfinite(t).any() else 'n/a'}"
        )


for batch in loader:
    assert_finite("x", batch["x"])
    assert_finite("y", batch["y"])
```

Откуда берутся NaN во входе: деление на ноль при нормализации признака с нулевой дисперсией,
`log` от неположительного значения, пропуски, заполненные `np.nan` вместо импутации,
битая строка в parquet. Для табличных пайплайнов это причина в большинстве случаев.

**Шаг 2. Проверить значение лосса на первом шаге.** Оно должно совпадать с теоретическим
для случайной инициализации: для $K$-классовой кросс-энтропии это $\ln K$
(для 1000 классов ≈ 6.9), для бинарной ≈ 0.693, для MSE — дисперсия таргета.
Если первый лосс сильно другой — сломана не оптимизация, а постановка: перепутаны оси,
не те метки, лосс применён к вероятностям вместо логитов.

**Шаг 3. Найти конкретную операцию.**

```python
# Медленно (в разы), поэтому только для отладки: PyTorch запомнит стек создания каждого
# тензора и при NaN в градиенте покажет строку кода, где родилась операция
with torch.autograd.detect_anomaly():
    loss = criterion(model(x), y)
    loss.backward()
```

Если NaN появляется только в градиенте (forward конечен), `detect_anomaly` укажет
на функцию — обычно это `SqrtBackward` (производная $\sqrt{x}$ в нуле бесконечна),
`DivBackward`, `LogBackward` или `PowBackward` с дробной степенью.

**Шаг 4. Расставить хуки и найти слой.**

```python
def add_nan_hooks(model: nn.Module) -> list:
    handles = []

    def fwd_hook(name):
        def hook(_module, _inp, out):
            t = out[0] if isinstance(out, tuple) else out
            if torch.is_tensor(t) and not torch.isfinite(t).all():
                raise RuntimeError(f"NaN/inf на выходе {name}")
        return hook

    for name, module in model.named_modules():
        if len(list(module.children())) == 0:          # только листовые модули
            handles.append(module.register_forward_hook(fwd_hook(name)))
    return handles


handles = add_nan_hooks(model)
# ... воспроизвести шаг ...
for h in handles:
    h.remove()                                          # хуки надо снимать: иначе утечка
```

**Шаг 5. Посмотреть на нормы градиентов до взрыва.** NaN редко приходит внезапно —
обычно ему предшествует рост нормы на несколько порядков.

```python
def grad_global_norm(model: nn.Module) -> float:
    total = 0.0
    for p in model.parameters():
        if p.grad is not None:
            total += p.grad.detach().float().pow(2).sum().item()
    return total ** 0.5


# логировать каждые N шагов; если норма растёт экспоненциально — это взрыв градиента
```

Лечение взрыва: `torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)`
перед `optimizer.step()`, снижение learning rate, добавление warmup.

**Шаг 6. Проверить численную стабильность своих формул.** Типовые источники:

| Конструкция | Проблема | Замена |
|---|---|---|
| `torch.log(p)` | `-inf` при `p = 0` | `F.log_softmax` / `*_with_logits` |
| `torch.sqrt(x)` | градиент `inf` при `x = 0` | `torch.sqrt(x + eps)` |
| `x / y` | `NaN` при `y = 0` | `x / y.clamp(min=eps)` |
| `torch.exp(x)` | `inf` при `x > 88` (fp32) | вычесть максимум (log-sum-exp) |
| `(1 - p) ** gamma` | `0 ** 0.5` градиент `inf` | `clamp(min=1e-8)` |
| `x.std()` | `NaN` при одном элементе | проверить размер |
| `acos`, `atanh` | `NaN` вне области определения | `clamp(-1 + eps, 1 - eps)` |

**Шаг 7. Проверить маски.** Полностью замаскированная строка в softmax даёт `NaN` —
подробно разобрано в задаче 4. Признак: NaN появляется на конкретных батчах,
а не на конкретном шаге.

**Шаг 8. Проверить fp16.** Если обучение идёт в fp16 (не bf16), NaN может быть переполнением:
максимум fp16 — 65504, и квадрат активации величиной 300 уже `inf`.

```python
# Диагностика: временно переключиться на fp32 или bf16
# Если в bf16 NaN исчезает — проблема была в диапазоне fp16, а не в математике
with torch.amp.autocast("cuda", dtype=torch.bfloat16):
    ...
```

bf16 имеет тот же диапазон экспоненты, что fp32 (при меньшей мантиссе), поэтому
переполняется практически никогда. На Ampere и новее это дефолтный выбор.

**Сводная таблица «симптом → причина».**

| Симптом | Наиболее вероятная причина |
|---|---|
| NaN на первом же шаге | NaN во входных данных или в метках |
| Лосс на первом шаге далёк от $\ln K$ | перепутаны оси/метки, лосс от вероятностей |
| NaN после длительного нормального обучения | взрыв градиента, слишком высокий LR, отсутствие warmup |
| NaN сразу после падения лосса | `log(0)` в самописном лоссе на уверенных предсказаниях |
| NaN только на некоторых батчах | пустая последовательность, полностью замаскированная строка, деление на нулевую длину |
| NaN только в fp16, в fp32 всё нормально | переполнение диапазона; переходить на bf16 |
| `inf` в лоссе, а потом NaN | переполнение в forward до появления NaN |

> 💬 **На собеседовании.** Спросят: «Лосс стал NaN. Что делаете?» Хороший ответ — назвать
> протокол в правильном порядке: сначала воспроизвести и локализовать шаг, потом проверить
> данные (это чаще всего), потом сверить лосс первого шага с теоретическим, потом
> `detect_anomaly` и хуки для локализации слоя, потом посмотреть на историю нормы градиента,
> и только потом лезть в гиперпараметры. Отдельно — проверить, не fp16 ли это. Плохой ответ:
> «уменьшу learning rate» — иногда помогает, но это не диагностика, и на следующем вопросе
> «а если не помогло?» разговор заканчивается.

---

## 8. Задача 7. Найти утечку памяти

**Постановка.** Обучение на GPU падает с OOM не сразу, а через N шагов или в конце эпохи.
Память растёт монотонно. Найдите причину.

**Классический код с утечкой — найдите её сами, прежде чем читать дальше:**

```python
losses = []
val_predictions = []

for epoch in range(10):
    for x, y in train_loader:
        optimizer.zero_grad()
        out = model(x)
        loss = criterion(out, y)
        loss.backward()
        optimizer.step()
        losses.append(loss)                    # (1)

    model.eval()
    for x, y in val_loader:
        val_predictions.append(model(x))       # (2)
    print(f"epoch {epoch}: {sum(losses) / len(losses)}")   # (3)
```

**Три утечки.**

**(1) `losses.append(loss)`.** `loss` — это тензор, связанный с графом вычислений.
Пока на него есть ссылка, Python не может освободить **весь граф** этого шага, а вместе
с графом — все сохранённые для backward активации. За эпоху в 5000 шагов вы удерживаете
5000 графов. Правильно: `losses.append(loss.item())` — извлекает питоновское число и рвёт
связь с графом. Альтернатива, если нужен тензор: `loss.detach()`.

**(2) `val_predictions.append(model(x))`.** То же самое, плюс отсутствие `torch.no_grad()`:
на валидации граф вообще не нужен, а строится. Правильно:

```python
model.eval()
with torch.inference_mode():         # строже, чем no_grad: запрещает и запись version counter
    for x, y in val_loader:
        val_predictions.append(model(x).cpu())   # .cpu() освобождает GPU-память
```

**(3) `sum(losses)`.** Если в списке тензоры, `sum` строит цепочку сложений — ещё один граф.

**Правильная версия:**

```python
running_loss = 0.0
n_batches = 0

for x, y in train_loader:
    optimizer.zero_grad(set_to_none=True)
    loss = criterion(model(x), y)
    loss.backward()
    optimizer.step()
    running_loss += loss.item()        # item() ещё и синхронизирует; для скорости — раз в N шагов
    n_batches += 1
```

**Полный список причин роста памяти:**

| Причина | Симптом | Лечение |
|---|---|---|
| Накопление тензоров с графом в списке | линейный рост в пределах эпохи | `.item()` / `.detach()` |
| Нет `no_grad` на валидации | скачок памяти на валидации | `torch.inference_mode()` |
| `loss.backward(retain_graph=True)` без нужды | рост от шага к шагу | убрать флаг; он нужен только при нескольких backward по одному графу |
| Хранение выходов на GPU | рост на валидации/инференсе | `.cpu()` сразу после получения |
| Незакрытые хуки | медленный рост, замедление | `handle.remove()` |
| Рост длины последовательностей | пила с ростом пиков | сортировка по длине даёт стабильный пик; мерить `max_memory_allocated` на самом длинном батче |
| Фрагментация аллокатора | `reserved` >> `allocated`, OOM при свободной памяти | `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`, фиксированные формы |
| Утечка в `num_workers` (RAM, не GPU) | растёт потребление CPU-памяти | не хранить в `Dataset` питоновские списки/словари — они копируются из-за refcount; использовать numpy-массивы |
| Кэш в `Dataset` | RAM растёт по эпохе | ограничить размер кэша |

**Инструменты диагностики:**

```python
# 1. Быстрый мониторинг в цикле
if step % 100 == 0:
    print(f"alloc {torch.cuda.memory_allocated()/2**20:.0f} MiB, "
          f"reserved {torch.cuda.memory_reserved()/2**20:.0f} MiB")

# 2. Подробный отчёт по пулам аллокатора
print(torch.cuda.memory_summary())

# 3. Кто именно держит память: перечислить все живые тензоры
import gc
def live_tensors(min_mb=1.0):
    rows = []
    for obj in gc.get_objects():
        try:
            if torch.is_tensor(obj) and obj.is_cuda:
                mb = obj.numel() * obj.element_size() / 2**20
                if mb >= min_mb:
                    rows.append((tuple(obj.shape), str(obj.dtype), round(mb, 1)))
        except Exception:
            continue
    return sorted(rows, key=lambda r: -r[2])

# 4. Профиль аллокаций во времени (PyTorch 2.1+): пишет снимок, который открывается
#    на https://pytorch.org/memory_viz — видно, какие аллокации не освобождаются
torch.cuda.memory._record_memory_history(max_entries=100_000)
# ... несколько шагов обучения ...
torch.cuda.memory._dump_snapshot("mem_snapshot.pickle")
torch.cuda.memory._record_memory_history(enabled=None)
```

**Важное различие, которое часто путают.** `torch.cuda.empty_cache()` **не чинит утечки**.
Он возвращает драйверу память, которую PyTorch уже освободил внутри себя, но держит
в кэше — то есть уменьшает `reserved`, но не `allocated`. Если ваша проблема в том,
что `allocated` растёт, `empty_cache()` не поможет, зато замедлит обучение
(следующие аллокации пойдут через драйвер).

> ⚠️ **Типичная ошибка.** Увидев OOM, добавить `torch.cuda.empty_cache()` в цикл обучения.
> Это карго-культ: если память течёт, вызов не поможет, а если не течёт — он не нужен
> и только замедляет. Уместен он ровно в одном сценарии: между принципиально разными фазами
> (закончили обучение, начали инференс с другими формами тензоров).

---

## 9. Задача 8. Ускорить обучающий цикл

**Постановка.** Эпоха идёт 40 минут, `nvidia-smi` показывает загрузку GPU 25%.
Ускорьте, не меняя модель и не теряя качества.

**Первый шаг — измерить, а не угадывать.** Загрузка GPU 25% почти всегда означает,
что GPU ждёт данные.

```python
import time
import torch


def profile_loop(model, loader, criterion, optimizer, device, n_steps=50):
    """Грубое, но честное разделение времени: сколько уходит на данные, сколько на GPU.
    Ключ — torch.cuda.synchronize(): без него замеры бессмысленны, потому что
    CUDA-операции асинхронны и возвращают управление до фактического выполнения."""
    model.train()
    t_data = t_compute = 0.0
    t0 = time.perf_counter()

    for step, (x, y) in enumerate(loader):
        if step >= n_steps:
            break
        torch.cuda.synchronize()
        t_data += time.perf_counter() - t0

        t1 = time.perf_counter()
        x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
        optimizer.zero_grad(set_to_none=True)
        loss = criterion(model(x), y)
        loss.backward()
        optimizer.step()
        torch.cuda.synchronize()
        t_compute += time.perf_counter() - t1

        t0 = time.perf_counter()

    total = t_data + t_compute
    print(f"данные: {t_data:.1f} с ({100*t_data/total:.0f}%), "
          f"вычисления: {t_compute:.1f} с ({100*t_compute/total:.0f}%)")
```

Более точный инструмент — штатный профайлер:

```python
from torch.profiler import profile, ProfilerActivity, schedule

with profile(
    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    schedule=schedule(wait=1, warmup=1, active=3),   # прогрев обязателен: первые шаги нерепрезентативны
    record_shapes=True,
    profile_memory=True,
) as prof:
    for step, (x, y) in enumerate(loader):
        if step >= 5:
            break
        # ... шаг обучения ...
        prof.step()

print(prof.key_averages().table(sort_by="self_cuda_time_total", row_limit=15))
```

**Чек-лист ускорения, в порядке отношения «выигрыш / усилие».**

**Если узкое место — данные (GPU простаивает):**

```python
loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True,
    num_workers=8,             # ~число физических ядер; 0 = загрузка в основном процессе
    pin_memory=True,           # закреплённая память -> асинхронное копирование на GPU
    persistent_workers=True,   # не пересоздавать воркеры каждую эпоху (экономит секунды×эпохи)
    prefetch_factor=4,         # сколько батчей воркер готовит заранее
    drop_last=True,
)
# и в цикле:
x = x.to(device, non_blocking=True)   # работает ТОЛЬКО вместе с pin_memory=True
```

Дальше по данным: перенести тяжёлую предобработку из `__getitem__` в офлайн-подготовку;
хранить данные в формате, который читается без разбора (numpy memmap, parquet вместо CSV,
предтокенизированные последовательности); делать аугментации на GPU, если они векторизуемы.

**Если узкое место — вычисления:**

| Приём | Типичный выигрыш | Цена |
|---|---|---|
| AMP (bf16/fp16) | 1.5–3× на Ampere+ | почти ноль (см. задачу 10) |
| `torch.set_float32_matmul_precision("high")` | 1.2–2× для fp32-матмулов | небольшая потеря точности (TF32) |
| Увеличить batch size до заполнения памяти | 1.2–2× | нужно скорректировать LR |
| `torch.compile(model)` | 1.1–2× | минуты на компиляцию, ломается при динамических формах |
| `F.scaled_dot_product_attention` вместо своей | 2–4× на длинных последовательностях | ноль |
| `channels_last` для CNN | 1.2–1.8× | одна строка |
| Убрать `.item()` / `.cpu()` из горячего цикла | 1.05–1.5× | логировать реже |
| Fused-оптимизатор (`fused=True` в AdamW) | 1.05–1.15× | требует CUDA |

```python
# Компиляция и формат памяти
torch.set_float32_matmul_precision("high")      # разрешить TF32 на матмулах
model = model.to(memory_format=torch.channels_last)   # для свёрточных сетей
model = torch.compile(model)                    # PyTorch 2.x; первый шаг будет долгим
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, fused=torch.cuda.is_available())
```

**Про `.item()` — неочевидное.** Каждый вызов `.item()`, `.cpu()`, `print(tensor)`,
`if loss > threshold` заставляет CPU **дождаться** завершения всех поставленных в очередь
CUDA-операций. Конвейер «CPU ставит задачи — GPU их считает» рушится. В цикле, где
логирование идёт каждый шаг, это отнимает 10–30%. Правильно — копить лосс в тензоре
на GPU и синхронизироваться раз в N шагов:

```python
loss_accum = torch.zeros((), device=device)
for step, batch in enumerate(loader):
    ...
    loss_accum += loss.detach()               # остаётся на GPU, синхронизации нет
    if step % 100 == 0:
        print(f"loss: {(loss_accum / 100).item():.4f}")   # одна синхронизация на 100 шагов
        loss_accum.zero_()
```

**Про `torch.compile` и динамические формы.** При каждой новой комбинации форм входа
происходит перекомпиляция. Для NLP с переменной длиной это убивает выигрыш: если длины
непрерывно разные, компилятор перезапускается постоянно. Лечение — округлять длину
батча до кратной 64 (bucketing из задачи 2), либо `torch.compile(model, dynamic=True)`.

> 💬 **На собеседовании.** Спросят: «Обучение медленное, что делать?» Хороший ответ
> начинается с измерения: посмотреть загрузку GPU (`nvidia-smi dmon` или профайлер)
> и разделить время на «ждём данные» и «считаем». Дальше — разные наборы мер: для данных
> `num_workers`, `pin_memory`, `persistent_workers`, вынос предобработки в офлайн;
> для вычислений — AMP, больший батч, `torch.compile`, штатный SDPA, устранение
> синхронизаций. И отдельно: сначала проверить, не считаете ли вы что-то лишнее
> (валидация каждый шаг, метрики на CPU, лог в файл). Плохой ответ: сразу «возьму
> более мощную карту» или «уменьшу модель» — обе меры меняют задачу, а не решают её.

---

## 10. Задача 9. Градиентное накопление

**Постановка.** Целевой эффективный батч — 256, в память влезает только 32. Реализуйте
градиентное накопление. Что при этом эквивалентно большому батчу, а что нет?

**Решение.**

```python
def train_epoch_with_accumulation(
    model, loader, criterion, optimizer, scheduler, device,
    accum_steps: int = 8, max_grad_norm: float = 1.0,
):
    model.train()
    optimizer.zero_grad(set_to_none=True)
    n_batches = len(loader)

    for step, (x, y) in enumerate(loader):
        x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)

        loss = criterion(model(x), y)

        # Делим на accum_steps: criterion с reduction='mean' уже усреднил внутри
        # микробатча, а нам нужно среднее по ВСЕМ accum_steps микробатчам.
        # Без деления норма градиента вырастет в accum_steps раз — фактически
        # вы поднимете learning rate в 8 раз и удивитесь расхождению.
        (loss / accum_steps).backward()

        is_accum_end = (step + 1) % accum_steps == 0
        is_last_batch = (step + 1) == n_batches      # чтобы не потерять хвост эпохи

        if is_accum_end or is_last_batch:
            # Клиппинг делаем ПОСЛЕ накопления всех микробатчей: клиппинг каждого
            # микробатча по отдельности — это другая (и обычно нежелательная) операция
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
            optimizer.step()
            optimizer.zero_grad(set_to_none=True)
            scheduler.step()      # шаг расписания привязан к шагу ОПТИМИЗАТОРА, не к батчу
```

**Объяснение.**

**Что эквивалентно большому батчу.** Градиент. Для лосса с `reduction='mean'`

$$
\frac{1}{N}\sum_{i=1}^{N} \nabla \ell_i
\;=\;
\frac{1}{k}\sum_{j=1}^{k}\left(\frac{1}{m}\sum_{i \in B_j} \nabla \ell_i\right)
$$

где $N = k \cdot m$ — размер эффективного батча, $k$ — число шагов накопления,
$m$ — размер микробатча, $B_j$ — $j$-й микробатч, $\nabla \ell_i$ — градиент лосса
на объекте $i$. Равенство выполняется точно (с точностью до ошибок округления)
**при условии, что все микробатчи одного размера** — отсюда `drop_last=True`.

**Что НЕ эквивалентно — четыре вещи, за которые дают балл:**

1. **BatchNorm.** Статистики считаются по микробатчу из 32 объектов, а не по 256.
   Оценка среднего и дисперсии шумнее, и результат обучения отличается. Лечение:
   `nn.SyncBatchNorm` (не помогает для накопления, только для DDP), `GroupNorm`
   или `LayerNorm` вместо BatchNorm, либо смириться.
2. **Dropout и другие стохастические слои.** Маски разные в каждом микробатче —
   это скорее плюс (больше усреднения), но строго это не тот же вычислительный граф.
3. **Скорость.** Накопление **не ускоряет** обучение: вы делаете те же $k$ прямых
   и обратных проходов. Экономится только память под активации.
4. **In-batch negatives.** Для контрастивного обучения (двухбашенки, CLIP, SimCLR)
   негативы берутся внутри батча. При накоплении негативов остаётся 32, а не 256 —
   и качество падает существенно. Это ловушка, о которой почти никто не помнит.
   Обходится специальными приёмами (GradCache, кэширование эмбеддингов), но «просто
   накопить» здесь не работает.

**В DDP — обязательный нюанс.** По умолчанию `DistributedDataParallel` синхронизирует
градиенты между процессами на **каждом** `backward()`. При накоплении это лишний
all-reduce на каждом микробатче:

```python
from contextlib import nullcontext

for step, batch in enumerate(loader):
    is_accum_end = (step + 1) % accum_steps == 0
    # no_sync() отключает синхронизацию градиентов на промежуточных микробатчах
    sync_ctx = nullcontext() if is_accum_end else model.no_sync()
    with sync_ctx:
        (criterion(model(batch["x"]), batch["y"]) / accum_steps).backward()
    if is_accum_end:
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)
```

Выигрыш на медленном интерконнекте — десятки процентов.

> 💬 **На собеседовании.** Спросят: «Чем градиентное накопление отличается от обучения
> с большим батчем?» Хороший ответ: по градиенту это математически то же самое при
> одинаковых микробатчах и правильном делении лосса; отличия — в слоях, зависящих
> от статистики батча (BatchNorm считает по 32, а не по 256), в in-batch negatives
> для контрастивных задач, и в том, что скорости накопление не даёт — только экономию
> памяти. Плюс упомянуть `no_sync()` в DDP. Плохой ответ: «это одно и то же» без оговорок
> либо «это просто способ ускорить обучение».

---

## 11. Задача 10. Mixed precision

**Постановка.** Включите обучение в смешанной точности. Объясните, зачем `GradScaler`
и когда он не нужен.

**Решение (fp16 + GradScaler):**

```python
import torch

use_cuda = torch.cuda.is_available()
device = "cuda" if use_cuda else "cpu"
# GradScaler безвреден при enabled=False — код одинаково работает на CPU
scaler = torch.amp.GradScaler("cuda", enabled=use_cuda)

for x, y in loader:
    x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
    optimizer.zero_grad(set_to_none=True)

    # Внутри autocast операции подбирают тип автоматически: матмулы и свёртки в fp16,
    # softmax/нормализации/лоссы остаются в fp32. Лосс считаем ВНУТРИ блока
    with torch.amp.autocast("cuda", dtype=torch.float16, enabled=use_cuda):
        loss = criterion(model(x), y)

    # Масштабируем лосс перед backward: градиенты умножатся на тот же коэффициент
    scaler.scale(loss).backward()

    # Перед клиппингом градиенты надо вернуть в исходный масштаб — иначе max_norm
    # будет применён к раздутым числам и клиппинг не сработает
    scaler.unscale_(optimizer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

    scaler.step(optimizer)   # пропустит шаг, если в градиентах есть inf/NaN
    scaler.update()          # подстроит масштаб: уменьшит при переполнении, поднимет со временем
```

**Решение (bf16, современный дефолт на Ampere+):**

```python
# Для bf16 GradScaler НЕ нужен: у bf16 тот же диапазон экспоненты, что у fp32,
# и градиенты не проваливаются в машинный ноль
with torch.amp.autocast("cuda", dtype=torch.bfloat16):
    loss = criterion(model(x), y)
loss.backward()
torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
optimizer.step()
```

**Объяснение.**

**Зачем вообще масштабировать.** fp16 имеет 5 бит экспоненты: наименьшее нормальное
положительное число ≈ $6 \cdot 10^{-5}$, с денормалями ≈ $6 \cdot 10^{-8}$. Градиенты
в глубоких сетях легко бывают порядка $10^{-8}$ и меньше — они обнуляются, и слой
перестаёт обучаться, причём молча. `GradScaler` умножает лосс на большой коэффициент
$S$ (стартует с $2^{16}$); по правилу дифференцирования все градиенты умножаются
на тот же $S$ и уезжают из зоны денормалей. Перед шагом оптимизатора масштаб снимается.

**Динамическая подстройка.** Слишком большой $S$ вызовет переполнение в другую сторону.
Поэтому `scaler.step()` сначала проверяет градиенты на `inf`/`NaN`: если они есть —
**шаг пропускается**, а $S$ уменьшается вдвое. Если несколько сотен шагов подряд прошли
без переполнения — $S$ удваивается. Отсюда важное следствие: в начале обучения несколько
шагов действительно пропускаются, это нормально и не является багом.

**Почему bf16 проще.** bfloat16 — это fp32 с обрезанной мантиссой: 8 бит экспоненты
(как в fp32) и 7 бит мантиссы. Диапазон тот же, что у fp32, поэтому ни переполнения,
ни исчезновения градиентов нет — масштабирование не нужно. Плата: меньшая точность
представления (относительная погрешность ~$2^{-8}$ против ~$2^{-11}$ у fp16), что
на обучении почти не сказывается. Требуется Ampere (A100, RTX 30xx) или новее;
на V100 и старее доступен только fp16.

**Что автокаст оставляет в fp32.** PyTorch держит список операций: матричные умножения
и свёртки идут в пониженной точности, а `softmax`, `log_softmax`, нормализации,
`sum` по большим осям и функции потерь — в fp32, потому что там точность критична.
Поэтому лосс надо считать **внутри** блока `autocast`: он сам решит, что где считать.

**Сколько экономит.** Память под активации падает примерно вдвое (веса и состояния
Adam остаются в fp32 — см. задачу 5). Скорость на Tensor Cores растёт в 1.5–3 раза
для матрично-тяжёлых моделей. Для маленьких моделей и на данных, где узкое место —
DataLoader, выигрыша может не быть вовсе.

> ⚠️ **Типичная ошибка.** Поставить `scaler.unscale_(optimizer)` после `scaler.step()`
> или вызвать `unscale_` дважды за шаг — оба варианта дают `RuntimeError`. И вторая:
> обернуть в `autocast` весь цикл, включая `backward()` и `optimizer.step()`.
> Внутри `autocast` должен быть **только forward и вычисление лосса**; backward
> использует те же типы автоматически, а шаг оптимизатора обязан идти в fp32.

---

## 12. Задача 11. Воспроизводимость

**Постановка.** Два запуска одного и того же скрипта дают разный результат. Сделайте
обучение воспроизводимым и объясните, где полного детерминизма добиться нельзя.

**Решение.**

```python
import os
import random
import numpy as np
import torch


def set_seed(seed: int = 42) -> None:
    """Фиксируем все источники случайности. Вызывать ДО создания модели:
    инициализация весов тоже использует глобальный генератор."""
    os.environ["PYTHONHASHSEED"] = str(seed)   # влияет на порядок обхода set/dict в подпроцессах
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)           # на все видимые GPU


def enable_full_determinism(seed: int = 42) -> None:
    """Полный детерминизм — ценой скорости. Для отладки и для регрессионных тестов."""
    set_seed(seed)
    # Некоторые CUBLAS-ядра недетерминированы без выделенного workspace.
    # Переменную надо выставить ДО первой CUDA-операции, лучше — в начале скрипта
    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
    # Упадёт с ошибкой на операциях, у которых нет детерминированной реализации,
    # — это лучше, чем молча получить недетерминизм
    torch.use_deterministic_algorithms(True, warn_only=False)
    torch.backends.cudnn.deterministic = True
    # benchmark=True подбирает быстрейший алгоритм свёртки при первом вызове;
    # выбор зависит от загрузки карты, поэтому недетерминирован
    torch.backends.cudnn.benchmark = False


def seed_worker(worker_id: int) -> None:
    """DataLoader с num_workers>0 форкает процессы; каждому нужен свой воспроизводимый seed.
    torch.initial_seed() в воркере уже уникален и зависит от base_seed генератора."""
    worker_seed = torch.initial_seed() % 2**32
    np.random.seed(worker_seed)
    random.seed(worker_seed)


set_seed(42)
g = torch.Generator()
g.manual_seed(42)

loader = torch.utils.data.DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,
    worker_init_fn=seed_worker,   # без этого numpy-аугментации во всех воркерах одинаковы
    generator=g,                  # фиксирует порядок перемешивания
)
```

**Объяснение — где детерминизма нет и почему.**

**Атомарные операции на GPU.** `scatter_add`, `index_add`, обратный проход
`nn.Embedding` с повторяющимися индексами, `bincount` складывают значения в порядке,
который зависит от планирования потоков. Сложение float неассоциативно:
$(a + b) + c \ne a + (b + c)$ в конечной точности. Отсюда — разные результаты
при одинаковом входе. `torch.use_deterministic_algorithms(True)` заставляет PyTorch
использовать детерминированные (более медленные) варианты либо падать с внятной ошибкой.

**Многопоточность на CPU.** Порядок редукции в OpenMP-ядрах тоже может плавать;
`torch.set_num_threads(1)` устраняет, ценой скорости.

**Разное железо и версии.** Один и тот же код на A100 и на V100 даст разные числа:
другие ядра, другой TF32, другие алгоритмы свёртки. Между версиями PyTorch/cuDNN —
то же самое. **Детерминизм воспроизводим только в фиксированном окружении**, и это
надо говорить вслух: воспроизводимость эксперимента обеспечивается не только seed'ом,
но и зафиксированным образом (версии библиотек, драйвер, тип GPU).

**Распределённое обучение.** Порядок редукции в NCCL all-reduce не гарантирован;
плюс любое изменение числа процессов меняет разбиение данных.

**Что делать практически.** Полный детерминизм включают для отладки и для тестов
(«обучение из одного и того же состояния даёт тот же лосс» — отличный регрессионный
тест, см. [следующую главу](07-testing-and-code-quality.md)). Для продовых прогонов
обычно достаточно **статистической** воспроизводимости: фиксируем seed, но принимаем,
что метрика колеблется. И тогда важнее другое — **логировать разброс**: запустить
обучение с 3–5 разными seed'ами и указывать в отчёте среднее и стандартное отклонение.
Улучшение на 0.2%, которое меньше межзапускного разброса, — не улучшение.

> 💬 **На собеседовании.** Спросят: «Как сделать обучение воспроизводимым?» Хороший ответ:
> перечислить все источники случайности (Python `random`, numpy, torch CPU и CUDA,
> воркеры DataLoader, порядок перемешивания через `generator`, аугментации), включить
> `use_deterministic_algorithms` и `cudnn.deterministic`, зафиксировать
> `CUBLAS_WORKSPACE_CONFIG`. И **сразу** добавить, что полного детерминизма между
> разным железом и версиями библиотек не бывает из-за неассоциативности сложения float
> и атомарных операций — поэтому в отчётах правильно указывать разброс по нескольким
> seed'ам, а не одно число. Плохой ответ: «поставлю `torch.manual_seed(42)`» — этого
> не хватает даже для одной машины.

---

## 13. Задача 12. Early stopping и лучший чекпоинт

**Постановка.** Реализуйте раннюю остановку по валидационной метрике и сохранение
лучшего чекпоинта, из которого можно продолжить обучение.

**Решение.**

```python
from dataclasses import dataclass, field
from pathlib import Path
import torch


@dataclass
class EarlyStopping:
    patience: int = 5              # сколько эпох терпим отсутствие улучшения
    min_delta: float = 1e-4        # улучшение меньше этого не считается улучшением
    mode: str = "min"              # "min" для лосса, "max" для accuracy/AUC
    best: float = field(init=False)
    counter: int = field(init=False, default=0)
    should_stop: bool = field(init=False, default=False)

    def __post_init__(self):
        if self.mode not in {"min", "max"}:
            raise ValueError(self.mode)
        self.best = float("inf") if self.mode == "min" else float("-inf")

    def is_better(self, value: float) -> bool:
        # min_delta со знаком: улучшением считается только заметное изменение,
        # иначе шум на 6-м знаке будет бесконечно сбрасывать счётчик терпения
        if self.mode == "min":
            return value < self.best - self.min_delta
        return value > self.best + self.min_delta

    def step(self, value: float) -> bool:
        """Возвращает True, если это новая лучшая метрика."""
        if self.is_better(value):
            self.best = value
            self.counter = 0
            return True
        self.counter += 1
        self.should_stop = self.counter >= self.patience
        return False


def save_checkpoint(path: Path, *, model, optimizer, scheduler, epoch, best_metric, scaler=None):
    """Сохраняем state_dict, а НЕ сам объект модели: pickle всей модели привязывает
    файл к путям импорта и версиям классов — через полгода он не загрузится."""
    payload = {
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),      # без него дообучение стартует с нулевых моментов
        "scheduler": scheduler.state_dict() if scheduler is not None else None,
        "scaler": scaler.state_dict() if scaler is not None else None,
        "epoch": epoch,
        "best_metric": best_metric,
        "torch_version": torch.__version__,       # чтобы понять, чем открывать
    }
    tmp = path.with_suffix(path.suffix + ".tmp")
    torch.save(payload, tmp)
    tmp.replace(path)     # атомарная замена: прерывание записи не оставит битый чекпоинт


def load_checkpoint(path: Path, *, model, optimizer=None, scheduler=None, map_location="cpu"):
    # weights_only=True (дефолт с torch 2.6) запрещает исполнение произвольного кода
    # при загрузке — обязательно для любых чужих чекпоинтов
    ckpt = torch.load(path, map_location=map_location, weights_only=True)
    model.load_state_dict(ckpt["model"])
    if optimizer is not None and ckpt.get("optimizer"):
        optimizer.load_state_dict(ckpt["optimizer"])
    if scheduler is not None and ckpt.get("scheduler"):
        scheduler.load_state_dict(ckpt["scheduler"])
    return ckpt["epoch"], ckpt["best_metric"]
```

Использование:

```python
stopper = EarlyStopping(patience=5, mode="max")     # следим за ROC-AUC
ckpt_path = Path("runs/exp1/best.pt")
ckpt_path.parent.mkdir(parents=True, exist_ok=True)

for epoch in range(100):
    train_one_epoch(model, train_loader, criterion, optimizer, device)
    val_auc = evaluate(model, val_loader, device)

    if stopper.step(val_auc):
        save_checkpoint(ckpt_path, model=model, optimizer=optimizer,
                        scheduler=scheduler, epoch=epoch, best_metric=val_auc)
        print(f"epoch {epoch}: новый лучший AUC {val_auc:.4f}, чекпоинт сохранён")

    if stopper.should_stop:
        print(f"ранняя остановка на эпохе {epoch}; лучший AUC {stopper.best:.4f}")
        break

# ВАЖНО: после цикла в памяти лежит модель последней (не лучшей) эпохи
load_checkpoint(ckpt_path, model=model)
```

**Объяснение — четыре детали, которые отличают рабочий код от учебного.**

**Последняя строка.** После ранней остановки в памяти находится модель **последней**
эпохи, которая по определению хуже лучшей — иначе остановки бы не было. Забыть загрузить
лучший чекпоинт — очень частая ошибка, и она даёт систематически заниженное качество
на тесте.

**`min_delta`.** Без него шум четвёртого знака валидационной метрики будет считаться
улучшением, счётчик терпения обнуляться, и ранняя остановка никогда не сработает.

**Атомарная запись.** `torch.save` в тот же файл, который читается или уже существует,
при падении процесса (OOM, прерывание по таймауту в кластере) оставляет обрезанный файл.
Запись во временный файл и `replace` решают это одной строкой.

**Что кладём в чекпоинт.** Для **инференса** достаточно `model.state_dict()`.
Для **продолжения обучения** нужны ещё состояние оптимизатора (моменты Adam),
состояние планировщика (номер шага), состояние `GradScaler` и номер эпохи. Без моментов
Adam дообучение после перезапуска даёт заметный провал качества на первых шагах —
классический симптом «после рестарта лосс подскочил».

**Про early stopping как регуляризацию.** Ранняя остановка — это форма регуляризации,
и как всякая регуляризация она использует валидацию для выбора модели. Следствие:
метрика на этой же валидации становится **смещённой оценкой** качества. Если по ней же
подбирались гиперпараметры, для честного числа нужен отдельный тестовый набор.
См. [валидация и утечки](../02-classic-ml/13-validation-and-leakage.md).

---

## 14. Задача 13. Собрать всё вместе

**Постановка.** Напишите обучающий цикл, который объединяет всё из предыдущих задач:
AMP, накопление градиентов, клиппинг, early stopping, чекпоинты, воспроизводимость,
корректный подсчёт метрик. Это финальный «эталон», к которому стоит сводить любой
свой проект.

```python
from pathlib import Path
import torch
import torch.nn as nn


def train(
    model: nn.Module,
    train_loader,
    val_loader,
    criterion,          # с reduction='mean' — для обучения
    criterion_sum,      # тот же лосс с reduction='sum' — для честного среднего на валидации
    optimizer,
    scheduler,
    device: str,
    *,
    epochs: int = 50,
    accum_steps: int = 1,
    max_grad_norm: float = 1.0,
    amp_dtype: torch.dtype | None = torch.bfloat16,
    ckpt_path: Path = Path("best.pt"),
    log_every: int = 100,
):
    use_amp = amp_dtype is not None and device.startswith("cuda")
    # GradScaler нужен только для fp16; для bf16 он не требуется (см. задачу 10)
    scaler = torch.amp.GradScaler(device, enabled=use_amp and amp_dtype is torch.float16)
    stopper = EarlyStopping(patience=5, mode="min")
    ckpt_path.parent.mkdir(parents=True, exist_ok=True)

    for epoch in range(epochs):
        # ---------- обучение ----------
        model.train()
        optimizer.zero_grad(set_to_none=True)
        # Накапливаем лосс на GPU, чтобы не синхронизироваться каждый шаг
        running = torch.zeros((), device=device)
        n_batches = len(train_loader)

        for step, batch in enumerate(train_loader):
            x = batch["x"].to(device, non_blocking=True)
            y = batch["y"].to(device, non_blocking=True)

            with torch.amp.autocast(device, dtype=amp_dtype, enabled=use_amp):
                loss = criterion(model(x), y)

            scaler.scale(loss / accum_steps).backward()
            running += loss.detach()

            if (step + 1) % accum_steps == 0 or (step + 1) == n_batches:
                scaler.unscale_(optimizer)          # вернуть масштаб перед клиппингом
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
                scaler.step(optimizer)
                scaler.update()
                optimizer.zero_grad(set_to_none=True)
                if scheduler is not None:
                    scheduler.step()

            if step % log_every == 0 and step > 0:
                print(f"epoch {epoch} step {step}: loss {(running / log_every).item():.4f}, "
                      f"lr {optimizer.param_groups[0]['lr']:.2e}")
                running.zero_()

        # ---------- валидация ----------
        model.eval()
        val_loss_sum = torch.zeros((), device=device)
        val_count = 0
        with torch.inference_mode():                 # ни графа, ни лишней памяти
            for batch in val_loader:
                x = batch["x"].to(device, non_blocking=True)
                y = batch["y"].to(device, non_blocking=True)
                with torch.amp.autocast(device, dtype=amp_dtype, enabled=use_amp):
                    # reduction='sum' + деление на общее число объектов: иначе последний
                    # неполный батч получит завышенный вес в среднем по батчам
                    val_loss_sum += criterion_sum(model(x), y)
                val_count += y.numel()
        val_loss = (val_loss_sum / max(val_count, 1)).item()
        print(f"epoch {epoch}: val_loss {val_loss:.4f}")

        # ---------- чекпоинт и остановка ----------
        if stopper.step(val_loss):
            save_checkpoint(ckpt_path, model=model, optimizer=optimizer,
                            scheduler=scheduler, epoch=epoch,
                            best_metric=val_loss, scaler=scaler)
        if stopper.should_stop:
            print(f"ранняя остановка на эпохе {epoch}")
            break

    load_checkpoint(ckpt_path, model=model)          # вернуть лучшие веса
    return model, stopper.best
```

**Что здесь стоит заметить, кроме собранных ранее приёмов.**

**Усреднение валидационного лосса.** `sum` по объектам с делением на общее число,
а не среднее по батчам. При `drop_last=False` последний батч меньше остальных,
и «среднее средних» даёт систематическую ошибку. На маленьких валидациях расхождение
достигает нескольких процентов — достаточно, чтобы принять неверное решение
о лучшем чекпоинте.

**`model.train()` / `model.eval()`.** Переключают поведение Dropout (в eval выключается)
и BatchNorm (в eval использует накопленные скользящие статистики вместо статистики батча).
Забыть `model.eval()` перед валидацией — классика: метрика получится хуже и шумнее,
и вы будете искать проблему в модели. Забыть `model.train()` обратно — ещё хуже: Dropout
не работает, модель переобучается, а вы не понимаете почему.

**`inference_mode` вместо `no_grad`.** Строже: помимо отключения графа запрещает
изменение version counter тензоров, что даёт чуть больше оптимизаций. Ограничение:
тензоры, созданные внутри `inference_mode`, нельзя потом использовать в autograd —
для валидации это не мешает.

---

## 15. Подводные камни

**Модель обучается, но часть слоёв — нет.**
Симптом: лосс падает, но некоторые слои не меняются; `len(list(model.parameters()))`
меньше ожидаемого.
Причина: подмодули собраны в обычный список Python вместо `nn.ModuleList`,
либо оптимизатор создан до добавления слоёв.
Что делать: `nn.ModuleList`/`nn.ModuleDict`; проверять
`sum(p.numel() for p in model.parameters())` против аналитического расчёта;
создавать оптимизатор **после** полной сборки модели и после `.to(device)`.

**После `model.to(device)` падает с device mismatch.**
Симптом: `Expected all tensors to be on the same device`.
Причина: тензор создан внутри `forward` без `device=` (например,
`torch.arange(L)`), или он был присвоен как обычный атрибут, а не буфер.
Что делать: создавать тензоры как `torch.arange(L, device=x.device)`;
константы регистрировать через `register_buffer`.

**Лосс не падает вообще, с любым learning rate.**
Симптом: метрика на уровне случайного угадывания.
Причина: не вызывается `optimizer.step()`; оптимизатор создан на копии параметров;
градиенты обнуляются после `backward`, а не до; `requires_grad=False` на всех параметрах;
перепутаны оси в лоссе.
Что делать: диагностический тест «переобучись на одном батче» — рабочая модель должна
довести лосс почти до нуля на 32 примерах за сотню шагов. Если не может — баг в коде,
а не в гиперпараметрах. Это первое, что надо запускать.

**Валидационный лосс лучше обучающего.**
Симптом: `val_loss < train_loss` стабильно.
Причина: Dropout активен на обучении и выключен на валидации (это нормально
и часто объясняет разрыв целиком); либо валидация проще; либо утечка.
Что делать: сравнить обучающий лосс, посчитанный в `eval`-режиме, с валидационным.
Если разрыв исчез — всё в порядке.

**Метрика после рестарта из чекпоинта подскочила.**
Симптом: лосс прыгнул вверх на первых шагах после загрузки.
Причина: не восстановлено состояние оптимизатора (моменты Adam) и/или планировщика.
Что делать: сохранять и загружать `optimizer.state_dict()` и `scheduler.state_dict()`.

**`num_workers > 0` замедляет вместо ускорения.**
Симптом: с воркерами эпоха дольше, чем без них.
Причина: `Dataset` слишком лёгкий (накладные расходы на IPC больше выигрыша);
данные уже в памяти как тензоры; воркеры конкурируют за CPU с основным процессом
(при `torch.set_num_threads` по умолчанию).
Что делать: измерять; для in-memory тензоров использовать `num_workers=0`
и батчевую индексацию.

**`torch.compile` дал замедление.**
Симптом: первые шаги очень долгие, дальше выигрыша нет.
Причина: динамические формы вызывают перекомпиляцию на каждой новой длине;
graph breaks из-за питоновской логики в `forward` (`if` по значению тензора, `.item()`).
Что делать: `TORCH_LOGS="recompiles,graph_breaks"` для диагностики; bucketing длин;
убрать зависимости от значений тензоров в графе.

**Обучение идёт, GPU загружен на 100%, но эпоха всё равно медленная.**
Симптом: `nvidia-smi` показывает полную загрузку.
Причина: утилизация в `nvidia-smi` — это доля времени, когда на GPU есть хоть одно ядро,
а не эффективность. Множество мелких ядер даёт 100% при почти нулевой полезной работе.
Что делать: профайлер и метрика «объектов в секунду»; увеличить батч; проверить,
не считается ли что-то поэлементно в цикле Python.

**Разные результаты при одинаковом seed.**
Симптом: два запуска расходятся.
Причина: недетерминированные CUDA-ядра, `cudnn.benchmark=True`, аугментации в воркерах
без `worker_init_fn`, порядок файлов из `os.listdir` (он не сортирован).
Что делать: см. задачу 11; отдельно — всегда сортировать списки файлов.

---

## 16. Проверь себя

<details>
<summary><b>🌱 Вопрос.</b> Что делает <code>optimizer.zero_grad()</code> и что будет, если его не вызвать?</summary>

**Короткий ответ.** Обнуляет (или, с `set_to_none=True`, освобождает) поле `.grad`
у параметров. Без него градиенты накапливаются между шагами, и оптимизатор двигается
по сумме градиентов всех предыдущих батчей.

**Развёрнуто.** Накопление — сознательное решение авторов PyTorch: на нём построены
градиентное накопление и обучение с несколькими лоссами по одному графу. Плата —
обязанность обнулять вручную. `set_to_none=True` (дефолт с PyTorch 2.0) не заполняет
тензор нулями, а ставит `None`: это экономит память и один проход по всем градиентам,
но меняет поведение — оптимизаторы с momentum не будут обновлять параметр, у которого
градиент `None`, тогда как при нулевом градиенте momentum продолжал бы двигать веса.
Ошибка не вызывается: обучение просто расходится или встаёт, причём не сразу.

**Чего ждёт интервьюер:** знания, что ошибки не будет, и понимания, зачем накопление
вообще существует.

**Провал:** «упадёт с исключением».
</details>

<details>
<summary><b>🎯 Вопрос.</b> Чем <code>nn.Parameter</code> отличается от буфера и от обычного тензора-атрибута?</summary>

**Короткий ответ.** `nn.Parameter` обучается, попадает в `parameters()`, `state_dict()`
и переезжает на устройство. Буфер (`register_buffer`) не обучается, но тоже в `state_dict()`
и тоже переезжает. Обычный тензор-атрибут не делает ничего из этого.

**Развёрнуто.** `nn.Module.__setattr__` перехватывает присваивание: `nn.Parameter` кладётся
в `_parameters`, зарегистрированные буферы — в `_buffers`, вложенные модули — в `_modules`.
Именно из этих словарей строятся `parameters()`, `buffers()`, `state_dict()` и рекурсивный
`.to(device)`. Обычный тензор останется на CPU после `model.cuda()` и даст ошибку
device mismatch. Буферы нужны для необучаемых состояний: `running_mean` в BatchNorm,
causal-маски, кэш RoPE. `persistent=False` исключает буфер из `state_dict()` — для
вычислимых кэшей, которые не надо хранить в файле весов.

**Чего ждёт интервьюер:** понимания механики регистрации, а не заученных названий.

**Провал:** «`Parameter` — это тензор с `requires_grad=True`» — верно, но не объясняет,
почему обычный тензор с `requires_grad=True` не обучается моделью.
</details>

<details>
<summary><b>🎯 Вопрос.</b> Почему в attention делят на квадратный корень из <code>d_k</code>?</summary>

**Короткий ответ.** Чтобы дисперсия скалярных произведений не росла с размерностью.
При независимых компонентах с единичной дисперсией $q^\top k$ имеет дисперсию $d_k$;
softmax от значений разброса $\pm\sqrt{d_k}$ насыщается, и градиент по всем позициям,
кроме максимальной, становится экспоненциально малым.

**Развёрнуто.** $q^\top k = \sum_{i=1}^{d_k} q_i k_i$ — сумма $d_k$ независимых слагаемых
с дисперсией 1, значит, дисперсия суммы равна $d_k$, а стандартное отклонение $\sqrt{d_k}$.
При $d_k = 64$ это разброс порядка 8; softmax при таком разбросе почти one-hot, производная
softmax в зоне насыщения близка к нулю, и градиент не течёт. Деление возвращает дисперсию
к 1 и держит softmax в рабочей зоне. Тонкость: критично это прежде всего при инициализации —
обученная сеть может частично компенсировать масштаб нормой весов, но без нормировки
она до этого состояния не доучится.

**Чего ждёт интервьюер:** вывода через дисперсию, а не фразы «для стабильности».

**Провал:** «чтобы значения были маленькими».
</details>

<details>
<summary><b>🧠 Вопрос.</b> Почему функции потерь в PyTorch принимают логиты, а не вероятности?</summary>

**Короткий ответ.** Численная устойчивость: объединённая операция
`log_softmax`/`log_sigmoid` внутри лосса использует log-sum-exp с вычитанием максимума
и остаётся конечной при любых входах, тогда как `log(softmax(x))` даёт `-inf` при нулевой
вероятности.

**Развёрнуто.** `exp` переполняется в fp32 при аргументе больше ~88, а `softmax` от больших
логитов даёт машинный ноль для неглавных классов; `log(0) = -inf`, дальше `inf - inf = NaN`
в градиенте. Приём log-sum-exp: $\log \sum_i e^{z_i} = m + \log \sum_i e^{z_i - m}$,
где $m = \max_i z_i$ — все экспоненты не превышают 1. Практическое следствие: пишем
`nn.CrossEntropyLoss` от логитов (не от softmax),
`F.binary_cross_entropy_with_logits` (не `binary_cross_entropy(sigmoid(x))`),
и в собственных лоссах тоже начинаем с логитов. Симптом нарушения — NaN появляется
не сразу, а после того, как модель стала уверенной.

**Чего ждёт интервьюер:** что вы понимаете, откуда берётся NaN, и что это не «магия
фреймворка».

**Провал:** «так удобнее» или «чтобы не писать softmax дважды».
</details>

<details>
<summary><b>🎯 Вопрос.</b> Как обучать на последовательностях разной длины?</summary>

**Короткий ответ.** Паддинг до максимума внутри батча плюс маска, которая пробрасывается
в attention, пулинг и лосс. Дополнительно — bucketing по длине, чтобы уменьшить долю паддинга.

**Развёрнуто.** Дефолтный коллатор падает на разных длинах, поэтому пишем свой `collate_fn`
с `pad_sequence`. Маска обязательна: без неё mean pooling делит на `L_max` вместо реальной
длины, attention смотрит на `<pad>`, лосс учитывает паддинг как класс. В лоссе паддинг
убирается через `ignore_index`. Паддинг до максимума **в батче**, а не в датасете:
attention квадратичен по длине, и разница в скорости достигает нескольких раз.
Bucketing (батчи из примеров близкой длины) даёт ещё выигрыш, но требует двойного
перемешивания, иначе градиентные шаги окажутся скоррелированы с длиной. Для RNN есть
`pack_padded_sequence`, который вообще не тратит вычисления на паддинг.

**Чего ждёт интервьюер:** маску. Кандидаты про паддинг говорят все, про последствия
для пулинга — единицы.

**Провал:** «дополню нулями до фиксированной длины».
</details>

<details>
<summary><b>🧠 Вопрос.</b> Обучение упало с NaN на 800-м шаге. Ваш протокол?</summary>

**Короткий ответ.** Воспроизвести и локализовать шаг → проверить входные данные
на NaN/inf → сверить лосс первого шага с теоретическим → `detect_anomaly` и хуки
для локализации слоя → посмотреть историю нормы градиента → проверить свои формулы
на `log(0)`/деление/`sqrt(0)` → проверить маски → проверить, не fp16 ли это.

**Развёрнуто.** Порядок важен: данные — самая частая причина, и проверять их дешевле всего.
Появление NaN не сразу, а после падения лосса, указывает на `log(0)` в самописном лоссе
на уверенных предсказаниях. NaN на отдельных батчах — на полностью замаскированную строку
в softmax или пустую последовательность. Плавный экспоненциальный рост нормы градиента
до взрыва — на слишком высокий LR и отсутствие warmup, лечится `clip_grad_norm_`.
NaN только в fp16 при работающем fp32 — переполнение диапазона (максимум fp16 — 65504),
лечится переходом на bf16. Отдельно: `torch.autograd.detect_anomaly()` замедляет в разы,
поэтому только для отладки.

**Чего ждёт интервьюер:** структурированного протокола. Это вопрос про инженерную зрелость,
а не про знание PyTorch.

**Провал:** «уменьшу learning rate».
</details>

<details>
<summary><b>🎯 Вопрос.</b> Память на GPU растёт от шага к шагу. Где искать?</summary>

**Короткий ответ.** Первым делом — накопление тензоров с графом: `losses.append(loss)`
вместо `loss.item()`, сбор предсказаний без `detach()`/`.cpu()`, валидация без
`torch.no_grad()`. Дальше — `retain_graph=True`, незакрытые хуки, рост длин
последовательностей, фрагментация аллокатора.

**Развёрнуто.** Ссылка на тензор, связанный с графом, удерживает весь граф этого шага
вместе с сохранёнными активациями. Диагностика: логировать
`torch.cuda.memory_allocated()` и `memory_reserved()`; если растёт `allocated` — это
настоящая утечка, если только `reserved` — фрагментация. Точную картину даёт
`torch.cuda.memory._record_memory_history()` со снимком, который открывается
в визуализаторе памяти PyTorch. `torch.cuda.empty_cache()` утечку не чинит: он снижает
`reserved`, но не `allocated`, и в цикле обучения только замедляет работу.

**Чего ждёт интервьюер:** знания, что тензор с графом держит активации, и различия
allocated/reserved.

**Провал:** «добавлю `empty_cache()`».
</details>

<details>
<summary><b>🎯 Вопрос.</b> Чем градиентное накопление отличается от обучения с большим батчем?</summary>

**Короткий ответ.** По градиенту это то же самое (при одинаковых микробатчах и делении
лосса на число шагов накопления). Отличия — в слоях со статистикой батча (BatchNorm),
в in-batch negatives, и в том, что скорости накопление не даёт: экономится только память.

**Развёрнуто.** Равенство $\frac{1}{N}\sum \nabla \ell_i = \frac{1}{k}\sum_j \left(\frac{1}{m}\sum_{i \in B_j}\nabla \ell_i\right)$ выполняется при $N = km$ и равных
микробатчах, отсюда `drop_last=True` и деление `loss / accum_steps` (без деления
эффективный LR вырастет в $k$ раз). BatchNorm считает статистику по микробатчу — результат
отличается; лечится заменой на LayerNorm/GroupNorm. Для контрастивного обучения негативы
берутся внутри микробатча, поэтому «эффективный батч 256» даёт качество батча 32 —
частая и незамеченная потеря. В DDP на промежуточных микробатчах надо оборачивать
backward в `model.no_sync()`, иначе будет лишний all-reduce на каждом.

**Чего ждёт интервьюер:** списка того, что НЕ эквивалентно. Про эквивалентность
градиента говорят все.

**Провал:** «это способ ускорить обучение».
</details>

<details>
<summary><b>🧠 Вопрос.</b> Зачем нужен GradScaler и когда он не нужен?</summary>

**Короткий ответ.** Он компенсирует узкий диапазон fp16: умножает лосс на большой
коэффициент, чтобы малые градиенты не обнулились в денормалях, и снимает масштаб перед
шагом оптимизатора. Для bf16 не нужен — у него тот же диапазон экспоненты, что у fp32.

**Развёрнуто.** У fp16 5 бит экспоненты, наименьшее нормальное число ≈ 6e-5; градиенты
порядка 1e-8 обнуляются, и слой молча перестаёт обучаться. `GradScaler` умножает лосс
на $S$ (старт $2^{16}$), проверяет градиенты на `inf`/`NaN` перед шагом: при переполнении
шаг **пропускается**, а $S$ уменьшается вдвое; после серии успешных шагов $S$ растёт.
Отсюда: несколько пропущенных шагов в начале — нормальное поведение. Важные детали
использования: `unscale_(optimizer)` перед клиппингом (иначе `max_norm` применяется
к раздутым градиентам), внутри `autocast` — только forward и лосс, шаг оптимизатора
и backward снаружи. bf16 требует Ampere и новее; на V100 остаётся только fp16 со скейлером.

**Чего ждёт интервьюер:** понимания, что проблема в диапазоне, а не в точности,
и знания различия fp16/bf16.

**Провал:** «он ускоряет обучение».
</details>

<details>
<summary><b>🎯 Вопрос.</b> Как сделать обучение воспроизводимым и где предел?</summary>

**Короткий ответ.** Зафиксировать seed для `random`, `numpy`, `torch` (CPU и CUDA),
задать `generator` и `worker_init_fn` для DataLoader, включить
`torch.use_deterministic_algorithms(True)`, `cudnn.deterministic=True`,
`cudnn.benchmark=False` и `CUBLAS_WORKSPACE_CONFIG`. Предел — разное железо и версии
библиотек: там детерминизма не бывает.

**Развёрнуто.** Причина фундаментальна: сложение float неассоциативно, а атомарные
операции на GPU (`scatter_add`, backward у `Embedding` с повторами) складывают
в непредсказуемом порядке. Разные GPU используют разные ядра, TF32 включается по-разному,
NCCL не гарантирует порядок редукции. Поэтому воспроизводимость эксперимента — это
не только seed, но и зафиксированное окружение (образ, версии, тип карты). Практический
вывод для отчётов: запускать 3–5 seed'ов и указывать среднее и разброс; улучшение меньше
межзапускного разброса улучшением не является.

**Чего ждёт интервьюер:** и списка мер, и честного «полного детерминизма не бывает».

**Провал:** `torch.manual_seed(42)` как исчерпывающий ответ.
</details>

<details>
<summary><b>🌱 Вопрос.</b> Что делают <code>model.train()</code> и <code>model.eval()</code>?</summary>

**Короткий ответ.** Переключают флаг `training` у всех подмодулей. Это меняет поведение
Dropout (в eval отключается) и BatchNorm (в eval использует накопленные скользящие
статистики вместо статистики текущего батча). На вычисление градиентов они не влияют.

**Развёрнуто.** Частая путаница: `model.eval()` и `torch.no_grad()` — про разное.
Первое меняет **поведение слоёв**, второе отключает **построение графа**. На валидации
нужны оба. Симптомы ошибок: забыли `eval()` — метрика хуже и шумнее (Dropout активен,
BatchNorm считает статистику по валидационному батчу, что вдобавок является утечкой
информации между объектами батча); забыли вернуть `train()` — Dropout не работает,
модель переобучается. Отдельная тонкость: при батче размера 1 BatchNorm в режиме
`train` падает или даёт нули дисперсии.

**Чего ждёт интервьюер:** различия между `eval()` и `no_grad()`.

**Провал:** «`eval()` отключает градиенты».
</details>

<details>
<summary><b>🧠 Вопрос.</b> Как быстро проверить, что в обучающем коде нет бага?</summary>

**Короткий ответ.** Переобучиться на одном батче: взять 16–32 примера и обучаться
только на них. Рабочий код доводит лосс почти до нуля за сотню шагов. Если не может —
баг в коде, а не в гиперпараметрах.

**Развёрнуто.** Тест ловит почти весь класс «модель не учится»: отсутствующий
`optimizer.step()`, оптимизатор на чужих параметрах, перепутанные оси в лоссе,
неправильные метки, замороженные веса, обнуление градиентов после `backward`, ошибку
в маске. Второй по полезности тест — сверка лосса первого шага с теоретическим
($\ln K$ для $K$ классов). Третий — проверка форм на каждом шаге через `assert`.
Все три занимают минуты и экономят дни. В регрессионном виде эти проверки стоит
держать в тестах — см. [следующую главу](07-testing-and-code-quality.md).

**Чего ждёт интервьюер:** что у вас есть инженерная привычка проверять код, а не
крутить learning rate.

**Провал:** «запущу на всём датасете и посмотрю на графики».
</details>

---

## 17. Практика

**Задача 1. Слой и его тест (40 минут).**
Реализуйте с нуля SwiGLU-блок FFN: $\mathrm{SwiGLU}(x) = \big(\mathrm{SiLU}(xW_1) \odot xW_3\big)W_2$,
где $W_1, W_3 \in \mathbb{R}^{d \times h}$, $W_2 \in \mathbb{R}^{h \times d}$, $\odot$ —
поэлементное произведение, $h$ — скрытая размерность. Напишите тесты на форму,
на регистрацию параметров, на наличие градиента и на число параметров.
*Сделано правильно: `sum(p.numel() ...)` совпадает с вашим аналитическим расчётом
$3dh$; тесты падают, если убрать `super().__init__()` или заменить `nn.Parameter`
на тензор.*

**Задача 2. Коллатор с bucketing (1 час).**
Возьмите любой корпус, сгенерируйте распределение длин с тяжёлым хвостом (например,
логнормальное) и сравните три стратегии: паддинг до фиксированной длины,
паддинг до максимума в батче, bucketing.
*Сделано правильно: у вас есть таблица «стратегия → средняя доля паддинга → время эпохи».
Bucketing даёт минимум вдвое меньше паддинга, и вы можете назвать, чем за это платите.*

**Задача 3. Focal loss против взвешенной BCE (1 час).**
Сгенерируйте бинарную задачу с дисбалансом 1:200. Обучите одну модель с BCE,
вторую с `pos_weight`, третью с focal loss. Сравните PR-AUC, ROC-AUC и калибровку
(reliability diagram).
*Сделано правильно: вы видите, что focal loss и `pos_weight` дают близкий PR-AUC,
но focal loss заметно хуже калиброван, и можете объяснить почему.*

**Задача 4. Attention и его сверка (1 час).**
Реализуйте MHA из §5 и напишите четыре теста: сверка с `F.scaled_dot_product_attention`,
проверка каузальности «от противного», проверка, что паддинг не влияет на выход
валидных позиций, проверка отсутствия NaN при полностью замаскированной строке.
*Сделано правильно: все четыре теста проходят, и вы можете сломать реализацию
(перепутать `tril`/`triu`, убрать `contiguous`, поставить `-inf`) так, что падает
ровно ожидаемый тест.*

**Задача 5. Бюджет памяти (45 минут).**
Для модели с $L = 24$, $d = 1024$, $V = 32000$, $s = 2048$ посчитайте на бумаге
число параметров и память для обучения с AdamW в fp32 и в AMP. Затем измерьте
реальное потребление и сравните.
*Сделано правильно: расхождение расчёта и замера не больше 30%, и вы можете объяснить,
куда ушла разница (активации, фрагментация, временные буферы).*

**Задача 6. Сломай и почини (1.5 часа).**
Возьмите рабочий обучающий цикл и внесите по одному пять багов из списка:
`losses.append(loss)` без `.item()`; отсутствующий `optimizer.zero_grad()`;
`log(sigmoid(x))` вместо `_with_logits`; забытый `model.eval()`; список слоёв
вместо `nn.ModuleList`. Для каждого зафиксируйте симптом и время, за которое
вы его нашли.
*Сделано правильно: у вас есть таблица «баг → симптом → способ обнаружения»,
и по симптому вы теперь опознаёте баг за минуты.*

**Задача 7. Ускорение (1.5 часа).**
Возьмите заведомо медленный цикл (`num_workers=0`, fp32, `.item()` каждый шаг,
маленький батч) и ускорьте его минимум в 3 раза, применяя меры по одной
и замеряя после каждой.
*Сделано правильно: у вас есть график «мера → objects/sec», вы знаете вклад каждой
и можете назвать, какая мера дала больше всего в вашем случае и почему.*

---

## 18. Что читать дальше

- [Официальный туториал PyTorch: `torch.autograd`](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html) —
  как строится и уничтожается граф; читать перед задачей об утечках памяти.
- [Документация: `torch.amp` и рецепты смешанной точности](https://pytorch.org/docs/stable/amp.html) —
  список операций, которые autocast оставляет в fp32, и правила использования `GradScaler`.
  Самая полезная страница по задаче 10.
- [Документация: воспроизводимость](https://pytorch.org/docs/stable/notes/randomness.html) —
  исчерпывающий список источников недетерминизма и способов их подавить.
- [Документация: управление CUDA-памятью](https://pytorch.org/docs/stable/notes/cuda.html#memory-management) —
  кэширующий аллокатор, `PYTORCH_CUDA_ALLOC_CONF`, разница allocated/reserved.
- [`torch.profiler`: рецепт](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) —
  как читать вывод профайлера и находить узкое место.
- [Lin et al. «Focal Loss for Dense Object Detection» (ICCV 2017)](https://arxiv.org/abs/1708.02002) —
  оригинал focal loss с обоснованием выбора $\gamma$ и $\alpha$ и с разбором,
  почему инициализация смещения последнего слоя важна при сильном дисбалансе.
- [Vaswani et al. «Attention Is All You Need» (NeurIPS 2017)](https://arxiv.org/abs/1706.03762) —
  первоисточник attention; сверяйте свою реализацию с формулами из §3.2.
- [Zhang & Sennrich. «Root Mean Square Layer Normalization» (NeurIPS 2019)](https://arxiv.org/abs/1910.07467) —
  RMSNorm из задачи 1, с экспериментальным обоснованием отказа от центрирования.
- [Micikevicius et al. «Mixed Precision Training» (ICLR 2018)](https://arxiv.org/abs/1710.03740) —
  откуда взялся loss scaling и почему нужна мастер-копия весов в fp32.
- [Andrej Karpathy. «A Recipe for Training Neural Networks»](https://karpathy.github.io/2019/04/25/recipe/) —
  лучший текст про методику отладки обучения; тест «переобучись на одном батче»
  и порядок действий взяты оттуда.
- Продолжение в хендбуке: [PyTorch на практике](../03-deep-learning/05-pytorch-in-practice.md) —
  систематически про autograd и DataLoader; [масштабирование обучения](../03-deep-learning/06-scaling-and-efficiency.md) —
  DDP, FSDP, gradient checkpointing; [тесты и качество кода](07-testing-and-code-quality.md) —
  как превратить проверки из этой главы в регрессионные тесты.

---

⬅️ [SQL: тренировка](05-sql-drills.md) | 🏠 [Оглавление](../index.md) | ➡️ [Тесты и качество кода в ML](07-testing-and-code-quality.md)
