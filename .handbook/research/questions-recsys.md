# RecSys (рекомендательные системы) — research dump

> Дата сбора: 2026-07-26.
> Область: рекомендательные системы для MLE/DS-собеседований (junior → middle+), русскоязычный и англоязычный рынок.
>
> **Важное методологическое замечание про источники.** В этой сессии исходящий HTTPS шёл через политику egress-прокси,
> которая пропускала только `github.com` / `raw.githubusercontent.com`. Все остальные хосты (habr.com, arxiv.org,
> education.yandex.ru, aman.ai, eugeneyan.com, evidentlyai.com, proglib.io, enigmai.ru, jointaro, teamblind, medium и т. д.)
> отдавали 403 от прокси. Поэтому ниже источники честно разделены на две группы:
> **(A) полностью вычитанные страницы** (я видел их содержимое целиком) и
> **(B) страницы, содержимое которых я видел только через выдержки/цитаты поискового движка** (WebSearch реально читает
> страницу и возвращает цитаты, но я не видел документ целиком).
> Ничего, чего не было ни в (A), ни в (B), в этот файл не попало. Придуманных URL и придуманных вопросов здесь нет.

---

## Источники, которые реально просмотрены

### A. Полностью вычитанные страницы (fetch вернул содержимое)

| # | URL | Что там |
|---|-----|---------|
| A1 | https://raw.githubusercontent.com/ixlander/interview-questions/main/all-real-questions.md | **Главный источник.** Банк «вопросов с реальных собеседований» на русском: 274 вопроса, раздел ML-RECSYS (37 шт.) и MLSD-GENERAL (22 шт.). Каждый вопрос помечен грейдом (Junior/Middle/Senior) и компанией: Ozon, VK, Wildberries, Самокат, Constructor, ZinBrains, Quantum One, Дром.ру, Сбер, Т-Банк, Яндекс, Mayflower, Infomedia, Waibee. |
| A2 | https://raw.githubusercontent.com/ixlander/interview-questions/main/README.md | Метаданные того же банка: 8 разделов (ML-GENERAL 45, ML-RECSYS 37, ML-CV 17, ML-NLP 10, MLSD-GENERAL 22, LANG-PYTHON 19, SQL-DATABASES 5, HR-SCREENING 42), перечень компаний (Avito, Яндекс, VK, Sber, Тинькофф, Wildberries, Ozon и др.). |
| A3 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/5%20Recommendations/5_syllabus.md | Русскоязычный 19-дневный курс-конспект по RecSys с явным блоком «Примеры вопросов, которые могут задать на собеседовании» на каждый день + развёрнутый пример ответа на MLSD-вопрос «design a movie recommender for Netflix-scale». |
| A4 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/5%20Recommendations/5_plan.md | План того же курса: I Введение, II CF, III MF (SVD/ALS/BPR), IV контент+гибрид, V LightGCN, VI Sequential/Generative (SASRec, BERT4Rec, ARGUS), VII Candidate Generation/ANN, VIII Filtering, IX Feature Engineering, X Scoring/Ranking (LTR, cascade), XI Post-processing (диверсификация, fairness), XII Explore-Exploit, XIII A/B и метрики. |
| A5 | https://github.com/Maha-Rossomaha/LLM_projects/tree/main/5%20Recommendations/1%20Theory | Список конспектов: Intro; EDA and Baselines; Basics; CF Basics; CF Models; MF: SVD and ALS; MF: BPR; Content Based and Hybrid; Ranking Task with BPR and WARP; LightGCN. |
| A6 | https://raw.githubusercontent.com/TheAndreyZakharov/IT-Interview-Question-Bank/main/RU/Questions_By_Topic_RU/%23%23%2014.%20Data%20-%20ML%20-%20Analytics.md | Русский банк вопросов, блок Data/ML/Analytics: рекомендательные системы, ранжирование, embeddings, feature store, feedback loops, offline vs online evaluation, interleaving/champion-challenger. |
| A7 | https://github.com/TheAndreyZakharov/IT-Interview-Question-Bank/tree/main/RU/Questions_By_Topic_RU | Оглавление банка: 20 тематических файлов (скрининг, поведенческое, архитектура и системный дизайн, Data-ML-Analytics, практические задачи и т. д.). |
| A8 | https://github.com/Devinterview-io/recommendation-systems-interview-questions | 50 вопросов «Recommendation Systems interview questions», из них 15 открыто в README (CF vs content-based, cold start, serendipity/novelty/diversity, MF, implicit vs explicit, user-based/item-based CF, kNN, ALS, SVD, association rules, гибриды, DL в рекомендациях). |
| A9 | https://github.com/LongxingTan/Machine-learning-interview/blob/main/02_ml/17_recommendation.md | Плотный конспект «推荐系统» под собес:召回/排序, двухбашенные модели, негативы (in-batch + logQ correction), i2i/u2i, семейство ранкеров (LR, GBDT, FM, FFM, DNN, Wide&Deep, DCN/DCNv2, DeepFM, DIN, xDeepFM, DIEN), cold start, position bias (IPW, позиция как фича, bias-модуль), long tail, offline/online несогласованность, метрики. |
| A10 | https://github.com/LongxingTan/Machine-learning-interview/blob/main/03_system/03_ml/recommendation.md | ML System Design для рекомендаций: воронка recall→ranking, функциональные/нефункциональные требования,粗排/精排/重排, фичи (dense/sparse/cross/sequence), метрики (MAP, NDCG / CTR, CVR, GMV), cold start, latency (real-time user emb, offline item emb, FAISS + PCA/PQ, parameter server). |
| A11 | https://github.com/LongxingTan/Machine-learning-interview/blob/main/03_system/03_ml/video_recommendation.md | Полный разбор YouTube-подобной задачи: latency <200 мс (идеально <100 мс), 100M видео / 100M DAU, двухстадийная воронка + reranking, two-tower, негативы (random с popularity^0.75, in-batch, hard negatives из грубого ранкера), `cosine(a,b_i) - log(p_i)` для подавления popularity bias, cold start. |
| A12 | https://github.com/LongxingTan/Machine-learning-interview/blob/main/03_system/03_ml/twitter_recommendation.md | Дизайн ленты: in-network / out-of-network кандидаты, MaskNet как ранкер, эвристики и фильтры (блокировки, NSFW, уже виденное), offline Recall@k / hit_rate, online CTR. |
| A13 | https://github.com/LongxingTan/Machine-learning-interview/tree/main/03_system/03_ml | Список MLSD-кейсов: ad_click, coupon_deliver, friend_recommedation, news_feed, poi_recommendation, recommendation, search_engine, twitter_recommendation, video_recommendation, video_search и др. |
| A14 | https://github.com/LongxingTan/Machine-learning-interview | Структура репо: 01_leetcode, 02_ml (ML breadth/depth, product sense, math), 03_system (OOD + ML system design), 04_bq, 05_case. |
| A15 | https://github.com/alirezadir/machine-learning-interviews/blob/main/src/MLSD/ml-system-design.md | 9-шаговая формула ML System Design (problem formulation → metrics → архитектурные компоненты → данные → фичи → модель и offline eval → prediction service → online testing/деплой → scaling/monitoring) + список типовых задач, где рекомендации доминируют. |
| A16 | https://github.com/alirezadir/machine-learning-interviews/blob/main/src/MLSD/mlsd-video-recom.md | Уточняющие вопросы кандидата («Use case? Homepage?», «Business objective?», «How many videos? 100 million», «Latency requirements — 200msec?»), offline precision@k/mAP/diversity, online CTR/watch time, воронка candidate generation → ranking → re-ranking, two-tower + ANN. |
| A17 | https://github.com/alirezadir/machine-learning-interviews/blob/main/src/MLSD/mlsd-metrics.md | Формулировки Recall@k, Precision@k, MRR, mAP, DCG/nDCG + онлайн-метрики (CTR, conversion rate, bounce rate, engagement rate, time on page). |
| A18 | https://github.com/alirezadir/machine-learning-interviews/tree/main/src/MLSD | Полный список MLSD-файлов (ads-ranking, event-recom, game-recom, newsfeed, pymk, search, typeahead, video-recom, harmful-content, metrics, feature-eng, modeling-popular-archs …). |
| A19 | https://github.com/km1994/RES-Interview-Notes | Оглавление китайского банка «面试题» ровно по RecSys: введение (14 вопросов), CF, MF/隐语义, LR, FM, FFM, GBDT+LR, DL-блок (AutoRec, NeuralCF, Deep Crossing, Wide&Deep, FM+DL), «落地», «многоаспектный взгляд», «методы оценки», «инженерное внедрение». |
| A20 | https://github.com/HirahTang/Interview-Notes | Список вопросов по 推荐/搜索/广告: UserCF vs ItemCF, CTR vs CVR и ESMM, повторы в рекомендациях, распределение фич между wide и deep, подавление хайповых айтемов на этапе отбора, multi-path recall, метрики recall-модели, cold start, embedding-методы, offline/online расхождение, AUC и чувствительность к сэмплингу, различие рекомендаций/поиска/рекламы. |
| A21 | https://github.com/wangshusen/RecommenderSystem | Оглавление индустриального курса: ItemCF, Swing, UserCF, дискретные признаки, matrix completion, two-tower (обучение / позитивы и негативы / online serving / self-supervised), deep retrieval, доп. каналы отбора, exposure filtering; ranking (multi-objective, MMoE, score fusion, watch-time modeling, три-башенный грубый ранкер); FM, DCN, LHUC, SENet/FiBiNet; sequence modeling (DIN, SIM); diversity (MMR, DPP); cold start (метрики, отбор, кластерный recall, Look-Alike, traffic control, A/B для cold start). |
| A22 | https://github.com/creyesp/Awesome-recsys | Карта тем и канона: implicit feedback CF, BPR, item2vec, Wide&Deep, YouTube DNN, NCF, BERT4Rec, SSL for large-scale item rec, ItemSage; two-tower retrieval, LTR (pointwise/pairwise/listwise), графовые методы, RL, session-based; метрики (MAP@k, diversity, calibration); cold start, bias/fairness, multi-task, A/B; инструменты (TFRS, LightFM, implicit, RecBole, NVIDIA Merlin, Cornac, Metarank). |
| A23 | https://github.com/Doragd/Algorithm-Practice-in-Industry | Индустриальный сборник статей по поиску/рекламе/рекомендациям: recall и ranking модели, cold start, multi-task, GNN, мультимодальность, causal inference, инфраструктура (Redis, embedding-системы). Собственно «面经» там нет — это сборник практик. |
| A24 | https://github.com/Tinkoff/career/blob/main/interview/sections/system-design-ml.md | Официальное описание секции ML System Design в Тинькофф/Т-Банке: кандидату дают задачу на дизайн; канва — формализация задачи и требований → декомпозиция на подзадачи → сбор данных → обсуждение ML-архитектур подзадач → деплой и тестирование. |
| A25 | https://github.com/epishchik/ML-Interview + https://github.com/epishchik/ML-Interview/blob/main/README.md | Русский банк вопросов на MLE (сильный крен в CV/генеративные модели), но полезен как образец рубрикации: «Основы ML», «Метрики и оценка моделей», «Python», «Дополнительные темы». |
| A26 | https://raw.githubusercontent.com/Extremesarova/ds_resources/main/README.md | Русскоязычный список ресурсов для подготовки: курсы «Your First RecSys» / «Your Second RecSys by MTS» на ods.ai, репозиторий shashist/recsys-course, книга К. Фалька, «Recommenders: Best Practices», хендбук Яндекса по рекомендациям, Aman.AI GNN for RecSys, «Revisiting BPR». |
| A27 | https://raw.githubusercontent.com/khangich/machine-learning-interview/master/README.md | MVP-план подготовки к ML-интервью FAANG; раздел «Recommendations» и MLSD-кейсы (YouTube DNN, LinkedIn Feed Ranking, Instagram Explore, TikTok, Wide&Deep, Twitter timeline ranking). |
| A28 | https://github.com/slgero/testovoe | Сборник тестовых заданий на DS-позиции в РФ/СНГ (Diginetica, OLX-Hermes, МТС, Сбер, СКБ Контур, Gett, Wargaming, БКС и др.) — источник домашек, в т.ч. по ранжированию/рекомендациям. |
| A29 | https://raw.githubusercontent.com/anokhin/recsys-course-spring-2024/master/README.md | Русскоязычный вузовский курс по RecSys (программа лежит в папке slides; README подтверждает акцент на продакшн-архитектуре и «долгосрочном здоровье» рекомендаций). |

