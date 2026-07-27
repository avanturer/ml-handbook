# books-modern — прочёс программ

Область: современные книги-учебники и их **оглавления** (тема за темой).
Дата прочёса: 2026-07-27.

Важное про доступ: сетевой прокси в этой сессии режет почти все хосты, кроме
`raw.githubusercontent.com`. Отдали 403 (policy denial на CONNECT, а не защита сайта):
`d2l.ai`, `udlbook.github.io`, `mitpress.mit.edu`, `probml.github.io`, `cambridge.org`,
`oreilly.com`, `link.springer.com`, `springerprofessional.de`, `dokumen.pub`, `leanpub.com`,
`freecomputerbooks.com`, `web.stanford.edu/~jurafsky/slp3`, `web.archive.org`, `r.jina.ai`.
Обход, который сработал: (1) исходники книг и их PDF-оглавления в GitHub-репозиториях через
`raw.githubusercontent.com`; (2) ручная распаковка PDF-потоков (zlib + разбор операторов `Tj`/`TJ`),
потому что `pdftotext`/`poppler` в среде нет; (3) WebSearch там, где репозитория нет.

---

## Что реально открыл (со ссылками)

### [ОТКРЫЛ] — содержимое реально получено и прочитано

| Источник | Ссылка, которую открыл | Что получил |
|---|---|---|
| **Dive into Deep Learning (d2l.ai)** | `https://raw.githubusercontent.com/d2l-ai/d2l-en/master/index.md` | полный toctree: 23 главы + приложения |
| d2l — гауссовы процессы | `.../master/chapter_gaussian-processes/index.md` | 3 секции |
| d2l — HPO | `.../master/chapter_hyperparameter-optimization/index.md` | 5 секций |
| d2l — computational performance | `.../master/chapter_computational-performance/index.md` | 7 секций |
| d2l — RL | `.../master/chapter_reinforcement-learning/index.md` | 3 секции |
| d2l — оптимизация | `.../master/chapter_optimization/index.md` | 11 секций |
| d2l — recsys | `.../master/chapter_recommender-systems/index.md` | 10 секций |
| d2l — attention/transformers | `.../master/chapter_attention-mechanisms-and-transformers/index.md` | 9 секций |
| **Probabilistic ML: An Introduction (Murphy, кн. 1)** | `https://raw.githubusercontent.com/probml/pml-book/main/toc1.pdf` | полное оглавление до уровня X.Y (23 главы, 6 частей) |
| **Probabilistic ML: Advanced Topics (Murphy, кн. 2)** | `https://raw.githubusercontent.com/probml/pml2-book/main/toc2-long-2023-01-19.pdf` | полное оглавление до уровня X.Y (36 глав, 6 частей) |
| **AI Engineering (Chip Huyen)** | `https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md` | полное оглавление до 3-го уровня с номерами страниц |
| **Designing ML Systems (Chip Huyen)** | `https://raw.githubusercontent.com/chiphuyen/dmls-book/main/ToC.pdf` + `.../summary.md` | полное оглавление до 3-го уровня + резюме всех 11 глав |
| **Build a LLM From Scratch (Raschka)** | `https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/README.md` | 7 глав, 5 приложений, весь bonus-материал |
| **Designing Data-Intensive Applications (1-е изд.)** | `https://raw.githubusercontent.com/Vonng/ddia/master/README.md` | 3 части, 12 глав |
| **Practical Statistics for Data Scientists (2-е изд.)** | `https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/python/notebooks/Chapter%20{1..7}%20-%20*.ipynb` | заголовки секций глав 1–7 (структура ноутбуков повторяет разделы книги) |
| **Understanding Deep Learning (Prince)** | `https://raw.githubusercontent.com/SanDiegoMachineLearning/bookclub/master/understanding-deep-learning.md` | список всех 21 главы |
| Murphy, страницы книг | `https://raw.githubusercontent.com/probml/pml-book/main/book1.html`, `.../book2.html` | открыл, но короткое оглавление там — картинка; текст взял из PDF выше |

### [ТОЛЬКО ОПИСАНИЕ] — оглавление собрано из поисковой выдачи, сама страница не открылась

| Источник | Что удалось собрать |
|---|---|
| **Speech and Language Processing, 3rd ed (Jurafsky & Martin)** | список из 24 глав + 8 веб-приложений (сводка поиска; `web.stanford.edu` даёт 403) |
| **Trustworthy Online Controlled Experiments (Kohavi, Tang, Xu)** | 5 частей, 23 главы (сводка поиска; `cambridge.org` 403) |
| **ML System Design Interview (Aminian & Xu)** | 11 глав-кейсов (сводка поиска; `oreilly`/`amazon` 403) |
| **Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood)** | подтверждены названия глав 1, 2, 4, 8, 9, 10, 11, 15 + темы глав про Fairness/Training Systems; полного списка 1–15 собрать не удалось |
| **Recommender Systems Handbook, 3-е изд. (Ricci, Rokach, Shapira)** | 5 частей + точечно подтверждённые главы (5, 6, 9, 13, 15, 16, 18, 19); полного списка ~28 глав не собрал |
| **Machine Learning Engineering (Burkov)** | последовательность глав по жизненному циклу (сводка поиска) |
| **The Hundred-Page ML Book (Burkov)** | 11 глав (сводка поиска) |
| **Understanding Deep Learning — подглавы** | описания глав 20 и 21 (сводка поиска) |
| **DDIA, 2-е изд. (2026, Kleppmann & Riccomini)** | подтверждены новые главы «Trade-offs in Data Systems Architecture», «Defining Nonfunctional Requirements», переименование partitioning→sharding, переписанная глава про consistency/consensus |

### [НЕ ДОСТУПЕН]

