# ru-universities — прочёс программ

Область: российские университетские / школьные курсы по ML, DL, NLP, RecSys, Speech, MLOps.
Дата прочёса: 2026-07-27.
Цель: собрать **программы** (полные списки тем) и вычислить **дельту** относительно нашего
манифеста `/home/user/ml-handbook/.handbook/STRUCTURE.md` (117 глав).

Пометки: **[ОТКРЫЛ]** — реально получил содержимое; **[ТОЛЬКО ОПИСАНИЕ]** — видел лишь
описание/структуру репозитория без программы; **[НЕ ДОСТУПЕН]** — 403/404/DNS.

---

## Что реально открыл (со ссылками)

### ШАД / Yandex Data School (org: yandexdataschool)

Список репозиториев организации получен целиком (99 публичных репозиториев, GitHub API через
MCP): https://github.com/orgs/yandexdataschool/repositories — **[ОТКРЫЛ]**.
Учебные репозитории (остальное — HEP/физика, соревнования, служебное):
`nlp_course`, `recsys_course`, `Practical_DL`, `Practical_RL`, `deep_vision_and_graphics`,
`speech_course`, `sdc_course`, `crowd_course`, `cuda_course`, `cpp0_course`, `algorithms`,
`python_public`, `asml`, `dlatscale_draft`, `reproducible_analysis_course`,
`ML-Handbook`, `ML-Handbook-materials`, `YSDA_deeplearning17`, `CSC_deeplearning`,
`inverse-problem-intensive`, `MLatImperial2016/2017/2018/2022`, `MLatGradDays`, `mlda`,
`modelgym`, `roc_comparison`, `mlhep*` (серия школ по ML в физике высоких энергий).

- https://github.com/yandexdataschool/nlp_course (ветка `2025`) — **[ОТКРЫЛ]**
- https://github.com/yandexdataschool/recsys_course (ветка `2026_spring`) — **[ОТКРЫЛ]**
- https://github.com/yandexdataschool/Practical_DL (ветка `fall25`) — **[ОТКРЫЛ]** (README обрывается
  на неделе 3 пометкой «to be updated»; полную программу восстановил по именам папок в дереве)
- https://github.com/yandexdataschool/Practical_RL — **[ОТКРЫЛ]**
- https://github.com/yandexdataschool/deep_vision_and_graphics (ветка `fall25`) — **[ОТКРЫЛ]**
- https://github.com/yandexdataschool/speech_course — **[ОТКРЫЛ]**
- https://github.com/yandexdataschool/crowd_course — **[ОТКРЫЛ]** (2 лекции 2024 + ДЗ)
- https://github.com/yandexdataschool/dlatscale_draft — **[ОТКРЫЛ]**, курс переехал в `mryab/efficient-dl-systems`
- https://github.com/yandexdataschool/cuda_course — **[ТОЛЬКО ОПИСАНИЕ]** (есть `content/`, `slides/`,
  сайт курса на GitHub Pages отдаёт 403)
- https://github.com/yandexdataschool/ML-Handbook-materials — **[ТОЛЬКО ОПИСАНИЕ]**: в `chapters/`
  видны папки `ensembles`, `nlp`, `representation_learning`
- https://github.com/yandexdataschool/asml — **[ТОЛЬКО ОПИСАНИЕ]** (`datasets/`, `notebooks/`, описания нет)
- https://github.com/yandexdataschool/reproducible_analysis_course — **[ТОЛЬКО ОПИСАНИЕ]**
  («A course on tools for collaborative and reproducible machine learning», программы в README нет)

### Efficient DL Systems (ВШЭ + ШАД)
- https://github.com/mryab/efficient-dl-systems — **[ОТКРЫЛ]**

### ВШЭ ФКН
- https://github.com/esokolov/ml-course-hse — **[ОТКРЫЛ]** (README + дерево репозитория:
  семестры с 2016-fall по `ml1-2026-spring` / `ml2-2026-spring`)
- https://github.com/esokolov/ml-course-hse/tree/master/2025-fall/lecture-notes — **[ОТКРЫЛ]**
- https://github.com/esokolov/ml-course-hse/tree/master/2025-spring/lecture-notes — **[ОТКРЫЛ]**
- https://github.com/esokolov/ml-course-hse/tree/master/2023-spring/lecture-notes — **[ОТКРЫЛ]**
- https://github.com/esokolov/ml-course-hse/tree/master/2022-spring/lecture-notes — **[ОТКРЫЛ]** (`tabular_dl.pdf`)
- https://github.com/esokolov/ml-course-hse/tree/master/ml2-2026-spring/seminars — **[ОТКРЫЛ]**
- https://github.com/isadrtdinov/intro-to-dl-hse — **[ОТКРЫЛ]**
- https://github.com/mryab/dl-hse-ami — **[ОТКРЫЛ]**
- https://github.com/elvarid/gnn_course_hse — **[ТОЛЬКО ОПИСАНИЕ]** (страница курса помечена WIP;
  сказано, что курс основан на стэнфордском CS224W)
- https://github.com/Pyatachokk/hse_ts_course — **[ТОЛЬКО ОПИСАНИЕ]** («Моделирование временных рядов»,
  ФКН ВШЭ, Б. Демешев; в дереве семестры `2020-fall` … `2026-spring`, но имена файлов лекций
  в листинге не раскрылись)
- https://github.com/mannefedov/compling_nlp_hse_course — **[ОТКРЫЛ]** (Школа лингвистики ВШЭ)

### МГУ ВМК (Дьяконов)
- https://github.com/Dyakonov/MSUML — **[ОТКРЫЛ]**
- https://github.com/Dyakonov/PZAD — **[ОТКРЫЛ]**

### МФТИ
- https://github.com/r-isachenko/2025-DGM-MIPT-YSDA-course — **[ОТКРЫЛ]** (совместный МФТИ+ШАД)
- https://github.com/r-isachenko/2021-DGM-Ozon-course — **[ОТКРЫЛ]** (Ozon Masters)
- https://github.com/DLSchool/deep-learning-school — **[ОТКРЫЛ]** (Deep Learning School при ФПМИ МФТИ,
  дерево + программа первой части в README)

### girafe-ai / ODS / прочее
- https://github.com/girafe-ai/ml-course (ветка `master`) — **[ОТКРЫЛ]**
- https://github.com/girafe-ai/ml-course (ветка `23f_yandex_ml_trainings`) — **[ОТКРЫЛ]**
- https://github.com/Yorko/mlcourse.ai — **[ОТКРЫЛ]**
- https://github.com/sb-ai-lab/RecSys-Course (Sber AI Lab) — **[ОТКРЫЛ]**
- https://github.com/sharthZ23/your-second-recsys (ODS «Your Second RecSys») — **[ОТКРЫЛ]**
- https://github.com/anokhin/recsys-course-spring-2024 — **[ТОЛЬКО ОПИСАНИЕ]** (структура сервиса
  `botify`/`sim`/`hw`/`slides` открылась, сама программа лежит PDF-ами в `slides/`, листинг папки — 404)
- https://github.com/bayesgroup/deepbayes-2019 — **[ТОЛЬКО ОПИСАНИЕ]** (`lectures/day1..day6`,
  `seminars/day1..day6`, названия файлов внутри не раскрылись)
- https://github.com/IrinaGoloshchapova/ml_system_design_doc_ru — **[ОТКРЫЛ]** (шаблон ML System Design Doc)

---

## Программы (по каждому источнику — полный список тем)

### 1. ШАД — NLP course (`yandexdataschool/nlp_course`, ветка 2025) [ОТКРЫЛ]
Ценность: эталонная современная программа NLP/LLM. Грейд: middle → middle+/senior.

