# Приёмы подачи из эталонных технических текстов

Разбор семи источников, которые считаются эталоном объяснения. Цель — не оценка «хорошо/плохо»,
а извлечение **конкретных переносимых приёмов**: как устроена глава, чем открывается тема, как
подаются формулы, где стоят задачи, как сделана навигация, как показывают ошибки.

Дата сбора: 2026-07-27.

---

## Легенда достоверности

| Маркер | Значение |
|---|---|
| **[ВИДЕЛ]** | Я открыл первоисточник (исходники книги, PDF, репозиторий) и прочитал конкретный текст. Приведённые цитаты и числа получены прямым измерением. |
| **[ПО ОТЗЫВАМ]** | Первоисточник недоступен; сведения из поисковой выдачи, обзоров, вторичных описаний. Формулировки могут быть неточны. |
| **[НЕ УДАЛОСЬ]** | Достать не получилось. Ничего не додумываю. |

### Что удалось достать и как

| Источник | Доступ | Что именно читал |
|---|---|---|
| d2l.ai | **[ВИДЕЛ]** | `d2l.ai` отдаёт 403. Взял **исходники книги** — `github.com/d2l-ai/d2l-en`, полный `git clone`. Книга пишется в markdown, это лучше рендера. Прочитал `chapter_linear-regression/linear-regression.md` (760 строк), `chapter_multilayer-perceptrons/mlp.md`, `chapter_preface/index.md`, плюс исходник тулчейна `d2l-ai/d2l-book`. |
| Understanding Deep Learning (Prince) | **[ВИДЕЛ]** | Скачал официальный PDF 5-го издания (541 стр., release v5.0.3) + репозиторий `udlbook/udlbook` (ноутбуки, `UDL_Equations.tex`, `PDFFigures`, `UDL_Answer_Booklet_Students.pdf`). Читал главы 3–4 постранично, извлекал текст и координаты блоков. |
| Distill.pub | **[ВИДЕЛ]** | `distill.pub` заблокирован egress-политикой. Взял **исходный HTML статей** из их репозиториев: `distillpub/post--research-debt`, `distillpub/post--momentum`. Это ровно тот текст, что на сайте. |
| 3Blue1Brown | **[ВИДЕЛ]** (текстовые версии) | `3blue1brown.com` заблокирован. Взял `github.com/3b1b/3Blue1Brown.com` — сайт хранит уроки как MDX. Читал `app/pages/lessons/2017/neural-networks/index.mdx` (441 строка) целиком, с компонентами. **[ПО ОТЗЫВАМ]** — общая метода Гранта (порядок «конкретное → абстрактное») по вторичным источникам. |
| ESL / ISLR | **[ВИДЕЛ]** | Оба PDF достал через LFS-зеркала на GitHub. ISLR v2 — 612 стр., ESL 2-е изд. — 764 стр. Читал предисловия, оглавления, главу 3 обеих книг, разделы упражнений. |
| The Missing Semester (MIT) | **[ВИДЕЛ]** | `github.com/missing-semester/missing-semester`, `_2020/course-shell.md` — полный текст лекции 1 с упражнениями. |
| Хендбуки Яндекса | **[ВИДЕЛ]** (ML-учебник ШАД) / **[НЕ УДАЛОСЬ]** (education.yandex.ru) | `education.yandex.ru` и `habr.com` заблокированы egress-политикой, и `ml-handbook.ru` не резолвится. **Но** нашёл исходники ML-учебника ШАД на GitLab: `gitlab.com/yandexdataschool/ml-handbook` — 26 файлов глав, 1.16 МБ markdown, плюс Jekyll-шаблоны. Это первоисточник. Хендбук по **алгоритмам** и хендбук по **математике** достать не удалось — там ниже только `[ПО ОТЗЫВАМ]`. |

**Важно про блокировки.** Домены `education.yandex.ru`, `habr.com`, `distill.pub`, `3blue1brown.com`,
`d2l.ai`, `statlearning.com`, `web.archive.org` закрыты egress-политикой организации (403 на CONNECT).
Я не обходил политику — я шёл к первоисточникам (репозитории авторов, официальные PDF-релизы),
которые содержат тот же контент и открыты.

---

## 1. Dive into Deep Learning (d2l.ai)

Связка «формула ↔ исполняемый код», упражнения, обсуждения.

### Измеренные факты [ВИДЕЛ]

Полный клон `d2l-en`, 165 содержательных файлов-разделов (без `index.md`):

| Элемент | Покрытие |
|---|---|
| `## Summary` в конце раздела | 151 / 165 (92%) |
| `## Exercises` в конце раздела | 158 / 165 (96%) |
| Ссылка на форум `discuss.d2l.ai` | 162 / 165 (98%) |
| `:numref:` — перекрёстные ссылки | 894 употребления (≈5.4 на раздел) |
| `:cite:` — ссылки на литературу | 480 |
| `:eqlabel:` — именованные формулы | 130 |

### Приёмы

**1.1. Раздел открывается не определением, а перечнем задач, где это встречается.**

Дословное начало главы про линейную регрессию:

> *Regression* problems pop up whenever we want to predict a numerical value. Common examples
> include predicting prices (of homes, stocks, etc.), predicting the length of stay (for patients
> in the hospital), forecasting demand (for retail sales), among numerous others.
> **Not every prediction problem is one of classical regression.**

Дальше сразу вводится **сквозной пример** («оценить цену дома по площади и возрасту»), и на нём же
вводится вся терминология: training set, example, label, feature.

- **Делают X** → первые 2 абзаца это (а) список реальных ситуаций, (б) явная граница «а вот это сюда
  не относится», (в) один конкретный пример, который тянется через всю главу.
- **Эффект Y** → читатель до первой формулы знает, зачем она, и весь остальной текст цепляется за
  один образ, а не за десяток разрозненных иллюстраций.
- **Перенос** → жёсткое правило: **до первой формулы — минимум 3 конкретных применения и один
  сквозной пример, который переиспользуется во всех последующих секциях главы**. Плюс отдельная
  фраза «а вот это НЕ про то» — она экономит читателю ложные ожидания.

**1.2. Новая тема открывается разбором того, почему предыдущая ломается.**

Глава про MLP начинается не с MLP, а с секции `### Limitations of Linear Models`. Там три примера
нарастающей тяжести: (1) доход → вероятность возврата кредита — монотонно, но не линейно, чинится
логит-преобразованием; (2) температура тела → риск — немонотонно, чинится признаком `|t - 37|`;
(3) картинки кошек и собак — **и тут починить препроцессингом уже нельзя**:

> Reliance on a linear model corresponds to the implicit assumption that the only requirement for
> differentiating cats and dogs is to assess the brightness of individual pixels. This approach is
> doomed to fail in a world where inverting an image preserves the category.

- **Делают X** → лестница из 3 контрпримеров, где первые два **чинятся** известными средствами, а
  третий принципиально нет.
- **Эффект Y** → новая сущность вводится как вынужденная, а не как «а ещё бывает вот такое».
  Читатель сам приходит к необходимости скрытого слоя.
- **Перенос** → шаблон открытия главы: `Что мы уже умеем → пример, где это чинится костылём →
  пример, где костыль не помогает → значит, нужен новый инструмент`. Три примера, не один.

**1.3. Демонстрация вырождения: показывают, что наивная конструкция ничего не даёт.**

После введения скрытого слоя честно пишут:

> You might be surprised to find out that---in the model defined above---***we gain nothing for our
> troubles***!

И тут же алгебраически схлопывают два слоя в один: `W = W⁽¹⁾W⁽²⁾`, `b = b⁽¹⁾W⁽²⁾ + b⁽²⁾`. Только
после этого вводится нелинейность.

- **Делают X** → строят очевидную конструкцию, показывают формулой, что она эквивалентна старой,
  и лишь потом добавляют недостающий кусок.
- **Эффект Y** → читатель понимает, **зачем** нужна функция активации, а не просто запоминает, что
  она есть. Это защита от типичной ошибки на собеседовании «а зачем вообще активация?».
- **Перенос** → для каждого нетривиального элемента архитектуры/алгоритма добавлять микро-секцию
  «что будет, если этот элемент убрать» с выкладкой на 3–5 строк. Это самый дешёвый способ сделать
  текст объясняющим, а не описательным.

**1.4. Формула → код → замер → вывод. Именно в таком порядке и с числом в конце.**

