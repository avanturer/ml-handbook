# intl-courses — прочёс программ

Прочёс зарубежных университетских курсов ради **сравнения программ** с нашим манифестом
`.handbook/STRUCTURE.md` (117 глав). Дата: 2026-07-27.

**Важное техническое ограничение.** Из этой среды доступны только `github.com`,
`raw.githubusercontent.com` и поисковая выдача. Все канонические домены курсов отдают **403**:
`cs336.stanford.edu`, `stanford-cs336.github.io`, `stanford-cs329s.github.io`,
`cs231n.stanford.edu`, `cs231n.github.io`, `web.stanford.edu/class/cs224n`,
`rail.eecs.berkeley.edu`, `hanlab.mit.edu`, `efficientml.ai`, `fullstackdeeplearning.com`,
`madewithml.com`, `huyenchip.com`, `dlsyscourse.org`, `dcai.csail.mit.edu`, `mmds.org`,
`classcentral.com`, `youtube.com`. `web.archive.org` заблокирован на уровне инструмента,
`curl` через прокси возвращает `CONNECT tunnel failed 403`.
Обход: **исходные репозитории сайтов курсов на GitHub** (Jekyll-исходники, `_data/*.yml`,
собранный `_site/`), репозитории заданий, репозитории конспектов, awesome-списки.
Это сработало для большинства ключевых курсов, включая полные расписания CS336, CS329S,
CS294 AI-Sys, CMU 11-667 и CMU 11-777.

---

## Что реально открыл (со ссылками)

### [ОТКРЫЛ] — полный текст программы получен

| Курс | Ссылка, которую реально открыл | Что получил |
|---|---|---|
| **Stanford CS336** Language Modeling from Scratch, Spring 2025 | `https://raw.githubusercontent.com/stanford-cs336/stanford-cs336.github.io/main/spring2025/index.html` | Полное расписание 19 лекций + 5 заданий с дедлайнами |
| CS336 — материалы лекций | `https://github.com/stanford-cs336/spring2025-lectures/tree/main/nonexecutable` | Имена PDF: подтверждают названия лекций 3,4,5,7,9,11,15,16 |
| CS336 — лекция 10 (Inference) | `https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_10.py` | Полный план темы «инференс» |
| CS336 — лекция 2 (Resource accounting) | `https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_02.py` | Полный план темы «учёт ресурсов» |
| CS336 — задания 2/3/4/5 | `https://github.com/stanford-cs336/assignment2-systems`, `.../assignment3-scaling`, `.../assignment4-data`, `.../assignment5-alignment` | Состав практики |
| CS336 — список репозиториев | `https://github.com/orgs/stanford-cs336/repositories` | 22 репо, структура курса |
| **Stanford CS329S** ML Systems Design | `https://raw.githubusercontent.com/stanford-cs329s/stanford-cs329s.github.io/main/syllabus.html` | Полный силлабус, 18 лекций |
| **Berkeley CS294 AI-Sys** (Systems for AI), Sp22 | `https://raw.githubusercontent.com/ucbrise/cs294-ai-sys-sp22/main/index.md` | Полное расписание 12 лекций |
| **CMU 11-667** Large Language Models, Fall 2025 | `https://raw.githubusercontent.com/cmu-llms-class/cmu-llm-class-website-2025/main/_site/schedule/index.html` | Полное расписание 23 лекций |
| CMU 11-667 — силлабус | `https://raw.githubusercontent.com/cmu-llms-class/cmu-llm-class-website-2025/main/syllabus.md` | Описание курса (без расписания) |
| **CMU 11-777** Multimodal ML, Fall 2023 | `https://raw.githubusercontent.com/cmu-multicomp-lab/mmml-course/master/_data/lectures_2023.yml` | Полный список лекций с подтемами |
| **Stanford CS324** LLM, Winter 2022 | `https://github.com/stanford-cs324/winter2022/tree/master/lectures` | Полный список тем-файлов лекций |
| Stanford CS324, Winter 2023 | `https://raw.githubusercontent.com/stanford-cs324/winter2023/main/syllabus.md` | Тематические блоки курса |
| **MIT 6.5940 / 6.S965** EfficientML.ai | `https://raw.githubusercontent.com/erectbranch/TinyML_and_Efficient_DLC/master/README.md` (и `https://github.com/erectbranch/MIT-Efficient-AI`) | Полный разбор лекций 2–19 по блокам |
| **CMU 10-414/714** Deep Learning Systems | `https://github.com/navalnica/dl_sys_course_notes` | Полный список 24 лекций |
| **Stanford CS231n** — конспекты (модули) | `https://raw.githubusercontent.com/cs231n/cs231n.github.io/master/index.html` | Модули 0–2 + подтемы + список заданий 2026 |
| **MIT Data-Centric AI** (IAP 2023/2024) | `https://github.com/dcai-course/dcai-lab` | 9 лабораторных = 9 тем лекций |
| **MLOps Zoomcamp** (DataTalksClub) | `https://github.com/DataTalksClub/mlops-zoomcamp` | 7 модулей с подтемами |
| **LLM Zoomcamp** (DataTalksClub) | `https://github.com/DataTalksClub/llm-zoomcamp` | 7 модулей + воркшоп + капстоун |
| **Full Stack Deep Learning 2022** — лабы | `https://github.com/full-stack-deep-learning/fsdl-text-recognizer-2022-labs` | Список 9 лабораторных |
| **fast.ai course22** | `https://github.com/fastai/course22` | Список ноутбуков-уроков |
| **Made With ML** — навигация кода | `https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/mkdocs.yml` | nav: data/models/train/tune/evaluate/predict/serve/utils |
| **CS224W** — конспекты TA | `https://raw.githubusercontent.com/snap-stanford/cs224w-notes/master/index.md` | Полное оглавление конспектов |
| **Awesome System for ML** (таксономия ML-систем) | `https://raw.githubusercontent.com/HuaizhengZhang/Awesome-System-for-Machine-Learning/master/README.md` | Полное оглавление категорий |
| Stanford CS224n — исторический силлабус (2015) | `https://raw.githubusercontent.com/stanfordnlp/cs224n-web/master/syllabus.shtml` | 20 лекций, **устарело**, для дельты бесполезно |
| CS231n 2025 — конспекты (неофиц.) | `https://github.com/raimbekovm/cs231n-2025-notes` | Только лекции 1–4 (репозиторий в работе) |

### [ТОЛЬКО ОПИСАНИЕ] — сайт недоступен, программа собрана из поисковой выдачи

| Курс | Что удалось узнать | Ограничение |
|---|---|---|
| **Stanford CS229** ML | Понедельный план (Summer 2024): недели 1–8 | Официальный PDF-силлабус не открылся |
| **Stanford CS224n** NLP (W2025/W2026) | Тематический состав курса, отдельные названия лекций (1, 2, 9, 10, 11) | Полное расписание по номерам недоступно |
| **Stanford CS231n** 2025 | Названия лекций 5, 6, 9, 10, 12–18 | Полное расписание 1–18 не собрано |
| **Stanford CS246** MMDS | Полный тематический список курса | Пословное расписание по датам не собрано |
| **MIT 6.5940** Fall 2024 | Лекции 18, 20, 21, 22, 23 (дополнение к [ОТКРЫЛ]) | С сайта hanlab не открылось |
| **Berkeley CS285** Deep RL | Лекции 1–16 + упоминание Inverse RL | Полное расписание с сайта не открылось |
| **Berkeley CS182/282A** | Тематический состав (Sp21) | Расписание конкретного семестра не собрано |
| **CMU 10-701** Intro to ML (PhD) | Тематический состав | Пословное расписание не собрано |
| **UW CSE 599W** Systems for ML | Тематический состав + лекции 3, 4, 9, 10, 11, 12 | Полный список 1–20 не собран |
| **Full Stack Deep Learning 2022** — лекции | Лекции 1–9 (названия) | Сайт 403 |
| **FSDL LLM Bootcamp Spring 2023** | 8 лекций (названия) | Сайт 403 |
| **Made With ML** — уроки | Перечень названий уроков (без строгой группировки) | madewithml.com 403 |
| **MIT Data-Centric AI 2024** | Даты и названия 7 лекций | dcai.csail.mit.edu 403 |
| **fast.ai part 2** (Stable Diffusion) | Состав уроков 9, 9A, 9B, 10 | course.fast.ai 403 |
| **Oxford Advanced ML / Stats ML** | Тематический состав | Полного расписания нет |
| **Stanford CS224W** | Полный список лекций по названиям | Официальное расписание не открылось |

### [НЕ ДОСТУПЕН] — не получил ни программы, ни содержательного описания