1. Word Embeddings
2. Language Modeling
3. Seq2seq and Attention
4. Transfer Learning
5. Large Language Models
6. Prompting & In-Context Learning
7. Fine-tuning (PEFT & RLHF)
8. Efficiency
9. Retrieval-Augmented Generation (RAG)
10. AI Agents
11. **Interpretability**
12. Multimodal LLMs
13. Building LLM Systems
14. AI Agents in Production

### 2. ШАД — RecSys course (`yandexdataschool/recsys_course`, ветка 2026_spring) [ОТКРЫЛ]
Ценность: самая свежая индустриальная программа по рекомендациям на русском рынке.
Грейд: middle+ / senior RecSys.

- **W1 Intro.** Лекция: обзор курса, постановка задачи рекомендаций. Семинар: базовые
  рекомендатели, латентное пространство user-item.
- **W2 Candidate generation & metrics.** Лекция: метрики рекомендаций, генерация кандидатов —
  классический ML, ANN, смешивание источников. Семинар: обзор контеста yambda, baseline.
- **W3 Ranking, diversity & metrics.** Лекция: реранкинг — лоссы, алгоритмы, метрики;
  **управление разнообразием, MRR / DPP**. Семинар: классические алгоритмы (**MF, SLIM, EASE**);
  ранжирование — построение пула, undersampling, композитные таргеты.
- **W4 DL for RecSys & neural candidate generation.** Двухбашенная архитектура, softmax-модель и
  sampled softmax loss, контрастивное обучение, сэмплирование негативов и LogQ. Семинар: разбор
  статей по LogQ-коррекции и техникам сэмплирования негативов.
- **W5 Neural candidate generation pt.2.** Холодный старт и длинный хвост, стратегии кодирования
  user/item, последовательные модели, за пределами two-tower (**GPU retrieval, генеративный ретривал**).
  Семинар: аспекты обучения нейросетей для RecSys.
- **W6 Neural ranking pt.1.** Зачем DL, кодирование признаков (категориальные, эмбеддинги, скалярные),
  композиция моделей. Семинар: разбор статей про **Piecewise Linear Encoding и Unified Embeddings**.
- **W7 Neural ranking pt.2.** Моделирование взаимодействия признаков, MLP,
  **многозадачность и дистилляция знаний**. Семинар: разбор архитектуры **DCNv2**.
- **W8 System Design pt.1.** Архитектуры данных, логирование, смещения, дрифт данных и мониторинг.
  Семинар: хранилища признаков для разных масштабов.
- **W9 System Design pt.2.** Runtime-дизайн, воронка кандидатов, **GPU-инференс, доставка данных,
  управляемая деградация**, холодный старт. Семинар: разбор статей по GPU-ретривалу — **LiNR, SilverTorch**.
- **W10 RecSys Transformers applications.** Последовательные модели (трансформеры) на истории
  действий пользователя. Семинар: **PinnerFormer & TransAct** (Pinterest).
- **W11 Reinforcement Learning in RecSys.** Бандиты — алгоритмы, Thompson sampling, контекстные
  бандиты. Семинар: применение бандитов и off-policy оценка для e-grocery.
- **W12 Case Studies сервисов Яндекса.** Дизайн рекомендаций для e-grocery, киносервиса,
  ленты блогов и новостей. Практика: разбор рекомендательной системы Лавки.
- **W13 Trends in RecSys.** SOTA-подходы и свежие статьи. Практика: лучшие решения контеста
  yambda retrieval.

### 3. ШАД — Practical_DL (`yandexdataschool/Practical_DL`, ветка fall25) [ОТКРЫЛ]
README обрывается после недели 3; программа восстановлена по именам папок в дереве ветки `fall25`.
Ценность: связка «классический DL → LLM → генеративные модели → инференс → RL → аудио».
Грейд: junior+ → middle.

`week01_backprop`, `week02_autodiff`, `week03_convnets`, `week04_finetuning`,
`week05_interpretability`, `week06_nlp`, `week07_lm`, `week08_transformer`, `week09_llm`,
**`week10_generative`**, **`week11_diffusion`**, `week12_inference`, **`week13_rl`**, `week14_audio`.

Из README (первые 3 недели, дословно):
1. «Deep learning — introduction, backpropagation algorithm, adaptive optimization methods»; семинар — нейросети на numpy.
2. «Deep learning as a language, dropout, batch/layer normalization, other tricks, deep learning frameworks»; семинар — основы PyTorch.
3. «Computer vision tasks, Convolution and Pooling layers, ConvNet architectures, Data Augmentation».

### 4. ШАД — Practical_RL (`yandexdataschool/Practical_RL`) [ОТКРЫЛ]
Ценность: единственный полный русскоязычный курс по RL от индустрии; фундамент под RLHF и бандиты.
Грейд: middle+.

- **week01_intro** — задачи RL вокруг нас; процессы принятия решений; стохастическая оптимизация,
  метод кросс-энтропии; поиск в пространстве параметров vs в пространстве действий.
- **week02_value_based** — MDP с дисконтированием; value-based подход; value iteration; policy iteration.
- **week03_model_free** — Q-learning; SARSA; off-policy vs on-policy; N-шаговые алгоритмы; TD(λ).
- **recap_deep_learning** — Deep learning 101; PyTorch/TF, классификация изображений свёртками.
- **week04_approx_rl** — бесконечное/непрерывное пространство состояний; аппроксимация функции ценности;
  условия сходимости; experience replay, target networks, double/dueling/bootstrap DQN.
- **week05_explore** — контекстные бандиты; Thompson Sampling, UCB, байесовский UCB; исследование в
  model-based RL, MCTS; эвристики исследования.
- **week06_policy_based** — мотивация policy-based; policy gradient; log-derivative trick;
  REINFORCE; снижение дисперсии (baseline); advantage actor-critic, **GAE**.
- **week07_seq2seq** — проблемы последовательных данных; RNN; BPTT; затухание/взрыв градиентов;
  LSTM, GRU; клиппинг градиента.
- **week08_pomdp** — POMDP: обучение агентов с памятью; планирование (POMCP); recurrent A3C, DRQN.
- **week09_policy_II** — TRPO; NPO/PPO; детерминированный policy gradient; DDPG.
- **week10_planning** — model-based RL, планирование, имитационное обучение и inverse RL; MCTS.
- **yet_another_week** — inverse RL и imitation learning.

### 5. ШАД + Сколтех — Deep Vision and Graphics (`yandexdataschool/deep_vision_and_graphics`, fall25) [ОТКРЫЛ]
Ценность: полная CV-программа, включая генеративные модели и 3D. Грейд: middle+ CV.

1. Интро, повтор основ нейросетей, оптимизация, backprop, биологические сети, изображения,
   линейная фильтрация, свёрточные сети, батчнормы, аугментации.
2. Архитектуры ConvNet и как их искать; **разреженные свёртки в 3D**; ConvNet для видео; transfer learning.
3. Несвёрточные архитектуры: трансформеры, **mixers, FFT-свёртки**.
4. Визуализация и понимание глубоких архитектур, **adversarial examples**.
5. Плотное предсказание: семантическая сегментация, суперразрешение/синтез изображений, **perceptual losses**.
6. Детекция объектов, instance/panoptic сегментация, 2D/3D оценка позы человека.
7. **Representation learning: распознавание лиц, задачи верификации, self-supervised learning**, image captioning.
8. **Латентные модели (GLO, AE, VQ-VAE). Flow-модели, CLIP, DALL-E.**
9. **Генеративно-состязательные сети.**
10. **Диффузионные модели, генеративные трансформеры.**
11. Оценка формы и движения: spatial transformers, **оптический поток, стерео, monodepth**,
    генерация облаков точек, неявные и полунеявные представления формы.
12. Синтез новых видов: multi-plane images, **NeRF**, mesh- и point-based представления, нейронные рендереры.

### 6. ШАД — Speech Processing (`yandexdataschool/speech_course`) [ОТКРЫЛ]
Ценность: единственная открытая полная русскоязычная программа по речи. Грейд: middle+ speech.

