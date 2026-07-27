# Канон источников

> Отобранный список материалов, на которых стоит хендбук. Каждый источник проверялся
> на существование: часть страниц скачивалась целиком, статьи сверялись по карточкам arXiv,
> остальное подтверждалось поисковой выдачей. Ссылок «по памяти» здесь нет.

## Как читать этот список

**Не читайте его подряд.** Это карта, а не программа. Правильный порядок работы такой:
проходите главу хендбука → делаете задачи → и только потом идёте в первоисточник, если тема
стала вашей рабочей. Оригинальные статьи написаны для тех, кто уже держит контекст в голове;
до главы они читаются вечер, после — полчаса.

**Легенда.** `[MUST]` — источник, без которого на указанном грейде будет заметная дыра.
`[OPT]` — берите по мере надобности. Грейд означает, **с какого уровня** источник начинает
быть нужным, а не «для кого он написан».

**Про русскоязычные источники.** Они выделены намеренно: если вы собеседуетесь в РФ, вопросы
часто формулируются языком учебника ШАДа и открытого курса ODS, а разборы Дьяконова закрывают
тонкости (ROC-AUC, утечки, метрики), которых нет больше нигде на русском.

---

Легенда: **[MUST]** — обязательно к прочтению для соответствующего грейда; **[OPT]** — опционально/по мере надобности.
Грейд означает: на каком уровне этот источник начинает быть нужен.

### 0. Математика и статистика (глава 01-math)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Хендбук по математике для аналитики и ML (Яндекс)** | https://education.yandex.ru/handbook/math | актуальный | Быстрое закрытие дыр по линалу/матану/теорверу на русском. Для junior — основной вход, для middle — справочник. | **[MUST]** junior |
| **Mathematics for Machine Learning (Deisenroth, Faisal, Ong)** | https://mml-book.github.io | 2020 | Единственная книга, где линал+матан+вероятности изложены *через* задачи ML (PCA, GMM, SVM выведены с нуля). Брать главы 2–5 и 10–12. | **[MUST]** junior→middle |
| **Курс матстата и A/B Ф. Ульянкина** | https://github.com/FUlyankin/matstat-AB | — | 16 недель на русском: ЗБЧ/ЦПТ → оценки → доверительные интервалы → проверка гипотез → непараметрический бутстрап → A/B. Единственный русский материал, где бутстрап объяснён до уровня «могу вывести на собесе». | **[MUST]** middle |
| **Stanford CS109 + книга «Probability for Computer Scientists»** | https://chrispiech.github.io/probabilityForComputerScientists/en/index.html | актуальный | Вероятностная база в формате «для программистов»: без меры, но с корректными доказательствами. | **[OPT]** junior |
| **Boyd & Vandenberghe, Convex Optimization** | https://web.stanford.edu/~boyd/cvxbook/ | 2004 | Из всей книги для MLE нужны гл. 2–3 (выпуклые множества и функции), 5 (двойственность — чтобы понимать SVM) и 9–10 (методы спуска). Читать целиком не нужно и не надо. | **[OPT]** middle_plus |
| **Seeing Theory (Brown)** | https://seeing-theory.brown.edu/index.html | — | Интерактивные визуализации ЦПТ, доверительных интервалов, байесовского вывода. Хорошо как «первый контакт» и как источник картинок для главы. | **[OPT]** junior |
| **Causal Inference: What If (Hernán & Robins)** | https://miguelhernan.org/whatifbook | 2020 | Нужна, когда в A/B-главе доходишь до confounding, switchback и quasi-experiments. | **[OPT]** middle_plus |

