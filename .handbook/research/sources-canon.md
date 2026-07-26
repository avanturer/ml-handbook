# Источники (канон литературы для MLE-хендбука) — research dump

> Дата сбора: 2026-07-26.
> **Важное методологическое замечание.** В этой сессии egress-политика прокси пропускала на `WebFetch`
> только `github.com` / `raw.githubusercontent.com`. Домены `arxiv.org`, `habr.com`, `education.yandex.ru`,
> `hastie.su.domains`, `deeplearningbook.org`, `openreview.net`, `huggingface.co`, `wikipedia.org`
> отдавали 403 от прокси (organization egress policy, см. `/root/.ccr/README.md`, раздел «403 / 407 from the proxy»).
> Поэтому верификация шла тремя каналами, и **у каждого источника ниже проставлен уровень верификации**:
>
> - `[FETCH]` — страница реально скачана и прочитана целиком (26 URL, все GitHub);
> - `[ARXIV]` — карточка статьи (заголовок + дата + организация + абстракт) получена через alphaXiv MCP (25 статей);
> - `[SEARCH]` — URL + заголовок + фрагмент содержания подтверждены поисковой выдачей (WebSearch), полный текст не открывался;
> - `[REF]` — источник упомянут внутри уже скачанного `[FETCH]`-документа (то есть его рекомендует верифицированный список), но сама страница не открывалась.
>
> Ничего, что не попало хотя бы в одну из этих четырёх категорий, в файл не включено.

---

## Источники, которые реально просмотрены

### A. Полностью скачанные страницы (`[FETCH]`, 26 URL)

| # | URL | Что это и что оттуда взято |
|---|-----|----------------------------|
| 1 | https://github.com/Yorko/mlcourse.ai | Репозиторий открытого курса ODS mlcourse.ai. Подтверждены все 10 тем и прямые ссылки на соответствующие статьи на Habr. |
| 2 | https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/README.md | README того же курса: таблица из 10 демо-домашек с ссылками на nbviewer и Kaggle. |
| 3 | https://github.com/Pe4enIks/ML-Interview | Русскоязычный банк вопросов с собеседований на MLE (уклон в CV/мультимодалку). ~70 вопросов дословно. |
| 4 | https://github.com/Extremesarova/ds_resources | **Ключевая находка.** Гигантский аннотированный каталог DS/ML-ресурсов (RU+EN): книги, курсы, статьи, блоги, A/B, MLOps, system design, RecSys, Big Data. Основной каркас канона ниже собран отсюда. |
| 5 | https://github.com/alirezadir/Machine-Learning-Interviews | Гайд по MLE/AS-интервью в FAANG. Структура из 6 глав, обновление 2026 под LLM/GenAI и агентные системы. |
| 6 | https://github.com/khangich/machine-learning-interview | «Minimum Viable Study Plan for ML Interviews». 9 блоков подготовки + короткий список источников. |
| 7 | https://github.com/eugeneyan/applied-ml | Каталог инженерных блогов и статей компаний (RecSys, Search&Ranking, MLOps, A/B). Подтверждены разделы и перечни компаний. |
| 8 | https://github.com/probml/pml-book | Серия Кевина Мёрфи: book0 (2012), book1 (2022), book2 (2023) с ссылками на официальные страницы. |
| 9 | https://github.com/ML-SystemDesign/MLSystemDesign | Компаньон к книге Manning «Machine Learning System Design»: шаблон `basic_ml_design_doc.md` (12 разделов), `design_doc_checklist.md`, кейсы (Retail Demand Forecasting, RAG Chat with Document Versions). |
| 10 | https://github.com/IrinaGoloshchapova/ml_system_design_doc_ru | Русскоязычный шаблон ML System Design Doc от сообщества Reliable ML + чек-лист оценки (ITMO & Reliable ML). |
| 11 | https://github.com/chiphuyen/machine-learning-systems-design | Буклет Chip Huyen 2019: 4 части (project setup / data pipeline / modeling / serving) + 27 открытых вопросов по ML system design. |
| 12 | https://raw.githubusercontent.com/chiphuyen/machine-learning-systems-design/master/content/case-studies.md | 12 индустриальных кейсов с атрибуцией компаний: Airbnb ×2, Netflix ×3, Booking.com, Lyft, Uber ×2, Chicisimo, Instacart, Dropbox. |
| 13 | https://github.com/chiphuyen/dmls-book | Репозиторий книги «Designing Machine Learning Systems» (O'Reilly, 2022): саммари глав, список MLOps-инструментов, переводы (в т.ч. русский). |
| 14 | https://github.com/Dyakonov/MLDM | Потоковый курс А. Дьяконова «Машинное обучение и анализ данных», ВМК МГУ. Подтверждён список из 10 лекций весны 2022. |
| 15 | https://github.com/mryab/efficient-dl-systems | Курс «Efficient Deep Learning Systems» (ФКН ВШЭ + ШАД), итерация 2026. 10 недель: CUDA → профилирование → data-parallel → sharded → инференс. |
| 16 | https://github.com/stas00/ml-engineering | Открытая книга Stas Bekman по инженерии обучения LLM/VLM (опыт BLOOM-176B, IDEFICS-80B): железо, оркестрация, отладка, инференс. |
| 17 | https://github.com/slgero/testovoe | Коллекция реальных тестовых заданий на DS-позиции по компаниям: Uber, Gett, S7, МТС, Сбер (Деловая Среда), СКБ Контур, Альфабанк KZ, БКС, Wargaming, PWC, BCG Gamma и др. |
| 18 | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/platform-ml.md | **Официальный список литературы для подготовки к ML-секции Тинькофф/Т-Банка.** Прямо называет ESL, PRML, Goodfellow DL, Manning IR, курсы ШАДа, книгу Николенко. |
| 19 | https://github.com/Tinkoff/career/blob/main/interview/README.md | Описание структуры интервью Т-Банка: 2–4 секции, 1–1.5 ч каждая, включая ML Platform и ML System Design. |
| 20 | https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/theory.md | Банк теоретических вопросов с разметкой сложности (👶 junior / ⭐ middle / 🚀 senior). Считано 60 вопросов дословно. |
| 21 | https://github.com/EthicalML/awesome-production-machine-learning | Курируемый каталог open-source инструментов для деплоя, мониторинга, версионирования и масштабирования ML. |
| 22 | https://github.com/FUlyankin/matstat-AB | Русский курс по матстату и A/B-тестам (Ф. Ульянкин), 16 недель / 3 курса: от ЗБЧ и ЦПТ до бутстрапа, A/B и байесовских методов. |
| 23 | https://github.com/sb-ai-lab/RecSys-Course | Курс по рекомендательным системам от SB AI Lab на базе библиотеки RePlay. 17 модулей: ItemKNN/UserKNN → SLIM/EASE → ALS/iALS → BPR/WARP → LightFM → двухстадийные → нейросети → секвенциальные → бандиты → графовые → Spark/ANN/прод. |
| 24 | https://github.com/yandexdataschool/Practical_DL | Курс YSDA + ВШЭ + Сколтех по DL, поток осени 2025: 14 недель, от backprop до диффузии, инференса и аудио. |
| 25 | https://github.com/DataTalksClub/mlops-zoomcamp | Бесплатный 9-недельный MLOps-курс: MLflow, оркестрация, деплой (Flask / Kinesis+Lambda / batch), мониторинг (Evidently, Prometheus, Grafana), CI/CD, Terraform. |
| 26 | https://github.com/yandexdataschool/nlp_course | Курс NLP ШАДа, поток 2025: 14 недель, от word embeddings до LLM, prompting, RAG, агентов, интерпретируемости и мультимодальности. |

### B. Статьи, верифицированные через alphaXiv (`[ARXIV]`, 25 карточек)

Для каждой получены заголовок, дата первой публикации, организация-автор и абстракт.

| arXiv ID | Заголовок | Дата | Организация |
|----------|-----------|------|-------------|
| 1706.03762 | Attention Is All You Need | 2017-06-13 | Google Brain / Google Research / U. Toronto |
| 1810.04805 | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | 2018-10-11 | Google AI Language |
| 2005.14165 | Language Models are Few-Shot Learners (GPT-3) | 2020-05-28 | OpenAI, JHU |
| 2203.02155 | Training language models to follow instructions with human feedback (InstructGPT) | 2022-03-04 | OpenAI |
| 2203.15556 | Training Compute-Optimal Large Language Models (Chinchilla) | 2022-03-29 | Google DeepMind |
| 2106.09685 | LoRA: Low-Rank Adaptation of Large Language Models | 2021-06-18 | Microsoft, CMU |
| 2205.14135 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | 2022-05-28 | Stanford, SUNY Buffalo |
| 2309.06180 | Efficient Memory Management for LLM Serving with PagedAttention (vLLM) | 2023-09-12 | UC Berkeley, Stanford, UCSD |
| 2305.18290 | Direct Preference Optimization: Your Language Model is Secretly a Reward Model | 2023-05-30 | Stanford, CZ Biohub |
| 2302.13971 | LLaMA: Open and Efficient Foundation Language Models | 2023-02-28 | Meta |
| 2404.10981 | A Survey on Retrieval-Augmented Text Generation for Large Language Models | 2024-08-23 | York University |
| 1502.03167 | Batch Normalization: Accelerating Deep Network Training… | 2015-02-13 | Google |
| 1512.03385 | Deep Residual Learning for Image Recognition (ResNet) | 2015-12-10 | Microsoft |
| 1603.05027 | Identity Mappings in Deep Residual Networks (ResNet v2) | 2016-03-16 | Microsoft |
| 1706.09516 | CatBoost: unbiased boosting with categorical features | 2017-06-28 | Yandex |
| 2305.17094 | Benchmarking state-of-the-art gradient boosting algorithms for classification | 2023-05-26 | Wrocław Univ. of S&T |
| 1205.2618 | BPR: Bayesian Personalized Ranking from Implicit Feedback | 2012-05-09 | — |
| 1808.09781 | Self-Attentive Sequential Recommendation (SASRec) | 2018-08-20 | — |
| 1904.06690 | BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer | 2019-08-21 | — |
| 2309.07602 | Turning Dross Into Gold Loss: is BERT4Rec really better than SASRec? | 2023-09-14 | — |
| 2002.02126 | LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation | 2020-05-15 | — |
| 1806.01973 | Graph Convolutional Neural Networks for Web-Scale Recommender Systems (PinSage) | 2018-06-06 | Pinterest / Stanford |
| 1606.07792 | Wide & Deep Learning for Recommender Systems | 2016-06-24 | Google |
| 1703.04247 | DeepFM: A Factorization-Machine based Neural Network for CTR Prediction | 2017-03-13 | HIT, Huawei |
| 1706.06978 | Deep Interest Network for Click-Through Rate Prediction (DIN) | 2018-09-13 | Alibaba |
| 2305.05065 | Recommender Systems with Generative Retrieval (TIGER, semantic IDs) | 2023-05-08 | Google DeepMind / Google / UW–Madison |
| 1708.05031 | Neural Collaborative Filtering (NCF) | 2017-08-16 | NUS, TAMU, Columbia, SDU |

*(в таблице 27 строк — 25 «канонических» + 2 бонусных: 2305.17094 и 2309.07602)*

### C. URL, подтверждённые поисковой выдачей (`[SEARCH]`)

Ниже — только те, по которым поисковик вернул и заголовок, и содержательный фрагмент.

