# Production ML / MLOps / Big Data — research dump

> Собрано веб-поиском и прямыми фетчами 2026-07-26.
>
> **Правило дампа.** Сюда попадают только вопросы, которые я реально видел в загруженном контенте.
> Ничего не выдумано, ни один URL не «восстановлен по памяти».
>
> **Техническое ограничение этой сессии, влияющее на состав источников.** Прокси окружения
> пропустил только `github.com` и `raw.githubusercontent.com`. Все остальные домены
> (habr.com, datatalks.ru, medium.com, dev.to, huyenchip.com, evidentlyai.com, neptune.ai,
> glassdoor.com, interviewquery.com, yandex.ru/jobs, sberdevices.ru, karpov.courses,
> ml-system-design.ru, datavidhya.com, jobswithscala.com, pipecode.ai, hashdork.com,
> mentorcruise.com, wecreateproblems.com, datainterview.com, geeksforgeeks.org)
> вернули **HTTP 403** и на WebFetch, и на curl. Поэтому:
> - §«Источники A» — то, что реально загружено целиком (это ~95 % материала ниже);
> - §«Источники B» — страницы, от которых я видел **только сниппет поисковой выдачи**.
>   Оттуда я беру только те формулировки/факты, которые дословно присутствовали в сниппете,
>   и помечаю их тегом `[снippet]`. Всё, что помечено `[snippet]`, стоит перепроверить
>   при переносе в главу.
>
> **Оговорка про грейды.** Ни один из открывшихся источников по MLOps/Big Data не даёт
> авторской разметки по сложности (в отличие от `alexeygrigorev/data-science-interviews`
> в classic-ML, где есть 👶/⭐️/🚀). Поэтому **грейд везде — моя атрибуция** по глубине вопроса:
> - `junior` — определение/назначение инструмента, «что такое X»;
> - `middle` — механика, сравнение альтернатив, «как это работает внутри», типовой тюнинг;
> - `middle_plus` — компромиссы под нагрузкой, дизайн системы, разбор инцидента, цифры и SLA.
>
> **Оговорка про компании.** Пофамильную привязку «этот вопрос задали в компании X»
> публичные источники по MLOps почти не дают. Что удалось подтвердить документально:
> - **Т-Банк (Tinkoff)** — состав секций для направления «Машинное обучение» и описание секции
>   «Дизайн ML-систем» (репозиторий `Tinkoff/career`, дословная цитата ниже);
> - **`andreyyarigin/de-interview-questions`** — русскоязычная база, автор прямо пишет:
>   «вопросы (в том числе с реальных тех. собеседований)», и в формате карточки есть поле
>   «**Вопрос — точная формулировка с собеседования**». Работодатели не названы;
> - **`SepidehHosseinian/MLOPs-Interview-Questions`** — набор позиционируется как вопросы
>   для интервью на MLOps-инженера (50 базовых + 10 для senior), работодатели не названы;
> - **`devflash101/ml-interview-questions`** — заголовок репозитория: «Interview Questions **I faced**»,
>   то есть вопросы с личных собеседований автора; компании не названы.
>
> Всё остальное — банки вопросов без атрибуции. Колонка «компания» почти везде пустая,
> и это честнее, чем проставить правдоподобные догадки.

---

## Источники, которые реально просмотрены

### A. Загружено целиком (контент получен)

#### A1. Русскоязычные

| Ключ | URL | Что там |
|---|---|---|
| `[RUDE]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/README.md | **Главный русскоязычный источник по Big Data.** База DE-вопросов в формате Obsidian; автор заявляет вопросы «в том числе с реальных тех. собеседований», формат карточки включает «точную формулировку с собеседования». |
| `[RUDE-SP]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_Spark.md | 12 вопросов по Spark, все — практические (память executor, стратегии join, coalesce vs repartition, UDF). |
| `[RUDE-SQL]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_SQL.md | 22 вопроса: JOIN (логические и физические), индексы OLTP vs OLAP, B-Tree/LSM/GIN/BRIN, MVCC, оконные функции. |
| `[RUDE-AF]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_Airflow.md | 13 вопросов по Airflow, включая каверзные (start_date, Reparse DAG, тяжёлые импорты в теле DAG). |
| `[RUDE-CH]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_ClickHouse.md | 20 вопросов по ClickHouse: движки, шардирование/партицирование, мутации, Keeper, Kafka engine. |
| `[RUDE-DWH]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_DWH.md | 11 вопросов: Data Vault 1.0/2.0, слои хранилища, SCD, идемпотентность. |
| `[RUDE-DL]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_DataLake.md | 6 вопросов: слои Data Lake, HDFS vs S3, Parquet в S3, data skew, schema-on-read. |
| `[RUDE-LH]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_DataLakehouse.md | 6 вопросов: merge-on-read vs copy-on-write, разделение storage/compute, small files, compaction в Iceberg, ACID-компромиссы. |
| `[RUDE-ETL]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_ETL.md | 4 вопроса: dbt best practices, Data Quality в ELT, Kafka→ClickHouse, CI/CD для дата-пайплайнов. |
| `[RUDE-MPP]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_MPP.md | 11 вопросов: Greenplum (ключ дистрибуции, Replicated, deadlock), StarRocks, Trino, data skew в MPP. |
| `[RUDE-NOSQL]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_NoSQL.md | 2 вопроса: Redis vs MongoDB, графовые и векторные БД. |
| `[RUDE-PY]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_Python.md | 11 вопросов по Python в контексте DE, включая «почему pandas в DE — не best practice». |
| `[RUDE-OTH]` | https://raw.githubusercontent.com/andreyyarigin/de-interview-questions/main/03_Questions/_Other.md | 27 вопросов: брокеры сообщений, идемпотентность, Saga, golden signals, OpenTelemetry, K8s-джобы, вероятностные структуры, MV. **Тут же — единственный найденный русский вопрос про стык DE↔ML.** |
| `[TK-INT]` | https://raw.githubusercontent.com/Tinkoff/career/main/interview/README.md | Т-Банк: этапы и состав секций. Для «Машинного обучения» — программирование + секция по ML + **дизайн ML-систем**. |
| `[TK-SDML]` | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/system-design-ml.md | **Дословное описание секции «Дизайн ML систем» Т-Банка** + список материалов для подготовки. |
| `[TK-ML]` | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/platform-ml.md | Секция по ML Т-Банка: «постановка задачи, выбор и обоснование метрик качества, сбор и валидация данных, ML-алгоритмы». |
| `[TK-SDB]` | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/system-design-backend.md | Бэкенд-системный дизайн Т-Банка — полезен как «соседняя секция» для MLE. |
| `[RUMLSD]` | https://raw.githubusercontent.com/IrinaGoloshchapova/ml_system_design_doc_ru/main/README.md | Reliable ML: что такое ML System Design Doc и зачем он нужен. |
| `[RUMLSD-T]` | https://raw.githubusercontent.com/IrinaGoloshchapova/ml_system_design_doc_ru/main/ML_System_Design_Doc_Template.md | **Русский шаблон ML System Design Doc.** Готовая рубрикация для главы про дизайн: цели/бизнес-требования → методология → пилот → внедрение (архитектура, инфраструктура, SLA, безопасность, издержки, риски). |
| `[RU-SD]` | https://raw.githubusercontent.com/beagreatengineer/learn-system-design/main/README.md | Русская подборка по System Design (канал careerunderhood). |
| `[RU-SDR]` | https://raw.githubusercontent.com/vladimir-maslov/system-design-roadmap/main/ru/README.md | Русская дорожная карта по System Design. |
| `[HEX]` | https://raw.githubusercontent.com/Hexlet/ru-interview-questions/main/README.md | Хекслет: сборник вопросов с собеседований по направлениям (есть «Аналитик данных», «Базы данных», DevOps). |
| `[MLI]` | https://raw.githubusercontent.com/Pe4enIks/ML-Interview/main/README.md | Русский репозиторий «вопросы с собеседований на MLE». **Проверено: MLOps/прод/Spark/Docker/K8s там практически нет** — это теоретический ML/CV/DL банк. Важный негативный результат: русские MLE-банки почти не покрывают прод. |
| `[EXTR]` | https://raw.githubusercontent.com/Extremesarova/ds_resources/main/README.md | Мета-индекс DS-ресурсов с русской секцией; через него найдены остальные источники. |

#### A2. Англоязычные — специализированные банки MLOps

| Ключ | URL | Что там |
|---|---|---|
| `[SEP-G]` | https://raw.githubusercontent.com/SepidehHosseinian/MLOPs-Interview-Questions/main/General%20MLOps/README.md | **36 пронумерованных вопросов Q1–Q36** с ответами. Самый плотный англоязычный MLOps-банк из открывшихся. |
| `[SEP-D]` | https://raw.githubusercontent.com/SepidehHosseinian/MLOPs-Interview-Questions/main/Model%20Deployment/README.md | **50 вопросов для интервью на MLOps-инженера + 10 для senior.** Формулировки «поведенческо-технические» («Can you discuss an experience you have had with…»). |
| `[SEP-M]` | https://raw.githubusercontent.com/SepidehHosseinian/MLOPs-Interview-Questions/main/Model%20Monitoring/README.md | 10 вопросов «для более продвинутых кандидатов»: distributed training в мультиоблаке, автоскейлинг, federated learning. |
| `[SEP-T]` | https://raw.githubusercontent.com/SepidehHosseinian/MLOPs-Interview-Questions/main/Model%20Testing%20and%20Validation/README.md | 6 вопросов Q1–Q6 с развёрнутыми ответами (static vs dynamic deployment, production testing, batch vs stream, train-serving skew, model registry). |
| `[SEP-R]` | https://github.com/SepidehHosseinian/MLOPs-Interview-Questions/tree/main | Структура репозитория (7 категорий). Категории Data Engineering / Model Training / Governance на момент фетча **пустые** (1 байт) — учтено. |
| `[DI-MLOPS]` | https://raw.githubusercontent.com/Devinterview-io/mlops-interview-questions/main/README.md | 15 первых из 50 вопросов (остальное за пейволом devinterview.io). |
| `[DI-LLMOPS]` | https://raw.githubusercontent.com/Devinterview-io/llmops-interview-questions/main/README.md | 15 первых из 50. Заметно пересекается с MLOps-набором, но акцент на LLM-специфике. |
| `[VENK]` | https://raw.githubusercontent.com/venkataravuri/ai-ml/master/docs/interview-notes/mlops.md (+ https://github.com/venkataravuri/ai-ml/blob/master/docs/interview-notes/mlops.md) | Заметки по MLOps/Kubeflow в форме прямых вопросов: упаковка артефактов, где хранятся модели в Kubeflow, GPU P-states, EFS/S3 для датасетов. |
| `[CM]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/README.md | Корневой индекс: явные треки «Data Engineering Track», «MLOps Track», «DevOps», «System Design». |
| `[CM-SERV]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/mlops/intro_model_serving.md | Паттерны сервинга + секция **Interview Q&A (Q1–Q6)**, статический/динамический батчинг, REST vs gRPC, blue-green/canary/shadow. |
| `[CM-FS]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/mlops/intro_feature_stores.md | Feature store + **Q1–Q5**, point-in-time correctness, offline/online store, Feast. |
| `[CM-MLF]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/mlops/intro_mlflow.md | MLflow + **Q1–Q11** (experiment vs run, registry vs артефакты, flavors, `infer_signature`, автологгинг и его лимиты). |
| `[CM-DQ]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/mlops/intro_data_quality.md | Data quality/дрейф + **Q1–Q5** (data vs concept drift, PSI и его интерпретация, data contracts, schema drift). |
| `[CM-AB]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/mlops/intro_ab_testing.md | A/B для ML + секция **Common Interview Questions** (SRM, CUPED, peeking). |
| `[CM-PIPE]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/data_engineering/intro_data_processing_pipelines.md | Спектр batch → microbatch → near-real-time → streaming + **Interview Questions & Answers**; watermarks. |
| `[CM-SPARK]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/data_engineering/intro_apache_spark.md | Spark: архитектура, партиционирование, кэш, broadcast, **AQE**. |
| `[CM-DOCKER]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/devops/intro_docker.md | Docker для ML: тома, сети, слои. |
| `[CM-K8S]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/devops/intro_kubernetes.md | Kubernetes для ML. |
| `[CM-API]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/frameworks/intro_fastapi.md | FastAPI как прод-бэкенд + **Interview Questions** (SSE vs WebSockets, rate limiting, fault tolerance). |
| `[CM-BSD]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/system_design/backend_system_design_interview_guide.md | 32 backend-концепции вокруг ML-систем: скейлинг, кэш, шардирование, CAP, Saga, consistent hashing. |
| `[CM-SD]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/system_design/intro_backend_ai_system_design.md | Дизайн AI-бэкенда. |
| `[CM-26A]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/docs/2026-additional-questions.md | 26 вопросов «банк 2026»: batch vs real-time vs async, мониторинг после деплоя, offline vs online eval, калибровка. |
| `[CM-26B]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/docs/interview_questions_2026.md | 20 вопросов с эталонными ответами; секции «Production AI Systems» и «System Design Scenarios». |
| `[CM-EVAL]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/mlops/intro_evaluation_guardrails.md | Eval и guardrails. |
| `[CM-LLMOPS]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/mlops/intro_llmops_mlops_engineering.md | LLMOps vs MLOps. |
| `[CM-DE4AI]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/data_engineering/intro_data_engineering_for_ai.md | DE для AI, feature store как система. |
| `[PUB]` | https://raw.githubusercontent.com/pubalisen/ai-ml-interview-deep-dives/main/README.md | «300+ real interview questions». **Ценнейшие для нас разделы:** *AI System Design* (25 end-to-end + 22 trade-off), *LLMOps and Production AI* (34 концептуальных + 11 сценарных), *AI Infrastructure and Scalability* (25). |
| `[JIC]` | https://raw.githubusercontent.com/JustInCache/awesome-ai-interviews/main/README.md | Топ-50 AI-вопросов с ответами; раздел **LLMOps & Production** содержит развёрнутую таблицу «Traditional MLOps vs LLMOps» и разбор мониторинга (TTFT, inter-token latency, cost per query). |
| `[DEVF]` | https://raw.githubusercontent.com/devflash101/ml-interview-questions/main/README.md | «Interview Questions **I faced**» — 20 вопросов с личных собеседований автора, сгруппированные по требованиям вакансии. Много про пайплайны и прод. |

#### A3. Англоязычные — Big Data / Data Engineering