### 1. Классический ML (глава 02-classic-ml)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **ESL — The Elements of Statistical Learning** | https://hastie.su.domains/ElemStatLearn/ · PDF: https://web.stanford.edu/~hastie/Papers/ESLII.pdf | 2009 (2nd ed., 12-й тираж 2017) | **Опорный текст всей главы.** Гл. 3 (линейные методы + регуляризация), 7 (bias-variance, AIC/BIC, кросс-валидация), 9 (деревья), 10 (бустинг), 15 (Random Forest). Именно эту книгу Т-Банк даёт кандидатам как литературу к ML-секции. | **[MUST]** middle |
| **ISLR / ISLP — An Introduction to Statistical Learning** | https://www.statlearning.com/ | 2013 / 2023 (Python ed.) | «ESL для людей»: те же темы без матрично-статистического аппарата. Для junior — читать вместо ESL, для middle — читать *до* ESL, чтобы построить интуицию. | **[MUST]** junior |
| **Учебник по ML ШАДа** | https://education.yandex.ru/handbook/ml · материалы: https://github.com/yandexdataschool/ML-Handbook-materials | 2021→наст. вр. | **Главный русскоязычный канон.** Прямо позиционируется как «продвинутый учебник без упрощений, от базовых алгоритмов до тем из свежих статей». На собесах в РФ вопросы часто формулируются его языком. | **[MUST]** junior→middle_plus |
| **Открытый курс ODS / mlcourse.ai** | https://github.com/Yorko/mlcourse.ai · https://ods.ai/tracks/open-ml-course | 2017→наст. вр. | 10 тем с полными статьями на Habr: EDA/Pandas → визуализация → деревья и kNN → линейные модели → бэггинг и RF → feature engineering → PCA/кластеризация → Vowpal Wabbit → временные ряды → градиентный бустинг. Лучший бесплатный русский вход в практику. | **[MUST]** junior |
| **Курс лекций К. В. Воронцова** | http://www.machinelearning.ru/wiki/index.php?title=Машинное_обучение_(курс_лекций,_К.В.Воронцов) | — | Академический русский канон: формальные постановки, теория обобщающей способности, метрические и линейные методы. Брать конспекты как источник строгих определений. | **[OPT]** middle |
| **Курс А. Дьяконова «ML and Data Mining» (ВМК МГУ)** | https://github.com/Dyakonov/MLDM | 2022 | 10 лекций: термины → постановки → математика в ML → метрические алгоритмы → линейная и логистическая регрессия → суррогатные функции и SVM → деревья (сложность, смещение, разброс) → ансамбли → разбор реальной задачи. Очень удачная последовательность для структуры главы. | **[MUST]** junior→middle |
| **Блог Дьяконова «Анализ малых данных»** | https://dyakonov.org/ag/ | — | Разборы тонкостей (ROC-AUC, метрики, утечки), которые больше нигде на русском не сформулированы так же аккуратно. | **[OPT]** middle |
| **Bishop, Pattern Recognition and Machine Learning** | https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/ | 2006 | Байесовский взгляд. Реально нужны гл. 1–4 (вероятностная постановка, линейные модели), 9 (EM/GMM). Тоже в списке литературы Т-Банка. | **[OPT]** middle_plus |
| **Murphy, Probabilistic ML: An Introduction / Advanced Topics** | https://probml.github.io/pml-book/ | 2022 / 2023 | Самый современный «большой учебник». Использовать как энциклопедию-справочник, а не как книгу для линейного чтения. Код на JAX/PyTorch/sklearn. | **[OPT]** middle_plus |
| **XGBoost: A Scalable Tree Boosting System** | https://arxiv.org/abs/1603.02754 | 2016 | Откуда берётся второй порядок в бустинге, регуляризация в целевой функции, sparsity-aware split finding, weighted quantile sketch. Классический вопрос: «почему XGBoost использует гессиан». | **[MUST]** middle |
| **LightGBM: A Highly Efficient GBDT** | https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree | 2017 | GOSS и EFB — два конкретных ответа на вопрос «чем LightGBM быстрее XGBoost». Плюс leaf-wise рост дерева. | **[MUST]** middle |
| **CatBoost: unbiased boosting with categorical features** | https://arxiv.org/abs/1706.09516 | 2017 | Ordered boosting и ordered target statistics — единственный корректный ответ на «что такое target leakage при кодировании категорий и как CatBoost с ним борется». Особенно важно на собесах в РФ. | **[MUST]** middle |
| **Interpretable Machine Learning (Molnar)** | https://christophm.github.io/interpretable-ml-book/ | — | Permutation importance, PDP/ICE, LIME, SHAP — с честным описанием, где каждый метод врёт. | **[OPT]** middle |
| **MLU-Explain (Amazon)** | https://mlu-explain.github.io/ | — | Интерактивные объяснения bias-variance, ROC/AUC, деревьев. Источник визуальных метафор для хендбука. | **[OPT]** junior |
| **StatQuest (Josh Starmer)** | https://www.youtube.com/@statquest/videos | — | Когда нужно «объяснить как на собесе за 3 минуты» — эталон подачи. | **[OPT]** junior |

### 2. Deep Learning (глава 03-deep-learning)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Goodfellow, Bengio, Courville — Deep Learning** | https://www.deeplearningbook.org/ | 2016 | Ч. II (гл. 6–9: MLP, регуляризация, оптимизация, CNN) — до сих пор лучший систематический текст. Ч. III устарела. В списке литературы Т-Банка. | **[MUST]** middle |
| **Dive into Deep Learning (d2l.ai)** | https://d2l.ai/index.html | актуальный | Единственная книга, где каждая формула сразу сопровождается исполняемым кодом на нескольких фреймворках. Для практики. | **[MUST]** junior→middle |
| **Understanding Deep Learning (Prince)** | https://udlbook.github.io/udlbook/ | 2023 | Современная замена Goodfellow: трансформеры, диффузия, GNN изложены с нуля и с отличными иллюстрациями. | **[MUST]** middle |
| **Bishop & Bishop — Deep Learning: Foundations and Concepts** | https://www.bishopbook.com | 2024 | Байесовский и вероятностный взгляд на DL. | **[OPT]** middle_plus |
| **Karpathy, Neural Networks: Zero to Hero** | https://karpathy.ai/zero-to-hero.html · https://github.com/karpathy/nn-zero-to-hero | 2022–2023 | micrograd → makemore → GPT с нуля. **Обязательно** тем, кто не может уверенно вывести backprop на бумаге — а это ловят почти везде. | **[MUST]** junior→middle |
| **Practical DL (ШАД + ВШЭ + Сколтех)** | https://github.com/yandexdataschool/Practical_DL | осень 2025 | 14 недель: backprop и оптимизация → dropout/нормализации → CNN → fine-tuning → интерпретируемость → NLP → LM → трансформеры → LLM → генеративные → диффузия → инференс → RL → аудио. Хороший скелет для оглавления DL-раздела. | **[MUST]** middle |
| **Deep Learning School ФПМИ МФТИ** | https://dls.samcs.ru/ · https://stepik.org/course/230362/promo | 2025 | Бесплатный русскоязычный вход в DL (2 семестра по 12–13 недель). Для junior и для тех, кто переучивается из аналитики. | **[MUST]** junior |
| **Adam: A Method for Stochastic Optimization** | https://arxiv.org/abs/1412.6980 | 2014 | Первый и второй моменты, bias correction. Классический вопрос: «почему нужна bias correction на первых шагах». | **[MUST]** junior→middle |
| **Batch Normalization** | https://arxiv.org/abs/1502.03167 | 2015 | Формулировка через internal covariate shift + различие train/eval режимов (running statistics). Важно: современное объяснение эффекта другое — стоит указать в хендбуке. | **[MUST]** junior→middle |
| **Deep Residual Learning (ResNet)** | https://arxiv.org/abs/1512.03385 | 2015 | Почему skip-connection складывают, а не конкатенируют, и как это решает деградацию градиента. | **[MUST]** junior→middle |
| **Identity Mappings in Deep Residual Networks** | https://arxiv.org/abs/1603.05027 | 2016 | Pre-activation блок; объясняет, почему порядок BN/ReLU/conv имеет значение. | **[OPT]** middle_plus |
| **Dropout: A Simple Way to Prevent NN from Overfitting** | JMLR 15 (2014) | 2014 | Интерпретация как ансамбль подсетей + inverted dropout на инференсе. | **[MUST]** junior |
| **Google Deep Learning Tuning Playbook** | https://github.com/google-research/tuning_playbook | 2023 | Единственный источник, где системно расписано, *в каком порядке* крутить гиперпараметры. Прямо переносится в раздел «как отлаживать обучение». | **[MUST]** middle |
| **Efficient DL Systems (ВШЭ + ШАД)** | https://github.com/mryab/efficient-dl-systems | 2026 | CUDA/GPU → профилирование → data-parallel и All-Reduce → обучение больших моделей → sharded (ZeRO/FSDP) → перформанс from first principles → деплой → системные и алгоритмические оптимизации инференса. Закрывает почти весь middle_plus DL-инфраструктурный блок. | **[MUST]** middle_plus |
| **ml-engineering (Stas Bekman)** | https://github.com/stas00/ml-engineering | актуальный | Практика обучения LLM/VLM на кластере (опыт BLOOM-176B, IDEFICS-80B): ускорители, сеть, storage, SLURM, отладка падений. Уникально тем, что это записи реальных инцидентов. | **[OPT]** middle_plus |
| **The Little Book of Deep Learning (Fleuret)** | https://fleuret.org/francois/lbdl.html | — | 160 страниц на телефоне — идеально для повторения перед собесом. | **[OPT]** junior |
| **Deep Learning Interviews (arXiv 2201.00650)** | https://arxiv.org/abs/2201.00650 | 2022 | Сборник задач с решениями по DL в формате интервью. | **[OPT]** middle |
| **DLtest (Дьяконов)** | https://github.com/Dyakonov/BOOKs/blob/main/DLtest_Dyakonov.pdf | — | Русскоязычный тест по DL — удобный формат для «проверь себя» в конце главы. | **[OPT]** middle |