1. Введение в цифровую обработку сигналов (DSP). Семинар: реализация DSP-пайплайна. ДЗ: мел-спектрограммы.
2. **Voice Activity Detection (VAD) и Sound Event Detection (SED)**; введение в дискриминативные нейромодели речи.
3. **Keyword Spotting и речевая биометрия**; ДЗ: обучение биометрии **ECAPA-TDNN с контрастивным лоссом**.
4. Распознавание речи I. Семинар: **CTC forward-backward, мягкое выравнивание**. ДЗ: **CTC/RNN-T декодирование, RNN-T forward-backward**.
5. **Предобучение в распознавании речи**; семинар: квантизация и лоссы для speech pretraining.
6. **ASR-инференс**; ДЗ: потоковый (streaming) инференс.
7. Введение в TTS: нормализация, задачи, метрики.
8. Акустические модели TTS и вокодинг: **Tacotron2, FastPitch, HiFiGAN**; оценка pitch.
9. **Квантизация и нейронные аудиокодеки**.
10. **Диффузии и трансформеры для клонирования голоса**; ДЗ: slow-fast transformer inference.
11. **Spoken dialogue models**.
13. **Acoustic Echo Cancellation (AEC) и beamforming**.

### 7. ВШЭ + ШАД — Efficient Deep Learning Systems (`mryab/efficient-dl-systems`) [ОТКРЫЛ]
Ценность: главный источник по «железу и инференсу» в русскоязычном пространстве. Грейд: middle+ / senior.

1. **Введение.** Обзор курса. **Ключевые концепции архитектуры GPU и CUDA API.** Семинар: CUDA-операции
   в PyTorch, введение в бенчмаркинг.
2. **Общие оптимизации обучения, профилирование.** Измерение производительности GPU-софта;
   mixed-precision; **оптимизации хранения и загрузки данных**; инструменты профилирования.
   Семинар: AMP в PyTorch; **py-spy, PyTorch Profiler, Memory Snapshot, Nsight Systems**;
   **динамический паддинг для последовательностей и бенчмарки декодирования JPEG**.
3. **Data-parallel обучение и All-Reduce.** Введение в распределённое обучение; All-Reduce и его
   эффективные реализации. Семинар: PyTorch Distributed, примитивы data-parallel.
4. **Методы обучения больших моделей.** Тензорный, пайплайн, **sequence parallelism**;
   gradient checkpointing, **offloading**.
5. **Sharded data-parallel, оптимизации распределённого обучения.** FSDP и его оптимизации.
   Семинар: **PyTorch Device Mesh, DTensor, FSDP2, Distributed Checkpoint**.
6. **Производительность DL из первых принципов.** «**Arithmetic of Deep Learning**».
   Семинар: **kernel fusion, torch.compile, иерархия памяти GPU, Liger kernels**.
7. **Основы деплоя веб-сервиса.**
8. **Системные оптимизации инференса.** Метрики скорости инференса; KV-кэш, батч-инференс,
   continuous batching; FlashAttention и его модификации, PagedAttention; обзор фреймворков сервинга LLM.
   Семинар: утилизация KV-кэша, continuous batching, замеры prefill и decode.
9. **Алгоритмические оптимизации инференса.** Сценарии и метрики инференса LLM; оптимизации архитектуры,
   квантизация, speculative decoding, **сжатие KV-кэша**, дистилляция. Семинар: **доказательство
   сохранения распределения в speculative decoding; матричное умножение на Triton; nsys profile**.
10. Приглашённая лекция.

### 8. ШАД — Crowdsourcing (`yandexdataschool/crowd_course`) [ОТКРЫЛ]
Ценность: единственный найденный курс про разметку как инженерную дисциплину. Грейд: middle+.
Лекции 2024 (по именам файлов):
1. **«Введение. Данные и разметка в ML»** (Никита Курышев)
2. **«Контроль качества и бюджета»** (Юлия Силова)
Плюс домашнее задание `Home_work_3_step_2024`.

### 9. ВШЭ ФКН — Машинное обучение (`esokolov/ml-course-hse`) [ОТКРЫЛ]
Ценность: канонический русскоязычный курс с математическими конспектами. Грейд: junior → middle.
Дерево репозитория: семестры `2016-fall` … `2025-fall`, `2025-spring`, а также
`ml1-2026-spring` и `ml2-2026-spring`.

**Осенний семестр (ML1), по README и конспектам `2025-fall/lecture-notes`:**
вводная лекция → линейная регрессия → линейная регрессия и градиентное обучение →
продвинутые градиентные методы и линейная классификация (`lecture04..06-linclass`) →
метрики качества классификации → логистическая регрессия → SVM и многоклассовая классификация →
`lecture07-deeplearning` → решающие деревья (`lecture09-trees`) → разложение bias-variance →
случайный лес и градиентный бустинг (`lecture10-ensembles`) → стекинг → обучение без учителя и
кластеризация → визуализация и **representation learning** → рекомендательные системы.

**Весенний семестр (ML2), по конспектам `2025-spring/lecture-notes`:**
- lecture13-kernels, lecture14-kernels — **ядровые методы**
- lecture15-em — **EM-алгоритм**
- lecture16-anomaly — поиск аномалий
- lecture17-clusterization — кластеризация
- lecture18-knn — метрические методы

**`ml2-2026-spring/seminars` (новая версия ML2):**
`sem01-pca`, `sem02-clustering`, **`sem03-graph-clustering`**, **`sem04-graph`**.

**`2022-spring/lecture-notes`:** единственный файл — **`tabular_dl.pdf`** (глубокое обучение
для табличных данных).

### 10. ВШЭ ФКН — Введение в глубинное обучение (`isadrtdinov/intro-to-dl-hse`) [ОТКРЫЛ]
Ценность: базовый DL-курс ПМИ. Грейд: junior → middle. Темы семинаров:
1. Введение в PyTorch. Автоматическое дифференцирование. Полносвязные нейросети.
2. Операция свёртки. Свёрточные нейросети для изображений. Аугментации данных.
3. Современные свёрточные архитектуры. Fine-tuning предобученных сетей. Пакетная нормализация.
4. Обработка последовательностей. Рекуррентные нейросети. Генерация последовательностей.
5. Модуль внимания (attention). Архитектура трансформера.
6. **Дистилляция и прореживание (pruning) нейронных сетей.**
ДЗ: PyTorch и полносвязные сети; классификация изображений; тексты, эмбеддинги, RNN и трансформеры;
бонус — kNN и автоэнкодеры.

### 11. ВШЭ ФКН — Глубинное обучение (`mryab/dl-hse-ami`) [ОТКРЫЛ]
Ценность: продвинутая версия DL-курса. Грейд: middle+. Модули:
Introduction → Core concepts: automatic differentiation; architectures; training and regularization;
best practices → Advanced: applications to Computer Vision; applications to NLP; Transformer models;
**Adversarial X**; **Probabilistic models**; **Differentiable programming**; **Non-differentiable models**
→ приглашённые доклады.

### 12. ВШЭ Школа лингвистики — Компьютерная лингвистика (`mannefedov/compling_nlp_hse_course`) [ОТКРЫЛ]
Ценность: «классический» NLP-слой, которого нет в трансформерных курсах. Грейд: junior → middle.
Вводная часть: regexps; ngrams; **lexical disambiguation**; language classification; basic LLM usage.
Основная часть:
1. Предобработка текста
2. Классификация текста (мешок слов)
3. **Поиск и исправление опечаток (spellchecking)**
4. Базовое языковое моделирование
5. Векторные представления слов
6. CNN
7. RNN и извлечение именованных сущностей
8. BERT
9. GPT
10. Машинный перевод
11. Instruct fine-tuning. Quantization, PEFT
12. Reinforcement learning
13. Multimodality (vision) — CLIP, SigLIP, VQGAN
14. Multimodality (vision) — nanovlm, VQGAN + LLM
15. Multimodality (audio)