Полные подглавы **Understanding Deep Learning** (репозиторий `udlbook/udlbook` через raw отдаёт 404 на
`README.md` во всех ветках; сайт книги 403). Полное оглавление **Recommender Systems Handbook** и
**Reliable Machine Learning** (Springer/O'Reilly закрыты прокси, GitHub-зеркал нет).
Оглавление **Practical Statistics** 3-го изд. (репозиторий `gedeck/ai-assisted-statistics-for-data-scientists`
упомянут, но не проверялся). Отсутствие находки — тоже результат.

---

## Программы (по каждому источнику — полный список тем)

### 1. Dive into Deep Learning — d2l.ai [ОТКРЫЛ]

Верхний уровень (23 главы + 2 приложения):
1. Introduction · 2. Preliminaries · 3. Linear Regression · 4. Linear Classification ·
5. Multilayer Perceptrons · 6. Builder's Guide · 7. Convolutional Neural Networks ·
8. Modern Convolutional Neural Networks · 9. Recurrent Neural Networks ·
10. Modern Recurrent Neural Networks · 11. Attention Mechanisms and Transformers ·
12. Optimization Algorithms · 13. Computational Performance · 14. Computer Vision ·
15. NLP: Pretraining · 16. NLP: Applications · **17. Reinforcement Learning** ·
**18. Gaussian Processes** · **19. Hyperparameter Optimization** · 20. GANs ·
21. Recommender Systems · Appendix: Mathematics for Deep Learning · Appendix: Tools for Deep Learning.

Раскрытые главы:
- **Optimization (12):** intro · convexity · gd · sgd · minibatch-sgd · momentum · adagrad · rmsprop ·
  **adadelta** · adam · lr-scheduler.
- **Computational Performance (13):** hybridize (imperative vs symbolic) · async-computation ·
  auto-parallelism · **hardware** · multiple-gpus · multiple-gpus-concise · **parameterserver**.
- **Reinforcement Learning (17):** mdp · value-iteration · q-learning.
- **Gaussian Processes (18):** gp-intro · gp-priors (weight-space → function-space, ядра и обобщение) ·
  gp-inference (апостериор, код с нуля + GPyTorch).
- **Hyperparameter Optimization (19):** hyperopt-intro · hyperopt-api · **random search async** ·
  **successive halving intro** · **successive halving async (ASHA)**.
- **Attention & Transformers (11):** queries-keys-values · attention-pooling · attention-scoring-functions ·
  bahdanau-attention · multihead-attention · self-attention-and-positional-encoding · transformer ·
  vision-transformer · large-pretraining-transformers.
- **Recommender Systems (21):** recsys-intro · movielens · mf · **autorec** · ranking · **neumf** ·
  seqrec (Caser) · ctr · fm · deepfm.

Ценность: единственный источник, где HPO, гауссовы процессы и «железо/параллелизм» разобраны
кодом. Грейд: junior→middle (главы 1–11), middle+ (12, 13, 18, 19).

### 2. Understanding Deep Learning — Simon Prince [ОТКРЫЛ список глав]

1. Introduction · 2. Supervised learning · 3. Shallow neural networks · 4. Deep neural networks ·
5. Loss functions · 6. Fitting models · 7. Gradients and initialization · 8. Measuring performance ·
9. Regularization · 10. Convolutional networks · 11. Residual networks · 12. Transformers ·
**13. Graph neural networks** · 14. Unsupervised learning · **15. Generative adversarial networks** ·
**16. Normalizing flows** · **17. Variational autoencoders** · **18. Diffusion models** ·
**19. Reinforcement learning** · **20. Why does deep learning work?** · **21. Deep learning and ethics**.

Гл. 20 [ТОЛЬКО ОПИСАНИЕ]: почему глубокие сети легко обучаются, почему обобщают, зачем столько
параметров, нужна ли глубина; структура ландшафта функции потерь, **double descent**, **grokking**,
**lottery tickets**.
Гл. 21 [ТОЛЬКО ОПИСАНИЕ]: вред от систем ИИ — алгоритмическая предвзятость, необъяснимость,
нарушения приватности данных, милитаризация, мошенничество, экологический след.

Ценность: лучший современный учебник по теории DL; гл. 15–18 — единственное системное покрытие
генеративных моделей. Грейд: middle → middle+.

### 3. Probabilistic ML: An Introduction — Murphy, кн. 1 [ОТКРЫЛ полностью]

**1. Introduction** (что такое ML, supervised, unsupervised, RL, данные — включая
предобработку дискретных и текстовых входов и **обработку пропусков**).

**Part I. Foundations**
- **2. Probability: Univariate Models** — что такое вероятность, типы неопределённости,
  вероятность как расширение логики; случайные величины; правило Байеса; Бернулли/биномиальное;
  категориальное/мультиномиальное; гауссово; прочие одномерные распределения; преобразования СВ.
- **3. Probability: Multivariate Models** — совместные распределения; многомерное гауссово;
  **линейно-гауссовы системы**; **экспоненциальное семейство**; смеси; **вероятностные графические модели**.
- **4. Statistics** — MLE; ERM; **другие методы оценивания** (моменты, онлайн-оценивание);
  регуляризация; **байесовская статистика** (сопряжённые априорные, апостериор, credible intervals);
  частотная статистика (bootstrap, доверительные интервалы, «патологии»).
- **5. Decision Theory** — **байесовская теория решений** (матрицы потерь, Байес-риск, отказ от
  предсказания, ROC/PR как решающие правила); **байесовская проверка гипотез** (Байес-фактор, BIC);
  частотная теория решений (риск, admissibility); ERM; частотная проверка гипотез (p-value, Neyman-Pearson).
- **6. Information Theory** — энтропия; KL; взаимная информация.
- **7. Linear Algebra** — умножение матриц; обращение; EVD; SVD; **другие разложения** (QR, Cholesky);
  решение СЛАУ; матричное исчисление.
- **8. Optimization** — методы первого порядка; **второго порядка** (Ньютон, квазиньютон/BFGS);
  SGD; **условная оптимизация** (KKT, Лагранж); **проксимальный градиент** (ISTA, проекции);
  **bound optimization / MM (в т.ч. EM)**; **чёрный ящик и безградиентная оптимизация**.

**Part II. Linear Models**
- **9. Linear Discriminant Analysis** — **гауссов дискриминантный анализ (LDA/QDA)**; наивный Байес;
  генеративные vs дискриминативные классификаторы.
- **10. Logistic Regression** — бинарная; мультиномиальная; **робастная логрегрессия**;
  **байесовская логрегрессия** (Лапласова аппроксимация).
- **11. Linear Regression** — МНК; ridge; lasso; **регрессионные сплайны**; **робастная регрессия
  (Huber, Student-t)**; **байесовская линейная регрессия**.
- **12. Generalized Linear Models** — примеры (Пуассон, гамма); **неканонические функции связи**;
  MLE; разбор задачи предсказания страховых выплат.

**Part III. Deep Neural Networks** — 13. Для структурированных данных (MLP, backprop, обучение,
регуляризация) · 14. Для изображений · 15. Для последовательностей (RNN, 1d CNN, attention,
трансформеры, LM и обучение представлений без разметки).

**Part IV. Nonparametric Models**
- **16. Exemplar-based Methods** — kNN; **обучение метрик расстояния (metric learning)**;
  **ядерная оценка плотности (KDE)**.
- **17. Kernel Methods** — ядра Мерсера; **гауссовы процессы**; SVM; **sparse vector machines (RVM)**.
- **18. Trees, Forests, Bagging, Boosting** — CART; ансамбли; бэггинг; RF; бустинг;
  **интерпретация ансамблей деревьев**.

**Part V. Beyond Supervised Learning**
- **19. Learning with Fewer Labeled Examples** — аугментация; **transfer learning**;
  **semi-supervised learning**; **active learning**; **meta-learning**; **few-shot learning**;
  **weakly supervised learning**.
- **20. Dimensionality Reduction** — PCA; **факторный анализ**; автоэнкодеры; **manifold learning**;
  эмбеддинги слов.
- **21. Clustering** — иерархическая; k-means; смеси; **спектральная кластеризация**; **бикластеризация**.
- **22. Recommender Systems** — explicit; implicit; сторонняя информация;
  **компромисс exploration/exploitation**.
- **23. Graph Embeddings** — encoder/decoder-постановка; **мелкие графовые эмбеддинги (DeepWalk/node2vec)**;
  GNN; глубокие графовые эмбеддинги; применения.

Ценность: строгая вероятностная база под всё, что MLE делает руками. Грейд: middle → middle+.

### 4. Probabilistic ML: Advanced Topics — Murphy, кн. 2 [ОТКРЫЛ полностью]

**Part I. Fundamentals** — 2. Probability (распределения, гауссовы совместные, **экспоненциальное
семейство**, преобразования, **марковские цепи**, **меры расхождения между распределениями**) ·
3. Statistics (байесовская и частотная, **сопряжённые/неинформативные/иерархические априорные**,
**empirical Bayes**, **выбор модели**, **проверка модели**, проверка гипотез, **пропущенные данные**) ·
4. Graphical models (**байесовские сети**, **марковские случайные поля**, **CRF**,
сравнение направленных и ненаправленных, расширения PGM, **структурные причинные модели**) ·
5. Information theory (KL, энтропия, MI, **сжатие данных**, **помехоустойчивое кодирование**,
**information bottleneck**) · 6. Optimization (**автодифференцирование**, стохастическая,
**natural gradient**, MM-алгоритмы, **байесовская оптимизация**, безградиентная,
**оптимальный транспорт**, **субмодулярная оптимизация**).

**Part II. Inference** — 7. Обзор алгоритмов вывода · 8. **Гауссова фильтрация и сглаживание**
(линейно-гауссовы SSM, **фильтр Калмана**, EKF/UKF, assumed density filtering) ·
9. **Message passing** (belief propagation, loopy BP, variable elimination, junction tree) ·
10. **Вариационный вывод** (градиентный VI, CAVI, более точные апостериоры, EP) ·
11. **Монте-Карло** (интегрирование, rejection/importance sampling, снижение дисперсии) ·
12. **MCMC** (Metropolis-Hastings, Гиббс, HMC, диагностика сходимости, стохастический градиентный MCMC,
reversible jump, отжиг) · 13. **SMC** (частичные фильтры, RBPF, SMC-сэмплеры).

**Part III. Prediction** — 14. Обзор предиктивных моделей (оценивание, **конформальное предсказание**) ·
15. **GLM** (линейная, логистическая, **пробит**, **многоуровневые/иерархические GLM**) ·
16. Глубокие сети · 17. **Байесовские нейросети** (априорные, апостериорные, обобщение, онлайн-вывод) ·
18. **Гауссовы процессы** (ядра Мерсера, негауссовы правдоподобия, масштабирование, обучение ядра,
GP + DNN, **GP для прогнозирования временных рядов**) ·
19. **За пределами i.i.d.** (**сдвиг распределений**, детекция сдвигов, **робастность к сдвигу**,
**адаптация к сдвигу**, обучение на нескольких распределениях, **continual learning**,
**состязательные примеры**).

**Part IV. Generation** — 20. Обзор генеративных моделей (**типы, цели, оценка генеративных моделей**) ·
21. **VAE** (основы, обобщения, **posterior collapse**, иерархические, **VQ-VAE**) ·
22. **Авторегрессионные модели** (NADE, causal CNN, трансформеры) · 23. **Нормализующие потоки** ·
24. **Energy-based models** (**score matching**, **noise contrastive estimation**) ·
25. **Диффузионные модели** (DDPM, **score-based**, непрерывное время/SDE, **ускорение сэмплирования**,
**условная генерация**) · 26. **GAN** (обучение сравнением, conditional GAN, вывод в GAN, архитектуры).

**Part V. Discovery** — 27. Обзор · 28. **Латентные факторные модели** (смеси, факторный анализ,
не-гауссовы априорные, **тематические модели/LDA**, **ICA**) · 29. **State-space models**
(**HMM** и применения/обучение, **линейные динамические системы**, **switching LDS**,
нелинейные и негауссовы SSM, **структурные модели временных рядов**, **deep SSM**) ·
30. **Обучение графов** (латентные модели графов, **structure learning**) ·
31. Непараметрические байесовские модели · 32. **Обучение представлений** (оценка и сравнение
представлений, подходы, теория) · 33. **Интерпретируемость** (методы, свойства, **оценка
интерпретируемости**).

**Part VI. Action** — 34. **Принятие решений в условиях неопределённости** (статистическая теория
решений, **диаграммы влияния**, **A/B-тестирование**, **контекстные бандиты**, **MDP**,
планирование в MDP, **активное обучение**) · 35. **RL** (value-based, policy-based, model-based,
**offline RL**, **control as inference**) · 36. **Причинность** (**каузальный формализм**, RCT,
**корректировка на конфаундеры**, **инструментальные переменные**, **DiD**,
**проверки правдоподобности (sensitivity analysis)**, **do-исчисление**).

Ценность: словарь и глубина по всему, что «за пределами supervised». Грейд: middle+ / senior,
как справочник.

### 5. Designing ML Systems — Chip Huyen [ОТКРЫЛ полностью, до 3-го уровня]

1. **Overview of ML Systems** — когда использовать ML; кейсы; ML в исследованиях vs в проде;
   ML-системы vs традиционный софт.
2. **Introduction to ML Systems Design** — бизнес- и ML-цели; требования (reliability, scalability,
   maintainability, adaptability); итеративный процесс; постановка ML-задачи (типы задач, целевые функции);
   **mind vs data**.
3. **Data Engineering Fundamentals** — источники данных; форматы (JSON, **row-major vs column-major**,
   текст vs бинарь); **модели данных (реляционная, NoSQL — документная и графовая)**;
   структурированные vs неструктурированные; **OLTP vs OLAP**; **ETL**;
   **режимы передачи данных: через БД, через сервисы, через real-time transport**;
   батч vs стрим.
4. **Training Data** — **сэмплирование: непробабилистическое, простое случайное, стратифицированное,
   взвешенное, reservoir sampling, importance sampling**; разметка: ручная, **natural labels**,
   **как жить без разметки (weak supervision, semi-supervision, transfer learning, active learning)**;
   дисбаланс классов; аугментация (label-preserving трансформации, **перturbation**, **синтез данных**).
5. **Feature Engineering** — выученные vs сконструированные признаки; пропуски; масштабирование;
   **дискретизация**; кодирование категорий; **feature crossing**;
   **дискретные и непрерывные позиционные эмбеддинги**; утечки данных (причины, детекция);
   важность признаков; **обобщаемость признаков**.
6. **Model Development and Offline Evaluation** — выбор модели; ансамбли; трекинг и версионирование
   экспериментов; распределённое обучение; **AutoML (soft/hard, NAS, learned optimizers)**;
   офлайн-оценка: **бейзлайны**, методы оценки (**perturbation tests, invariance tests,
   directional expectation tests, calibration, slice-based evaluation**).
7. **Model Deployment and Prediction Service** — 4 мифа о деплое; батч vs онлайн;
   **объединение батч- и стрим-пайплайнов**; сжатие модели (**low-rank factorization**, дистилляция,
   прунинг, квантизация); **ML в облаке и на edge**; **компиляция и оптимизация под edge**;
   **ML в браузере**.
8. **Data Distribution Shifts and Monitoring** — причины отказов ML-систем (софтверные,
   **ML-специфичные: production-данные ≠ train, edge cases, degenerate feedback loops**);
   типы сдвигов; детекция; борьба; мониторинг и observability (ML-метрики, инструменты).
9. **Continual Learning and Test in Production** — **stateless retraining vs stateful training**;
   зачем continual learning; вызовы; **4 стадии continual learning**; как часто обновлять;
   тест в проде: shadow, A/B, canary, **interleaving**, **бандиты**.
10. **Infrastructure and Tooling for MLOps** — storage/compute; облако vs свои ДЦ; dev-окружение и его
    стандартизация; контейнеры; управление ресурсами (cron, шедулеры, оркестраторы);
    workflow management; ML-платформа (деплой, **model store**, feature store); **build vs buy**.
11. **The Human Side of ML** — UX (консистентность предсказаний, **«в основном верные» предсказания**,
    **smooth failing**); структура команды (**кросс-функциональные команды vs end-to-end DS**);
    **Responsible AI** (кейсы безответственного ИИ, **фреймворк ответственного ИИ**).

Ценность: базовый словарь ML System Design-секции. Грейд: middle → middle+.

### 6. AI Engineering — Chip Huyen [ОТКРЫЛ полностью, до 3-го уровня]

1. **Introduction to Building AI Applications with Foundation Models** — от LM к LLM к foundation
   models к AI engineering; use-кейсы; **планирование AI-приложений (оценка кейса, ожидания,
   майлстоуны, поддержка)**; **стек AI-инжиниринга (3 слоя)**; **AI engineering vs ML engineering
   vs full-stack**.
2. **Understanding Foundation Models** — обучающие данные (**мультиязычные модели**,
   **доменные модели**); архитектура; размер модели; **post-training (SFT, preference finetuning)**;
   сэмплирование (основы, стратегии, **test-time compute**, **структурированный вывод**,
   **вероятностная природа ИИ**).
3. **Evaluation Methodology** — сложности оценки FM; **метрики языкового моделирования: энтропия,
   кросс-энтропия, bits-per-character / bits-per-byte, перплексия и её интерпретация**;
   точная оценка (**functional correctness**, сходство с эталоном, эмбеддинги);
   **AI as a judge** (зачем, как, ограничения, какие модели годятся в судьи);
   **сравнительная оценка и ранжирование моделей** (сложности, будущее).
4. **Evaluate AI Systems** — критерии (доменная способность, генерация, следование инструкциям,
   **стоимость и латентность**); **выбор модели** (workflow, **build vs buy**,
   **навигация по публичным бенчмаркам**); **проектирование evaluation-пайплайна**
   (оценивать все компоненты, гайдлайн оценки, методы и данные).
5. **Prompt Engineering** — ICL zero/few-shot; system vs user prompt; **длина и эффективность
   контекста**; практики (ясные инструкции, контекст, декомпозиция, «дать время подумать»,
   итерации, инструменты, **организация и версионирование промптов**);
   **защитный промпт-инжиниринг** (**проприетарные промпты и reverse prompt engineering**,
   jailbreaking и prompt injection, **извлечение информации**, защиты).
6. **RAG and Agents** — архитектура RAG; алгоритмы поиска; оптимизация retrieval;
   **RAG за пределами текста**; агенты (обзор, инструменты, **планирование**,
   **режимы отказов агентов и их оценка**); **память**.
7. **Finetuning** — когда дообучать и когда нет; **finetuning vs RAG**;
   узкие места по памяти (backprop и обучаемые параметры, **memory math**,
   **численные представления**, квантизация); техники (PEFT,
   **model merging и multi-task finetuning**, тактики дообучения).
8. **Dataset Engineering** — курирование данных (**качество, покрытие, количество**,
   получение и разметка); **аугментация и синтез** (зачем, традиционные техники,
   **синтез с помощью ИИ**, **дистилляция модели**); обработка (инспекция, **дедупликация**,
   очистка и фильтрация, форматирование).
9. **Inference Optimization** — обзор инференса; **метрики производительности инференса**;
   **AI-ускорители**; оптимизация модели и оптимизация сервиса инференса.
10. **AI Engineering Architecture and User Feedback** — пошаговая архитектура (контекст → guardrails →
    **роутер и gateway** → кэши → агентные паттерны); мониторинг и observability;
    **оркестрация AI-пайплайна**; **обратная связь пользователей** (извлечение диалоговой обратной
    связи, **дизайн обратной связи**, **ограничения обратной связи**).

Ценность: самая свежая карта LLM-продакшена. Грейд: middle+ (LLM-роли).

### 7. Build a Large Language Model From Scratch — Raschka [ОТКРЫЛ]

Главы: 1. Understanding LLMs · 2. Working with Text Data · 3. Coding Attention Mechanisms ·
4. Implementing a GPT Model from Scratch · 5. Pretraining on Unlabeled Data ·
6. Finetuning for Text Classification · 7. Finetuning to Follow Instructions.
Приложения: A. PyTorch · B. References · C. Exercise Solutions ·
D. Bells and Whistles to the Training Loop · E. PEFT with LoRA.

Bonus-материал (важен, потому что это и есть «продвинутая» часть программы):
BPE-токенизатор с нуля; сравнение embedding-слоёв; интуиция даталоадера;
эффективные реализации multi-head attention; **PyTorch buffers**; **подсчёт FLOPs**; **KV-cache**;
**альтернативы attention: Grouped-Query, Multi-Head Latent Attention, Sliding Window**;
**Mixture-of-Experts**; загрузка весов, претрейн на Project Gutenberg, LR-шедулеры, тюнинг
гиперпараметров, UI; конвертация GPT→Llama/Qwen3/Gemma/Olmo/Aya; эксперименты с дообучением слоёв;
классификация IMDb; утилиты датасетов, оценка модели, **генерация instruction-датасета**, **DPO**.

Ценность: единственный источник, где всё пишется руками. Грейд: middle.

### 8. Designing Data-Intensive Applications [ОТКРЫЛ 1-е изд.; 2-е — ТОЛЬКО ОПИСАНИЕ]

1-е издание:
- **Part I. Foundations of Data Systems** — 1. Reliability, Scalability, Maintainability ·
  2. **Data Models and Query Languages** · 3. **Storage and Retrieval** (LSM vs B-tree, индексы,
  колоночное хранение) · 4. **Encoding and Evolution** (Avro/Protobuf/Thrift,
  **обратная и прямая совместимость схем**).
- **Part II. Distributed Data** — 5. **Replication** · 6. **Partitioning** · 7. **Transactions**
  (уровни изоляции) · 8. **The Trouble with Distributed Systems** (часы, частичные отказы) ·
  9. **Consistency and Consensus** (линеаризуемость, CAP, кворумы, консенсус).
- **Part III. Derived Data** — 10. **Batch Processing** · 11. **Stream Processing** (CDC, event
  sourcing, обработка по времени события, exactly-once) · 12. **The Future of Data Systems**.

2-е издание (2026) [ТОЛЬКО ОПИСАНИЕ]: добавлены «Trade-offs in Data Systems Architecture» и
**«Defining Nonfunctional Requirements»**; partitioning переименован в **sharding**;
глава про consistency/consensus переписана.

Ценность: инфраструктурная часть ML System Design. Грейд: middle+.

### 9. Trustworthy Online Controlled Experiments — Kohavi, Tang, Xu [ТОЛЬКО ОПИСАНИЕ]

- **Part I. Introductory Topics for Everyone** — 1. Introduction and Motivation ·
  2. Running and Analyzing Experiments · 3. **Twyman's Law and Experimentation Trustworthiness** ·
  4. **Experimentation Platform and Culture**.
- **Part II. Selected Topics for Everyone** — 5. **Speed Matters: An End-to-End Case Study** ·
  6. **Organizational Metrics** · 7. **Metrics for Experimentation and the OEC** ·
  8. **Institutional Memory and Meta-analysis** · 9. **Ethics in Controlled Experiments**.
- **Part III. Complementary and Alternative Techniques** — 10. **Complementary Techniques**
  (логи, опросы, фокус-группы, UX-исследования, human evaluation) ·
  11. **Observational Causal Studies**.
- **Part IV. Advanced Topics for Building an Experimentation Platform** —
  12. **Client-side Experiments** · 13. **Instrumentation** · 14. Choosing a Randomization Unit ·
  15. Ramping Experiment Exposure · 16. **Scaling Experiment Analyses**.
- **Part V. Advanced Topics for Analyzing Experiments** — 17. The Statistics Behind OCE ·
  18. Variance Estimation and Improved Sensitivity · 19. The A/A Test ·
  20. **Triggering for Improved Sensitivity** · 21. Guardrail Metrics ·
  22. Leakage and Interference Between Variants · 23. Measuring Long-Term Treatment Effects.

Ценность: канон по A/B. Грейд: middle → middle+.

### 10. Practical Statistics for Data Scientists, 2-е изд. [ОТКРЫЛ секции глав 1–7]

1. **Exploratory Data Analysis** — оценки положения; оценки разброса; перцентили и боксплоты;
   частотные таблицы и гистограммы; оценки плотности; бинарные и категориальные данные; корреляция.
2. **Data and Sampling Distributions** — выборочное распределение статистики; бутстрап;
   доверительные интервалы; нормальное распределение; **стандартное нормальное и QQ-графики**;
   **длиннохвостые распределения**; биномиальное; **пуассоновское, экспоненциальное, Вейбулла**.
3. **Statistical Experiments and Significance Testing** — ресэмплинг; значимость и p-value; t-тесты;
   **ANOVA и F-статистика (включая двухфакторный)**; χ²-тест (и его ресэмплинговая версия);
   **точный тест Фишера**; мощность и размер выборки.
4. **Regression and Prediction** — простая линейная регрессия (уравнение, остатки);
   множественная (оценка модели, **выбор модели и пошаговая регрессия/AIC**, **взвешенная регрессия**);
   факторные переменные (дамми, **много уровней**); интерпретация коэффициентов
   (**коррелированные предикторы**, **конфаундеры**, **взаимодействия и главные эффекты**);
   **диагностика регрессии: выбросы, влиятельные наблюдения (Кука), гетероскедастичность,
   ненормальность и коррелированные ошибки, графики частных остатков и нелинейность,
   полиномиальная и сплайновая регрессия, обобщённые аддитивные модели (GAM)**.
5. **Classification** — наивный Байес; **дискриминантный анализ (LDA)**; логистическая регрессия
   (**связь с GLM**, odds ratio, оценка модели); оценка классификаторов (матрица ошибок,
   precision/recall/**specificity**, ROC, AUC); стратегии при дисбалансе (undersampling,
   oversampling и веса, генерация данных).
6. **Statistical Machine Learning** — kNN (**стандартизация**, **kNN как feature engine**);
   деревья (рекурсивное разбиение, меры неоднородности); бэггинг и RF (**важность переменных**);
   бустинг (XGBoost, регуляризация, гиперпараметры и кросс-валидация).
7. **Unsupervised Learning** — PCA (**интерпретация компонент**, **корреспондентный анализ**);
   k-means (алгоритм, интерпретация кластеров, выбор k); иерархическая (дендрограмма,
   меры несходства); **модельная кластеризация (смеси нормальных, выбор числа компонент)**;
   масштабирование и категориальные переменные (**доминирующие переменные**,
   **расстояние Гауэра и проблемы кластеризации смешанных типов**).

Ценность: покрывает «статистическую» секцию собеса аналитиков и MLE. Грейд: junior → middle.

### 11. Speech and Language Processing, 3-е изд. — Jurafsky & Martin [ТОЛЬКО ОПИСАНИЕ]

- **Part I. Fundamental Algorithms** — 1. Introduction · 2. **Regular Expressions, Tokenization,
  Edit Distance** · 3. **N-gram Language Models** · 4. Naive Bayes, Text Classification, Sentiment ·
  5. Logistic Regression · 6. Vector Semantics and Embeddings · 7. Neural Networks ·
  8. RNNs and LSTMs · 9. Transformers · 10. Large Language Models · 11. Masked Language Models ·
  12. Model Alignment, Prompting, and In-Context Learning.
- **Part II. NLP Applications** — 13. Machine Translation · 14. **Question Answering, Information
  Retrieval, and RAG** · 15. **Chatbots and Dialogue Systems** · 16. ASR and TTS.
- **Part III. Annotating Linguistic Structure** — 17. Sequence Labeling for POS and Named Entities ·
  18. **Context-Free Grammars and Constituency Parsing** · 19. **Dependency Parsing** ·
  20. **Information Extraction: Relations, Events, and Time** · 21. **Semantic Role Labeling** ·
  22. **Lexicons for Sentiment, Affect, and Connotation** ·
  23. **Coreference Resolution and Entity Linking** · 24. **Discourse Coherence**.
- **Веб-приложения** — A. **Hidden Markov Models** · B. **Spelling Correction and the Noisy Channel** ·
  C. Statistical Constituency Parsing · D. CFG · E. CCG · F. **Logical Representations of Sentence
  Meaning** · G. **Word Senses and WordNet** · H. Phonetics.

Ценность: единственный источник, где классический NLP-инструментарий не выкинут. Грейд: middle.

### 12. Machine Learning System Design Interview — Aminian & Xu [ТОЛЬКО ОПИСАНИЕ]

1. Introduction and Overview (**7-шаговый фреймворк**) · 2. **Visual Search System** ·
3. **Google Street View Blurring System** · 4. **YouTube Video Search** ·
5. **Harmful Content Detection** · 6. Video Recommendation System ·
7. **Event Recommendation System** · 8. Ad Click Prediction on Social Platforms ·
9. **Similar Listings on Vacation Rental Platforms** · 10. Personalized News Feed ·
11. **People You May Know**.

Ценность: набор кейсов, которые дословно спрашивают. Грейд: middle → middle+.

### 13. Recommender Systems Handbook, 3-е изд. [ТОЛЬКО ОПИСАНИЕ]

Пять частей: (1) общие техники рекомендаций — коллаборативная фильтрация, семантические методы,
**рекомендации по неявной обратной связи**, **глубокие нейросети (гл. 5)**,
**контекстно-зависимые рекомендации (гл. 6)**; (2) специальные техники — **сессионные рекомендации**,
**состязательное ML для RecSys (гл. 9: атаки, защиты)**, **групповые рекомендации**,
**реципрокные рекомендации**, **NLP-техники для RecSys**, **кросс-доменные рекомендации (гл. 13)**;
(3) ценность и влияние — **оценка рекомендательных систем (гл. 15)**, **их бизнес-ценность**,
**мультистейкхолдерная перспектива**, **справедливость (гл. 18)**,
**новизна и разнообразие (гл. 16)**; (4) человеко-машинное взаимодействие —
**объяснения (гл. 19: за пределами объяснения одного айтема)**, **личность пользователя**,
**поддержка индивидуальных и групповых решений**; (5) применения — еда, музыка, мода, мультимедиа.

Ценность: единственный источник по «неалгоритмической» половине рекомендаций. Грейд: middle+.

### 14. Reliable Machine Learning — Chen, Murphy, Parisa, Sculley, Underwood [ТОЛЬКО ОПИСАНИЕ, частично]

Подтверждённые главы: 1. Introduction · 2. **Data Management Principles** · 4. **Feature and
Training Data** · 8. Serving · 9. Monitoring and Observability for Models · 10. **Continuous ML** ·
11. **Incident Response** · 15. **Case Studies: MLOps in Practice**.
Подтверждённые сквозные темы: **ML Lifecycle** (сбор и анализ данных, обучающие пайплайны,
сборка и валидация приложений, оценка качества, **определение и измерение SLO**, запуск,
мониторинг и петли обратной связи); **Data as Liability** (фазы данных: создание, приём,
обработка, хранение, управление, анализ и визуализация; **надёжность данных**: durability,
consistency, **version control**, performance, availability, **integrity**, **security**,
**privacy**, **policy and compliance**); **Fairness** (определения справедливости,
как её добиваться, справедливость как процесс); **Privacy**; **Responsible AI**;
**Training Systems** (признаки, feature stores, системы управления моделями, оркестрация, мониторинг).

Ценность: SRE-взгляд на ML — SLO, error budget, дежурство. Грейд: middle+.

### 15. Machine Learning Engineering — Burkov [ТОЛЬКО ОПИСАНИЕ]

Порядок глав по жизненному циклу: 1. Introduction · 2. **Before the Project Starts**
(**приоритизация ML-проектов, оценка сложности и стоимости, состав команды, когда ML не нужен**) ·
3. Data Collection and Preparation · 4. Feature Engineering ·
5. Supervised Model Training · 6. Model Evaluation (**офлайн и онлайн**,
**статистические границы качества / доверительные интервалы для метрик**) ·
7. Model Deployment (**паттерны и стратегии деплоя, упаковка модели и кода, автоматизация**) ·
8. Model Serving, Monitoring, and Maintenance.

### 16. The Hundred-Page Machine Learning Book — Burkov [ТОЛЬКО ОПИСАНИЕ]

1. Introduction · 2. Notation and Definitions · 3. Fundamental Algorithms ·
4. Anatomy of a Learning Algorithm · 5. Basic Practice · 6. Neural Networks and Deep Learning ·
7. Problems and Solutions (дисбаланс, **комбинирование моделей**, **несколько входов/выходов**,
transfer learning, **алгоритмическая эффективность**) · 8. Advanced Practice ·
9. Unsupervised Learning · 10. **Other Forms of Learning** (**metric learning**, learning to rank,
learning to recommend, **word embeddings**) · 11. Conclusion (**тематическое моделирование**,
**GLM**, GAN, RL, **one-shot / zero-shot**).

---

## ДЕЛЬТА: темы, которых нет в нашем манифесте

Правило: если тема в манифесте есть (пусть кратко) — не пишу. Ниже только то, чего нет.

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Подбор гиперпараметров как отдельная дисциплина: grid/random search, Bayesian optimization/TPE, Hyperband, Successive Halving, ASHA, multi-fidelity, асинхронный HPO, Optuna** | d2l гл. 19 (5 секций); Murphy кн.2 §6.6 «Bayesian optimization» | В манифесте есть «тюнинг по шагам» только для бустинга. Вопрос «как подобрать гиперпараметры, когда обучение стоит часы» — стандартный на middle+; ASHA/Hyperband — то, что реально крутится в проде | `docs/02-classic-ml/08-boosting-in-practice.md` (практика) + `docs/03-deep-learning/02-training-dynamics.md` (для DL) |
| **Основы RL: MDP, value iteration, Q-learning, policy gradient, advantage** | d2l гл. 17; UDL гл. 19; Murphy кн.2 гл. 35 | У нас есть RLHF/PPO/GRPO в `05-llm/03` и бандиты, но без MDP/advantage объяснить PPO нечем. Спрашивают на LLM-ролях | `docs/05-llm/03-sft-and-alignment.md` (преамбула «RL за 3 страницы») |
| **Генеративные модели: VAE (ELBO, репараметризация, posterior collapse, VQ-VAE), GAN, нормализующие потоки, energy-based/score matching** | UDL гл. 15–17; Murphy кн.2 гл. 21–24; d2l гл. 20 | Полностью отсутствуют в манифесте. VAE/VQ-VAE — база для semantic IDs в рекомендациях (у нас есть TIGER в `06-recsys/11`, но без VQ) | новая тема в `docs/03-deep-learning/` — вписать в `06-scaling-and-efficiency.md` нельзя; логичнее расширить `docs/13-optional/03-multimodal.md` или завести подраздел в `03-deep-learning/03-cnn-and-rnn.md` |
| **Диффузионные модели: DDPM, score-based/SDE, ускорение сэмплирования, conditional generation, guidance** | UDL гл. 18; Murphy кн.2 гл. 25 | Отдельная продуктовая область (картинки/видео/аудио), спрашивают даже не-CV инженеров как «что вы знаете о современных генеративных моделях» | `docs/13-optional/01-computer-vision.md` (обзорно) + упоминание в `docs/13-optional/03-multimodal.md` |
| **Double descent, grokking, lottery ticket, ландшафт функции потерь, flat minima, неявная регуляризация SGD** | UDL гл. 20 | Прямо ломает классический bias-variance, который у нас в `02-classic-ml/01`. Любимый вопрос «почему переобученная сеть обобщает» | `docs/02-classic-ml/01-learning-theory.md` (расширить bias-variance) + `docs/03-deep-learning/02-training-dynamics.md` |
| **Fairness/справедливость: demographic parity, equalized odds, equal opportunity, невозможность одновременного выполнения, дебиасинг pre/in/post-processing, аудит по срезам** | UDL гл. 21; DMLS гл. 11 (Responsible AI); Reliable ML (Fairness); RecSys Handbook гл. 18 | В манифесте нет ни одной строки про fairness. На middle+ спрашивают в связке с регуляторкой и с продуктовыми рисками | `docs/09-monitoring/01-what-to-monitor.md` (срезовый анализ) + отдельный блок в `docs/07-mlops/01-ml-lifecycle.md` |
| **Безопасность ML-модели: data poisoning, adversarial examples, model extraction/stealing, membership inference, защита** | Murphy кн.2 §19.8; RecSys Handbook гл. 9 «Adversarial Recommender Systems: Attack, Defense»; Reliable ML (security) | У нас безопасность есть только для LLM (`05-llm/10`, prompt injection). Атаки на рекомендательные и антифрод-модели — реальный прод-риск | `docs/05-llm/10-llm-safety-and-guardrails.md` расширить до «безопасность ML-систем» + кейс в `docs/11-system-design/04-case-fraud-detection.md` |
| **Конформальное предсказание (conformal prediction) и оценка неопределённости с гарантиями** | Murphy кн.2 §14.3 | Единственный способ дать честный интервал на предсказание без байесовщины; всё чаще спрашивают вместе с калибровкой | `docs/02-classic-ml/12-imbalance-and-calibration.md` |
| **Обобщённые линейные модели: пуассоновская регрессия, гамма/Tweedie, функции связи, offset/exposure** | Murphy кн.1 гл. 12; Practical Statistics §5 (GLM); Hundred-Page гл. 11 | Счётные и денежные таргеты (заказы, страховые выплаты, спрос) — регулярные задачи; MSE на них неправильный | `docs/02-classic-ml/02-linear-models.md` |
| **Диагностика регрессии: гетероскедастичность, влиятельные наблюдения (расстояние Кука), графики частных остатков, VIF, взаимодействия, AIC/пошаговый отбор, взвешенная регрессия** | Practical Statistics гл. 4 | «Модель хорошая по R², но что не так» — базовый вопрос на аналитической секции; у нас в `02-linear-models` только мультиколлинеарность | `docs/02-classic-ml/02-linear-models.md` |
| **Сплайны и GAM (обобщённые аддитивные модели)** | Practical Statistics §4; Murphy кн.1 §11.5 | Интерпретируемая нелинейность — то, что просят в кредитном скоринге и в медицине вместо бустинга | `docs/02-classic-ml/02-linear-models.md` |
| **LDA/QDA (дискриминантный анализ), генеративные vs дискриминативные классификаторы** | Murphy кн.1 гл. 9; Practical Statistics §5 | Классический вопрос «чем naive Bayes отличается от логрегрессии»; у нас в `09-svm-knn-bayes` только NB | `docs/02-classic-ml/09-svm-knn-bayes.md` |
| **Робастная регрессия (Huber, Student-t) и робастная логрегрессия** | Murphy кн.1 §11.6, §10.4 | Выбросы в проде — норма; знание, что менять loss, а не выкидывать данные | `docs/02-classic-ml/02-linear-models.md` |
| **Байесовская статистика для практики: сопряжённые априорные, credible intervals, empirical Bayes, иерархические модели, байесовский A/B** | Murphy кн.1 §4.6; Murphy кн.2 гл. 3, §34.3 | Байесовский A/B и «probability to be best» спрашивают на всех продуктовых собесах; у нас в `10-ab-testing` только частотный подход | `docs/10-ab-testing/02-statistical-criteria.md` + `docs/01-math/03-statistics.md` |
| **Теория решений: матрица потерь, Байес-оптимальное правило, cost-sensitive порог, опция «отказаться от предсказания» (reject option)** | Murphy кн.1 гл. 5 | Порог у нас выбирается «по метрике», а спрашивают «по деньгам»: FP и FN стоят разного | `docs/02-classic-ml/04-metrics.md` |
| **Доверительные интервалы для метрик качества (бутстрап AUC, сравнение двух моделей статистически)** | Burkov MLE гл. 6 «Model Evaluation» | «Модель А лучше модели Б на 0.3% AUC — это значимо?» — вопрос, на котором сыпятся | `docs/02-classic-ml/04-metrics.md` |
| **ANOVA / F-тест, точный тест Фишера** | Practical Statistics гл. 3 | Многовариантные A/B (3+ группы) и малые выборки в конверсиях | `docs/10-ab-testing/02-statistical-criteria.md` |
| **Пуассоновский процесс, экспоненциальное распределение, Вейбулл, длиннохвостые распределения, QQ-графики** | Practical Statistics гл. 2 | Моделирование потока событий, time-to-event, диагностика хвостов перед t-тестом | `docs/01-math/02-probability.md` |
| **Экспоненциальное семейство, достаточные статистики, натуральные параметры** | Murphy кн.1 §3.4; кн.2 §2.4 | Связывает softmax, логрегрессию, GLM и MaxEnt в одну картинку — «почему именно такая функция потерь» | `docs/01-math/03-statistics.md` |
| **Оптимизация 2-го порядка (Ньютон, квазиньютон/L-BFGS), проксимальные методы, MM/EM как оптимизация, безградиентная оптимизация** | Murphy кн.1 гл. 8; кн.2 гл. 6 | У нас в `01-math/04` только 1-й порядок; L-BFGS реально используется в логрегрессии/CRF, а EM у нас упоминается лишь в GMM | `docs/01-math/04-optimization.md` |
| **Обучение при дефиците разметки: active learning, semi-supervised, weak supervision / programmatic labeling (Snorkel), self-training, meta-learning, few-shot** | Murphy кн.1 гл. 19; DMLS гл. 4 | «Разметки нет / бюджет 10k примеров — что делаете?» — вопрос почти на каждом собесе; в манифесте нет ни active learning, ни weak supervision | `docs/02-classic-ml/14-feature-engineering.md` не подходит — нужна вставка в `docs/07-mlops/03-data-and-feature-store.md` или расширение `docs/02-classic-ml/13-validation-and-leakage.md`; оптимально — блок в `docs/07-mlops/01-ml-lifecycle.md` |
| **Стратегии сэмплирования данных: reservoir sampling, importance sampling, взвешенное и стратифицированное сэмплирование для сбора обучающих данных** | DMLS гл. 4 | Reservoir sampling для потоков — классическая задача кодинг-секции и реальная задача логирования; у нас сэмплирование не описано нигде | `docs/08-big-data/05-streaming.md` (потоки) + `docs/12-coding/04-algorithms.md` (как задача) |
| **Metric learning / обучение метрик расстояния (contrastive, triplet loss, ArcFace)** | Murphy кн.1 §16.2; Hundred-Page гл. 10 | Основа visual search, дедупликации, антифрод-матчинга и двухбашенных моделей; у нас есть in-batch negatives, но нет самой темы лоссов метрик | `docs/06-recsys/06-two-tower-and-ann.md` + `docs/13-optional/03-multimodal.md` |
| **Тематическое моделирование: LDA, NMF, оценка когерентности** | Murphy кн.2 §28.5; Hundred-Page гл. 11 | Всё ещё первый бейзлайн для «разбери 10 млн отзывов на темы»; в манифесте отсутствует | `docs/04-nlp/05-nlp-tasks-and-metrics.md` |
| **ICA и факторный анализ** | Murphy кн.1 §20.2; кн.2 §28.3, §28.6 | Дополняет PCA там, где нужна независимость, а не декорреляция (сигналы, сенсоры) | `docs/02-classic-ml/11-dimensionality-reduction.md` |
| **Спектральная кластеризация, бикластеризация, кластеризация смешанных типов (расстояние Гауэра), доминирующие переменные при масштабировании** | Murphy кн.1 §21.5–21.6; Practical Statistics гл. 7 | «Как кластеризовать таблицу, где есть и категории, и числа» — практический вопрос без ответа в текущем манифесте | `docs/02-classic-ml/10-clustering.md` |
| **HMM, фильтр Калмана, линейные динамические системы, структурные модели временных рядов (BSTS)** | Murphy кн.2 гл. 8, гл. 29; SLP3 приложение A | HMM — база для CTC/ASR и для sequence labeling; Кальман и BSTS — для сглаживания метрик и causal impact | `docs/02-classic-ml/16-time-series.md` |
| **CRF и структурное предсказание для sequence labeling** | Murphy кн.2 §4.4; SLP3 гл. 17 | BiLSTM-CRF и BERT-CRF до сих пор дефолт в NER-проде; у нас в `04-nlp/05` только схема BIO | `docs/04-nlp/05-nlp-tasks-and-metrics.md` |
| **Графические модели (байесовские сети, MRF), d-разделение** | Murphy кн.1 §3.6; кн.2 гл. 4 | Язык, на котором формулируются причинные графы и допущения; нужен для главы про uplift | `docs/02-classic-ml/17-uplift-and-causal.md` |
| **Причинные DAG, backdoor/frontdoor-критерий, do-исчисление, проверки правдоподобности (sensitivity analysis, negative controls, refutation tests)** | Murphy кн.2 гл. 36; Kohavi гл. 11 «Observational Causal Studies» | В `02-classic-ml/17` есть DiD/IV/propensity, но нет самого аппарата «какие переменные контролировать» и как проверять устойчивость вывода | `docs/02-classic-ml/17-uplift-and-causal.md` |
| **Адаптация к сдвигу распределений: importance weighting при covariate shift, domain adaptation, robustness, continual learning и катастрофическое забывание** | Murphy кн.2 гл. 19; DMLS гл. 9 | У нас `09-monitoring/03` только детектирует дрифт; вопрос «обнаружили — что делать» закрыт слабо | `docs/09-monitoring/03-drift-detection.md` + `docs/09-monitoring/07-retraining.md` |
| **Stateless retraining vs stateful (инкрементальное) обучение, 4 стадии continual learning** | DMLS гл. 9; Reliable ML гл. 10 «Continuous ML» | «Дообучать с нуля или инкрементально» — прямой вопрос в `07-retraining`, но самих терминов и стадий зрелости в манифесте нет | `docs/09-monitoring/07-retraining.md` |
| **Slice-based evaluation, perturbation/invariance/directional-expectation тесты модели (поведенческое тестирование, CheckList-подход)** | DMLS гл. 6 | Это то, что реально называют «тестами модели» в CI; в `12-coding/07` тесты описаны, но без этой таксономии | `docs/12-coding/07-testing-and-code-quality.md` + `docs/07-mlops/07-ci-cd-for-ml.md` |
| **AutoML: soft/hard AutoML, NAS, learned optimizers** | DMLS гл. 6 | Вопрос «зачем нам DS, если есть AutoML» и практический выбор между AutoML и ручным пайплайном | `docs/02-classic-ml/08-boosting-in-practice.md` |
| **Edge/on-device ML: компиляция под устройство, компиляторы и IR (TVM/XLA), ML в браузере (WASM)** | DMLS гл. 7 | Латентность и приватность гонят инференс на устройство; у нас есть ONNX/TensorRT, но не сама постановка | `docs/07-mlops/09-inference-optimization.md` |
| **Аппаратная сторона: иерархия памяти, пропускная способность, arithmetic intensity/roofline, специфика GPU/TPU-ускорителей** | d2l §13.4 «hardware»; AI Engineering §9 «AI Accelerators» | Без roofline нельзя объяснить, почему decode memory-bound и почему батчинг помогает; у нас есть вывод, но не модель | `docs/05-llm/05-inference-and-serving.md` + `docs/07-mlops/10-cost-and-capacity.md` |
| **Parameter server как альтернатива all-reduce; синхронный/асинхронный SGD в такой архитектуре** | d2l §13.7 | В `08-big-data/07` есть только all-reduce; PS всё ещё живёт в рекламных системах с гигантскими эмбеддингами | `docs/08-big-data/07-distributed-training.md` |
| **Imperative vs symbolic исполнение, `torch.compile`/графовый режим, асинхронное вычисление, авто-параллелизм** | d2l §13.1–13.3 | Ускорение обучения «бесплатно» и типовой вопрос «как ускорили обучение» | `docs/03-deep-learning/05-pytorch-in-practice.md` |
| **Model merging и multi-task finetuning (model soups, task arithmetic, TIES/DARE)** | AI Engineering §7 «Model Merging and Multi-Task Finetuning» | Дешёвая альтернатива мультизадачному дообучению; в `05-llm/04` есть только слияние LoRA-адаптеров | `docs/05-llm/04-peft-and-quantization.md` |
| **Test-time compute как ось масштабирования (best-of-N, verifier, reasoning-модели)** | AI Engineering §2 «Test Time Compute» | Отдельный рычаг качества наравне с обучением; в `05-llm/06` есть только self-consistency | `docs/05-llm/02-pretraining-and-scaling.md` + `docs/05-llm/06-prompting-and-structured-output.md` |
| **Bits-per-character / bits-per-byte как метрики LM и их связь с перплексией при разной токенизации** | AI Engineering §3 | Перплексии несравнимы между токенизаторами — типичная ошибка при сравнении моделей | `docs/05-llm/02-pretraining-and-scaling.md` |
| **Dataset engineering для дообучения: покрытие, необходимое количество, синтез данных ИИ и его риски (model collapse), дедупликация SFT-данных** | AI Engineering гл. 8 | «Сколько примеров нужно для SFT и где их взять» — практический вопрос на LLM-собесе; в `05-llm/03` описан формат, но не инженерия датасета | `docs/05-llm/03-sft-and-alignment.md` |
| **Дизайн пользовательской обратной связи: извлечение диалогового фидбэка, явный vs неявный сигнал, ограничения и смещения фидбэка** | AI Engineering §10 «User Feedback» | Источник данных для дообучения и для онлайн-метрик LLM-продукта | `docs/05-llm/09-llm-evaluation.md` |
| **Reverse prompt engineering / извлечение системного промпта как класс атак** | AI Engineering §5 «Defensive Prompt Engineering» | В `05-llm/10` есть injection и jailbreak, но не кража промпта — а это бизнес-риск | `docs/05-llm/10-llm-safety-and-guardrails.md` |
| **MLA (Multi-Head Latent Attention) и sliding-window attention как альтернативы GQA** | Raschka, bonus гл. 4 | В `05-llm/01` есть GQA/MQA/MoE; MLA (DeepSeek) и SWA (Mistral) — то, что сейчас спрашивают про сжатие KV-кэша | `docs/05-llm/01-llm-architecture.md` |
| **Триггерирование (triggering) для повышения чувствительности A/B + counterfactual triggering** | Kohavi гл. 20 | Самый действенный после CUPED способ поднять чувствительность; в `10-ab-testing/03` его нет | `docs/10-ab-testing/03-variance-reduction.md` |
| **Инструментирование и качество логов эксперимента; client-side эксперименты (мобильные релиз-поезда, отложенное обновление, эффект «не обновился»)** | Kohavi гл. 12–13 | Мобильные A/B ломаются иначе, чем веб; спрашивают в продуктовых компаниях | `docs/10-ab-testing/04-pitfalls.md` |
| **Платформа экспериментов и культура: фазы зрелости (crawl→walk→run→fly), масштабирование анализа экспериментов, институциональная память и мета-анализ накопленных тестов** | Kohavi гл. 4, 8, 16 | Вопрос уровня middle+ «как построить экспериментальную платформу на 100 тестов в неделю» | `docs/10-ab-testing/01-experiment-design.md` |
| **Альтернативы A/B: логи-анализ, опросы, фокус-группы, UX-исследования, человеческая оценка — и когда A/B неприменим** | Kohavi гл. 10 | На собесе ценится ответ «здесь A/B не нужен/невозможен, вот чем заменить» | `docs/10-ab-testing/05-complex-designs.md` |
| **Этика экспериментов: информированное согласие, риски для пользователя, что нельзя тестировать** | Kohavi гл. 9 | Регуляторно значимо и всплывает в поведенческой секции | `docs/10-ab-testing/04-pitfalls.md` |
| **Latency/скорость как объект эксперимента (slowdown-эксперименты, связь латентности с деньгами)** | Kohavi гл. 5 «Speed Matters» | Даёт цифру, которой обосновывают бюджет латентности в system design | `docs/11-system-design/01-framework.md` + `docs/07-mlops/10-cost-and-capacity.md` |
| **Управление данными как обязательством: приватность, retention, GDPR/удаление, происхождение и целостность данных, комплаенс, версионирование данных** | Reliable ML гл. 2 «Data Management Principles», «Data as Liability» | Право на забвение → переобучение модели без пользователя; вопрос всплывает в fintech/health | `docs/07-mlops/03-data-and-feature-store.md` |
| **SLO/error budget для ML-сервиса в терминах SRE и обучение дежурных** | Reliable ML («Defining and Measuring SLOs») | В `09-monitoring/01` есть SLI/SLO, но нет error budget как механизма принятия решений о релизах | `docs/09-monitoring/01-what-to-monitor.md` |
| **Репликация, шардирование, транзакции и уровни изоляции, линеаризуемость/CAP, консенсус** | DDIA ч. II (гл. 5–9) | Всплывает, как только ML System Design упирается в хранилище фич и в консистентность онлайн/офлайн | `docs/08-big-data/01-storage-and-formats.md` + `docs/11-system-design/01-framework.md` |
| **Эволюция схем и совместимость (backward/forward), Avro/Protobuf как контракт между продьюсером и консьюмером** | DDIA гл. 4 | Ломающееся изменение схемы — самая частая причина «модель молча деградировала»; у нас есть контракты данных, но не правила совместимости | `docs/07-mlops/03-data-and-feature-store.md` + `docs/09-monitoring/02-data-quality.md` |
| **CDC (change data capture) и event sourcing как способ строить фичи из БД** | DDIA гл. 11 | Практический способ получить near-real-time фичи без двойной записи | `docs/08-big-data/05-streaming.md` |
| **Нефункциональные требования как отдельный шаг проектирования (2-е изд. DDIA)** | DDIA 2-е изд., гл. «Defining Nonfunctional Requirements» | Прямо ложится в первый шаг нашего фреймворка system design | `docs/11-system-design/01-framework.md` |
| **Кейс: детекция вредного контента (мультимодальная модерация, ранняя/поздняя фузия, сильный дисбаланс, многозадачность, human-in-the-loop)** | Aminian гл. 5 | Один из 3–4 самых частых кейсов ML System Design; у нас его нет | новый кейс в `docs/11-system-design/` (или врезка в `04-case-fraud-detection.md`) |
| **Кейс: визуальный поиск / поиск похожих изображений (эмбеддинги + ANN + contrastive обучение)** | Aminian гл. 2, 9 | Второй частый кейс; переиспользует наши two-tower и ANN, но с другой постановкой | врезка в `docs/06-recsys/06-two-tower-and-ann.md` или новый кейс в `docs/11-system-design/` |
| **Кейс: «люди, которых вы можете знать» (графовые признаки, генерация кандидатов по графу, ранжирование связей)** | Aminian гл. 11 | Третий частый кейс; наш `06-recsys/10` описывает графовые модели, но не постановку friend-recommendation | врезка в `docs/06-recsys/10-graph-recsys.md` |
| **Кейс: рекомендации событий (сильная временная и гео-локальность, «одноразовые» айтемы, экстремальный холодный старт)** | Aminian гл. 7 | Показывает границы обычного CF: айтем живёт один раз | врезка в `docs/06-recsys/12-cold-start-and-bias.md` |
| **Мультистейкхолдерные рекомендации (интересы пользователя vs поставщика vs платформы) и бизнес-ценность RecSys** | RecSys Handbook, часть 3 | Прямой ответ на «как вы балансируете метрики продавца и покупателя на маркетплейсе» | `docs/06-recsys/01-recsys-foundations.md` |
| **Групповые и реципрокные рекомендации** | RecSys Handbook, часть 2 | Реципрокные — это dating/рекрутинг/маркетплейс труда: матч должен устраивать обе стороны | `docs/06-recsys/01-recsys-foundations.md` |
| **Объяснения рекомендаций (за пределами объяснения одного айтема) и влияние объяснений на доверие** | RecSys Handbook гл. 19, часть 4 | В `06-recsys/11` объяснения упомянуты только как применение LLM; тут — самостоятельная тема с метриками | `docs/06-recsys/11-llm-recsys.md` или `docs/06-recsys/01-recsys-foundations.md` |
| **Кросс-доменные рекомендации (перенос знаний между доменами/сервисами)** | RecSys Handbook гл. 13 | Экосистемы (банк+маркет+медиа) — типичная российская реальность; решает холодный старт нового сервиса | `docs/06-recsys/12-cold-start-and-bias.md` |
| **N-граммные языковые модели и сглаживание (Kneser-Ney, backoff), перплексия для n-грамм** | SLP3 гл. 3 | Спрашивают как проверку понимания «что такое языковая модель до нейросетей»; и это база для интерпретации перплексии | `docs/04-nlp/01-text-representation.md` |
| **Минимальное редакционное расстояние (DP), noisy channel и исправление опечаток** | SLP3 гл. 2, приложение B | Классическая задача кодинг-секции и реальный компонент поиска (fuzzy matching, нормализация запросов) | `docs/12-coding/04-algorithms.md` + `docs/04-nlp/01-text-representation.md` |
| **Извлечение информации: извлечение отношений, событий и времени; связывание сущностей (entity linking); разрешение кореференции** | SLP3 гл. 20, 23 | В `04-nlp/05` есть NER, но продуктовые задачи (граф знаний, аналитика документов) требуют шага после NER | `docs/04-nlp/05-nlp-tasks-and-metrics.md` |
| **Задачно-ориентированные диалоговые системы: фреймы/слоты, dialogue state tracking, политика диалога** | SLP3 гл. 15 | LLM-ассистенты в проде до сих пор строятся вокруг слотов и состояния — без этого агент не проходит эксплуатацию | `docs/05-llm/08-agents-and-tools.md` |
| **Синтаксический разбор (constituency/dependency parsing) и семантические роли** | SLP3 гл. 18, 19, 21 | Низкий приоритет для middle+ MLE, но нужен для правил-based извлечения и для русскоязычных задач с морфологией | упоминанием в `docs/04-nlp/05-nlp-tasks-and-metrics.md` |
| **Приоритизация ML-проектов до старта: оценка целесообразности, стоимости, сложности, когда ML не нужен** | Burkov MLE гл. 2 «Before the Project Starts»; DMLS гл. 1 «When to Use ML» | В `07-mlops/01` есть жизненный цикл, но нет шага «а надо ли вообще»; на middle+ это половина сеньорности | `docs/07-mlops/01-ml-lifecycle.md` |
| **Гауссовы процессы: ядра, апостериор, масштабирование, GP для временных рядов** | d2l гл. 18; Murphy кн.1 гл. 17, кн.2 гл. 18 | Нужны как база под байесовскую оптимизацию гиперпараметров и как честный способ дать неопределённость на малых данных | `docs/02-classic-ml/09-svm-knn-bayes.md` (рядом с ядрами) |
| **Shallow graph embeddings: DeepWalk, node2vec, постановка encoder/decoder** | Murphy кн.1 гл. 23 | В `06-recsys/10` сразу GCN; node2vec — дешёвый и до сих пор рабочий бейзлайн для графовых фич | `docs/06-recsys/10-graph-recsys.md` |
| **Оценка генеративных моделей (FID/IS, likelihood, human eval) и цели генеративного моделирования** | Murphy кн.2 гл. 20 | Нужна, как только в продукте появляется генерация картинок/аудио | `docs/13-optional/03-multimodal.md` |
| **Self-supervised обучение представлений вне текста (SimCLR/BYOL, masked modeling) и оценка качества представлений** | Murphy кн.2 гл. 32; Murphy кн.1 §1.3.3 | В `13-optional/03` есть только CLIP; SSL — способ получить эмбеддинги без разметки для табличных/CV/логовых данных | `docs/13-optional/03-multimodal.md` + `docs/04-nlp/02-embeddings.md` |
| **AutoRec и NeuMF как отдельные архитектуры рекомендаций** | d2l гл. 21 (autorec, neumf) | NeuMF — обязательный бейзлайн в статьях и частый вопрос «чем нейросеть лучше MF» (правильный ответ: часто ничем — см. критику воспроизводимости) | `docs/06-recsys/08-neural-ranking.md` |
| **Adadelta, Adagrad, RMSProp как отдельные оптимизаторы (не только Adam/AdamW)** | d2l гл. 12 | В `01-math/04` и `03-deep-learning/02` есть momentum/Adam/AdamW; Adagrad/RMSProp спрашивают как «откуда взялся Adam» | `docs/01-math/04-optimization.md` |
| **Model store / реестр моделей как компонент платформы и build-vs-buy решения по ML-платформе** | DMLS гл. 10 | В `07-mlops/04` реестр упомянут; build vs buy для платформы — вопрос архитектурного уровня на middle+ | `docs/07-mlops/01-ml-lifecycle.md` |

---

## Чего найти не удалось

1. **Полные подглавы Understanding Deep Learning.** Репозиторий `udlbook/udlbook` через
   `raw.githubusercontent.com` отдаёт 404 на `README.md` в ветках `main` и `master`; сайт книги и
   MIT Press закрыты прокси. Есть только список 21 главы (через bookclub-репозиторий) и описания
   глав 20–21 из поисковой выдачи. Подглавы (например, конкретные разделы про диффузию) не проверены.
2. **Полное оглавление Recommender Systems Handbook, 3-е изд.** Springer закрыт (403).
   Подтверждены только части и отдельные главы по DOI-суффиксам (5, 6, 9, 13, 15, 16, 18, 19).
   Не удалось подтвердить наличие/названия глав про trust, group recommenders, session-based
   и NLP для RecSys как отдельных глав — они упоминаются только в аннотации частей.
3. **Полное оглавление Reliable Machine Learning.** O'Reilly закрыт. Подтверждены главы
   1, 2, 4, 8, 9, 10, 11, 15; главы 3, 5, 6, 7, 12, 13, 14 не подтверждены по названиям
   (темы Fairness/Privacy/Training Systems встречаются, но привязать к номерам главы не получилось).
4. **Точное оглавление Machine Learning Engineering (Burkov)** — только реконструкция по стадиям
   жизненного цикла из вторичных источников; `mlebook.com`, `leanpub.com`, `dokumen.pub` закрыты.
5. **Оглавление Practical Statistics for Data Scientists 3-го изд.** — репозиторий второго издания
   сообщает о переезде в `gedeck/ai-assisted-statistics-for-data-scientists`, содержимое не проверялось.
6. **Постраничное оглавление Speech and Language Processing 3rd ed.** — `web.stanford.edu` закрыт,
   список глав собран только из поисковой выдачи; номера глав могут отличаться от актуального
   черновика 2026 года (в выдаче фигурируют новые главы про агентов и RLHF, которых нет в списке 24 глав).
7. **Оглавление ML System Design Interview (Aminian & Xu)** — только список 11 глав-кейсов;
   внутренняя структура каждого кейса (какие шаги фреймворка раскрываются) не получена.
8. **Полный TOC DDIA 2-го издания (2026)** — подтверждены только отдельные новые главы;
   сквозной список 1–13 не собран.