### B. Источники, содержимое которых я видел только через цитаты поискового движка (хост заблокирован egress-политикой)

| # | URL | Что оттуда реально процитировано |
|---|-----|----------------------------------|
| B1 | https://habr.com/ru/articles/993674/ | «Что спрашивают на собесах в 2025–2026: разбираем данные с 9 247 технических интервью» — аналитика по транскрипциям реальных интервью (сервис Энигма): кто, куда, на какие позиции, какие вопросы задают на теории. |
| B2 | https://habr.com/ru/articles/995600/ | «Реальные задачи с собеседований в Яндекс, VK, Ozon и Сбер» — вторая часть той же серии, про live-coding: 17 задач, 10 компаний, 5 стеков. |
| B3 | https://habr.com/ru/companies/yandex/articles/919058/ | ARGUS: как масштабировать рекомендательные трансформеры. 4 конфигурации трансформера от 3.2M до 1.007B параметров, контекст 8k событий, автоагрегатное моделирование пользовательской последовательности. |
| B4 | https://habr.com/ru/companies/yandex/articles/1037766/ | «От фич и каскадов к генеративной модели: как мы переосмыслили рекомендации с помощью ARGUS» — прямой переход «каскад фич → генеративная модель». |
| B5 | https://habr.com/ru/companies/click/news/1024506/ | ARGUS в Яндекс Рекламе: память рекомендательной системы увеличена до года / 8000 событий вместо «десятков дней и 256 действий». |
| B6 | https://habr.com/ru/companies/avito/articles/1004694/ | «Как мы улучшили рекомендации для пользователей Авито с помощью трансформенной персонализации»: эмбеддинги объявлений, скалярное произведение user-emb × item-emb. |
| B7 | https://habr.com/ru/companies/ozontech/articles/648231/ | Ozon Prod2Vec: единое векторное представление товаров (fastText/трансформеры для текста + CNN для картинок), избавление от зоопарка эмбеддингов. |
| B8 | https://habr.com/ru/companies/ozontech/articles/990518/ | Архитектура факторов ранжирования в runtime поиска Ozon: feature-meta-store, таблицы метаинформации по типам факторов, ML-модели (CatBoost) как факторы. |
| B9 | https://habr.com/ru/companies/ozontech/articles/750196/ | Ozon Tech meetup: система рекомендаций — отбор нескольких тысяч кандидатов под контекст полки, затем ранжирование 2000–3000 товаров по вероятности покупки; десятки рекомендательных полок. |
| B10 | https://habr.com/ru/companies/zvuk/articles/1002212/ | «Онлайн-оценка рекомендательных систем: метрики, которые говорят сейчас» (Звук): онлайн-метрики, novelty как «насколько новым для пользователя является предложенный трек». |
| B11 | https://habr.com/ru/companies/otus/articles/732842/ | «Метрики оценки для рекомендательных систем»: coverage, novelty, serendipity, diversity — определения и почему smотреть надо на несколько метрик сразу. |
| B12 | https://education.yandex.ru/handbook/ml/article/intro-recsys | Хендбук Яндекса, 9.1 «Введение в рекомендательные системы»: item2item / user2user CF и переход к матричным разложениям. |
| B13 | https://education.yandex.ru/handbook/ml/article/rekomendacii-na-osnove-matrichnyh-razlozhenij | 9.2 «Рекомендации на основе матричных разложений»: латентные векторы, SVD, SGD; «в чистом виде MF почти не используют для выдачи — используют для генерации кандидатов из сотен тысяч/миллионов айтемов». |
| B14 | https://education.yandex.ru/handbook/ml/article/kontentnye-rekomendacii | 9.3 «Контентные рекомендации»: factorization machines как способ соединить коллаборативный и контентный сигнал. |
| B15 | https://education.yandex.ru/handbook/ml/article/horoshie-svojstva-rekomendatelnyh-sistem | 9.4 «Хорошие свойства рекомендательных систем»: как оптимизация «неправильной» метрики порождает кликбейт; формализация удовлетворённости пользователя. |
| B16 | https://yandex.ru/jobs/interview/mldev | Официальная страница Яндекса «Как мы нанимаем ML-специалистов»: явно упомянуты high-level архитектура рекомендательной системы, метрики, данные, стадии рекомендательной системы и применимые на них модели, дизайн ранжирования, генерация кандидатов, проблемы вроде разнообразия. |
| B17 | https://www.jointaro.com/interviews/companies/yandex/experiences/ml-engineer-russia-june-2-2025-declined-offer-positive-ee9e15b8/ | Отчёт кандидата про ML Engineer в Яндекс (Россия): 3 общих раунда — leetcode, ML-теория, recsys; затем по интервью на каждую продуктовую команду; спрашивали про **смещения (biases) при проектировании рекомендательной системы и способы их избежать**. |
| B18 | https://enigmai.ru/interview/wildberries/ds-wildberries/ | Гайд по DS-собеседованию в Wildberries: middle/senior в ранжирование, логистику, рекламу; тренд — переход от классического ML к LLM-агентам и графовым сетям; часто просят спроектировать систему, работающую **не в батче, а в онлайн-потоке**. |
| B19 | https://kariernik.ru/blog/sobesedovanie-ml-engineer-avito | Гайд по ML Engineer в Авито: поиск/ранжирование/рекомендации, антифрод, модерация, динамическое ценообразование, CV; стек Python, PyTorch, CatBoost, Kubernetes, Kafka, ClickHouse; блоки подготовки — Python+ML+ranking, K8s/Docker, MLOps и feature stores, system design, мониторинг и деплой. |
| B20 | https://habr.com/ru/company/ods/blog/698698/ | ODS: «Что я бы хотел знать про ML System Design раньше» — «не решать задачу сразу, а задать уточняющие вопросы: какую бизнес-метрику оптимизируем». |
| B21 | https://kolodezev.ru/mlsysd2.html | Лекция Д. Колодезева по ML System Design: функциональные требования, ограничения по времени ответа, RPS, CPU/RAM. |
| B22 | https://habr.com/ru/companies/yandex/articles/475584/ | «Как проходят секции по машинному обучению на собеседованиях в Яндекс». |
| B23 | https://habr.com/ru/articles/704128/ | «Как устроен процесс найма и собеседований на позицию Machine Learning Engineer»: ML System Design = путь ML-задачи от старта до прода. |
| B24 | https://habr.com/ru/companies/prequel/articles/573880/ | «Рекомендательные системы: проблемы и методы решения. Часть 2» — Learn to Rank и методы улучшения ранжирования. |
| B25 | https://habr.com/ru/companies/surfingbird/articles/168733/ | «Рекомендательная система: введение в проблему холодного старта» — разделение на cold start пользователя и cold start айтема. |
| B26 | https://habr.com/ru/companies/yandex/articles/857068/ | «ML-тренды рекомендательных технологий: шесть приёмов» — сэмплированный софтмакс с logQ-коррекцией (смесь in-batch и равномерных негативов), шум в неявном фидбэке (положительный implicit + отрицательный explicit). |
| B27 | https://eugeneyan.com/writing/counterfactual-evaluation/ | Counterfactual evaluation для рекомендаций: off-policy оценка на логах, IPS как основа всех counterfactual-оценщиков, нужны propensities. |
| B28 | https://www.evidentlyai.com/ranking-metrics/evaluating-recommender-systems | «10 metrics to evaluate recommender and ranking systems» — precision@k / recall@k / MAP / NDCG / MRR / coverage / novelty / serendipity / personalization. |
| B29 | https://aman.ai/recsys/metrics/ и https://vinija.ai/recsys/metrics/ | Справочники по метрикам и лоссам RecSys; rank-aware (MAP/MRR/NDCG) vs non-rank-aware (P@k/R@k). |
| B30 | https://www.yuan-meng.com/posts/mle_interviews_2.0/ | Гид по MLE-интервью (2024–2025): практические болевые точки RecSys, которые спрашивают на deep dive — **cold start, positional bias, diversity (дедуп и реранк по теме/автору), value models (веса целей в multi-objective ранжировании)**; совет читать по 1–2 статьи на каждую тему. |
| B31 | https://medium.com/data-science/two-tower-networks-and-negative-sampling-in-recommender-systems-fdc88411601b | Two-tower + негативное сэмплирование (Roizner): in-batch/out-of-batch негативы, logQ-коррекция, hard negatives. |
| B32 | https://research.google/pubs/mixed-negative-sampling-for-learning-two-tower-neural-networks-in-recommendations/ | Mixed Negative Sampling: подмешивание равномерных негативов к in-batch. |
| B33 | https://arxiv.org/abs/2305.05065 (Recommender Systems with Generative Retrieval, TIGER) | TIGER: RQ-VAE квантует контентный эмбеддинг айтема в semantic ID; двухстадийное обучение (сначала RQ-VAE, потом генеративная модель); генеративный retrieval вместо ANN. |
| B34 | https://arxiv.org/pdf/2507.22224 | «Generative Recommendation with Semantic IDs: A Practitioner's Handbook». |
| B35 | https://arxiv.org/pdf/2604.03949 | «Semantic IDs for Recommender Systems at Snapchat: Use Cases, Technical Challenges, and Design Choices» — индустриальные грабли семантических ID. |
| B36 | https://www.emergentmind.com/topics/hierarchical-sequential-transduction-unit-hstu | HSTU (Meta, 2024): трансдьюсер до 1.5T параметров, NLP-подобные scaling laws для рекомендаций; унификация retrieval и ranking как sequence prediction. |
| B37 | https://arxiv.org/pdf/2507.06507 | GR-LLMs: обзор генеративных рекомендаций на LLM (LLM-as-ranker, семантические идентификаторы, cold start). |
| B38 | https://arxiv.org/pdf/2010.03240 (Bias and Debias in Recommender System: A Survey) | Таксономия смещений и методы: IPS (взвешивание по позиционно-зависимой propensity), error-imputation (EIB), doubly robust (DR); главная проблема IPS — корректная спецификация propensity. |
| B39 | https://arxiv.org/pdf/1809.03672 (DIEN) | DIN моделирует разнообразие интересов через attention к таргет-айтему; DIEN добавляет GRU-энкодер интересов + GRU с attentional update gate для эволюции интересов. |
| B40 | https://www.pingcap.com/article/approximate-nearest-neighbor-ann-search-explained-ivf-vs-hnsw-vs-pq/ , https://bigdataboutique.com/blog/hnsw-vs-ivfflat-how-to-choose-the-right-vector-index , https://markaicode.com/benchmarks/faiss-production-benchmark-latency/ | HNSW vs IVF vs IVF-PQ: HNSW точнее и быстрее по p95 (0.42 мс против 0.83 мс на 10M векторов), но требует ~3× RAM и долго строится; IVF/IVF-PQ дешевле по памяти и быстро перестраивается. |
| B41 | https://arxiv.org/pdf/2008.07146 (Open Bandit Dataset and Pipeline) / https://sites.google.com/cornell.edu/recsys2021tutorial | Off-policy evaluation, SNIPS, туториал RecSys 2021 по counterfactual learning/evaluation. |
| B42 | https://arxiv.org/html/2307.15053 | NDCG как off-policy метрика для top-n рекомендаций; фундаментальный mismatch между «next-item» офлайн-метриками и онлайн-метриками (CTR). |
| B43 | https://habr.com/ru/articles/792994/ | «Шпаргалка по рекомендательным системам» (Хабр). |
| B44 | https://habr.com/ru/articles/1019070/ | «Рекомендательные системы для бизнеса — мой опыт разработчика»: практика систем ранжирования, метрики качества, оптимизация. |
| B45 | https://ai.itmo.ru/blog/classic-ml-sobesedovanie-ml-engineer | «Classic ML на собеседовании»: ранжирование как отдельный блок (pointwise/pairwise/listwise), «в рекомендательных системах важны одни метрики, в прогнозе спроса — другие». |
| B46 | https://ods.ai/tracks/recsys-course2021 (через A26) | «Your Second RecSys by MTS» — базовый русскоязычный курс, на который ссылаются при подготовке. |