- https://education.yandex.ru/handbook/ml — «Учебник по машинному обучению» ШАДа; бесплатный интерактивный, требует линала, матана и теорвера.
- https://education.yandex.ru/handbook/ml/article/about — страница «Об этой книге».
- https://education.yandex.ru/handbook/math — «Хендбук по математике для аналитики и машинного обучения».
- https://education.yandex.ru/handbook/python — хендбук по Python от Яндекса.
- https://academy.yandex.ru/handbook/algorithms — хендбук по алгоритмам.
- https://habr.com/ru/companies/yandex/news/590001/ — «Как мы делаем новый учебник ШАДа по машинному обучению».
- https://yandexdataschool.gitlab.io/ml-handbook/ — старая GitLab-версия учебника ШАДа (содержание).
- https://gitlab.com/yandexdataschool/ml-handbook — исходники учебника.
- https://hastie.su.domains/ElemStatLearn/ — официальная страница ESL (Hastie/Tibshirani/Friedman), 2nd ed., бесплатный PDF.
- https://web.stanford.edu/~hastie/Papers/ESLII.pdf — прямой PDF ESL (именно эту ссылку даёт Т-Банк).
- https://www.statlearning.com/ — ISLR/ISLP; Python-издание бесплатно для чтения.
- https://probml.github.io/pml-book/book1.html — Murphy, «Probabilistic ML: An Introduction» (2022).
- https://probml.github.io/pml-book/book2.html — Murphy, «Probabilistic ML: Advanced Topics» (2023).
- https://probml.github.io/pml-book/toc1.pdf — оглавление book1.
- https://www.deeplearningbook.org/ — Goodfellow/Bengio/Courville, «Deep Learning» (MIT Press, 2016).
- https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/ — официальная страница Bishop PRML с бесплатным PDF.
- https://www.bishopbook.com — Bishop & Bishop, «Deep Learning: Foundations and Concepts» (2024).
- https://mlcourse.ai/book/index.html — self-paced англ. версия открытого курса ODS.
- https://ods.ai/tracks/open-ml-course — русская версия открытого курса ODS.
- https://habr.com/ru/companies/ods/articles/322626/ — Тема 1 (Pandas & EDA).
- https://habr.com/ru/companies/ods/articles/323210/ — Тема 2 (визуализация).
- https://habr.com/ru/companies/ods/articles/326418/ — Тема 8 (Vowpal Wabbit).
- https://habr.com/ru/company/ods/blog/438940/ — «Открытый курс "Deep Learning на пальцах"».
- http://www.machinelearning.ru/wiki/index.php?title=Машинное_обучение_(курс_лекций,_К.В.Воронцов) — курс Воронцова.
- http://www.machinelearning.ru/wiki/index.php?title=Введение_в_машинное_обучение_(курс_лекций,_К.В.Воронцов) — вводный курс Воронцова.
- https://dyakonov.org/ag/ — блог А. Дьяконова «Анализ малых данных».
- https://lena-voita.github.io/nlp_course.html — «NLP Course | For You» Лены Войты (расширение курса ШАДа).
- https://dls.samcs.ru/ — Deep Learning School ФПМИ МФТИ (бесплатно, Stepik).
- https://stepik.org/course/230363/promo, https://stepik.org/course/230362/promo — потоки DLS весны 2025.
- https://developers.google.com/machine-learning/guides/rules-of-ml — Zinkevich, «Rules of Machine Learning» (43 правила).
- https://martin.zinkevich.org/rules_of_ml/ — авторская страница того же документа.
- https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems — Sculley et al., NIPS 2015.
- https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ — Breck et al., 2017, 28 тестов.
- https://alexdeng.github.io/public/files/kdd2023-inexp.pdf — Deng, «Variance Reduction Using In-Experiment Data» (KDD 2023).
- https://www.amazon.com/Trustworthy-Online-Controlled-Experiments-Practical/dp/1108724264 — Kohavi/Tang/Xu, Cambridge UP, 2020.
- https://www.uber.com/us/en/blog/scaling-michelangelo/ — «Scaling Machine Learning at Uber with Michelangelo».
- https://www.uber.com/us/en/blog/uber-science-machine-learning-platform/ — «Powering Machine Learning at Uber».
- https://huyenchip.com/ — сайт Chip Huyen.
- https://huyenchip.com/ml-interviews-book/ — «Introduction to ML Interviews» (бесплатно онлайн).
- https://huyenchip.com/mlops/ — подборка MLOps-материалов.
- https://www.oreilly.com/library/view/ai-engineering/9781098166298/ — Chip Huyen, «AI Engineering» (2025).
- https://github.com/chiphuyen/aie-book — репозиторий-компаньон «AI Engineering».
- https://www.amazon.com/Machine-Learning-System-Design-Interview/dp/1736049127 — Aminian & Xu, «ML System Design Interview» (ByteByteGo, 2023).
- https://www.amazon.com/Generative-AI-System-Design-Interview/dp/1736049143 — Aminian & Sheng, «Generative AI System Design Interview» (2024-11-18).
- https://dataintensive.net/ — Kleppmann, DDIA (O'Reilly, 2017); рус. «Высоконагруженные приложения», Питер, 2018, ISBN 978-5-4461-0512-0.
- https://www.tbank.ru/career/it/interview/ml/ — официальная страница «Как проходит интервью ML-инженеров» Т-Банка.
- https://ods.ai/tracks/mts-recsys-df2020 — «MTS. Your first RecSys» (Даниил Потапов, MTS Big Data).
- https://ods.ai/tracks/recsys-course2021 — «Your Second RecSys».
- https://ods.ai/tracks/ml-system-design-22 и https://ods.ai/tracks/ml-system-design-23 — треки ML System Design ODS.
- https://ods.ai/tracks/ml-in-production-spring-22, https://ods.ai/tracks/ml-in-production-spring-23 — ML in Production.
- https://github.com/MobileTeleSystems/RecTools — библиотека RecTools от МТС.
- https://arxiv.org/abs/1603.02754 — XGBoost: A Scalable Tree Boosting System.
- https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree — LightGBM, NIPS 2017, Ke et al.
- https://karpathy.ai/zero-to-hero.html и https://github.com/karpathy/nn-zero-to-hero — «Neural Networks: Zero to Hero».
- https://jalammar.github.io/illustrated-transformer/ — «The Illustrated Transformer».
- https://lilianweng.github.io/ — блог Lilian Weng.
- https://habr.com/ru/companies/avito/articles/846832/ — «Как работает поисковое ранжирование для миллионов объявлений Авито».
- https://habr.com/ru/companies/avito/articles/1004694/ — «Как мы улучшили рекомендации Авито с помощью трансформенной персонализации».
- https://habr.com/ru/companies/avito/articles/974682/ — «Нейросетевая модель интересов пользователя» (главная Авито).
- https://habr.com/ru/companies/avito/articles/948626/ — автогенерация описаний, CLIP + LLM.
- https://habr.com/ru/companies/X5Tech/articles/845398/ — обновлённый бенчмарк ruMTEB и лидерборд.
- https://habr.com/ru/companies/sberdevices/articles/831150/ — «ruMTEB: новый бенчмарк для русскоязычных эмбеддеров».
- https://habr.com/ru/companies/sberdevices/articles/909924/ — «Знакомьтесь, FRIDA. Открытая эмбеддинг-модель для русского языка».
- https://habr.com/ru/companies/ozontech/articles/750196/ и .../768734/ — митапы Ozon Tech по поиску/рекомендациям/рекламе и ML-инфраструктуре.
- https://habr.com/ru/articles/667282/ — «Как я готовился к собеседованию на позицию Senior ML Engineer».
- https://habr.com/ru/articles/704128/ — «Как устроен процесс найма и собеседований на позицию Machine Learning Engineer».
- https://habr.com/ru/companies/skillfactory/articles/551004/ — «Собеседование на позицию Data Scientist: 20 типичных вопросов».
- https://ai.itmo.ru/blog/classic-ml-sobesedovanie-ml-engineer — «Classic ML на собеседовании: что нужно знать ML Engineer и Data Scientist».
- https://kariernik.ru/blog/sobesedovanie-ml-engineer-avito — разбор собеседования MLE в Авито.
- https://avito.tech/education/statistics — курс по статистике от Авито.
- https://karpov.courses/ml-start и https://karpov.courses/ml-start/demo — Start ML и его бесплатная демоверсия.

### D. Источники, рекомендованные внутри верифицированных списков (`[REF]`)

Полный «сырой» перечень из `Extremesarova/ds_resources` и `Tinkoff/career` вынесен в разделы канона ниже —
чтобы не дублировать, здесь только отмечу: этот каталог содержит **несколько сотен** ссылок,
сгруппированных по 20+ темам (Interview Prep, Algorithms, Python, SQL, ML, MLOps, DL, NLP/LLM, CV, GNN, RL,
RecSys, Time Series, Big Data, System Design, ML System Design, Math, Causal Inference, A/B Testing).
Ниже отобрано то, что имеет статус «канона», а не «ещё одной ссылки».

---

## Канон источников по разделам хендбука

Легенда: **[MUST]** — обязательно к прочтению для соответствующего грейда; **[OPT]** — опционально/по мере надобности.
Грейд означает: на каком уровне этот источник начинает быть нужен.

### 0. Математика и статистика (глава 01-math)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Хендбук по математике для аналитики и ML (Яндекс)** `[SEARCH]` | https://education.yandex.ru/handbook/math | актуальный | Быстрое закрытие дыр по линалу/матану/теорверу на русском. Для junior — основной вход, для middle — справочник. | **[MUST]** junior |
| **Mathematics for Machine Learning (Deisenroth, Faisal, Ong)** `[REF]` | https://mml-book.github.io | 2020 | Единственная книга, где линал+матан+вероятности изложены *через* задачи ML (PCA, GMM, SVM выведены с нуля). Брать главы 2–5 и 10–12. | **[MUST]** junior→middle |
| **Курс матстата и A/B Ф. Ульянкина** `[FETCH]` | https://github.com/FUlyankin/matstat-AB | — | 16 недель на русском: ЗБЧ/ЦПТ → оценки → доверительные интервалы → проверка гипотез → непараметрический бутстрап → A/B. Единственный русский материал, где бутстрап объяснён до уровня «могу вывести на собесе». | **[MUST]** middle |
| **Stanford CS109 + книга «Probability for Computer Scientists»** `[REF]` | https://chrispiech.github.io/probabilityForComputerScientists/en/index.html | актуальный | Вероятностная база в формате «для программистов»: без меры, но с корректными доказательствами. | **[OPT]** junior |
| **Boyd & Vandenberghe, Convex Optimization** `[REF]` | https://web.stanford.edu/~boyd/cvxbook/ | 2004 | Из всей книги для MLE нужны гл. 2–3 (выпуклые множества и функции), 5 (двойственность — чтобы понимать SVM) и 9–10 (методы спуска). Читать целиком не нужно и не надо. | **[OPT]** middle_plus |
| **Seeing Theory (Brown)** `[REF]` | https://seeing-theory.brown.edu/index.html | — | Интерактивные визуализации ЦПТ, доверительных интервалов, байесовского вывода. Хорошо как «первый контакт» и как источник картинок для главы. | **[OPT]** junior |
| **Causal Inference: What If (Hernán & Robins)** `[REF]` | https://miguelhernan.org/whatifbook | 2020 | Нужна, когда в A/B-главе доходишь до confounding, switchback и quasi-experiments. | **[OPT]** middle_plus |