### 3. NLP и LLM (главы 04-nlp, 05-llm)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Attention Is All You Need** | https://arxiv.org/abs/1706.03762 | 2017 | Первоисточник трансформера. На собесе спрашивают: зачем деление на √d_k, зачем multi-head, чем self- отличается от cross-attention, почему сложность O(n²). | **[MUST]** junior→middle |
| **BERT** | https://arxiv.org/abs/1810.04805 | 2018 | MLM + NSP, [CLS]/[SEP], двунаправленность. Обязательный вопрос «как обучался BERT». | **[MUST]** junior→middle |
| **GPT-3 / Language Models are Few-Shot Learners** | https://arxiv.org/abs/2005.14165 | 2020 | Откуда взялись few-shot/in-context learning и почему decoder-only победил. | **[MUST]** middle |
| **InstructGPT** | https://arxiv.org/abs/2203.02155 | 2022 | Трёхстадийный пайплайн SFT → Reward Model → PPO. Каноничный ответ на «как устроен RLHF». | **[MUST]** middle |
| **DPO** | https://arxiv.org/abs/2305.18290 | 2023 | Почему можно выкинуть отдельную reward-модель и PPO. Стандартный follow-up после RLHF. | **[MUST]** middle→middle_plus |
| **Chinchilla / Training Compute-Optimal LLMs** | https://arxiv.org/abs/2203.15556 | 2022 | Соотношение параметров и токенов (~20 токенов на параметр). Ответ на «как выбрать размер модели под бюджет». | **[MUST]** middle_plus |
| **LoRA** | https://arxiv.org/abs/2106.09685 | 2021 | Низкоранговые адаптеры, rank/alpha, почему экономит память оптимизатора, а не активаций. Самая частая практическая тема на LLM-собесах. | **[MUST]** middle |
| **FlashAttention** | https://arxiv.org/abs/2205.14135 | 2022 | IO-awareness, tiling, отказ от материализации матрицы внимания. Ответ на «как бороться с квадратичной памятью внимания». | **[MUST]** middle_plus |
| **PagedAttention / vLLM** | https://arxiv.org/abs/2309.06180 | 2023 | KV-cache как виртуальная память, continuous batching. Ключ к разделу про инференс и throughput. | **[MUST]** middle_plus |
| **LLaMA** | https://arxiv.org/abs/2302.13971 | 2023 | RMSNorm, SwiGLU, RoPE, pre-norm — «архитектурный стандарт» современных открытых LLM. | **[MUST]** middle |
| **RAG (обзор)** | https://arxiv.org/abs/2404.10981 | 2024 | Систематизация RAG-пайплайнов; удобно как источник таксономии для главы. Оригинальную статью Lewis et al. 2020 (arXiv:2005.11401) стоит указать, но она в этой сессии не верифицирована. | **[MUST]** middle |
| **NLP Course | For You (Lena Voita)** | https://lena-voita.github.io/nlp_course.html | актуальный | Word embeddings, классификация, LM, seq2seq+attention, transfer learning. Лучшие в мире объяснения attention с анимациями. | **[MUST]** junior→middle |
| **YSDA NLP Course** | https://github.com/yandexdataschool/nlp_course | 2025 | 14 недель: embeddings → LM → seq2seq/attention/BPE → transfer learning (ELMo/GPT/BERT) → LLM и scaling laws → prompting и CoT → fine-tuning → эффективность → RAG → агенты → интерпретируемость → мультимодальность → прод. Готовое оглавление NLP+LLM-раздела. | **[MUST]** middle |
| **Speech and Language Processing (Jurafsky & Martin), 3rd ed.** | https://web.stanford.edu/~jurafsky/slp3/ | draft | Классика для «дотрансформерного» NLP: токенизация, N-граммы, HMM, парсинг. Нужно, когда спрашивают про TF-IDF, BM25, CRF. | **[OPT]** middle |
| **The Illustrated Transformer (Jay Alammar)** | https://jalammar.github.io/illustrated-transformer/ | 2018 | Каноническое визуальное объяснение. Использовать как ориентир для собственных схем в хендбуке. | **[MUST]** junior |
| **The Annotated Transformer (Harvard NLP)** | https://github.com/harvardnlp/annotated-transformer | — | Статья построчно превращена в код. Для тех, кого просят «напиши multi-head attention». | **[MUST]** middle |
| **Блог Lilian Weng** | https://lilianweng.github.io/ | — | «The Transformer Family», «Attention? Attention!», обзоры по агентам и галлюцинациям. Часто это лучший обзор темы вообще. | **[MUST]** middle |
| **LLMs-from-scratch (Raschka)** | https://github.com/rasbt/LLMs-from-scratch | 2024 | Сборка GPT-подобной модели с нуля; закрывает вопросы про токенизацию, KV-cache и генерацию. | **[MUST]** middle |
| **CS336: Language Modeling from Scratch (Stanford)** | https://stanford-cs336.github.io/spring2025/ | 2025 | Самый глубокий публичный курс про то, как реально строят LLM (данные, токенизация, параллелизм, alignment, инференс). | **[OPT]** middle_plus |
| **minbpe (Karpathy)** | https://github.com/karpathy/minbpe | 2024 | BPE в 200 строк — закрывает популярный вопрос «как работает токенизатор». | **[MUST]** middle |
| **NLP Course by Hugging Face** | https://huggingface.co/course/chapter0 | актуальный | Практический стандарт индустрии: `transformers`, `datasets`, `peft`. | **[MUST]** junior→middle |
| **ruMTEB / FRIDA (SberDevices, X5 Tech)** | https://habr.com/ru/companies/sberdevices/articles/831150/ · https://habr.com/ru/companies/X5Tech/articles/845398/ · https://habr.com/ru/companies/sberdevices/articles/909924/ | 2024–2025 | **Обязательно для российского рынка.** Как выбирать эмбеддинг-модель под русский язык, какие бенчмарки существуют, чем FRIDA отличается от e5/BGE. Вопрос «какую эмбеддинг-модель возьмёшь для русского RAG» встречается регулярно. | **[MUST]** middle |
| **What are Embeddings (Vicki Boykis)** | https://vickiboykis.com/what_are_embeddings/index.html | 2023 | История эмбеддингов от one-hot до трансформеров, честно про подводные камни. | **[OPT]** middle |
| **Prompt Engineering Guide** | https://www.promptingguide.ai/ · https://github.com/dair-ai/Prompt-Engineering-Guide | актуальный | Систематика приёмов; полезнее как справочник, чем как чтение. | **[OPT]** junior |
| **Advanced RAG Techniques (NirDiamant)** | https://github.com/NirDiamant/RAG_Techniques | 2024 | Каталог продвинутых RAG-приёмов с кодом: reranking, query rewriting, hybrid search, self-RAG. | **[MUST]** middle_plus |
| **AI Engineering (Chip Huyen)** | https://www.oreilly.com/library/view/ai-engineering/9781098166298/ · https://github.com/chiphuyen/aie-book | 2025 | Как строить продукты поверх foundation models: оценка, промптинг vs finetuning, RAG vs агенты, инференс-оптимизация, экономика. Самая читаемая книга платформы O'Reilly в 2025. | **[MUST]** middle→middle_plus |