### 13. МГУ ВМК — Методы машинного обучения (`Dyakonov/MSUML`) [ОТКРЫЛ]
Ценность: самая широкая «классическая» программа. Грейд: junior → middle.
1. Вводная лекция · 2. Питон и его библиотеки · 3. Постановка основных задач ·
4. Метрические алгоритмы · 5. Линейная регрессия · 6. Оптимизация в ML · 7. Логистическая регрессия ·
8. Выбор модели · 9. Линейные классификаторы, SVM · 10. Нелинейные методы, трюки с ядрами ·
11. Сложность алгоритмов, переобучение, смещение и разброс · 12. Деревья решений ·
13. Ансамбли алгоритмов · 14. Случайные леса и AdaBoost · 15. Градиентный бустинг ·
16. Селекция (отбор) признаков · 17. Функции ошибки и функционалы качества · 18. Нейронные сети ·
19. Борьба с переобучением в нейронных сетях · 20. Архитектуры нейросетей ·
**21. Ассоциативные правила** · 22. Кластеризация · 23. Качество кластеризации · 24. EM-алгоритм ·
25. Обучение без учителя · 26. Другие методы понижения размерности · 27. Детектирование аномалий ·
28. Байесовский подход · 29. Рекомендательные системы · 30. Ранжирование ·
**31. Специальные задачи: многоклассовые, с частичной разметкой, активное обучение**

### 14. МГУ ВМК — Прикладные задачи анализа данных (`Dyakonov/PZAD`) [ОТКРЫЛ]
Ценность: прикладной курс с очень подробным блоком метрик и графов. Грейд: middle.
1. Введение · 2. Оценки среднего, вероятности и плотности; весовые схемы · 3. CASE: прогнозирование
визитов покупателей супермаркетов · 4. CASE: задача о пробках · 5. Искусство визуализации (ч.1,
историческая) · 6. Игра «Что изображено?» · 7. Искусство визуализации (ч.2, одномерный анализ) ·
8. Искусство визуализации (ч.3, многомерный анализ: корреляции, диаграммы рассеивания, сводные таблицы) ·
9. **Метрики качества ч.1: функции ошибки в регрессии** — MAE, MSE, RMSE, R², **функция Хьюбера** ·
10. **Метрики ч.2: чёткая бинарная классификация** — матрица ошибок, Accuracy, Recall, Precision, F1,
**каппа Коэна** · 11. **Метрики ч.3: скоринговые функции и кривые** — Log Loss, ROC, AUROC,
**GINI, Gain и Lift Curves** · 12. **Метрики ч.4: многоклассовые задачи, ранжирование, кластеризация** —
**многоклассовый AUC-ROC**, MAP, MRR, DCG, оценка кластеризации · 13. Метрики: задачи и кейсы ·
14. Подготовка данных: очистка, сокращение, трансформация · 15. Генерация признаков: типы числовых
признаков, **контекстные признаки, служебные признаки** · 16. Ансамбли: бэггинг, стекинг, AdaBoost ·
17. Случайный лес: OOB, параметры · 18. **Важность признаков в ансамблях деревьев**: impurity-based,
перестановочная, **Boruta, ACE** · 19. **Анализ социальных/сложных сетей**: теория графов,
**степенные законы, модель малого мира**, кластеризация · 20. **Прогнозирование появления ребра в
динамическом графе**: признаковые пространства по графам, сходство вершин ·
21. **Выделение сообществ**: методы разбиения графа, **модулярность, спектральная теория** ·
22. Градиентный бустинг: TreeBoost, XGBoost, LightGBM, CatBoost.
Дополнительные/планировавшиеся темы: рекомендательные системы; DL в рекомендациях; интерпретация;
отбор признаков; детектирование аномалий; спектральная теория графов; **теория нечётких множеств**;
**анализ выживаемости**; бизнес-аспекты.

### 15. МФТИ + ШАД — Deep Generative Models (`r-isachenko/2025-DGM-MIPT-YSDA-course`) [ОТКРЫЛ]
Ценность: полная современная программа по генеративным моделям, от AR до flow matching и
дискретной диффузии. Грейд: middle+ / senior.
- **L1.** Обзор и мотивация генеративных моделей. Постановка задачи. Divergence minimization framework.
  Авторегрессионные модели (ImageGPT). *Сем.: MLE, гистограммы, теорема Байеса, PixelCNN, VAR.*
- **L2.** Normalizing Flow: линейные NF, гауссовский авторегрессионный NF, coupling layer (RealNVP).
  Latent Variable Models. *Сем.: planar и radial flows; forward vs reverse KL.*
- **L3.** LVM. **Вариационная нижняя оценка (ELBO). Амортизированный вывод. Градиенты ELBO,
  reparametrization trick. VAE.**
- **L4.** Дискретные латентные представления VAE. **Векторное квантование, straight-through
  оценка градиента (VQ-VAE). ELBO surgery и оптимальный prior. Обучаемый prior.**
  *Сем.: GMM и MLE, ELBO и EM-алгоритм, вариационный EM для GMM.*
- **L5.** Likelihood-free обучение. Теорема оптимальности GAN. Расстояние Вассерштейна. WGAN.
  *Сем.: VAE — детали реализации, posterior collapse, beta-VAE.*
- **L6.** **Оценка генеративных моделей (FID, Precision-Recall, CLIP score, human eval).**
  Динамика Ланжевена. **Score matching. Denoising score matching.**
  *Сем.: vanilla GAN в 1D, mode collapse и затухание градиентов, non-saturating GAN, WGAN-GP.*
- **L7.** Denoising score matching. **NCSN**. Прямой гауссовский диффузионный процесс.
  Denoising score matching для диффузии. Обратный процесс. *Сем.: Progressive Growing GAN, StyleGAN.*
- **L8.** Гауссовская диффузия как VAE. **ELBO для DDPM.** Репараметризация и обзор DDPM.
- **L9.** Диффузия как score-based модель. **Guidance: classifier guidance, classifier-free guidance.**
  Continuous-in-time NF и **neural ODE**. *Сем.: DDPM, DDIM.*
- **L10.** Уравнение непрерывности для log-likelihood NF. Основы SDE. Уравнение Колмогорова–Фоккера–Планка.
  Probability flow ODE. Обратное SDE. *Сем.: guidance; CLIP, GLIDE, DALL-E 2, Imagen.*
- **L11.** Variance Preserving и Variance Exploding SDE. Score-based модели через SDE. **Flow matching.**
  *Сем.: Latent Diffusion Model, Stable Diffusion.*
- **L12.** **Conditional flow matching.** Конические гауссовские пути. Линейная интерполяция.
  *Сем.: методы управления LDM — **ControlNet, IP-Adapter, Dreambooth, LoRA**.*
- **L13.** Связь с диффузией и score matching. **Дискретная диффузия**: прямой и обратный дискретный
  процесс, дискретный ELBO.
- **L14.** **Дискретная диффузия для последовательностей. Absorbing diffusion. Continuous-time
  masked diffusion language model.**

Более ранняя версия (`2021-DGM-Ozon-course`) [ОТКРЫЛ] дополнительно содержала: MADE, WaveNet,
PixelCNN++; mean-field приближение; **автогрессионные flows (MAF, IAF), flow KL duality,
uniform/variational dequantization; IWAE; VampPrior + авторегрессионный prior; posterior collapse;
disentanglement learning (beta-VAE, DIP-VAE)**; DCGAN; **Spectral Normalization GAN; f-divergence
minimization; Inception score; AVB**; **FFJORD**; **Gumbel-Softmax, VQ-VAE-2, DALL-E**.