### 1. Классический ML (глава 02-classic-ml)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **ESL — The Elements of Statistical Learning** `[SEARCH]` | https://hastie.su.domains/ElemStatLearn/ · PDF: https://web.stanford.edu/~hastie/Papers/ESLII.pdf | 2009 (2nd ed., 12-й тираж 2017) | **Опорный текст всей главы.** Гл. 3 (линейные методы + регуляризация), 7 (bias-variance, AIC/BIC, кросс-валидация), 9 (деревья), 10 (бустинг), 15 (Random Forest). Именно эту книгу Т-Банк даёт кандидатам как литературу к ML-секции. | **[MUST]** middle |
| **ISLR / ISLP — An Introduction to Statistical Learning** `[SEARCH]` | https://www.statlearning.com/ | 2013 / 2023 (Python ed.) | «ESL для людей»: те же темы без матрично-статистического аппарата. Для junior — читать вместо ESL, для middle — читать *до* ESL, чтобы построить интуицию. | **[MUST]** junior |
| **Учебник по ML ШАДа** `[SEARCH]` | https://education.yandex.ru/handbook/ml | 2021→наст. вр. | **Главный русскоязычный канон.** Прямо позиционируется как «продвинутый учебник без упрощений, от базовых алгоритмов до тем из свежих статей». На собесах в РФ вопросы часто формулируются его языком. | **[MUST]** junior→middle_plus |
| **Открытый курс ODS / mlcourse.ai** `[FETCH]` | https://github.com/Yorko/mlcourse.ai · https://ods.ai/tracks/open-ml-course | 2017→наст. вр. | 10 тем с полными статьями на Habr: EDA/Pandas → визуализация → деревья и kNN → линейные модели → бэггинг и RF → feature engineering → PCA/кластеризация → Vowpal Wabbit → временные ряды → градиентный бустинг. Лучший бесплатный русский вход в практику. | **[MUST]** junior |
| **Курс лекций К. В. Воронцова** `[SEARCH]` | http://www.machinelearning.ru/wiki/index.php?title=Машинное_обучение_(курс_лекций,_К.В.Воронцов) | — | Академический русский канон: формальные постановки, теория обобщающей способности, метрические и линейные методы. Брать конспекты как источник строгих определений. | **[OPT]** middle |
| **Курс А. Дьяконова «ML and Data Mining» (ВМК МГУ)** `[FETCH]` | https://github.com/Dyakonov/MLDM | 2022 | 10 лекций: термины → постановки → математика в ML → метрические алгоритмы → линейная и логистическая регрессия → суррогатные функции и SVM → деревья (сложность, смещение, разброс) → ансамбли → разбор реальной задачи. Очень удачная последовательность для структуры главы. | **[MUST]** junior→middle |
| **Блог Дьяконова «Анализ малых данных»** `[SEARCH]` | https://dyakonov.org/ag/ | — | Разборы тонкостей (ROC-AUC, метрики, утечки), которые больше нигде на русском не сформулированы так же аккуратно. | **[OPT]** middle |
| **Bishop, Pattern Recognition and Machine Learning** `[SEARCH]` | https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/ | 2006 | Байесовский взгляд. Реально нужны гл. 1–4 (вероятностная постановка, линейные модели), 9 (EM/GMM). Тоже в списке литературы Т-Банка. | **[OPT]** middle_plus |
| **Murphy, Probabilistic ML: An Introduction / Advanced Topics** `[FETCH]` | https://probml.github.io/pml-book/ | 2022 / 2023 | Самый современный «большой учебник». Использовать как энциклопедию-справочник, а не как книгу для линейного чтения. Код на JAX/PyTorch/sklearn. | **[OPT]** middle_plus |
| **XGBoost: A Scalable Tree Boosting System** `[SEARCH]` | https://arxiv.org/abs/1603.02754 | 2016 | Откуда берётся второй порядок в бустинге, регуляризация в целевой функции, sparsity-aware split finding, weighted quantile sketch. Классический вопрос: «почему XGBoost использует гессиан». | **[MUST]** middle |
| **LightGBM: A Highly Efficient GBDT** `[SEARCH]` | https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree | 2017 | GOSS и EFB — два конкретных ответа на вопрос «чем LightGBM быстрее XGBoost». Плюс leaf-wise рост дерева. | **[MUST]** middle |
| **CatBoost: unbiased boosting with categorical features** `[ARXIV]` | https://arxiv.org/abs/1706.09516 | 2017 | Ordered boosting и ordered target statistics — единственный корректный ответ на «что такое target leakage при кодировании категорий и как CatBoost с ним борется». Особенно важно на собесах в РФ. | **[MUST]** middle |
| **Interpretable Machine Learning (Molnar)** `[REF]` | https://christophm.github.io/interpretable-ml-book/ | — | Permutation importance, PDP/ICE, LIME, SHAP — с честным описанием, где каждый метод врёт. | **[OPT]** middle |
| **MLU-Explain (Amazon)** `[REF]` | https://mlu-explain.github.io/ | — | Интерактивные объяснения bias-variance, ROC/AUC, деревьев. Источник визуальных метафор для хендбука. | **[OPT]** junior |
| **StatQuest (Josh Starmer)** `[REF]` | https://www.youtube.com/@statquest/videos | — | Когда нужно «объяснить как на собесе за 3 минуты» — эталон подачи. | **[OPT]** junior |

### 2. Deep Learning (глава 03-deep-learning)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Goodfellow, Bengio, Courville — Deep Learning** `[SEARCH]` | https://www.deeplearningbook.org/ | 2016 | Ч. II (гл. 6–9: MLP, регуляризация, оптимизация, CNN) — до сих пор лучший систематический текст. Ч. III устарела. В списке литературы Т-Банка. | **[MUST]** middle |
| **Dive into Deep Learning (d2l.ai)** `[REF]` | https://d2l.ai/index.html | актуальный | Единственная книга, где каждая формула сразу сопровождается исполняемым кодом на нескольких фреймворках. Для практики. | **[MUST]** junior→middle |
| **Understanding Deep Learning (Prince)** `[REF]` | https://udlbook.github.io/udlbook/ | 2023 | Современная замена Goodfellow: трансформеры, диффузия, GNN изложены с нуля и с отличными иллюстрациями. | **[MUST]** middle |
| **Bishop & Bishop — Deep Learning: Foundations and Concepts** `[SEARCH]` | https://www.bishopbook.com | 2024 | Байесовский и вероятностный взгляд на DL. | **[OPT]** middle_plus |
| **Karpathy, Neural Networks: Zero to Hero** `[SEARCH]` | https://karpathy.ai/zero-to-hero.html · https://github.com/karpathy/nn-zero-to-hero | 2022–2023 | micrograd → makemore → GPT с нуля. **Обязательно** тем, кто не может уверенно вывести backprop на бумаге — а это ловят почти везде. | **[MUST]** junior→middle |
| **Practical DL (ШАД + ВШЭ + Сколтех)** `[FETCH]` | https://github.com/yandexdataschool/Practical_DL | осень 2025 | 14 недель: backprop и оптимизация → dropout/нормализации → CNN → fine-tuning → интерпретируемость → NLP → LM → трансформеры → LLM → генеративные → диффузия → инференс → RL → аудио. Хороший скелет для оглавления DL-раздела. | **[MUST]** middle |
| **Deep Learning School ФПМИ МФТИ** `[SEARCH]` | https://dls.samcs.ru/ · https://stepik.org/course/230362/promo | 2025 | Бесплатный русскоязычный вход в DL (2 семестра по 12–13 недель). Для junior и для тех, кто переучивается из аналитики. | **[MUST]** junior |
| **Adam: A Method for Stochastic Optimization** `[SEARCH]` | https://arxiv.org/abs/1412.6980 | 2014 | Первый и второй моменты, bias correction. Классический вопрос: «почему нужна bias correction на первых шагах». | **[MUST]** junior→middle |
| **Batch Normalization** `[ARXIV]` | https://arxiv.org/abs/1502.03167 | 2015 | Формулировка через internal covariate shift + различие train/eval режимов (running statistics). Важно: современное объяснение эффекта другое — стоит указать в хендбуке. | **[MUST]** junior→middle |
| **Deep Residual Learning (ResNet)** `[ARXIV]` | https://arxiv.org/abs/1512.03385 | 2015 | Почему skip-connection складывают, а не конкатенируют, и как это решает деградацию градиента. | **[MUST]** junior→middle |
| **Identity Mappings in Deep Residual Networks** `[ARXIV]` | https://arxiv.org/abs/1603.05027 | 2016 | Pre-activation блок; объясняет, почему порядок BN/ReLU/conv имеет значение. | **[OPT]** middle_plus |
| **Dropout: A Simple Way to Prevent NN from Overfitting** `[SEARCH]` | JMLR 15 (2014) | 2014 | Интерпретация как ансамбль подсетей + inverted dropout на инференсе. | **[MUST]** junior |
| **Google Deep Learning Tuning Playbook** `[REF]` | https://github.com/google-research/tuning_playbook | 2023 | Единственный источник, где системно расписано, *в каком порядке* крутить гиперпараметры. Прямо переносится в раздел «как отлаживать обучение». | **[MUST]** middle |
| **Efficient DL Systems (ВШЭ + ШАД)** `[FETCH]` | https://github.com/mryab/efficient-dl-systems | 2026 | CUDA/GPU → профилирование → data-parallel и All-Reduce → обучение больших моделей → sharded (ZeRO/FSDP) → перформанс from first principles → деплой → системные и алгоритмические оптимизации инференса. Закрывает почти весь middle_plus DL-инфраструктурный блок. | **[MUST]** middle_plus |
| **ml-engineering (Stas Bekman)** `[FETCH]` | https://github.com/stas00/ml-engineering | актуальный | Практика обучения LLM/VLM на кластере (опыт BLOOM-176B, IDEFICS-80B): ускорители, сеть, storage, SLURM, отладка падений. Уникально тем, что это записи реальных инцидентов. | **[OPT]** middle_plus |
| **The Little Book of Deep Learning (Fleuret)** `[REF]` | https://fleuret.org/francois/lbdl.html | — | 160 страниц на телефоне — идеально для повторения перед собесом. | **[OPT]** junior |
| **Deep Learning Interviews (arXiv 2201.00650)** `[REF]` | https://arxiv.org/abs/2201.00650 | 2022 | Сборник задач с решениями по DL в формате интервью. | **[OPT]** middle |
| **DLtest (Дьяконов)** `[REF]` | https://github.com/Dyakonov/BOOKs/blob/main/DLtest_Dyakonov.pdf | — | Русскоязычный тест по DL — удобный формат для «проверь себя» в конце главы. | **[OPT]** middle |