Секция `## Vectorization for Speed` не рассказывает, что векторизация быстрее. Она:
1. заявляет тезис,
2. даёт код с `for`-циклом на 10000 элементов и `time.time()`,
3. даёт код с `a + b`,
4. и только потом: «The second method is dramatically faster than the first. Vectorizing code often
   yields **order-of-magnitude speedups**».

Аналогично с ReLU: сначала формула `ReLU(x) = max(x, 0)`, потом код построения графика функции,
потом текст про производную, потом код построения графика производной.

- **Делают X** → каждое утверждение о поведении сопровождается минимальным исполняемым кодом,
  который это утверждение проверяет, и **числом/графиком как результатом**.
- **Эффект Y** → читатель может воспроизвести и не обязан верить на слово. Утверждения становятся
  фальсифицируемыми.
- **Перенос** → правило: **любое количественное утверждение («быстрее», «стабильнее», «хуже
  сходится») сопровождается сниппетом на 5–15 строк, который его измеряет, и явно выписанным
  результатом замера в тексте.** Без сниппета утверждение либо убирается, либо переформулируется
  как ссылка на источник.

**1.5. Один и тот же текст выпускается в четырёх вариантах фреймворка — механикой разметки.**

В исходнике:

```markdown
:begin_tab:`pytorch`
[Discussions](https://discuss.d2l.ai/t/258)
:end_tab:
```

и блоки кода помечены `%%tab pytorch` / `%%tab all`. Читатель на сайте переключает вкладку.

- **Делают X** → вариативная часть (код) изолирована в помеченные блоки, инвариантная (текст,
  математика) написана один раз.
- **Эффект Y** → нет дублирования главы под каждый фреймворк, объяснение не расходится между
  версиями.
- **Перенос** → в mkdocs-material это `pymdownx.tabbed` (уже подключён в `mkdocs.yml`). Использовать
  для пар «PyTorch / TensorFlow», «pandas / polars», «SQL-диалекты». Но — см. раздел про
  непереносимое: на GitHub вкладки не отрендерятся, поэтому **инвариантный текст должен читаться
  без вкладок**.

**1.6. Упражнения — деревом, а не списком. И они выходят за рамки главы.**

Из главы про линейную регрессию (дословно):

> 1. Assume that we have some data $x_1,\ldots,x_n$. Our goal is to find a constant $b$ such that
>    $\sum_i (x_i-b)^2$ is minimized.
>    1. Find an analytic solution for the optimal value of $b$.
>    2. How does this problem and its solution relate to the normal distribution?
>    3. What if we change the loss to $\sum_i |x_i-b|$?

И дальше — задачи, которые тянут в соседние области: пуассоновская регрессия для счётчиков
(«you are selling apples, not oil»), логарифм цены вместо цены, Блэк–Шоулз для пенни-стоков.

- **Делают X** → задача = ствол + 2–4 подпункта, где каждый следующий меняет ровно один параметр
  условия. Плюс явные `Hint:` внутри условия.
- **Эффект Y** → одна задача покрывает целое семейство, читатель видит, от чего зависит ответ.
  Подсказка снижает шанс, что читатель просто бросит.
- **Перенос** → формат задачи в хендбуке: **корневая формулировка + подпункты «а что если…»**.
  Минимум один подпункт должен ломать предпосылку (сменить лосс, убрать условие, сделать данные
  вырожденными). Подсказку писать прямо в условии как `Подсказка: …`.

**1.7. У каждого раздела есть постоянный адрес обсуждения.**

98% разделов заканчиваются ссылкой на конкретную тему форума. Не «наш форум», а **тред именно этого
раздела**.

- **Эффект Y** → вопросы читателей копятся по месту, и следующий читатель их находит. Фактически
  это растущий FAQ, который авторы не пишут.
- **Перенос** → в конец каждой главы — ссылка на **предзаведённый GitHub Discussion / Issue с
  меткой главы**. Ключевое: тред должен существовать заранее, иначе никто его не создаст.

**1.8. Заявленная методика: «just in time» + двойная реализация.**

Из предисловия, дословно:

> In this book, we teach most concepts *just in time*. In other words, you will learn concepts at
> the very moment that they are needed to accomplish some practical end.

> we often present two versions of the example: one where we implement everything from scratch,
> relying only on NumPy-like functionality and automatic differentiation, and a more practical
> example, where we write succinct code using the high-level APIs.

- **Перенос** → (а) не выносить всю теорию в начало — давать ровно тот кусок, что нужен сейчас;
  (б) для базовых механизмов давать **две реализации: «руками, чтобы увидеть» и «как в проде»**, и
  после этого пользоваться только второй.

---

## 2. Understanding Deep Learning (Simon Prince)

Иллюстрации и как они заменяют абзацы текста.

### Измеренные факты [ВИДЕЛ]

PDF 5-го издания, 541 страница:

| Метрика | Значение |
|---|---|
| Уникальных ссылок «Figure N.M» | 276 |
| Уникальных задач «Problem N.M» | 197 |
| Уникальных ноутбуков «Notebook N.M» | 68 |
| Плотность рисунков | ≈0.51 на страницу (**рисунок раз в две страницы**) |

Контракт конца главы (проверено на главах 3 и 4): `N.x Summary` → `Notes` → `Problems` → следующая
глава. В репозитории отдельно лежат: `PDFFigures/` (все рисунки), `Slides/`, `UDL_Equations.tex`
(**все формулы книги отдельным документом**), `UDL_Answer_Booklet_Students.pdf`, `UDL_Errata.pdf`.

### Приёмы

**2.1. Подпись под рисунком — самостоятельный абзац, который можно читать вместо текста.**

Подпись к figure 3.12 целиком (это подпись, не основной текст):

> **Figure 3.12 Terminology.** A shallow network consists of an input layer, a hidden layer, and an
> output layer. Each layer is connected to the next by forward connections (arrows). For this reason,
> these models are referred to as feed-forward networks. When every variable in one layer connects
> to every variable in the next, we call this a fully connected network. Each connection represents
> a slope parameter in the underlying equation, and these parameters are termed weights. The
> variables in the hidden layer are termed neurons or hidden units. The values feeding into the
> hidden units are termed pre-activations, and the values at the hidden units (i.e., after the ReLU
> function is applied) are termed activations.

Вся терминология главы введена **в подписи**. Основной текст после неё добавляет одно предложение.

- **Делают X** → подпись несёт содержание, а не название. Она вводит термины, объясняет обозначения
  и делает вывод.
- **Эффект Y** → читатель, листающий книгу по картинкам, всё равно получает полный смысл. Подписи
  работают как второй, ускоренный проход по материалу.
- **Перенос** → **запретить подписи вида «Рис. 3. Архитектура трансформера».** Формат подписи:
  `**Рис. N. <Заголовок-тезис>.** <2–5 предложений: что на панелях, что означают оси/цвета, какой
  вывод>`. Проверка: если удалить основной текст вокруг и оставить только рисунок с подписью —
  смысл должен сохраниться.

**2.2. Панельная нумерация внутри рисунка: a), b), c) … j).**

В книге встречаются ссылки вида `figure 3.3j`, `figure 3.13a–f`, `figure 4.1a`. Один рисунок
содержит до 10 панелей, и текст адресует **конкретную панель**.

- **Делают X** → вместо 10 отдельных рисунков — один рисунок с 10 панелями и буквенной адресацией.
- **Эффект Y** → можно показать процесс/развёртку (как из трёх ReLU складывается кусочно-линейная
  функция) и ссылаться на любой шаг из любого места книги, включая задачи.
- **Перенос** → в markdown: одна картинка-сетка панелей + подпись, где каждая панель описана
  отдельным пунктом списка. В тексте ссылаться `(рис. 4б)`. Это дешевле, чем 10 картинок, и лучше
  для чтения с телефона.

**2.3. Маргиналии: указатели на задачу / ноутбук / приложение прямо у релевантного абзаца.**

Извлёк по координатам текстовых блоков (ширина страницы 612 pt, блоки на x≈47 и x≈506, то есть в
полях). Реальные примеры маргиналий: `Problems 2.1–2.2`, `Problem 3.18`, `Notebook 7.2
Backpropagation`, `Notebook 10.1 1D convolution`, `Appendix B.1.3 Gamma function`,
`Appendix B.3.7`, `Appendix B.1.2`.