### 4. Рекомендательные системы (глава 06-recsys)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **BPR: Bayesian Personalized Ranking** | https://arxiv.org/abs/1205.2618 | 2012 | Pairwise-функция потерь для implicit feedback; откуда берётся негативное сэмплирование. Базовый вопрос RecSys-собеса. | **[MUST]** middle |
| **Neural Collaborative Filtering** | https://arxiv.org/abs/1708.05031 | 2017 | Переход от MF к MLP над эмбеддингами; полезно вместе с критикой (NCF vs хорошо настроенный iALS). | **[OPT]** middle |
| **Wide & Deep Learning for RecSys** | https://arxiv.org/abs/1606.07792 | 2016 | Memorization vs generalization — до сих пор основная рамка для объяснения гибридных архитектур. | **[MUST]** middle |
| **DeepFM** | https://arxiv.org/abs/1703.04247 | 2017 | Автоматические взаимодействия признаков второго порядка без ручного feature crossing. | **[MUST]** middle |
| **Deep Interest Network (DIN)** | https://arxiv.org/abs/1706.06978 | 2018 | Attention по истории пользователя относительно кандидата — ключевая идея современного ранжирования. | **[MUST]** middle |
| **SASRec** | https://arxiv.org/abs/1808.09781 | 2018 | Каузальный трансформер для next-item. De-facto бейзлайн секвенциальных рекомендаций. | **[MUST]** middle |
| **BERT4Rec** | https://arxiv.org/abs/1904.06690 | 2019 | Двунаправленный вариант с masked item prediction. | **[MUST]** middle |
| **Is BERT4Rec really better than SASRec?** | https://arxiv.org/abs/2309.07602 | 2023 | Отличный материал для главы «как не обмануться в офлайн-сравнении»: воспроизводимость, влияние лосса и бюджета обучения. | **[MUST]** middle_plus |
| **LightGCN** | https://arxiv.org/abs/2002.02126 | 2020 | Что в GCN для рекомендаций реально работает (только соседское усреднение), а что — лишнее. | **[OPT]** middle_plus |
| **PinSage / Graph CNN for Web-Scale RecSys** | https://arxiv.org/abs/1806.01973 | 2018 | Как масштабировать GNN до миллиардов узлов: random-walk сэмплирование, producer-consumer minibatch, MapReduce-инференс. | **[OPT]** middle_plus |
| **TIGER / Recommender Systems with Generative Retrieval** | https://arxiv.org/abs/2305.05065 | 2023 | Semantic IDs и генеративный retrieval вместо ANN-поиска. Самая горячая тема RecSys-собесов 2025–2026. | **[MUST]** middle_plus |
| **YSDA RecSys Course (ШАД)** | https://github.com/yandexdataschool/recsys_course | актуальный | 13 недель от постановки задачи до продакшена: метрики и ANN → реранкинг и разнообразие (MF/SLIM/EASE) → двухбашенки и контрастивное обучение → холодный старт и последовательные модели → нейроранжирование, взаимодействие признаков, многозадачность и дистилляция → системный дизайн, мониторинг, GPU-инференс, управляемая деградация → трансформеры, бандиты, разборы кейсов Яндекса. Семинары построены на разборе статей и контестах. **Самая близкая к этому хендбуку программа на русском** — полезно сверяться. | **[MUST]** middle→middle_plus |
| **Yambda (Яндекс Музыка)** | https://huggingface.co/datasets/yandex/yambda · статья: https://arxiv.org/abs/2505.22238 | 2025 | ~4,8 млрд взаимодействий, 1 млн пользователей, 9,4 млн треков; неявные и явные сигналы, точные метки времени, флаг `is_organic` (органика против рекомендованного). Крупнейший открытый датасет для рекомендаций; доступен в размерах 50M / 500M / 5B. Нужен, когда хочется мерить на данных, похожих на промышленные, а не на MovieLens. | **[MUST]** middle |
| **RecSys-Course (SB AI Lab, RePlay)** | https://github.com/sb-ai-lab/RecSys-Course | — | 17 модулей на русском: сплиты и метрики → non-personalized → ItemKNN/UserKNN → SLIM/EASE → SVD/ALS/iALS → triplet/BPR/WARP → LightFM → двухстадийные модели → нейросети → секвенциальные → бандиты → графовые → Spark/Polars → ANN → прод. **Готовый скелет главы.** | **[MUST]** middle |
| **MTS «Your First RecSys» / «Your Second RecSys» (ODS)** | https://ods.ai/tracks/mts-recsys-df2020 · https://ods.ai/tracks/recsys-course2021 | 2020 / 2021 | Русскоязычный практический вход: постановка задачи, сбор данных, фреймворки, прототип → прод. | **[MUST]** junior→middle |
| **RecTools (МТС)** | https://github.com/MobileTeleSystems/RecTools | актуальный | Библиотека с единым API для iALS/LightFM/DSSM/секвенциальных моделей. Стандарт де-факто в русскоязычном RecSys. | **[MUST]** middle |
| **Авито: поисковое ранжирование** | https://habr.com/ru/companies/avito/articles/846832/ | 2024 | Как устроен многоступенчатый ранкер на миллионах объявлений — реальный кейс для system-design-раздела. | **[MUST]** middle |
| **Авито: трансформенная персонализация** | https://habr.com/ru/companies/avito/articles/1004694/ | 2025 | Пользовательские эмбеддинги в Redis, скалярное произведение как фича в ранкере. Прямо отвечает на вопрос «как отдавать эмбеддинги в реалтайме». | **[MUST]** middle_plus |
| **Авито: нейросетевая модель интересов пользователя** | https://habr.com/ru/companies/avito/articles/974682/ | 2025 | Разнообразие и релевантность на главной; полезно для раздела про diversity/serendipity. | **[MUST]** middle_plus |
| **applied-ml (eugeneyan)** | https://github.com/eugeneyan/applied-ml | актуальный | Каталог блогов компаний по RecSys/Search/MLOps/A-B: Netflix, Spotify, Pinterest, Amazon, YouTube, TikTok, LinkedIn, DoorDash, Airbnb, Etsy, Alibaba. **Основной источник индустриальных кейсов.** | **[MUST]** middle |
| **Personalized Machine Learning (McAuley)** | https://cseweb.ucsd.edu/~jmcauley/pml/ | 2022 | Академический учебник по персонализации от автора SASRec. | **[OPT]** middle_plus |
| **Yandex: рекомендательные системы (knowledge)** | https://education.yandex.ru/knowledge/rekomendatelnye-sistemy.-mashinnoe-obuchenie | — | Короткий русскоязычный обзор. | **[OPT]** junior |