### 16. МФТИ — Deep Learning School, часть 1 (`DLSchool/deep-learning-school`) [ОТКРЫЛ]
Ценность: школьный/вводный уровень. Грейд: junior.
1. Python: основы, Google Colab · 2. Введение в линейную алгебру, векторы, матрицы, NumPy ·
3. Pandas и Matplotlib, основы ML · 4. Элементы теории оптимизации, градиент, градиентный спуск,
линейные модели · 5. Основы машинного обучения · 6. Линейные модели · 7. Композиции алгоритмов и
выбор модели · 8. Введение в DL, свёрточные сети, PyTorch, свёрточный и пулинг-слой ·
9. Transfer Learning, популярные архитектуры CV · 10. Сегментация: SegNet, U-Net ·
11. Object Detection: YOLOv3 · 12. Автоэнкодеры · 13. Классический GAN, нейронный перенос стиля.

### 17. girafe-ai — ML course (`girafe-ai/ml-course`, master) [ОТКРЫЛ]
Ценность: базовый курс МФТИ/ВШЭ-формата. Грейд: junior. Последний семестр в `master` — осень 2022.
W1 Intro, Naive Bayes, kNN · доп. неделя — повтор линейной алгебры · W2 Linear Regression ·
W3 Linear Classification · W4 SVM, PCA · W5 Trees and ensembles · W6 Gradient boosting ·
W7 разбор контрольной · W8 Intro into Deep Learning · W9 Backpropagation ·
W10 Dropout and Batchnorm · W11 Embeddings and seq2seq model.

### 18. girafe-ai — Тренировки по ML Яндекса, осень 2023 (ветка `23f_yandex_ml_trainings`) [ОТКРЫЛ]
Ценность: интенсив «под собес». Грейд: junior → middle.
1. Введение, kNN, Naive Bayes: задачи ML, формальная постановка обучения с учителем, правдоподобие,
наивный байесовский классификатор · 2. Линейная регрессия и регуляризация: аналитическое решение,
неустойчивость, **теорема Гаусса–Маркова**, L1/L2 · 3. Линейная классификация, метод максимального
правдоподобия: отступ, логистическая функция потерь, оценка качества · 4. Решающие деревья,
композиции, Random Forest: информационные критерии, бутстрап, бэггинг · 5. Градиентный бустинг ·
6. Основы Deep Learning · 7. **Интерпретация предсказаний** · 8. **Механизм дистилляции**, методы
обучения с учителем.

### 19. ODS — mlcourse.ai (`Yorko/mlcourse.ai`) [ОТКРЫЛ]
Ценность: классический открытый курс ODS. Грейд: junior → middle.
1. EDA с Pandas · 2. Визуальный анализ данных · 3. Классификация, решающие деревья и kNN ·
4. Линейная классификация и регрессия · 5. Бэггинг и случайный лес · 6. Feature Engineering и
Feature Selection · 7. Обучение без учителя: PCA и кластеризация ·
8. **Vowpal Wabbit: обучение на гигабайтах данных** (SGD, онлайн-обучение) ·
9. Анализ временных рядов (ARIMA) + Prophet · 10. Градиентный бустинг (XGBoost, LightGBM, CatBoost).

### 20. Sber AI Lab — RecSys-Course (`sb-ai-lab/RecSys-Course`) [ОТКРЫЛ]
Ценность: структурированная русскоязычная программа RecSys с папками-практикумами. Грейд: junior+ → middle.
**Модуль 1. Введение:** 1. Введение и постановка задачи · 2. Предобработка и разбиение данных ·
3. Метрики · 4. Классификация алгоритмов, неперсонализированные алгоритмы.
**Модуль 2. Базовые алгоритмы:** 5. ItemKNN, UserKNN · 6. **SLIM, EASE** ·
7. Матричная факторизация: SVD, ALS, iALS · 8. Ранжирующие лоссы (**Triplet loss**, BPR, WARP) ·
9. Гибридные модели: факторизационные машины, **LightFM** · 10. Двухуровневые модели.
**Модуль 3. Продвинутые:** 11. Нейросетевые подходы · 12. Рекомендации на последовательностях ·
13. RL (бандиты) · 14. Графовые подходы.
**Модуль 4. В проде:** 15. Масштабирование (**Spark, Polars**) · 16. ANN ·
17. Особенности построения рекомендаций в проде.
Папки: `02_splits`, `03_metrics`, `04_nonpers`, `05_knn`, `06_slim`, `07_matrix_factorization`,
`08_bpr`, `09_lightfm`, `10_two_stage`, `11_neural`, `12_sequence`, `13_rl`, `14_graph`,
`15_spark`, `16_ann`, `17_production`.

### 21. ODS — Your Second RecSys (`sharthZ23/your-second-recsys`) [ОТКРЫЛ]
Ценность: продуктово-инженерный взгляд. Грейд: middle.
**Ч.1 Your first money/experiment:** 1. Бизнес-эффект от рекомендаций · 2. Дополнительные методы
оценки качества рекомендаций.
**Ч.2 Your first prod:** 3. Рекомендации в проде · 4. Ускорение рекомендаций в проде.
**Ч.3 Your second model:** 5. Двухэтапная модель · 6. Нейросетевая матричная факторизация и DSSM.
Соревнование на данных онлайн-кинотеатра КИОН.

### 22. ML System Design Doc (`IrinaGoloshchapova/ml_system_design_doc_ru`, Reliable ML) [ОТКРЫЛ]
Ценность: шаблон дизайн-документа — артефакт, который просят на секции ML System Design. Грейд: middle+.
1. **Цели и предпосылки** — 1.1 Зачем идём в разработку продукта · 1.2 Бизнес-требования и
ограничения · 1.3 Что входит в скоуп проекта/итерации, что не входит · 1.4 Предпосылки решения.
2. **Методология** — 2.1 Постановка задачи · 2.2 Блок-схема решения · 2.3 Этапы решения задачи.
3. **Подготовка пилота** — 3.1 Способ оценки пилота · 3.2 Что считаем успешным пилотом ·
3.3 Подготовка пилота.
4. **Внедрение** — 4.1 Архитектура решения · 4.2 Описание инфраструктуры и масштабируемости ·
4.3 Требования к работе системы · 4.4 **Безопасность системы** · 4.5 **Безопасность данных** ·
4.6 **Издержки** · 4.7 **Integration points** · 4.8 **Риски**.

---

## ДЕЛЬТА: темы, которых нет в нашем манифесте