- **Cambridge MLMI** (MPhil in Machine Learning and Machine Intelligence) — нашёл только страницу
  «Course Structure» без списка модулей и лекций.
- **NYU Deep Learning (LeCun/Canziani, DLSP20/DLSP21)** — README репозиториев содержат только
  инструкции по установке; сайт `atcold.github.io` не открылся. Понедельного плана нет.
- **MIT 6.036** Introduction to Machine Learning — программу получить не удалось.
- **CMU 11-777 Fall 2023 rendered schedule** — Jekyll-шаблон открылся, но данные лекций 2023
  взял из `_data/lectures_2023.yml` (это и есть источник, помечен [ОТКРЫЛ]).

---

## Программы (по каждому источнику — полный список тем)

### 1. Stanford CS336 — Language Modeling from Scratch (Spring 2025) [ОТКРЫЛ]
`https://raw.githubusercontent.com/stanford-cs336/stanford-cs336.github.io/main/spring2025/index.html`

Лекции:
1. Overview, tokenization (Percy Liang)
2. PyTorch, resource accounting (Percy)
3. Architectures, hyperparameters (Tatsu Hashimoto)
4. Mixture of experts (Tatsu)
5. GPUs (Tatsu)
6. Kernels, Triton (Tatsu)
7. Parallelism (Tatsu)
8. Parallelism (Percy)
9. Scaling laws (Tatsu)
10. Inference (Percy)
11. Scaling laws / Scaling details (Tatsu)
12. Evaluation (Percy)
13. Data (Percy)
14. Data (Percy)
15. Alignment — SFT/RLHF (Tatsu)
16. Alignment — RL / RLVR (Tatsu)
17. Alignment — RL (Percy)
18. Guest lecture — Junyang Lin
19. Guest lecture — Mike Lewis

Задания: 1 Basics · 2 Systems · 3 Scaling · 4 Data · 5 Alignment and Reasoning RL.

Детализация лекции 2 (Resource accounting) — из `lecture_02.py`:
учёт памяти (float32/float16/bfloat16/fp8, динамический диапазон vs точность), tensor storage /
slicing / views, elementwise-операции, FLOPs матричного умножения, einops, **расчёт FLOPs и MFU
(Model FLOPs Utilization)**, FLOPs обратного прохода, инициализация (Xavier), memory-mapped
загрузка данных, детерминизм, реализация оптимизаторов (SGD, AdaGrad), чекпоинтинг и
восстановление, mixed precision, **методология бюджетирования ресурсов и спеки железа (A100/H100)**.

Детализация лекции 10 (Inference) — из `lecture_10.py`:
сценарии инференса (чат, оценка, RL), метрики TTFT/latency/throughput, **arithmetic intensity и
ограничение пропускной способностью памяти**, KV-cache, prefill (compute-bound) vs decode
(memory-bound); «срезание углов» с потерями — уменьшение KV-кэша: **GQA, MLA (multi-head latent
attention), CLA (cross-layer attention), локальное внимание**; альтернативы трансформеру —
**SSM (S4, Mamba, Jamba, BASED)**, **диффузионные языковые модели** (параллельная генерация);
квантизация (fp32→int4, **LLM.int8() с обработкой выбросов**, activation-aware); прунинг и
дистилляция; «срезание углов» без потерь — **speculative decoding, гарантия точного сэмплирования,
Medusa, EAGLE**; динамическая нагрузка — **continuous batching, PagedAttention, prefix sharing и
copy-on-write**.

Ценность: единственный курс, где ML-система LLM собирается целиком снизу вверх — от FLOPs до RL.
Грейд: **middle+ / senior**, обязателен для LLM-инженера.

---

### 2. Stanford CS329S — Machine Learning Systems Design (Chip Huyen) [ОТКРЫЛ]
`https://raw.githubusercontent.com/stanford-cs329s/stanford-cs329s.github.io/main/syllabus.html`

1. Understanding Machine Learning Production (кейс: 150 ML-моделей в Booking.com)
2. ML and Data Systems Fundamentals (кейс Airbnb home value; разбор «Twitter Trending Hashtags»)
3. Training Data
4. Feature Engineering
5. Model Selection, Development, and Training
6. Offline Evaluation
7. Model Evaluation (туториал; **RecList** — поведенческое тестирование рекомендаций)
8. Deployment
9. Deployment Tutorials (оценка MLOps-инструментов; Ray Serve)
10. Diagnosis of ML System Failures, Data Distribution Shifts & Monitoring
11. Monitoring & Continual Learning (**дрейф на потоковых данных**)
12. Case Study + Tutorial (деплой в Stitch Fix; трекинг экспериментов в W&B)
13. Monitoring Tutorials (WhyLogs, Evidently)
14. Guest: Time Series Forecasting + GNN; **ML Beyond Accuracy: Fairness, Security, Governance**
15. **ML Infrastructure and Platform**
16. Final Project Discussion
17. **Integrating ML into Business** (питч, go-to-market, бизнес-ценность AI)
18. Demo Day

Ценность: эталон структуры ML System Design. Грейд: **middle → middle+**.

---

### 3. Berkeley CS294 AI-Sys — Systems for AI / AI for Systems (Spring 2022) [ОТКРЫЛ]
`https://raw.githubusercontent.com/ucbrise/cs294-ai-sys-sp22/main/index.md`

1. Introduction and Course Overview (история ML+систем)
2. Big Data Systems (Reynold Xin, Databricks): unified analytics, distributed datasets, lakehouse
3. **Hardware for Machine Learning** (Sophia Shao): точность вычислений, spatial-архитектуры,
   энергоэффективность, DNN-акселераторы
4. Distributed Deep Learning I: Systems (команда Microsoft DeepSpeed) — pipeline parallelism
5. Distributed Deep Learning II: Scaling Constraints (Michael Houston, Nvidia) — эффекты
   data parallelism, законы масштабирования
6. Project Proposals
7. **Machine Learning Applied to Systems** (Tim Kraska): learned indexes, device placement
8. **ML Frameworks and Automatic Differentiation** (Tianqi Chen): дизайн фреймворков, компиляция
9. **Efficient Machine Learning** (Vikas Chandra, Facebook): квантизация, прунинг, hardware-aware NAS
10. Cloud ML and Modern Data Stack (Matei Zaharia): облачная инфраструктура, оптимизация стоимости
11. **Benchmarking ML Workloads** (Vijay Reddi, Harvard): MLPerf, анализ производительности
12. **ML and Security**: federated learning, differential privacy, adversarial robustness

Ценность: именно тот курс, где живут темы, отсутствующие в обычных ML-курсах.
Грейд: **middle+ / senior**.

---

### 4. CMU 11-667 — Large Language Models: Methods and Applications (Fall 2025) [ОТКРЫЛ]
`https://raw.githubusercontent.com/cmu-llms-class/cmu-llm-class-website-2025/main/_site/schedule/index.html`

1. Building blocks of modern LLMs
2. Transformer architecture and pre-training learning objectives
3. Pre-training data curation and tokenization
4. Architecture Advancement on Transformers
5. Automatic evaluation of LLMs
6. In-context learning, task-oriented finetuning, parameter-efficient tuning
7–8. Guest lectures
9. Surprising Behaviours of In-Context Learning and Model Alignment
10. Embedding Learning and Tool Use
11. Guest lecture
12. Scaling Up LLMs — Scaling laws
13. Scaling up LLMs — Optimization and Parallel Training
14. **Interpretability methods**
15. Guest lecture
16. **Attacking LLM systems + benchmark leakage**
17. **Bias and ethical issues**
18. **Efficient Pretraining with Sparse Models**
19. Efficient Inference Methods
20. Chatbots and LLM Agents
21. Guest lecture
22. **Long-context models**
23. **Training with Synthetic Data**

Ценность: самая свежая академическая карта LLM-инженерии. Грейд: **middle+**.

---

### 5. Stanford CS324 — Large Language Models (Winter 2022 / 2023) [ОТКРЫЛ]
`https://github.com/stanford-cs324/winter2022/tree/master/lectures` (файлы лекций) и
`https://raw.githubusercontent.com/stanford-cs324/winter2023/main/syllabus.md`

Winter 2022, темы лекций (по именам файлов): introduction, capabilities, **harms-1**, **harms-2**,
data, **security**, **legality**, modeling, training, parallelism, scaling-laws,
**selective-architectures**, adaptation, **environment**.

Winter 2023, блоки:
- **Fundamentals**: что такое foundation models; как данные влияют на FM и последствия;
  как обучают FM и последствия; архитектуры и целевые функции; **emergent behaviors and
  capabilities**; адаптация к новым задачам и доменам; методы обучения и инфраструктура.
- **Survey**: текстовые и masked-LM FM; image-text и мультимодальные FM.
- **Societal**: **Security and Privacy**, **Environmental Impact**, **Legal Considerations**.