- **Делают X** → в поле напротив абзаца стоит маркер: «здесь есть задача», «здесь есть ноутбук»,
  «если не помнишь гамма-функцию — приложение B.1.3».
- **Эффект Y** → два эффекта сразу. (1) Практика привязана к точке текста, а не свалена в конец.
  (2) **Пробел в подготовке чинится в момент возникновения** — читателю не нужно бросать главу.
- **Перенос** → это самый ценный приём отсюда. В markdown — короткая строка-врезка сразу после
  абзаца:
  ```markdown
  > 📐 Нужна матричная производная? → [01-math/04-matrix-calculus.md](../01-math/04-matrix-calculus.md)
  > ✍️ Проверь себя: задача 3 в конце главы
  > 💻 Код: `code/03-deep-learning/backprop.py`
  ```
  Правило: **на каждый математический факт, который читатель мог забыть, — ссылка на место, где он
  разобран, в том же абзаце.** Не «предполагается знание линейной алгебры» в начале главы.

**2.4. Раздел `Notes`: история и литература вынесены из основного повествования.**

Между `Summary` и `Problems` стоит `Notes` — набор мини-очерков с тематическими подзаголовками:
`"Neural" networks:`, `History of neural networks:`, `Activation functions:`, `Linear, affine, and
nonlinear functions:`. Внутри — плотные ссылки (McCulloch & Pitts 1943, Rosenblatt 1958, Minsky &
Papert 1969, …), обсуждение dying ReLU, перечисление leaky/parametric/concatenated ReLU, GELU, SiLU,
ELU, SELU, Swish, HardSwish с формулой.

Показательно: честный вывод вместо рекомендации —

> There is no definitive answer as to which of these activations functions is empirically superior.

- **Делают X** → основной текст держит одну линию рассуждения; всё «а ещё бывает», «а исторически»,
  «а вот терминологическая тонкость» вынесено в отдельный раздел после Summary.
- **Эффект Y** → основной текст читается быстро и не рвётся, но энциклопедическая полнота не
  теряется. Читатель сам выбирает глубину.
- **Перенос** → секция `## Заметки на полях` перед задачами. Туда: варианты метода, историю,
  терминологические расхождения, «почему в статье X называют это иначе». Формат — подзаголовок
  жирным + абзац. И обязательно оставлять честные «однозначного ответа нет», а не выдумывать
  рекомендацию.

**2.5. Задачи адресуют рисунки и требуют рисовать, а не только считать. Сложные помечены `∗`.**

Дословно:

> **Problem 3.2** For each of the four linear regions in figure 3.3j, indicate which hidden units are
> inactive and which are active.
>
> **Problem 3.4** Draw a version of figure 3.3 where the y-intercept and slope of the third hidden
> unit have changed as in figure 3.14c.
>
> **Problem 3.3∗** Derive expressions for the positions of the "joints" …
>
> **Problem 3.8** … Redraw a version of figure 3.3 for each of these functions. The original
> parameters were: ϕ = {−0.23, −1.3, 1.3, 0.66, −0.2, 0.4, −0.9, 0.9, 1.1, −0.7}.

Заметь: в задаче 3.8 **даны конкретные числа**, чтобы читатель мог реально построить график, а не
рассуждать абстрактно.

- **Делают X** → (а) задача ссылается на рисунок из главы; (б) требует построить/перерисовать;
  (в) даёт конкретные численные параметры; (г) звёздочка = повышенная сложность.
- **Эффект Y** → проверяется понимание картинки, а не умение подставить в формулу. Числа делают
  задачу выполнимой без додумывания.
- **Перенос** → доля задач формата «перерисуй/построй график/что изменится на рисунке, если…» —
  не меньше четверти. Всегда давать конкретные числа. Помечать сложные задачи (`*`), чтобы читатель
  не застревал.

**2.6. Инфраструктурные артефакты книги вынесены отдельными файлами.**

`UDL_Equations.tex` — все формулы книги одним документом, по главам, без текста. `PDFFigures/` — все
рисунки. `UDL_Errata.pdf` — публичный список ошибок. `UDL_Answer_Booklet_Students.pdf` — ответы к
части задач. В шапке каждой страницы PDF: `Draft: please send errata to udlbookmail@gmail.com`.

- **Эффект Y** → формулы можно взять для шпаргалки/слайдов; преподаватели берут рисунки; ошибки
  чинятся публично, а не накапливаются.
- **Перенос** → (а) автогенерируемый `resources/formulas.md` — все формулы хендбука по главам
  (можно собрать скриптом из `$$…$$`); (б) видимая на каждой странице ссылка «нашли ошибку →
  issue»; (в) отдельный файл ответов, а не ответы в тексте.

**2.7. Ноутбуки построены на «предскажи → потом запусти».**

Из `Notebooks/Chap04/4_1_Composing_Networks.ipynb`, дословные ячейки:

```python
# TODO
# Take a piece of paper and draw what you think will happen when we feed the
# output of the first network into the second one.
```
```python
# Now let's see if your predictions were right
```

Так — четыре раза подряд, каждый раз меняя один параметр. Финальная ячейка:

```python
# Take away conclusion:  with very few parameters, we can make A LOT of linear regions, but
# they depend on one another in complex ways that quickly become too difficult to understand intuitively.
```

- **Делают X** → перед каждым запуском требуют записать прогноз. Цикл «прогноз → проверка»
  повторяется, меняя ровно одну переменную. В конце — явный вывод, включая честное «это быстро
  становится слишком сложно для интуиции».
- **Эффект Y** → читатель обнаруживает **разрыв между своей моделью и реальностью**. Пассивное
  чтение кода такого не даёт.
- **Перенос** → в markdown это ложится идеально:
  ```markdown
  **Прогноз.** Что будет с loss, если увеличить lr в 10 раз? Запиши ответ до запуска.

  <details><summary>Что происходит на самом деле</summary>

  … объяснение …
  </details>
  ```
  Правило: **перед каждым нетривиальным экспериментом — требование прогноза.**

---

## 3. Distill.pub

Интерактивные объяснения и почему они работают.

### Приёмы

**3.1. Статья открывается работающей моделью с ползунками — до всякого текста. [ВИДЕЛ]**

В `post--momentum/public/index.html` первый элемент после `<h1>` — `<figure>` с контролами
`Step-size α = 0.02` и `Momentum β = 0.99`. Подпись под ней заканчивается **вопросом**:

> We often think of Momentum as a means of dampening oscillations and speeding up the iterations…
> But it has other interesting behavior. It allows a larger range of step-sizes to be used, and
> creates its own oscillations. **What is going on?**

- **Делают X** → сначала дают потрогать явление и **создают недоумение**, потом объясняют.
- **Эффект Y** → у читателя появляется собственный вопрос. Дальнейший текст воспринимается как
  ответ, а не как изложение.
- **Перенос** → открывать главу коротким воспроизводимым артефактом (10–20 строк кода / готовый
  график) + вопросом «почему так?», ответ на который даётся в середине главы. Не «в этой главе мы
  изучим momentum», а «вот два прогона, отличаются одним числом, результат противоположный — почему?».

**3.2. Народное объяснение проговаривается, а потом ломается. [ВИДЕЛ]**

Дословно:

> Here's a popular story about momentum: gradient descent is a man walking down a hill. He follows
> the steepest path downwards; his progress is slow, but steady. Momentum is a heavy ball rolling
> down the same hill. The added inertia acts both as a smoother and an accelerator…
>
> **This standard story isn't wrong, but it fails to explain many important behaviors of momentum.**
> In fact, momentum can be understood far more precisely if we study it on the right model.

- **Делают X** → сначала честно и качественно излагают ходячую аналогию (не соломенное чучело —
  она изложена сильно), потом точно указывают, **что именно** она не объясняет.
- **Эффект Y** → снимается конфликт с тем, что читатель уже слышал. Он не обязан «забыть шарик» — он
  понимает границы этой картинки.
- **Перенос** → приём «стальной человечек». Секция:
  `**Ходячее объяснение.** <изложить сильно> **Что оно не объясняет.** <2–3 конкретных вопроса>`
  Особенно ценно для тем с популярными мифами: dropout «ансамбль сетей», attention «на что смотрит
  модель», BatchNorm «против internal covariate shift».

**3.3. Явный выбор простейшей нетривиальной модели, с обоснованием. [ВИДЕЛ]**