Проверено против всех 117 глав `STRUCTURE.md`. Темы, которые у нас **уже есть**
(RAG, агенты, PEFT/LoRA, квантизация, speculative decoding, FlashAttention/PagedAttention,
KV-кэш, DDP/FSDP/ZeRO, bias-variance, бустинги, LambdaMART, two-tower + logQ, HNSW/IVF-PQ,
SASRec/BERT4Rec, LightGCN, TIGER/semantic IDs, CUPED, дельта-метод, дрифт/PSI, feature store,
uplift, бандиты и off-policy, интерпретируемость SHAP/LIME, CTC/Whisper, CLIP) — **не включены**.

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Генеративные модели: VAE (ELBO, reparametrization trick), GAN (теорема оптимальности, mode collapse, WGAN), диффузия (DDPM/DDIM, classifier-free guidance), normalizing flows, flow matching** | DGM МФТИ+ШАД L1–L12; Practical_DL `week10_generative`, `week11_diffusion`; deep_vision_and_graphics W8–W10 | Целого класса моделей у нас нет вообще. На собесах middle+ спрашивают ELBO и reparametrization trick как проверку понимания вариационного вывода; диффузия — база для любого продукта с генерацией картинок/аудио | **Новая глава** `docs/03-deep-learning/07-generative-models.md`; краткая врезка в `13-optional/01-computer-vision.md` |
| **Дискретные латентные представления: векторное квантование, VQ-VAE, straight-through estimator, Gumbel-Softmax** | DGM L4 и `2021-DGM-Ozon` L13; deep_vision_and_graphics W8 | Это механика, на которой стоят semantic IDs в генеративном ретривале (у нас есть TIGER, но без объяснения, откуда берутся ID) и нейронные аудиокодеки | `docs/03-deep-learning/07-generative-models.md` (новая) + ссылка из `06-recsys/11-llm-recsys.md` |
| **Оценка генеративных моделей: FID, Inception Score, Precision-Recall для генеративных моделей, CLIP score, human eval** | DGM L6; `2021-DGM-Ozon` L11–L12 | Отдельный класс метрик; вопрос «как измерите качество генерации» — типовой на секции метрик | `docs/03-deep-learning/07-generative-models.md` (новая) |
| **Основы RL: MDP, value/policy iteration, Q-learning, SARSA, TD(λ), DQN (replay, target net, double/dueling), policy gradient, REINFORCE, actor-critic, GAE, TRPO/PPO как общий алгоритм** | Practical_RL W1–W10; Practical_DL `week13_rl`; recsys_course W11 | У нас PPO/GRPO появляются сразу внутри RLHF, без фундамента. На собесе по RLHF просят объяснить, что такое advantage и почему нужен baseline | Расширить `docs/05-llm/03-sft-and-alignment.md` **или** новая `docs/03-deep-learning/08-rl-foundations.md` |
| **Вариационный вывод: ELBO, amortized inference, mean-field, вариационный EM, posterior collapse** | DGM L3–L4 + семинар 4; `2021-DGM-Ozon` L2, L4; bayesgroup/deepbayes | У нас EM есть только в контексте GMM. Вариационный вывод — общий инструмент и обязательная база под VAE и байесовские методы | Расширить `docs/02-classic-ml/10-clustering.md` (блок EM) + новая глава по генеративным моделям |
| **Глубокое обучение для табличных данных: FT-Transformer/NODE/TabNet, эмбеддинги числовых признаков, piecewise linear encoding, когда нейросеть обходит GBDT** | `esokolov/ml-course-hse` `2022-spring/lecture-notes/tabular_dl.pdf`; recsys_course W6 (PLE, Unified Embeddings) | Прямой вопрос на собесе: «почему на табличке бустинг, а когда нет?». В рекомендательных ранкерах кодирование скалярных признаков — рабочая тема 2024–2026 | Новый раздел в `docs/02-classic-ml/08-boosting-in-practice.md`; кодирование числовых — в `06-recsys/08-neural-ranking.md` |
| **CUDA и производительность из первых принципов: модель GPU, arithmetic intensity, kernel fusion, torch.compile, Triton, иерархия памяти GPU, Liger kernels** | efficient-dl-systems W1, W6, W9; `yandexdataschool/cuda_course` | Отличает middle от middle+ в вопросах «почему инференс медленный». У нас есть FSDP и квантизация, но нет уровня «что происходит на устройстве» | Новый блок в `docs/03-deep-learning/06-scaling-and-efficiency.md` + `docs/07-mlops/09-inference-optimization.md` |
| **Профилирование DL-кода: py-spy, PyTorch Profiler, Memory Snapshot, Nsight Systems/nsys; оптимизация загрузки данных, динамический паддинг, стоимость декодирования JPEG** | efficient-dl-systems W2 | Практический навык, который спрашивают через кейс «обучение упирается не в GPU — что делать». У нас «профилирование» упомянуто одним словом | `docs/03-deep-learning/05-pytorch-in-practice.md` (расширить блок профилирования) |
| **Сжатие KV-кэша** | efficient-dl-systems W9 | У нас KV-кэш есть, но только про размер; сжатие — стандартный рычаг экономии памяти при длинном контексте | `docs/05-llm/05-inference-and-serving.md` |
| **Краудсорсинг и разметка как инженерная дисциплина: организация разметки, контроль качества, агрегация меток, согласованность разметчиков, бюджет** | `yandexdataschool/crowd_course` (обе лекции 2024); косвенно ML System Design Doc §3 | Middle+ отвечает за то, откуда берётся таргет. Вопрос «как вы собирали разметку и как убедились, что она качественная» звучит на секции по данным и на LLM-оценке | Новая глава `docs/09-monitoring/08-data-labeling.md` **или** большой раздел в `docs/02-classic-ml/13-validation-and-leakage.md` / `05-llm/09-llm-evaluation.md` |
| **Каппа Коэна и согласие разметчиков** | Dyakonov/PZAD лекция 10 | Единственная метрика, которой измеряют качество разметки; напрямую связана с предыдущим пунктом | `docs/02-classic-ml/04-metrics.md` |
| **Lift и Gain кривые, коэффициент Джини (GINI) как метрика скоринга** | Dyakonov/PZAD лекция 11 | Стандарт в банковском/скоринговом и маркетинговом ML; на собесах в финтехе спрашивают вместо ROC-AUC | `docs/02-classic-ml/04-metrics.md` |
| **Многоклассовый ROC-AUC (macro/micro/OvR/OvO) и функция Хьюбера** | Dyakonov/PZAD лекции 9, 12 | У нас ROC-AUC разобран только для бинарного случая; Huber — стандартный робастный лосс регрессии | `docs/02-classic-ml/04-metrics.md` |
| **Анализ выживаемости (survival analysis): цензурирование, Каплан–Майер, модель Кокса** | Dyakonov/PZAD (доп. темы) | Правильная постановка для оттока, времени до события, времени жизни клиента — часто ошибочно решается как бинарная классификация | `docs/02-classic-ml/16-time-series.md` (отдельный раздел) или `11-system-design/07-case-churn-uplift.md` |
| **Ассоциативные правила: Apriori, FP-growth, support/confidence/lift, анализ корзины** | Dyakonov/MSUML лекция 21; PZAD | Базовый ретейл-инструмент и частый источник «дешёвых» кандидатов в рекомендациях; спрашивают в e-commerce | `docs/06-recsys/01-recsys-foundations.md` или `docs/02-classic-ml/10-clustering.md` |
| **Активное обучение (active learning): стратегии выбора объектов, uncertainty/diversity sampling** | Dyakonov/MSUML лекция 31 | Прямо связано с бюджетом разметки; типовой ответ на «данных мало, размечать дорого» | Новая глава по разметке **или** `docs/02-classic-ml/14-feature-engineering.md` (блок «мало данных») |
| **Обучение с частичной разметкой: semi-supervised, self-training, PU-learning** | Dyakonov/MSUML лекция 31 | Реальная постановка в антифроде и в задачах с редким позитивом (у нас есть дисбаланс, но не «нет негативов вовсе») | `docs/02-classic-ml/12-imbalance-and-calibration.md` или `docs/11-system-design/04-case-fraud-detection.md` |
| **Графовое ML вне рекомендаций: node2vec/DeepWalk, выделение сообществ, модулярность, спектральная кластеризация, link prediction в динамическом графе, степенные законы, модель малого мира** | Dyakonov/PZAD лекции 19–21; `esokolov` `ml2-2026-spring` `sem03-graph-clustering`, `sem04-graph`; `elvarid/gnn_course_hse` | У нас граф есть только внутри `06-recsys/10-graph-recsys` (GCN/GraphSAGE/LightGCN). Спектральная кластеризация отсутствует и в главе про кластеризацию. Link prediction — самостоятельная постановка (антифрод, соцсети) | Спектральную кластеризацию — в `docs/02-classic-ml/10-clustering.md`; node2vec, сообщества, link prediction — расширить `docs/06-recsys/10-graph-recsys.md` |
| **Тематическое моделирование: PLSA, LDA, ARTM/BigARTM, регуляризаторы, мультимодальные тематические модели** | К. В. Воронцов, курсы «Вероятностные тематические модели» и «Математические методы анализа текстов» **[ТОЛЬКО ОПИСАНИЕ]** — сайт machinelearning.ru отдаёт 403; `ancatmara/data-science-nlp` **[ТОЛЬКО ОПИСАНИЕ]** | Классический способ разметить большой корпус без учителя; всё ещё живёт в аналитике текстов и в холодном старте контентных рекомендаций | `docs/04-nlp/01-text-representation.md` или `docs/04-nlp/05-nlp-tasks-and-metrics.md` |
| **Исправление опечаток и коррекция запросов (spellchecking, noisy channel, расстояние Левенштейна, fuzzy matching)** | `mannefedov/compling_nlp_hse_course` п.3 | Обязательный слой любого поиска и любого продукта с пользовательским вводом; у нас в кейсе поиска не разобран | `docs/04-nlp/05-nlp-tasks-and-metrics.md` + `docs/11-system-design/03-case-search.md` |
| **Разрешение лексической неоднозначности (lexical disambiguation), морфология для русского** | `mannefedov/compling_nlp_hse_course` (вводная часть) | Специфика русского языка при токенизации/лемматизации; у нас есть «токенизация для русского», но не разбор неоднозначности | `docs/04-nlp/01-text-representation.md` |
| **Интерпретируемость LLM (механистическая): probing, анализ голов внимания, разреженные автоэнкодеры** | `nlp_course` W11; Practical_DL `week05_interpretability`; girafe-ai ML-тренировки лекция 7 | У нас интерпретируемость — только классическая (SHAP/LIME/PDP). Для LLM-продуктов диагностика галлюцинаций через анализ внутренностей — растущая тема | `docs/05-llm/09-llm-evaluation.md` (новый раздел) или `docs/02-classic-ml/15-interpretability.md` (врезка «а что с LLM») |
| **Adversarial-атаки и безопасность ML вне LLM: adversarial examples, отравление обучающих данных, кража модели, безопасность данных и системы** | deep_vision_and_graphics W4; `mryab/dl-hse-ami` («Adversarial X»); ML System Design Doc §4.4–4.5 | У нас безопасность есть только для LLM (prompt injection, PII). Для антифрода и любого внешнего API вопрос «как модель атакуют» — прямой | `docs/09-monitoring/06-incidents-and-runbooks.md` или новая глава в `07-mlops`; врезка в `11-system-design/04-case-fraud-detection.md` |
| **ML System Design Doc как письменный артефакт: структура дизайн-дока, пилот и критерии успеха пилота, integration points, издержки, реестр рисков** | `IrinaGoloshchapova/ml_system_design_doc_ru` (полный шаблон) | У нас `11-system-design/01-framework` — устный каркас ответа на собесе. Письменный дизайн-док — то, что middle+ пишет на работе, и его часто просят приложить к тестовому | `docs/11-system-design/01-framework.md` (раздел «дизайн-док») |
| **Диверсификация выдачи: MMR, DPP как алгоритм переранжирования** | recsys_course W3 («diversity control and MRR / DPP») | У нас разнообразие есть как **метрика**, но нет **алгоритма**, который его обеспечивает. Типовой вопрос: «лента однообразная — что сделаете?» | `docs/06-recsys/07-learning-to-rank.md` или `docs/06-recsys/14-recsys-in-production.md` |
| **SLIM и EASE (item-item регрессионные модели)** | recsys_course W3 (семинар); `sb-ai-lab/RecSys-Course` модуль 6 | EASE — сильный и почти бесплатный baseline с решением в замкнутой форме; регулярно бьёт нейросети на небольших каталогах | `docs/06-recsys/03-collaborative-filtering.md` |
| **DCN/DCNv2 — явное моделирование пересечений признаков (cross network)** | recsys_course W7 (разбор архитектуры DCNv2) | Стандарт индустриального CTR-ранкера наравне с DLRM, которого у нас нет | `docs/06-recsys/08-neural-ranking.md` |
| **Дистилляция знаний внутри ранкера (teacher-student между стадиями воронки)** | recsys_course W7 | Способ перенести качество тяжёлого ранкера в лёгкий — частый ответ на «как уложиться в латентность» | `docs/06-recsys/08-neural-ranking.md` или `docs/06-recsys/14-recsys-in-production.md` |
| **GPU-ретривал и управляемая деградация (LiNR, SilverTorch), доставка данных в рантайме** | recsys_course W9 | Свежая индустриальная альтернатива ANN на CPU; «управляемая деградация» — то, чего ждут от middle+ в вопросах про отказоустойчивость | `docs/06-recsys/06-two-tower-and-ann.md` + `docs/06-recsys/14-recsys-in-production.md` |
| **LightFM и гибридные факторизационные модели с признаками** | `sb-ai-lab/RecSys-Course` модуль 9 | Рабочая библиотека для холодного старта; у нас есть FM/DeepFM, но не гибридная схема с side features как отдельный инструмент | `docs/06-recsys/05-factorization-machines.md` |
| **Triplet loss и metric learning (в т.ч. ArcFace, задачи верификации)** | `sb-ai-lab/RecSys-Course` модуль 8; deep_vision_and_graphics W7; speech_course W3 (ECAPA-TDNN с контрастивным лоссом) | Общая техника для верификации, дедупликации, матчинга и биометрии. У нас контрастивное обучение упомянуто только в связке с CLIP | `docs/13-optional/03-multimodal.md` (расширить) или `docs/03-deep-learning/07-generative-models.md`-соседняя врезка; матчинг — `docs/04-nlp/05-nlp-tasks-and-metrics.md` |
| **Self-supervised learning как отдельная парадигма (pretext-задачи, SimCLR-подобные схемы)** | deep_vision_and_graphics W7; `mryab/dl-hse-ami` | Ответ на «данных много, разметки нет»; у нас предобучение раскрыто только для текста | `docs/13-optional/01-computer-vision.md` + врезка в `docs/03-deep-learning/02-training-dynamics.md` |
| **Речь за пределами ASR: VAD, Sound Event Detection, keyword spotting, речевая биометрия/верификация диктора, RNN-T (forward-backward и декодирование), нейронные аудиокодеки, AEC и beamforming, streaming-инференс** | `yandexdataschool/speech_course` W2–W6, W9, W13 | Наша глава по звуку покрывает сигнал, CTC, Whisper и TTS. Всё, что делает голосовой продукт продуктом (детекция речи, активация по слову, кто говорит, эхоподавление, потоковость), отсутствует | `docs/13-optional/02-audio-and-speech.md` (существенно расширить) |
| **Spoken dialogue models (речевые диалоговые модели end-to-end)** | `speech_course` W11 | Быстро растущий класс продуктов (голосовые ассистенты на LLM); связывает наши разделы LLM и звука | `docs/13-optional/02-audio-and-speech.md` или `docs/13-optional/03-multimodal.md` |
| **Хэширование признаков (hashing trick) и онлайн-обучение на потоке (Vowpal Wabbit, FTRL)** | `Yorko/mlcourse.ai` тема 8 | Классический ответ на «категорий миллионы, памяти нет» и на «модель должна обновляться каждую минуту». У нас есть «категории высокой мощности», но не хэширование и не онлайн-обучение как метод | `docs/02-classic-ml/14-feature-engineering.md` + `docs/09-monitoring/07-retraining.md` |
| **Boruta и ACE как методы отбора признаков; ловушки impurity-based важности** | Dyakonov/PZAD лекция 18 | У нас «отбор признаков» есть строкой; Boruta — конкретный метод, который называют на собесе | `docs/02-classic-ml/14-feature-engineering.md` / `docs/02-classic-ml/15-interpretability.md` |
| **Prunning (прореживание) нейросетей как отдельная техника наряду с дистилляцией** | `isadrtdinov/intro-to-dl-hse` семинар 6 | У нас прунинг упомянут одним словом в `07-mlops/09`; структурный vs неструктурный прунинг и lottery ticket — конкретика, которую спрашивают | `docs/07-mlops/09-inference-optimization.md` (расширить) |
| **Polars как альтернатива pandas для больших таблиц** | `sb-ai-lab/RecSys-Course` модуль 15 | Быстро вытесняет pandas в препроцессинге; вопрос «чем заменить pandas, когда не влезает» — практический | `docs/12-coding/02-numpy-pandas.md` |
| **Sequence parallelism и offloading как отдельные виды параллелизма** | efficient-dl-systems W4 | У нас перечислены тензорный и пайплайн-параллелизм и FSDP/ZeRO; sequence parallelism (длинный контекст) и offloading в CPU/NVMe отсутствуют | `docs/03-deep-learning/06-scaling-and-efficiency.md` |