Ценность: единственный источник по юридическим/приватностным/энергетическим аспектам LLM.
Грейд: **middle+** (нужно для ответов «а можно ли обучаться на этих данных»).

---

### 6. MIT 6.5940 / 6.S965 — TinyML and Efficient Deep Learning Computing (EfficientML.ai) [ОТКРЫЛ + ТОЛЬКО ОПИСАНИЕ]
`https://raw.githubusercontent.com/erectbranch/TinyML_and_Efficient_DLC/master/README.md`

Блок «Основы»:
- Лекция 2: базовые термины, формы тензоров; **метрики эффективности** (latency, throughput,
  energy, #params, MACs, memory footprint)

Блок «Эффективный инференс»:
- Лекция 3: **гранулярность прунинга и критерии прунинга**
- Лекция 4: **автоматический прунинг, lottery ticket hypothesis, системная и аппаратная поддержка
  fine-grained sparsity, sparse matrix-matrix multiplication, поддержка разрежённости на GPU**
- Лекция 5: базовые понятия квантизации, **векторная квантизация**
- Лекция 6: **post-training quantization**; **quantization-aware training**, low-bit quantization
- Лекция 7: **Neural Architecture Search** — базовые понятия, ручные архитектуры, пространство поиска
- Лекция 8: **NAS: оценка производительности и hardware-aware NAS**
- Лекция 10: **knowledge distillation** и дистилляция под приложения
- Лекция 11: **MCUNet** (инференс на микроконтроллерах)

Блок «Эффективное обучение и системная поддержка»:
- Лекция 15: **on-device training, transfer learning**
- Лекция 16: **Tiny Training Engine, компиляторы, graph-level оптимизация**
- Лекция 17: **оптимизация циклов на микроконтроллере, оптимизация инференса**

Блок «Доменные оптимизации»:
- Лекция 12: Transformer, варианты дизайна трансформера
- Лекция 13: **квантизация LLM, эффективная системная поддержка, прунинг и разрежённость LLM,
  системы сервинга LLM**
- Лекция 14: LLM post-training, prompt engineering
- Лекция 15 (2024): **длинный контекст, эффективное внимание, за пределами трансформеров**
- Лекция 18: эффективное распознавание облаков точек
- Лекция 19: эффективное понимание видео, GAN

Дополнение по Fall 2024 [ТОЛЬКО ОПИСАНИЕ]: Лекция 16 Vision Transformer; Лекция 18 **Diffusion
Model**; Лекция 19 **Distributed Training (Part I)**; Лекция 20 **Distributed Training (Part II)**;
Лекция 21 **On-Device Training and Transfer Learning**; Лекция 22 Course Summary + Quantum ML I;
Лекция 23 Quantum ML II. Также в описании курса: **gradient compression**, data/model parallelism.

Ценность: **главный источник дельты по эффективности и инференсу**. Грейд: **middle+ / senior**.

---

### 7. CMU 10-414/714 — Deep Learning Systems: Algorithms and Implementation (Chen, Kolter) [ОТКРЫЛ]
`https://github.com/navalnica/dl_sys_course_notes`

1. Introduction and Logistics
2. ML Refresher / Softmax Regression
3. «Manual» Neural Networks (I, II)
4. **Automatic Differentiation**
5. **Automatic Differentiation Implementation**
6. Fully Connected Networks, Optimization, Initialization
7. **Neural Network Abstractions**
8. **Neural Network Library Implementation**
9. Normalization and Regularization
10. Convolutional Networks
11. **Hardware Acceleration**
12. **GPU Acceleration**
13. **Hardware Acceleration Implementation**
14. **Implementing Convolutions** (im2col и т.п.)
15. **Training Large Models**
16–17. Generative Adversarial Networks (+ implementation)
18–19. Sequence Modeling and Recurrent Networks (+ implementation)
20–21. Transformers and Attention (+ implementation)
23. **Model Deployment**
24. **Machine Learning Compilation and Deployment Implementation**

Проект курса: собрать фреймворк «Needle» с нуля (autodiff, GPU-операции, слои, лоссы, даталоадеры).

Ценность: понимание «что внутри PyTorch». Грейд: **middle+**.

---

### 8. UW CSE 599W — Systems for ML (Tianqi Chen) [ТОЛЬКО ОПИСАНИЕ]
Темы курса: основы DL; модели программирования для выражения ML-моделей; автоматическое
дифференцирование; **оптимизация памяти**; **планирование (scheduling)**; распределённое обучение;
**аппаратное ускорение**; **предметно-ориентированные языки (TVM)**; **сервинг моделей**.
Подтверждённые номера: Лекция 3 Components Overview of DL System; Лекция 4 Backprop and Autodiff;
**Лекция 9 Memory Optimization**; **Лекция 10 Parallel Scheduling**; **Лекция 11 Distributed
Training and Communication Protocols**; **Лекция 12 Model Serving**.
Грейд: **middle+ / senior**.

---

### 9. Stanford CS231n — Deep Learning for Computer Vision [ОТКРЫЛ (конспекты) + ТОЛЬКО ОПИСАНИЕ (2025)]
`https://raw.githubusercontent.com/cs231n/cs231n.github.io/master/index.html`

Модуль 0: Preparation — software setup, Python/NumPy tutorial.
Модуль 1: Neural Networks —
- Image Classification: data-driven подход, kNN, train/val/test, L1/L2, подбор гиперпараметров, CV
- Linear classification: SVM, Softmax, bias trick, hinge loss, cross-entropy, L2-регуляризация
- Optimization: SGD, ландшафты оптимизации, локальный поиск, learning rate, аналитический и
  численный градиент
- Backpropagation: chain rule, real-valued circuits, паттерны потока градиента
- Neural Networks 1: модель нейрона, активации, архитектура, выразительная способность
- Neural Networks 2: препроцессинг, инициализация весов, batch normalization, регуляризация, лоссы
- Neural Networks 3: **gradient checks, sanity checks, babysitting learning**, momentum,
  методы второго порядка, Adagrad/RMSprop, подбор гиперпараметров, ансамбли моделей
- Putting it together: минимальный кейс-стади

Модуль 2: Convolutional Neural Networks —
- CNN: слои, пространственная организация, паттерны слоёв и размеров, AlexNet/ZFNet/VGGNet,
  вычислительные ограничения
- **Understanding and Visualizing CNNs**: t-SNE-эмбеддинги, деконволюции, градиенты по данным,
  **fooling ConvNets** (обман сети), сравнение с человеком
- Transfer Learning and Fine-tuning

Задания 2026: A1 — классификация, kNN, Softmax, FC-сети; A2 — BatchNorm, Dropout, ConvNets,
Network Visualization, Image Captioning с RNN; A3 — **Image Captioning с трансформерами,
Self-Supervised Learning, Diffusion Models, CLIP и DINO**.

Расписание 2025 [ТОЛЬКО ОПИСАНИЕ]: Л3 Regularization and Optimization; Л5, Л6 Training CNNs и
CNN Architectures; **Л9 Detection, Segmentation, Visualization and Understanding**;
**Л10 Video Understanding**; **Л12 Self-Supervised Learning**; **Л13 VAE, GAN**;
**Л14 Diffusion Models**; **Л15 3D Vision, NeRF**; **Л16 Vision & Language (CLIP, VQA)**;
**Л17 Robot Learning**; **Л18 Human-Centered AI**.
Группировка курса 2025: «Generative and Interactive Visual Intelligence» (Л13–16),
«Human-Centered Applications and Implications» (Л17–18).

Грейд: **junior → middle** для базы, **middle+** для генеративного блока.

---

### 10. Stanford CS224n — NLP with Deep Learning [ТОЛЬКО ОПИСАНИЕ]
Состав курса (W2025 / W2026): word vectors, feed-forward networks, recurrent networks, attention,
encoder-decoder, transformers, **pretraining, post-training (RLHF), efficient adaptation,
benchmarking, reasoning, agents, multilinguality, multimodality, interpretability**, немного
лингвистики и философии. Подтверждённые лекции: Л1 Introduction and Word Vectors; Л2 Word Vectors 2;
Л9 Pretraining; Л10 Post-training; Л11 Benchmarking.
Исторический силлабус 2015 [ОТКРЫЛ] — 20 лекций про SMT, выравнивание слов, парсинг,
кореференцию, MaxEnt-классификаторы, tree-RNN — **полностью устарел**, для дельты не использую.

---

### 11. Stanford CS229 — Machine Learning [ТОЛЬКО ОПИСАНИЕ]
Понедельный план (Summer 2024):
- Неделя 1: линейная регрессия, МНК, градиентный спуск, метрики ошибок, переобучение,
  bias-variance
- Неделя 2: регуляризация, Ridge, LASSO, валидационные выборки, кросс-валидация
- Неделя 3: линейные классификаторы, логистическая регрессия, обучение на взвешенных данных,
  SGD, **GLM**, **GDA**, наивный Байес
- Неделя 4: нейросети I и II; CA-лекция по последовательным моделям (RNN, LSTM)
- Неделя 5: обучение без учителя, k-means, GMM + EM
- Неделя 6: решающие деревья, бустинг, AdaBoost, PCA, SVD
- Недели 7–8: **обучение с подкреплением (лекции 13–14), TD-learning**, обзор,
  **ML Advice** и **Fairness**
Общий состав: supervised (генеративное/дискриминативное, параметрическое/непараметрическое,
нейросети, SVM); unsupervised (кластеризация, снижение размерности, ядровые методы);
**теория обучения (bias/variance, VC-теория, large margins)**; **RL и адаптивное управление**.

---

### 12. Stanford CS246 — Mining Massive Data Sets [ТОЛЬКО ОПИСАНИЕ]
Темы: системы больших данных (Hadoop, **MapReduce**, Spark); **Link Analysis (PageRank, детекция
спама)**; **поиск похожих объектов (locality-sensitive hashing, shingling, min-hashing)**;
**обработка потоков данных**; рекомендательные системы; **анализ графов социальных сетей /
community detection**; **ассоциативные правила (frequent itemsets)**; снижение размерности
(**UV, SVD, CUR**); алгоритмы крупномасштабного майнинга (кластеризация, поиск ближайших соседей);
крупномасштабное ML (ансамбли деревьев); **многорукие бандиты**; **вычислительная реклама**.
Учебник: «Mining of Massive Datasets» (Leskovec, Rajaraman, Ullman).

---

### 13. Stanford CS224W — Machine Learning with Graphs [ТОЛЬКО ОПИСАНИЕ + ОТКРЫЛ конспекты]
Лекции: Introduction to ML for Graphs; Traditional Methods for ML on Graphs; **Node Embeddings**;
**Link Analysis: PageRank**; **Label Propagation for Node Classification**; Graph Neural Networks
(GNN Model, Design Space); Applications and Theory of GNNs; **Knowledge Graph Embeddings**;
**Reasoning over Knowledge Graphs**; **Frequent Subgraph Mining with GNNs**; **Community Structure
in Networks**; Traditional and Deep Generative Models for Graphs; Advanced Topics on GNNs.

Оглавление конспектов TA [ОТКРЫЛ] `snap-stanford/cs224w-notes`:
- Preliminaries: Introduction and Graph Structure; **Measuring Networks and Random Graphs**;
  **Motifs and Graphlets**
- Network Methods: **Structural Roles in Networks**; **Spectral Clustering**; **Influence
  Maximization**; **Outbreak Detection**; **Link Analysis**; **Network Effects and Cascading
  Behavior**; **Network Robustness**; **Network Evolution**; **Knowledge Graphs and Metapaths**
- ML with Networks: **Message Passing and Node Classification**; Node Representation Learning;
  Graph Neural Networks; **Generative Models for Graphs**

---

### 14. CMU 11-777 — Multimodal Machine Learning (Fall 2023) [ОТКРЫЛ]
`https://raw.githubusercontent.com/cmu-multicomp-lab/mmml-course/master/_data/lectures_2023.yml`

- 1.1 Course introduction: **шесть ключевых вызовов мультимодальности**, силлабус
- 1.2 Multimodal applications: задачи, датасеты, проекты
- 2.1 Unimodal representations: **измерения гетерогенности**, визуальные представления
- 2.2 Unimodal representations: языковые, сигнальные, графовые и прочие представления
- 3.1 Multimodal representations: **кросс-модальные взаимодействия, multimodal fusion**
- 3.2 Multimodal representations: **coordinated representations, multimodal fission**
- 4.1 **Alignment and grounding**: явное выравнивание, мультимодальное обучение, grounding
- 4.2 Aligned representations: self-attention трансформеры, маскирование и SSL
- 5.1 Multimodal transformers: языковой претрейн, мультимодальный трансформер, архитектура
- 5.2 **Structured Representation and Reasoning**: структурные и иерархические модели, модели памяти
- 6.1 Multimodal transformers: vision transformer, video transformer, vision-language transformer
- 6.2 Guest talk
- 7.1 **Multimodal Interaction**: язык и RL, интерактивное обучение, Q-learning, policy-based методы
- 7.2 **Multimodal Inference and Knowledge**: дискретные концепты, **каузальный вывод**,
  внешние знания, reasoning
- 9.1 **Multimodal Generation**: перевод, суммаризация, создание; генеративные модели; авторегрессия
- 9.2 New Generation Models: **смеси гауссиан, VAE, диффузионные модели**, открытые проблемы генерации
- 11.2 **Transference**: multimodal co-learning, co-training и self-training
- 12.1 New research directions: недоисследованные модальности
- 12.2 **Quantification**: математический аппарат для взаимодействий модальностей,
  количественная оценка мультимодального взаимодействия, оптимизационные проблемы

Грейд: **middle+** для мультимодального трека.

---

### 15. Berkeley CS285 — Deep Reinforcement Learning [ТОЛЬКО ОПИСАНИЕ]
1. Introduction and Course Overview
2. **Supervised Learning of Behaviors (imitation learning)**
3. PyTorch Tutorial
4. **Introduction to Reinforcement Learning (MDP)**
5. **Policy Gradients**
6. **Actor-Critic Algorithms**
7. **Value Function Methods**
8. **Deep RL with Q-Functions**
9. **Advanced Policy Gradients (TRPO/PPO)**
10. **Optimal Control and Planning**
11. **Model-Based RL**
12. Model-Based Policy Learning
13–14. **Exploration (I, II)**
15–16. **Offline RL (I, II)**
далее — **Inverse RL** и др.

### 16. Berkeley CS182/282A — Deep Neural Networks [ТОЛЬКО ОПИСАНИЕ]
Темы: Getting Neural Nets to Train; Computer Vision; Generating Images from CNNs; RNN;
Sequence-to-Sequence; **Transformers**; Applications in NLP; **Learning-Based Control &
Imitation**; **Autoencoders & Latent Variable Models**; **Variational Autoencoders & Invertible
Models**; **GANs & Adversarial Attacks**; **Meta Learning**.

### 17. CMU 10-701 — Introduction to Machine Learning (PhD) [ТОЛЬКО ОПИСАНИЕ]
MLE и MAP; наивный Байес; линейная и логистическая регрессия; SVM (прямая и двойственная задача,
двойственность, **условия KKT**); ядровые методы и kernel trick; ансамбли (AdaBoost, random forest).
Требования на входе: вероятность, линейная алгебра, статистика, алгоритмы.
Дельты по отношению к нашему манифесту не даёт — всё покрыто разделом 02.

---

### 18. Full Stack Deep Learning 2022 [ТОЛЬКО ОПИСАНИЕ] + лабы [ОТКРЫЛ]
Лекции:
1. When to Use ML and Course Vision
2. Development Infrastructure & Tooling
3. Troubleshooting & Testing
4. Data Management
5. Deployment
6. **Continual Learning**
7. **Foundation Models**
8. **ML Teams and Project Management**
9. **Ethics**

Лабораторные (`github.com/full-stack-deep-learning/fsdl-text-recognizer-2022-labs`):
Overview (архитектура Text Recognizer); 01 Deep Neural Networks in PyTorch; 02a PyTorch Lightning;
02b Training CNNs on Synthetic Handwriting; 03 Transformers and Paragraph Recognition;
04 Experiment Tracking; 05 Troubleshooting & Testing; **06 Data Annotation Workflows**;
07 Model Deployment; 08 Production Monitoring.
Стек: PyTorch, Lightning, W&B, Docker, AWS Lambda, Gradio, Gantry.

### 19. FSDL LLM Bootcamp Spring 2023 [ТОЛЬКО ОПИСАНИЕ]
8 лекций: LLM Foundations; **Prompt Engineering**; **LLMOps**; **UX for Language User Interfaces**;
**Augmented Language Models**; Launch an LLM App in One Hour; Project Walkthrough; What's Next.

---

### 20. MLOps Zoomcamp (DataTalksClub) [ОТКРЫЛ]
`https://github.com/DataTalksClub/mlops-zoomcamp`

- Модуль 1 Introduction: что такое MLOps, **MLOps maturity model**, NY Taxi dataset, зачем MLOps,
  структура курса и окружение
- Модуль 2 Experiment Tracking & Model Management: трекинг, MLflow, сохранение/загрузка моделей,
  **model registry**
- Модуль 3 Orchestration & ML Pipelines: оркестрация workflow
- Модуль 4 Model Deployment: online (web, streaming) vs offline (batch); Flask; **streaming через
  AWS Kinesis + Lambda**; batch scoring
- Модуль 5 Model Monitoring: мониторинг веб-сервиса через **Prometheus + Evidently + Grafana**;
  мониторинг батч-джобов через **Prefect + MongoDB + Evidently**
- Модуль 6 Best Practices: юнит- и интеграционные тесты, линтеры/форматтеры/**pre-commit hooks**,
  **CI/CD в GitHub Actions**, **Infrastructure as Code (Terraform)**
- Модуль 7 Final Project

### 21. LLM Zoomcamp (DataTalksClub) [ОТКРЫЛ]
`https://github.com/DataTalksClub/llm-zoomcamp`

- Модуль 1 **Agentic RAG**: RAG на keyword-поиске, «агентизация» через function calling
- Модуль 2 Vector Search: семантический поиск, minsearch, sqlitesearch, **PGVector**
- Модуль 3 Orchestration: AI-оркестрация (Kestra)
- Воркшоп Data Ingestion: **dlt-пайплайны для загрузки и анализа LLM-трейсов**, DuckDB, marimo
- Модуль 4 Evaluation: качество ретривала и ответа, **offline и online оценка**
- Модуль 5 Monitoring: **мониторинг пользовательского фидбека** и здоровья системы, live-дашборды
- Модуль 6 Best Practices: LangChain, гибридный поиск, реранкинг
- Модуль 7 End-to-End Project + Capstone

### 22. Made With ML (Goku Mohandas / Anyscale) [ОТКРЫЛ (nav) + ТОЛЬКО ОПИСАНИЕ (уроки)]
Навигация кода: data, models, train, tune, evaluate, predict, serve, utils.
Названия уроков (из выдачи, без точной группировки): Purpose, Product, **Systems design**,
Project, Organization, Packaging, Git, Pre-commit, Logging, Documentation, Styling,
Command-line, **Labeling**, Preprocessing, Exploratory data analysis, Splitting, Augmentation,
Modeling, **Experiment tracking**, **Optimization/tuning**, Evaluation, **Testing (code, data,
model)**, **Reproducibility**, Versioning, **Docker**, Makefile, **RESTful API**, Dashboard,
Interfaces, **CI/CD workflows**, **Monitoring**, **Feature store**, **Pipelines**,
**Orchestration**, **Infrastructure**, Production, **Data engineering**, Scripting, Code.
Практика: Ray Train / Ray Tune / Ray Serve, Anyscale Jobs и Services, continual learning workflows.

### 23. fast.ai — Practical Deep Learning for Coders [ОТКРЫЛ (part 1) + ТОЛЬКО ОПИСАНИЕ (part 2)]
Part 1 (course22): 00 Is it a bird? · 01 Jupyter 101 · 02 Saving a basic fastai model ·
03 Which image models are best (**timm-бенчмарки**) · 04 How does a neural net really work ·
05 Linear model and neural net from scratch · 06 Why you should use a framework ·
07 **How random forests really work** · 08–10 Road to the Top 1/2/3 (**итеративное улучшение
решения на соревновании: first steps → small models → scaling up**).
Part 2 «From Deep Learning Foundations to Stable Diffusion» [ТОЛЬКО ОПИСАНИЕ]:
Л9 Stable Diffusion (Diffusers pipelines, концептуальные части SD); Л9A глубокий разбор
кода и понятий SD; Л9B математика диффузии; Л10 свой diffusion pipeline «с фундамента».
Далее: **DDPM, DDIM**, безусловные и условные диффузионные модели с нуля, разные сэмплеры,
**textual inversion, DreamBooth**.

### 24. MIT — Introduction to Data-Centric AI (IAP 2023/2024) [ОТКРЫЛ]
`https://github.com/dcai-course/dcai-lab` (9 лабораторных = 9 тем)

1. **Data-Centric AI vs Model-Centric AI** — улучшение данных вместо модели
2. **Label Errors** — автоматический поиск ошибок разметки, **Confident Learning**
3. **Dataset Creation and Curation** — датасеты с несколькими аннотаторами, качество разметки
4. **Data-Centric Evaluation of ML Models** — улучшение модели через данные
5. **Class Imbalance, Outliers, and Distribution Shift** — методы детекции выбросов
6. **Growing or Compressing Datasets** — **active learning**, оптимизация состава датасета
7. **Interpretability in Data-Centric ML** — поиск проблем датасета через интерпретируемость
8. **Encoding Human Priors: Data Augmentation and Prompt Engineering**
9. **Data Privacy and Security** — **membership inference attack**
Лекции 2024 добавляют: **Advanced Confident Learning, LLM and GenAI applications**;
**Data Curation for LLMs**.

### 25. Awesome System for Machine Learning — таксономия [ОТКРЫЛ]
`https://raw.githubusercontent.com/HuaizhengZhang/Awesome-System-for-Machine-Learning`
Категории: ML/DL Infra — Data Processing, Training System, **Inference System**,
ML Infrastructure. LLM Infra — **LLM Training**, **LLM Serving**. Domain-Specific Infra —
Video System, **AutoML System**, **Edge AI**, **GNN System**, **Federated Learning System**,
**Deep RL System**. Конференции: OSDI, SOSP, SIGCOMM, NSDI, **MLSys**, ATC, EuroSys, Middleware,
SoCC, TinyML.

### 26. Oxford — Advanced ML / Statistical ML [ТОЛЬКО ОПИСАНИЕ]
Bayesian modelling, **гауссовские процессы**, рандомизированные методы, **байесовские нейросети**,
**приближённый вывод (approximate inference)**, VAE, генеративные модели; SVM и ядровые методы,
**байесовская оптимизация**, латентные переменные.

---

## ДЕЛЬТА: темы, которых нет в нашем манифесте

Порядок — по убыванию важности для middle+ MLE. Темы, уже присутствующие в `STRUCTURE.md`
(GQA/MQA, PagedAttention, vLLM, continuous batching, speculative decoding, FlashAttention,
LoRA/QLoRA, GPTQ/AWQ/GGUF, DDP/FSDP/ZeRO, tensor/pipeline parallelism, mixed precision,
gradient checkpointing, RAG, DPO/GRPO, Chinchilla, PSI/KS-дрифт, CUPED, HNSW/IVF-PQ, LambdaMART
и т.д.), в таблицу **не включены**.

### A. Эффективность, железо, инференс — главный источник дельты

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Устройство GPU: SM, warps, иерархия памяти (HBM/SRAM/регистры), tensor cores, occupancy** | CS336 Л5 «GPUs»; CS294 AI-Sys Л3 «Hardware for ML»; CMU 10-414 Л11–12 | Без этого нельзя объяснить, почему decode memory-bound, почему FlashAttention быстрее и зачем батчить. Прямо спрашивают на LLM-инференс-собесах | `docs/03-deep-learning/06-scaling-and-efficiency.md` (новый блок «железо») + ссылка из `docs/07-mlops/09-inference-optimization.md` |
| **Arithmetic intensity и roofline-модель; compute-bound vs memory-bound** | CS336 Л10 (`lecture_10.py`); MIT 6.5940 Л2 «Efficiency Metrics» | Единственный корректный язык для ответа «почему инференс не ускоряется от более быстрого GPU». Позволяет считать, а не гадать | `docs/05-llm/05-inference-and-serving.md` |
| **FLOPs-бюджет и MFU (Model FLOPs Utilization); формула 6·N·D; как считать FLOPs forward/backward** | CS336 Л2 (`lecture_02.py`) | Стандартный вопрос «сколько будет обучаться модель X на Y GPU». MFU — метрика, по которой оценивают качество инфраструктуры | `docs/03-deep-learning/06-scaling-and-efficiency.md` |
| **Кастомные CUDA/Triton-ядра, fusion операторов, зачем и когда писать своё ядро** | CS336 Л6 «Kernels, Triton»; CMU 10-414 Л13–14 | Отличает middle от middle+ в LLM-инфраструктуре; объясняет природу FlashAttention | `docs/03-deep-learning/06-scaling-and-efficiency.md` |
| **Компиляция моделей: graph capture, operator fusion, `torch.compile`, TVM, XLA, ONNX Runtime graph optimizations** | CS294 AI-Sys Л8; CMU 10-414 Л24 «ML Compilation and Deployment»; UW CSE 599W (TVM) | У нас есть ONNX/TensorRT как «инструменты», но нет объяснения, что они делают. Частый вопрос «как ускорили инференс без потери качества» | `docs/07-mlops/09-inference-optimization.md` |
| **Прунинг всерьёз: гранулярность (unstructured / structured / N:M, 2:4), критерии, lottery ticket hypothesis, аппаратная поддержка разрежённости, sparse matmul** | MIT 6.5940 Л3, Л4; CS294 AI-Sys Л9 | У нас прунинг упомянут одним словом. Без гранулярности ответ «сделаем прунинг» бессмыслен: unstructured не даёт ускорения без поддержки железа | `docs/07-mlops/09-inference-optimization.md` |
| **QAT (quantization-aware training), straight-through estimator, симметричная/асимметричная квантизация, per-tensor/per-channel/per-group, калибровка, векторная квантизация** | MIT 6.5940 Л5, Л6 | У нас перечислены форматы (int8, GPTQ, AWQ, GGUF), но не сам механизм. На собесе спрашивают «в чём разница PTQ и QAT и когда какой» | `docs/05-llm/04-peft-and-quantization.md` |
| **Neural Architecture Search: пространство поиска, оценка производительности (weight sharing, supernet), hardware-aware NAS, once-for-all** | MIT 6.5940 Л7, Л8; CS294 AI-Sys Л9 | Полностью отсутствует у нас. Появляется в вопросах «как выбрать архитектуру под ограничение по латентности» | `docs/07-mlops/09-inference-optimization.md` (обзорно) |
| **Бенчмаркинг ML-нагрузок: MLPerf, как честно измерять latency/throughput, warm-up, устойчивые замеры, отчётность** | CS294 AI-Sys Л11 | У нас есть p50/p95/p99, но нет методологии измерения. Типичная ошибка кандидата — мерить на холодном кэше и одном запросе | `docs/07-mlops/09-inference-optimization.md` |
| **Длинный контекст: sliding-window / attention sinks (StreamingLLM), позиционная интерполяция и YaRN, эффективное внимание, «за пределами трансформеров»** | MIT 6.5940 Л15 (2024); CMU 11-667 Л22 «Long-context models» | У нас есть RoPE/ALiBi, но нет того, как контекст расширяют после обучения. Актуальнейший продуктовый вопрос | `docs/05-llm/01-llm-architecture.md` |
| **State-space модели (S4, Mamba, Jamba) и диффузионные языковые модели как альтернативы трансформеру** | CS336 Л10 (`lecture_10.py`); MIT 6.5940 Л15 | Вопрос «что придёт на смену трансформеру» задают на middle+/senior; нужен внятный ответ про линейную сложность и trade-off | `docs/05-llm/01-llm-architecture.md` |
| **MLA (multi-head latent attention), CLA (cross-layer attention), локальное внимание — как способы сжать KV-кэш** | CS336 Л10 (`lecture_10.py`) | У нас только GQA/MQA. MLA (DeepSeek) — уже индустриальный стандарт; сравнение «на сколько сжали KV и какой ценой» — конкретный инженерный вопрос | `docs/05-llm/05-inference-and-serving.md` |
| **Medusa / EAGLE — обучаемые головы для спекулятивного декодинга; prefix sharing + copy-on-write** | CS336 Л10 (`lecture_10.py`) | У нас speculative decoding общий и «префиксное кэширование» одной строкой. Здесь — конкретные механизмы, которые внедряют | `docs/05-llm/05-inference-and-serving.md` |
| **LLM.int8() и обработка выбросов активаций (outlier features)** | CS336 Л10; MIT 6.5940 Л13 | Объясняет, почему наивная int8-квантизация LLM ломает качество — а это ровно тот вопрос, который задают после «мы квантизовали» | `docs/05-llm/04-peft-and-quantization.md` |
| **Gradient compression / квантизованный all-reduce; коммуникационные примитивы (ring all-reduce, all-gather, reduce-scatter) как отдельная тема** | MIT 6.5940 (описание курса); CS294 AI-Sys Л4–5; UW CSE 599W Л11 | У нас «DDP изнутри (all-reduce)», но нет остальных примитивов и их стоимости. Нужно, чтобы объяснить, почему FSDP дороже DDP по трафику | `docs/08-big-data/07-distributed-training.md` |
| **Sequence / context parallelism; expert parallelism для MoE; комбинирование видов параллелизма (3D)** | CS336 Л7–8 «Parallelism»; MIT 6.5940 Л19–20 | У нас data/tensor/pipeline. Для обучения LLM с длинным контекстом и MoE этого набора уже не хватает | `docs/03-deep-learning/06-scaling-and-efficiency.md` |
| **Инференс на edge / микроконтроллерах: MCUNet, TinyEngine, patch-based inference, оптимизация циклов** | MIT 6.5940 Л11, Л16, Л17; Awesome-Sys «Edge AI» | Нишево, но вылезает на собесах в мобильных/IoT-командах и хорошо показывает понимание memory-bound ограничений | `docs/07-mlops/09-inference-optimization.md` (короткий блок) |
| **On-device training и transfer learning на устройстве** | MIT 6.5940 Л15, Л21 | Понимание, почему обучение на устройстве упирается в память активаций, а не весов | `docs/07-mlops/09-inference-optimization.md` (короткий блок) |

### B. ML-системы и инфраструктура

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Infrastructure as Code (Terraform) для ML-инфраструктуры** | MLOps Zoomcamp Модуль 6; Made With ML («Infrastructure») | У нас есть Docker и k8s, но нет слоя «как эта инфраструктура создаётся». На собесе в командах с облаком спрашивают напрямую | `docs/07-mlops/06-docker-and-k8s.md` |
| **Слои ML-платформы: feature store / model store / evaluation store / dev-окружение; build vs buy** | CS329S Л15 «ML Infrastructure and Platform»; Made With ML | У нас feature store есть отдельной главой, но нет карты платформы целиком и логики «покупать или строить» — это ровно то, что оценивают на System Design у middle+ | `docs/07-mlops/01-ml-lifecycle.md` |
| **Устройство ML-фреймворка изнутри: абстракции Tensor / Op / Module / Optimizer, обратный граф, расширение autograd своей операцией** | CMU 10-414 Л4–8; UW CSE 599W Л3–4 | Даёт корректный ответ на «как работает `.backward()`» глубже, чем «цепное правило»; часто просят написать свою `autograd.Function` | `docs/12-coding/06-pytorch-drills.md` |
| **Реализация свёртки: im2col, тайлинг, почему наивная реализация медленная** | CMU 10-414 Л14 | Конкретная задача с собеса «реализуйте conv2d» и объяснение, откуда берётся скорость cuDNN | `docs/12-coding/03-ml-from-scratch.md` |
| **ML applied to systems: learned indexes, device placement, обучаемые эвристики в инфраструктуре** | CS294 AI-Sys Л7 | Расширяет кругозор и даёт хороший ответ на «где ещё в системе может жить ML»; иногда обсуждают на System Design | `docs/11-system-design/01-framework.md` (врезка) |

### C. Безопасность, приватность, право, справедливость

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Fairness: demographic parity, equalized odds, equal opportunity; аудит модели на смещения по группам; governance и model cards** | CS329S Л14 «ML Beyond Accuracy»; CMU 11-667 Л17 «Bias and ethical issues»; FSDL 2022 Л9 «Ethics»; CS229 (Fairness); CS324 harms-1/harms-2 | **Полностью отсутствует у нас**, при этом это стандартная секция в скоринге, HR-tech, медицине и в любой компании с регулятором. Вопрос «как проверите, что модель не дискриминирует» — реальный | `docs/02-classic-ml/15-interpretability.md` (расширить) или врезка в `docs/09-monitoring/01-what-to-monitor.md` |
| **Adversarial-атаки на модели, adversarial robustness, «обман» сети (fooling networks)** | CS294 AI-Sys Л12; CS182 «GANs & Adversarial Attacks»; CS231n «Fooling ConvNets» | У нас есть prompt injection для LLM, но нет атак на классические/CV-модели. Для антифрода и модерации это прямая рабочая тема | `docs/05-llm/10-llm-safety-and-guardrails.md` (расширить до «безопасность ML-моделей») |
| **Differential privacy и federated learning** | CS294 AI-Sys Л12; CS324 «security»; Awesome-Sys «Federated Learning System» | Возникает в задачах с персональными данными и в мобильных сценариях; DP-SGD спрашивают на позициях, связанных с приватностью | `docs/05-llm/10-llm-safety-and-guardrails.md` или `docs/07-mlops/03-data-and-feature-store.md` |
| **Membership inference, extraction-атаки и запоминание обучающих данных (memorization) моделью** | MIT DCAI Лаб 9; CS324 «security» | Ответ на «может ли модель выдать чужие данные» — обязателен, если продукт обучается на пользовательских данных | `docs/05-llm/10-llm-safety-and-guardrails.md` |
| **Data poisoning / backdoor-атаки на обучающую выборку** | CS324 «security»; CS294 AI-Sys Л12 | Реально в системах с пользовательской обратной связью и в RecSys (петля обратной связи + злоумышленник) | `docs/09-monitoring/02-data-quality.md` |
| **Правовые аспекты обучающих данных: лицензии, copyright / fair use, персональные данные и регуляторика** | CS324 «legality»; CS324 W2023 «Legal Considerations» | Middle+ обязан уметь сказать «на этих данных обучаться нельзя». Мы про PII говорим, а про лицензии на корпуса — нет | `docs/05-llm/02-pretraining-and-scaling.md` |
| **Экологическая цена обучения: энергопотребление, углеродный след, отчётность** | CS324 «environment»; CS324 W2023 «Environmental Impact» | Низкий приоритет, но встречается в вопросах про бюджет и в требованиях крупных компаний | `docs/07-mlops/10-cost-and-capacity.md` (абзац) |

### D. Данные и разметка (data-centric)

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Поиск ошибок разметки: Confident Learning, оценка качества аннотаций, согласие аннотаторов** | MIT DCAI Лаб 2, 3; CS329S Л3 «Training Data»; FSDL Лаб 6 | У нас разметка упоминается только в контексте LLM-оценки. «Модель не учится — виноваты метки» — реальный сценарий, и его надо уметь диагностировать | `docs/02-classic-ml/05-validation-and-leakage.md` или `docs/07-mlops/03-data-and-feature-store.md` |
| **Active learning и коресеты: как решить, что размечать дальше; сжатие/наращивание датасета** | MIT DCAI Лаб 6; CS329S Л3 | Прямой ответ на «бюджет разметки ограничен, что делать» | `docs/02-classic-ml/14-feature-engineering.md` или новая врезка в `docs/07-mlops/03-data-and-feature-store.md` |
| **Data-centric подход как парадигма: улучшать данные вместо модели; систематическая работа с датасетом** | MIT DCAI Лаб 1, 4; CS329S Л3–4 | Ровно то, что отличает middle+ («поднял качество без смены модели») от middle («взял модель побольше») | `docs/02-classic-ml/14-feature-engineering.md` |
| **Синтетические данные: генерация, self-instruct, дистилляция из большой модели, риски (model collapse, утечка бенчмарков)** | CMU 11-667 Л23 «Training with Synthetic Data» | Стандартная практика 2024–2026 при нехватке данных; спрашивают про риски | `docs/05-llm/03-sft-and-alignment.md` |
| **Пайплайн фильтрации веб-корпуса: определение языка (fastText), quality-классификатор, эвристики (Gopher rules), удаление PII, токсичности, near-dedup** | CS336 Л13–14 «Data» + задание 4 (WET-файлы, `is_english`); CMU 11-667 Л3; CS324 «data» | У нас «данные и их фильтрация, дедупликация» одной строкой. Здесь — конкретный воспроизводимый пайплайн, о котором спрашивают предметно | `docs/05-llm/02-pretraining-and-scaling.md` |
| **MinHash / SimHash / LSH: шинглинг, near-duplicate detection** | CS246 «similarity search»; CS336 Л13–14 (дедупликация корпусов) | **Отсутствует у нас полностью.** Используется и для дедупликации корпусов LLM, и для дедупликации выдачи в RecSys, и в антифроде. Классический вопрос с собеса про большие данные | `docs/08-big-data/01-storage-and-formats.md` или `docs/02-classic-ml/12-dimensionality-reduction.md` |

### E. Оценка и качество моделей

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Поведенческое тестирование моделей (CheckList / RecList): инвариантности, directional expectations, minimum functionality tests, slice-based оценка** | CS329S Л7 (RecList); FSDL 2022 Л3 «Troubleshooting & Testing» | У нас есть «сегментный анализ» и тесты кода, но нет самой концепции behavioral testing. Это конкретный, воспроизводимый ответ на «как вы тестируете модель, а не код» | `docs/12-coding/07-testing-and-code-quality.md` и `docs/02-classic-ml/04-metrics.md` |
| **Error analysis по Ng: ceiling analysis, ablative analysis, приоритизация улучшений по вкладу в метрику** | CS229 (лекция «ML Advice»); FSDL 2022 Л3 | Ровно тот навык, который проверяют вопросом «модель даёт 0.7 AUC, что делаете дальше». Отвечать «потюню гиперпараметры» — провал | `docs/11-system-design/01-framework.md` и `docs/02-classic-ml/04-metrics.md` |
| **Интерпретируемость нейросетей и LLM: probing, механистическая интерпретируемость, визуализация признаков, интерпретируемость ради поиска проблем в данных** | CMU 11-667 Л14 «Interpretability methods»; CS231n «Visualizing and Understanding CNNs»; MIT DCAI Лаб 7 | У нас глава про интерпретируемость целиком про табличные модели (SHAP/LIME/PDP). Для DL/LLM инструментов нет | `docs/02-classic-ml/15-interpretability.md` (расширить) или врезка в `docs/05-llm/09-llm-evaluation.md` |
| **Диагностика обучения по инструментам: gradient checks, sanity checks, «babysitting» процесса обучения** | CS231n Neural Networks Part 3 | У нас есть «диагностика обучения по графикам», но не конкретные проверки (градиентная проверка, оверфит на одном батче) | `docs/03-deep-learning/02-training-dynamics.md` |

### F. Генеративные модели и CV/мультимодальность

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Диффузионные модели: DDPM, DDIM, latent diffusion, сэмплеры, conditioning; textual inversion / DreamBooth** | CS231n 2025 Л14; MIT 6.5940 Л18 (Fall 2024); fast.ai part 2; CMU 11-777 Л9.2 | **Отсутствует у нас полностью.** В 2026 это базовая грамотность: генерация контента есть почти в каждом продукте; спрашивают «чем диффузия отличается от GAN и почему победила» | `docs/13-optional/01-computer-vision.md` (расширить) или новая врезка в `docs/13-optional/03-multimodal.md` |
| **VAE и GAN: латентные переменные, ELBO, режимы отказа GAN (mode collapse)** | CS231n 2025 Л13; CS182 «Autoencoders & Latent Variable Models», «VAE & Invertible Models», «GANs»; CMU 10-414 Л16–17; CMU 11-777 Л9.2; Oxford AdvML | У нас автоэнкодеры есть (в снижении размерности и аномалиях), но VAE/GAN как генеративные модели — нет. Нужны как фон для диффузии и для вопросов про генерацию | `docs/13-optional/01-computer-vision.md` |
| **Self-supervised learning в CV: contrastive (SimCLR, MoCo), self-distillation (DINO), masked image modeling (MAE)** | CS231n 2025 Л12 + задание A3 (SSL, DINO); CMU 11-777 Л4.2 | У нас контрастивное обучение упомянуто только через CLIP. SSL — стандартный ответ на «мало разметки, много картинок» | `docs/13-optional/01-computer-vision.md` |
| **Мультимодальность как таксономия: representation, alignment/grounding, reasoning, generation, transference, quantification; multimodal fusion (early/late/tensor), coordinated representations** | CMU 11-777 (Л1.1, 3.1, 3.2, 4.1, 5.2, 11.2, 12.2) | У нас глава про мультимодальность — это CLIP + VLM. Таксономия даёт язык, на котором обсуждают дизайн мультимодальной системы на System Design | `docs/13-optional/03-multimodal.md` |
| **Video understanding (temporal modeling) и 3D/NeRF — обзорно** | CS231n 2025 Л10, Л15; MIT 6.5940 Л18–19 | Низкий приоритет для не-CV MLE, но полезно как «что вообще существует» | `docs/13-optional/01-computer-vision.md` (по одному абзацу) |

### G. Обучение с подкреплением

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Базис RL: MDP, value/policy iteration, Q-learning, TD-learning, REINFORCE/policy gradient, actor-critic, TRPO/PPO** | Berkeley CS285 Л4–9; CS229 недели 7–8; CMU 11-777 Л7.1 | У нас RL появляется только «изнутри» RLHF (PPO, DPO, GRPO) и в бандитах. Без базиса нельзя объяснить, что такое advantage, baseline, KL-штраф — а именно это спрашивают, когда копают RLHF | `docs/05-llm/03-sft-and-alignment.md` (предварительный блок) или новая врезка в `docs/10-recsys/13-exploration-and-bandits.md` |
| **Offline RL и imitation learning / behavior cloning** | Berkeley CS285 Л2, Л15–16 | Прямо связано с обучением на логах в RecSys и с off-policy оценкой; даёт корректный язык для «учимся на исторических логах» | `docs/10-recsys/13-exploration-and-bandits.md` |
| **RLVR — RL с верифицируемыми наградами; reasoning-модели и test-time compute** | CS336 Л16 «RLVR», задание 5 «Alignment and Reasoning RL»; CMU 11-667 | Ключевой сдвиг 2025–2026 (o1/R1-стиль). У нас есть CoT и self-consistency, но нет обучения рассуждению и масштабирования вычислений на инференсе | `docs/05-llm/03-sft-and-alignment.md` и `docs/05-llm/06-prompting-and-structured-output.md` |

### H. Большие данные и графы

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Вероятностные структуры для потоков: Bloom filter, HyperLogLog, Count-Min sketch, reservoir sampling** | CS246 «Stream data processing» | У нас глава про стриминг — это Kafka/окна/watermark. Приближённые структуры — классика собеса по большим данным (уникальные пользователи за день, дедупликация в потоке) | `docs/08-big-data/05-streaming.md` |
| **Частые наборы и ассоциативные правила: A-Priori, PCY, support/confidence/lift** | CS246 «Association rules» | Market basket по-прежнему спрашивают в ретейле и e-commerce; у нас темы нет вообще | `docs/02-classic-ml/11-clustering.md` (соседняя тема unsupervised) или `docs/08-big-data/02-sql-for-mle.md` |
| **PageRank и персонализированный PageRank; борьба со спамом в графе (TrustRank)** | CS246 «Link Analysis»; CS224W | У нас графы только в RecSys-главе (GCN/LightGCN). PPR — базовый алгоритм кандидатогенерации и графового поиска | `docs/10-recsys/10-graph-recsys.md` |
| **Random-walk эмбеддинги графа: DeepWalk, node2vec; label propagation** | CS224W («Node Embeddings», «Label Propagation»); конспекты CS224W | Дешёвая и до сих пор рабочая альтернатива GNN; спрашивают как «а если GNN не потянет по масштабу» | `docs/10-recsys/10-graph-recsys.md` |
| **Графы знаний и их эмбеддинги (TransE и др.), reasoning over KG, метапути** | CS224W («Knowledge Graph Embeddings», «Reasoning over KG», «Knowledge Graphs and Metapaths»); CMU 11-777 Л7.2 | Основа GraphRAG и структурированного поиска; актуально для RAG-систем поверх корпоративных данных | `docs/05-llm/07-rag.md` (продвинутые схемы) |
| **Community detection / modularity, spectral clustering на графах** | CS246; CS224W («Community Structure», «Spectral Clustering») | Расширяет главу о кластеризации на графовые данные (сегментация пользователей по связям, антифрод-кластеры) | `docs/02-classic-ml/11-clustering.md` |
| **MapReduce как модель вычислений (не только Spark API)** | CS246; CS294 AI-Sys Л2 | У нас Spark разобран, но парадигма map/shuffle/reduce как таковая — нет. Помогает отвечать на «спроектируйте распределённый подсчёт X» | `docs/08-big-data/03-spark-fundamentals.md` |
| **CUR-разложение** | CS246 «Dimensionality reduction: UV, SVD, CUR» | Низкий приоритет; упомянуть рядом с SVD как интерпретируемую альтернативу | `docs/02-classic-ml/12-dimensionality-reduction.md` (абзац) |

### I. Реклама и продуктовые механики

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Вычислительная реклама: аукционы (second-price/GSP), AdWords и BALANCE, распределение бюджета, pacing** | CS246 «Computational advertising» | У нас есть кейс «предсказание CTR в рекламе», но нет механики монетизации. Вопрос «CTR предсказали — а как решаем, чью рекламу показать» ставит кандидата в тупик | `docs/11-system-design/08-case-ads-ctr.md` |
| **UX-паттерны LLM-приложений: стриминг, черновики/варианты, undo, индикация неуверенности, дизайн доверия** | FSDL LLM Bootcamp «UX for Language User Interfaces» | Middle+ обсуждает продуктовую сторону: «модель иногда врёт» решается не только моделью, но и интерфейсом | `docs/05-llm/11-llm-in-production.md` |
| **Сбор и использование пользовательского фидбека (thumbs up/down) как контура улучшения LLM-продукта** | LLM Zoomcamp Модуль 5; CS329S Л11 | Замыкает петлю «мониторинг → данные → дообучение» для LLM; у нас петля описана для классического ML | `docs/05-llm/09-llm-evaluation.md` |

### J. Организация работы

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Управление ML-проектом: состав и структура команды, оценка сроков в условиях неопределённости, почему ML-проекты проваливаются** | FSDL 2022 Л8 «ML Teams and Project Management»; CS329S Л17 | На middle+ спрашивают «как вы планировали работу, если непонятно, взлетит ли модель». У нас есть роли в жизненном цикле, но нет управления проектом | `docs/14-career/02-behavioral.md` или `docs/07-mlops/01-ml-lifecycle.md` |
| **Итеративное улучшение решения (baseline → small models → scaling up) как рабочая методика** | fast.ai part 1, уроки 08–10 «Road to the Top»; CS329S Л5 | Даёт кандидату скелет ответа на любую практическую секцию: начинать с маленького и быстро итерироваться | `docs/00-start/04-study-method.md` или `docs/11-system-design/01-framework.md` |

---

## Чего найти не удалось

1. **Полное понедельное расписание Stanford CS224n** (W2025/W2026) — сайт 403, GitHub-зеркала
   с расписанием нет. Есть только тематический состав и названия лекций 1, 2, 9, 10, 11.
   Единственный найденный официальный силлабус в GitHub (`stanfordnlp/cs224n-web`) — **версия 2015
   года**, полностью устаревшая (SMT, word alignment, tree-RNN).
2. **Полное расписание Stanford CS231n 2025** (лекции 1–18 списком) — собрано частично из
   поисковой выдачи (Л3, 5, 6, 9, 10, 12–18). Неофициальный репозиторий конспектов
   `raimbekovm/cs231n-2025-notes` заполнен только до лекции 4.
3. **Пословное расписание Stanford CS246 по датам** — есть только тематический список курса.
   Учебник mmds.org (оглавление) недоступен — 403.
4. **Полное расписание Berkeley CS182/282A** для конкретного семестра — только тематический состав
   версии Spring 2021.
5. **Полное расписание Berkeley CS285** с сайта — собрано из выдачи до лекции 16, дальше
   (Inverse RL, transfer/meta-RL, RL as inference) подтверждено только упоминанием.
6. **NYU Deep Learning (LeCun/Canziani)** — понедельного плана получить не удалось: README
   репозиториев DLSP20/DLSP21 содержат только инструкции по установке окружения,
   сайт `atcold.github.io` недоступен.
7. **Cambridge MLMI** — детального списка модулей и лекций не нашёл; открылась только страница
   «Course Structure» без содержания.
8. **MIT 6.036** — программу получить не удалось.
9. **Made With ML** — точная группировка уроков по секциям (Design / Data / Model / Develop /
   Utilities / Test / Reproducibility / Production / Data Engineering) не подтверждена: названия
   уроков собраны, но их порядок и разбиение — только из поисковой выдачи, сайт 403.
10. **MIT 6.5940 Fall 2024** — лекции 2 и 9 (номера между подтверждёнными блоками) не
    идентифицированы точно; нумерация между Fall 2023 и Fall 2024 сдвинута, и я не смог
    получить единый официальный список одного семестра.
11. **CMU 11-777 Fall 2023** — в `_data/lectures_2023.yml` отсутствуют лекции 8.x, 10.x и 11.1
    (в файле их нет). Это пробел самого источника, не поиска.
12. **Oxford / Cambridge** — ничего, что дало бы дельту сверх уже найденного: гауссовские процессы,
    байесовские нейросети и approximate inference — единственные кандидаты, но для MLE-собеса
    в продуктовой компании они малорелевантны, поэтому в дельту я их не выносил.

### Отдельно: что проверил и дельты НЕ нашёл

- **CMU 10-701** — полностью покрывается нашим разделом 02 (MLE/MAP, наивный Байес, SVM с
  двойственностью и KKT, ядра, бустинг, RF). KKT у нас уже есть в `01-math/04-optimization.md`.
- **CS229** — покрыт, кроме `ML Advice` и `Fairness` (вынесены в дельту).
- **fast.ai part 1** — покрыт, кроме методики «Road to the Top» (вынесена в дельту).
- **MLOps Zoomcamp** — покрыт целиком, кроме Terraform/IaC (вынесен в дельту).
- **LLM Zoomcamp** — покрыт целиком (RAG, гибридный поиск, реранкинг, offline/online оценка,
  мониторинг), кроме контура пользовательского фидбека (вынесен в дельту).
- **CS329S лекции 1–6, 8–13** — покрыты нашими разделами 07 и 09 практически один в один.