### 5. MLOps, продакшн, мониторинг (главы 07-mlops, 09-monitoring)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Hidden Technical Debt in Machine Learning Systems (Sculley et al.)** | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 2015 | Каноническая рамка: CACE, entanglement, hidden feedback loops, undeclared consumers, data dependencies, конфигурационный долг, «ML-код — малая часть системы». **Самая цитируемая статья на MLOps-собесах.** | **[MUST]** middle |
| **Rules of Machine Learning (Zinkevich, Google)** | https://developers.google.com/machine-learning/guides/rules-of-ml · https://martin.zinkevich.org/rules_of_ml/ | 2017 | 43 правила в трёх фазах. Из них на собесах реально спрашивают: начни без ML, сначала инфраструктура и метрики, следи за train/serving skew, не переусложняй фичи раньше времени. | **[MUST]** junior→middle |
| **The ML Test Score (Breck, Cai, Nielsen, Salib, Sculley)** | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 2017 | 28 конкретных тестов по 4 группам (данные, модель, инфраструктура, мониторинг). Готовый чек-лист для главы «как понять, что модель готова к проду». | **[MUST]** middle |
| **Designing Machine Learning Systems (Chip Huyen)** | https://github.com/chiphuyen/dmls-book · https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/ | 2022 | Опорная книга всего MLOps-раздела: data engineering fundamentals, feature engineering, оценка моделей, деплой, батч vs стрим, дрифт, continual learning, инфраструктура, human side. Есть русский перевод. | **[MUST]** middle |
| **MLOps Zoomcamp (DataTalksClub)** | https://github.com/DataTalksClub/mlops-zoomcamp | актуальный | Единственный бесплатный курс, где всё руками: MLflow → оркестрация → Flask/Kinesis+Lambda/batch деплой → Evidently+Prometheus+Grafana → CI/CD GitHub Actions → Terraform. | **[MUST]** middle |
| **Uber Michelangelo** | https://www.uber.com/us/en/blog/scaling-michelangelo/ · https://www.uber.com/us/en/blog/uber-science-machine-learning-platform/ | 2017 / 2019+ | Первый публично описанный end-to-end ML-платформенный стек: feature store, тренировка, деплой, мониторинг. Эталон для вопроса «спроектируй ML-платформу». | **[MUST]** middle_plus |
| **ml_system_design_doc_ru (Reliable ML)** | https://github.com/IrinaGoloshchapova/ml_system_design_doc_ru | актуальный | **Русскоязычный шаблон дизайн-дока** + чек-лист оценки (ITMO & Reliable ML). Обязателен, потому что в РФ на middle+ часто просят именно написать дизайн-док, а не «поговорить». | **[MUST]** middle |
| **MLSystemDesign (компаньон книги Manning)** | https://github.com/ML-SystemDesign/MLSystemDesign | актуальный | `basic_ml_design_doc.md` из 12 разделов + `design_doc_checklist.md` + разобранные кейсы (Retail Demand Forecasting, RAG Chat with Document Versions). | **[MUST]** middle |
| **awesome-production-machine-learning** | https://github.com/EthicalML/awesome-production-machine-learning | актуальный | Каталог инструментов: деплой, мониторинг, версионирование, масштабирование, privacy-preserving ML, интерпретируемость. Нужен, чтобы в главе не изобретать список тулов. | **[OPT]** middle |
| **Practitioner's Guide to MLOps (Google whitepaper)** | https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf | 2021 | Формальная модель зрелости MLOps (уровни 0/1/2) — язык, на котором говорят на собесах в крупных компаниях. | **[MUST]** middle |
| **MLOps by Chip Huyen (подборка)** | https://huyenchip.com/mlops/ | — | Курируемый список инструментов и статей. | **[OPT]** middle |
| **ODS: ML in Production / ML System Design** | https://ods.ai/tracks/ml-in-production-spring-23 · https://ods.ai/tracks/ml-system-design-23 | 2022–2023 | Русскоязычные треки с разбором реальных дизайн-доков. | **[MUST]** middle |
| **Made With ML** | https://madewithml.com/#mlops | актуальный | End-to-end проект от разметки до CI/CD — хорошо как «сделай сам» в конце главы. | **[OPT]** junior→middle |
| **Reliable Machine Learning (O'Reilly)** | https://www.amazon.com/Reliable-Machine-Learning-Principles-Production/dp/1098106229/ | 2022 | SRE-подход к ML: SLO для моделей, on-call, постмортемы. | **[OPT]** middle_plus |

### 6. Big Data и инфраструктура данных (глава 08-big-data)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Designing Data-Intensive Applications (Kleppmann)** | https://dataintensive.net/ | 2017 (рус. «Высоконагруженные приложения», Питер, 2018, ISBN 978-5-4461-0512-0) | **Единственная обязательная книга раздела.** Гл. 3 (storage engines, LSM vs B-tree), 4 (форматы и эволюция схем — прямо про Parquet/Avro), 6 (партиционирование), 7 (транзакции), 11 (стриминг). | **[MUST]** middle |
| **Learning Spark, 2nd ed. (Databricks)** | https://pages.databricks.com/rs/094-YMS-629/images/LearningSpark2.0.pdf | 2020 | Бесплатный PDF. DataFrame API, Catalyst, Tungsten, оконные функции, структурированный стриминг. | **[MUST]** middle |
| **Data Analysis with Python and PySpark (Manning)** | https://www.manning.com/books/data-analysis-with-python-and-pyspark | 2022 | PySpark для тех, кто пришёл из pandas. | **[OPT]** middle |
| **PySpark для аналитики (Avito, ч. 1 и 2)** | https://habr.com/ru/companies/avito/articles/732870/ · https://habr.com/ru/companies/avito/articles/740232/ | 2023 | Русскоязычная практика: партиционирование, скошенные джойны, broadcast. | **[MUST]** middle |
| **Spark для начинающих (Альфа)** | https://habr.com/ru/companies/alfa/articles/808415/ | 2024 | Разбор архитектуры Spark на русском. | **[OPT]** junior |
| **Vowpal Wabbit / обучение на гигабайтах (тема 8 ODS)** | https://habr.com/ru/companies/ods/articles/326418/ | 2017 | Hashing trick, online learning, out-of-core — до сих пор актуальные ответы на «что делать, если данные не влезают в память». | **[OPT]** middle |

### 7. A/B-тестирование и эксперименты (глава 10-ab-testing)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Kohavi, Tang, Xu — Trustworthy Online Controlled Experiments** | https://www.amazon.com/Trustworthy-Online-Controlled-Experiments-Practical/dp/1108724264 | 2020 | **Библия A/B.** OEC, guardrail-метрики, SRM (sample ratio mismatch), сетевые эффекты, ловушки подглядывания, Twyman's law. Почти любой вопрос A/B-секции — оттуда. | **[MUST]** middle |
| **CUPED — Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (Deng, Xu, Kohavi, Walker)** | KDD/WSDM 2013 | 2013 | Дисперсия падает в (1 − ρ²) раз; на Bing давало ~50% снижения дисперсии, т.е. вдвое меньше пользователей при той же мощности. Обязательный вопрос на middle+. | **[MUST]** middle→middle_plus |
| **Variance Reduction Using In-Experiment Data (Deng, KDD 2023)** | https://alexdeng.github.io/public/files/kdd2023-inexp.pdf | 2023 | Продолжение CUPED, когда предэкспериментальных данных нет (новые пользователи). | **[OPT]** middle_plus |
| **Курс матстата и A/B Ульянкина** | https://github.com/FUlyankin/matstat-AB | — | Русскоязычная база: оценки, доверительные интервалы, гипотезы, бутстрап, A/B. Осознанно не «чёрный ящик». | **[MUST]** middle |
| **Курс по статистике от Авито** | https://avito.tech/education/statistics | актуальный | Индустриальная русскоязычная подача A/B от компании, которая этим живёт. | **[MUST]** middle |
| **A/B Testing Roadmap (Balandin)** | https://github.com/YuriyBalandin/ab_testing_roadmap/blob/main/Roadmap/Roadmap.md | — | Структурированный план изучения — можно взять как каркас главы. | **[OPT]** middle |
| **Google: Overlapping Experiment Infrastructure** `[FETCH via applied-ml]` | (каталог eugeneyan/applied-ml) | 2010 | Слои экспериментов — ответ на «как запускать 100 экспериментов одновременно». | **[MUST]** middle_plus |
| **Кейсы платформ экспериментов: Netflix, Uber, Airbnb, DoorDash, Spotify** `[FETCH via applied-ml]` | https://github.com/eugeneyan/applied-ml | 2016–2021 | Разделы A/B Testing & Experimentation в каталоге. Подтверждено наличие постов Netflix «It's All A/Bout Testing», Uber (2017–2020), Airbnb (2017, 2021), DoorDash, Spotify (2020). | **[MUST]** middle_plus |
| **Practitioner's Guide to Statistical Tests (VK Team)** | https://vkteam.medium.com/practitioners-guide-to-statistical-tests-ed2d580ef04f | — | Русскоязычная команда, англоязычный текст: какой тест когда применять. | **[OPT]** middle |
| **Applied Causal Inference / Causal ML book** | https://causalml-book.org · https://alexdeng.github.io/causal/index.html | 2024 | Когда A/B невозможен: DiD, synthetic control, switchback. | **[OPT]** middle_plus |

### 8. ML System Design и собеседования (главы 11-system-design, 14-career)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **ML System Design Interview (Aminian & Xu)** | https://www.amazon.com/Machine-Learning-System-Design-Interview/dp/1736049127 | 2023 | Пошаговый фреймворк + разобранные задачи (видео-рекомендации, поиск по картинке, лента, реклама, детекция вредного контента). Де-факто стандарт подготовки. | **[MUST]** middle |
| **Generative AI System Design Interview (Aminian & Sheng)** | https://www.amazon.com/Generative-AI-System-Design-Interview/dp/1736049143 | 2024-11-18 | 7-шаговый фреймворк + 10 задач по генеративным системам. Дополняет предыдущую, а не заменяет. | **[MUST]** middle_plus |
| **chiphuyen/machine-learning-systems-design** | https://github.com/chiphuyen/machine-learning-systems-design | 2019 | 27 открытых вопросов по ML system design + 4-частная рамка (project setup / data pipeline / modeling / serving). | **[MUST]** middle |
| **Case studies (Chip Huyen)** | https://raw.githubusercontent.com/chiphuyen/machine-learning-systems-design/master/content/case-studies.md | 2019 | 12 кейсов с атрибуцией: Airbnb (оценка стоимости жилья; ранжирование Experiences), Netflix (качество стриминга; DL для рекомендаций; надёжность ML-алгоритмов), Booking.com («150 Successful ML Models: 6 Lessons Learned»), Lyft (from shallow to deep learning in fraud), Uber (Big Data Platform 100+ PB; Scaling ML with Michelangelo), Chicisimo, Instacart, Dropbox. | **[MUST]** middle |
| **Introduction to ML Interviews Book (Chip Huyen)** | https://huyenchip.com/ml-interviews-book/ | 2021 | Бесплатно онлайн. Как устроен процесс найма + большой банк вопросов. | **[MUST]** junior→middle |
| **alirezadir/Machine-Learning-Interviews** | https://github.com/alirezadir/Machine-Learning-Interviews | обновл. 2026 | 6 глав: general coding, ML coding, ML breadth, ML system design, **agentic AI systems**, behavioral. Автор — по офферам Meta/Google/Amazon/Apple/Roku. Обновление 2026 под LLM/мультимодальность и агентов. | **[MUST]** middle |
| **khangich/machine-learning-interview** | https://github.com/khangich/machine-learning-interview | актуальный | «Minimum Viable Study Plan»: LeetCode, SQL (джойны, оконные), programming, статистика/вероятности, Big Data (Spark, Cassandra), ML fundamentals, A/B, DL, ML system design. Компании: Google, Facebook, Amazon, Apple, Microsoft, Snapchat, LinkedIn, Coupang, StitchFix, Booking, NVIDIA, Intel. | **[MUST]** middle |
| **Extremesarova/ds_resources** | https://github.com/Extremesarova/ds_resources | актуальный | **Самый полный русскоязычно-ориентированный каталог** ресурсов для подготовки. Отдельно ценны разделы Company-Specific Resources и Home Assignments. | **[MUST]** все грейды |
| **Tinkoff/career — секция ML** | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/platform-ml.md | актуальный | **Официальный список литературы российской компании.** Прямо называет: ESL (PDF Стэнфорда), PRML, Goodfellow DL, Manning «Introduction to Information Retrieval», Practical_DL / Practical_RL / nlp_course ШАДа, Catalyst DL course, книгу Николенко–Кадурина–Архангельской «Глубокое обучение», банки вопросов (kojino/120, iamtodor, alexeygrigorev, dingran/quant-notes). | **[MUST]** все грейды |
| **Tinkoff/career — структура интервью** | https://github.com/Tinkoff/career/blob/main/interview/README.md | актуальный | 2–4 секции по 1–1.5 ч: programming, ML platform, ML system design. | **[MUST]** все грейды |
| **alexeygrigorev/data-science-interviews** | https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/theory.md | актуальный | Банк теории с **явной разметкой сложности**: 👶 = junior, ⭐ = middle, 🚀 = senior. Эта разметка — готовая рубрика грейдов для хендбука. | **[MUST]** все грейды |
| **Pe4enIks/ML-Interview** | https://github.com/Pe4enIks/ML-Interview | актуальный | Русскоязычный банк вопросов MLE с уклоном в CV/мультимодалку. | **[MUST]** middle |
| **slgero/testovoe** | https://github.com/slgero/testovoe | актуальный | Реальные тестовые задания: Uber, Gett, S7, МТС, Сбер (Деловая Среда), СКБ Контур, Альфабанк KZ, БКС, Wargaming, PWC, BCG Gamma, Accenture, AUTO1, Diginetica, OLX-Hermes, Zyfra и др. | **[MUST]** middle |
| **The System Design Primer** | https://github.com/donnemartin/system-design-primer | актуальный | Общий (не ML) system design: кэши, шардирование, CAP, очереди. Нужен как фундамент под ML SD. | **[MUST]** middle |
| **ML Systems Design Interview Guide (Patrick Halina)** | http://patrickhalina.com/posts/ml-systems-design-interview-guide/ | — | Короткий, но очень плотный фреймворк ответа. | **[MUST]** middle |
| **ML System Design: 500 case studies (Evidently AI)** | https://www.evidentlyai.com/ml-system-design | актуальный | База индустриальных кейсов с фильтрами по индустрии и задаче. | **[MUST]** middle |
| **Stanford CS329S: ML Systems Design** | https://stanford-cs329s.github.io/syllabus.html | 2022 | Курс, из которого выросла книга Chip Huyen. | **[OPT]** middle |
| **eugeneyan.com + applyingml.com** | https://eugeneyan.com/ · https://applyingml.com/ | актуальный | Эссе про прикладной ML, дизайн-доки, оценку LLM. Один из немногих блогов, который стоит читать подряд. | **[MUST]** middle |

### 9. Программирование, алгоритмы, SQL (глава 12-coding)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Хендбук по алгоритмам (Яндекс)** | https://academy.yandex.ru/handbook/algorithms | актуальный | Русскоязычный канон по алгоритмам и структурам данных. | **[MUST]** junior |
| **Хендбук по Python (Яндекс)** | https://education.yandex.ru/handbook/python | актуальный | База Python на русском. | **[MUST]** junior |
| **NeetCode Roadmap** | https://neetcode.io/roadmap | актуальный | Наиболее эффективный порядок прохождения LeetCode по паттернам. | **[MUST]** junior→middle |
| **LeetCode Patterns (Sean Prashad)** | https://seanprashad.com/leetcode-patterns/ | актуальный | Группировка задач по приёмам. | **[MUST]** junior |
| **What the f*ck Python** | https://github.com/satwikkansal/wtfpython | актуальный | Источник каверзных вопросов про мутабельность, кэш малых int, замыкания в циклах — ровно то, что спрашивают в Python-секции. | **[OPT]** middle |
| **Comprehensive Python Cheatsheet** | https://github.com/gto76/python-cheatsheet | актуальный | Справочник на одну страницу. | **[OPT]** junior |
| **DataLemur / sql-practice / PostgreSQL Exercises** | https://datalemur.com/questions?category=SQL · https://www.sql-practice.com/ · https://pgexercises.com/ | актуальный | Практика SQL до уровня оконных функций и self-join — на MLE-собесах в РФ SQL спрашивают почти всегда. | **[MUST]** junior→middle |
| **Algorithmica (рус.)** | https://ru.algorithmica.org/ | актуальный | Русскоязычный учебник по алгоритмам. | **[OPT]** junior |
| **CodeRun (Яндекс)** | https://coderun.yandex.ru | актуальный | Задачи в формате, максимально близком к реальным собесам Яндекса. | **[MUST]** junior→middle |

---

---

## Смежное

- [Сводный список источников по главам](reading-list.md) — что читать после каждой конкретной главы.
- [Оглавление хендбука](../docs/index.md)

---

🏠 [К README репозитория](../README.md)