**Низкий приоритет (нашёл, но для middle+ MLE-собеса вряд ли окупится):**
Neural ODE / FFJORD / continuous-in-time NF, SDE и уравнение Фоккера–Планка, дискретная диффузия для
последовательностей (DGM L9–L14); NeRF и синтез новых видов, оптический поток, monodepth,
разреженные 3D-свёртки (deep_vision_and_graphics W11–W12); POMDP и inverse RL (Practical_RL W8, W10);
теория нечётких множеств (PZAD); ядровые методы вглубь — RKHS, Nyström, random features
(esokolov ML2 lecture13–14: у нас ядра уже есть в главе про SVM, не хватает только этой глубины).

---

## Чего найти не удалось

**Заблокировано (403 / 404 / DNS) — программы получить не удалось:**
- `https://education.yandex.ru/handbook/ml` — **[НЕ ДОСТУПЕН]**, 403. Учебник ШАД по ML — самый
  прямой аналог нашего хендбука; оглавление не получено.
- `https://yandexdataschool.gitlab.io/ml-handbook/` (зеркало того же учебника) — **[НЕ ДОСТУПЕН]**, 403.
- `https://gitlab.com/yandexdataschool/ml-handbook/-/tree/master/chapters` — страница открылась,
  но листинг директорий не отрендерился (GitLab грузит дерево скриптом).