> We begin by studying gradient descent on the simplest model possible which isn't trivial — the
> convex quadratic … Simple as this model may be, it is rich enough to approximate many functions
> (think of A as your favorite model of curvature — the Hessian, Fisher Information Matrix, etc)
> and captures all the key features…

- **Делают X** → объявляют объект анализа, доказывают, что он одновременно **достаточно прост**
  (решается в замкнутой форме) и **достаточно богат** (воспроизводит нужные эффекты).
- **Эффект Y** → читатель не подозревает автора в подгонке под удобный случай.
- **Перенос** → перед любым разбором «на игрушечном примере» — явный абзац: *почему именно этот
  пример, что он сохраняет из реальности, что теряет*. Одно-два предложения, но обязательно.

**3.4. Одна диаграмма получает несколько подписей по мере прокрутки. [ВИДЕЛ]**

Извлечённые `<figcaption>` идут фрагментами: `and perturbed by an external force field` →
`We can think of −yᵢᵏ as velocity` → `which is dampened at each step` → `And x is our particle's
position` → `which is moved at each step by a small amount in the direction of the velocity`.

Это одна и та же картинка, к которой по мере скролла добавляются пояснения по частям.

- **Делают X** → сложная диаграмма не вываливается целиком — она **собирается по слоям**, каждый
  слой подписан отдельно.
- **Эффект Y** → нет момента «стена из стрелок». Читатель добавляет по одному элементу.
- **Перенос** → без скролла это делается серией из 3–4 картинок нарастающей сложности («шаг 1: только
  данные», «шаг 2: добавили градиент», «шаг 3: добавили инерцию») либо одной картинкой с панелями
  a/b/c и подписью, разобранной по пунктам. **Никогда не давать финальную схему сразу.**

**3.5. Сноски и `<d-footnote>` уводят оговорки из основного текста. [ВИДЕЛ]**

В `post--research-debt` — 11 `<d-footnote>` и 15 `<d-cite>`. Оговорки вроде «It is possible, however,
to construct very specific counterexamples where momentum does not converge, even on convex
functions» стоят сноской, а не в основном потоке.

- **Эффект Y** → строгость сохраняется, но темп чтения не падает.
- **Перенос** → `footnotes` уже подключён в `mkdocs.yml`. Правило: **контрпримеры, краевые случаи и
  «строго говоря» — в сноску; основной текст держит одну мысль.**

**3.6. Почему интерактив вообще работает — их собственная аргументация. [ВИДЕЛ]**

Из `Research Debt`, дословно:

> **Unavailable Tools** – Whether you are a student programming for the first time, or an expert
> trying to reproduce an experiment, being able to easily dive into topics and get your hands dirty
> is critical. **Availability of tools makes it easier to learn because people can test their mental
> models. Rapid feedback is a documentation all of its own**, and quick results are an incredible
> motivation.

И ключевая мысль про экономику объяснения:

> There's a tradeoff between the energy put into explaining an idea, and the energy needed to
> understand it… **if N people are trying to understand each other, it takes each one O(1) effort to
> write an explanation of their ideas but O(N) effort to understand** … For example, Christopher's
> average blog post is read by over 100,000 people; if he can save each reader just one second,
> he's saved humanity 30 hours.

И про то, что объяснение — это не полировка:

> It's tempting to think of explaining an idea as just putting a layer of polish on it, but **good
> explanations often involve transforming the idea**.

- **Перенос** → механизм интерактива — **проверка ментальной модели с быстрой обратной связью**.
  Значит, в markdown его заменяет не «красивая картинка», а **воспроизводимый сниппет, который
  читатель запускает и меняет один параметр**. Это единственная замена, которая сохраняет механизм.
  Отсюда практическое правило: у сниппета сверху должен быть блок настраиваемых констант с
  комментарием «поменяй это и посмотри».

---

## 4. 3Blue1Brown

Построение интуиции до формализма.

Источник — MDX-исходники сайта, урок «But what is a Neural Network?» (441 строка). **[ВИДЕЛ]**

### Измеренные факты

В одном уроке: `<Figure>` — **36 штук**, `<LessonLink>` — 3, `<Question>` — 2, `<Interactive>` — 1,
`<FreeResponse>` — 1, `<Collapsible>` — 1, плюс сноски `[^1]`…`[^6]`. Фронтматтер содержит
`title`, `description`, `date`, `chapter`, `video` (id), `source` (путь к manim-скрипту), `credits`,
`interactive: true`.

### Приёмы

**4.1. Опора на то, что читатель уже умеет, — а потом фиксация парадокса одним жирным предложением.**

Дословно:

> you can tell instantly that these are all images of the digit three … Each three is drawn
> differently, so the particular light-sensitive cells in your eye that fire are different for each,
> but something in that crazy smart visual cortex of yours resolves all these as representing the
> same idea …
>
> But if I told you to sit down and write a program … the task goes from comically trivial to
> dauntingly difficult.
>
> **Somehow identifying digits is incredibly easy for your brain to do, but almost impossible to
> describe _how_ to do.**

- **Делают X** → показывают, что читатель **уже решает** задачу; затем — что описать решение он не
  может; фиксируют разрыв **одним выделенным предложением**.
- **Эффект Y** → мотивация не декларируется («нейросети важны»), а переживается. И у главы появляется
  одна формулируемая цель.
- **Перенос** → в начале главы — **ровно одно жирное предложение-парадокс**, к которому текст будет
  возвращаться. Формат: «X делается легко, но Y при этом невозможно / X очевидно, но Y противоречит
  X». Проверка: если это предложение вычеркнуть, глава не должна потерять точку сборки — значит, оно
  было пустым.

**4.2. Временное, заведомо упрощённое определение — с явной пометкой, что оно временное.**

> **Right now, when I say neuron, all I want you to think is** "a thing that holds a number."
> Specifically, a number between 0.0 and 1.0.

- **Делают X** → дают заведомо неполное определение, но явно ограничивают его срок действия словами
  «right now», «all I want you to think».
- **Эффект Y** → снимается страх «я что-то недопонял»; читатель получает разрешение думать грубо и не
  застревает.
- **Перенос** → маркировать рабочие определения: `**Пока считаем, что** …` и обязательно позже
  `**Уточняем определение:** …`. Ключевое — **вернуться и уточнить**, иначе это просто враньё.
  Полезно завести в конце главы список «что мы упростили и где это уточняется».

**4.3. Плотность рисунков экстремальная: 36 на один урок.**

Почти каждый абзац сопровождается картинкой, и подпись — одно предложение с выводом:

> The input layer contains 784 neurons, each of which corresponds to a single pixel in the original
> image.

Часть `<Figure>` имеет и `image`, и `video`, с параметром `show="video"` — статичный вариант служит
запасным.

- **Перенос** → целевая плотность в главе хендбука: **иллюстрация на каждый смысловой блок**, а не
  1–2 на главу. Формат подписи — одно предложение-вывод. Там, где нужна анимация, — статичная серия
  панелей (см. 3.4).

**4.4. Вопрос с вариантами, где объясняются все дистракторы.**

Дословно из `<Question>`:

> question: "Suppose a neuron in the second layer has weights as indicated above. Rank the four
> images (A, B, C, and D) based on how much they would activate that neuron"
> answer: 2
>
> **B gives the highest activation because it only activates the neurons with positive weights.
> C gives the lowest activation because it is the exact inverse of B. A has a weighted sum of zero
> because all the input neurons are off, but D has a positive activation because it activates 24
> positive weights but only 16 negative weights.**

- **Делают X** → разбор объясняет **каждый** вариант, включая неверные, с конкретными числами
  (24 положительных против 16 отрицательных).
- **Эффект Y** → вопрос учит, а не только проверяет. Читатель, выбравший неверно, понимает, где
  именно сломалась его модель.
- **Перенос** → в блоке «Проверь себя» — тестовые вопросы, где в раскрывающемся ответе разобраны
  **все** варианты. Неверные варианты конструировать из реальных заблуждений (перепутан порядок,
  забыт bias, спутаны precision/recall), а не как случайный шум.

**4.5. `<FreeResponse>` — предскажи, потом раскрой. И `<Collapsible>` — для отступлений.**

`<FreeResponse>` содержит просто ответ («It's having trouble deciding whether the input image is a 4
or a 9») — то есть читателю сначала задаётся открытый вопрос, ответ спрятан.