### 3. NLP и LLM (главы 04-nlp, 05-llm)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Attention Is All You Need** `[ARXIV]` | https://arxiv.org/abs/1706.03762 | 2017 | Первоисточник трансформера. На собесе спрашивают: зачем деление на √d_k, зачем multi-head, чем self- отличается от cross-attention, почему сложность O(n²). | **[MUST]** junior→middle |
| **BERT** `[ARXIV]` | https://arxiv.org/abs/1810.04805 | 2018 | MLM + NSP, [CLS]/[SEP], двунаправленность. Обязательный вопрос «как обучался BERT». | **[MUST]** junior→middle |
| **GPT-3 / Language Models are Few-Shot Learners** `[ARXIV]` | https://arxiv.org/abs/2005.14165 | 2020 | Откуда взялись few-shot/in-context learning и почему decoder-only победил. | **[MUST]** middle |
| **InstructGPT** `[ARXIV]` | https://arxiv.org/abs/2203.02155 | 2022 | Трёхстадийный пайплайн SFT → Reward Model → PPO. Каноничный ответ на «как устроен RLHF». | **[MUST]** middle |
| **DPO** `[ARXIV]` | https://arxiv.org/abs/2305.18290 | 2023 | Почему можно выкинуть отдельную reward-модель и PPO. Стандартный follow-up после RLHF. | **[MUST]** middle→middle_plus |
| **Chinchilla / Training Compute-Optimal LLMs** `[ARXIV]` | https://arxiv.org/abs/2203.15556 | 2022 | Соотношение параметров и токенов (~20 токенов на параметр). Ответ на «как выбрать размер модели под бюджет». | **[MUST]** middle_plus |
| **LoRA** `[ARXIV]` | https://arxiv.org/abs/2106.09685 | 2021 | Низкоранговые адаптеры, rank/alpha, почему экономит память оптимизатора, а не активаций. Самая частая практическая тема на LLM-собесах. | **[MUST]** middle |
| **FlashAttention** `[ARXIV]` | https://arxiv.org/abs/2205.14135 | 2022 | IO-awareness, tiling, отказ от материализации матрицы внимания. Ответ на «как бороться с квадратичной памятью внимания». | **[MUST]** middle_plus |
| **PagedAttention / vLLM** `[ARXIV]` | https://arxiv.org/abs/2309.06180 | 2023 | KV-cache как виртуальная память, continuous batching. Ключ к разделу про инференс и throughput. | **[MUST]** middle_plus |
| **LLaMA** `[ARXIV]` | https://arxiv.org/abs/2302.13971 | 2023 | RMSNorm, SwiGLU, RoPE, pre-norm — «архитектурный стандарт» современных открытых LLM. | **[MUST]** middle |
| **RAG (обзор)** `[ARXIV]` | https://arxiv.org/abs/2404.10981 | 2024 | Систематизация RAG-пайплайнов; удобно как источник таксономии для главы. Оригинальную статью Lewis et al. 2020 (arXiv:2005.11401) стоит указать, но она в этой сессии не верифицирована. | **[MUST]** middle |
| **NLP Course | For You (Lena Voita)** `[SEARCH]` | https://lena-voita.github.io/nlp_course.html | актуальный | Word embeddings, классификация, LM, seq2seq+attention, transfer learning. Лучшие в мире объяснения attention с анимациями. | **[MUST]** junior→middle |
| **YSDA NLP Course** `[FETCH]` | https://github.com/yandexdataschool/nlp_course | 2025 | 14 недель: embeddings → LM → seq2seq/attention/BPE → transfer learning (ELMo/GPT/BERT) → LLM и scaling laws → prompting и CoT → fine-tuning → эффективность → RAG → агенты → интерпретируемость → мультимодальность → прод. Готовое оглавление NLP+LLM-раздела. | **[MUST]** middle |
| **Speech and Language Processing (Jurafsky & Martin), 3rd ed.** `[REF]` | https://web.stanford.edu/~jurafsky/slp3/ | draft | Классика для «дотрансформерного» NLP: токенизация, N-граммы, HMM, парсинг. Нужно, когда спрашивают про TF-IDF, BM25, CRF. | **[OPT]** middle |
| **The Illustrated Transformer (Jay Alammar)** `[SEARCH]` | https://jalammar.github.io/illustrated-transformer/ | 2018 | Каноническое визуальное объяснение. Использовать как ориентир для собственных схем в хендбуке. | **[MUST]** junior |
| **The Annotated Transformer (Harvard NLP)** `[REF]` | https://github.com/harvardnlp/annotated-transformer | — | Статья построчно превращена в код. Для тех, кого просят «напиши multi-head attention». | **[MUST]** middle |
| **Блог Lilian Weng** `[SEARCH]` | https://lilianweng.github.io/ | — | «The Transformer Family», «Attention? Attention!», обзоры по агентам и галлюцинациям. Часто это лучший обзор темы вообще. | **[MUST]** middle |
| **LLMs-from-scratch (Raschka)** `[REF]` | https://github.com/rasbt/LLMs-from-scratch | 2024 | Сборка GPT-подобной модели с нуля; закрывает вопросы про токенизацию, KV-cache и генерацию. | **[MUST]** middle |
| **CS336: Language Modeling from Scratch (Stanford)** `[REF]` | https://stanford-cs336.github.io/spring2025/ | 2025 | Самый глубокий публичный курс про то, как реально строят LLM (данные, токенизация, параллелизм, alignment, инференс). | **[OPT]** middle_plus |
| **minbpe (Karpathy)** `[REF]` | https://github.com/karpathy/minbpe | 2024 | BPE в 200 строк — закрывает популярный вопрос «как работает токенизатор». | **[MUST]** middle |
| **NLP Course by Hugging Face** `[REF]` | https://huggingface.co/course/chapter0 | актуальный | Практический стандарт индустрии: `transformers`, `datasets`, `peft`. | **[MUST]** junior→middle |
| **ruMTEB / FRIDA (SberDevices, X5 Tech)** `[SEARCH]` | https://habr.com/ru/companies/sberdevices/articles/831150/ · https://habr.com/ru/companies/X5Tech/articles/845398/ · https://habr.com/ru/companies/sberdevices/articles/909924/ | 2024–2025 | **Обязательно для российского рынка.** Как выбирать эмбеддинг-модель под русский язык, какие бенчмарки существуют, чем FRIDA отличается от e5/BGE. Вопрос «какую эмбеддинг-модель возьмёшь для русского RAG» встречается регулярно. | **[MUST]** middle |
| **What are Embeddings (Vicki Boykis)** `[REF]` | https://vickiboykis.com/what_are_embeddings/index.html | 2023 | История эмбеддингов от one-hot до трансформеров, честно про подводные камни. | **[OPT]** middle |
| **Prompt Engineering Guide** `[REF]` | https://www.promptingguide.ai/ · https://github.com/dair-ai/Prompt-Engineering-Guide | актуальный | Систематика приёмов; полезнее как справочник, чем как чтение. | **[OPT]** junior |
| **Advanced RAG Techniques (NirDiamant)** `[REF]` | https://github.com/NirDiamant/RAG_Techniques | 2024 | Каталог продвинутых RAG-приёмов с кодом: reranking, query rewriting, hybrid search, self-RAG. | **[MUST]** middle_plus |
| **AI Engineering (Chip Huyen)** `[SEARCH]` | https://www.oreilly.com/library/view/ai-engineering/9781098166298/ · https://github.com/chiphuyen/aie-book | 2025 | Как строить продукты поверх foundation models: оценка, промптинг vs finetuning, RAG vs агенты, инференс-оптимизация, экономика. Самая читаемая книга платформы O'Reilly в 2025. | **[MUST]** middle→middle_plus |

### 4. Рекомендательные системы (глава 06-recsys)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **BPR: Bayesian Personalized Ranking** `[ARXIV]` | https://arxiv.org/abs/1205.2618 | 2012 | Pairwise-функция потерь для implicit feedback; откуда берётся негативное сэмплирование. Базовый вопрос RecSys-собеса. | **[MUST]** middle |
| **Neural Collaborative Filtering** `[ARXIV]` | https://arxiv.org/abs/1708.05031 | 2017 | Переход от MF к MLP над эмбеддингами; полезно вместе с критикой (NCF vs хорошо настроенный iALS). | **[OPT]** middle |
| **Wide & Deep Learning for RecSys** `[ARXIV]` | https://arxiv.org/abs/1606.07792 | 2016 | Memorization vs generalization — до сих пор основная рамка для объяснения гибридных архитектур. | **[MUST]** middle |
| **DeepFM** `[ARXIV]` | https://arxiv.org/abs/1703.04247 | 2017 | Автоматические взаимодействия признаков второго порядка без ручного feature crossing. | **[MUST]** middle |
| **Deep Interest Network (DIN)** `[ARXIV]` | https://arxiv.org/abs/1706.06978 | 2018 | Attention по истории пользователя относительно кандидата — ключевая идея современного ранжирования. | **[MUST]** middle |
| **SASRec** `[ARXIV]` | https://arxiv.org/abs/1808.09781 | 2018 | Каузальный трансформер для next-item. De-facto бейзлайн секвенциальных рекомендаций. | **[MUST]** middle |
| **BERT4Rec** `[ARXIV]` | https://arxiv.org/abs/1904.06690 | 2019 | Двунаправленный вариант с masked item prediction. | **[MUST]** middle |
| **Is BERT4Rec really better than SASRec?** `[ARXIV]` | https://arxiv.org/abs/2309.07602 | 2023 | Отличный материал для главы «как не обмануться в офлайн-сравнении»: воспроизводимость, влияние лосса и бюджета обучения. | **[MUST]** middle_plus |
| **LightGCN** `[ARXIV]` | https://arxiv.org/abs/2002.02126 | 2020 | Что в GCN для рекомендаций реально работает (только соседское усреднение), а что — лишнее. | **[OPT]** middle_plus |
| **PinSage / Graph CNN for Web-Scale RecSys** `[ARXIV]` | https://arxiv.org/abs/1806.01973 | 2018 | Как масштабировать GNN до миллиардов узлов: random-walk сэмплирование, producer-consumer minibatch, MapReduce-инференс. | **[OPT]** middle_plus |
| **TIGER / Recommender Systems with Generative Retrieval** `[ARXIV]` | https://arxiv.org/abs/2305.05065 | 2023 | Semantic IDs и генеративный retrieval вместо ANN-поиска. Самая горячая тема RecSys-собесов 2025–2026. | **[MUST]** middle_plus |
| **RecSys-Course (SB AI Lab, RePlay)** `[FETCH]` | https://github.com/sb-ai-lab/RecSys-Course | — | 17 модулей на русском: сплиты и метрики → non-personalized → ItemKNN/UserKNN → SLIM/EASE → SVD/ALS/iALS → triplet/BPR/WARP → LightFM → двухстадийные модели → нейросети → секвенциальные → бандиты → графовые → Spark/Polars → ANN → прод. **Готовый скелет главы.** | **[MUST]** middle |
| **MTS «Your First RecSys» / «Your Second RecSys» (ODS)** `[SEARCH]` | https://ods.ai/tracks/mts-recsys-df2020 · https://ods.ai/tracks/recsys-course2021 | 2020 / 2021 | Русскоязычный практический вход: постановка задачи, сбор данных, фреймворки, прототип → прод. | **[MUST]** junior→middle |
| **RecTools (МТС)** `[SEARCH]` | https://github.com/MobileTeleSystems/RecTools | актуальный | Библиотека с единым API для iALS/LightFM/DSSM/секвенциальных моделей. Стандарт де-факто в русскоязычном RecSys. | **[MUST]** middle |
| **Авито: поисковое ранжирование** `[SEARCH]` | https://habr.com/ru/companies/avito/articles/846832/ | 2024 | Как устроен многоступенчатый ранкер на миллионах объявлений — реальный кейс для system-design-раздела. | **[MUST]** middle |
| **Авито: трансформенная персонализация** `[SEARCH]` | https://habr.com/ru/companies/avito/articles/1004694/ | 2025 | Пользовательские эмбеддинги в Redis, скалярное произведение как фича в ранкере. Прямо отвечает на вопрос «как отдавать эмбеддинги в реалтайме». | **[MUST]** middle_plus |
| **Авито: нейросетевая модель интересов пользователя** `[SEARCH]` | https://habr.com/ru/companies/avito/articles/974682/ | 2025 | Разнообразие и релевантность на главной; полезно для раздела про diversity/serendipity. | **[MUST]** middle_plus |
| **applied-ml (eugeneyan)** `[FETCH]` | https://github.com/eugeneyan/applied-ml | актуальный | Каталог блогов компаний по RecSys/Search/MLOps/A-B: Netflix, Spotify, Pinterest, Amazon, YouTube, TikTok, LinkedIn, DoorDash, Airbnb, Etsy, Alibaba. **Основной источник индустриальных кейсов.** | **[MUST]** middle |
| **Personalized Machine Learning (McAuley)** `[REF]` | https://cseweb.ucsd.edu/~jmcauley/pml/ | 2022 | Академический учебник по персонализации от автора SASRec. | **[OPT]** middle_plus |
| **Yandex: рекомендательные системы (knowledge)** `[REF]` | https://education.yandex.ru/knowledge/rekomendatelnye-sistemy.-mashinnoe-obuchenie | — | Короткий русскоязычный обзор. | **[OPT]** junior |