---

## Вопросы с собеседований

Легенда грейдов: `junior` — ожидается от стажёра/джуна; `middle` — типовой мидловый вопрос; `middle_plus` — вопрос «на вырост», где ждут trade-off'ов, продовых деталей и своего опыта.
Грейды из источника A1 отображены так: Junior → `junior`, Middle → `middle`, Senior → `middle_plus`.

### 1. Постановка задачи и продуктовое мышление

1. **«Расскажите подробно про рекомендательный проект: постановка задачи, тестирование, проблемы.»** — `middle` — Quantum One — A1
2. **«Расскажите про ваш последний опыт с рекомендательными системами: что делали, как, какие результаты?»** — `middle` — ZinBrains — A1
3. **«Расскажите про ваш личный вклад в задачи рекомендаций: item-to-item и transformer-based.»** — `middle` — Дром.ру — A1
4. **«Какую бизнес-метрику оптимизировать в рекомендательной системе коротких видео? Среднее время сессии или суммарное?»** — `middle_plus` — VK — A1
5. **«Как бы вы измеряли успех рекомендательной системы?»** — `middle` — A6
6. **«Как бы вы объяснили роль рекомендательных систем в современных сервисах?»** — `junior` — A3 (День 1)
7. **«Что такое recommendation systems?» / «Какие основные подходы к рекомендательным системам вы знаете?»** — `junior` — A6
8. **"What is a recommendation system and how does it work?"** — `junior` — A8
9. **«Какие модели и подходы рекомендательных систем вы знаете?»** — `middle` — A1 (RecSys-секция, компания не указана)
10. **«Назовите основные проблемы рекомендательных систем и способы их решения.»** — `middle` — Самокат — A1
11. **"What are the main challenges in building recommendation systems?"** — `middle` — A8
12. **«推荐系统 与 搜索、广告 的 异同?» / «Advertising vs recommendation vs search system differences»** (чем рекомендации отличаются от поиска и рекламы) — `middle_plus` — A19, A20
13. **«Какую задачу мы вообще решаем: предсказание рейтинга, предсказание клика или ранжирование? Почему?»** (переформулировка «ML objective options: max P(watch|U,C) vs max expected total watch time») — `middle` — A16, A11
14. **«Business objective? Increase user engagement (play, like, click, share), purchase?»** (уточняющий вопрос, который должен задать сам кандидат) — `middle` — A16
15. **«Какую бизнес-метрику оптимизируем?»** — обязательный уточняющий вопрос в ML System Design — `middle` — B20
16. **«Рекомендательные системы: какие проблемы возникают, если оптимизировать не ту метрику (кликбейт)?»** — `middle_plus` — B15

### 2. Коллаборативная фильтрация, implicit feedback

17. **«Что такое collaborative filtering?»** — `junior` — A6
18. **«Что такое content-based recommendation?»** — `junior` — A6
19. **"Can you explain the difference between collaborative filtering and content-based recommendations?"** — `junior` — A8
20. **"Explain user-based and item-based collaborative filtering."** — `junior`/`middle` — A8
21. **«UserCF vs ItemCF: сценарии применения»** — `middle` — A20 (см. также A19, A21)
22. **«Почему memory-based CF страдает при холодном старте?»** — `middle` — A3 (День 2)
23. **«Какая метрика сходства лучше для бинарных предпочтений?»** (cosine / Jaccard / Swing) — `middle` — A3 (День 2), A21
24. **«Что такое implicit feedback и explicit feedback?»** — `junior` — A6
25. **"Describe the concept of implicit versus explicit feedback in the context of recommendation systems."** — `junior` — A8
26. **«Как обрабатывается неявный фидбэк в MF?»** (confidence weighting, все ненаблюдаемые — негативы с малым весом) — `middle` — A3 (День 3)
27. **«Как работает Implicit ALS (Alternating Least Squares) для неявного фидбека?»** — `middle` — ZinBrains — A1
28. **"What is the purpose of using Alternating Least Squares (ALS) in recommendation systems?"** — `middle` — A8
29. **«В сигнале много шума: за положительным implicit-фидбэком может следовать отрицательный explicit. Как с этим жить?»** — `middle_plus` — B26
30. **"How would you implement a recommendation system using the k-NN algorithm?"** — `junior` — A8
31. **«Explain the concept of a recommendation system using association rule mining.»** / «Co-purchase analysis, ассоциативные правила» — `middle` — A8, A1 (Quantum One)
32. **«Как определяли совместимость категорий товаров для рекомендаций?»** — `middle` — Quantum One — A1
33. **«What is a hybrid recommendation system and when would you use it?»** — `middle` — A8
34. **«Что такое user profile и item profile в рекомендательной системе?»** — `junior` — A8