`<Collapsible title="Bonus Note: The Problem With Sigmoids">` — целое отступление про то, почему
сигмоида плоха, включая метафору «13,000-dimensional game of hot and cold», убрано под спойлер.

- **Перенос** → прямое соответствие в GitHub-markdown: `<details><summary>`. Два разных
  использования: (1) спрятанный ответ на открытый вопрос, (2) бонусное отступление, не нужное для
  основной линии.

**4.6. Честная отправка читателя к чужому источнику.**

> Since it's such a common starting point, there are plenty of other resources … take a look at
> [this excellent online textbook](http://neuralnetworksanddeeplearning.com/) by Michael Nielsen.

- **Эффект Y** → доверие. Автор не делает вид, что он единственный источник.
- **Перенос** → в «Что читать дальше» — не список всего подряд, а **1–3 источника с объяснением,
  кому именно и зачем туда идти**.

### Про общий метод [ПО ОТЗЫВАМ]

Формулировка Гранта «concrete before abstract: give examples before general frameworks» и
инверсия обычного порядка (сначала мотивирующие примеры, потом абстракция) — из вторичных
источников и описаний его выступлений, самого текста я не видел. Содержательно это совпадает с
тем, что я наблюдал в MDX-уроке, но дословную цитату подтвердить не могу.

---

## 5. ESL и ISLR

Как одна и та же тема подана для двух уровней читателя.

Оба PDF прочитаны. **[ВИДЕЛ]** ISLR v2 — 612 стр., ESL 2-е изд. — 764 стр.

### Приёмы

**5.1. Разделение уровней объявлено явно и без снисходительности.**

ISLR, дословно:

> ISL is not intended to replace ESL, which is a far more comprehensive text both in terms of the
> number of approaches considered and the depth to which they are explored. We consider **ESL to be
> an important companion for professionals** (with graduate degrees in statistics, machine learning,
> or related fields) who need to understand the technical details … Therefore, there is a place for
> a **less technical and more accessible version of ESL**.

И четыре принципа ISL (сокращённо, п. 2–3 дословно):

> 2. **Statistical learning should not be viewed as a series of black boxes.** No single approach
>    will perform well in all possible applications. Without understanding all of the cogs inside
>    the box, or the interaction between those cogs, it is impossible to select the best box.
> 3. **While it is important to know what job is performed by each cog, it is not necessary to have
>    the skills to construct the machine inside the box!** … we have almost completely avoided the
>    use of matrix algebra.

- **Делают X** → формулируют не «упрощённая версия», а **другой контракт с читателем**: понимать
  устройство обязательно, уметь вывести — нет. Граница проведена по конкретному признаку (матричная
  алгебра).
- **Эффект Y** → читатель точно знает, что он получит и чего не получит, и не чувствует себя
  второсортным.
- **Перенос** → в начале хендбука зафиксировать **явный контракт по уровням** с проверяемым
  критерием, а не размытым «для начинающих/продвинутых». Например: *базовый уровень — понимаешь,
  что делает метод и когда ломается; углублённый — можешь вывести формулу обновления*. И маркировать
  секции по этому признаку.

**5.2. Один и тот же материал — два разных контракта конца главы.**

Измерено по оглавлениям:

| | ESL | ISLR |
|---|---|---|
| Конец главы | `Bibliographic Notes` → `Exercises` | `Lab: <тема>` → `Exercises` |
| Тип упражнений | `Ex. 3.1 Show that…`, `Ex. 3.3 Gauss–Markov theorem: (a) Prove…` | Две группы: **Conceptual** и **Applied** |
| Вопрос в упражнении | доказать, вывести | «Describe the null hypotheses…», «Carefully explain the differences between KNN classifier and KNN regression» |

ISLR, `Conceptual` вопрос 1 главы 3 (дословно):

> Describe the null hypotheses to which the p-values given in Table 3.4 correspond… **Your
> explanation should be phrased in terms of sales, TV, radio, and newspaper, rather than in terms of
> the coefficients of the linear model.**

- **Делают X** → ESL требует доказать, ISLR требует **объяснить на языке предметной области**.
  Последнее предложение прямо запрещает отвечать формулами.
- **Эффект Y** → ISLR тренирует именно тот навык, который проверяют на собеседовании: объяснить
  результат заказчику.
- **Перенос** → **два типа задач в каждой главе, помеченных явно**:
  `Концептуальные` (объясни словами, без формул — прямо запретить формулы в ответе) и
  `Прикладные` (сделай на данных/в коде). Первые — заготовка ответа на собеседовании.

**5.3. Глава открывается списком вопросов бизнеса и закрывается ответами на них.**

Глава 3 ISLR открывается:

> Suppose that in our role as statistical consultants we are asked to suggest, on the basis of this
> data, a marketing plan for next year… Here are a few important questions that we might seek to
> address:
> 1. Is there a relationship between advertising budget and sales? …

А раздел 3.4 называется `The Marketing Plan` и начинается:

> We now briefly return to the seven questions about the Advertising data that we set out to answer
> at the beginning of this chapter.

Дальше каждый вопрос повторён и на него дан ответ **со ссылкой на раздел, где инструмент был
получен**: «This question can be answered by fitting a multiple regression model… In Section 3.2.2,
we showed that the F-statistic can be used…».

- **Делают X** → «рамка»: N вопросов в начале → инструменты в середине → раздел, где на каждый
  вопрос отвечают по порядку, с обратными ссылками.
- **Эффект Y** → глава ощущается завершённой, и читатель видит, **какой инструмент какой вопрос
  закрывает**. Это же готовая структура ответа на собеседовании.
- **Перенос** → **самый ценный приём для хендбука по подготовке к собеседованию.** Схема главы:
  ```markdown
  ## Вопросы, на которые эта глава отвечает
  1. …  2. …  3. …

  … материал …

  ## Возвращаемся к вопросам
  **1. …?** — <ответ>. Инструмент разобран в [§2](#…).
  ```
  Вопросы формулировать **ровно так, как их задают на интервью**.

**5.4. Маргинальный глоссарий: термин выносится в поле при первом употреблении.**

В извлечённом тексте ISLR видно, что при первом появлении в поле страницы печатаются: `intercept`,
`slope`, `coefficient`, `parameter`, `least squares`, `residual`, `binary`, а в лабораторных
разделах — имена функций: `residuals()`, `rstudent()`, `hatvalues()`, `which.max()`, `q()`,
`savehistory()`, `loadhistory()`.

- **Эффект Y** → книгу можно листать назад и находить, где термин был введён, не открывая индекс.
- **Перенос** → (а) выделять термин **жирным при первом употреблении** и (б) автоматически собирать
  из этих вхождений `00-start/05-glossary.md` с обратной ссылкой на место введения. В репозитории
  глоссарий уже есть — стоит связать его двунаправленно.

**5.5. Лаборатория — часть главы, а не приложение, и ей отведена треть учебного времени.**

ISLR, дословно:

> we have devoted a section within each chapter to R computer labs. In each lab, we walk the reader
> through a realistic application of the methods considered in that chapter. When we have taught
> this material in our courses, **we have allocated roughly one-third of classroom time to working
> through the labs**.

Проверено по оглавлению: `Lab` присутствует в главах 2–13 **без исключений** (2.3, 3.6, 4.7, 5.3,
6.5, 7.8, 8.3, 9.6, 10.9, 11.8, 12.5, 13.6).

- **Эффект Y** → предсказуемость: читатель всегда знает, что в конце главы будет разбор на данных.
- **Перенос** → **нерушимый контракт главы**. Если в одной главе есть практика, она должна быть во
  всех. Отсутствие практики в главе — это баг, а не особенность темы.

**5.6. Таблица «что нового» во втором издании — по главам.**

Предисловие ко 2-му изданию ESL содержит таблицу `Chapter | What's new`: «3. Linear Methods for
Regression — LAR algorithm and generalizations of the lasso», «15. Random Forests — New», и т.д.
Плюс заметки вроде «Chapters 15 and 16 follow naturally from Chapter 10, and the chapters are
probably best read in that order» и честное признание: «In the first edition, the discussion of
error-rate estimation in Chapter 7 **was sloppy** … We have fixed this».

- **Перенос** → `CHANGELOG.md` в разрезе глав, а не коммитов: возвращающийся читатель видит, что
  перечитать. Плюс честные пометки об исправленных ошибках — это дёшево и сильно повышает доверие.

---

## 6. The Missing Semester of Your CS Education (MIT)

Практикоориентированность. Источник — `missing-semester/_2020/course-shell.md`. **[ВИДЕЛ]**

### Приёмы

**6.1. Мотивация формулируется через стыд, а не через пользу.**

Первый раздел называется `# Motivation`, дословно:

> many of us utilize only a small fraction of those tools; **we only know enough magical incantations
> by rote to get by, and blindly copy-paste commands from the internet when we get stuck.**
> This class is an attempt to address this.

- **Делают X** → называют реальное поведение читателя, которое тот за собой знает и стесняется.
- **Эффект Y** → узнавание сильнее, чем абстрактная польза («вы станете продуктивнее»).
- **Перенос** → открывать практические главы описанием того, **как читатель делает это сейчас, и
  почему это работает через раз**. Для ML-хендбука: «обычно берут `train_test_split` с
  `random_state=42`, потому что так во всех туториалах, и не проверяют, не утекло ли время».

**6.2. Всё показано как терминальная сессия с фиксированным промптом и с выводом.**

Везде единый вымышленный промпт `missing:~$`, и **обязательно печатается результат**:

```console
missing:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
missing:~$ which echo
/bin/echo
```

- **Делают X** → команда и её вывод неразделимы; промпт одинаков во всех лекциях.
- **Эффект Y** → читатель сверяет свой результат с эталонным и сразу видит расхождение.
- **Перенос** → **правило для всех сниппетов: показывать ожидаемый вывод.** Либо блоком
  ```` ```text ```` под кодом, либо комментарием `# → 0.847`. Сниппет без вывода нельзя
  верифицировать, и он бесполезен как проверка.

**6.3. Неправильное действие показывается первым, вместе с настоящим текстом ошибки.**

Лучший фрагмент лекции, дословно:

> **Your first instinct might be to do something like:**
> ```console
> $ sudo echo 3 > brightness
> An error occurred while redirecting file 'brightness'
> open: Permission denied
> ```
> **This error may come as a surprise. After all, we ran the command with `sudo`!** This is an
> important thing to know about the shell. Operations like `|`, `>`, and `<` are done _by the shell_,
> not by the individual program … the _shell_ (which is authenticated just as your user) tries to
> open the brightness file for writing, before setting that as `sudo echo`'s output.
>
> Using this knowledge, we can work around this:
> ```console
> $ echo 3 | sudo tee brightness
> ```

Структура ровно такая: **инстинкт → реальный текст ошибки → «это удивительно, потому что…» →
объяснение неверной ментальной модели → исправление**.

- **Эффект Y** → чинится не симптом, а причина. Читатель уносит правило «редирект делает шелл», а не
  рецепт «пиши tee».
- **Перенос** → **это лучший найденный шаблон для секции «Подводные камни»**, которая уже есть в
  `AUTHORING.md`. Переписать её стандарт под 5 обязательных элементов:
  ```markdown
  **Первый инстинкт.** <код, который напрашивается>

  **Что происходит.** <дословный текст ошибки или конкретное неверное число>

  **Почему это удивляет.** <какое убеждение читателя нарушено>

  **Настоящая причина.** <объяснение механизма>

  **Как правильно.** <код> — и почему теперь работает
  ```
  Ключевое, чего обычно не делают: **дословный текст ошибки** и явная формулировка нарушенного
  ожидания.

**6.4. Упражнения — одна связная цепочка, строящая один артефакт, с намеренным провалом посередине.**

Все 11 упражнений лекции 1 — одна линия: создать `/tmp/missing` → `touch semester` → записать в него
скрипт → **попытаться выполнить и не смочь** → понять почему по `ls` → запустить через `sh` →
`chmod` → перенаправить вывод в файл → прочитать `/sys`.

Дословно упражнение 6:

> Try to execute the file … **Understand why it doesn't work** by consulting the output of `ls`
> (hint: look at the permission bits of the file).

И упражнение 7: «Why does this work, while `./semester` didn't?»

Плюс честная позиция авторов:

> **We have not written solutions for the exercises.** If you are stuck on anything in particular,
> feel free to send us an email describing what you've tried so far.

- **Делают X** → (а) цепочка, а не набор; (б) намеренный провал внутри цепочки как обучающий шаг;
  (в) подсказка вместо ответа; (г) требование объяснить, а не только сделать.
- **Эффект Y** → в конце есть работающий артефакт и понимание, а не 11 отдельных «сделал и забыл».
- **Перенос** → блок «Практика» переделать в **одну связную задачу из 6–10 шагов**, где шаг 3–4
  намеренно приводит к ошибке, а следующий шаг просит объяснить её. Финал — работающий артефакт
  (скрипт, ноутбук, пайплайн).

**6.5. Явное «что вы теперь умеете» перед упражнениями.**

Раздел `# Next steps` перед `# Exercises`:

> At this point you know your way around a shell enough to accomplish basic tasks. You should be able
> to navigate around to find files of interest and use the basic functionality of most programs. In
> the next lecture, we will…

- **Эффект Y** → самопроверка формулируется через **действия**, а не через темы («вы изучили пайпы»).
- **Перенос** → перед задачами — блок `## Что ты теперь умеешь` списком глаголов действия:
  «объяснить, почему…», «вывести формулу…», «отладить ситуацию, когда…». Это же готовый чек-лист
  перед собеседованием.

**6.6. Границы курса объявлены заранее.**

> Due to the limited time we have, we won't be able to cover all the tools in the same level of
> detail a full-scale class might. Where possible, we will try to point you towards resources for
> digging further.

- **Перенос** → в каждой главе — короткий блок `Что осталось за рамками` со ссылками. Дёшево и
  предотвращает ощущение, что тема закрыта.

---

## 7. Хендбуки Яндекса

### 7.1. Учебник по машинному обучению (ШАД) — **[ВИДЕЛ]**

Исходники: `gitlab.com/yandexdataschool/ml-handbook`, Jekyll, 26 файлов глав, **1.16 МБ markdown**.

**Измеренные факты:**

| Метрика | Значение |
|---|---|
| Блоков `{% include details.html %}` (спойлер) | **43** |
| Из них «Ответ (не открывайте сразу; сначала подумайте сами!)» | **20** |
| Врезок `**Вопрос на подумать**` | **29** |
| Блоков кода (` ``` `) на главу | 0–16, медиана ≈2 |
| `**Замечание**` | 7 |

Важное наблюдение: **кода почти нет**. Главы `prob_intro`, `prob_maxent`, `ml_theory` — 0 блоков
кода. Это математический текст с задачами на подумать, а не практикум.

**Приём 7.1.1. «Вопрос на подумать» + спойлер с ответом и с запретом подглядывать.**

Дословно из главы про линейные модели:

> **Вопрос на подумать**. Если вы посмотрите содержание учебника, то не найдёте в нём ни
> «полиномиальных» моделей, ни каких-нибудь «логарифмических», хотя, казалось бы, зависимости бывают
> довольно сложными. Почему так?
>
> ```
> {% include details.html
>   summary="Ответ (не открывайте сразу; сначала подумайте сами!)"
>   details="Линейные зависимости не так просты, как кажется…
>            $$y \approx w_1 x_1 + w_2 x_2 + w_3\log{x_1} + w_4\text{sgn}(x_1x_2) + w_0,$$
>            и в итоге из двумерной нелинейной задачи мы получили четырёхмерную линейную регрессию."
> %}
> ```

И — критично для нас — вот чем оказывается этот include (`_includes/details.html` целиком):

```html
<details>
  <summary markdown="span">{{include.summary}}</summary>
  <div>
  {{include.details}}
  </div>
</details>
```

То есть **это обычный HTML `<details>`, который работает в GitHub-markdown без единой доработки**.

- **Делают X** → вопрос вплетён в текст в момент, когда читатель уже имеет всё для ответа; ответ
  спрятан; в самой формулировке `summary` стоит просьба не открывать сразу.
- **Эффект Y** → активное припоминание вместо пассивного чтения, при этом читатель не застревает.
  Соцдоговор в тексте `summary` работает лучше, чем вынос ответов в конец книги.
- **Перенос** → **брать дословно.** 29 вопросов на 26 глав ≈ **один-два «вопроса на подумать» на
  главу минимум**. Формулировка `summary` должна содержать просьбу подумать, а не просто «Ответ».

**Приём 7.1.2. Спойлер используется для восьми разных функций, не только для ответов.**

Полная выборка `summary` по корпусу показывает таксономию:

| Функция | Пример `summary` (дословно) |
|---|---|
| Ответ на самопроверку (20 шт.) | «Ответ (не открывайте сразу; сначала подумайте сами!)» |
| Вывод формулы | «Вывод формулы градиента» |
| Доказательство | «Доказательство для любопытных» |
| Углубление | «Более подробно о затухании градиента», «Немного подробнее об энтропии» |
| Разобранный пример | «Гистограммный метод на примере», «Примеры» |
| Предостережение | «Утверждение выше может вызывать у вас желание использовать AUC в качестве метрики в задачах ранжирования, но мы призываем вас быть аккуратными.» |
| История из практики | «История из жизни про бананы и квадратичный штраф за ошибку» |
| **Повторное объяснение для отставших** | «Если вы не уследили за вычислениями в предыдущем примере, давайте более подробно разберём его чуть более конкретную версию» |
| **Контент, гейтированный пререквизитом** | «…однако если вы не знаете про сингулярное разложение, то лучше вернитесь сюда, когда узнаете.» |

Два последних — самые интересные и почти нигде не встречающиеся.

- **Эффект Y** → одна глава обслуживает читателей разного уровня без ветвления текста. Отставший
  получает второй, медленный проход; опережающий — доказательство; неподготовленный получает честное
  «вернись позже», а не стену.
- **Перенос** → завести **фиксированный набор типов спойлеров** и использовать их системно:
  `Ответ`, `Вывод`, `Доказательство`, `Подробнее`, `Пример`, `Осторожно`, `Из практики`,
  `Разбор помедленнее`, `Нужен пререквизит`. Последние два внести в `AUTHORING.md` как обязательные
  к рассмотрению в каждой математически тяжёлой главе.

**Приём 7.1.3. Глава открывается объяснением своего места в книге.**

Дословно, первый абзац главы про линейные модели:

> Мы начнем с самых простых и понятных моделей машинного обучения: линейных. В этой главе мы
> разберёмся, что это такое, почему они работают и в каких случаях их стоит использовать. **Так как
> это первый класс моделей, с которым вы столкнётесь, мы постараемся подробно проговорить все важные
> моменты. Заодно объясним, как работает машинное обучение, на сравнительно простых примерах.**

- **Делают X** → объясняют не только тему, но и **почему эта глава здесь и что в ней будет сделано
  сверх темы** (на простом объекте объяснить общие механизмы ML).
- **Перенос** → первый абзац главы отвечает на три вопроса: что за тема, почему она в этом месте
  оглавления, что читатель заодно поймёт про предмет в целом.

**Приём 7.1.4. Введение книги: честные предпосылки, отказ от упрощений, приглашение чинить ошибки.**

Дословно:

> Идея была такая: записать сложившийся в ШАДе курс машинного обучения в виде книги, при этом
> **избежав каких-либо компромиссов: нигде ничего не упрощать чрезмерно**, дать необходимую теорию,
> описать и исторически важные алгоритмы, и применяющиеся сегодня…

> Математика — это один из языков, на котором написан учебник. Мы будем стараться давать необходимые
> пояснения, но всё же **уверенное владение линейной алгеброй, математическим анализом и теорией
> вероятностей будет большим плюсом.** Знания статистики и методов выпуклой оптимизации не
> обязательны, хотя сделают чтение комфортнее.

> Читая книгу, вы, возможно, заметите в ней ошибки, неточности и плохо объяснённые детали. В таком
> случае, пожалуйста, **дайте нам знать об этом** … — так вы поможете и другим читателям.

Там же — прямая ссылка на источники, из которых выросла книга (курс Воронцова, NLP Course Лены
Войта), с указанием, чем именно каждый повлиял.

- **Перенос** → раздел «как читать» должен содержать: (1) явные пререквизиты с делением на
  обязательные и желательные; (2) заявленную позицию по упрощениям; (3) приглашение репортить ошибки;
  (4) честное указание источников влияния.

**Приём 7.1.5. Персональное авторство главы с контактом.**

Фронтматтер главы:

```yaml
---
title: Линейные модели
author: filipp_sinicin, evgenii_sokolov
---
```

а `_data/authors.yml` разворачивает это в имя + telegram + email, и шаблон `authors.html` рисует под
заголовком «Авторы: …» со ссылками на связь.

- **Эффект Y** → у главы есть ответственный; вопрос можно задать конкретному человеку. Это заметно
  поднимает воспринимаемое качество.
- **Перенос** → фронтматтер `author:` в каждой главе + `resources/authors.yml`. Даже если автор один,
  это дисциплинирует.

**Приём 7.1.6. Навигация — прогресс-бар, боковое меню, оглавление, отдельный `pages.yaml`.**

В `_includes/`: `progressBar.html` + `progressBar.js` (индикатор прочитанного в главе), `sidebar.html`,
`toc.html`, `tooltip.js`, `highlight_active_nav_item.js`. Структура навигации вынесена в
`_data/pages.yaml` — группировка по разделам («Классическое обучение с учителем» → список глав), а не
по папкам.

- **Перенос** → в mkdocs-material прогресс-бар и подсветка активного пункта есть из коробки
  (`toc.follow`, `navigation.tracking` — уже включены). Ценное здесь другое: **навигация описана
  смысловыми группами отдельно от файловой структуры**. В репозитории `nav` генерируется скриптом
  `tools/build_nav.py` — стоит убедиться, что группировка смысловая, а не алфавитная по папкам.

### 7.2. Хендбук по алгоритмам и хендбук по математике — **[ПО ОТЗЫВАМ]**

`education.yandex.ru` закрыт egress-политикой, зеркал не нашёл. Ниже — **только** то, что следует из
поисковой выдачи; исходников я не видел и структуру глав описать не могу.

Что удалось установить из описаний:

- Хендбук «Основы алгоритмов»: **9 глав**; теория плюс практические задания с **автопроверкой**;
  проверка решений идёт **автоматически через систему Яндекс.Контест**; заявлена также автопроверка
  эффективности решения, а не только корректности. Указано, что бо́льшая часть основана на
  интерактивном учебнике Александра Куликова и Павла Певзнера.
- Хендбук по математике: сделан совместно с ФКН ВШЭ; заявлено сочетание теории, примеров, **квизов** и
  сниппетов на Python, плюс задания, где нужно писать код. Порядок глав описан как смешанный: сначала
  базовые понятия из каждой области с демонстрацией решаемых задач, затем углубление.
- Общий механизм прогресса: чтобы решать задачи и отслеживать прогресс, **нужна регистрация**
  (Яндекс ID); в конце главы читатель ставит отметку «Глава прочитана».

**[НЕ УДАЛОСЬ]**: увидеть, как именно свёрстана глава, как выглядят формулы, где стоят задачи
относительно теории, есть ли подсказки и сколько попыток даётся. Ничего из этого не достраиваю.

Что из подтверждённого стоит перенести:

- **Автопроверка как часть учебника, а не отдельный сайт.** Перенос в GitHub-репозиторий: задача →
  файл-заготовка в `code/` → `pytest`-тест, который читатель запускает локально (`make test-ch03`).
  Это единственная честная замена контесту в статичном хендбуке.
- **Явная отметка «глава прочитана».** Перенос: чек-лист прогресса в `00-start/` с чекбоксами
  markdown (`pymdownx.tasklist` уже подключён), который читатель форкает/копирует себе.
- **Смешанный порядок глав** (сначала по верхам всех областей с демонстрацией применимости, потом
  углубление) — альтернатива линейной подаче; стоит рассмотреть для трека «быстрая подготовка».

---

## Что невозможно перенести в GitHub-markdown и чем заменить

Ключевой ограничитель: репозиторий читают **в двух режимах** — как markdown на GitHub и как сайт
mkdocs-material. GitHub игнорирует admonitions (`!!! note`), вкладки, `attr_list`, MathJax-специфику;
mkdocs не рендерит GitHub-алерты (`> [!NOTE]`). Поэтому ниже я разделяю «нельзя нигде» и «нельзя на
GitHub, можно в mkdocs».

### A. Невозможно в принципе

| Приём оригинала | Почему не переносится | Замена |
|---|---|---|
| **Ползунки Distill** (α, β в реальном времени) | Нет JS в статичном markdown | Сниппет с **явным блоком констант вверху** и комментарием «поменяй и перезапусти» + **готовая сетка результатов таблицей** для 3–5 значений параметра. Механизм («проверка ментальной модели + быстрая обратная связь») сохраняется, если читатель реально запускает. |
| **Анимации 3B1B** (непрерывная трансформация пространства) | Нет анимации | Серия из 3–4 статичных кадров ключевых моментов + подпись, объясняющая **что изменилось между кадрами**. Именно дельта, а не описание каждого кадра. Опционально — короткий `.gif`/`.mp4` (GitHub рендерит `.gif` в markdown, mkdocs тоже). |
| **Прокрутка-по-шагам Distill** (одна диаграмма, подписи по мере скролла) | Нет скролл-триггеров | Панели a/b/c одной картинкой + разбор подписи по пунктам списка (см. 3.4). |
| **Исполняемые ячейки d2l/UDL** (Colab-кнопка, вывод под ячейкой) | markdown не исполняется | Код в `code/` + **обязательно вставленный в текст ожидаемый вывод** (приём 6.2) + ссылка «открыть в Colab» на файл в репозитории. Вывод в тексте — обязателен, иначе теряется весь смысл. |
| **Автопроверка Яндекс.Контеста** | Нет сервера | `pytest`-тесты в репозитории + `make check-<глава>`. Читатель получает зелёный/красный локально. |
| **Маргиналии UDL** (текст физически в поле страницы) | markdown одноколоночный | Строка-врезка сразу после абзаца (см. 2.3). Семантика («это относится вот к этому абзацу») сохраняется, визуальная лёгкость — нет. Компенсируется краткостью: одна строка, эмодзи-маркер, ссылка. |
| **Форум под каждым разделом d2l** | Нет комментариев в markdown | Предзаведённый GitHub Discussion на главу + ссылка в футере главы. Работает только если треды созданы заранее. |
| **Прогресс-бар и отметка «прочитано»** | Нет состояния | В mkdocs частично есть (`toc.follow`). Для «прочитано» — чек-лист с `- [ ]` в `00-start/`, который читатель ведёт в своём форке. |
| **Переключение фреймворков d2l** (одна страница, 4 версии кода) | На GitHub вкладок нет | `pymdownx.tabbed` для сайта **плюс** требование: текст вокруг вкладок должен быть валиден без них. На GitHub вкладки развернутся в последовательные блоки — это приемлемо, если каждый блок подписан («PyTorch:», «TensorFlow:»). |

### B. Возможно, но по-разному в двух режимах — писать с оглядкой

| Приём | GitHub | mkdocs-material | Рекомендация |
|---|---|---|---|
| Спойлер / скрытый ответ | ✅ `<details><summary>` | ✅ (`md_in_html` подключён) | **Использовать `<details>`, а не `??? note`.** Работает везде. Это подтверждено исходниками ШАД — у них ровно `<details>`. |
| Формулы | ✅ `$…$`, `$$…$$` | ✅ `arithmatex` | Писать в `$$…$$` на отдельных строках. Избегать конструкций, которые расходятся между KaTeX (GitHub) и MathJax. |
| Врезка-предупреждение | ❌ `!!! warning` не рендерится | ✅ | Использовать `>`-цитату с жирным префиксом: `> **Осторожно.** …`. Читается везде. |
| Сноски | ⚠️ GitHub поддерживает `[^1]` | ✅ `footnotes` | Можно. |
| Таблицы | ✅ | ✅ | Основной инструмент для сравнений «метод / когда / когда не». |
| Mermaid-диаграммы | ✅ (GitHub рендерит) | ✅ (настроен `superfences`) | Хороший способ отдать схемы текстом: версионируются в git, видны в diff. |
| Чек-боксы | ✅ | ✅ `tasklist` | Для «что ты теперь умеешь» и трекинга прогресса. |

### C. Что важнее любых замен

Три приёма из разобранных **не требуют никакой технологии** и дают наибольший эффект на единицу
усилий. Если переносить только три вещи, то эти:

1. **Показ ошибки целиком** (Missing Semester, 6.3): первый инстинкт → дословный текст ошибки →
   почему это удивляет → настоящая причина → как правильно.
2. **Рамка из вопросов** (ISLR, 5.3): N вопросов собеседования в начале главы → ответы на них в
   конце с обратными ссылками на разделы.
3. **Вопрос на подумать со спрятанным ответом** (ШАД, 7.1.1): `<details>` с просьбой не открывать
   сразу, 1–2 штуки на главу минимум.

---

## Сводный контракт главы

Синтез контрактов всех семи источников — что из этого стоит зафиксировать как обязательное.
Сопоставлено с уже существующей структурой в `.handbook/AUTHORING.md`.

| Блок | Откуда взят | Обязателен? |
|---|---|---|
| Автор(ы) главы с контактом | ШАД 7.1.5 | да |
| Первый абзац: тема + почему она здесь + что заодно поймёшь | ШАД 7.1.3 | да |
| Вопросы собеседования, на которые глава отвечает | ISLR 5.3 | да |
| Открытие: 3 применения + сквозной пример + «а это не сюда» | d2l 1.1 | да |
| Провал предыдущего метода лестницей из 3 примеров | d2l 1.2 | если тема надстраивается над предыдущей |
| Одно жирное предложение-парадокс | 3B1B 4.1 | да |
| Ходячее объяснение → что оно не объясняет | Distill 3.2 | если у темы есть популярный миф |
| Временные определения с явной пометкой + последующее уточнение | 3B1B 4.2 | по ситуации |
| Иллюстрация на каждый смысловой блок, подпись-абзац | UDL 2.1, 3B1B 4.3 | да |
| Панельные рисунки a/b/c вместо серии | UDL 2.2 | да |
| Врезки-указатели на пререквизит / задачу / код | UDL 2.3 | да |
| «Что будет, если убрать этот элемент» с выкладкой | d2l 1.3 | для каждого нетривиального элемента |
| Замер с числом под каждое количественное утверждение | d2l 1.4 | да |
| Ожидаемый вывод под каждым сниппетом | Missing Semester 6.2 | да |
| Подводные камни по 5-шаговому шаблону с текстом ошибки | Missing Semester 6.3 | да |
| Спойлеры 9 типов (Ответ / Вывод / Доказательство / Подробнее / Пример / Осторожно / Из практики / Помедленнее / Нужен пререквизит) | ШАД 7.1.2 | да |
| 1–2 «вопроса на подумать» со спрятанным ответом | ШАД 7.1.1 | да, минимум |
| `Заметки на полях`: история, варианты, терминология | UDL 2.4 | да |
| `Что ты теперь умеешь` — списком глаголов | Missing Semester 6.5 | да |
| Задачи: Концептуальные (без формул!) + Прикладные | ISLR 5.2 | да |
| Задачи деревом «а что если…», со звёздочкой для сложных | d2l 1.6, UDL 2.5 | да |
| Практика одной цепочкой с намеренным провалом | Missing Semester 6.4 | да |
| Возврат к вопросам из начала главы | ISLR 5.3 | да |
| `Что осталось за рамками` | Missing Semester 6.6 | да |
| Ссылка на обсуждение главы | d2l 1.7 | да |
| 1–3 внешних источника с объяснением «кому туда» | 3B1B 4.6 | да |

Инфраструктура уровня книги: `CHANGELOG` по главам (ESL 5.6), автосборка `resources/formulas.md`
(UDL 2.6), глоссарий, связанный двунаправленно с местами введения терминов (ISLR 5.4), видимая
ссылка «нашли ошибку» (UDL 2.6, ШАД 7.1.4).

---

## Итоговое наблюдение

Ни один из семи источников не удерживает внимание за счёт «интересного изложения». Все семь делают
одно и то же структурно: **создают у читателя вопрос до того, как дать ответ**, и **дают способ
проверить себя, не дожидаясь конца главы**.

Различаются только носители: Distill — ползунок, 3B1B — анимация и `<Question>`, UDL — «нарисуй на
бумаге, потом запусти», d2l — исполняемая ячейка с замером, ISLR — семь вопросов в рамке главы,
Missing Semester — команда, которая падает, ШАД — `<details>` с просьбой не подглядывать.

В GitHub-markdown из этих носителей доступны два, но они покрывают механизм полностью:
**`<details>` со спрятанным ответом** и **сниппет с явно выписанным ожидаемым выводом**.
Всё остальное — вопрос дисциплины автора, а не возможностей формата.