- `https://ml-handbook.ru/` — **[НЕ ДОСТУПЕН]**, домен не резолвится.
- `http://www.machinelearning.ru/...` — **[НЕ ДОСТУПЕН]**, 403. Не получены полные программы курсов
  К. В. Воронцова: «Машинное обучение», «Вероятностные тематические модели», «Математические методы
  анализа текстов», а также курса Ветрова/Кропотова «Байесовские методы машинного обучения».
  Темы тематического моделирования занесены в дельту по описаниям поисковой выдачи, помечены
  как [ТОЛЬКО ОПИСАНИЕ].
- `http://wiki.cs.hse.ru/...` — **[НЕ ДОСТУПЕН]**, 403. Официальные вики-страницы курсов ФКН ВШЭ
  («Машинное обучение 1/2», «Глубинное обучение 1 25/26», «Глубинное обучение в анализе графовых
  данных», «Моделирование временных рядов») — программы восстанавливались по GitHub-репозиториям.
- `https://www.hse.ru/edu/courses/...` — **[НЕ ДОСТУПЕН]**, 403 (карточки курсов ВШЭ, в т.ч.
  «Байесовские методы в машинном обучении», «Эффективные системы глубинного обучения»).
- `https://bayesgroup.github.io/bmml/` — **[НЕ ДОСТУПЕН]**, 403.
- `https://www.dlschool.org/` — **[НЕ ДОСТУПЕН]**, 403. Программа **второй части** Deep Learning School
  (NLP-поток) и продвинутого потока не получена; открыта только первая часть (CV) по GitHub-репозиторию.
- `https://yandexdataschool.github.io/cuda_course/` — **[НЕ ДОСТУПЕН]**, 403. Полная программа
  CUDA-курса ШАД не получена, только структура репозитория.
- `https://ml-system-design.ru/` и `https://mlsystemdesign-6490.github.io/` — **[НЕ ДОСТУПЕН]**, 403.
- `https://habr.com/...` — **[НЕ ДОСТУПЕН]**, 403 (статья о создании учебника ШАД).

**Открылось частично — программы внутри нет:**
- `yandexdataschool/Practical_DL` README обрывается на неделе 3 пометкой «(to be updated)» и в ветке
  `fall25`, и в `fall23`. Полная программа восстановлена по именам папок недель — тем лекций
  дословно нет.
- `anokhin/recsys-course-spring-2024`: README отсылает к папке `slides`, листинг папки отдаёт 404,
  программа лежит PDF-ами. Курс зафиксирован как [ТОЛЬКО ОПИСАНИЕ].
- `Pyatachokk/hse_ts_course` (ВШЭ, «Моделирование временных рядов»): дерево семестров открылось
  (`2020-fall` … `2026-spring`), но имена файлов лекций внутри `2026-spring/lectures` не раскрылись
  (видны только `lecture_01_intro` и `ts_notes`). **Дельты по временным рядам не зафиксировано** —
  ни один открытый источник не дал тем сверх нашей главы `02-classic-ml/16-time-series.md`.
- `bayesgroup/deepbayes-2019`: видны только `lectures/day1..day6` и `seminars/day1..day6`,
  названия материалов не раскрылись.
- `elvarid/gnn_course_hse` (ВШЭ, глубинное обучение на графах): README помечен WIP, программы нет;
  указано только, что курс основан на стэнфордском CS224W.
- `yandexdataschool/ML-Handbook-materials`: в `chapters/` подтверждены лишь три папки —
  `ensembles`, `nlp`, `representation_learning`; полный список глав не раскрылся.
- `yandexdataschool/asml`, `yandexdataschool/cuda_course`, `yandexdataschool/reproducible_analysis_course`:
  структура есть, описания и программы отсутствуют.

**Искал, но содержательных открытых программ не нашёл:**
- **ИТМО** — по запросам находятся только студенческие репозитории с лабораторными
  (`anton-bannykh/ml-2012`, `testpassword/Machine-learning-and-data-analysis`) и курс на OpenEdu
  без открытой программы. Официальной программы кафедры получить не удалось.
- **Сколтех** — отдельной открытой актуальной программы нет. Сколтех фигурирует как соразработчик
  `Practical_DL` и `deep_vision_and_graphics` (обе программы выписаны выше); найденные репозитории
  `dzisandy/Deep-Learning`, `vadim-v-lebedev/dl-course`, `KovalevEvgeny/Skoltech-DL` —
  либо студенческие, либо README отдаёт 404.
- **MADE (VK)** — программа заявлена как «более 25 дисциплин», но публичного списка дисциплин
  в открытом доступе нет; только маркетинговые описания.
- **ШАД, официальный учебный план** — `shad.yandex.ru` в выдаче есть, но постраничный список
  обязательных и выборных курсов по семестрам получить не удалось. Программа ШАД реконструирована
  по открытым репозиториям организации `yandexdataschool` (см. выше).
- **Отдельного русскоязычного университетского курса по MLOps** не нашёл: ближайшее —
  `yandexdataschool/reproducible_analysis_course` (без программы) и
  `mryab/efficient-dl-systems` W7 (деплой веб-сервиса). Дельты по разделу `07-mlops` из российских
  университетских курсов **не зафиксировано** — наш раздел шире всего найденного.
- **Дельты по разделу `10-ab-testing`** ни один из открытых российских университетских курсов
  не дал: A/B-тестирование в них практически отсутствует (ближайшее — «Дополнительные методы
  оценки качества рекомендаций» в ODS Your Second RecSys и W8 recsys_course про логирование
  и смещения). Наш раздел по A/B заметно подробнее всех найденных программ.
- **Дельты по разделу `12-coding`** также нет: `yandexdataschool/python_public` и
  `yandexdataschool/algorithms` существуют, но программ в открытом виде не содержат.