| Ключ | URL | Что там |
|---|---|---|
| `[OB]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/README.md | Индекс «More than 2000+ Data engineer interview questions» (1.7k★). |
| `[OB-SPARK]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/spark.md | **161 КБ, ~140 вопросов по Spark** с ответами. Самый большой открывшийся Spark-банк. |
| `[OB-SQL]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/sql.md | 193 КБ, сотни SQL-вопросов и задач «напиши запрос». |
| `[OB-KAFKA]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/kafka.md | 23 вопроса по Kafka (ISR, exactly-once, offset, leader/follower, QueueFullException). |
| `[OB-AF]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/airflow.md | 16 вопросов по Airflow (executors и их плюсы/минусы, XCom, Jinja). |
| `[OB-K8S]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/kubernetes.md | 25 вопросов по Kubernetes, заметно эксплуатационнее, чем у Devinterview (PDB, init-контейнеры, troubleshooting нешедулящегося пода). |
| `[OB-HIVE]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/hive.md | ~60 вопросов по Hive. |
| `[OB-HADOOP]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/hadoop.md | 115 КБ вопросов по Hadoop/HDFS/YARN/MapReduce. |
| `[OB-FLINK]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/flink.md | ~50 вопросов по Flink (watermark, state, slots, bounded/unbounded). |
| `[OB-PY]` | https://raw.githubusercontent.com/OBenner/data-engineering-interview-questions/master/content/python.md | Python для DE. |
| `[DI-SPARK]` | https://raw.githubusercontent.com/Devinterview-io/apache-spark-interview-questions/main/README.md | 15 первых из 55 (RDD/DataFrame, lazy eval, DAG scheduler, Catalyst, Tungsten). |
| `[DI-HADOOP]` | https://raw.githubusercontent.com/Devinterview-io/hadoop-interview-questions/main/README.md | 15 первых из 50 (HDFS, YARN, rack awareness, HBase, Hive, Sqoop, Oozie, ZooKeeper). |
| `[DI-SQL]` | https://raw.githubusercontent.com/Devinterview-io/sql-interview-questions/main/README.md | 15 первых из 100. |
| `[DI-DOCKER]` | https://raw.githubusercontent.com/Devinterview-io/docker-interview-questions/main/README.md | 15 первых из 55. |
| `[DI-K8S]` | https://raw.githubusercontent.com/Devinterview-io/kubernetes-interview-questions/main/README.md | 15 первых из 42. |
| `[DI-PYML]` | https://raw.githubusercontent.com/Devinterview-io/python-ml-interview-questions/main/README.md | Python для ML. |
| `[DI-MS]` | https://raw.githubusercontent.com/Devinterview-io/microservices-interview-questions/main/README.md | Микросервисы — контекст для «модель как сервис». |
| `[DEH]` | https://raw.githubusercontent.com/DataExpert-io/data-engineer-handbook/main/README.md | Data Engineering Handbook — карта тем DE. |
| `[COOK]` | https://raw.githubusercontent.com/andkret/Cookbook/master/README.md | The Data Engineering Cookbook — рубрикация тем DE. |
| `[DEZC]` | https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/README.md | Программа DE Zoomcamp — эталонный порядок тем. |

#### A4. Англоязычные — ML System Design и прод

| Ключ | URL | Что там |
|---|---|---|
| `[CHIP]` | https://raw.githubusercontent.com/chiphuyen/machine-learning-systems-design/master/build/build1/consolidated.html | **Chip Huyen, «Machine Learning Systems Design».** 27 открытых design-задач + разделы Project setup / Data pipeline / Modeling / **Scaling** / **Serving** с явными списками вопросов, которые надо задать интервьюеру. Дословно: *«This part contains 27 open-ended questions… it's almost guaranteed that you'll be asked at least one during your interview process»*. |
| `[ALZ]` | https://raw.githubusercontent.com/alirezadir/Machine-Learning-Interviews/main/src/MLSD/ml-system-design.md | **9-шаговая формула ML System Design** + список типовых design-вопросов по доменам (рекомендации, поиск, ранжирование, NLP, CV, AV) + раздел 9 «Scaling, Monitoring, and Updates». |
| `[ALZ-R]` | https://raw.githubusercontent.com/alirezadir/Machine-Learning-Interviews/main/README.md | Структура ML-интервью по модулям. |
| `[PLDL]` | https://raw.githubusercontent.com/alirezadir/Production-Level-Deep-Learning/master/README.md | «A Guide to Production Level Deep Learning» — full-stack пайплайн: Data Management (sources/labeling/storage/**versioning**/processing) → Development (**resource management**, **experiment management**, HPO, **distributed training**) → Testing & Deployment (CI/CD, web deployment, **service mesh & traffic routing**, **monitoring**, embedded/mobile) → TFX/Airflow/Kubeflow. **Указан Т-Банком как материал для подготовки к секции «Дизайн ML-систем».** |
| `[DLIP]` | https://raw.githubusercontent.com/ahkarami/Deep-Learning-in-Production/master/README.md | Практика деплоя DL: конвертация моделей (TorchScript, ONNX), сервинг, оптимизация. **Тоже указан Т-Банком.** |
| `[KHAN]` | https://raw.githubusercontent.com/khangich/machine-learning-interview/master/README.md | Minimum Viable Study Plan для ML-интервью. Явная секция **«Big data (NOT required for Google, Facebook interview)»** — важный сигнал про региональную разницу требований. |
| `[MLOPSZC]` | https://raw.githubusercontent.com/DataTalksClub/mlops-zoomcamp/main/README.md | Программа MLOps Zoomcamp: 6 модулей — Intro → **Experiment Tracking & Model Management** → **Orchestration & ML Pipelines** → **Model Deployment** → **Model Monitoring** → **Best Practices**. Лучшая внешняя опора для рубрикации глав. |
| `[MWML]` | https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/README.md | Made With ML: Design · Develop · Deploy · Iterate. |
| `[EY]` | https://raw.githubusercontent.com/eugeneyan/applied-ml/main/README.md | 104 КБ ссылок на инженерные блоги реальных компаний по прод-ML (Netflix, Uber, Airbnb, LinkedIn, DoorDash…) — сырьё для кейсов «как в проде на самом деле». |
| `[AWMLOPS]` | https://raw.githubusercontent.com/visenger/awesome-mlops/master/README.md | 74 КБ — карта MLOps-инструментов и статей. |
| `[DAIR]` | https://raw.githubusercontent.com/dair-ai/MLOPs-Primer/main/README.md | MLOps Primer. |
| `[MLDP]` | https://raw.githubusercontent.com/GoogleCloudPlatform/ml-design-patterns/master/README.md | Код к книге «Machine Learning Design Patterns» — **прямо рекомендована Т-Банком** для секции дизайна ML-систем. |
| `[EVID]` | https://raw.githubusercontent.com/evidentlyai/evidently/main/README.md | Evidently — эталонный инструмент мониторинга дрейфа/качества данных. |
| `[ALIBI]` | https://raw.githubusercontent.com/SeldonIO/alibi-detect/master/README.md | 26 КБ: каталог детекторов дрейфа и outlier-детекции — **источник названий тестов (KS, MMD, Chi-Squared, Least-Squares Density Difference, Learned Kernel, Context-aware MMD)**. |
| `[STAS]` | https://raw.githubusercontent.com/stas00/ml-engineering/master/README.md | «Machine Learning Engineering Open Book» — оглавление: Hardware (Compute/Storage/Network) → **Orchestration (SLURM)** → Training → **Inference** → Debugging → Testing. |
| `[STAS-P]` | https://raw.githubusercontent.com/stas00/ml-engineering/master/training/performance/README.md | 63 КБ про производительность обучения — база для вопросов про DDP/FSDP/ZeRO и утилизацию GPU. |
| `[JUN]` | https://raw.githubusercontent.com/junfanz1/Software-Engineer-Coding-Interviews/main/README.md | DSA + (GenAI/ML) System Design + DevOps. |
| `[EHER]` | https://raw.githubusercontent.com/eherrerosj/mle-tech-interviews/master/README.md | MLE tech interview prep: DSA + System Design + SQL. |
| `[BICC]` | https://raw.githubusercontent.com/bicced/ai-engineer-interview-handbook/main/README.md | AI Engineer / Forward Deployed Engineer (OpenAI, Anthropic, Palantir) — соседний профиль роли. |
| `[ASH]` | https://raw.githubusercontent.com/ashishtele/Quick-Notes-for-ML-DS/master/README.md | Quick Notes for ML, DS, **MLOps, LLMOps**. |
| `[SHARP]` | https://raw.githubusercontent.com/sharpest-minds/data-interview-questions/master/README.md | SharpestMinds community: DS/DA/DE/ML. |
| `[AG-T]` | https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/technical.md | Technical-секция: 11 SQL-задач + Python + алгоритмы. **Проверено: Spark/распределённых/деплойных вопросов там нет** — ещё один негативный результат. |

#### A5. Поисковые страницы GitHub (просмотрены для отбора репозиториев)

| URL | Что дало |
|---|---|
| https://github.com/search?q=MLOps+interview+questions&type=repositories&s=stars&o=desc | Нашёл `SepidehHosseinian`, `Devinterview-io/mlops`, `pubalisen`, `JustInCache`, `bicced`, `devflash101`. |
| https://github.com/search?q=data+engineering+interview+questions&type=repositories&s=stars&o=desc | Нашёл `OBenner/data-engineering-interview-questions` (1.7k★, 2000+ вопросов). |
| https://github.com/search?q=вопросы+с+собеседований&type=repositories&s=stars&o=desc | Нашёл `Hexlet/ru-interview-questions`, `epishchik/ML-Interview`, **`andreyyarigin/de-interview-questions`**. |
| https://github.com/search?q=spark+interview+questions&type=repositories&s=stars&o=desc | Подтвердил, что OBenner — крупнейший открытый Spark-банк. |
| https://github.com/Devinterview-io | 173 репозитория; проверено, что тематических repo по Kafka/Airflow/MLflow/Big Data у них **нет** (404). |

### B. Видел только сниппет поисковой выдачи (домен вернул 403 на фетч)

Всё, что взято отсюда, помечено ниже тегом `[snippet]`. Формулировки вопросов оттуда я **не**
привожу как «дословный вопрос с собеса» — только факты/пороги/термины, которые дословно были в сниппете.

| URL | Что дал сниппет |
|---|---|
| https://habr.com/ru/companies/X5Tech/articles/572596/ | Собеседование на Data Engineer **в X5** — в сниппете: «дисбаланс данных, поиск узких мест, оптимизация вычислений, разные виды join в Spark». |
| https://habr.com/ru/companies/X5Tech/articles/584966/ | Часть 2 того же цикла. |
| https://habr.com/ru/articles/828984/ | «Вопросы по Apache Spark к собеседованиям для Data Engineer»: партиционирование, shuffle, **salting** при skew, `spark.sql.shuffle.partitions`. |
| https://datatalks.ru/pyspark-interview-questions-and-answers/ | PySpark Interview (RU): конфиги для оптимизации shuffle-партиций. |
| https://habr.com/ru/companies/otus/articles/859006/ | «5 вопросов на собеседовании на роль ML Team Lead»: MLflow, CI/CD, DVC, FastAPI+Docker+ECS, Evidently AI; «модель без мониторинга — бомба с таймером». |
| https://habr.com/ru/companies/ruvds/articles/990814/ | «MLOps — дитя DevOps и ML»: типы дрейфа (признаков / концептуальный / предсказаний), тесты KS, **PSI**, дивергенция Йенсена–Шеннона; Evidently AI / Fiddler / WhyLabs; стратегии ретрейна. |
| https://www.statstest.com/drift-detection-ks-test-psi-interpret-signals | Пороги PSI: <0.1 / 0.1–0.25 / >0.25. |
| https://www.fiddler.ai/blog/measuring-data-drift-population-stability-index | Альтернативная шкала PSI: <0.1 / 0.1–0.2 / >0.2. |
| https://www.systemoverflow.com/learn/ml-training-infrastructure/continuous-training/drift-detection-and-staleness-budgets | «drift sustained over sufficient sample size before triggering retrain» — против «retraining storms». |
| https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring | Мониторинг прод-ML (Google ML Crash Course). |
| https://building.nubank.com/dealing-with-train-serve-skew-in-real-time-ml-models-a-short-guide/ | Nubank про train-serve skew в реалтайм-моделях. |
| https://www.conduktor.io/glossary/exactly-once-semantics-in-kafka | EOS: `enable.idempotence=true` + Transactional API; PID + sequence number на партицию. |
| https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/optimization.html | Triton dynamic batching: `preferred_batch_size`, `max_queue_delay_microseconds`. |
| https://github.com/triton-inference-server/tutorials/blob/main/Conceptual_Guide/Part_2-improving_resource_utilization/README.md | Улучшение утилизации ресурсов в Triton. |
| https://www.gmicloud.ai/en/blog/torchserve-vs-triton-pytorch | TorchServe (только PyTorch, TorchScript, dynamic batching) vs Triton (мультибэкенд, continuous batching). |
| https://dev.to/datanestdigital/spark-optimization-playbook-adaptive-query-execution-aqe-tuning-guide-166f | AQE: реоптимизация после shuffle, coalesce мелких партиций, смена стратегии join. |
| https://datavidhya.com/blog/apache-spark-data-engineering-interview-questions/ | «70 Spark Interview Questions (Real Asks, 2026)»; правило `spark.sql.shuffle.partitions` ≈ 2–4 × cores. |
| https://oneuptime.com/blog/post/2026-01-30-mlops-model-rollback/view | Цель отката < 5 минут от решения до старой версии в проде. |
| https://mljar.com/ai-prompts/mlops/production-incident-response/ | P1-инциденты: p99 > 2× SLA >10 мин, error rate >1 %, PSI > 0.5, тихая деградация >10 %. |
| https://www.multisoftsystems.com/interview-questions/top-30-apache-airflow-interview-questions-answers-2026 | Идемпотентность, backfill, `retry_exponential_backoff`. |
| https://apxml.com/courses/feature-stores-for-ml/chapter-3-data-consistency-quality/point-in-time-correctness | Point-in-time correctness и «time travel»-утечка. |
| https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines | FTI-разбиение: Feature / Training / Inference пайплайны. |
| https://engineeringenablement.substack.com/p/ml-system-design-interview-questions | Что реально спрашивают на ML System Design. |
| https://yandex.ru/jobs/pages/mldev-interview | Яндекс: «3–4 технические встречи», трек подбирается индивидуально. |
| https://sberdevices.ru/career/ML/interview/ | SberDevices: этапы; в сниппете — «обсуждение инференса и его ускорения». |
| https://karpov.courses/ml-design | Курс ML System Design Валерия Бабушкина; этапы: постановка задачи и baseline → дата-пайплайн и генерация фичей → тренировочный пайплайн → интеграция и API → мониторинг → разбор ошибок и поддержка. |
| https://www.youtube.com/watch?v=VPg2Uu1MYgI | Открытое mock-собеседование по ML System Design (karpov.courses). |
| https://www.youtube.com/watch?v=zBRsgZgDeIk | Mock-собеседование ML System Design с Team Lead Яндекса. |

---

## Вопросы с собеседований

> Формат строки: **вопрос** — `грейд` — источник — (компания, если известна).
> Английские формулировки оставлены как есть — так их и задают; русские — как в источнике.

---

### 1. MLOps: базовые понятия и жизненный цикл

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 1.1 | What is MLOps and how does it differ from DevOps? | junior | `[DI-MLOPS]` Q1, `[SEP-G]` Q2, `[DI-LLMOPS]` Q1 |
| 1.2 | What is the difference between MLOps, ModelOps, and AIOps? | junior | `[SEP-G]` Q1, Q18 |
| 1.3 | Can you explain the MLOps lifecycle and its key stages? | junior | `[DI-MLOPS]` Q2 |
| 1.4 | Define the term "Lifecycle" within the context of MLOps. | junior | `[DI-LLMOPS]` Q2 |
| 1.5 | Describe the typical stages of the machine learning lifecycle. | junior | `[DI-LLMOPS]` Q3 |
| 1.6 | What are some of the benefits of implementing MLOps practices in a machine learning project? | junior | `[DI-MLOPS]` Q3, `[SEP-G]` Q19 |
| 1.7 | Can You Tell Me The Components Of MLOps? | junior | `[SEP-G]` Q20 |
| 1.8 | What are the key components of a robust MLOps infrastructure? | middle | `[DI-LLMOPS]` Q4 |
| 1.9 | How Do Data Scientists, Data Engineers, And ML Engineers Vary From One Another? | junior | `[SEP-G]` Q17 |
| 1.10 | What are DataOps and how do they relate to MLOps? | middle | `[DI-MLOPS]` Q7 |
| 1.11 | How Many Different Ways May MLOps Be Applied, In Your Opinion? / How many ways do you know to implement MLOps? | middle | `[SEP-G]` Q23, `[SEP-T]` Q1 |
| 1.12 | Describe The Enterprise-Level Applications Of The MLOps Lifecycle? | middle_plus | `[SEP-G]` Q31 |
| 1.13 | Can you explain the concept of MLOps and its importance in the industry? | junior | `[SEP-D]` |
| 1.14 | What Risks Come With Using Data Science? | middle | `[SEP-G]` Q21 |
| 1.15 | How do you stay current with the latest developments and trends in MLOps? | junior | `[SEP-D]` |
| 1.16 | What is LLMOps, and how does it differ from traditional MLOps? | middle | `[PUB]` LLMOps, `[JIC]` Q37, `[CM-LLMOPS]` |
| 1.17 | Explain the AI product lifecycle from ideation to production. | middle | `[PUB]` LLMOps |
| 1.18 | What is AI Engineering, and how does it differ from Machine Learning Engineering? | junior | `[PUB]` Behavioral |

---

### 2. Упаковка модели и артефакты

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 2.1 | What are the ways of packaging ML Models? | middle | `[SEP-G]` Q13 |
| 2.2 | Why you should package ML models? | junior | `[SEP-G]` Q34 |
| 2.3 | What is a structure of a typical ML Artifact? | middle | `[SEP-G]` Q36 |
| 2.4 | How do you package model artifacts? | middle | `[VENK]` |
| 2.5 | Difference between saving ML model & packaging a model? What are different formats for packaging model? | middle | `[VENK]` |
| 2.6 | What is an MLflow *flavor* and why does it matter? | middle | `[CM-MLF]` Q3 |
| 2.7 | What is the `mlflow.models.infer_signature` function and why should you use it? | middle | `[CM-MLF]` Q5 |
| 2.8 | What are the pros and cons of using Microservices? (в контексте «модель как микросервис») | middle | `[SEP-G]` Q35 |
| 2.9 | Cloud vs on-device Model Deployment for AI applications. | middle | `[PUB]` LLMOps |
| 2.10 | How do you optimize inference for edge and mobile deployment? | middle_plus | `[PUB]` Infra |
| 2.11 | Can you discuss an experience you have had with deploying machine learning models on edge devices? | middle_plus | `[SEP-D]` |
| 2.12 | How would you convert a PyTorch model for production (TorchScript / ONNX) and what breaks in the process? | middle_plus | `[DLIP]` (раздел «Convert PyTorch Models in Production») |
| 2.13 | `[snippet]` Как ONNX и TensorRT соотносятся: ONNX — мост, TensorRT — компилятор движка под NVIDIA (FP16/INT8, kernel fusion)? | middle_plus | `[snippet]` medium/@linghuang_76674 |

---

### 3. Сервинг: REST / gRPC / FastAPI / TorchServe / Triton

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 3.1 | What are the tradeoffs between REST and gRPC for model serving? | middle_plus | `[CM-SERV]` Q5 |
| 3.2 | Have you worked with any tools or platforms for model deployment and serving, such as TensorFlow Serving, Seldon, or Clipper? | middle | `[SEP-D]` |
| 3.3 | Have you worked with any tools or platforms for MLOps, such as TensorFlow Serving, Kubernetes, or SageMaker? | junior | `[SEP-D]` |
| 3.4 | How do you serve LLMs in production? | middle_plus | `[PUB]` LLMOps |
| 3.5 | Why use FastAPI for LLM backends instead of Flask or Django? | middle | `[CM-API]` |
| 3.6 | How do you implement streaming LLM responses in FastAPI? | middle_plus | `[CM-API]` |
| 3.7 | What's the difference between SSE and WebSockets for LLM streaming? | middle_plus | `[CM-API]` |
| 3.8 | How do you implement rate limiting for an LLM API? / How do you implement rate limiting and throttling for LLM APIs? | middle | `[CM-API]`, `[PUB]` LLMOps |
| 3.9 | How would you design a fault-tolerant LLM backend? | middle_plus | `[CM-API]` |
| 3.10 | What is the difference between synchronous and asynchronous inference, and when do you use each? | middle | `[PUB]` Infra |
| 3.11 | How do you implement request queuing and priority scheduling for AI services? | middle_plus | `[PUB]` Infra |
| 3.12 | How do you handle cold start latency for serverless AI deployments? | middle_plus | `[PUB]` Infra |
| 3.13 | Can you discuss your experience with using serverless or FaaS (Function as a Service) in MLOps? | middle | `[SEP-D]` |
| 3.14 | What is a gateway pattern for LLM API management? / Design an AI gateway/proxy for managing LLM access across an organization | middle_plus | `[PUB]` LLMOps, Arch |
| 3.15 | What is semantic routing, and how do you implement it in a multi-model system? | middle_plus | `[PUB]` LLMOps |
| 3.16 | What is model routing at the infrastructure level, and how do you route requests based on complexity and cost? | middle_plus | `[PUB]` Infra |
| 3.17 | How do you manage GPU memory for serving multiple models? | middle_plus | `[PUB]` Infra |
| 3.18 | `[snippet]` Чем Triton отличается от TorchServe/TF Serving (мультибэкенд vs один фреймворк) и что даёт continuous batching? | middle_plus | `[snippet]` gmicloud.ai, ai.aioz.io |
| 3.19 | `[snippet]` Как настраивается dynamic batching в Triton (`preferred_batch_size`, `max_queue_delay_microseconds`) и как это влияет на p99? | middle_plus | `[snippet]` docs.nvidia.com |

---

### 4. Batch vs online vs streaming inference

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 4.1 | What is the difference between batch and real-time inference? | junior | `[CM-SERV]` Q1 |
| 4.2 | What's the difference between Batch Processing and Stream Processing? / What Distinguishes Stream Processing From Batch Processing? | middle | `[SEP-T]` Q4, `[SEP-G]` Q26 |
| 4.3 | What's the difference between Static Deployment and Dynamic Deployment? / What Separates Static Deployment From Dynamic Deployment? | middle | `[SEP-T]` Q2, `[SEP-G]` Q24 |
| 4.4 | How would you choose between batch inference, real-time inference, and asynchronous inference? | middle_plus | `[CM-26A]` Q16 |
| 4.5 | What's the difference between microbatch and streaming? | middle | `[CM-PIPE]` |
| 4.6 | Why not just use real-time/streaming for everything? | middle_plus | `[CM-PIPE]` |
| 4.7 | When would you pick batch over streaming even though streaming is "better"? | middle_plus | `[CM-PIPE]` |
| 4.8 | What is near real-time and when is it the right choice? | middle | `[CM-PIPE]` |
| 4.9 | What makes data quality harder in streaming than in batch? | middle_plus | `[CM-PIPE]` |
| 4.10 | What are watermarks and why do they matter? | middle_plus | `[CM-PIPE]`, `[OB-FLINK]` («What is Watermark in Flink?») |
| 4.11 | Зачем нужен Spark Structured Streaming, если есть Flink? | middle_plus | `[RUDE-SP]` |
| 4.12 | Когда выбирать событийную модель (Kafka), а когда синхронный вызов (gRPC) для загрузки данных? | middle_plus | `[RUDE-OTH]` |

---

### 5. Latency / throughput / оптимизация инференса

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 5.1 | How would you reduce serving latency for a large deep learning model? | middle_plus | `[CM-SERV]` Q6 |
| 5.2 | What is dynamic batching and why is it important for GPU serving? | middle_plus | `[CM-SERV]` Q2 |
| 5.3 | How do you improve inference speed in production LLM deployments? | middle_plus | `[PUB]` Infra |
| 5.4 | How does continuous batching improve LLM inference throughput? | middle_plus | `[PUB]` Infra |
| 5.5 | What is speculative decoding, and how does it speed up inference? | middle_plus | `[PUB]` Infra |
| 5.6 | What is KV cache, and how do you manage memory for it? / What is Paged Attention? | middle_plus | `[PUB]` Infra |
| 5.7 | How does vLLM work? / How does SGLang work? | middle_plus | `[PUB]` LLMOps |
| 5.8 | Prefill vs Decode. | middle_plus | `[PUB]` LLMOps |
| 5.9 | How does Prompt Caching work? / What is prompt caching and how does it reduce costs? | middle | `[PUB]` LLMOps, `[CM-26B]` Q8 |
| 5.10 | How does Token Streaming work? | middle | `[PUB]` LLMOps |
| 5.11 | What is model quantization? / What is model quantization (INT8, INT4, FP16, BF16), and how does it affect quality? | middle | `[PUB]` LLMOps + Infra, `[CM-26A]` Q14 |
| 5.12 | You quantized your LLM, but accuracy dropped significantly. How do you minimize quantization loss? | middle_plus | `[PUB]` LLMOps scenario |
| 5.13 | What is model distillation and when is it useful? | middle | `[CM-26A]` Q13 |
| 5.14 | How do you select GPUs for LLM inference? | middle_plus | `[PUB]` Infra |
| 5.15 | Explain critical GPU performance measures? / What are P States in GPU? | middle_plus | `[VENK]` |
| 5.16 | What are the key SLAs and metrics for production AI systems (latency, throughput, availability)? | middle_plus | `[PUB]` LLMOps |
| 5.17 | How do you monitor and profile LLM inference in production (TTFT, inter-token latency, GPU utilization)? | middle_plus | `[PUB]` Infra, `[JIC]` Q38 |
| 5.18 | Your LLM API has latency spikes during peak hours. How do you stabilize it? | middle_plus | `[PUB]` scenario |
| 5.19 | Your AI system handles 100 requests/sec but crashes at 5000. How do you scale for concurrent requests? | middle_plus | `[PUB]` scenario |
| 5.20 | A traffic spike brings down your AI system. How do you handle peak traffic? | middle_plus | `[PUB]` scenario |
| 5.21 | How do you design for latency vs quality trade-offs in AI systems? | middle_plus | `[PUB]` Arch |
| 5.22 | How do you implement caching strategies for LLM applications? / How do you implement model caching to reduce redundant computations? | middle | `[PUB]` Arch + Infra |
| 5.23 | Describe a time when you had to choose between model accuracy and latency. How did you make the decision? | middle_plus | `[PUB]` Behavioral |
| 5.24 | How do you manage the performance and resource usage of machine learning models in production? | middle | `[SEP-D]` |
| 5.25 | How do you handle model performance and scalability in production? | middle_plus | `[SEP-D]` |
| 5.26 | Как ускорить инференс модели (обсуждение инференса и его ускорения на секции). | middle_plus | `[snippet]` sberdevices.ru — **SberDevices** |

---

### 6. Docker для ML

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 6.1 | What is Docker, and how is it different from virtual machines? | junior | `[DI-DOCKER]` Q1 |
| 6.2 | Can you explain what a Docker image is? / How does a Docker container differ from a Docker image? | junior | `[DI-DOCKER]` Q2–Q3 |
| 6.3 | Explain the Dockerfile and its significance in Docker. | junior | `[DI-DOCKER]` Q5 |
| 6.4 | How does Docker use layers to build images? | middle | `[DI-DOCKER]` Q6 |
| 6.5 | What's the difference between the `COPY` and `ADD` commands in a Dockerfile? | junior | `[DI-DOCKER]` Q7 |
| 6.6 | What's the purpose of the `.dockerignore` file? | junior | `[DI-DOCKER]` Q8 |
| 6.7 | **In practice, how do you reduce the size of Docker images?** (multi-stage, small base, .dockerignore, кэш пакетных менеджеров) | middle | `[DI-DOCKER]` Q10 |
| 6.8 | How would you go about creating a Docker image from an existing container? | middle | `[DI-DOCKER]` Q9 |
| 6.9 | Can you explain what a Docker namespace is and its benefits? | middle | `[DI-DOCKER]` Q12 |
| 6.10 | What is a Docker volume, and when would you use it? | junior | `[DI-DOCKER]` Q13 |
| 6.11 | Explain the use and significance of the `docker-compose` tool. | junior | `[DI-DOCKER]` Q14 |
| 6.12 | Can Docker containers running on the same host communicate with each other by default? If so, how? | middle | `[DI-DOCKER]` Q15 |
| 6.13 | How do containerization and virtualization technologies support MLOps practices? | middle | `[DI-MLOPS]` Q10, `[DI-LLMOPS]` Q10 |
| 6.14 | Can you discuss your experience with using containerization and virtualization technologies in MLOps? | middle | `[SEP-D]` |
| 6.15 | What is Container Op in Kubeflow pipelines? Isn't it too heavy creating containers for every step? | middle_plus | `[VENK]` |
| 6.16 | `[snippet]` Почему CUDA-версия в контейнере должна совпадать с версией обучения и как это ломает загрузку модели? | middle_plus | `[snippet]` lifebit.ai, kodekloud.com |

---

### 7. Kubernetes для ML

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 7.1 | What is Kubernetes, and why is it used for container orchestration? | junior | `[DI-K8S]` Q1 |
| 7.2 | Что такое Kubernetes? Для чего используют именно такой способ деплоя? | junior | `[RUDE-OTH]` |
| 7.3 | Describe the roles of master and worker nodes in the Kubernetes architecture. | junior | `[DI-K8S]` Q2 |
| 7.4 | How do Pods facilitate the management of containers in Kubernetes? | junior | `[DI-K8S]` Q3 |
| 7.5 | What types of Services exist in Kubernetes, and how do they facilitate pod communication? | middle | `[DI-K8S]` Q4 |
| 7.6 | Differentiate between Deployments, StatefulSets, and DaemonSets. | middle | `[DI-K8S]` Q6 |
| 7.7 | What are Jobs in Kubernetes, and when is it suitable to use them? | middle | `[DI-K8S]` Q8 |
| 7.8 | Что такое контейнеризированные джобы в Kubernetes? Readiness/Liveness пробы для джоб. | middle_plus | `[RUDE-OTH]` |
| 7.9 | What would you consider when performing a rolling update in Kubernetes? | middle_plus | `[DI-K8S]` Q10 |
| 7.10 | Describe the purpose of Ingress and its key components. / How to configure TLS with Ingress? | middle | `[DI-K8S]` Q12, `[OB-K8S]` |
| 7.11 | How do we control the resource usage of POD? | middle | `[OB-K8S]` |
| 7.12 | What is PDB (Pod Disruption Budget)? | middle_plus | `[OB-K8S]` |
| 7.13 | What's the init container and when it can be used? | middle | `[OB-K8S]` |
| 7.14 | **How to troubleshoot if the POD is not getting scheduled?** | middle_plus | `[OB-K8S]` |
| 7.15 | How to run a POD on a particular node? (nodeSelector/affinity — базовый вопрос для GPU-нод) | middle | `[OB-K8S]` |
| 7.16 | How to do maintenance activity on the K8 node? | middle_plus | `[OB-K8S]` |
| 7.17 | How to monitor the Kubernetes cluster? / How to get the central logs from POD? | middle | `[OB-K8S]` |
| 7.18 | What are the various things that can be done to increase Kubernetes security? | middle_plus | `[OB-K8S]` |
| 7.19 | What is an Operator? Why do we need Operators? | middle_plus | `[OB-K8S]` |
| 7.20 | Why use namespaces? What is the problem with using the default namespace? | middle | `[OB-K8S]`, `[DI-K8S]` Q5 |
| 7.21 | What is the difference between Docker Swarm and Kubernetes? | junior | `[OB-K8S]` |
| 7.22 | How do you implement Network Policies, and what are their benefits? | middle_plus | `[DI-K8S]` Q15 |
| 7.23 | Can you discuss your experience with using Kubernetes or other container orchestration platforms in MLOps? | middle | `[SEP-D]` |
| 7.24 | How do you implement auto-scaling for AI workloads? / Can you discuss an experience you have had with implementing auto-scaling for machine learning models in production? | middle_plus | `[PUB]` Infra, `[SEP-M]` |
| 7.25 | What is the role of load balancing in AI serving infrastructure? | middle | `[PUB]` Infra |
| 7.26 | How to use AWS EFS to store training datasets and make it available for Kubeflow pods? How to sync data between S3 to EFS? | middle_plus | `[VENK]` |
| 7.27 | Kubeflow Pipelines vs Jobs | middle | `[VENK]` |

---

### 8. CI/CD для ML, тестирование, воспроизводимость

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 8.1 | Explain the concept of continuous integration and continuous delivery (CI/CD) in the context of machine learning. | middle | `[DI-MLOPS]` Q6, `[DI-LLMOPS]` Q7 |
| 8.2 | How can you create CI/CD pipelines for Machine Learning? | middle | `[SEP-G]` Q4 |
| 8.3 | What is CI/CD for AI applications, and how does it differ from traditional CI/CD? | middle | `[PUB]` LLMOps |
| 8.4 | Can you discuss an experience you have had with implementing continuous integration and delivery for machine learning models? | middle | `[SEP-D]` |
| 8.5 | Тестирование и CI/CD для Data-пайплайнов | middle_plus | `[RUDE-ETL]` |
| 8.6 | Какие есть паттерны тестирования в дата-инжиниринге (интеграционные, нагрузочные, Property-based)? | middle_plus | `[RUDE-OTH]` |
| 8.7 | **What testing should be done before deploying an ML model into production?** | middle_plus | `[SEP-G]` Q7 |
| 8.8 | Can you walk me through your approach to testing and validation for machine learning models? | middle | `[SEP-D]` |
| 8.9 | How do you build a regression test suite for AI applications? | middle_plus | `[PUB]` Eval |
| 8.10 | How does MLOps facilitate reproducibility in machine learning projects? | middle | `[DI-LLMOPS]` Q5 |
| 8.11 | Explain environment reproducibility and its challenges in MLOps. | middle_plus | `[DI-MLOPS]` Q14 |
| 8.12 | How do you ensure the reproducibility of machine learning experiments? | middle | `[SEP-D]` |
| 8.13 | How do you reproduce an MLflow run exactly? | middle_plus | `[CM-MLF]` Q10 |
| 8.14 | An external auditor cannot reproduce your model's results. How do you ensure audit reproducibility? | middle_plus | `[PUB]` Eval scenario |
| 8.15 | What is the concept of "Immutable Infrastructure"? | middle_plus | `[SEP-G]` Q14 |
| 8.16 | How does infrastructure as code (IaC) support machine learning operations? | middle_plus | `[DI-MLOPS]` Q15 |
| 8.17 | How do you create Infrastructure in MLOps? | middle | `[SEP-G]` Q3 |
| 8.18 | What is the importance of using version control for MLOps? | junior | `[SEP-G]` Q9 |
| 8.19 | How do you handle version control for machine learning models? | middle | `[SEP-D]` |
| 8.20 | Что такое виртуальные окружения и зачем они нужны? | junior | `[RUDE-PY]` |

---

### 9. Реестр моделей, трекинг экспериментов, версионирование данных

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 9.1 | What is a model registry and what role does it play in MLOps? / What Do You Mean By Model Registry? | junior | `[DI-MLOPS]` Q4, `[SEP-G]` Q28, `[SEP-T]` Q6 |
| 9.2 | Can You Elaborate On The Benefits Of Model Registry? | middle | `[SEP-G]` Q29 |
| 9.3 | Describe the function of model registries in MLOps. | junior | `[DI-LLMOPS]` Q11 |
| 9.4 | Where are models stored in Kubeflow? What is a model registry (or model repository)? Are your models stored in S3? What are popular tools for model store/registry? How are models versioned? | middle_plus | `[VENK]` |
| 9.5 | What are typical containers behind Kubeflow Model Registry? / How to choose between Kubeflow Model Registry and Hugging Face Model Hub? | middle_plus | `[VENK]` |
| 9.6 | Describe the significance of experiment tracking in MLOps. | junior | `[DI-MLOPS]` Q8 |
| 9.7 | What is the difference between an MLflow experiment and a run? | junior | `[CM-MLF]` Q1 |
| 9.8 | How does the MLflow Model Registry differ from just storing model artifacts in a run? | middle | `[CM-MLF]` Q2 |
| 9.9 | What backends does MLflow support for storing tracking data and artifacts? | middle | `[CM-MLF]` Q7 |
| 9.10 | How would you set up MLflow in a team environment? | middle_plus | `[CM-MLF]` Q8 |
| 9.11 | What is the difference between `mlflow.log_metric` with a `step` parameter and without? | middle | `[CM-MLF]` Q9 |
| 9.12 | What are the limitations of MLflow autologging? | middle_plus | `[CM-MLF]` Q11 |
| 9.13 | How does MLflow handle experiment tracking in a distributed training environment? | middle_plus | `[CM-MLF]` Q6 |
| 9.14 | How would you implement a blue-green deployment strategy using MLflow? | middle_plus | `[CM-MLF]` Q4 |
| 9.15 | How to setup experiments in Kubeflow? | middle | `[VENK]` |
| 9.16 | Have you worked with any tools or platforms for model governance, such as MLflow or ModelDB? | middle | `[SEP-D]` |
| 9.17 | Have you worked with any tools or platforms for model tracking and management, such as DataRobot or Algorithmia? | middle | `[SEP-D]` |
| 9.18 | What role does data versioning play in MLOps? | middle | `[DI-LLMOPS]` Q6 |
| 9.19 | How do you handle versioning and rollback of data sets in MLOps? | middle_plus | `[SEP-D]` |
| 9.20 | How do you handle data lineage and traceability in an MLOps pipeline? | middle_plus | `[SEP-D]` |
| 9.21 | What is model versioning, and how do you handle model rollbacks? | middle | `[PUB]` LLMOps |
| 9.22 | How do you version and manage prompts in production? / Build a simple prompt versioning system. | middle | `[PUB]` LLMOps + Coding |
| 9.23 | Как работает версионирование в MinIO? В каких случаях применяется? | middle | `[RUDE-OTH]` |

---

### 10. Стратегии деплоя: shadow / canary / blue-green / A-B / champion-challenger

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 10.1 | What is the difference between Canary and Blue-Green strategies of deployment? | middle | `[SEP-G]` Q11 |
| 10.2 | Can you explain the concept of "canary deployment" and how it can be used in MLOps? | middle | `[SEP-D]` |
| 10.3 | Can you explain the concept of "blue-green deployment" and how it can be used in MLOps? | middle | `[SEP-D]` |
| 10.4 | Can you explain the concept of "dark launching" and how it can be used in MLOps? | middle_plus | `[SEP-D]` |
| 10.5 | How do you do a canary deployment for an ML model? | middle_plus | `[CM-SERV]` Q3 |
| 10.6 | What is shadow mode and when would you use it? | middle_plus | `[CM-SERV]` Q4 |
| 10.7 | What production Testing methods do you know? / What Production Testing Techniques Are You Aware Of? (batch test / A-B test / stage-shadow test) | middle_plus | `[SEP-T]` Q3, `[SEP-G]` Q25 |
| 10.8 | Can You Explain how The Champion-Challenger Technique Works? | middle_plus | `[SEP-G]` Q30 |
| 10.9 | What is the difference between A/B testing model deployment and Multi-Arm Bandit? | middle_plus | `[SEP-G]` Q10 |
| 10.10 | Can you discuss an experience you have had with A/B testing or multi-armed bandit approaches? / …with implementing A/B testing or multi-armed bandit approaches in production? | middle_plus | `[SEP-D]` (дважды) |
| 10.11 | What is the A/B split approach of model evaluation? | middle | `[SEP-G]` Q8 |
| 10.12 | How do you handle rollbacks and roll forwards in an MLOps pipeline? | middle_plus | `[SEP-D]` |
| 10.13 | How do you handle model updates and migrations without downtime? | middle_plus | `[PUB]` LLMOps |
| 10.14 | What is the role of feature flags in AI deployments? | middle | `[PUB]` LLMOps |
| 10.15 | How do you implement A/B testing for LLM systems? / How would you A/B test a new LLM model vs the existing one? | middle_plus | `[PUB]` LLMOps, `[CM-26B]` Q19 |
| 10.16 | How would you design an A/B test for a recommendation model? | middle_plus | `[CM-AB]` |
| 10.17 | What is a Sample Ratio Mismatch (SRM) and why is it critical? | middle_plus | `[CM-AB]` |
| 10.18 | When would you use CUPED? | middle_plus | `[CM-AB]` |
| 10.19 | The test shows p=0.03 but you checked yesterday and p=0.06. What happened? (peeking) | middle_plus | `[CM-AB]` |
| 10.20 | How do you determine how long to run an A/B test? | middle | `[CM-AB]` |
| 10.21 | How do you handle model deployments in multi-cloud or hybrid environments? | middle_plus | `[SEP-D]` |
| 10.22 | Can you discuss an experience you have had with using cloud-based platforms for MLOps, such as AWS SageMaker, GCP ML Engine, or Azure ML? | middle | `[SEP-D]` |
| 10.23 | What is the role of cloud computing in MLOps? | junior | `[DI-MLOPS]` Q11 |

---

### 11. Feature store и train/serve skew

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 11.1 | What are feature stores, and why are they important in MLOps? | middle | `[DI-MLOPS]` Q5, `[DI-LLMOPS]` Q14 |
| 11.2 | Can you explain the concept of "feature store" and its role in MLOps? | middle | `[SEP-D]` |
| 11.3 | What problem does a feature store solve? | middle | `[CM-FS]` Q1 |
| 11.4 | **What is point-in-time correctness and why does it matter?** | middle_plus | `[CM-FS]` Q2 |
| 11.5 | What is the difference between online and offline feature stores? | middle | `[CM-FS]` Q3 |
| 11.6 | How does feature freshness work in a feature store? | middle_plus | `[CM-FS]` Q4 |
| 11.7 | How would you implement a feature store for a fraud detection system? | middle_plus | `[CM-FS]` Q5 |
| 11.8 | **What Do You Mean By Training Serving Skew? / What is Training-Serving Skew?** | middle_plus | `[SEP-G]` Q27, `[SEP-T]` Q5 |
| 11.9 | Explain the concept of a data pipeline and its role in MLOps. | junior | `[DI-LLMOPS]` Q15 |
| 11.10 | How do you handle data pipeline and feature engineering in an MLOps pipeline? | middle | `[SEP-D]` |
| 11.11 | How do you handle data pipeline and feature engineering for time-series data in an MLOps pipeline? | middle_plus | `[SEP-M]` |
| 11.12 | What are steps/tasks in "Data Acquisition" and "Data preparation & processing" pipelines? What are steps in "feature engineering" pipelines? | middle | `[VENK]` |
| 11.13 | Explain the CAP theorem's relevance to ML feature stores. | middle_plus | `[CM-26B]` Q12 |
| 11.14 | Что такое признаки для ML-модели? Как дата-инженер участвует в их подготовке? | middle | `[RUDE-OTH]` |
| 11.15 | What is data leakage in modern ML systems? | middle | `[CM-26A]` Q17 |
| 11.16 | How do you handle data labeling and annotation in an MLOps pipeline? | middle | `[SEP-D]` |

---

### 12. Мониторинг, дрейф, деградация, алерты

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 12.1 | What is model or concept drift? / Can You Explain, What Is Model Drift? | junior | `[SEP-G]` Q5, Q22 |
| 12.2 | **What is the difference between data drift and concept drift?** | middle | `[CM-DQ]` Q1 |
| 12.3 | How do you handle data drift and concept drift in an MLOps pipeline? | middle_plus | `[SEP-D]` |
| 12.4 | Can you discuss an experience you have had with data drift and how you addressed it? / Can you discuss an example with data drift and how it can be addressed? | middle | `[SEP-D]`, `[SEP-G]` Q33 |
| 12.5 | **What is PSI (Population Stability Index) and how do you interpret it?** | middle | `[CM-DQ]` Q3 |
| 12.6 | How does monitoring differ from logging? | middle | `[SEP-G]` Q6 |
| 12.7 | Discuss the importance of monitoring and logging in MLOps. | junior | `[DI-LLMOPS]` Q8 |
| 12.8 | **Why would you monitor feature attribution rather than feature distribution?** | middle_plus | `[SEP-G]` Q12 |
| 12.9 | Can you explain how to monitor the performance of an ML model over time? | middle | `[SEP-G]` Q32 |
| 12.10 | How do you monitor and troubleshoot machine learning models in production? | middle | `[SEP-D]` |
| 12.11 | How do you monitor and alert on machine learning model performance? | middle_plus | `[SEP-D]` |
| 12.12 | How do you measure and improve the performance of machine learning models in production? | middle | `[SEP-D]` |
| 12.13 | How would you monitor an ML model after deployment? | middle | `[CM-26A]` Q18 |
| 12.14 | How would you monitor data quality in a production ML pipeline? | middle_plus | `[CM-DQ]` Q2 |
| 12.15 | **What are data contracts and why are they important?** | middle_plus | `[CM-DQ]` Q4 |
| 12.16 | How do you handle schema drift in an ML pipeline? | middle_plus | `[CM-DQ]` Q5 |
| 12.17 | Как алертить на аномалии в данных (падение объёма, нарушение схем) в контексте Data Quality? | middle_plus | `[RUDE-OTH]` |
| 12.18 | Data Quality — автоматизация проверок в ELT-конвейере | middle_plus | `[RUDE-ETL]` |
| 12.19 | Что такое «золотые сигналы» в мониторинге? Какие важны для ETL-процессов? | middle_plus | `[RUDE-OTH]` |
| 12.20 | Мониторинг дата-платформы — от инфраструктуры до бизнес-метрик | middle_plus | `[RUDE-OTH]` |
| 12.21 | Как отследить путь одного события через всю цепочку трансформаций в OpenTelemetry/Jaeger? | middle_plus | `[RUDE-OTH]` |
| 12.22 | How do you implement logging and tracing for LLM applications? | middle | `[PUB]` LLMOps |
| 12.23 | What is LLM observability? / How do you monitor LLM applications in production? | middle_plus | `[PUB]` LLMOps, `[JIC]` Q38, `[CM-26B]` Q10 |
| 12.24 | What is model drift in production LLM systems, and how do you detect it? (upstream model drift / prompt drift / RAG staleness / query distribution shift) | middle_plus | `[CM-26B]` Q11 |
| 12.25 | Your AI pipeline has zero visibility into which step is failing. How do you add observability? | middle_plus | `[PUB]` scenario |
| 12.26 | Your model was fair at deployment, but became biased 6 months later. How do you monitor continuously? | middle_plus | `[PUB]` Eval scenario |
| 12.27 | What metrics matter for a production ML or AI service besides accuracy? | middle | `[CM-26A]` Q11 |
| 12.28 | What is the difference between offline evaluation and online evaluation? | middle | `[CM-26A]` Q21, `[PUB]` Eval |
| 12.29 | What is calibration and why can it matter more than accuracy? | middle_plus | `[CM-26A]` Q22 |
| 12.30 | Can you discuss an experience you have had with implementing model monitoring and feedback loops? | middle_plus | `[SEP-D]` |
| 12.31 | How do you implement continuous evaluation for production AI systems? | middle_plus | `[PUB]` Eval |
| 12.32 | `[snippet]` Пороги PSI: <0.1 — минимальный дрейф, 0.1–0.25 — умеренный, >0.25 — значимый (у Fiddler: >0.2 — «строить новую модель»). Как обосновать выбранный порог? | middle_plus | `[snippet]` statstest.com, fiddler.ai |
| 12.33 | `[snippet]` Почему KS-тест «пересрабатывает» на больших выборках и что с этим делать? | middle_plus | `[snippet]` statstest.com |
| 12.34 | Какие детекторы дрейфа вы знаете кроме KS и PSI? (MMD, Chi-Squared, Least-Squares Density Difference, Learned Kernel MMD, Context-aware MMD) | middle_plus | `[ALIBI]` |

---

### 13. Ретрейн, continual learning, инциденты

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 13.1 | How do you handle model drift and retraining in production? | middle_plus | `[SEP-D]` |
| 13.2 | Кто/что триггерит переобучение: расписание, детекция дрейфа или онлайн-обучение? | middle_plus | `[snippet]` habr ruvds 990814 |
| 13.3 | How would you handle a situation where your AI system's quality degrades over time? | middle_plus | `[PUB]` Behavioral |
| 13.4 | Continual training: train from scratch or from a base model? How often — daily, weekly, monthly? | middle_plus | `[ALZ]` §9 |
| 13.5 | What is the role of human-in-the-loop systems in AI products? | middle | `[CM-26A]` Q19 |
| 13.6 | Active learning / Human in the loop ML — когда и зачем встраивать в цикл обновления? | middle_plus | `[ALZ]` §9 |
| 13.7 | How do you handle failover and fallback strategies for AI systems? / How do you implement fallback strategies when the primary model is unavailable or rate-limited? | middle_plus | `[PUB]` Arch + LLMOps |
| 13.8 | How do you design an AI system for high availability and fault tolerance? | middle_plus | `[PUB]` Arch |
| 13.9 | How do you design an AI system that gracefully degrades when the model is unavailable? / One failing AI component can take down your entire platform. How do you design graceful degradation? | middle_plus | `[PUB]` Arch + scenario |
| 13.10 | One LLM provider outage took down your entire system. How do you eliminate single points of failure? | middle_plus | `[PUB]` scenario |
| 13.11 | Your application depends on one LLM provider. How do you switch providers without downtime? | middle_plus | `[PUB]` scenario |
| 13.12 | Your multi-LLM pipeline fails when one model in the chain breaks. How do you handle orchestration failure? | middle_plus | `[PUB]` scenario |
| 13.13 | How would you design an AI incident response plan? | middle_plus | `[PUB]` Safety |
| 13.14 | System failures: SW system failure (dependency, deployment, hardware, downtime) vs ML system failure (train/serve distribution difference, feedback loops, edge cases, junk input). Какие алармы вы поставите на каждый класс? | middle_plus | `[ALZ]` §9 |
| 13.15 | Mention some common issues involved in ML model deployment. | middle | `[SEP-G]` Q15 |
| 13.16 | What are the challenges associated with model deployment and how does MLOps address them? | middle | `[DI-LLMOPS]` Q12 |
| 13.17 | Can you discuss an experience you have had with deploying machine learning models at scale? | middle_plus | `[SEP-D]` |
| 13.18 | `[snippet]` Какие пороги вы поставите в P1: p99 > 2× SLA дольше 10 минут, error rate > 1 %, PSI > 0.5, тихая деградация accuracy > 10 %? SLA ответа — 15 мин на ack, 4 ч на митигацию. | middle_plus | `[snippet]` mljar.com |
| 13.19 | `[snippet]` Цель по времени отката — меньше 5 минут от решения до старой версии в проде. Как это реализуется технически? | middle_plus | `[snippet]` oneuptime.com |
| 13.20 | `[snippet]` «Gradual quality collapse»: латентность и error rate в норме, а модель уверенно ошибается. Как это ловить? | middle_plus | `[snippet]` mljar.com |
| 13.21 | Как избежать «retraining storms» — требовать устойчивости дрейфа на достаточном объёме выборки перед триггером? | middle_plus | `[snippet]` systemoverflow.com |

---

### 14. Spark: архитектура и основы

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 14.1 | What is Apache Spark and what are its main components? / Explain key features of Spark. | junior | `[DI-SPARK]` Q1, `[OB-SPARK]` |
| 14.2 | Explain how Apache Spark differs from Hadoop MapReduce. / What are benefits of Spark over MapReduce? | junior | `[DI-SPARK]` Q2, `[OB-SPARK]` |
| 14.3 | Describe the concept of RDDs (Resilient Distributed Datasets) in Spark. / What is RDD? Name the different types of RDD. | junior | `[DI-SPARK]` Q3, `[OB-SPARK]` |
| 14.4 | What are DataFrames in Spark and how do they compare to RDDs? / On what basis can you differentiate RDD, DataFrame and DataSet? | middle | `[DI-SPARK]` Q4, `[OB-SPARK]` |
| 14.5 | What is a DataSet and what are its advantages over DataFrame and RDD? | middle | `[OB-SPARK]` |
| 14.6 | What is lazy evaluation and how does it benefit Spark computations? / What are the benefits of lazy evaluation? | junior | `[DI-SPARK]` Q5, `[OB-SPARK]` |
| 14.7 | How does Spark achieve fault tolerance? / Hadoop uses Replication to achieve Fault Tolerance — how is this achieved in Apache Spark? | middle | `[DI-SPARK]` Q6, `[OB-SPARK]` |
| 14.8 | What is an RDD Lineage? / What is Lineage Graph? | middle | `[OB-SPARK]` |
| 14.9 | What is the role of Spark Driver and Executors? / What is Spark Executor? What do you understand by worker node? | junior | `[DI-SPARK]` Q7, `[OB-SPARK]` |
| 14.10 | How does Spark's DAG (Directed Acyclic Graph) Scheduler work? / What is the working of DAG in Spark? | middle | `[DI-SPARK]` Q8, `[OB-SPARK]` |
| 14.11 | **Как Spark дробит задачу?** (job → stage → task) | middle | `[RUDE-SP]` |
| 14.12 | **Широкие и узкие операции в Spark** | middle | `[RUDE-SP]` |
| 14.13 | Explain the concept of a Spark Session and its purpose. / What is the use of SparkContext in Apache Spark? | junior | `[DI-SPARK]` Q9, `[OB-SPARK]` |
| 14.14 | Describe the various ways to run Spark applications (cluster, client, local modes). / Under what scenarios do you use Client and Cluster modes for deployment? | middle | `[DI-SPARK]` Q11, `[OB-SPARK]` |
| 14.15 | How does Spark integrate with Hadoop components like HDFS and YARN? / Do you need to install Spark on all nodes of the YARN cluster? Why? | middle | `[DI-SPARK]` Q10, `[OB-SPARK]` |
| 14.16 | What are the different types of Cluster Managers in Apache Spark? | middle | `[OB-SPARK]` |
| 14.17 | What is the significance of the Catalyst optimizer in Spark SQL? / Explain Catalyst framework. | middle_plus | `[DI-SPARK]` Q14, `[OB-SPARK]` |
| 14.18 | How does Tungsten contribute to Spark's performance? | middle_plus | `[DI-SPARK]` Q15 |
| 14.19 | Explain the run time architecture of Spark. | middle | `[OB-SPARK]` |
| 14.20 | What do you mean by Speculative execution in Apache Spark? | middle_plus | `[OB-SPARK]` |
| 14.21 | Which are some important internal daemons used in Apache Spark? | middle | `[OB-SPARK]` |
| 14.22 | How can you achieve High Availability in Apache Spark? | middle_plus | `[OB-SPARK]` |
| 14.23 | What are the limitations of Spark? / Illustrate some demerits of using Spark. | middle | `[OB-SPARK]` |
| 14.24 | При каких условиях DuckDB может заменить Spark? Какие будут ограничения? | middle_plus | `[RUDE-SP]` |
| 14.25 | Сравнение ClickHouse, Spark и Trino по основным критериям | middle_plus | `[RUDE-MPP]` |

---

### 15. Spark: shuffle, партиционирование, skew, join, AQE, память

> Это **ядро Big-Data-секции для MLE**. Именно здесь чаще всего заваливают.

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 15.1 | **What is a Shuffle operation in Spark? What are the operations that can cause a shuffle?** | middle | `[OB-SPARK]` |
| 15.2 | **What do you understand by Shuffling in Spark?** | middle | `[OB-SPARK]` |
| 15.3 | **Какие бывают методы оптимизации в Spark?** | middle_plus | `[RUDE-SP]` |
| 15.4 | **How will you do memory tuning in Spark?** | middle_plus | `[OB-SPARK]` |
| 15.5 | **Как распределяется память на executor в Spark?** | middle_plus | `[RUDE-SP]` |
| 15.6 | What is Executor Memory in a Spark application? / What are the steps to calculate the executor memory? | middle_plus | `[OB-SPARK]` |
| 15.7 | **Типы join в Spark — как оптимизатор выбирает стратегию?** | middle_plus | `[RUDE-SP]` |
| 15.8 | Describe join operation. How is outer join supported? | middle | `[OB-SPARK]` |
| 15.9 | **Coalesce и repartition — когда при coalesce будет shuffle?** | middle_plus | `[RUDE-SP]` |
| 15.10 | Describe coalesce operation. When can you coalesce to a larger number of partitions? Explain. | middle_plus | `[OB-SPARK]` |
| 15.11 | **Как управлять партициями в Spark?** | middle_plus | `[RUDE-SP]` |
| 15.12 | Define Partitions in Apache Spark. / Describe Partition and Partitioner in Apache Spark. / How can you manually partition the RDD? | middle | `[OB-SPARK]` |
| 15.13 | What is the partitioning approach used in GraphX of Apache Spark? | middle_plus | `[OB-SPARK]` |
| 15.14 | **How will you minimize data transfer while working with Apache Spark? / How can the data transfers be minimized while working with Spark?** | middle_plus | `[OB-SPARK]`, `[DI-SPARK]` |
| 15.15 | **Why do we need broadcast variables in Spark? What is a Broadcast variable in Apache Spark?** | middle | `[OB-SPARK]`, `[DI-SPARK]` Q13 |
| 15.16 | Discuss the role of accumulators and broadcast variables in Spark. / What is an Accumulator in Apache Spark? | middle | `[DI-SPARK]` Q13, `[OB-SPARK]` |
| 15.17 | What is the difference in `cache()` and `persist()` methods in Apache Spark? / What are different Persistence levels? How will you select the storage level? | middle | `[OB-SPARK]`, `[DI-SPARK]` |
| 15.18 | How will you remove data from cache in Apache Spark? / How are automatic clean-ups triggered in Spark for handling the accumulated metadata? | middle | `[OB-SPARK]` |
| 15.19 | What is Checkpointing in Apache Spark? / Does Apache Spark provide checkpointing? | middle | `[OB-SPARK]`, `[DI-SPARK]` |
| 15.20 | **В каких кейсах нужно писать кастомные UDF?** (и почему обычно не нужно) | middle_plus | `[RUDE-SP]` |
| 15.21 | **Что такое parquet? / Explain the Parquet File format in Apache Spark. When is it best to choose this?** | middle | `[RUDE-SP]`, `[OB-SPARK]` |
| 15.22 | **Как понять, сколько тасок будет после считывания parquet?** | middle_plus | `[RUDE-SP]` |
| 15.23 | What are the common faults of the developer while using Apache Spark? / What are the common mistakes developers make when running Spark Applications? | middle_plus | `[OB-SPARK]` |
| 15.24 | Explain the level of parallelism in Spark Streaming. | middle_plus | `[OB-SPARK]` |
| 15.25 | What is Structured Streaming in Apache Spark? / What is a DStream? Explain different transformations on DStream. | middle | `[DI-SPARK]`, `[OB-SPARK]` |
| 15.26 | What is written-ahead log / journaling in Spark Streaming? | middle_plus | `[OB-SPARK]` |
| 15.27 | What is the significance of the Sliding Window Operation? | middle | `[OB-SPARK]` |
| 15.28 | How Spark handles Monitoring and Logging in Standalone Mode? / How will you monitor Apache Spark? | middle | `[OB-SPARK]` |
| 15.29 | Adaptive Query Execution (AQE): что делает и когда включать | middle_plus | `[CM-SPARK]` |
| 15.30 | `[snippet]` AQE реоптимизирует план после shuffle по реальной статистике: коалесит мелкие партиции и меняет стратегию join. Как AQE лечит skew автоматически (сплит крупных партиций + дублирование другой стороны)? | middle_plus | `[snippet]` dev.to/datanestdigital |
| 15.31 | `[snippet]` `spark.sql.shuffle.partitions` по умолчанию 200 — почти всегда неверно; правило 2–4 × cores. Как вы подбираете значение? | middle_plus | `[snippet]` datavidhya.com, habr 828984 |
| 15.32 | `[snippet]` Salting для перекошенного ключа при join: добавляем случайный префикс, реплицируем вторую сторону, джойним по солёному ключу. | middle_plus | `[snippet]` habr 828984 |
| 15.33 | **Что такое data skew и как с ним бороться?** | middle_plus | `[RUDE-DL]` |
| 15.34 | **Что такое data skew? Причины возникновения, на что влияет, механизмы лечения в различных MPP-системах.** | middle_plus | `[RUDE-MPP]` |
| 15.35 | `[snippet]` Дисбаланс данных, поиск узких мест, оптимизация вычислений, разные виды join в Spark — темы секции DE. | middle_plus | `[snippet]` habr X5Tech 572596 — **X5** |
| 15.36 | Spark OOM: `java.lang.OutOfMemoryError: Java heap space` — что и в каком порядке смотреть? | middle_plus | `[KHAN]` (раздел Big data, прямая ссылка на разбор) |

---

### 16. SQL для MLE / DE

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 16.1 | **Какие бывают типы JOIN в SQL? / Какие бывают физические типы JOIN в SQL?** | middle | `[RUDE-SQL]` |
| 16.2 | **В каких системах какие физические типы JOIN используются и почему?** | middle_plus | `[RUDE-SQL]` |
| 16.3 | Что такое self join? Для чего он используется? | junior | `[RUDE-SQL]` |
| 16.4 | **Как эффективно джойнить таблицы в реляционной базе? Паттерны и антипаттерны.** | middle_plus | `[RUDE-SQL]` |
| 16.5 | **На каком этапе SQL-запроса выполняются оконные функции?** | middle_plus | `[RUDE-SQL]` |
| 16.6 | **Чем принципиально отличается индексация в OLTP-системах от OLAP-систем?** | middle_plus | `[RUDE-SQL]` |
| 16.7 | Какие основные типы индексов существуют в классических реляционных БД (PostgreSQL, MySQL)? | middle | `[RUDE-SQL]` |
| 16.8 | Что такое B-Tree, как он устроен, и почему он считается универсальным индексом? | middle | `[RUDE-SQL]` |
| 16.9 | Что такое LSM-дерево и чем его логика индексации отличается от B-Tree? | middle_plus | `[RUDE-SQL]` |
| 16.10 | Какие типы индексов характерны для аналитических колоночных БД (ClickHouse, Vertica)? | middle_plus | `[RUDE-SQL]` |
| 16.11 | Что такое покрывающий индекс и как он позволяет избежать чтения таблицы? | middle | `[RUDE-SQL]` |
| 16.12 | В каких сценариях хэш-индекс эффективнее B-Tree, а в каких — бесполезен? | middle | `[RUDE-SQL]` |
| 16.13 | Почему в аналитических базах часто используют bitmap-индексы, но не в OLTP? | middle_plus | `[RUDE-SQL]` |
| 16.14 | Какие проблемы возникают при индексации в высоконагруженных системах? | middle_plus | `[RUDE-SQL]` |
| 16.15 | Как индексы связаны с физическими типами join? | middle_plus | `[RUDE-SQL]` |
| 16.16 | Что такое GIN и BRIN индексы? Когда использовать GIN (JSON/массивы) или BRIN (большие отсортированные даты/логи)? | middle_plus | `[RUDE-SQL]` |
| 16.17 | **В чём разница между Index Scan и Index Only Scan (умение читать `EXPLAIN ANALYZE`)?** | middle_plus | `[RUDE-SQL]` |
| 16.18 | Как работает MVCC, настройка autovacuum для высоконагруженных таблиц, борьба с bloat? | middle_plus | `[RUDE-SQL]` |
| 16.19 | Какие плюсы и минусы у JSONB против нормализованных таблиц? | middle | `[RUDE-SQL]` |
| 16.20 | Какие типы шардирования бывают? Что такое шардирование на уровне приложения? | middle_plus | `[RUDE-SQL]` |
| 16.21 | What is the difference between WHERE and HAVING clauses? | junior | `[DI-SQL]` Q5, `[OB-SQL]` |
| 16.22 | Define what a JOIN is in SQL and list its types. / What is the difference between inner join and outer join? left vs right outer join? | junior | `[DI-SQL]` Q6, `[OB-SQL]` |
| 16.23 | What are indexes and how can they improve query performance? | junior | `[DI-SQL]` Q12 |
| 16.24 | What is normalization? Explain with examples. / Describe denormalization and when you would use it. / What are the reasons for denormalizing the data? | junior | `[DI-SQL]` Q10–Q11, `[OB-SQL]` |
| 16.25 | What is a subquery, and when would you use one? | junior | `[DI-SQL]` Q14 |
| 16.26 | Write SQL query to get the nth highest salary among all employees. | junior | `[OB-SQL]` |
| 16.27 | Write SQL query to find max salary and department name from each department. | junior | `[OB-SQL]` |
| 16.28 | Write SQL query to find records in table A that are not in table B **without using NOT IN**. | middle | `[OB-SQL]` |
| 16.29 | Write query to find employees with duplicate email. / find employees that have same name and email. | junior | `[OB-SQL]` |
| 16.30 | What is the difference between DELETE and TRUNCATE in SQL? / DDL vs DML? | junior | `[OB-SQL]` |
| 16.31 | Как посчитать медиану в SQL без встроенной функции? | middle | `[MLI]` |
| 16.32 | SQL-задачи «продуктового» типа: подсчёт активных объявлений и кампаний, агрегация событий, расчёт CTR/CVR, разбивка по датам. | middle | `[AG-T]` |
| 16.33 | Что такое Materialized View? В чём разница концепций MV в OLTP и OLAP базах? Какие best practices использования? | middle_plus | `[RUDE-OTH]` |

---

### 17. Kafka и стриминг

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 17.1 | What is Apache Kafka? / List the various components in Kafka. | junior | `[OB-KAFKA]` |
| 17.2 | What is the traditional method of transferring messages? What are the benefits of Apache Kafka over the traditional technique? | junior | `[OB-KAFKA]` |
| 17.3 | What is the meaning of broker in Apache Kafka? | junior | `[OB-KAFKA]` |
| 17.4 | What is Zookeeper's role in Kafka's ecosystem and can we use Kafka without Zookeeper? | middle | `[OB-KAFKA]` |
| 17.5 | How are messages consumed by a consumer in Apache Kafka? | junior | `[OB-KAFKA]` |
| 17.6 | What is the role of the offset in Kafka? / Is it possible to get the message offset after producing to a topic? | middle | `[OB-KAFKA]` |
| 17.7 | **How can you get Exactly-Once Messaging from Kafka during data production?** | middle_plus | `[OB-KAFKA]` |
| 17.8 | **What is In-Sync Replicas (ISR)? How can we reduce churn in ISR? When does a broker leave ISR? What does it indicate if a replica stays out of ISR for a long time? What happens if the preferred replica is not in the ISR list?** | middle_plus | `[OB-KAFKA]` (5 связанных вопросов) |
| 17.9 | What is the purpose of replication in Apache Kafka? | middle | `[OB-KAFKA]` |
| 17.10 | Can you explain the concept of `leader` and `follower` in the Kafka ecosystem? | middle | `[OB-KAFKA]` |
| 17.11 | How do you define a Partitioning Key? | middle | `[OB-KAFKA]` |
| 17.12 | **How can you improve the throughput of a remote consumer?** | middle_plus | `[OB-KAFKA]` |
| 17.13 | What is the maximum size of a message that Kafka can receive? | middle | `[OB-KAFKA]` |
| 17.14 | In the Producer, when does QueueFullException occur? | middle_plus | `[OB-KAFKA]` |
| 17.15 | Can you please explain the role of the Kafka Producer API? | junior | `[OB-KAFKA]` |
| 17.16 | Mention what is the difference between Apache Kafka, Apache Storm, and Apache Flink? | middle | `[OB-KAFKA]` |
| 17.17 | **На основании каких критериев выбирать между Kafka и RabbitMQ? Что такое NATS JetStream?** | middle_plus | `[RUDE-OTH]` |
| 17.18 | **Какие бывают паттерны доставки в брокерах сообщений? Что такое Outbox pattern? Как обработать дубликаты?** | middle_plus | `[RUDE-OTH]` |
| 17.19 | **Как обеспечивать совместимость схем (Schema Registry) при эволюции форматов сообщений?** | middle_plus | `[RUDE-OTH]` |
| 17.20 | Kafka → ClickHouse: паттерны потребления и гарантированная доставка | middle_plus | `[RUDE-ETL]` |
| 17.21 | Как работает движок таблиц Kafka в ClickHouse? | middle_plus | `[RUDE-CH]` |
| 17.22 | `[snippet]` EOS требует `enable.idempotence=true` + Transactional API; брокер держит PID и sequence number на партицию и глушит дубли. Что происходит при ребалансе? | middle_plus | `[snippet]` conduktor.io |
| 17.23 | `[snippet]` Eager vs cooperative rebalance: чем «stop-the-world» плох для стриминг-инференса? | middle_plus | `[snippet]` datavidhya.com |
| 17.24 | What are the differences between Flink and Spark Streaming? | middle_plus | `[OB-FLINK]` |
| 17.25 | What is Watermark in Flink? What kinds of time are there in Flink (event/ingestion/processing)? | middle_plus | `[OB-FLINK]` |
| 17.26 | Do you know what windows in Flink are? | middle | `[OB-FLINK]` |
| 17.27 | Flink's state storage? What if Flink encounters an abnormal restart of the program? | middle_plus | `[OB-FLINK]` |
| 17.28 | What is TaskSlot? What is the relationship between Flink's slot and parallelism? | middle_plus | `[OB-FLINK]` |
| 17.29 | What is Unbounded / Bounded streams in Apache Flink? | middle | `[OB-FLINK]` |
| 17.30 | How does Apache Flink handle fault tolerance? | middle_plus | `[OB-FLINK]` |
| 17.31 | Does Flink need to depend on Hadoop? / Broadcast variables in Flink / Flink's distributed cache | middle | `[OB-FLINK]` |

---

### 18. Airflow и оркестрация

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 18.1 | What is Airflow? What issues does Airflow resolve? | junior | `[OB-AF]` |
| 18.2 | Explain Airflow Architecture and its components. | middle | `[OB-AF]` |
| 18.3 | **What are the types of Executors in Airflow? Pros and cons of SequentialExecutor / LocalExecutor / CeleryExecutor / KubernetesExecutor?** | middle_plus | `[OB-AF]` (5 вопросов подряд) |
| 18.4 | **Что такое executor в Airflow и какие типы бывают?** | middle | `[RUDE-AF]` |
| 18.5 | Explain how workflow is designed in Airflow? / How to define a workflow in Airflow? | junior | `[OB-AF]` |
| 18.6 | How to schedule DAG in Airflow? / **Какие способы планирования и оркестрации задач есть в Airflow?** | middle | `[OB-AF]`, `[RUDE-AF]` |
| 18.7 | **Почему сегодня в 18:00 не запустился DAG, у которого `start_date` сегодня в 18:00?** | middle | `[RUDE-AF]` |
| 18.8 | What is XComs in Airflow? What is `xcom_pull`? / **Что такое XCom в Airflow?** | middle | `[OB-AF]`, `[RUDE-AF]` |
| 18.9 | What is Jinja templates? How to use Airflow XComs in Jinja templates? | middle | `[OB-AF]` |
| 18.10 | **Какие операторы есть в Airflow и когда какой использовать?** | middle | `[RUDE-AF]` |
| 18.11 | **Что такое сенсоры в Airflow?** | middle | `[RUDE-AF]` |
| 18.12 | **Какой путь проходит таска в Airflow?** (состояния) | middle | `[RUDE-AF]` |
| 18.13 | **Что такое pool в Airflow?** | middle | `[RUDE-AF]` |
| 18.14 | **Что такое dataset в Airflow?** | middle_plus | `[RUDE-AF]` |
| 18.15 | **Масштабирование Airflow: 50+ production пайплайнов, cascade failures, динамические DAG** | middle_plus | `[RUDE-AF]` |
| 18.16 | **Как лучше размещать в DAG импорт коннекшена и подключение — в теле DAG или в каждой таске?** | middle_plus | `[RUDE-AF]` |
| 18.17 | **Какие есть лучшие практики по импорту тяжёлых библиотек в Airflow в теле DAG?** | middle_plus | `[RUDE-AF]` |
| 18.18 | **Что делает кнопка Reparse DAG в интерфейсе Airflow?** | middle_plus | `[RUDE-AF]` |
| 18.19 | How do you make the module available to Airflow if you're using Docker Compose? | middle | `[OB-AF]` |
| 18.20 | **Что такое идемпотентность и как она обеспечивается?** | middle_plus | `[RUDE-DWH]` |
| 18.21 | Идемпотентность в гибридной архитектуре Oracle + Kafka → ClickHouse | middle_plus | `[RUDE-DWH]` |
| 18.22 | How does Apache Oozie help in workflow scheduling in Hadoop? | junior | `[DI-HADOOP]` Q14 |
| 18.23 | When would you use n8n instead of LangGraph or Airflow? / When would you use n8n in an AI system, and when would you avoid it? | middle | `[CM-26A]` Q26, `[CM-26B]` Q20 |
| 18.24 | `[snippet]` Идемпотентность в Airflow: partition overwrite, upsert/MERGE по стабильному ключу, параметризация logical date. Почему backfill обязан идти тем же кодовым путём, что и live-ingestion? | middle_plus | `[snippet]` multisoftsystems.com |

---

### 19. Hadoop / HDFS / Hive / YARN

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 19.1 | What is Hadoop and what are its core components? | junior | `[DI-HADOOP]` Q1 |
| 19.2 | Explain the concept of HDFS and its architecture. | junior | `[DI-HADOOP]` Q2 |
| 19.3 | How does the MapReduce programming model work in Hadoop? / **Что такое MapReduce? Предпосылки появления и использование в Hadoop.** | junior | `[DI-HADOOP]` Q3, `[RUDE-OTH]` |
| 19.4 | What is YARN, and how does it improve Hadoop's resource management? | middle | `[DI-HADOOP]` Q4 |
| 19.5 | Explain the role of the Namenode and Datanode in HDFS. | junior | `[DI-HADOOP]` Q5 |
| 19.6 | What is a Rack Awareness algorithm in HDFS, and why is it important? | middle_plus | `[DI-HADOOP]` Q6 |
| 19.7 | What differentiates Hadoop from traditional RDBMS? | junior | `[DI-HADOOP]` Q7 |
| 19.8 | How can you secure a Hadoop cluster? Name some of the security mechanisms available. | middle_plus | `[DI-HADOOP]` Q8 |
| 19.9 | Describe the role of HBase in the Hadoop ecosystem. / What is the difference between HBase and Hive? | middle | `[DI-HADOOP]` Q9, `[OB-HIVE]` |
| 19.10 | What is Apache Hive and what types of problems does it solve? | junior | `[DI-HADOOP]` Q10 |
| 19.11 | **How will you improve the performance of a program in Hive?** | middle_plus | `[OB-HIVE]` |
| 19.12 | Can we use Hive for OLTP systems? | middle | `[OB-HIVE]` |
| 19.13 | What is Metastore in Hive? What is SerDe in Hive? | middle | `[OB-HIVE]` |
| 19.14 | What is the difference between SORT BY and ORDER BY in Hive? | middle_plus | `[OB-HIVE]` |
| 19.15 | What is the use of strict mode in Hive? | middle_plus | `[OB-HIVE]` |
| 19.16 | What are the main limitations of Apache Hive? | middle | `[OB-HIVE]` |
| 19.17 | What is Apache Sqoop and how does it interact with Hadoop? / How does Apache Flume help with log and event data collection? | junior | `[DI-HADOOP]` Q12–Q13 |
| 19.18 | What is Apache ZooKeeper and why is it important for Hadoop? | middle | `[DI-HADOOP]` Q15 |
| 19.19 | Practice problem: finding friends with MapReduce | middle_plus | `[KHAN]` |

---

### 20. Хранилища, форматы, lakehouse

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 20.1 | **Какие предпосылки стояли за появлением архитектуры Data Lake и впоследствии Data Lakehouse?** | middle | `[RUDE-DL]` |
| 20.2 | **Какие слои нужно использовать при проектировании Data Lake? / Какие есть слои в хранилище данных?** | middle | `[RUDE-DL]`, `[RUDE-DWH]` |
| 20.3 | **В чём отличия HDFS от S3?** | middle | `[RUDE-DL]` |
| 20.4 | **Как организовывать хранение Parquet в S3 для lakehouse?** | middle_plus | `[RUDE-DL]` |
| 20.5 | Что такое Schema-on-read? Когда появилось и в каких кейсах используется? | middle | `[RUDE-DL]` |
| 20.6 | **По каким критериям выбирать DWH, Data Lake или Lakehouse?** | middle_plus | `[RUDE-DWH]` |
| 20.7 | Какая технология построения аналитического хранилища предпочтительнее в зависимости от размера данных, среды и масштаба инфраструктуры? | middle_plus | `[RUDE-DWH]` |
| 20.8 | **Что такое merge-on-read и copy-on-write?** | middle_plus | `[RUDE-LH]` |
| 20.9 | **Разделение Storage/Compute — кэширование latency, small files, compaction в Iceberg** | middle_plus | `[RUDE-LH]` |
| 20.10 | Какие проблемы возникают в lakehouse и как с ними бороться? | middle_plus | `[RUDE-LH]` |
| 20.11 | Какие компромиссы допускаются в современных системах хранения с точки зрения ACID? | middle_plus | `[RUDE-LH]` |
| 20.12 | Эволюция архитектуры: от монолитной DWH к Lakehouse | middle_plus | `[RUDE-LH]` |
| 20.13 | Чем DuckLake отличается от других Lakehouse-фреймворков? | middle_plus | `[RUDE-LH]` |
| 20.14 | Чем отличается Data Vault 1.0 от Data Vault 2.0? / Почему DV 1.0 относится к RDBMS, а 2.0 к Big Data (хеш-ключи, ELT, PIT-таблицы)? | middle_plus | `[RUDE-DWH]` |
| 20.15 | Data Vault поверх Iceberg — специфические сложности, SCD в Satellites | middle_plus | `[RUDE-DWH]` |
| 20.16 | С чего начинать проектирование хранилища по технологии Data Vault 2.0? Алгоритм проектирования. | middle_plus | `[RUDE-DWH]` |
| 20.17 | **Как использовать SCD при проектировании пайплайнов?** | middle_plus | `[RUDE-DWH]` |
| 20.18 | Какие есть лучшие практики использования dbt? | middle | `[RUDE-ETL]` |
| 20.19 | Что такое ключи шардирования и партицирования? | middle | `[RUDE-OTH]` |
| 20.20 | `[snippet]` Predicate pushdown: чем ответ junior («Parquet — колоночный») отличается от ответа senior (алгоритмы сжатия, pushdown, когда Avro лучше для стриминга)? | middle_plus | `[snippet]` seattledataguy.substack.com |
| 20.21 | `[snippet]` Delta Lake хранит упорядоченный transaction log из JSON-коммитов + периодические Parquet-checkpoint; Iceberg — manifest-файлы + корневой metadata. Как это влияет на time travel и schema evolution? | middle_plus | `[snippet]` tacnode.io, medium/@moshahriari |

---

### 21. ClickHouse / MPP / Greenplum / Trino

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 21.1 | **Какие есть движки в ClickHouse? / Типичные сценарии использования ClickHouse — движки семейства MergeTree и прочие** | middle | `[RUDE-CH]` |
| 21.2 | **Как работают индексы в ClickHouse? / Чем индексирование в ClickHouse отличается от индексирования в реляционных базах?** | middle_plus | `[RUDE-CH]` |
| 21.3 | **Как правильно шардировать и партицировать в ClickHouse? По каким правилам выделять ключи? Хеш vs реальное значение, проблема суперпользователя.** | middle_plus | `[RUDE-CH]` |
| 21.4 | **С чего начинать и к чему стремиться при оптимизации запроса в ClickHouse? / Как читать план запроса в ClickHouse?** | middle_plus | `[RUDE-CH]` |
| 21.5 | Что такое partition pruning в ClickHouse? | middle_plus | `[RUDE-CH]` |
| 21.6 | Нетривиальные оптимизации ClickHouse — проекции, TTL агрегации, `primary_key` vs `sorting_key` | middle_plus | `[RUDE-CH]` |
| 21.7 | Какие процессы происходят в ClickHouse в фоновом режиме и при чём здесь merge-on-read и copy-on-write? | middle_plus | `[RUDE-CH]` |
| 21.8 | Что за процедуры мутаций в ClickHouse? Для чего нужны? Как инициируются и выполняются? Как отслеживать запросами? | middle_plus | `[RUDE-CH]` |
| 21.9 | Какие системные таблицы в ClickHouse наиболее информативны для отслеживания процессов? | middle_plus | `[RUDE-CH]` |
| 21.10 | Какие худшие практики работы в ClickHouse? | middle_plus | `[RUDE-CH]` |
| 21.11 | В чём заключается роль ClickHouse Keeper в работе кластера? | middle_plus | `[RUDE-CH]` |
| 21.12 | Как наполнять витрины в ClickHouse? / Как реализовать SCD в ClickHouse? | middle_plus | `[RUDE-CH]` |
| 21.13 | Как работает `ANY LEFT ANTI JOIN` в ClickHouse? Какую конструкцию он замещает и в каких кейсах используется? | middle_plus | `[RUDE-CH]` |
| 21.14 | В чём разница между Greenplum и ClickHouse? | middle | `[RUDE-CH]` |
| 21.15 | Какие типы таблиц и ориентации есть в Greenplum? / **Как выбирать ключ дистрибуции в Greenplum?** | middle_plus | `[RUDE-MPP]` |
| 21.16 | Что такое Replicated дистрибуция, для чего она? | middle_plus | `[RUDE-MPP]` |
| 21.17 | Что такое партицирование и когда его применять (Greenplum)? | middle | `[RUDE-MPP]` |
| 21.18 | Что делать при Deadlock и когда он может произойти? | middle_plus | `[RUDE-MPP]` |
| 21.19 | **Какие есть особенности и best practices для джойнов в MPP-системах? При чём тут ключ шардирования?** | middle_plus | `[RUDE-MPP]` |
| 21.20 | Что такое Trino? Чем отличается его архитектура от других Lakehouse-движков? | middle_plus | `[RUDE-MPP]` |
| 21.21 | Что такое StarRocks? В чём его преимущества? В каких кейсах StarRocks лучше Trino и наоборот? | middle_plus | `[RUDE-MPP]` |
| 21.22 | Что такое Redis и MongoDB? Что общего и в чём различия? | junior | `[RUDE-NOSQL]` |
| 21.23 | В каких кейсах используются графовые и векторные базы данных? | middle | `[RUDE-NOSQL]` |
| 21.24 | Что такое политики кэширования данных? Как использовать Redis для горячих справочников (LFU/LRU)? | middle_plus | `[RUDE-OTH]` |
| 21.25 | What is the difference between a vector database and a traditional database? | middle | `[CM-26A]` Q7 |
| 21.26 | Cassandra best practices / when to use Cassandra and when to steer clear / Cassandra performance | middle_plus | `[KHAN]` |

---

### 22. Распределённое обучение и масштабирование тренировки

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 22.1 | What is model parallelism vs data parallelism in distributed training? | middle | `[PUB]` Infra, `[ALZ]` §9 |
| 22.2 | What is tensor parallelism, and how does it help serve large models? / What is pipeline parallelism? | middle_plus | `[PUB]` Infra |
| 22.3 | What is model sharding, and when would you use it? | middle_plus | `[PUB]` Infra |
| 22.4 | **What is FSDP (Fully Sharded Data Parallel), and how does it differ from DeepSpeed ZeRO?** | middle_plus | `[PUB]` Infra |
| 22.5 | How does MLOps support model scalability and distribution? | middle | `[DI-LLMOPS]` Q13 |
| 22.6 | How do you handle distributed training and deployment of machine learning models in a multi-cloud environment? | middle_plus | `[SEP-M]` |
| 22.7 | Synchronous SGD vs Asynchronous SGD: stragglers vs gradient staleness — как выбирать? | middle_plus | `[CHIP]` §Scaling, `[ALZ]` §9 |
| 22.8 | При data parallelism на 128 машинах суммарный батч становится огромным. Что делать с learning rate и почему нельзя просто линейно увеличить? | middle_plus | `[CHIP]` §Scaling |
| 22.9 | Как балансировать нагрузку между master worker и остальными воркерами? | middle_plus | `[CHIP]` §Scaling |
| 22.10 | Датасет не помещается в память: как препроцессить (zero-centering, normalizing, whitening), шаффлить и батчить данные, которые не влезают в RAM? | middle_plus | `[CHIP]` §Scaling |
| 22.11 | Один сэмпл не влезает в память: что такое gradient checkpointing и какой у него trade-off? | middle_plus | `[CHIP]` §Scaling |
| 22.12 | Mixed precision training: почему FP16+FP32 даёт ×2 батч и ускорение; что такое Tensor Cores и bfloat16? | middle_plus | `[CHIP]` §Scaling |
| 22.13 | What considerations are important when choosing a computation resource for training machine learning models? | middle_plus | `[DI-MLOPS]` Q13 |
| 22.14 | How would you design a scalable machine learning infrastructure? | middle_plus | `[DI-MLOPS]` Q12 |
| 22.15 | Can you discuss an experience you have had with hyperparameter tuning and optimization? / Have you worked with any AutoML tools? | middle | `[SEP-D]` |
| 22.16 | Can you discuss your experience with implementing federated learning in an MLOps pipeline? | middle_plus | `[SEP-M]` |
| 22.17 | Can you discuss an experience you have had with implementing reinforcement learning in an MLOps pipeline? | middle_plus | `[SEP-M]` |
| 22.18 | Explain training pipelines? What are experiment pipelines? | middle | `[VENK]` |
| 22.19 | `[snippet]` DDP реплицирует модель на все GPU и синхронизирует градиенты ring-AllReduce; FSDP шардирует веса/градиенты/состояния оптимизатора и использует reduce-scatter. Почему reduce-scatter экономнее all-reduce? | middle_plus | `[snippet]` anyscale.com, saturncloud.io |
| 22.20 | `[snippet]` Как считается эффективный батч при `per_device_train_batch_size` × GPU × `gradient_accumulation_steps` и как это меняет LR? | middle_plus | `[snippet]` ailearnings.in |

---

### 23. «Спроектируйте пайплайн / систему» (design-вопросы)

#### 23.1. Как формулируется секция

> **Т-Банк, «Секция по дизайну ML систем» (дословно):**
> «Цель этой секции — обсудить подходы к проектированию и декомпозиции сложной ML системы.
> Во время секции Вам предложат систему, которую необходимо спроектировать. Можно выделить
> следующий общий дизайн решения: **форматизация задачи и требований, декомпозиция на подзадачи,
> сбор данных, разбор ML архитектур для подзадач, деплой и тестирование итоговой системы**.» — `[TK-SDML]`

> **Chip Huyen (дословно):** *«This part contains 27 open-ended questions that test your ability to
> put together what you've learned to design systems to solve practical problems… This type of question
> has become so popular that it's almost guaranteed that you'll be asked at least one during your
> interview process. In an hour-long interview, you might have time to go over only one or two questions.»* — `[CHIP]`

> **karpov.courses, ML System Design (Бабушкин)** `[snippet]`: этапы — постановка задачи и выбор baseline →
> дата-пайплайн и генерация фичей → тренировочный пайплайн → интеграция и API → мониторинг →
> разбор ошибок и поддержка системы.

#### 23.2. Уточняющие вопросы, которые кандидат ОБЯЗАН задать (`[CHIP]`, `[ALZ]`)

| Блок | Вопросы |
|---|---|
| Project setup | Goals? User experience (пошагово: когда и как показываются предсказания)? Performance constraints (насколько быстро/точно; что дороже — FP или FN)? Evaluation (как мерить и в трейне, и в инференсе; что делать, если онлайн-метрика недифференцируема)? Personalization (одна модель на всех / на группу / на пользователя)? Project constraints (срок, компьют, люди, готовые системы)? |
| Data pipeline | Data availability and collection: сколько данных есть, размечены ли, качество разметки, стоимость разметки, сколько аннотаторов на сэмпл, как разрешать разногласия, бюджет на данные, можно ли weak/self-supervision? User data: какие данные нужны от пользователей, как собирать фидбек, использовать его онлайн или периодически? Storage: где лежат данные (cloud/local/on-device), размер сэмпла, влезает ли в память, какие структуры данных и их trade-off, как часто приходят новые данные? Preprocessing: нужен ли feature engineering, нормализация, что с пропусками, что с дисбалансом, **как проверить, что train и test из одного распределения, и что делать, если нет**, как совмещать разные модальности? Privacy: какие privacy-требования, анонимизация, можно ли забирать данные на сервер? Biases: какие смещения в данных, как корректировать, инклюзивна ли разметка? |
| Serving | On-device vs cloud inference и trade-off? Мерить ли confidence и что делать при низкой уверенности (эскалация человеку / сбор данных)? Как часто обновлять модель? Дообучать на новых сэмплах или переучивать с нуля (и почему добавление нового класса требует полного переобучения)? Интерпретируемость vs качество? Ablation study по компонентам? Bias и misuse: что если у злоумышленника есть доступ к системе? |

#### 23.3. Открытые design-задачи, зафиксированные дословно

**Из `[CHIP]` (27 упражнений, приведены полностью):**

| # | Задача | Грейд |
|---|---|---|
| 23.3.1 | Duolingo… When a student is learning a new language, Duolingo wants to recommend increasingly difficult stories to read. **How would you measure the difficulty level of a story? Given a story, how would you edit it to make it easier or more difficult?** | middle_plus |
| 23.3.2 | Given a dataset of credit card purchases information, each record is labelled as fraudulent or safe, how would you build a fraud detection algorithm? | middle |
| 23.3.3 | You run an e-commerce website. Sometimes, users want to buy an item that is no longer available. Build a recommendation system to suggest replacement items. | middle_plus |
| 23.3.4 | For any user on Twitter, how would you suggest who they should follow? What do you do when that user is new? What are some of the limitations of data-driven recommender systems? | middle_plus |
| 23.3.5 | When you enter a search query on Google, you're shown a list of related searches. How would you generate a list of related searches for each query? | middle_plus |
| 23.3.6 | Build a system that returns images associated with a query like in Google Images. | middle_plus |
| 23.3.7 | How would you build a system to suggest trending hashtags on Twitter? | middle_plus |
| 23.3.8 | Each question on Quora often gets many different answers. How do you create a model that ranks all these answers? **How computationally intensive is this model?** | middle_plus |
| 23.3.9 | How do you build a system to display top 10 results when a user searches for rental listings in a certain location on Airbnb? | middle_plus |
| 23.3.10 | Autocompletion: how would you build an algorithm to finish your sentence when you text? | middle_plus |
| 23.3.11 | When you type a question on StackOverflow, you're shown a list of similar questions… How do you build such a system? | middle |
| 23.3.12 | How would you design an algorithm to match pool riders for Lyft or Uber? | middle_plus |
| 23.3.13 | On social networks like Facebook, users can list their high schools. Can you estimate what percentage of high schools listed on Facebook are real? How do we find out, **and deploy at scale**, a way of finding invalid schools? | middle_plus |
| 23.3.14 | How would you build a trigger word detection algorithm to spot the word "activate" in a 10 second long audio clip? | middle |
| 23.3.15 | If you were to build a Netflix clone, how would you build a system that predicts when a user stops watching a TV show, whether they are tired of that show or they're just taking a break? | middle_plus |
| 23.3.16 | Facebook would like to estimate the month and day of people's birthdays, regardless of whether people give us that information directly. What methods would you propose, and what data would you use? | middle_plus |
| 23.3.17 | Build a system to predict the language a text is written in. | junior |
| 23.3.18 | Predict the house price for a property listed on Zillow. Use that system to predict whether we invest in buying more properties in a certain city. | middle |
| 23.3.19 | Imagine you were working on iPhone. Every time users open their phones, you want to suggest one app they are most likely to open first with 90% accuracy. How would you do that? | middle_plus |
| 23.3.20 | How do you map nicknames (Pete, Andy, Nick, Rob, etc) to real names? | middle |
| 23.3.21 | An e-commerce company is trying to minimize the time it takes customers to purchase their selected items. As a machine learning engineer, what can you do to help them? | middle_plus |
| 23.3.22 | Build a chatbot to help people book hotels. | middle_plus |
| 23.3.23 | How would you design a question answering system that can extract an answer from a large collection of documents given a user query? | middle_plus |
| 23.3.24 | How would you train a model to predict whether the word "jaguar" in a sentence refers to the animal or the car? | middle |
| 23.3.25 | Suppose you're building software to manage the stock portfolio of your clients… How do you decide which of your currently owned stocks to drop so that you can buy this new stock? | middle_plus |
| 23.3.26 | How would you create a model to recognize whether an image is a triangle, a circle, or a square? | junior |
| 23.3.27 | Given only CIFAR-10 dataset, how to build a model to recognize if an image is in the 10 classes of CIFAR-10 or not? | middle_plus |

**Из `[ALZ]` — типовые ML System Design задачи по доменам:**

- Recommendation: Video/Movie recommendation (Netflix, YouTube); Friends/follower recommendation (Facebook, Twitter, LinkedIn); Event recommendation (Eventbrite); Game recommendation; **Replacement product recommendation (Instacart)**; Rental recommendation (Airbnb); Place recommendation.
- Search: Text query search (full-text, semantic); Image/Video search; Multimodal search.
- Ranking: Newsfeed ranking; Ads serving (retrieval + ranking); Ads click prediction.
- NLP: Named entity linking; Autocompletion / typeahead; Sentiment analysis; Language identification; Chatbot; QA system.
- CV: Image blurring system; OCR/Text recognition.
- AV: Self-driving (perception/prediction/planning), pedestrian jaywalking detection; Ride matching.
- Other: Proximity service / Yelp; Food delivery time approximation; **Harmful content / Spam detection**; Fraud detection; Healthcare diagnosis.
- GenAI (выделяется в **отдельный раунд** — «GenAI / LLM system design»): RAG document Q&A; LLM-powered customer support chatbot с guardrails и fallback на человека; Agentic workflow; Enterprise/semantic search с цитатами; Code assistant; Content generation at scale; LLM-based recommendation.

**Из `[PUB]` — End-to-End Design Questions (25):**

Design ChatGPT: Training to Serving (End to End) · Design a RAG System · Design Memory for a Personal AI Assistant · Design a Deep Research Agent · Design a Multi-Agent Customer Support System · Design an On-Device AI Assistant · Design a Multimodal Search System (Text, Image, Video) · **Design an LLM Inference Platform (vLLM-as-a-Service)** · Design an LLM Evaluation Platform · Design a Text-to-Image Generation Service · Design a Music Generation Service · Design a Video Generation Service · Design an AI Coding Agent · Design a code generation and review system · Design a content moderation system using AI · **Design a real-time AI recommendation system** · Design an AI-powered email assistant · Design a medical diagnosis assistant · Design a fraud detection system powered by LLMs · **Design an AI-powered data extraction pipeline from unstructured documents** · Design a personalized learning assistant · Design an AI system for automated code migration · Design an AI-powered legal document review system · Design a conversational AI system with memory across sessions.

**Из `[PUB]` — Architecture & Trade-off (22), самое релевантное для MLOps:**

- How do you approach **capacity planning** for an AI system?
- What are the key considerations for **multi-region deployment** of AI systems?
- Design a **multi-tenant** AI chatbot platform where each business gets a custom chatbot.
- Design an AI meeting summarizer system for thousands of meetings daily.
- Design an AI-powered **anomaly detection system for cloud infrastructure**.
- Design an AI-powered document processing pipeline for financial institutions.
- Design an AI **dynamic pricing engine**.
- Design an AI resume screening system that handles **100K applications per week**.
- Design a **real-time AI transcription system** for concurrent audio streams.
- Design an AI-powered **live streaming content moderation** system.
- Design an AI notification system that prioritizes instead of broadcasting.
- Design an AI-powered search engine for an e-commerce platform.

**Из `[CM-26B]`:**

- **Q18: Design a real-time product recommendation system for an e-commerce site with 10M users.** — middle_plus
- Q20: When would you use n8n in an AI system, and when would you avoid it? — middle

**Из `[CM-26A]`:**

- **Q20: How would you answer "Design an AI assistant for enterprise knowledge search" in an interview?** — middle_plus

#### 23.4. Русский шаблон дизайн-документа как чек-лист ответа (`[RUMLSD-T]`)

Разделы, по которым проверяют полноту ответа:
1. Цели и предпосылки — зачем идём в разработку; бизнес-требования и ограничения; что входит/не входит в скоуп; предпосылки решения (блоки данных, **горизонт прогноза, гранулярность модели**).
2. Методология — постановка задачи технически; **блок-схема отдельно для бейзлайна и отдельно для MVP** (с оговоркой: «Если блок-схема шаблонна — т.е. её можно скопировать и применить к разным продуктам, то она **некорректна**»); этапы решения; таблица «Название данных / есть ли данные в компании / требуемый ресурс / проверено ли качество»; формирование выборок train/test/val; **горизонт, гранулярность, частота пересчёта**; целевая переменная, согласованная с бизнесом; метрики качества и их связь с бизнес-результатом (пример из шаблона: `WAPE <= 50% для > 80% категорий, bias ~ 0`); риски этапа.
3. Подготовка пилота — способ оценки; что считаем успешным пилотом; **что можем позволить исходя из ожидаемых затрат на вычисления**.
4. Внедрение — архитектура (сервисы, назначения, методы API); **описание инфраструктуры и масштабируемости: какая инфраструктура выбрана и почему, плюсы/минусы, почему лучше альтернатив**; требования к работе системы (**SLA, пропускная способность и задержка**); безопасность системы; безопасность данных (GDPR); **издержки — расчётные затраты на работу системы в месяц**; integration points; риски.

---

### 24. Стоимость, capacity planning, экономика

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 24.1 | How do you estimate the cost of running an AI-powered feature in production? | middle_plus | `[PUB]` LLMOps |
| 24.2 | How do you optimize LLM inference costs in production? / Your LLM costs are too high in production. How do you reduce costs without degrading quality? | middle_plus | `[PUB]` LLMOps + scenario |
| 24.3 | How do you design rate limiting and cost management for AI APIs? | middle_plus | `[PUB]` Arch |
| 24.4 | What are the cost trade-offs between self-hosted and API-based AI inference? / How do you decide between using an LLM API vs self-hosting an open-source model? | middle_plus | `[PUB]` Infra + Behavioral |
| 24.5 | How do you approach capacity planning for an AI system? | middle_plus | `[PUB]` Arch |
| 24.6 | How do you approach cost optimization for an AI system that's exceeding budget? | middle_plus | `[PUB]` Behavioral |
| 24.7 | How do you measure the ROI of an AI feature? | middle_plus | `[PUB]` Behavioral |
| 24.8 | Издержки: расчётные затраты на работу системы в месяц | middle_plus | `[RUMLSD-T]` §4.6 |
| 24.9 | Как DuckDB используется в современных пайплайнах? Снижение стоимости облачного compute. | middle_plus | `[RUDE-OTH]` |
| 24.10 | Capacity estimation you should be able to do quickly (QPS → инстансы → память → диск) | middle_plus | `[CM-BSD]` |
| 24.11 | When is it worth upgrading GPUs? (фреймворк принятия решения на реальном бенчмарке H200 → B200) | middle_plus | `[STAS]` |
| 24.12 | How to choose a cloud provider — какие вопросы задать провайдеру | middle_plus | `[STAS]` |

---

### 25. Backend-фундамент, который спрашивают у MLE

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 25.1 | Horizontal vs Vertical Scaling; Load Balancing; Rate Limiting; Auto-Scaling | middle | `[CM-BSD]` #1–4 |
| 25.2 | SQL vs NoSQL; Database Indexing; Replication; Sharding | middle | `[CM-BSD]` #5–8 |
| 25.3 | Cache-Aside; Write-Through / Write-Behind; CDN и edge caching; **Consistent Hashing** | middle_plus | `[CM-BSD]` #9–12 |
| 25.4 | CAP Theorem; Strong vs Eventual Consistency; Leader Election; Consensus и Raft; Two-Phase Commit; **Saga Pattern** | middle_plus | `[CM-BSD]` #13–18 |
| 25.5 | Что такое распределённые транзакции? Паттерн Saga для согласованности между микросервисами. | middle_plus | `[RUDE-OTH]` |
| 25.6 | Как избежать некорректных агрегатов при параллельной записи? Блокировки vs оптимистичный контроль. | middle_plus | `[RUDE-OTH]` |
| 25.7 | Что такое external merge sort в контексте дата-инжиниринга? | middle_plus | `[RUDE-OTH]` |
| 25.8 | Какую роль играет хеш-таблица в задачах дедупликации? | middle | `[RUDE-OTH]` |
| 25.9 | Что такое PriorityQueue — где используется в контексте планирования задач? | middle | `[RUDE-OTH]` |
| 25.10 | Какие бывают вероятностные структуры данных? Где и как используются? (Bloom filter, HLL, Count-Min Sketch) | middle_plus | `[RUDE-OTH]` |
| 25.11 | Что такое GIL? / Итераторы и генераторы — как взаимодействуют с памятью? | middle | `[RUDE-PY]` |
| 25.12 | Почему использование pandas в задачах DE не считается best practice? | middle_plus | `[RUDE-PY]` |
| 25.13 | Какие правила нужно соблюдать при работе с Parquet в Python? | middle | `[RUDE-PY]` |

---

### 26. Поведенческо-технические («расскажите про свой опыт»)

> Эти формулировки прямо взяты из наборов, позиционированных как вопросы для интервью
> MLOps-инженера `[SEP-D]` и из репозитория «вопросы, с которыми я столкнулся» `[DEVF]`.

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 26.1 | Can you walk me through a recent project you worked on that involved MLOps? | middle | `[SEP-D]` |
| 26.2 | How do you approach the integration of machine learning models into a production environment? | middle | `[SEP-D]` |
| 26.3 | Can you give an example of a complex data pipeline you have built and the challenges you faced? | middle_plus | `[DEVF]` Q8 |
| 26.4 | How do you ensure the maintainability of data processing pipelines? | middle_plus | `[DEVF]` Q10 |
| 26.5 | How do you handle missing data in your pipelines? | middle | `[DEVF]` Q9 |
| 26.6 | What techniques do you use for feature engineering? | middle | `[DEVF]` Q7 |
| 26.7 | Can you explain the architecture of the Q&A system you developed using LLMs? | middle_plus | `[DEVF]` Q11 |
| 26.8 | What techniques did you use to reduce the response time of the LLM-based Q&A system? | middle_plus | `[DEVF]` Q15 |
| 26.9 | What steps did you take to ensure the security and privacy of the data used in the Q&A system? | middle_plus | `[DEVF]` Q17 |
| 26.10 | How do you determine which AI model or framework to use for a particular business problem? | middle | `[DEVF]` Q2 |
| 26.11 | Explain how you would evaluate the performance of a machine learning model in a real-world application. | middle | `[DEVF]` Q19 |
| 26.12 | Tell me about a challenging AI project you worked on. What was the problem? What approach did you take? What trade-offs did you make? What was the outcome? | middle_plus | `[PUB]` Behavioral |
| 26.13 | How do you decide whether a problem needs AI or a traditional software solution? | middle | `[PUB]` Behavioral |
| 26.14 | How do you communicate AI limitations to non-technical stakeholders? / A non-technical executive asks why your AI feature cannot be 100% accurate. How do you explain LLM limitations? | middle | `[PUB]` Behavioral |
| 26.15 | Your PM wants to ship an AI feature with a 15% hallucination rate on edge cases. How do you communicate the risk? | middle_plus | `[PUB]` Behavioral |
| 26.16 | You need to choose between a complex agentic system that scores 15% better on benchmarks, or a simpler RAG pipeline that is easier to maintain. How do you decide? | middle_plus | `[PUB]` Behavioral |
| 26.17 | How do you balance innovation with reliability in AI systems? | middle_plus | `[PUB]` Behavioral |
| 26.18 | Как готовиться: возьмите свой прошлый проект и ответьте — как вы собирали данные? как их обрабатывали? как решали, какие модели пробовать? какие в итоге сработали лучше и почему? были ли сюрпризы? как оценивали? **что бы вы сделали иначе, если бы делали проект заново?** | middle | `[CHIP]` §Tips on preparing |

---

### 27. Governance, приватность, безопасность (спрашивают в банках/финтехе)

| # | Вопрос | Грейд | Источник |
|---|---|---|---|
| 27.1 | How do you handle data privacy and security in an MLOps pipeline? | middle | `[SEP-D]` |
| 27.2 | How do you ensure the transparency and accountability of machine learning models in production? | middle_plus | `[SEP-D]` |
| 27.3 | How do you handle data bias and fairness in an MLOps pipeline? | middle_plus | `[SEP-D]` |
| 27.4 | Have you worked with any tools or platforms for model auditing and compliance, such as IBM AI Fairness 360 or Google What-If Tool? | middle_plus | `[SEP-D]` |
| 27.5 | Can you discuss an experience you have had with using MLOps in regulated industries or environments? / How do you handle security and compliance for machine learning models in a regulated industry? | middle_plus | `[SEP-D]`, `[SEP-M]` |
| 27.6 | Have you worked with any model interpretability or explainability tools? / …such as SHAP or LIME? / How do you handle model explainability and interpretability in production? / …in an ensemble or multi-model setting? / …for deep learning models? | middle_plus | `[SEP-D]` (×3), `[SEP-M]` (×2) |
| 27.7 | How do you handle PII and sensitive data in LLM inputs and outputs? | middle_plus | `[PUB]` LLMOps |
| 27.8 | How do you manage secrets and API keys securely in LLM applications? | middle | `[PUB]` LLMOps |
| 27.9 | How do you implement audit trails and logging for AI decisions? / What is model card documentation, and why is it important? | middle_plus | `[PUB]` Safety |
| 27.10 | Безопасность системы: потенциальная уязвимость. Безопасность данных: нет ли нарушений GDPR и других законов. | middle_plus | `[RUMLSD-T]` §4.4–4.5 |
| 27.11 | Your model passes one fairness metric but fails another. How do you handle conflicting audit results? | middle_plus | `[PUB]` Eval scenario |

---

## Что интервьюеры ловят этими вопросами

**1. «Ноутбук → прод» — есть ли он в биографии вообще.**
Ключевой водораздел, который бьёт по всему набору `[SEP-D]`: формулировки там сплошь
«*Can you discuss an experience you have had with…*». Интервьюер не проверяет определение —
он проверяет, было ли это в реальности. Кандидат, у которого не было, отвечает
определениями из статьи и мгновенно палится на follow-up «а что пошло не так?».

**2. Понимание, что модель — это не сервис, а система из пайплайнов.**
Три источника независимо задают одну и ту же декомпозицию: `[MLOPSZC]` (6 модулей),
`[PLDL]` (Data Management → Development → Testing&Deployment → Monitoring),
`[ALZ]` (9 шагов), `[RUMLSD-T]` (4 раздела). Кто отвечает «обернул в FastAPI и задеплоил» —
не показал ни данных, ни фичей, ни ретрейна, ни мониторинга.

**3. Умение выбрать самую скучную работающую архитектуру.**
`[CM-PIPE]` формулирует это как «interview soundbite»: *«Pick the highest-latency pipeline that
still meets the SLA. Latency is a cost you pay in engineering complexity, data-quality risk,
and on-call burden — so only buy as much of it as the business actually needs.»*
Отсюда весь блок §4 (batch vs streaming) и вопрос «Why not just use real-time for everything?».
Кандидат, который на всё отвечает «Kafka + Flink», проигрывает кандидату, который говорит
«тут хватит ночного батча, вот почему».

**4. Train/serve skew и point-in-time — «взрослый» маркер.**
Это единственная тема, которая встречается **во всех** MLOps-банках сразу
(`[SEP-G]` Q27, `[SEP-T]` Q5, `[CM-FS]` Q2, `[CM-26B]` Q12) и в поисковых сниппетах Nubank/Google.
Ей проверяют: понимает ли кандидат, что фича, посчитанная за 7 дней offline
и за «сколько успело накопиться» online — это две разные фичи.

**5. Умение отличать «дрейф есть» от «надо переучивать».**
Вопрос `[SEP-G]` Q12 — «*Why would you monitor feature attribution rather than feature distribution?*» —
специально сделан, чтобы поймать кандидата, который автоматически ставит алерт на любой сдвиг
распределения. Правильная линия ответа: сдвиг фичи, на которую модель не опирается, не важен;
важен сдвиг вклада фичи. Тот же смысл — в `[snippet]` systemoverflow про «retraining storms».

**6. Spark: понимание того, где происходит shuffle.**
Практически весь §15 сводится к одному: кандидат должен уметь на глаз сказать,
какая операция вызовет перекладку данных по сети, и что с этим делать
(broadcast, repartition/coalesce, salting, AQE, изменение ключа). `[RUDE-SP]` формулирует это
максимально прямо: «Как Spark дробит задачу?», «Широкие и узкие операции», «Coalesce и repartition —
**когда при coalesce будет shuffle**?». Последнее — классическая ловушка.

**7. Идемпотентность.**
`[RUDE-DWH]` («Что такое идемпотентность и как она обеспечивается?»),
`[RUDE-AF]` (масштабирование Airflow, cascade failures), `[snippet]` про backfill.
Проверяют: понимает ли кандидат, что ретрай и бэкфилл — норма, а не аварийная ситуация,
и что пайплайн должен переживать двойной запуск без дублей.

**8. Числа и SLA вместо прилагательных.**
`[RUMLSD-T]` требует «SLA, пропускная способность и задержка» и «расчётные издержки в месяц»;
`[PUB]` — «capacity planning», «100K applications per week»; `[snippet]` mljar — конкретные пороги P1.
Ответ «система должна быть быстрой и надёжной» не засчитывается.

**9. Способность разобрать инцидент, а не только построить систему.**
Целая группа сценарных вопросов `[PUB]`: latency spikes, крэш на 5000 RPS, отказ провайдера,
падение качества после квантизации, нулевая наблюдаемость пайплайна. Это проверка на on-call-опыт.

**10. Знание, где проходит граница ответственности.**
`[RUDE-OTH]` содержит показательный вопрос «Что такое признаки для ML-модели? **Как дата-инженер
участвует в их подготовке?**» — то есть на DE-собеседовании проверяют понимание ML-стороны,
а на ML-собеседовании (`[TK-SDML]`) — «сбор данных» и «деплой». MLE обязан держать обе стороны.

---

## Пробелы, которые чаще всего валят кандидатов

**Пробел 1. Русскоязычная подготовка по ML почти не покрывает прод.**
Проверено прямым фетчем: `[MLI]` (главный русский MLE-банк) — **нет** ни одного вопроса про
MLOps, Docker, Kubernetes, Spark, дрейф, деплой; `[AG-T]` — нет вопросов про Spark и распределённые
вычисления. При этом Т-Банк выделяет **отдельную секцию «Дизайн ML-систем»**, а SberDevices
`[snippet]` обсуждает «инференс и его ускорение». Кандидат готовится по русским ML-банкам
и приходит с нулём по половине интервью. **Это главный системный пробел, ради которого нужна
эта глава хендбука.**

**Пробел 2. Знание инструментов вместо знания механики.**
«Мы использовали MLflow» ≠ ответ на `[CM-MLF]` Q2 («чем registry отличается от просто артефактов в run»),
Q11 («ограничения автологгинга») или Q10 («как воспроизвести run в точности»).
Аналогично «мы использовали Airflow» ≠ ответ на «почему DAG со `start_date` сегодня в 18:00
сегодня в 18:00 не запустился» `[RUDE-AF]`.

**Пробел 3. Spark на уровне «читал статью».**
Кандидаты уверенно перечисляют RDD/DataFrame/lazy evaluation (§14) и рассыпаются на §15:
как считается память executor, почему coalesce иногда всё-таки шаффлит, как оптимизатор выбирает
между broadcast hash join / sort-merge join / shuffle hash join, что делает AQE, как лечить skew.
`[snippet]` X5Tech прямо называет темы секции: «дисбаланс данных, поиск узких мест, оптимизация
вычислений, разные виды join».

**Пробел 4. Мониторинг = «смотрим accuracy».**
Не различают data drift / concept drift / prediction drift `[CM-DQ]` Q1;
не знают ни одного статистического критерия кроме «сравним средние»;
не могут назвать порог PSI и обосновать его; не понимают, что метки в проде приходят с лагом
(и что делать, пока их нет). Отдельно — не различают мониторинг и логирование `[SEP-G]` Q6.

**Пробел 5. Стратегии выката перепутаны между собой.**
Blue-green ≠ canary ≠ shadow ≠ A/B ≠ champion-challenger ≠ MAB, а в ответах это один комок.
`[SEP-G]` держит под это сразу 4 вопроса (Q10, Q11, Q25, Q30), `[SEP-D]` — ещё 4.
Особенно проваливают: чем shadow отличается от canary (shadow **не влияет** на пользователя,
трафик дублируется), и почему для ML нужен champion-challenger, а не просто rolling update.

**Пробел 6. Отсутствие «нижней» инженерной базы.**
`[OB-K8S]` спрашивает «как дебажить под, который не шедулится», `[CM-BSD]` — consistent hashing и Saga,
`[RUDE-SQL]` — как читать `EXPLAIN ANALYZE` и чем Index Scan отличается от Index Only Scan.
DS без бэкенд-фона тут проваливается целиком. Обратное тоже верно: DE без ML-фона не отвечает
на `[RUDE-OTH]` «Что такое признаки для ML-модели?».

**Пробел 7. Design-вопрос без уточняющих вопросов.**
`[CHIP]` пишет об этом прямым текстом: *«Each interview starts with a purposefully vague task:
design X. It's your job as the candidate to ask for clarification and narrow down the problem.»*
Кандидат, который сразу начинает с «возьмём BERT», теряет секцию, даже если модель верная.
Симметрично `[RUMLSD-T]`: «Если блок-схема шаблонна… она **некорректна**».

**Пробел 8. Нет baseline.**
`[CHIP]` §Model selection: три baseline, которые «many candidates forget» — random, human,
simple heuristic. И цитата Zinkevich: *«if you think that machine learning will give you a 100 % boost,
then a heuristic will get you 50 % of the way there»*. Плюс правило «если в системе больше
100 вложенных if-else — пора на ML».

**Пробел 9. Игнорирование стоимости.**
Ни срок обучения, ни цена инференса, ни $/месяц не проговариваются. При этом это явный
раздел русского шаблона (`[RUMLSD-T]` §4.6 «Издержки») и целый блок `[PUB]` (§24 выше).

**Пробел 10. Распределённое обучение на уровне «поставил `DistributedDataParallel`».**
Не отвечают, чем FSDP отличается от ZeRO, зачем reduce-scatter вместо all-reduce, что делать
с LR при росте эффективного батча, что такое gradient checkpointing и какой у него trade-off
(§22). При этом `[KHAN]` честно помечает Big Data как «NOT required for Google, Facebook
interview» — то есть в РФ и в FAANG наборы требований **разные**, и об этом стоит предупредить
читателя прямо.

**Пробел 11. Нет ответа на «а что, если?».**
Классические follow-up, к которым не готовы: метки приходят через 30 дней — как мерить качество
сегодня? фича-сервис лёг — что отдаёт модель? модель уверенно ошибается, а латентность в норме —
как узнаете? откатились — что с уже записанными в фичестор значениями?

---

## Рекомендации для структуры глав хендбука по этой теме

Ниже — предлагаемая рубрикация. Она собрана как пересечение четырёх независимых внешних
структур (`[MLOPSZC]` 6 модулей, `[PLDL]` full-stack pipeline, `[ALZ]` 9 шагов,
`[RUMLSD-T]` 4 раздела) с фактическим распределением вопросов выше.

### Раздел 07 — MLOps

**07.1. Что такое MLOps и зачем он ML-инженеру**
Отличие от DevOps и от «просто деплоя». Три пайплайна вместо одного: Feature / Training /
Inference (FTI-разбиение, `[snippet]` Hopsworks). Роли DS / DE / MLE и где проходят границы.
Уровни зрелости MLOps. → закрывает §1.

**07.2. Артефакт модели и его упаковка**
Что попадает в артефакт кроме весов (препроцессинг, версии библиотек, сигнатура входа/выхода,
метаданные обучения). Форматы: pickle/joblib → ONNX → TorchScript → SavedModel.
Почему pickle в проде — мина. MLflow flavors и `infer_signature`. → §2, §9.

**07.3. Сервинг**
REST vs gRPC (когда и почему). FastAPI как дефолт; async, пулы воркеров, GIL.
Специализированные серверы: TorchServe, Triton, BentoML, TF Serving, Seldon — таблица «что когда».
Динамический батчинг: как он торгует latency за throughput; `preferred_batch_size` и
`max_queue_delay`. On-device vs cloud. → §3, §5.

**07.4. Batch vs online vs streaming**
Спектр batch → microbatch → near-real-time → streaming со столбцом «типичная латентность /
инженерная сложность / риск качества данных». Правило «бери самый медленный пайплайн,
который укладывается в SLA». Watermarks и late data. → §4.

**07.5. Docker и Kubernetes для ML**
Слои, multi-stage, `.dockerignore`, пиннинг зависимостей и CUDA-совместимость.
K8s-минимум для MLE: Deployment/Job/CronJob, requests/limits, probes, HPA,
node affinity под GPU, PDB. Отдельный подраздел «как дебажить под, который не шедулится». → §6, §7.

**07.6. CI/CD для ML и тестирование**
Что вообще тестировать в ML (данные, фичи, контракт модели, метрики на голден-сете,
инвариантность, поведенческие тесты). Пайплайн: lint → unit → data validation → train →
eval gate → registry → deploy. IaC и immutable infrastructure. → §8.

**07.7. Реестр моделей, трекинг, воспроизводимость, DVC**
Experiment vs run. Registry vs «S3 с папками». Stage/alias и промоушен.
Воспроизводимость: сид, версия данных, версия кода, версия окружения, версия фич.
DVC и почему git-lfs не заменяет его. → §9.

**07.8. Стратегии выката**
Отдельная страница-таблица: blue-green / canary / shadow / A-B / interleaving /
champion-challenger / multi-armed bandit — по осям «влияет ли на пользователя»,
«нужны ли метки», «скорость получения сигнала», «стоимость». Откат: цель < 5 минут.
Feature flags. → §10.

**07.9. Feature store и train/serve skew**
Offline/online store. Point-in-time correctness с картинкой временной шкалы.
Материализация и freshness. Когда feature store **не** нужен. Как ловить skew
(логировать фичи на инференсе и сравнивать с обучающими). → §11.

### Раздел 08 — Big Data

**08.1. Модель вычислений и хранения**
HDFS vs S3, MapReduce как исторический контекст, YARN/k8s как resource manager.
Колоночные форматы: Parquet (row groups, статистики, predicate pushdown), Avro для стриминга.
→ §19, §20.

**08.2. Spark: как он на самом деле работает**
Driver/executors, job → stage → task, узкие и широкие трансформации, DAG, Catalyst, Tungsten.
Lazy evaluation. cache vs persist и уровни хранения. → §14.

**08.3. Spark: производительность (ключевая глава)**
Shuffle: что его вызывает, что происходит на диске и в сети.
`spark.sql.shuffle.partitions` и как его считать. repartition vs coalesce (и когда coalesce
всё-таки шаффлит). Стратегии join и как оптимизатор выбирает; broadcast join и его лимит.
Skew: как диагностировать по Spark UI, salting, AQE skew join.
AQE целиком. Память executor: разбивка на regions, spill, OOM.
UDF vs нативные функции и почему Python UDF дорог. Small files problem.
**Отдельный подраздел «Разбор задачи: запрос идёт 4 часа, что вы смотрите первым»** — §15.

**08.4. SQL для MLE**
Оконные функции и порядок их выполнения. Физические типы join и их связь с индексами.
Индексы: B-Tree, hash, bitmap, GIN, BRIN; OLTP vs OLAP. `EXPLAIN ANALYZE`.
Продуктовые паттерны: сессионизация, воронка, retention-когорты, top-N per group, дедупликация.
→ §16.

**08.5. Kafka и стриминг**
Топики/партиции/consumer groups/offsets. Гарантии доставки и exactly-once
(идемпотентный продюсер + транзакции). ISR и что значит «реплика вылетела из ISR».
Ребаланс: eager vs cooperative. Outbox pattern и дедупликация.
Schema Registry и эволюция схем. Kafka vs RabbitMQ vs gRPC — критерии выбора.
Flink: event time, watermark, state, checkpoints. → §17.

**08.6. Airflow и оркестрация**
Архитектура и executors. `start_date`/`schedule`/logical date — источник классической ловушки.
XCom и почему через него нельзя гонять данные. Sensors, pools, datasets.
**Идемпотентность и backfill как отдельная тема.** Масштабирование: динамические DAG,
cascade failures, тяжёлые импорты в теле DAG. → §18.

**08.7. DWH / Data Lake / Lakehouse**
Слои хранилища. Delta/Iceberg/Hudi: transaction log vs manifests, time travel,
schema evolution, compaction, copy-on-write vs merge-on-read.
Разделение storage/compute. SCD. dbt. → §20.

**08.8. Аналитические СУБД (для РФ-рынка — обязательно)**
ClickHouse: MergeTree-семейство, первичный ключ ≠ индекс, партицирование и шардирование,
partition pruning, мутации, проекции, Keeper, Kafka engine, худшие практики.
Greenplum: ключ дистрибуции, Replicated, deadlock. Trino, StarRocks, DuckDB.
→ §21. *(В англоязычных банках этого почти нет — а в РФ спрашивают постоянно.)*

### Раздел 09 — Мониторинг и надёжность

**09.1. Что мониторить**
Три слоя: инфраструктура (латентность p50/p95/p99, error rate, RPS, утилизация GPU) →
данные (объём, схема, пропуски, кардинальность) → модель (распределение предсказаний,
метрики качества при наличии меток, feature attribution). Golden signals для ETL.
Логирование vs мониторинг vs трейсинг (OpenTelemetry). → §12.

**09.2. Дрейф**
Таксономия: covariate / label / concept / prediction drift.
Инструменты: PSI (формула, биннинг, пороги и почему они условны), KS (и почему он
пересрабатывает на больших N), Chi-Squared, JS/KL, MMD и её варианты (learned kernel,
context-aware). Что делать при дрейфе в категориальных и в высокоразмерных фичах.
Мониторинг attribution вместо распределения. → §12.

**09.3. Политика ретрейна**
По расписанию / по триггеру / continual / online learning.
Как не устроить retraining storm. Как быть с отложенными метками.
Champion-challenger как механизм принятия решения о замене. → §13.

**09.4. Инциденты и надёжность**
Классификация отказов: SW-отказ vs ML-отказ (сдвиг распределения, feedback loop, junk input).
Severity/SLA, раннбуки, откат, graceful degradation, fallback-модель, кэш ответов.
«Тихая деградация»: латентность в норме, модель уверенно ошибается. → §13.

**09.5. Стоимость и capacity**
Оценка QPS → инстансы → память → GPU. $/1000 запросов. Автоскейлинг и cold start.
Когда self-host дешевле API. → §24.

### Раздел 11 — ML System Design (стыкуется с этой темой)

Каркас ответа брать из пересечения `[ALZ]` (9 шагов), `[CHIP]` (4 компонента) и
`[RUMLSD-T]` (русский шаблон — **особенно ценен, потому что на русском и потому что явно
требует SLA, издержки и риски**). Обязательные элементы главы:
1. Чек-лист уточняющих вопросов (полностью выписан в §23.2 выше) — это то, чего не делают кандидаты.
2. Три baseline (random / human / heuristic) как обязательный шаг.
3. Шаблон блок-схемы «отдельно бейзлайн, отдельно MVP».
4. Секция «деплой и тестирование итоговой системы» — прямая формулировка Т-Банка.
5. 5–7 полностью разобранных кейсов. Рекомендую брать из §23.3 те, что одновременно
   популярны и имеют богатый прод-слой: **фрод-детекция**, **рекомендации замены товара
   (Instacart)**, **ранжирование ленты**, **детекция вредоносного контента**,
   **real-time рекомендации на 10M пользователей**, **поиск по корпоративной базе знаний (RAG)**.
6. Отдельный подраздел «GenAI system design» — `[ALZ]` фиксирует, что это уже **отдельный раунд**.

### Сквозные рекомендации по подаче

- **Каждую тему давать в двух срезах: «как рассказать за 2 минуты» и «на какой follow-up вы посыпетесь».**
  Формат `[RUDE]` (карточка: Вопрос → Суть → Как работает → Пример → **Edge cases** → **Тезисы для устного ответа**)
  — лучший из встреченных; его стоит скопировать как формат врезки в хендбуке.
- **Везде проставлять грейд.** Junior не обязан знать AQE, но обязан знать, что такое shuffle.
  Middle+ обязан назвать цифры.
- **Не прятать региональную разницу.** `[KHAN]` прямо пишет: Big Data «NOT required for Google,
  Facebook interview». В РФ (Т-Банк, X5, Ozon, Яндекс) Spark/SQL/ClickHouse спрашивают у MLE
  регулярно. Об этом надо сказать читателю прямым текстом в начале раздела 08.
- **Добавить главу «числа, которые надо знать наизусть»**: p99 против p50, порядок латентности
  сети/диска/памяти, PSI-пороги, дефолт `spark.sql.shuffle.partitions` = 200, правило
  2–4 × cores, целевое время отката < 5 мин, типовые SLA. Кандидаты, называющие числа,
  выглядят на голову сильнее.
- **Не изобретать собственные кейсы там, где есть канон.** Т-Банк сам публикует список
  материалов для подготовки к секции дизайна ML-систем: *Machine Learning Design Patterns*
  (Lakshmanan/Robinson/Munn), *Deep Learning Design Patterns* (Ferlitsch),
  `ahkarami/Deep-Learning-in-Production`, `alirezadir/Production-Level-Deep-Learning`,
  блог «Monitoring Machine Learning Models in Production» (christophergs.com),
  доклад «Как в YouDo машинное обучение катится в продакшен» (Адам Елдаров).
  Эту подборку стоит вынести в хендбук отдельным блоком «что читать перед секцией дизайна» —
  она подтверждена документально `[TK-SDML]`.