### 5. MLOps, продакшн, мониторинг (главы 07-mlops, 09-monitoring)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Hidden Technical Debt in Machine Learning Systems (Sculley et al.)** `[SEARCH]` | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 2015 | Каноническая рамка: CACE, entanglement, hidden feedback loops, undeclared consumers, data dependencies, конфигурационный долг, «ML-код — малая часть системы». **Самая цитируемая статья на MLOps-собесах.** | **[MUST]** middle |
| **Rules of Machine Learning (Zinkevich, Google)** `[SEARCH]` | https://developers.google.com/machine-learning/guides/rules-of-ml · https://martin.zinkevich.org/rules_of_ml/ | 2017 | 43 правила в трёх фазах. Из них на собесах реально спрашивают: начни без ML, сначала инфраструктура и метрики, следи за train/serving skew, не переусложняй фичи раньше времени. | **[MUST]** junior→middle |
| **The ML Test Score (Breck, Cai, Nielsen, Salib, Sculley)** `[SEARCH]` | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 2017 | 28 конкретных тестов по 4 группам (данные, модель, инфраструктура, мониторинг). Готовый чек-лист для главы «как понять, что модель готова к проду». | **[MUST]** middle |
| **Designing Machine Learning Systems (Chip Huyen)** `[FETCH]` | https://github.com/chiphuyen/dmls-book · https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/ | 2022 | Опорная книга всего MLOps-раздела: data engineering fundamentals, feature engineering, оценка моделей, деплой, батч vs стрим, дрифт, continual learning, инфраструктура, human side. Есть русский перевод. | **[MUST]** middle |
| **MLOps Zoomcamp (DataTalksClub)** `[FETCH]` | https://github.com/DataTalksClub/mlops-zoomcamp | актуальный | Единственный бесплатный курс, где всё руками: MLflow → оркестрация → Flask/Kinesis+Lambda/batch деплой → Evidently+Prometheus+Grafana → CI/CD GitHub Actions → Terraform. | **[MUST]** middle |
| **Uber Michelangelo** `[SEARCH]` | https://www.uber.com/us/en/blog/scaling-michelangelo/ · https://www.uber.com/us/en/blog/uber-science-machine-learning-platform/ | 2017 / 2019+ | Первый публично описанный end-to-end ML-платформенный стек: feature store, тренировка, деплой, мониторинг. Эталон для вопроса «спроектируй ML-платформу». | **[MUST]** middle_plus |
| **ml_system_design_doc_ru (Reliable ML)** `[FETCH]` | https://github.com/IrinaGoloshchapova/ml_system_design_doc_ru | актуальный | **Русскоязычный шаблон дизайн-дока** + чек-лист оценки (ITMO & Reliable ML). Обязателен, потому что в РФ на middle+ часто просят именно написать дизайн-док, а не «поговорить». | **[MUST]** middle |
| **MLSystemDesign (компаньон книги Manning)** `[FETCH]` | https://github.com/ML-SystemDesign/MLSystemDesign | актуальный | `basic_ml_design_doc.md` из 12 разделов + `design_doc_checklist.md` + разобранные кейсы (Retail Demand Forecasting, RAG Chat with Document Versions). | **[MUST]** middle |
| **awesome-production-machine-learning** `[FETCH]` | https://github.com/EthicalML/awesome-production-machine-learning | актуальный | Каталог инструментов: деплой, мониторинг, версионирование, масштабирование, privacy-preserving ML, интерпретируемость. Нужен, чтобы в главе не изобретать список тулов. | **[OPT]** middle |
| **Practitioner's Guide to MLOps (Google whitepaper)** `[REF]` | https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf | 2021 | Формальная модель зрелости MLOps (уровни 0/1/2) — язык, на котором говорят на собесах в крупных компаниях. | **[MUST]** middle |
| **MLOps by Chip Huyen (подборка)** `[SEARCH]` | https://huyenchip.com/mlops/ | — | Курируемый список инструментов и статей. | **[OPT]** middle |
| **ODS: ML in Production / ML System Design** `[SEARCH]` | https://ods.ai/tracks/ml-in-production-spring-23 · https://ods.ai/tracks/ml-system-design-23 | 2022–2023 | Русскоязычные треки с разбором реальных дизайн-доков. | **[MUST]** middle |
| **Made With ML** `[REF]` | https://madewithml.com/#mlops | актуальный | End-to-end проект от разметки до CI/CD — хорошо как «сделай сам» в конце главы. | **[OPT]** junior→middle |
| **Reliable Machine Learning (O'Reilly)** `[REF]` | https://www.amazon.com/Reliable-Machine-Learning-Principles-Production/dp/1098106229/ | 2022 | SRE-подход к ML: SLO для моделей, on-call, постмортемы. | **[OPT]** middle_plus |

### 6. Big Data и инфраструктура данных (глава 08-big-data)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Designing Data-Intensive Applications (Kleppmann)** `[SEARCH]` | https://dataintensive.net/ | 2017 (рус. «Высоконагруженные приложения», Питер, 2018, ISBN 978-5-4461-0512-0) | **Единственная обязательная книга раздела.** Гл. 3 (storage engines, LSM vs B-tree), 4 (форматы и эволюция схем — прямо про Parquet/Avro), 6 (партиционирование), 7 (транзакции), 11 (стриминг). | **[MUST]** middle |
| **Learning Spark, 2nd ed. (Databricks)** `[REF]` | https://pages.databricks.com/rs/094-YMS-629/images/LearningSpark2.0.pdf | 2020 | Бесплатный PDF. DataFrame API, Catalyst, Tungsten, оконные функции, структурированный стриминг. | **[MUST]** middle |
| **Data Analysis with Python and PySpark (Manning)** `[REF]` | https://www.manning.com/books/data-analysis-with-python-and-pyspark | 2022 | PySpark для тех, кто пришёл из pandas. | **[OPT]** middle |
| **PySpark для аналитики (Avito, ч. 1 и 2)** `[REF]` | https://habr.com/ru/companies/avito/articles/732870/ · https://habr.com/ru/companies/avito/articles/740232/ | 2023 | Русскоязычная практика: партиционирование, скошенные джойны, broadcast. | **[MUST]** middle |
| **Spark для начинающих (Альфа)** `[REF]` | https://habr.com/ru/companies/alfa/articles/808415/ | 2024 | Разбор архитектуры Spark на русском. | **[OPT]** junior |
| **Vowpal Wabbit / обучение на гигабайтах (тема 8 ODS)** `[FETCH]` | https://habr.com/ru/companies/ods/articles/326418/ | 2017 | Hashing trick, online learning, out-of-core — до сих пор актуальные ответы на «что делать, если данные не влезают в память». | **[OPT]** middle |

### 7. A/B-тестирование и эксперименты (глава 10-ab-testing)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Kohavi, Tang, Xu — Trustworthy Online Controlled Experiments** `[SEARCH]` | https://www.amazon.com/Trustworthy-Online-Controlled-Experiments-Practical/dp/1108724264 | 2020 | **Библия A/B.** OEC, guardrail-метрики, SRM (sample ratio mismatch), сетевые эффекты, ловушки подглядывания, Twyman's law. Почти любой вопрос A/B-секции — оттуда. | **[MUST]** middle |
| **CUPED — Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (Deng, Xu, Kohavi, Walker)** `[SEARCH]` | KDD/WSDM 2013 | 2013 | Дисперсия падает в (1 − ρ²) раз; на Bing давало ~50% снижения дисперсии, т.е. вдвое меньше пользователей при той же мощности. Обязательный вопрос на middle+. | **[MUST]** middle→middle_plus |
| **Variance Reduction Using In-Experiment Data (Deng, KDD 2023)** `[SEARCH]` | https://alexdeng.github.io/public/files/kdd2023-inexp.pdf | 2023 | Продолжение CUPED, когда предэкспериментальных данных нет (новые пользователи). | **[OPT]** middle_plus |
| **Курс матстата и A/B Ульянкина** `[FETCH]` | https://github.com/FUlyankin/matstat-AB | — | Русскоязычная база: оценки, доверительные интервалы, гипотезы, бутстрап, A/B. Осознанно не «чёрный ящик». | **[MUST]** middle |
| **Курс по статистике от Авито** `[SEARCH]` | https://avito.tech/education/statistics | актуальный | Индустриальная русскоязычная подача A/B от компании, которая этим живёт. | **[MUST]** middle |
| **A/B Testing Roadmap (Balandin)** `[REF]` | https://github.com/YuriyBalandin/ab_testing_roadmap/blob/main/Roadmap/Roadmap.md | — | Структурированный план изучения — можно взять как каркас главы. | **[OPT]** middle |
| **Google: Overlapping Experiment Infrastructure** `[FETCH via applied-ml]` | (каталог eugeneyan/applied-ml) | 2010 | Слои экспериментов — ответ на «как запускать 100 экспериментов одновременно». | **[MUST]** middle_plus |
| **Кейсы платформ экспериментов: Netflix, Uber, Airbnb, DoorDash, Spotify** `[FETCH via applied-ml]` | https://github.com/eugeneyan/applied-ml | 2016–2021 | Разделы A/B Testing & Experimentation в каталоге. Подтверждено наличие постов Netflix «It's All A/Bout Testing», Uber (2017–2020), Airbnb (2017, 2021), DoorDash, Spotify (2020). | **[MUST]** middle_plus |
| **Practitioner's Guide to Statistical Tests (VK Team)** `[REF]` | https://vkteam.medium.com/practitioners-guide-to-statistical-tests-ed2d580ef04f | — | Русскоязычная команда, англоязычный текст: какой тест когда применять. | **[OPT]** middle |
| **Applied Causal Inference / Causal ML book** `[REF]` | https://causalml-book.org · https://alexdeng.github.io/causal/index.html | 2024 | Когда A/B невозможен: DiD, synthetic control, switchback. | **[OPT]** middle_plus |

### 8. ML System Design и собеседования (главы 11-system-design, 14-career)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **ML System Design Interview (Aminian & Xu)** `[SEARCH]` | https://www.amazon.com/Machine-Learning-System-Design-Interview/dp/1736049127 | 2023 | Пошаговый фреймворк + разобранные задачи (видео-рекомендации, поиск по картинке, лента, реклама, детекция вредного контента). Де-факто стандарт подготовки. | **[MUST]** middle |
| **Generative AI System Design Interview (Aminian & Sheng)** `[SEARCH]` | https://www.amazon.com/Generative-AI-System-Design-Interview/dp/1736049143 | 2024-11-18 | 7-шаговый фреймворк + 10 задач по генеративным системам. Дополняет предыдущую, а не заменяет. | **[MUST]** middle_plus |
| **chiphuyen/machine-learning-systems-design** `[FETCH]` | https://github.com/chiphuyen/machine-learning-systems-design | 2019 | 27 открытых вопросов по ML system design + 4-частная рамка (project setup / data pipeline / modeling / serving). | **[MUST]** middle |
| **Case studies (Chip Huyen)** `[FETCH]` | https://raw.githubusercontent.com/chiphuyen/machine-learning-systems-design/master/content/case-studies.md | 2019 | 12 кейсов с атрибуцией: Airbnb (оценка стоимости жилья; ранжирование Experiences), Netflix (качество стриминга; DL для рекомендаций; надёжность ML-алгоритмов), Booking.com («150 Successful ML Models: 6 Lessons Learned»), Lyft (from shallow to deep learning in fraud), Uber (Big Data Platform 100+ PB; Scaling ML with Michelangelo), Chicisimo, Instacart, Dropbox. | **[MUST]** middle |
| **Introduction to ML Interviews Book (Chip Huyen)** `[SEARCH]` | https://huyenchip.com/ml-interviews-book/ | 2021 | Бесплатно онлайн. Как устроен процесс найма + большой банк вопросов. | **[MUST]** junior→middle |
| **alirezadir/Machine-Learning-Interviews** `[FETCH]` | https://github.com/alirezadir/Machine-Learning-Interviews | обновл. 2026 | 6 глав: general coding, ML coding, ML breadth, ML system design, **agentic AI systems**, behavioral. Автор — по офферам Meta/Google/Amazon/Apple/Roku. Обновление 2026 под LLM/мультимодальность и агентов. | **[MUST]** middle |
| **khangich/machine-learning-interview** `[FETCH]` | https://github.com/khangich/machine-learning-interview | актуальный | «Minimum Viable Study Plan»: LeetCode, SQL (джойны, оконные), programming, статистика/вероятности, Big Data (Spark, Cassandra), ML fundamentals, A/B, DL, ML system design. Компании: Google, Facebook, Amazon, Apple, Microsoft, Snapchat, LinkedIn, Coupang, StitchFix, Booking, NVIDIA, Intel. | **[MUST]** middle |
| **Extremesarova/ds_resources** `[FETCH]` | https://github.com/Extremesarova/ds_resources | актуальный | **Самый полный русскоязычно-ориентированный каталог** ресурсов для подготовки. Отдельно ценны разделы Company-Specific Resources и Home Assignments. | **[MUST]** все грейды |
| **Tinkoff/career — секция ML** `[FETCH]` | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/platform-ml.md | актуальный | **Официальный список литературы российской компании.** Прямо называет: ESL (PDF Стэнфорда), PRML, Goodfellow DL, Manning «Introduction to Information Retrieval», Practical_DL / Practical_RL / nlp_course ШАДа, Catalyst DL course, книгу Николенко–Кадурина–Архангельской «Глубокое обучение», банки вопросов (kojino/120, iamtodor, alexeygrigorev, dingran/quant-notes). | **[MUST]** все грейды |
| **Tinkoff/career — структура интервью** `[FETCH]` | https://github.com/Tinkoff/career/blob/main/interview/README.md | актуальный | 2–4 секции по 1–1.5 ч: programming, ML platform, ML system design. | **[MUST]** все грейды |
| **alexeygrigorev/data-science-interviews** `[FETCH]` | https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/theory.md | актуальный | Банк теории с **явной разметкой сложности**: 👶 = junior, ⭐ = middle, 🚀 = senior. Эта разметка — готовая рубрика грейдов для хендбука. | **[MUST]** все грейды |
| **Pe4enIks/ML-Interview** `[FETCH]` | https://github.com/Pe4enIks/ML-Interview | актуальный | Русскоязычный банк вопросов MLE с уклоном в CV/мультимодалку. | **[MUST]** middle |
| **slgero/testovoe** `[FETCH]` | https://github.com/slgero/testovoe | актуальный | Реальные тестовые задания: Uber, Gett, S7, МТС, Сбер (Деловая Среда), СКБ Контур, Альфабанк KZ, БКС, Wargaming, PWC, BCG Gamma, Accenture, AUTO1, Diginetica, OLX-Hermes, Zyfra и др. | **[MUST]** middle |
| **The System Design Primer** `[REF]` | https://github.com/donnemartin/system-design-primer | актуальный | Общий (не ML) system design: кэши, шардирование, CAP, очереди. Нужен как фундамент под ML SD. | **[MUST]** middle |
| **ML Systems Design Interview Guide (Patrick Halina)** `[REF]` | http://patrickhalina.com/posts/ml-systems-design-interview-guide/ | — | Короткий, но очень плотный фреймворк ответа. | **[MUST]** middle |
| **ML System Design: 500 case studies (Evidently AI)** `[REF]` | https://www.evidentlyai.com/ml-system-design | актуальный | База индустриальных кейсов с фильтрами по индустрии и задаче. | **[MUST]** middle |
| **Stanford CS329S: ML Systems Design** `[REF]` | https://stanford-cs329s.github.io/syllabus.html | 2022 | Курс, из которого выросла книга Chip Huyen. | **[OPT]** middle |
| **eugeneyan.com + applyingml.com** `[REF]` | https://eugeneyan.com/ · https://applyingml.com/ | актуальный | Эссе про прикладной ML, дизайн-доки, оценку LLM. Один из немногих блогов, который стоит читать подряд. | **[MUST]** middle |

### 9. Программирование, алгоритмы, SQL (глава 12-coding)

| Источник | URL | Год | Что брать и кому | Статус |
|---|---|---|---|---|
| **Хендбук по алгоритмам (Яндекс)** `[SEARCH]` | https://academy.yandex.ru/handbook/algorithms | актуальный | Русскоязычный канон по алгоритмам и структурам данных. | **[MUST]** junior |
| **Хендбук по Python (Яндекс)** `[SEARCH]` | https://education.yandex.ru/handbook/python | актуальный | База Python на русском. | **[MUST]** junior |
| **NeetCode Roadmap** `[REF]` | https://neetcode.io/roadmap | актуальный | Наиболее эффективный порядок прохождения LeetCode по паттернам. | **[MUST]** junior→middle |
| **LeetCode Patterns (Sean Prashad)** `[REF]` | https://seanprashad.com/leetcode-patterns/ | актуальный | Группировка задач по приёмам. | **[MUST]** junior |
| **What the f*ck Python** `[REF]` | https://github.com/satwikkansal/wtfpython | актуальный | Источник каверзных вопросов про мутабельность, кэш малых int, замыкания в циклах — ровно то, что спрашивают в Python-секции. | **[OPT]** middle |
| **Comprehensive Python Cheatsheet** `[REF]` | https://github.com/gto76/python-cheatsheet | актуальный | Справочник на одну страницу. | **[OPT]** junior |
| **DataLemur / sql-practice / PostgreSQL Exercises** `[REF]` | https://datalemur.com/questions?category=SQL · https://www.sql-practice.com/ · https://pgexercises.com/ | актуальный | Практика SQL до уровня оконных функций и self-join — на MLE-собесах в РФ SQL спрашивают почти всегда. | **[MUST]** junior→middle |
| **Algorithmica (рус.)** `[REF]` | https://ru.algorithmica.org/ | актуальный | Русскоязычный учебник по алгоритмам. | **[OPT]** junior |
| **CodeRun (Яндекс)** `[REF]` | https://coderun.yandex.ru | актуальный | Задачи в формате, максимально близком к реальным собесам Яндекса. | **[MUST]** junior→middle |

---

## Вопросы с собеседований

> Ниже — только вопросы, **дословно прочитанные** в скачанных документах. Для каждой группы указано,
> каким источником из канона выше вопрос закрывается — это и есть смысл раздела «источники»:
> связать вопрос ↔ текст, который на него отвечает.
> Грейды в `alexeygrigorev/data-science-interviews` размечены самим репозиторием (👶/⭐/🚀) — я сохраняю эту разметку.

### 9.1. Метавопросы про источники и самообучение

Прямых вербатим-формулировок вида «какие статьи вы читаете» в скачанных документах **не нашлось** —
поисковая выдача по такому запросу содержательных подтверждений не дала, поэтому такие вопросы я не выдумываю.
Что верифицировано косвенно, но железно:

- **Т-Банк официально публикует список литературы к ML-секции** (`[FETCH]`, https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/platform-ml.md). Это значит: на собесе ожидают знания именно ESL / PRML / Goodfellow / Manning IR и курсов ШАДа. Формально это не «вопрос», но это самый сильный сигнал о каноне на российском рынке. — grade: `middle`, source: Tinkoff/T-Bank.
- **Т-Банк описывает ML-секцию как** «Разбираем вопросы по анализу данных: о постановке задачи, выборе и обосновании метрик качества, сборе и валидации данных, ML-алгоритмах» (verbatim, там же). — grade: `middle`, source: Tinkoff/T-Bank, url: см. выше.

### 9.2. Классический ML — закрывается ESL гл. 3/7/9/10/15, ISLR, учебником ШАДа, курсом ODS

Из `Pe4enIks/ML-Interview` (`[FETCH]`, https://github.com/Pe4enIks/ML-Interview), RU:

| Вопрос (verbatim) | Grade | Чем закрывается |
|---|---|---|
| Что такое градиентный бустинг? Где там появляется градиент? | middle | ESL гл. 10; учебник ШАДа |
| Рассказать про RandomForest. | junior | ESL гл. 15; ODS тема 5 |
| Можно ли строить RandomForest над KNN, линейными моделями и нейросетями, почему? | middle_plus | ESL гл. 15 (про декорреляцию); ODS тема 5 |
| Как аналитически решается задача линейной регрессии? | junior | ESL гл. 3 (нормальное уравнение) |
| Как происходит процесс построения дерева? | junior | ESL гл. 9; ODS тема 3 |
| Что такое bagging? | junior | ESL гл. 8.7 |
| Что такое переобучение? Какие есть способы борьбы с ним? | junior | ESL гл. 7 |
| Какие существуют методы регуляризации? | junior | ESL гл. 3.4 |
| Почему L1 регуляризация зануляет часть весов? | middle | ESL гл. 3.4 (геометрия ромба vs круга) |
| Что такое bias, variance модели? | junior | ESL гл. 7.3 |
| Что такое bias-variance trade-off? | junior | ESL гл. 7.3; ISLR гл. 2 |
| Что такое дисбаланс классов и как с ним бороться? | junior | ODS тема 4; Molnar/метрики |

Из `alexeygrigorev/data-science-interviews` (`[FETCH]`, https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/theory.md), EN, разметка репозитория:

| Вопрос (verbatim) | Grade (по репо) | Чем закрывается |
|---|---|---|
| What is supervised machine learning? | 👶 junior | ISLR гл. 2 |
| What is regression? Which models can you use to solve a regression problem? | 👶 junior | ISLR гл. 3 |
| What are the main assumptions of linear regression? | ⭐ middle | ESL гл. 3 |
| What's the normal distribution? Why do we care about it? | 👶 junior | CS109; Ульянкин нед. 5 |
| How do we check if a variable follows the normal distribution? | ⭐ middle | Ульянкин; matstat-AB |
| What if we want to build a model for predicting prices? Are prices distributed normally? Do we need to do any pre-processing for prices? | ⭐ middle | ESL гл. 3; ODS тема 6 |
| What methods for solving linear regression do you know? | ⭐ middle | ESL гл. 3 |
| What is gradient descent? How does it work? | ⭐ middle | Goodfellow гл. 4/8 |
| What is the normal equation? | ⭐ middle | ESL гл. 3.2 |
| What is SGD — stochastic gradient descent? What's the difference with the usual gradient descent? | ⭐ middle | Goodfellow гл. 8 |
| Which metrics for evaluating regression models do you know? | 👶 junior | ISLR гл. 2 |
| What are MSE and RMSE? | 👶 junior | ISLR гл. 2 |
| What is the bias-variance trade-off? | 👶 junior | ESL гл. 7.3 |
| What is overfitting? | 👶 junior | ESL гл. 7 |
| How to validate your models? | 👶 junior | ESL гл. 7.10 |
| Why do we need to split our data into three parts: train, validation, and test? | 👶 junior | ESL гл. 7.2 |
| Can you explain how cross-validation works? | 👶 junior | ESL гл. 7.10 |
| What is K-fold cross-validation? | 👶 junior | ESL гл. 7.10 |
| How do we choose K in K-fold cross-validation? What's your favorite K? | 👶 junior | ESL гл. 7.10 |
| What is classification? Which models would you use to solve a classification problem? | 👶 junior | ISLR гл. 4 |
| What is logistic regression? When do we need to use it? | 👶 junior | ESL гл. 4.4 |
| Is logistic regression a linear model? Why? | 👶 junior | ESL гл. 4.4 |
| What is sigmoid? What does it do? | 👶 junior | ESL гл. 4.4 |
| How do we evaluate classification models? | 👶 junior | ODS тема 4 |
| What is accuracy? | 👶 junior | — |
| Is accuracy always a good metric? | 👶 junior | ODS тема 4 |
| What is the confusion table? What are the cells in this table? | 👶 junior | — |
| What are precision, recall, and F1-score? | 👶 junior | ODS тема 4 |
| Precision-recall trade-off | ⭐ middle | ODS тема 4 |
| What happens to our linear regression model if we have three columns in our data: x, y, z — and z is a sum of x and y? | ⭐ middle | ESL гл. 3 (мультиколлинеарность) |
| What happens to our linear regression model if the column z in the data is a sum of columns x and y and some random noise? | ⭐ middle | ESL гл. 3 |
| What is regularization? Why do we need it? | 👶 junior | ESL гл. 3.4 |
| Which regularization techniques do you know? | ⭐ middle | ESL гл. 3.4 |
| What kind of regularization techniques are applicable to linear models? | ⭐ middle | ESL гл. 3.4 |
| How does L2 regularization look like in a linear model? | ⭐ middle | ESL гл. 3.4.1 |
| How do we select the right regularization parameters? | 👶 junior | ESL гл. 7 |
| What's the effect of L2 regularization on the weights of a linear model? | ⭐ middle | ESL гл. 3.4.1 |
| How L1 regularization looks like in a linear model? | ⭐ middle | ESL гл. 3.4.2 |
| What's the difference between L2 and L1 regularization? | ⭐ middle | ESL гл. 3.4 |
| What is feature selection? Why do we need it? | 👶 junior | ODS тема 6 |
| Is feature selection important for linear models? | ⭐ middle | ESL гл. 3.3 |
| Which feature selection techniques do you know? | ⭐ middle | ODS тема 6 |
| Can we use L1 regularization for feature selection? | ⭐ middle | ESL гл. 3.4.2 |
| Can we use L2 regularization for feature selection? | ⭐ middle | ESL гл. 3.4.1 |
| What are the decision trees? | 👶 junior | ESL гл. 9.2 |
| How do we train decision trees? | ⭐ middle | ESL гл. 9.2 |
| What are the main parameters of the decision tree model? | 👶 junior | ODS тема 3 |
| How do we handle categorical variables in decision trees? | ⭐ middle | CatBoost paper; ESL гл. 9.2 |
| What are the benefits of a single decision tree compared to more complex models? | ⭐ middle | Molnar |
| How can we know which features are more important for the decision tree model? | ⭐ middle | Molnar; ESL гл. 15.3 |
| What is random forest? | 👶 junior | ESL гл. 15 |
| Why do we need randomization in random forest? | ⭐ middle | ESL гл. 15.2 |
| What are the main parameters of the random forest model? | ⭐ middle | ODS тема 5 |
| How do we select the depth of the trees in random forest? | ⭐ middle | ESL гл. 15 |
| How do we know how many trees we need in random forest? | ⭐ middle | ESL гл. 15 |
| Is it easy to parallelize training of a random forest model? How can we do it? | ⭐ middle | ESL гл. 15 |
| What are the potential problems with many large trees? | ⭐ middle | ESL гл. 15 |
| What if instead of finding the best split, we randomly select a few splits and just select the best from them. Will it work? | 🚀 middle_plus | ESL гл. 15 (Extra Trees) |
| What happens when we have correlated features in our data? | ⭐ middle | ESL гл. 3.3; Molnar |

### 9.3. Метрики и валидация — закрывается ODS тема 4, ESL гл. 7, блогом Дьяконова

Из `Pe4enIks/ML-Interview` (`[FETCH]`), RU:

| Вопрос (verbatim) | Grade | Чем закрывается |
|---|---|---|
| Какие метрики бинарной классификации есть? | junior | ODS тема 4 |
| Что такое TPR и FPR? | junior | ODS тема 4 |
| ROC-AUC = 0.9, что с ним будет если домножить все предсказания на число 3? | middle | блог Дьяконова (AUC инвариантен к монотонным преобразованиям) |
| Метрики multiclass классификации | middle | ODS тема 4 |
| Как происходит расчет ROC-AUC? | middle | ODS тема 4; блог Дьяконова |

### 9.4. Оптимизация и обучение НС — закрывается Goodfellow гл. 6–9, Adam, BatchNorm, Dropout, Tuning Playbook

Из `Pe4enIks/ML-Interview` (`[FETCH]`), RU:

| Вопрос (verbatim) | Grade | Чем закрывается |
|---|---|---|
| Какие знаешь оптимизаторы, в чем их идеи и различия? | middle | Adam (1412.6980); Goodfellow гл. 8 |
| Что такое gradient clipping? | middle | Goodfellow гл. 10.11 |
| Рассказать про gradient accumulation. | middle | efficient-dl-systems нед. 2 |
| Что такое Dropout? | junior | Dropout, JMLR 2014 |
| Как работает BatchNorm и LayerNorm? | junior | BatchNorm (1502.03167) |
| Почему сеть с BatchNorm сходится быстрее? | middle | BatchNorm (1502.03167) + современная критика ICS |
| Какие проблемы могут возникать при использовании функции активации Sigmoid? | junior | Goodfellow гл. 6 |
| Какой learning rate будешь использовать для большого батча? | middle_plus | Tuning Playbook (linear scaling rule) |
| Проблемы с инициализацией весов нулями | junior | Goodfellow гл. 8.4 |
| Почему в residual connection используется операция сложения? | middle | ResNet (1512.03385) |
| Почему модель на этапе обучения занимает больше памяти? | middle | efficient-dl-systems нед. 2 (активации + состояния оптимизатора) |

### 9.5. Трансформеры, NLP, LLM — закрывается Attention/BERT/LoRA/FlashAttention, курсом Войты, YSDA NLP

Из `Pe4enIks/ML-Interview` (`[FETCH]`), RU:

| Вопрос (verbatim) | Grade | Чем закрывается |
|---|---|---|
| Рассказать про multi-head attention в деталях. | middle | Attention Is All You Need (1706.03762); Annotated Transformer |
| В чем разница self-attention и cross-attention? | middle | 1706.03762; курс Войты |
| Что такое позиционные эмбеддинги и для чего они нужны? | middle | 1706.03762; RoPE (2104.09864) |
| Как борются с квадратичной сложностью механизма внимания? | middle_plus | FlashAttention (2205.14135) |
| Как обучался BERT? | middle | BERT (1810.04805) |
| Почему мы перешли от сверток (CNN) к механизму вниманию (Transformer)? | middle | 1706.03762; ViT |
| Рассказать про ControlNet, LoRA. | middle | LoRA (2106.09685) |
| CLIP — идея, функция потерь, способ обучения | middle | CLIP (2103.00020) |

### 9.6. Computer Vision — закрывается CS231n, ResNet, YSDA Practical_DL

Из `Pe4enIks/ML-Interview` (`[FETCH]`), RU:

| Вопрос (verbatim) | Grade |
|---|---|
| Рассказать про архитектуру ViT. | middle |
| Рассказать про идею ResNet, написать ResidualBlock. | middle |
| Рассказать про MobileNet и EfficientNet. | middle |
| Что такое операция свертки? | junior |
| Что такое receptive field? | junior |
| Может ли быть такое, что Atrous свертка вообще никогда не использует какой-то пиксель? | middle_plus |
| Можно ли заменить свертку 3x3 на две: 3x1 и 1x3? | middle |
| Как работает NMS (Non Maximum Suppression)? | middle |
| Рассказать про метрику MAP (Mean Average Precision) | middle |
| Что является таргетом в задаче детекции? | middle |
| Чем двухстадийные детекторы отличаются от одностадийных? | middle |
| Рассказать про венгерский алгоритм. | middle_plus |
| Что такое и зачем нужны RoI, RoI Pooling, RoI Align? | middle_plus |
| Что такое GAN, какие знаешь? | middle |
| Какая идея Cycle-GAN? | middle |
| Из каких частей состоит Stable Diffusion? | middle |
| Какая математическая идея у диффузионных моделей? | middle_plus |
| Что предсказывает U-Net в SD на каждом шаге? | middle_plus |
| Как обучаются модели SD? | middle_plus |

### 9.7. Статистика и вероятности — закрывается Ульянкиным, CS109, Kohavi

Из `Pe4enIks/ML-Interview` (`[FETCH]`), RU:

| Вопрос (verbatim) | Grade | Чем закрывается |
|---|---|---|
| Формулировка задачи Maximum Likelihood Estimation | middle | ESL гл. 8.2; Ульянкин нед. 12 |
| Коэффициент корреляции равен 0, можно ли утверждать, что выборки независимы? | junior | Ульянкин нед. 6 (нет: корреляция ловит только линейную связь) |
| Как проверить нормальность выборки? | middle | Ульянкин нед. 9 |
| Что такое pvalue и для чего оно нужно? | junior | Ульянкин нед. 9; Kohavi гл. 17 |

### 9.8. Python, SQL, алгоритмы — закрывается wtfpython, хендбуками Яндекса, DataLemur

Из `Pe4enIks/ML-Interview` (`[FETCH]`), RU:

| Вопрос (verbatim) | Grade |
|---|---|
| Отличие classmethod от staticmethod в Python? | junior |
| Какие типы данных подходят как ключ словаря? | junior |
| Какая структура данных лежит в основе dict в Python? | middle |
| Какие знаешь виды сортировок и их сложности? | junior |
| Что такое GIL в Python? | junior |
| Как реализуют параллельность с учетом GIL? | middle |
| Как посчитать медиану в SQL без встроенной функции? | middle |

### 9.9. ML System Design — закрывается Chip Huyen, Aminian & Xu, шаблонами дизайн-доков

Из `chiphuyen/machine-learning-systems-design` (`[FETCH]`) подтверждено наличие **27 открытых вопросов**
по ML system design; сами формулировки в скачанном фрагменте не раскрыты — фиксирую только факт и рамку
(project setup / data pipeline / modeling / serving).

Из `case-studies.md` (`[FETCH]`) — реальные индустриальные кейсы, которые интервьюеры используют как основу задач:

| Кейс (verbatim, EN) | Компания | Grade | url |
|---|---|---|---|
| Using Machine Learning to Predict Value of Homes On Airbnb | Airbnb | middle | https://raw.githubusercontent.com/chiphuyen/machine-learning-systems-design/master/content/case-studies.md |
| Machine Learning-Powered Search Ranking of Airbnb Experiences | Airbnb | middle_plus | там же |
| Using Machine Learning to Improve Streaming Quality at Netflix | Netflix | middle_plus | там же |
| Deep Learning for Recommender Systems | Netflix | middle | там же |
| Making Netflix Machine Learning Algorithms Reliable | Netflix | middle_plus | там же |
| 150 Successful Machine Learning Models: 6 Lessons Learned | Booking.com | middle | там же |
| From shallow to deep learning in fraud | Lyft | middle | там же |
| Uber's Big Data Platform: 100+ Petabytes with Minute Latency | Uber | middle_plus | там же |
| Scaling Machine Learning at Uber with Michelangelo | Uber | middle_plus | там же |

Из `Tinkoff/career` (`[FETCH]`): в интервью Т-Банка есть отдельные секции **ML Platform** и **ML System Design**,
всего кандидат проходит 2–4 секции по 1–1.5 часа. — grade: `middle`+, source: T-Bank,
url: https://github.com/Tinkoff/career/blob/main/interview/README.md

### 9.10. Тестовые задания (домашки) — по компаниям

Из `slgero/testovoe` (`[FETCH]`, https://github.com/slgero/testovoe) — подтверждённый список компаний,
чьи реальные тестовые задания лежат в репозитории:

- **RU/CIS:** МТС, Сбер (Деловая Среда), СКБ Контур (две версии), Альфабанк KZ, БКС, Ланит-ритейл, Zyfra (Цифра), Revo:Mokka, S7, One Factor, NeuroTrade.
- **Интернациональные:** Uber, Gett, Accenture, AUTO1, BCG Gamma, PWC, Wargaming, Diginetica, OLX-Hermes, Neuromation, PeakData AG, GamblingPro, Haensel AMS, Spectrm, Corpus, doc+, BHV Tech Development, Physician Partners, the-SAAS-co.

Grade: `middle` (тестовое обычно даётся после скрининга, до технической секции).

---

## Что интервьюеры ловят этими вопросами

**1. «Читал ли ты первоисточник или пересказ пересказа».**
Самый быстрый разделитель junior/middle. Признак «читал»: человек называет *механизм*, а не *эффект*.
Примеры маркеров:
- CatBoost — если кандидат говорит «он хорошо работает с категориями», это пересказ; если говорит
  «ordered target statistics + ordered boosting, чтобы убрать смещение от использования таргета того же объекта» —
  он открывал arXiv:1706.09516.
- LightGBM — «быстрее» vs «GOSS отбрасывает объекты с малым градиентом, EFB склеивает разреженные признаки, рост leaf-wise».
- BatchNorm — «ускоряет обучение» vs «в train используются батчевые статистики, в eval — накопленные running mean/var,
  отсюда баги при маленьком батче и при заморозке».

**2. Умение отличить «что было заявлено в статье» от «что оказалось правдой».**
Классические ловушки, которые прямо есть в каноне:
- BatchNorm заявляли через internal covariate shift, но последующие работы показали, что дело в сглаживании
  ландшафта. Хороший кандидат это оговаривает.
- BERT4Rec vs SASRec — arXiv:2309.07602 показывает, что исходное сравнение было нечестным по бюджету обучения.
  Тот, кто читал только BERT4Rec, скажет «BERT4Rec лучше» и провалит follow-up.
- NCF vs правильно настроенный iALS — та же история.

**3. Способность связать статью с продовым решением.**
Вопросы вида «как борются с квадратичной сложностью внимания» проверяют не знание FlashAttention как имени,
а понимание, что это **не аппроксимация**, а перестановка вычислений ради иерархии памяти GPU (HBM vs SRAM).
Аналогично PagedAttention — это не «оптимизация модели», а решение проблемы фрагментации KV-cache.

**4. Наличие «инженерной прошивки», а не только «модельной».**
Sculley et al. и Rules of ML ловят кандидатов, которые умеют обучать, но не умеют эксплуатировать:
train/serving skew, undeclared consumers, feedback loops, CACE. Практически на любом MLOps-собесе
всплывает картинка «ML-код — маленький чёрный прямоугольник» — и её нужно уметь развернуть в 10 минут речи.

**5. Статистическая честность.**
CUPED и Kohavi ловят два типа кандидатов: тех, кто не знает про снижение дисперсии вообще, и тех,
кто знает формулу, но не может сказать, **почему ковариата должна быть измерена до эксперимента**
(иначе она сама подвержена воздействию и оценка становится смещённой).

**6. Знание российского контекста.**
На отечественном рынке дополнительно проверяют: учебник ШАДа (терминология), CatBoost (Яндекс),
русскоязычные эмбеддинги (ruMTEB/FRIDA), ClickHouse/Spark-стек, RecTools. Кандидат, который весь канон
взял только из англоязычных источников, обычно спотыкается на «какую эмбеддинг-модель возьмёшь под русский».

---

## Пробелы, которые чаще всего валят кандидатов

1. **Знают названия статей, но не читали ни одной.** Названия «Attention Is All You Need», «ResNet», «BERT»
   произносят все; вывести формулу attention с √d_k и объяснить, почему делят именно на корень из размерности —
   единицы. Хендбук должен давать не список названий, а **вытяжку механизмов**.

2. **Разрыв «книга ↔ вопрос».** Кандидат прочитал ESL, но не понимает, какой вопрос собеса какой главой закрывается,
   поэтому читает всё подряд и не успевает. Отсюда прямая рекомендация: **в каждой главе хендбука указывать,
   какие 2–4 конкретные главы каких книг её закрывают**, а не «см. ESL».

3. **Русский канон игнорируют.** Люди готовятся по англоязычным репозиториям и приходят на собес,
   где терминология из учебника ШАДа и вопросы про CatBoost/ClickHouse. Учебник ШАДа + курс ODS +
   курс Воронцова/Дьяконова закрывают этот разрыв, но их почти не рекомендуют в англоязычных гайдах.

4. **Не знают, где остановиться.** Boyd целиком, Murphy целиком, PRML целиком — типичный способ
   потратить полгода и не подготовиться. Нужна явная маркировка «читать эти главы, остальное — справочник».

5. **Провал на «свежем слое».** Канон 2015–2020 (ResNet, BERT, XGBoost) знают, а слой 2022–2025
   (Chinchilla, LoRA, FlashAttention, PagedAttention, DPO, TIGER/semantic IDs) — нет. Именно там сейчас
   проходит граница middle / middle_plus.

6. **Не читают инженерные блоги компаний.** На вопрос «как бы ты построил ранжирование объявлений»
   отвечают абстракциями, хотя Авито, Ozon, Uber, Airbnb, Netflix публично описали свои решения.
   Каталог `eugeneyan/applied-ml` и хабы Авито/Ozon/X5/SberDevices закрывают это за 10–15 статей.

7. **A/B знают на уровне «t-тест».** Не знают SRM, guardrail-метрик, проблемы подглядывания,
   сетевых эффектов, CUPED. Это ровно содержание книги Kohavi, которую почти никто не открывал.

8. **Не умеют читать статью критически.** Не проверяют бейзлайны, бюджет обучения, воспроизводимость.
   Отсюда пункт 2 в предыдущем разделе. Хорошее лекарство — arXiv:2309.07602 и arXiv:2108.02497 (ML pitfalls).

9. **Отсутствие «единицы прочтения».** Кандидат не может за 3 минуты пересказать статью по схеме
   «проблема → что предложили → почему это работает → цена решения». Это тренируемый навык,
   и хендбук должен дать шаблон.

---

## Рекомендации для структуры глав хендбука по этой теме

### Р1. Отдельная глава «Канон: что читать и в каком порядке» в разделе 00-start

Не «список литературы в конце», а полноценная глава в начале, потому что первая проблема кандидата —
не отсутствие материалов, а их избыток. Структура главы:

- **Три трека по грейдам.** Junior-трек (~6 источников), middle-трек (~15), middle_plus-трек (~25).
  Явно: «если у тебя 4 недели — читай только это».
- **Правило одного якоря на тему.** Для каждой темы ровно один основной текст и 1–2 дополнения.
  Классика → ESL; DL → Goodfellow ч. II + Understanding Deep Learning; NLP → курс Войты + YSDA NLP;
  RecSys → RecSys-Course SB AI Lab; MLOps → Chip Huyen DMLS; A/B → Kohavi; Big Data → DDIA.
- **Русский канон отдельным блоком**, не как «локальная альтернатива», а как обязательная часть:
  учебник ШАДа, курс ODS, Воронцов, Дьяконов, DLS МФТИ, курс Ульянкина, RecTools/RePlay, хабы Авито/Ozon/X5/Sber.

### Р2. В каждой предметной главе — блок «Первоисточники» в фиксированном формате

Предлагаемый шаблон (одинаковый во всех главах, чтобы был предсказуем):

```
### Первоисточники главы
| Статья/книга | Год | Что именно отсюда | Грейд | must/opt |
```

Плюс подблок **«Что спросят по этому источнику»** — 2–4 реальных вопроса из банка выше.
Это и есть главная ценность: связь «источник ↔ вопрос ↔ грейд» нигде публично не собрана.

### Р3. Хронологическая шкала для каждого домена

Читателю нужно видеть не список, а линию развития, потому что вопросы на собесе почти всегда
формулируются как «а что было до / а почему отказались от».

- **Бустинг:** GBM (Friedman 2001) → XGBoost (2016) → LightGBM (2017) → CatBoost (2017).
- **Обучение НС:** Dropout (2014) → BatchNorm (2015) → ResNet (2015) → Adam (2014) → Tuning Playbook (2023).
- **NLP/LLM:** Attention (2017) → BERT (2018) → GPT-3 (2020) → InstructGPT (2022) → Chinchilla (2022) →
  LoRA (2021) → FlashAttention (2022) → LLaMA (2023) → vLLM/PagedAttention (2023) → DPO (2023) → RAG-эра (2024+).
- **RecSys:** iALS/BPR (2008–2012) → Wide&Deep (2016) → YouTube DNN (2016) → NCF (2017) → DeepFM (2017) →
  DIN (2018) → SASRec (2018) → PinSage (2018) → BERT4Rec (2019) → LightGCN (2020) →
  ревизия бейзлайнов (2023) → TIGER/semantic IDs (2023+).
- **MLOps:** Rules of ML (2017) → Hidden Technical Debt (2015) → ML Test Score (2017) →
  Michelangelo (2017) → DMLS (2022) → AI Engineering (2025).

### Р4. Формат «карточки статьи» — шаблон разбора

Дать читателю воспроизводимую единицу и использовать её во всём хендбуке:

```
**Название, год, организация.**
Проблема: <1 предложение>
Решение: <1–2 предложения, механизм, а не эффект>
Почему работает: <1–2 предложения>
Цена: <что ухудшилось: память, латентность, сложность реализации>
Что спрашивают: <1–3 вопроса>
Что говорить, если не читал: <честная стратегия>
```

Последняя строка особенно важна: она отличает хендбук от списка ссылок.

### Р5. Явные «стоп-границы» по объёмным книгам

Отдельная врезка «сколько читать»:
- ESL — гл. 3, 7, 9, 10, 15 (остальное — справочник).
- Goodfellow — ч. II (гл. 6–9); ч. III устарела.
- Boyd — гл. 2–3, 5, 9–10.
- PRML — гл. 1–4, 9.
- DDIA — гл. 3, 4, 6, 7, 11.
- Kohavi — гл. 1–4, 17–22 (метрики, SRM, дисперсия).
- Murphy — только как энциклопедия, не линейно.

### Р6. Блок «Индустриальные кейсы» в главах system design и RecSys

Свести в одну таблицу верифицированные кейсы (Airbnb ×2, Netflix ×3, Booking.com, Lyft, Uber ×2,
Авито ×3, Ozon, Uber Michelangelo) и для каждого дать «какой вопрос собеса он закрывает».
Каталог `eugeneyan/applied-ml` — основной поставщик, `chiphuyen/case-studies.md` — уже отобранный минимум.

### Р7. Раздел «Как поддерживать актуальность»

Практический, а не декларативный: конкретные ленты и как ими пользоваться —
блоги Lilian Weng и Eugene Yan, хабы Авито / Ozon Tech / X5 Tech / SberDevices на Habr, трекеры ODS,
`ml-engineering` Bekman, релиз-ноты vLLM/PyTorch. Плюс правило: одна статья в неделю, разобранная
по карточке из Р4, за год даёт ~50 первоисточников — больше, чем у 95% кандидатов.

### Р8. Единая рубрика грейдов, заимствованная из верифицированного источника

`alexeygrigorev/data-science-interviews` использует 👶 / ⭐ / 🚀. Предлагаю в хендбуке:
`junior` / `middle` / `middle_plus` с тем же смыслом и явным маппингом на источники:
junior — учебник ШАДа + ODS + ISLR; middle — ESL + Goodfellow ч.II + DMLS + Kohavi;
middle_plus — статьи 2022–2025 + efficient-dl-systems + Michelangelo + TIGER/FlashAttention/PagedAttention.

### Р9. Отдельная страница «Официальные материалы компаний»

Уникальная ценность, которую почти никто не собирает:
`Tinkoff/career/interview/sections/platform-ml.md` (официальный список литературы Т-Банка),
`https://www.tbank.ru/career/it/interview/ml/`, раздел Company-Specific Resources
в `Extremesarova/ds_resources`, `slgero/testovoe` (реальные тестовые по компаниям).
Это то, что кандидат не найдёт сам, и это самый прямой сигнал о том, что от него ждут.