### 3. Матричная факторизация: SVD, ALS, BPR, iALS, FM

35. **«Расскажите про SVD-разложение и как оно используется в рекомендательных системах.»** — `middle` — VK — A1
36. **"Can you describe the Singular Value Decomposition (SVD) and its role in recommendations?"** — `middle` — A8
37. **«Чем truncated SVD отличается от "SVD" в рекомендациях? Почему классический SVD не применим к матрице с пропусками?»** (вытекает из A1 #9: «Truncated SVD (k компонент) даёт low-rank приближение матрицы рейтингов») — `middle_plus` — A1, B13
38. **"How do matrix factorization techniques work in recommendation engines?"** — `middle` — A8
39. **«Что такое matrix factorization?»** — `junior` — A6
40. **«Чем отличается оптимизация MSE от BPR?»** — `middle` — A3 (День 3)
41. **«В чём разница между BPR loss и WARP loss?»** — `middle_plus` — ZinBrains — A1
42. **«Почему ALS масштабируется лучше SGD на миллионах пользователей? Как его параллелят?»** (из ответа A1 #9 про масштабируемость ALS) — `middle_plus` — VK — A1
43. **«隐语义模型 /矩阵分解: принцип, плюсы и минусы»** — `middle` — A19
44. **«FM vs matrix factorization: сходства и различия»** — `middle` — A20
45. **«FM и FFM: что это и в чём разница»** — `middle` — A19, A20
46. **«GBDT + LR: зачем такая связка в рекомендациях/CTR»** — `middle` — A19
47. **«Factorization machines как способ соединить коллаборативный и контентный сигнал»** — `middle_plus` — B14
48. **«Почему MF в чистом виде почти не используют для финальной выдачи, а используют для генерации кандидатов?»** — `middle_plus` — B13

### 4. Контентные подходы, эмбеддинги, item2vec, мультимодальность

49. **«Как строили эмбеддинги товаров для рекомендательной системы?»** — `middle` — Quantum One — A1
50. **«Какие ограничения у контентного метода?»** — `middle` — A3 (День 5)
51. **«Когда Item2Vec даёт преимущество над TF-IDF?»** — `middle` — A3 (День 5)
52. **«Что такое embedding? Где используются embeddings? Почему embeddings полезны для категориальных признаков и текста?»** — `junior` — A6
53. **«Что такое representation learning?»** — `middle` — A6
54. **«Common embedding methods / как эмбеддинги встраиваются в рекомендации»** — `middle` — A20
55. **«Как использовать мультимодальные фичи (текст + картинки) товаров для улучшения ранжирования?»** — `middle` — Constructor — A1 (ожидают BM25 по описанию, sentence-transformers/BERT, CLIP-эмбеддинги, офлайн-предрасчёт)
56. **«Мультимодальные эмбеддинги: визуальная часть через fine-tuned CV-модель (CLIP/Fashion-CLIP), contrastive loss на позитивах и hard negatives»** — `middle` — Quantum One — A1
57. **«Как закодировать товар с 7000 разнородными атрибутами для нейросетевой модели рекомендаций?»** — `middle_plus` — Ozon — A1
58. **«Как построить эмбеддинг пользователя на основе его последовательности действий?»** — `middle_plus` — Ozon — A1
59. **«Как объединить эмбеддинги пользователя и товара для предсказания релевантности?»** (dot product для ANN vs interaction network `[user; item; user*item] → MLP`) — `middle_plus` — Ozon — A1
60. **«Как вы работали с ограничением размерности эмбеддингов (256) в OpenSearch?»** — `middle` — Waibee — A1
61. **«Item2Vec использовался в промышленных системах — Авито улучшил рекомендации похожих объявлений с помощью Item2Vec. Как бы вы это воспроизвели?»** — `middle` — A3
62. **«Prod2Vec: как построить единый эмбеддинг товара из текста (fastText/трансформеры) и картинок (CNN), чтобы не плодить зоопарк эмбеддингов?»** — `middle_plus` — Ozon — B7

### 5. Two-tower / DSSM / candidate generation / ANN

63. **«Как использовать контентные и коллаборативные embeddings для candidate generation в RecSys?»** — `middle` — VK — A1
64. **«Как реализовать ANN-поиск масштабируемо?»** — `middle` — A3 (День 6)
65. **«В чём разница между sparse и dense retrieval?»** — `middle` — A3 (День 6)
66. **«Как работает индекс IVF (Inverted File Index) в библиотеке FAISS?»** — `middle` — ZinBrains — A1 (ожидают: k-means разбивает пространство на ячейки, nprobe — компромисс скорость/точность)
67. **«HNSW или IVF-PQ: что выберете и почему?»** (память vs recall vs скорость перестроения) — `middle_plus` — вытекает из A1 (#10 «ANN-поиск (HNSW или IVF-PQ в FAISS)»), детали в B40
68. **«Почему двухбашенная модель позволяет быстро отбирать кандидатов?»** (башни независимы; item-башня считается офлайн, user-башня — в рантайме; на запрос считается один вектор пользователя + ANN) — `middle` — A9
69. **«Почему в two-tower нельзя использовать cross-фичи user×item?»** — `middle_plus` — вытекает из A1 (#MLSD-8, interaction network vs dot product), A9, A11
70. **«Как формировать негативы для двухбашенной модели?»** — `middle_plus` — A9, A11, A21 (простые негативы из всего каталога; hard negatives из этапа грубого ранжирования; in-batch негативы с logQ-коррекцией)
71. **«Что такое logQ-коррекция и зачем она нужна?»** — `middle_plus` — A9, A11 (`cosine(a, b_i) − log(p_i)` при обучении, чистый cosine на инференсе), B26, B31
72. **«Зачем нужен multi-path recall (несколько каналов отбора кандидатов)?»** — `middle` — A20, A10 («ensemble retrieval from different models (rule, filtering, nn)»)
73. **«Какие метрики у recall-модели (модели отбора кандидатов)?»** — `middle` — A20, A21
74. **«Как подавлять хайповые/популярные айтемы на этапе отбора кандидатов?»** — `middle_plus` — A20
75. **«Deep retrieval / self-supervised two-tower — зачем и когда?»** — `middle_plus` — A21
76. **«Exposure filtering: как не показывать то, что уже показывали?»** (Bloom-фильтры и т. п.) — `middle` — A21
77. **«Как обеспечить отбор ~200 кандидатов за <20 мс?»** — `middle_plus` — A3 (пример эталонного ответа: Faiss-индекс, шардирование по item_id)

### 6. Ранжирование и learning-to-rank

78. **«Почему нельзя просто ранжировать по вероятности бинарного классификатора? В чём преимущество pairwise ranking?»** — `middle_plus` — VK — A1 (ожидают: «скоры не калиброваны друг относительно друга»)
79. **«Почему NDCG нельзя напрямую оптимизировать как loss? Какие альтернативы?»** — `middle_plus` — VK — A1 (ожидают LambdaRank: аппроксимация градиента через ΔNDCG при свопе пары)
80. **«Сравните pointwise и pairwise подходы в ранжировании: качество, скорость, метрики.»** — `middle` — Самокат — A1
81. **«Чем pointwise отличается от pairwise подходов в LTR?»** — `middle` — A3 (День 8)
82. **«Что такое pairwise, pointwise и listwise ranking?»** — `junior`/`middle` — A6
83. **«Какие типы loss-функций используются в задачах ранжирования?»** — `middle` — ZinBrains — A1 (pointwise MSE/BCE, pairwise BPR/LambdaRank, listwise ListNet/LambdaMART)
84. **«Какие loss functions используются в ranking?»** — `middle` — A6
85. **«Что такое learning to rank?»** — `junior` — A6
86. **«Что такое ranking-задачи? Чем ranking отличается от обычной классификации?»** — `junior` — A6
87. **«Какую модель выбрать для ранжирования и почему?»** — `middle` — A3 (День 8)
88. **«Почему выбрали Pointwise loss вместо Listwise для ранкера?»** — `middle` — Дром.ру — A1
89. **«Есть ли опыт с трансформерными моделями для ранжирования?»** — `middle` — Constructor — A1
90. **«Какие фичи использовались в модели ранжирования рекомендаций?»** — `middle` — Quantum One — A1 (item-фичи: цена, категория, бренд, популярность, CTR; cross-фичи: косинус эмбеддингов user-item, co-occurrence)
91. **«Как учесть контекст сессии пользователя при ранжировании? Например, подбор аксессуаров к уже выбранному товару.»** — `middle_plus` — Constructor — A1
92. **«Как оптимизировать ранжирование на маржу/выручку, а не просто на количество продаж?»** — `middle_plus` — Constructor — A1 (reweighting таргета по цене, oversampling дорогих товаров)
93. **«Как собирать таргет для задачи ранжирования в поиске?»** — `middle` — Constructor — A1
94. **«Что такое многоцелевое ранжирование и как сливать скоры разных голов (score fusion)?»** — `middle_plus` — A21, A9
95. **«MMoE: зачем нужна multi-gate mixture-of-experts в ранжировании?»** — `middle_plus` — A21
96. **«Как моделировать watch time / длительность просмотра, а не только клик?»** — `middle_plus` — A21, A11
97. **«Что такое 粗排 / 精排 / 重排 (грубое, точное и пере-ранжирование) и почему нужны три стадии?»** — `middle_plus` — A10, A21 (три-башенный грубый ранкер)
98. **«CTR-модель vs CVR-модель: в чём разница; что такое ESMM?»** — `middle_plus` — A20
99. **«Как распределять фичи между wide- и deep-частями Wide&Deep?»** — `middle_plus` — A20
100. **«Расскажите про LS-PLM / MLR как модель рекомендаций»** — `middle_plus` — A20
101. **«Зачем дискретизировать непрерывные признаки перед LR?»** — `middle` — A20
102. **«Как построить ROC-кривую; как AUC ведёт себя при сэмплировании негативов?»** — `middle` — A20

### 7. Нейросетевые архитектуры рекомендаций (DL-канон)

103. **«Какие нейросетевые архитектуры для рекомендаций вы знаете?»** — `middle` — Ozon — A1
104. **"Describe the use of deep learning in recommendation systems."** — `middle` — A8
105. **«Расскажите про AutoRec / NeuralCF / Deep Crossing / Wide&Deep / FM+DL»** — `middle` — A19 (блок «推荐系统深度学习篇»)
106. **«DCN / DCNv2 / DeepFM / xDeepFM: чем отличаются способы моделировать пересечения признаков?»** — `middle_plus` — A9
107. **«DIN: как attention к таргет-айтему решает проблему разнообразия интересов?»** — `middle_plus` — A9, A21, B39
108. **«DIEN: чем отличается от DIN и зачем два GRU?»** — `middle_plus` — A9, B39
109. **«SIM: как работать с очень длинной историей пользователя (десятки тысяч событий)?»** — `middle_plus` — A21
110. **«LHUC, SENet, FiBiNet — что это и зачем в ранжировании?»** — `middle_plus` — A21
111. **«DLRM: как устроена модель, где узкое место (embedding tables)?»** — `middle_plus` — A22, B39-контекст
112. **«MaskNet как ранкер ленты — что за модель?»** — `middle_plus` — A12

### 8. Sequential / transformer-based рекомендации

113. **«В чём разница между SASRec и BERT4Rec?»** — `middle` — Ozon — A1 (unidirectional causal next-item vs bidirectional masked item prediction)
114. **«Проведите аналогию SASRec/BERT4Rec с GPT/BERT в NLP.»** — `middle` — Ozon — A1
115. **«Расскажите про реализацию трансформер-based рекомендера (SASRec): данные, обучение, результаты.»** — `middle_plus` — ZinBrains — A1
116. **«Что такое GRU4Rec и когда session-based подход уместнее классического CF?»** — `middle` — A22 (session-based recommendations), A4
117. **«Как масштабируются рекомендательные трансформеры? Есть ли scaling laws?»** — `middle_plus` — B3, B36 (ARGUS: 3.2M → 1.007B параметров, контекст 8k событий; HSTU: до 1.5T, NLP-подобные scaling laws)
118. **«Как перейти от каскада "фичи + GBDT" к генеративной модели пользовательской последовательности?»** — `middle_plus` — Яндекс — B4
119. **«Как увеличить "память" рекомендательной системы с десятков дней/256 действий до года/8000 событий и что при этом ломается?»** — `middle_plus` — Яндекс Реклама — B5
120. **«Как Авито использует трансформенную персонализацию: user-эмбеддинг × item-эмбеддинг?»** — `middle_plus` — Авито — B6

### 9. Графовые рекомендации

121. **«Почему LightGCN проще классических GCN?»** — `middle_plus` — A3 (День 4)
122. **«Как решить проблему холодного старта в LightGCN?»** — `middle_plus` — A3 (День 4)
123. **«Сравните метрики LightGCN (Recall@10, nDCG@10) с ALS — что и почему выигрывает?»** — `middle_plus` — A3 (практическое задание того же курса)
124. **«Графовые методы в рекомендациях: PinSage/GNN — когда оправданы?»** — `middle_plus` — A22, A23, A26 (Aman.AI GNN for RecSys)
125. **«Как графовые свёртки усиливают popularity bias?»** — `middle_plus` — B38-контекст (arXiv 2305.14886, найдено в выдаче по popularity bias)

### 10. Офлайн-метрики

126. **«Расскажите о метриках качества ранжирования: Precision@K, Recall@K, NDCG, MRR.»** — `middle` — Wildberries — A1
127. **«Какие метрики ранжирования вы знаете?»** — `middle` — Ozon — A1
128. **«Какие метрики ранжирования вы знаете и в чём их различия?»** — `middle` — Самокат — A1
129. **«Какие метрики используются для оценки ранжирования?»** — `junior` — Constructor — A1
130. **«Как считается метрика NDCG?»** — `middle` — ZinBrains — A1 (`DCG = Σ rel_i / log2(i+1)`, нормировка на IDCG)
131. **«В чём разница между MAP и NDCG?»** — `middle` — Самокат — A1
132. **«В чём разница между метриками NDCG и MAP в ранжировании?»** — `middle` — ZinBrains — A1 (MAP — бинарная релевантность, NDCG — градуированная)
133. **«Какие метрики используют в рекомендательных системах?»** — `junior` — A6
134. **«Почему не используется Accuracy для оценки рекомендателя?»** — `junior`/`middle` — A3 (День 11)
135. **«Какая метрика важнее для Netflix: Precision@K или Recall@K?»** — `middle` — A3 (День 11)
136. **«Когда MRR — плохая метрика?»** (если надо вернуть ~10 объектов, один релевантный на 1-й позиции даёт MRR=1.0 при девяти мусорных) — `middle_plus` — B29
137. **«Что такое coverage, novelty, serendipity, diversity и чем они отличаются?»** — `middle` — A8 («Discuss the importance of serendipity, novelty, and diversity»), B10, B11, B28
138. **«Intra-list similarity и coverage — как их считать?»** — `middle_plus` — A3 (День 10)
139. **«Как выбрать K в метриках @K и почему офлайн-метрика на K=10 может не согласовываться с K=100?»** — `middle_plus` — вытекает из A17, B42
140. **«Метрики оценки recall-стадии отличаются от метрик ранжирующей стадии — чем именно?»** — `middle_plus` — A20, A21 (в cold-start блоке отдельные метрики)
141. **«RMSE / MSE / MAE в рекомендациях: когда они вообще уместны?»** — `junior` — A20

### 11. Онлайн-оценка, A/B, offline↔online расхождение

142. **«Какие офлайн и онлайн метрики использовать для рекомендаций? Как проводить A/B?»** — `middle` — Ozon — A1
143. **«Если A/B тест не показывает разницы по основной метрике (GMV), что делать?»** — `middle` — Самокат — A1 (проверить статистическую мощность, взять прокси-метрики CTR/watch time, сегментацию, длительность)
144. **«У нас новый алгоритм дал +5% офлайн precision. Раскатывать ли?»** — `middle` — A3 (День 12)
145. **«Как рассчитать минимальный размер выборки для A/B-теста?»** — `middle` — A3 (День 12)
146. **«Как проводить A/B тестирование модели так, чтобы не навредить бизнесу?»** — `middle` — A6
147. **«Что такое interleaving и champion-challenger подходы?»** — `middle_plus` — A6
148. **«Что такое offline evaluation vs online evaluation?»** — `middle` — A6
149. **«Что такое модельный сдвиг из-за feedback loops? Как рекомендательные системы или модели ранжирования могут ухудшать данные, на которых потом обучаются?»** — `middle_plus` — A6
150. **«Почему офлайн-метрики не гарантируют онлайн-успеха? Что такое SRM, novelty effect, feedback loop?»** — `middle_plus` — A3 (День 12)
151. **«线上线下不一致 (offline/online несогласованность): причины и что чинить»** — `middle_plus` — A9 (консистентность фичей, утечки фич, смещение старой модели), A20
152. **«Что такое counterfactual / off-policy evaluation и когда её применяют вместо А/В?»** — `middle_plus` — A10 («counterfactual evaluation» для коррекции смещений), B27, B41
153. **«Какие онлайн-метрики у рекомендаций: CTR, CVR, GMV, discovery rate?»** — `middle` — A9, A10, A17
154. **«Как выбрать guardrail-метрики, чтобы не оптимизировать залипание/кликбейт?»** — `middle_plus` — A1 (#6 VK — «guardrails против аддиктивных паттернов»), B15
155. **«A/B-тесты для cold start: чем отличаются от обычных?»** — `middle_plus` — A21

### 12. Cold start, popularity bias, position bias, дебиасинг

156. **«Как решить проблему холодного старта в рекомендательных системах?»** — `middle` — A1 (RecSys-секция)
157. **«Холодный старт — контентные модели, популярные рекомендации; popularity bias; filter bubble и exploration»** (в такой формулировке спрашивали набор проблем) — `middle` — Самокат — A1
158. **"How do cold start problems impact recommendation systems and how can they be mitigated?"** — `middle` — A8
159. **«Cold start пользователя и cold start айтема — это разные задачи. Как решается каждая?»** — `middle` — B25
160. **«Как решить проблему новичка контента, который алгоритм не показывает?»** — `middle_plus` — A3 (День 13)
161. **«Какие проблемы возникают при обучении только на кликах?»** — `middle_plus` — A3 (День 14)
162. **«Как убедиться, что рекомендер не дискриминирует продавцов?»** — `middle_plus` — A3 (День 14)
163. **«Какие смещения (biases) возникают при проектировании рекомендательной системы и как их избежать?»** — `middle_plus` — **Яндекс, ML Engineer** — B17
164. **«Position bias: как с ним бороться?»** — `middle_plus` — A9 (взвешивание сэмплов, IPW, позиция как фича, отдельный bias-модуль), B30, B38
165. **«Что такое IPS и почему он ломается, если propensity оценены неверно? Что такое doubly robust?»** — `middle_plus` — B38
166. **«长尾问题 (long tail): как обеспечить экспозицию непопулярным айтемам?»** — `middle_plus` — A9
167. **«Как подавлять popularity bias в двухбашенной модели?»** (`cosine − log p_i` при обучении) — `middle_plus` — A11
168. **«Look-Alike и кластерный recall для холодных айтемов — как устроены?»** — `middle_plus` — A21
169. **«Traffic control для новых айтемов: сколько трафика отдавать на разведку?»** — `middle_plus` — A21
170. **«Как решать проблему повторных/дублирующихся рекомендаций (один и тот же товар/видео)?»** — `middle` — A20

### 13. Explore/exploit и бандиты

171. **«Explore-exploit: как балансировать? Epsilon-greedy, UCB, Thompson Sampling — в чём разница?»** — `middle_plus` — A3 (День 13)
172. **«System health metrics: exploration vs exploitation — как измерять здоровье системы?»** — `middle_plus` — A20
173. **«Как через бандиты давать стартовый трафик новым айтемам?»** — `middle_plus` — A3 (в эталонном MLSD-ответе: «New items get initial embedding from content and some exploration traffic via bandit approach»)
174. **«Balance exploration vs exploitation, чтобы не переобучаться на историю»** — `middle_plus` — A11

### 14. Диверсификация и постобработка

175. **«Как диверсифицировать выдачу: MMR, DPP, правила "не более N из категории"?»** — `middle_plus` — A3 (День 10), A21
176. **«Как измерять разнообразие выдачи?»** — `middle` — A21 (diversity metrics), A3
177. **«Diversity: дедупликация и реранкинг по теме/автору — как это делают в проде?»** — `middle_plus` — B30
178. **«Проблема разнообразия в рекомендациях» — прямо назван как тема секции ML в Яндексе** — `middle_plus` — B16
179. **«Какие бизнес-правила накладываются поверх ранжирования (18+, микс жанров, фильтр купленного)?»** — `middle` — A3, A12

### 15. Многостадийная архитектура, latency, продакшн

180. **«Как бы вы спроектировали систему рекомендации видео для e-commerce платформы?»** — `middle_plus` — Самокат — A1
181. **«Как вывести ML-модель рекомендаций в продакшн?»** — `middle` — Самокат — A1 (Airflow пересчитывает эмбеддинги → FAISS/Redis; inference-сервер Triton/TorchServe с батчингом)
182. **«Как оптимизировать тяжёлую модель рекомендаций для продакшн-инференса?»** — `middle` — Ozon — A1
183. **«Как обеспечить латентность inference ML-модели менее 100 мс?»** — `middle` — ZinBrains — A1
184. **«Как происходит деплой ML-модели в продакшн?»** — `middle` — Ozon — A1
185. **«Как спроектировать систему, реагирующую на вирусные тренды?»** / «Как бы вы спроектировали систему, которая сразу реагирует на новые тренды (например, вирусное видео)?» — `middle_plus` — A3 (День 15)
186. **«Как обеспечить 99.9% uptime рекомендационного сервиса?»** — `middle_plus` — A3 (День 15)
187. **«Как справиться при x10 росте пользователей?»** — `middle_plus` — A3 (День 16)
188. **«Что является узким местом в типовой RecSys-архитектуре?»** — `middle_plus` — A3 (День 16)
189. **«Latency requirements — 200 msec?»** (кандидат обязан сам уточнить бюджет) — `middle` — A16; в A11 явно «under 200ms, ideally sub 100ms»
190. **«Как распилить бюджет латентности между retrieval, ranking и reranking?»** — `middle_plus` — A3 (эталонный ответ: 200 кандидатов за <20 мс, скоринг 200 айтемов <30 мс, итого ~50 мс)
191. **«Обучение модели занимает 12 часов. Как искать узкое место и ускорить процесс?»** — `middle` — ZinBrains — A1
192. **«Есть ли опыт с оптимизацией инференса — TensorRT, квантизация и т. д.?»** — `middle` — Infomedia — A1
193. **«Расскажите про полный ML-пайплайн от сбора данных до инференса — какие этапы и инструменты?»** — `middle` — Infomedia — A1
194. **«Как организован мониторинг сервисов? Есть ли on-call дежурство?»** — `middle` — Constructor — A1
195. **«Какие инструменты используете для логирования экспериментов и версионирования моделей?»** — `middle` — Infomedia — A1
196. **«Спроектируйте рекомендации не в батч-режиме, а в онлайн-потоке»** — `middle_plus` — Wildberries — B18
197. **«Какие паттерны проектирования feature store вы знаете?»** — `middle_plus` — A6
198. **«Какие вопросы вы бы задали кандидату про feature store, чтобы понять, что он реально с ним работал?»** (мета-вопрос, встречается в банке) — `middle_plus` — A6
199. **«Что первым внедрять в компании: feature store или model registry?»** — `middle_plus` — A6
200. **«Real-time фичи vs предрасчитанные: где граница и как избежать training/serving skew?»** — `middle_plus` — A10 (user emb в рантайме, item emb офлайн), B19
201. **«Как устроены факторы ранжирования в рантайме: feature-meta-store, таблицы по типам факторов, ML-модель (CatBoost) как фактор»** — `middle_plus` — Ozon — B8
202. **«Отбор нескольких тысяч кандидатов под контекст полки, затем ранжирование 2000–3000 товаров по вероятности покупки — почему именно такие числа?»** — `middle_plus` — Ozon — B9

### 16. LLM-волна в рекомендациях (2024–2026)

> Это самый «свежий» блок; на российском рынке он пока чаще звучит как обсуждение статей и трендов, чем как жёсткий чек-лист.
> Формулировки ниже основаны на источниках B33–B37, B18 и A4 (раздел VI плана «Sequential и Generative рекомендации — SASRec, BERT4Rec, ARGUS»).

203. **«Что такое semantic IDs и чем они лучше обычных item ID?»** — `middle_plus` — B33, B34, B35
204. **«Как RQ-VAE превращает контентный эмбеддинг айтема в иерархический дискретный код?»** — `middle_plus` — B33
205. **«Как устроен TIGER: два этапа обучения (сначала RQ-VAE, потом генеративная модель), и чем генеративный retrieval лучше ANN?»** — `middle_plus` — B33
206. **«Какие проблемы возникают с семантическими ID в проде (коллизии, дрейф каталога, переобучение кодбука)?»** — `middle_plus` — B35
207. **«HSTU / generative recommenders: как унифицировать retrieval и ranking в одной модели и что это даёт по scaling laws?»** — `middle_plus` — B36
208. **«LLM-as-ranker: где именно в воронке ставить LLM и как удержать латентность?»** — `middle_plus` — B37
209. **«Как использовать LLM-эмбеддинги для решения cold start?»** — `middle_plus` — B37
210. **«Что такое conversational recsys и чем он отличается от классической выдачи?»** — `middle_plus` — B37
211. **«Тренд Wildberries: переход от классического ML к LLM-агентам и графовым нейросетям для анализа связей "пользователь — товар" — что бы вы применили?»** — `middle_plus` — Wildberries — B18
212. **«ARGUS: как автогрегрессивное моделирование пользовательской последовательности заменяет каскад фич?»** — `middle_plus` — Яндекс — B3, B4

### 17. Смежное: код и «домашки» вокруг RecSys

213. **«Напишите AUC / реализуйте метрику ранжирования руками»** — `middle` — A20 («AUC implementation and sampling sensitivity»)
214. **«Реализуйте один шаг агрегирования LightGCN вручную (список соседей, усреднение эмбеддингов, 2–3 итерации)»** — `middle_plus` — A3 (практика)
215. **«Обучите LightGCN на MovieLens 1M (RecBole/torch_geometric), сравните Recall@10 и nDCG@10 с ALS»** — `middle` — A3 (практика)
216. **Тестовые задания на RecSys/ранжирование в РФ-компаниях** (Diginetica, OLX-Hermes, МТС, Сбер, Gett и др.) — `middle` — A28
217. **«Техническое собеседование: кодинг + ML System Design + System Design интеграции ML в highload»** (формат секции) — `middle` — Mayflower — A1

---

### Сводка по покрытию компаний (что реально видно в источниках)

| Компания | Что подтверждено | Источник |
|---|---|---|
| **Ozon** | 8 recsys/ранжирование вопросов + 5 MLSD (метрики ранжирования, SASRec vs BERT4Rec, нейроархитектуры, офлайн/онлайн метрики и A/B, кодирование товара с 7000 атрибутов, user-эмбеддинг из последовательности, объединение user/item эмбеддингов, оптимизация тяжёлой модели, деплой) | A1; архитектура — B7, B8, B9 |
| **VK** | 5 вопросов (бизнес-метрика для коротких видео, pairwise vs бинарный классификатор, недифференцируемость NDCG, SVD, candidate generation на контентных+коллаборативных эмбеддингах) | A1 |
| **Wildberries** | метрики ранжирования Precision@K/Recall@K/NDCG/MRR; онлайн-стрим вместо батча; тренд на LLM-агенты и GNN | A1, B18 |
| **Яндекс** | recsys — отдельный из трёх общих раундов; вопрос про biases в рекомендациях; в официальном описании секции — архитектура, метрики, стадии рекомендательной системы, генерация кандидатов, дизайн ранжирования, разнообразие | B17, B16; MLSD-вопросы про генерацию описаний — A1 |
| **Avito** | ранжирование/рекомендации/поиск как основной домен ML; Item2Vec для похожих объявлений; трансформенная персонализация | B19, A3, B6 |
| **Сбер** | вопрос про использованные архитектуры нейросетей (в ответе фигурируют two-tower для рекомендаций и retrieval); MLSD-антифрод | A1 |
| **Т-Банк / Тинькофф** | официальная канва секции ML System Design; MLSD-антифрод | A24, A1 |
| **Самокат** | 6 вопросов (метрики ранжирования, MAP vs NDCG, pointwise vs pairwise, проблемы рекомендаций, A/B без разницы по GMV, улучшение алгоритма по мере накопления данных) + 2 MLSD | A1 |
| **Constructor** (SaaS для e-com поиска/рекомендаций) | 6 вопросов (метрики, сбор таргета, трансформеры для ранжирования, контекст сессии, оптимизация на маржу, мультимодальные фичи) | A1 |
| **ZinBrains** | 7 вопросов (implicit ALS, NDCG, NDCG vs MAP, типы loss в ранжировании, BPR vs WARP, SASRec-реализация, опыт) + FAISS IVF, латентность <100 мс, ускорение обучения | A1 |
| **Quantum One, Дром.ру, Mayflower, Infomedia, Waibee, Candy.ai** | точечные вопросы, см. выше | A1 |

**Итого распознаваемых различимых вопросов в этом дампе: 217** (из них с явной привязкой к компании — 60+, с явным грейдом из источника — 59).

---

## Что интервьюеры ловят этими вопросами

1. **Понимает ли кандидат, что рекомендации — это не «предсказание рейтинга».**
   Классический ловец: вопрос про SVD (#35–37) или про «почему нельзя ранжировать по вероятности бинарного классификатора» (#78).
   Проверяется: осознаёт ли кандидат, что бизнес-задача — упорядочить, а не оценить; что MSE-регрессия на рейтинги
   решает не ту задачу; что скоры разных пользователей/сессий не сравнимы без калибровки.

2. **Умеет ли думать воронкой, а не одной моделью.**
   Вопросы #63–77, #97, #180, #190. Интервьюер хочет услышать: retrieval (миллионы → тысячи) → грубое ранжирование →
   точное ранжирование → реранкинг/бизнес-правила, с осмысленным бюджетом латентности на каждую стадию.
   Ключевой маркер зрелости — кандидат сам спрашивает про latency, RPS, размер каталога и DAU (A16, B21).

3. **Отличает ли implicit от explicit и знает ли, что «нет клика ≠ дизлайк».**
   Вопросы #24–29. Здесь ловят на confidence weighting в iALS, на негативном сэмплировании и на понимании, что
   ненаблюдаемое — это смесь «не понравилось» и «не показали».

4. **Знает ли, откуда берутся негативы.**
   Вопросы #70, #71. Это главный «водораздел» между тем, кто читал про two-tower, и тем, кто её обучал:
   in-batch негативы → перекос в популярное → logQ-коррекция; hard negatives из грубого ранкера; смесь равномерных и in-batch.

5. **Понимает ли разницу между офлайн- и онлайн-реальностью.**
   Вопросы #142–155. Любимая ловушка: «офлайн precision +5%, катим?» (#144) и «A/B не показал разницы по GMV» (#143).
   Проверяют: мощность теста, прокси-метрики, guardrails, длительность, сегментацию, novelty effect, SRM.

6. **Видит ли обратные связи и смещения.**
   Вопросы #149, #163, #164, #165. Яндекс прямо спрашивает про biases (B17). Ждут: position bias → IPW / позиция как фича /
   bias-модуль; popularity bias → logQ / нормировка / exploration; selection bias → мы учимся только на том, что показали;
   feedback loop → модель портит собственную обучающую выборку.

7. **Различает ли метрики по типу релевантности и по стадии.**
   Вопросы #126–141. Типовой отсев: кандидат перечисляет NDCG/MAP/MRR, но не может сказать,
   что MAP — про бинарную релевантность, NDCG — про градуированную, MRR — про «первый релевантный»,
   Recall@K — метрика retrieval-стадии, а не финальной выдачи.

8. **Есть ли продуктовое чутьё: что оптимизируем и чем это может кончиться.**
   Вопросы #4, #15, #16, #92, #154. Хороший ответ на «время сессии или суммарное время» включает guardrails,
   антикликбейт, долгосрочный retention, а не только «максимизируем watch time».

9. **Знает ли современный канон и умеет ли его датировать.**
   Вопросы #103–125, #203–212. Здесь смотрят не «зазубрил ли», а «понимает ли, зачем появилась каждая следующая модель»:
   MF → FM → Wide&Deep → DCN → DIN/DIEN → SASRec/BERT4Rec → LightGCN → генеративные рекомендации / semantic IDs.

10. **Может ли рассказать свой проект как инженер, а не как пересказ курса.**
    Вопросы #1–3, #115, #116. Формат ответа, который ждут (сформулирован прямо в A2):
    бизнес-задача → формализация (candidate generation + reranking) → данные (implicit/explicit, cold start) →
    модель (ALS, two-tower, cross-encoder для reranking) → офлайн-метрики (Recall@K, NDCG) → A/B (CTR, конверсия, GMV) →
    проблемы (cold start, position bias, latency) → trade-offs скорость/качество на каждом этапе.

---

## Пробелы, которые чаще всего валят кандидатов

Ниже — не гипотезы «вообще», а места, где источники прямо фиксируют разрыв между «знаю слова» и «понимаю».

1. **«SVD» в рекомендациях.** Кандидат называет SVD, но не может объяснить, что классическое SVD не определено на матрице
   с пропусками, что «SVD» Функа — это по сути градиентная MF с регуляризацией, и что truncated SVD даёт low-rank
   приближение только уже заполненной матрицы (A1 #9, B13). Отсюда же путаница «SVD == SVD++».

2. **Негативы и logQ.** Самый частый провал на middle+: человек знает, что есть in-batch негативы, но не знает,
   что без коррекции `− log p_i` модель уезжает в популярное, и не может сказать, где взять hard negatives (A9, A11, B26, B31).

3. **NDCG как loss.** Кандидат уверенно считает NDCG, но зависает на «почему её нельзя оптимизировать напрямую»
   (ступенчатая, недифференцируемая по скорам) и не знает про LambdaRank/LambdaMART как аппроксимацию градиента через ΔNDCG (A1 #8).

4. **Калибровка.** «Отранжируем по вероятности клика» — и на вопрос «а если голов несколько и их надо смешать?»
   ответа нет. Score fusion, калибровка, multi-objective, MMoE — зона провала (A21, A1 #7).

5. **Метрики без стадии.** Recall@1000 на retrieval и NDCG@10 на финальной выдаче измеряют разное; кандидаты часто
   меряют одной метрикой всю систему и не понимают, почему +Recall у ретривера не даёт +NDCG (A20, A21, B42).

6. **Офлайн→онлайн.** Нет ответа на «почему офлайн вырос, а А/В нет». Не звучат: сдвиг распределения из-за смены политики
   показа, position bias в логах, feedback loop, novelty effect, недостаточная мощность (A3 День 12, A9, B42).

7. **Cold start сводится к «покажем популярное».** Не звучат: контентные эмбеддинги, look-alike, кластерный recall,
   traffic control, отдельные метрики для cold-start, бандиты для разведки (A21, A3 День 13).

8. **Position bias.** Знают термин, но не умеют предложить конкретику: IPW с оценкой propensity, позиция как фича с
   занулением на инференсе, отдельная bias-башня; и не знают, что IPS несмещён только при корректно заданных propensity (A9, B38).

9. **ANN как чёрный ящик.** «Возьмём FAISS» — и всё. Не могут сравнить HNSW и IVF-PQ по памяти/recall/времени построения,
   не знают про nprobe, PQ, шардирование индекса, перестроение при обновлении каталога (A1 #16 MLSD, A10, B40).

10. **Латентность без цифр.** Не называют бюджет (200 мс / 100 мс), не декомпозируют его по стадиям, не объясняют,
    почему item-эмбеддинги считаются офлайн, а user-эмбеддинг — в рантайме (A11, A10, A3).

11. **Two-tower vs cross-encoder.** Не могут объяснить, почему в башнях нельзя использовать cross-фичи и почему
    interaction network `[u; i; u*i] → MLP` не индексируется в ANN (A1 MLSD #8).

12. **Разнообразие и «здоровье» системы.** Diversity/novelty/serendipity воспринимаются как «красивые слова»;
    MMR и DPP не называются; не звучит, что оптимизация только CTR порождает кликбейт и фильтр-пузырь (A21, B11, B15).

13. **Sequential-модели по названиям.** «SASRec и BERT4Rec» без понимания causal vs masked, без ответа на
    «что делать с историей в 8000 событий» и без представления о стоимости инференса (A1 #21, B3, B5).

14. **LLM-волна как хайп.** Кандидат слышал про «LLM в рекомендациях», но не может сказать, где именно в воронке
    это ставится, что такое semantic ID / RQ-VAE и почему генеративный retrieval вообще может заменить ANN (B33–B37).

15. **Отсутствие «своей истории».** Вопросы #1–3, #31, #115 — это проверка опыта. Ответ без цифр (сколько айтемов,
    какой прирост, какая метрика, какой A/B) читается как пересказ курса.

---

## Рекомендации для структуры глав хендбука по этой теме

Предлагаемая структура раздела `06-recsys` — 12 глав + приложения. Порядок отражает частотность на собеседованиях
(глава тем раньше, чем чаще её спрашивают), а не «академическую» логику.

### 06.00 — Как устроено собеседование по RecSys
- Три формата: (1) короткий блок в общей ML-секции, (2) отдельная RecSys-секция, (3) ML System Design «спроектируйте рекомендации».
- Разбор канвы MLSD: формализация → декомпозиция → данные → архитектуры подзадач → деплой и тестирование (A24, A15).
- Чек-лист уточняющих вопросов, которые кандидат обязан задать сам: бизнес-цель, размер каталога, DAU/RPS, latency, тип фидбэка, где показываем (A16, B20, B21).
- Матрица «грейд × ожидания»: junior — определения и метрики; middle — воронка, ALS/BPR, two-tower, NDCG/MAP, A/B; middle+ — негативы и logQ, дебиасинг, multi-objective, latency-бюджет, sequential/генеративные модели.

### 06.01 — Постановка задачи и метрики (офлайн)
- Rating prediction vs top-N ranking vs next-item prediction.
- Precision@K, Recall@K, MAP@K, MRR, HitRate, NDCG@K (с выводом DCG/IDCG вручную — вопрос #130 буквально «как считается»).
- Rank-aware vs non-rank-aware; бинарная vs градуированная релевантность (#131, #132).
- Метрики «здоровья»: coverage, novelty, serendipity, diversity, personalization, intra-list similarity (#137, #138).
- Отдельный параграф «метрика под стадию»: что мерить на retrieval, что на ranking, что на реранкинге (#140).
- Типовые ловушки: почему не accuracy (#134), когда MRR врёт (#136), как выбирать K.

### 06.02 — Данные: implicit/explicit, логи, таргет
- Явный и неявный фидбэк, шум в неявном (#29), веса уверенности.
- Как собирают таргет для ранжирования (#93): клики, дочитывания, покупки, watch time, взвешивание по цене/марже (#92).
- Логи показов и position bias уже здесь (почему логи — не i.i.d. выборка).
- Отрицательные примеры: экспозиция без клика vs «не показывали».

### 06.03 — Классика: CF, соседи, матричные разложения
- User-based / item-based CF, меры сходства, Swing (#20–23).
- MF: Funk-SVD, SVD++, ALS, iALS, доверие в implicit-ALS (#27, #28), BPR, WARP (#40, #41).
- FM/FFM как мост к контенту (#44–47).
- Почему MF сегодня — это генератор кандидатов, а не финальная выдача (#48).
- Практика: реализовать iALS на MovieLens, сравнить с BPR по Recall@10/NDCG@10.

### 06.04 — Контент, эмбеддинги, item2vec, мультимодальность
- Контентные признаки и их пределы (#50).
- item2vec / prod2vec, графовые эмбеддинги (node2vec, DeepWalk, EGES) (#51, #54, A9).
- Мультимодальные эмбеддинги: текст (BM25 → sentence-transformers) + картинки (CLIP) (#55, #56).
- Кейсы: Ozon Prod2Vec (B7), Avito item2vec (A3).
- Как кодировать товар с тысячами разнородных атрибутов (#57).

### 06.05 — Retrieval: two-tower, негативы, ANN
- Архитектура двухбашенной модели; почему башни независимы и что это даёт (#68).
- Что нельзя положить в башню: cross-фичи; two-tower vs cross-encoder/interaction network (#69, #59).
- Негативы: random ~ popularity^0.75, in-batch, cross-batch, hard negatives, mixed negative sampling (#70).
- Sampled softmax и logQ-коррекция — с формулой `cosine(a,b_i) − log p_i` (#71).
- Multi-path recall и ансамбль каналов (#72), exposure filtering (#76).
- ANN: HNSW vs IVF vs IVF-PQ vs ScaNN; nprobe, PQ, память/recall/время построения; шардирование индекса; обновление каталога (#66, #67).
- Метрики retrieval-стадии (#73).

### 06.06 — Ranking: LTR и нейросетевой канон
- Pointwise / pairwise / listwise, их лоссы и когда что (#80–84, #88).
- Почему NDCG нельзя оптимизировать напрямую; LambdaRank/LambdaMART (#79).
- Калибровка и несопоставимость скоров (#78).
- GBDT (CatBoost/LightGBM) как рабочая лошадка ранжирования в РФ-компаниях (B8, B19).
- Нейроканон по хронологии: Wide&Deep → DeepFM → DCN/DCNv2 → xDeepFM → DIN → DIEN → SIM → DLRM → MaskNet (#103–112).
- Фичи ранкера: user / item / cross / context / sequence; сессионный контекст (#90, #91).
- Multi-objective: несколько голов, MMoE, score fusion, watch-time modeling (#94–96).
- Каскад: грубое → точное → пере-ранжирование (#97).

### 06.07 — Sequential и генеративные рекомендации
- GRU4Rec, SASRec, BERT4Rec: causal vs masked, что и когда (#113, #114, #116).
- Длинная история: SIM, сжатие истории, стоимость инференса (#109, #119).
- Scaling laws для рекомендаций: HSTU, ARGUS (#117, #118, #120).
- Генеративный retrieval: semantic IDs, RQ-VAE, TIGER; чем заменяет ANN; индустриальные грабли (#203–207).
- LLM в рекомендациях: LLM-as-ranker, LLM-эмбеддинги для cold start, conversational recsys, P5-подобные постановки (#208–211).
- Отдельный «трезвый» параграф: где LLM реально окупается, а где это дорогая замена GBDT.

### 06.08 — Графовые рекомендации
- Bipartite-граф взаимодействий; LightGCN и почему из GCN выкинули трансформации и нелинейности (#121).
- PinSage и sampling на больших графах.
- Cold start в графовых моделях (#122); усиление popularity bias свёртками (#125).
- Когда GNN не нужен (честный раздел).

### 06.09 — Смещения, cold start, exploration
- Таксономия смещений: selection, exposure, position, popularity, conformity (#163).
- Position bias: IPW, позиция как фича, bias-башня; ограничения IPS; doubly robust (#164, #165).
- Popularity bias и long tail (#166, #167).
- Cold start пользователя и айтема: контент, look-alike, кластерный recall, traffic control, отдельные метрики и A/B (#156–160, #168, #169).
- Explore/exploit: ε-greedy, UCB, Thompson Sampling, контекстные бандиты; сколько трафика отдавать на разведку (#171–174).
- Feedback loop и деградация обучающей выборки (#149).

### 06.10 — Постобработка: разнообразие, правила, фильтры
- MMR, DPP, квоты по категориям/авторам, дедупликация (#175–177).
- Бизнес-правила и модерация поверх ранжирования (#179).
- Борьба с повторами (#170).
- Как разнообразие связано с долгосрочными метриками и «хорошими свойствами» рекомендаций (B15).

### 06.11 — Онлайн-оценка: A/B, guardrails, counterfactual
- Дизайн A/B для рекомендаций: рандомизация, длительность, SRM, novelty effect, сетевые эффекты в маркетплейсе (#144–150).
- Прокси-метрики и иерархия метрик; guardrails против кликбейта (#143, #154).
- Interleaving, champion–challenger, switchback (#147).
- Off-policy evaluation: IPS, SNIPS, doubly robust, replay; когда это дешевле A/B (#152).
- Почему офлайн растёт, а онлайн — нет: список причин с диагностикой (#150, #151).

### 06.12 — Продакшн: архитектура, latency, фичи, мониторинг
- Референсная многостадийная архитектура с бюджетом латентности (#189, #190).
- Офлайн-контур (Kafka → озеро → Spark/Airflow → пересчёт эмбеддингов → FAISS/Redis) и онлайн-контур (candidate service + ranking service) (#181, A3).
- Feature store: онлайн/офлайн, point-in-time корректность, training/serving skew (#197–200).
- Реалтайм-фичи и реакция на тренды (#185); онлайн-стрим вместо батча (#196).
- Оптимизация инференса: батчинг, дистилляция, квантизация, TensorRT/Triton (#182, #192).
- Мониторинг, on-call, дрейф, автоматический ретрейн (#194).
- Кейсы РФ: Ozon (полки, feature-meta-store, 2000–3000 кандидатов), Avito, Яндекс (ARGUS) (B6–B9, B3–B5).

### Приложения
- **A. Канон статей** (по A22, A26): Hu et al. iALS (2008), BPR (2009), item2vec (2016), Wide&Deep (2016), YouTube DNN (2016),
  NCF (2017), DIN (2018), DIEN (2019), SASRec (2018), BERT4Rec (2019), LightGCN (2020), SSL for large-scale item rec (2021),
  ItemSage (2022), TIGER / generative retrieval (2023), HSTU (2024), ARGUS (2025).
- **B. Банк вопросов** — 217 вопросов из этого дампа, сгруппированных по главам, с грейдами и компаниями.
- **C. Разбор трёх эталонных MLSD-кейсов**: лента коротких видео (VK-подобный), рекомендательная полка маркетплейса
  (Ozon-подобный), похожие объявления (Avito-подобный) — каждый с бюджетом латентности и списком метрик.
- **D. Русско-английский глоссарий** (retrieval/отбор кандидатов, ранжирование, реранкинг, холодный старт,
  смещение позиции, разнообразие, неявный фидбэк и т. д.) — на собеседованиях термины смешивают.
- **E. Инструменты**: implicit, LightFM, RecBole, RecTools (MTS), RePlay (Sber), TFRS, NVIDIA Merlin, FAISS/hnswlib/ScaNN (A22, A26, поиск по sb-ai-lab/RecSys-Course).

### Приоритет наполнения (если ресурс ограничен)
Сначала 06.01, 06.05, 06.06, 06.11, 06.09 — на них приходится большинство реальных вопросов.
Затем 06.03, 06.12, 06.07. Последними — 06.08 и LLM-часть 06.07 (их спрашивают реже и в основном на middle+).
