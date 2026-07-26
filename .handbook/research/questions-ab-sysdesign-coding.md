# A/B-тестирование, ML System Design и Coding-секции для MLE — research dump

> Дата сбора: 2026-07-26.
> Область: (1) A/B-тесты и эксперименты, (2) ML System Design интервью, (3) coding-секции для MLE.
> Целевые грейды: junior → middle → middle+ (RU-рынок + международный контекст).

## Методологическая оговорка про источники (читать обязательно)

В этой сессии исходящий HTTPS шёл через egress-прокси, который пропускал **только `github.com` / `raw.githubusercontent.com` / GitHub API**.
Все остальные хосты — `habr.com`, `medium.com`, `arxiv.org`, `kdnuggets.com`, `datainterview.com`, `interviewquery.com`,
`teamblind.com`, `leetcode.com`, `enigmai.ru`, `zasqlpython.ru`, `core-analytics.ru`, `bookdown.org`, `avito.tech`,
`microsoft.com`, `exp-platform.com`, `eugeneyan.com` — отдавали `403` от прокси (проверено: `curl` и `WebFetch` оба падают,
`recentRelayFailures` в `$HTTPS_PROXY/__agentproxy/status` это подтверждает).

Поэтому источники честно разделены на две группы:

- **(A) Полностью вычитанные страницы** — я видел содержимое целиком, могу цитировать дословно.
- **(B) Страницы, содержимое которых я видел только через цитаты поискового движка.** WebSearch реально читает страницу
  и возвращает фрагменты; я привожу только то, что реально было в этих фрагментах, и помечаю такие пункты как «через цитаты».

**Ничего, чего не было ни в (A), ни в (B), в этот файл не попало. Выдуманных URL и выдуманных вопросов здесь нет.**

Отдельно про грейды: там, где источник сам проставил грейд (банк `ixlander/interview-questions` — единственный источник
с явными тегами `Junior/Middle/Senior` + компанией), я сохраняю его метку и рядом ставлю нормализованный тег
`junior | middle | middle_plus` (Senior источника → `middle_plus`, потому что для нашего хендбука верхняя граница — middle+).
Там, где источник грейд не проставил, тег — **моя оценка** по формулировке вопроса, и это помечено как `(оценка)`.

---

## Источники, которые реально просмотрены

### A. Полностью вычитанные страницы

| # | URL | Что там |
|---|-----|---------|
| A1 | https://raw.githubusercontent.com/ixlander/interview-questions/main/all-real-questions.md | **Главный RU-источник реальных вопросов.** 274 вопроса с реальных собеседований, 14 разделов. Релевантны: `MLSD-GENERAL (22)`, `SYSTEM-DESIGN (17)`, `MATH-STATISTICS (13)` (внутри — блок A/B), `CODING (9)`, `SQL-DATABASES (5)`, `LANG-PYTHON (19)`, `DATA-ENGINEERING (10)`. Каждый вопрос помечен грейдом (Junior/Middle/Senior) и компанией: Самокат, Ozon, Сбер, Т-Банк, Яндекс, VK, Wildberries, Дром.ру, Constructor, ZinBrains, Quantum One, PulsePoint, Teza Technologies, Wunderfund, Headlands Technologies, Silver Mont HFT, Mayflower, ВТБ, Infomedia, Waibee, NNS, Автотехника (Sber Autonomous), Точка банк, X5 Tech, Avito, Учи.ру, Navi/Corsearch. |
| A2 | https://raw.githubusercontent.com/kirmipt/ab_articles/main/README.md | Карта русскоязычной A/B-методологии: 9 тем (размер выборки из мощности и MDE; сплит-система; репрезентативность и стратификация; проверка метода через FPR на A/A; методы расчёта A/B и повышения мощности — пуассон-бутстрап, бакетизация, дельта-метод, CUPED, постнормировка, парная стратификация; сравнение методов; подглядывание и досрочная остановка; расчёт срока по предэксп. данным; выводы из результатов). Со ссылками на разборы Тинькофф, ВК, Авито (2 части), Карпова (размер выборки, подглядывания), Учи.ру (Бонферрони, Покок, О'Брайен–Флеминг). |
| A3 | https://raw.githubusercontent.com/alselezneva/ds_mentor/main/Notion/Менторство/AB-тестирование.md | Русский менторский конспект по A/B (61 КБ) с явным блоком **«Вопросы на интервью — 💬 Спрашивают в 14% собеседований»**. Внутри: 7-шаговый алгоритм проведения теста, Монте-Карло симуляции (валидация FPR/TPR), направленность и прокси-метрики (Label Agreement, корреляция по дельтам, корреляция по t-статистикам), автоматизация A/B и репозиторий метрик, ratio-метрики (bias наивного CTR vs global CTR на численном примере), ускорение A/B (стратификация, пост-стратификация, CUPED с формулой и алгоритмом, трансформации), SUTVA и spillover. |
| A4 | https://raw.githubusercontent.com/TheAndreyZakharov/IT-Interview-Question-Bank/main/RU/Questions_By_Topic_RU/%23%23%2014.%20Data%20-%20ML%20-%20Analytics.md | Большой RU-банк вопросов (220 КБ). Релевантные подразделы: `14.1 Статистика и теория вероятностей`, `14.3 SQL для аналитики`, `14.4 Python/pandas`, `14.9.2 Monitoring, drift detection, A/B testing`, `14.10 Product analytics и A/B testing` (~230 вопросов только по экспериментам). **Это компиляция-банк, а не лог реальных собеседований** — использую как карту тем, а не как «спрашивали в компании X». |
| A5 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20System%20Design/3%20ML%20System%20Design%20Interviews/README.md | Русскоязычный **14-шаговый сценарий ответа на MLSD** + чек-лист «что должно быть в полном разборе» + план из 10 задач + принцип хорошего ответа (`requirement → design decision → guarantee → cost → alternative`). |
| A6 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests/2%20Minimum%20Detectable%20Effect.md | Конспект «Power Analysis и MDE» с практикой на Python: биномиальная vs непрерывная метрика, абсолютный vs относительный MDE, `statsmodels`, длительность эксперимента, зависимость от baseline p и σ, дизайн-эффект при кластеризации, счётчики/Пуассон, heavy-tail, power-кривые и обратные задачи. |
| A7 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests/4%20Sequential%20Tests%20and%20CUPED.md | Конспект: фиксированный горизонт, наивное подглядывание, group-sequential тесты, always-valid / sequential p-values, CUPED (интуиция, формула, применение, ограничения), комбинация sequential + CUPED. |
| A8 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests/3%20Holdout%20and%20Traffic%20Strategies.md | Конспект по holdout-группам и стратегиям распределения трафика. |
| A9 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests/5%20Effect%20Metrics%20and%20Interpretation.md | Конспект по метрикам эффекта и интерпретации результата. |
| A10 | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests/6%20AB%20Testing%20in%20ML%20Context.md | **Самый релевантный для MLE:** A/B как часть ML-пайплайна, A/B-тест vs просто смена модели, feature flags в ML, стратегии rollout, champion/challenger, rollback, оффлайн vs онлайн метрики и разрыв между ними, A/B + uplift-модели, практический шаблон A/B-теста для модели, что фиксировать в отчёте. |
| A11 | https://github.com/Maha-Rossomaha/LLM_projects/tree/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests (листинг через GitHub API) | Структура блока A/B: `0 Glossary`, `0 Stat Tests/`, `1 Basics`, `2 MDE`, `3 Holdout and Traffic Strategies`, `4 Sequential Tests and CUPED`, `5 Effect Metrics and Interpretation`, `6 AB Testing in ML Context`, `Code/`. Соседний блок — `2 Uplift Modeling/` (в т.ч. `3 Experimental Design.md`, `5 Uplift Architectures.md`, `8 Modern Causal Methods.md`). |
| A12 | https://raw.githubusercontent.com/justxor/MachineLearningRoadmap/main/interview-prep/04-system-design.md | «ML System Design: 10 кейсов с разбором». Универсальная 8-шаговая схема ответа с таймингом (5+3+5+10+10+5+10+5 мин на 60-минутную секцию), 10 кейсов, 8 финальных советов. |
| A13 | https://raw.githubusercontent.com/justxor/MachineLearningRoadmap/main/interview-prep/05-coding.md | «Coding-интервью для ML-инженеров»: **разбивка 50% алгоритмы / 20% SQL / 20% ML с нуля / 10% pandas-numpy**, топ-25 LeetCode-задач по категориям, 7-шаговый универсальный подход к задаче, антипаттерны, SQL-минимум + топ-10 SQL-задач + подводные камни, 8 ML-задач «с нуля», pandas/numpy типовые вопросы, чек-лист готовности. |
| A14 | https://raw.githubusercontent.com/alirezadir/machine-learning-interviews/main/src/MLSD/ml-system-design.md | **9-шаговая формула MLSD** (Problem Formulation → Metrics → Architectural Components → Data → Feature Engineering → Model Development & Offline Eval → Prediction Service → Online Testing & Deployment → Scaling/Monitoring/Updates) + большой список типовых задач по категориям (GenAI/LLM 2026, RecSys, Search, Ranking, NLP, CV, AV, Other). Шаг 8 явно включает A/B Experiments, Bandits, Shadow deployment, Canary release. |
| A15 | https://raw.githubusercontent.com/LongxingTan/Machine-learning-interview/master/02_ml/99_ml_coding.md | Реальный список «что реализуют руками на ML-coding»: `MSE`, `CrossEntropyLoss` (2 варианта), `FocalLoss`, `AUC`, `DecisionTree` + `TreeNode`, `KMeansCluster`, `Dense` слой, `Conv2D`, `image2col`/`col2image`, `conv2D`, `conv1d`, `scaled_dot_attention`, `MultiHeadAttention`, TF (`compute_term_frequency`), IDF (`compute_inverse_document_frequency`), TF-IDF вектор, BPE (`get_stats`, `merge_vocab`), `get_positional_embedding`, `top_k_sampling`. |
| A16 | https://raw.githubusercontent.com/LongxingTan/Machine-learning-interview/master/02_ml/97_product_sense.md | Product-case фреймворк: 4 типа задач (Launch or not / Investigation / How to measure / Want to know something / How to build a model), метрики (goal, monitoring, guardrail), trade-offs (engagement vs monetization, short vs long term, engagement vs safety), блок «эксперимент» с прямыми вопросами про randomization unit и network effect. Ключевая фраза про грейды: *«Junior pursues right or wrong; Senior looks for trade-offs»*. |
| A17 | https://github.com/LongxingTan/Machine-learning-interview/tree/master/02_ml (листинг через GitHub API) | Полный список файлов раздела ML: `00_ml_math`, `01_metrics`, …, `20_mlops`, `21_feature_engineering`, `22_online_learning`, `97_product_sense`, `98_project`, `99_ml_coding`. |
| A18 | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/system-design-ml.md | **Официальное описание секции ML System Design в Т-Банке (первоисточник от работодателя).** Дословно: «Цель этой секции — обсудить подходы к проектированию и декомпозиции сложной ML системы. Во время секции Вам предложат систему, которую необходимо спроектировать. Можно выделить следующий общий дизайн решения: форматизация задачи и требований, декомпозиция на подзадачи, сбор данных, разбор ML архитектур для подзадач, деплой и тестирование итоговой системы.» + список материалов для подготовки. |
| A19 | https://raw.githubusercontent.com/Tinkoff/career/main/interview/sections/platform-ml.md | Официальное описание ML-секции Т-Банка: «Разбираем вопросы по анализу данных: о постановке задачи, выборе и обосновании метрик качества, сборе и валидации данных, ML-алгоритмах. Вопросы разбираем на теоретических и практических кейсах.» + рекомендованные банки вопросов (dingran/quant-notes, iamtodor/data-science-interview-questions-and-answers, kojino/120-Data-Science-Interview-Questions, alexeygrigorev/data-science-interviews). |
| A20 | https://raw.githubusercontent.com/kojino/120-Data-Science-Interview-Questions/master/statistical-inference.md | 16 классических вопросов Statistical Inference — почти все про A/B (см. блок вопросов ниже). Этот банк **явно рекомендован Т-Банком** как материал подготовки (A19), поэтому он для RU-рынка не «просто западный». |
| A21 | https://raw.githubusercontent.com/kojino/120-Data-Science-Interview-Questions/master/product-metrics.md | 15 вопросов Product Metrics (метрики успеха продукта, расследование падения метрики, surge pricing Uber, churn, News Feed). |
| A22 | https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/theory.md | Теоретический банк DS-вопросов (80 КБ). Проверено: отдельного A/B-раздела там нет (grep по `A/B`/`experiment` пуст) — важный негативный факт: чисто «теоретические» банки A/B почти не покрывают, поэтому дыра в хендбуке закрывается отдельной главой. |
| A23 | https://github.com/Tinkoff/career/tree/main/interview/sections (листинг через GitHub API) | Полный список секций интервью Т-Банка: `platform-ml`, `system-design-ml`, `programming`, `programming-basic`, `system-design-backend`, `platform-backend`, `platform-sre`, `platform-web`, `platform-qa` и др. Подтверждает, что ML System Design — **отдельная именованная секция** в RU-компании. |
| A24 | https://raw.githubusercontent.com/ixlander/interview-questions/main/README.md | Метаданные банка A1 (перечень разделов и компаний). |
| A25 | https://github.com/LongxingTan/Machine-learning-interview/tree/master/05_case (листинг через GitHub API) | `01_pre_interview.md`, `02_cheat_sheet.md`, `03_post_interview.md`, `README.md` — структура кейс-подготовки. |

### B. Источники, содержимое которых я видел только через цитаты поискового движка (хост заблокирован egress-политикой)

| # | URL | Что оттуда реально процитировано |
|---|-----|----------------------------------|
| B1 | https://habr.com/ru/articles/664512/ | «Как одолеть вопросы по АБ тестам с собеседований» — вопросы для аналитиков/продуктовых аналитиков/менеджеров: что такое мощность и почему её важно учитывать при анализе экспериментов; что такое статистическая значимость; что такое преждевременная остановка теста. Ключевые концепты: H₀/H₁, ошибки I и II рода, alpha vs power, p-value, MDE. |
| B2 | https://core-analytics.ru/questions-ab-test/ | «Вопросы по AB тестам на собеседовании» — подтверждён факт существования тематической подборки; текст страницы получить не удалось (403). |
| B3 | https://aaefimov.medium.com/вопросы-на-собеседовании-по-a-b-тестам-d1aaf1053ca0 | «Вопросы на собеседовании по A/B тестам для аналитика» — подборка RU-вопросов; полный текст недоступен. |
| B4 | https://zasqlpython.ru/blog/sobesedovanie-analitika-dannyh-150-voprosov-2026 | Дословно из цитаты: «Современное собеседование аналитика данных включает 3-4 раунда: SQL-задачу live, Python-задачу live, **A/B-кейс с цифрами** и разбор продуктовой метрики». Заявлено 1000+ задач с собеседований Яндекс, Сбер, Ozon, Avito, Тинькофф, VK, X5, Wildberries, Lamoda. |
| B5 | https://habr.com/ru/companies/X5Tech/articles/780270/ | «А/Б тестирование с CUPED: детальный разбор» — CUPED как техника повышения чувствительности через предэкспериментальные данные; требуется ковариата, коррелированная с метрикой и не зависящая от эксперимента. |
| B6 | https://habr.com/ru/companies/X5Tech/articles/826488/ | «А/Б тестирование: CUPED vs Stratification» — прямое сравнение двух методов снижения дисперсии; пост-стратификация применяется, когда выборки сгенерированы без стратификации. |
| B7 | https://habr.com/ru/companies/X5Tech/articles/740476/ | «А/Б тесты с метрикой отношения. Дельта-метод». |
| B8 | https://habr.com/ru/companies/X5Tech/articles/679842/ | «Бутстреп и А/Б тестирование». |
| B9 | https://habr.com/ru/articles/762648/ | «Бутстрап: швейцарский нож аналитика в A/B-тестах». Из цитат: бутстрап применяется, когда t-test не работает; нужен минимум N≈100+; предполагает IID (для временных рядов/кластеров — block bootstrap); при выбросах использовать робастные статистики (медиана, winsorized). |
| B10 | https://habr.com/ru/companies/avito/articles/571094/ | «Как улучшить ваши A/B-тесты: лайфхаки аналитиков Авито. Часть 1» — гипотезы, доверительные интервалы и относительные метрики, проверка метода через FPR на A/A (сначала на искусственных, потом на реальных), относительный T-тест через дельта-метод, «о чём говорят серые метрики» (если эффект не обнаружен, он лежит в пределах доверительного интервала), выбросы и снижение дисперсии; чего **не** делать: Манн–Уитни, логарифмирование метрики, выкидывание выбросов внутри эксперимента (выкидывать можно по предэксп. периоду). |
| B11 | https://habr.com/ru/companies/avito/articles/571096/ | Часть 2: увеличение срока бесполезно; определение срока по предэксп. периоду; CUPED и постнормировка (через бутстрап); стратификация как метод разбивки на тест/контроль; парная стратификация с учётом ковариации; сравнение всех методов и их комбинаций. |
| B12 | https://habr.com/ru/companies/avito/articles/936804/ | «Методичка по AB-тестированию от аналитиков Авито». |
| B13 | https://habr.com/ru/company/avito/blog/454164 | «Как устроено A/B-тестирование в Авито». |
| B14 | https://habr.com/ru/companies/citymobil/articles/560426/ | «Switchback-эксперименты в Ситимобил. Эпизод 1: Скрытая сила switchback» — в сетевых средах классический A/B нарушает SUTVA. |
| B15 | https://habr.com/ru/companies/deliveryclub/articles/670762/ | «Как мы научились А/B-тестировать алгоритмы с помощью switchback-тестов» — switchback в логистике, когда эффективность одной доставки влияет на другие. Из цитаты: сетевые эффекты, измеренные классическим A/B, примерно **в 3 раза выше**, чем измеренные switchback (со ссылкой на исследование Яндекс.Такси). |
| B16 | https://habr.com/ru/companies/avito/articles/1048780/ | «Switchback-тесты: инфраструктура для экспериментов в условиях сетевых эффектов» (Авито) — настройка размера окна, доли трафика и весов групп для классического A/B и switchback в едином семантическом слое. |
| B17 | https://habr.com/ru/company/uchi_ru/blog/500918/ | Учи.ру: множественные сравнения (много срезов / метрик / тритментов) и Бонферрони; подглядывания и FPR > 5%; границы Покока и О'Брайена–Флеминга (+ Optimizely); расчёт срока из MDE по старым данным с учётом Покока и Бонферрони. |
| B18 | https://vkteam.medium.com/practitioners-guide-to-statistical-tests-ed2d580ef04f | ВК: FPR и мощность, равномерность p-value на A/A, выбор критерия сравнением FPR и мощности на искусственных данных; для `clicks` — t-тест vs Манна–Уитни; для `globalCTR` — binom-Z, bootstrap, delta-method, бакетизация, линеаризация. |
| B19 | https://habr.com/ru/companies/ods/articles/698698/ | «Что я бы хотел знать про ML System Design раньше» (ODS) — важно понимать все этапы дизайна и их последовательность, задавать правильные вопросы про бизнес-требования, аргументировать выбор методов/технологий и обсуждать pros/cons; не прыгать между моделью, данными и деплоем, забывая спросить про бизнес. |
| B20 | https://habr.com/ru/articles/704128/ | «Как устроен процесс найма и собеседований на позицию Machine Learning Engineer». |
| B21 | https://avito.tech/events/j0m3z4j2f1-sobesedovanie-ds-spetsialista-v-avito-13 | Публичное собеседование DS-специалиста в Авито: секция ML system design; разбирают кейс **с реальных интервью**, обсуждают целеполагание и влияние на пользователей, дают развёрнутый фидбек **по матрице компетенций**. |
| B22 | https://www.youtube.com/watch?v=mmdpL9cXEy4 и https://www.youtube.com/watch?v=hoivOhka710 | «Собеседование DS инженера в Авито: ML system design» — публичные записи разборов (первоисточник формата секции). |
| B23 | https://habr.com/ru/companies/yandex_praktikum/articles/834230/ | «Собеседование по System Design: как запроектировать и не потеряться» — первый этап всегда сбор требований: нужно сформировать список требований к проектируемому сервису, задавая вопросы интервьюеру; важно не найти единственно верное решение, а показать системное мышление, работу с абстракциями, логичное построение архитектуры и обоснованный выбор технологий. |
| B24 | https://habr.com/ru/articles/995600/ | «Реальные задачи с собеседований в Яндекс, VK, Ozon и Сбер — Go, Java, Python, React»: 17 задач, 10 компаний, 5 стеков. Из цитат: Python-задачи в live-coding встречаются в Ozon, Яндексе и Kaspersky с фокусом на **генераторах, декораторах и data processing**; ~70% компаний в России используют livecoding (Яндекс, Сбер, VK, T-Bank, Avito, OZON); конкретный пример — **Rate Limiter через декоратор `@rate_limit(max_calls=5, period=60)` (Kaspersky)**. |
| B25 | https://habr.com/ru/articles/993674/ | «Что спрашивают на собесах в 2025–2026: разбираем данные с 9 247 технических интервью» — аналитика по транскрипциям реальных интервью. |
| B26 | https://habr.com/ru/articles/926214/ | «Как я собеседовался в Ozon, Т-Банк, Mindbox и другие крупные компании». Из цитаты: в Ozon после скрининга три секции — технический скрининг, большая техническая секция и **system design** с коротким fit в конце; на system design просили спроектировать «корпоративную архитектуру продукта, например Instagram». |
| B27 | https://www.tbank.ru/career/it/interview/ml-product-management/ | Из цитаты: типовой процесс DS в Т-Банке — 4-5 этапов: HR → **SQL+статистика** → ML/кейс → финалы → behavioral; секция ML/Product case ~1 час (риск-моделирование или классические продуктовые задачи), Finals — **системное мышление, 1.5 часа, для middle+**, с упором на бизнес-логику. |
| B28 | https://www.datainterview.com/blog/ab-testing-interview-questions | «Top 30 A/B Testing Interview Questions (2026)». Из цитат: интервью **аналитика** фокусируется на определении метрик, интерпретации результатов и коммуникации trade-offs; интервью **дата-сайентиста** уходит глубже — power analysis, снижение дисперсии (CUPED), ratio-метрики и дельта-метод, sequential testing, network effects; **сеньоров дожимают** именно по ratio-метрикам, дельта-методу и снижению дисперсии. Отдельно: для ratio-метрик нужен дельта-метод, потому что числитель и знаменатель коррелированы, а наивная оценка дисперсии даёт анти-консервативные доверительные интервалы и больше ложных срабатываний. |
| B29 | https://medium.com/data-science/7-a-b-testing-questions-and-answers-in-data-science-interviews-eee6428a8b63 (зеркала: towardsdatascience.com/…, emmading.com/blog/…) | Emma Ding, «7 A/B Testing Questions and Answers in Data Science Interviews» — 4 из 7 вопросов процитированы дословно (см. блок вопросов A.16). |
| B30 | https://www.kdnuggets.com/2022/09/24-ab-testing-interview-questions-data-science-interviews-crack.html | «24 A/B Testing Interview Questions in Data Science Interviews and How to Crack Them» — 2 вопроса процитированы дословно (совпадают с B29). |
| B31 | https://bookdown.org/madinterviewllc/Product-Data-Science-Interview-The-Bar-to-Get-Hired/ab.html | Глава «3 A/B Testing» книги «Product Data Science Interview: The Bar to Get Hired». Из цитаты: парадокс Симпсона — **крайне популярная тема на интервью**, часто возникает неявно. |
| B32 | https://www.getdalton.com/blogs/simpsons-paradox-ab-testing, https://medium.com/homeaway-tech-blog/simpsons-paradox-in-a-b-testing-93af7a2f3307 | Симпсон в A/B: тренд во всех сегментах противоположен агрегату из-за конфаундера; для возникновения нужны неравные сплиты (следствие багованной рандомизации → selection bias); минимальная проверка — device type, traffic source, new vs returning. |
| B33 | https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/ | Microsoft EXP: SRM возникает, когда фактическое распределение не совпадает с задуманным (50/50 → 40/60); причины бывают на стадиях Assignment (некорректный бакетинг, битые user id), Execution (редирект одного варианта), Log Processing (неверные джойны), Analysis (смещённые условия). Оценка — chi-squared goodness-of-fit. SRM встречается примерно в **6–10% A/B-тестов**. |
| B34 | https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/deep-dive-into-variance-reduction/ | Microsoft EXP, «Deep Dive Into Variance Reduction». |
| B35 | https://bytepawn.com/reducing-variance-in-ab-testing-with-cuped.html, https://srome.github.io/Connections-Between-the-Delta-Method-OLS-and-CUPED-Illustrated/ | CUPED введён Deng, Xu, Kohavi, Walker; CUPED снижает дисперсию, регрессируя предэкспериментальные ковариаты, и **эквивалентен дельта-методу, когда в качестве ковариаты берётся знаменатель**. |
| B36 | https://arxiv.org/pdf/1911.03553 | «Dealing With Ratio Metrics in A/B Testing at the Presence of Intra-User Correlation and Segments» — канон по ratio-метрикам. |
| B37 | https://arxiv.org/pdf/2401.04062 | «Variance Reduction in Ratio Metrics for Efficient Online Experiments». |
| B38 | https://dl.acm.org/doi/10.1145/3534678.3539144 | KDD'22: «Multi Armed Bandit vs. A/B Tests in E-commerce — Confidence Interval and Hypothesis Test Power Perspectives». |
| B39 | https://www.optimizely.com/optimization-glossary/multi-armed-bandit, https://cxl.com/blog/bandit-tests/, https://vwo.com/blog/multi-armed-bandit-algorithm/ | Бандиты vs A/B: A/B — период чистого exploration, затем длинный exploitation; бандиты чередуют оба адаптивно; A/B нужен, когда важна оценка эффекта с доверительными интервалами, бандиты — когда важна автоматическая максимизация метрики без промежуточной интерпретации. |
| B40 | https://support.optimizely.com/hc/en-us/articles/38941939408269-Global-holdouts, https://docs.statsig.com/holdouts, https://www.geteppo.com/blog/holdouts-measuring-experiment-impact-accurately | Global holdout: небольшая доля пользователей изолируется от **всех** экспериментов и раскаток на уровне продукта и всех команд; так меряется кумулятивный эффект программы экспериментов и долгосрочный эффект. Рекомендованная доля — **не более 5%** трафика. |
| B41 | https://www.tryexponent.com/courses/ml-system-design/mlsd-rubric, https://www.tryexponent.com/courses/ml-system-design/mlsd-intro | Рубрика MLSD: оценивают умение превратить неоднозначную бизнес-задачу в ML-решение, практический опыт с ML-системами (особенно поиск точек наибольшего рычага), глубину знания современных техник. **Problem exploration — ось, по которой градируют сеньорити**: джуны прыгают сразу в feature engineering или в чистую технику без бизнес-контекста. Сеньорам дают более неоднозначные задачи и ждут, что кандидат сам найдёт оптимальную формулировку. |
| B42 | https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction | «Machine Learning System Design in a Hurry» — фреймворк подготовки. |
| B43 | https://igotanoffer.com/en/advice/machine-learning-system-design-interview, https://www.trybackprop.com/blog/ml_system_design_interview | Общие рубрики MLSD-интервью: problem framing, data-centric thinking, feature engineering depth, training-serving parity, evaluation rigor, production awareness (мониторинг, дрифт). |
| B44 | https://getassessai.com/blog/how-to-evaluate-system-design | Рубрика с числовой шкалой: 4.0–5.0 Strong Hire (senior/staff), 3.0–3.9 Hire (mid → senior), 2.0–2.9 Lean No (нужен коучинг), 1.0–1.9 No Hire. |
| B45 | https://medium.com/@davidfosterhq/meta-ml-system-design-interview-questions-and-guide-2026-39a79bbc2c0b, https://www.systemdesignhandbook.com/guides/google-ml-system-design-interview/ | Реальные MLSD-формулировки Meta/Google: design a personalized news ranking system; design a CTR prediction model for Google Ads; design an evaluation framework for ads ranking at Meta; design a fraud detection system for Stripe; design a budget pacing system for advertiser campaigns. |
| B46 | https://www.interviewquery.com/interview-guides/airbnb-data-scientist | Airbnb DS: **experiment design, clustered A/B testing**, robust primary and guardrail metrics, causal regressions, panel-building в SQL, browsing/conversion метрики, launch-impact estimation. Раунды: live coding, product sense + A/B case, **ML system design**, core-values behavioral. Отдельно: для двусторонних маркетплейсов interference между control и treatment даёт смещённую оценку эффекта. |
| B47 | https://www.interviewquery.com/interview-guides/amazon-data-scientist | Amazon DS: проведение A/B-тестов, дизайн экспериментов, определение success metrics для валидации продуктовых изменений. |
| B48 | https://prachub.com/interview-questions/debug-and-fix-a-pytorch-transformer-training-loop | **«Debug and fix a PyTorch Transformer training loop» — заявлено как вопрос с интервью OpenAI.** Постановка: causal LM на PyTorch «обучается», но loss не улучшается и иногда становится NaN; нужно для каждого бага назвать (a) симптом, (b) корневую причину, (c) минимальный фикс. Примеры багов: отсутствие `optimizer.zero_grad()`; слои, созданные в `forward` вместо `__init__` (не регистрируются в `parameters()`); один и тот же вектор позиционного кодирования на все позиции. |
| B49 | https://mentorcruise.com/questions/pytorch/, https://www.codinginterview.com/guide/pytorch-coding-interview-questions/ | PyTorch-секция: умеешь ли ты собрать модель, написать training loop и корректно загрузить данные; умеешь ли дебажить, находить bottleneck'и и ускорять обучение. |
| B50 | https://www.yuan-meng.com/posts/mle_interviews_2.0/, https://artgor.medium.com/my-experience-of-interview-preparation-as-mle-fe53627ba33e | Из цитат: основные типы интервью на MLE — LeetCode-style coding, ML System Design, ML-теория и статистика (иногда внутри MLSD), behavioral. «Implement common model architectures from scratch: Transformers (encoder/decoder/enc-dec), MLP, CNN, RNN (GRU, LSTM), либо traditional models — logistic regression, linear regression, KNN, K-Means, decision trees». «Вместо импорта из `torch.nn` реализуйте строительные блоки сами: embedding lookups, projection/linear layers, layer norm, batch norm, attention (causal и bidirectional), residual connections, dropout, activations». |
| B51 | https://www.interviewquery.com/p/python-machine-learning-interview-questions, https://www.shadecoder.com/blogs/machine-learning-coding-interview-prep-guide-2026-skills-practice-tools | Из цитат: планка — «fluent data manipulation, simple model implementations, and feature processing, с pandas и NumPy настолько отточенными, чтобы думать о задаче, а не о синтаксисе». Типовая формулировка: «Implement binary logistic regression using only NumPy. Include a `fit` method with gradient descent and a `predict` method» — проверяет одновременно сигмоиду, BCE-loss и обновление весов. |
| B52 | https://builder.ai2sql.io/blog/sql-interview-questions-faang, https://www.techprep.app/blog/funnel-cohort-and-retention-analysis-interview-questions, https://letsdatascience.com/blog/sql-cohort-retention-interview-questions | SQL-паттерны на DS/DA-скринах: window functions, self-joins, top-N per group, cohort/retention math, дедупликация, rolling metrics, funnel conversion, sessionization. Дословный пример задачи: «For each weekly signup cohort, compute Day-7 retention (% of users from the cohort who returned 7 days after signup) given `users(id, signup_date)` and `sessions(user_id, session_date)`». Техники: `ROW_NUMBER`/`DENSE_RANK` для первого события; `MIN(...) OVER (PARTITION BY ...)` для `cohort_date`; `LAG`/`LEAD` для гэпов и сессионизации; `SUM(...) OVER` для присвоения session_id по флагам гэпа. |
| B53 | https://www.analytics-toolkit.com/glossary/novelty-effect/, https://medium.com/codex/cracking-a-b-testing-for-interview-87e368162fae, https://www.emmading.com/blog/7-a-b-testing-questions-and-answers-in-data-science-interviews | Novelty vs primacy: novelty — пользователи взаимодействуют с новинкой больше обычного, метрика раздувается; primacy — пользователям не нравится изменение и они сначала избегают фичи, метрика падает. Детект: (1) построить treatment effect по времени — если лифт большой на 1-й неделе и сжимается к 3-й, это novelty; (2) сегментировать new vs returning — если фича выигрывает у returning, но не у new, это сильный признак novelty; (3) сравнить первичных пользователей control vs treatment. Лечение: держать тест 3-4 недели до стабилизации либо тестировать только на новых пользователях. |
| B54 | https://habr.com/ru/companies/ru_mts/articles/485980/, https://ods.ai/tracks/uplift-modelling-course, https://gopractice.ru/product/ml-retention-improvement/ | Uplift: оценка эффекта воздействия, предсказание изменения вероятности события под влиянием коммуникации; удержание строят **не на прогнозе оттока, а на uplift-моделировании**; метрика `uplift@k` для кампаний с ограниченным бюджетом; датасет X5 Retail Hero как канон. |
| B55 | https://enigmai.ru/tech-questions/ml-ds/, https://enigmai.ru/interview/ozon/, https://enigmai.ru/interview/yandex/, https://enigmai.ru/guides/system-design-prep/system-design-common-tasks/ | Из цитат: в 2026 стандартный пайплайн Яндекса — скрининг, 2-3 алгоритмические секции, системный дизайн, финалы с командами; для Junior меньше акцента на System Design и проще алгоритмические задачи, для Senior — глубокий System Design и больше поведенческих. В 2026 к задачам системного дизайна **добавилось динамическое ценообразование (surge pricing) на основе предсказательных моделей спроса**. |
| B56 | https://books.yandex.ru/books/Xw0IJfVk/read-online | «System Design. Машинное обучение» (перевод Aminian/Xu) — из цитаты: на собеседованиях оценивают умение проектировать комплексные ML-системы — визуальный поиск, рекомендации видео, предсказание кликов по рекламе. |
| B57 | https://zaringleb.medium.com/как-я-готовился-к-собеседованию-на-позицию-senior-ml-engineer-f2f6d8effa50 | Из цитаты: формальные секции называются ML System Design (например, «спроектировать newsfeed твиттера») плюс менее формальные разговоры про опыт ML-проектов. |
| B58 | https://www.hse.ru/edu/courses/452720245, https://www.hse.ru/edu/courses/1048866056 | Программы курсов ВШЭ «Теория и практика онлайн-экспериментов» и «A/B-тестирование: углублённый курс» — подтверждают академический канон тем (peeking и sequential analysis, A/B/X и множественная проверка, ускорение через CUPED и стратификацию). |
| B59 | https://karpov.courses/simulator, https://karpov.courses/simulator-ds | Из цитат: симулятор karpov.courses фокусируется на нюансах чувствительности тестов, **выборе между t-тестом и бутстрапом**, работе с метриками-отношениями; продвинутые курсы — дельта-метод и линеаризация для ratio, causal inference (Diff-in-Diff) для случаев, когда классический A/B невозможен. |
| B60 | https://kolodezev.ru/mlsystemdesign.html, https://kolodezev.ru/reliable_ml_itmo.html, https://github.com/IrinaGoloshchapova/ml_system_design_doc_ru | Курс и шаблон ML System Design Doc на русском (Reliable ML). Шаблон — де-факто канон структуры MLSD-документа в RU-компаниях. |
| B61 | https://hirehi.ru/blog/livecoding-na-sobesedovanii-10-algoritmicheskikh-zadach-kotorye-sprashivaiut-chashche-vsego, https://it-interview.io/interview-tasks, https://solvit.space/coding?company_ids=55 | Подборки live-coding задач с реальных собеседований, в т.ч. фильтр по Ozon. |
| B62 | https://leetcode.com/discuss/interview-question/1203126/google-onsite-ml-questions, https://leetcode.com/discuss/interview-experience/5204597/…, https://www.teamblind.com/post/ml-engineer-interview-prep-xoqpz6zb | Из цитаты: кандидат начинал собеседование в Amazon на LLM-команду, но был переведён на **sponsored ads A/B testing ML team**, из-за чего весь виртуальный онсайт состоял из нерелевантных ему вопросов — и вывод «нужно тренировать статистику». Подтверждает: A/B-статистика реально спрашивается на MLE-онсайтах в ads/experimentation-командах. |
| B63 | https://www.geeksforgeeks.org/machine-learning/a-b-testing-vs-multi-armed-bandits-statistical-decision-making-in-ml/ | Разбор различий A/B vs MAB для интервью. |
| B64 | https://www.tryexponent.com/blog/machine-learning-system-design-interview-guide, https://interviewkickstart.com/blogs/articles/machine-learning-system-design-interview-guide | Гайды по MLSD; список типовых задач: Personalized Recommendation Systems, Ranking and Retrieval, Fraud Detection, ETA Prediction, Visual Search. |

---

## Вопросы с собеседований

Легенда тегов: `junior` / `middle` / `middle_plus`.
Формат: **вопрос** — `грейд` | источник/компания | ссылка.
Пометка `[A1:Senior]` означает «в источнике A1 стоит грейд Senior».

---

### A. A/B-тестирование и эксперименты

#### A.1 База: гипотезы, ошибки, p-value, мощность

1. **«Что такое A/B-тест с точки зрения статистики?»** — `junior` | A4 (RU-банк) | https://raw.githubusercontent.com/TheAndreyZakharov/IT-Interview-Question-Bank/main/RU/Questions_By_Topic_RU/%23%23%2014.%20Data%20-%20ML%20-%20Analytics.md
2. **«Что такое null hypothesis и alternative hypothesis в A/B тесте?»** — `junior` | A4
3. **«Что такое power теста?» / «От чего зависит мощность теста?»** — `junior` | A4; тот же вопрос независимо подтверждён в B1 («что такое мощность и почему её важно учитывать при анализе экспериментов») | https://habr.com/ru/articles/664512/
4. **«Что такое significance level?» / «Что такое p-value?» / «Как интерпретировать p-value правильно?»** — `junior` | A4; B1
5. **«What is a p-value? What is the difference between type-1 and type-2 error?»** — `junior` | A20, вопрос №9 | https://raw.githubusercontent.com/kojino/120-Data-Science-Interview-Questions/master/statistical-inference.md
6. **«Что означает statistical significance?» / «Что означает practical significance?» / «Почему статистическая значимость не равна бизнес-значимости?»** — `middle` | A4
7. **«Что такое confidence interval?» / «Почему confidence interval часто полезнее одного p-value?»** — `middle` | A4
8. **«What is a confidence interval and how do you interpret it?»** — `middle` | A20, вопрос №14
9. **«Что такое false positive?» / «Что такое false negative?» / «Какие компромиссы между ними в продуктовых экспериментах?»** — `junior` | A4
10. **«Как объяснить менеджеру, почему "рост на 3%" ещё не означает успех?»** — `middle` | A4
11. **«Что делать, если тест статистически незначим?» / «Можно ли считать тест "успешным", если статистической значимости нет?»** — `middle` | A4. Канонический разбор — «серые метрики» Авито (B10): корректная формулировка не «эффекта нет», а «если эффект есть, он лежит внутри доверительного интервала» | https://habr.com/ru/companies/avito/articles/571094/

#### A.2 Дизайн эксперимента: MDE, размер выборки, длительность

12. **«Как определить необходимую длительность A/B теста?»** — `middle` | **A1, Самокат** `[A1:Middle]` | https://raw.githubusercontent.com/ixlander/interview-questions/main/all-real-questions.md
    - Ожидаемый ответ из источника: power analysis; вход — α (обычно 0.05), мощность 1−β (обычно 0.8), MDE, дисперсия метрики; `n = (z_{α/2} + z_β)² · 2σ² / MDE²` на группу; делим на дневной трафик; тест должен покрывать полный цикл (минимум 1–2 недели ради сезонности); подглядывание без коррекции завышает FPR.
13. **«Что такое minimum detectable effect?» / «Как выбрать MDE?»** — `middle` | A4
14. **«Как рассчитать размер выборки для эксперимента?» / «От чего зависит необходимый размер выборки?»** — `middle` | A4
15. **«Как определить необходимый размер выборки до эксперимента?»** — `middle` | A4 (раздел 14.1 Статистика)
16. **Расчётная задача: «Текущий CTR ≈ 5%. Хотим заметить относительное изменение +5% (то есть 5.25%). При alpha=0.05, beta=0.2 — сколько нужно пользователей/просмотров? Достаточно ли у вас трафика, чтобы тест длился разумное время?»** — `middle` | A6/RecSys-силлабус того же автора | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/5%20Recommendations/5_syllabus.md
17. **«Как долго нужно держать эксперимент?» / «Почему важно покрыть полный продуктовый цикл пользователя?»** — `middle` | A4
18. **«Что делать, если трафика мало и тест будет идти слишком долго?» / «Какие альтернативы A/B тестированию вы знаете при маленьком трафике?»** — `middle_plus` | A4
19. **«Как проводить A/B тестирование при ограниченном трафике?»** — `middle_plus` | A4 (раздел 14.9.2)
20. **«Как определить длительность теста по предэкспериментальным данным?»** — `middle_plus` | B11 (Авито, часть 2: «увеличение срока бесполезно; определение срока в предэксп. период») | https://habr.com/ru/companies/avito/articles/571096/
21. **«Как рассчитать срок теста из MDE по старым данным, если вы используете границы Покока и поправку Бонферрони?»** — `middle_plus` | B17 (Учи.ру) | https://habr.com/ru/company/uchi_ru/blog/500918/

#### A.3 Рандомизация, сплит-система, A/A, SRM

22. **«Что такое A/A-тест и зачем он нужен?»** — `middle` | **A1, Constructor** `[A1:Middle]`
    - Ответ из источника: обе группы получают одинаковую версию; валидация системы сплитования; калибровка стат. критериев; проверка отсутствия ложных срабатываний.
23. **«What might be the benefits of running an A/A test, where you have two buckets who are exposed to the exact same product?»** — `middle` | A20, вопрос №2
24. **«In an A/B test, how can you check if assignment to the various buckets was truly random?»** — `middle` | A20, вопрос №1
25. **«Что такое randomization?» / «Почему рандомизация важна?»** — `junior` | A4
26. **«Что такое unit of randomization?» / «На каком уровне можно рандомизировать эксперимент: user, session, device, account, team?» / «Какие проблемы возникают при выборе неправильной единицы рандомизации?»** — `middle` | A4
27. **«Как выбрать unit of randomization в A/B тесте?»** — `middle` | A4 (раздел 14.9.2)
28. **«Randomization unit. 為何選擇這個，而不是另一個？最常回答的用 user_id 來當作 randomization unit, pros and cons?»** (кит.: «Почему выбрали именно эту единицу, а не другую? Чаще всего отвечают user_id — какие pros/cons?») — `middle` | A16 | https://raw.githubusercontent.com/LongxingTan/Machine-learning-interview/master/02_ml/97_product_sense.md
29. **«Что такое sample ratio mismatch?» / «Как обнаружить sample ratio mismatch?» / «Какие причины sample ratio mismatch вы знаете?»** — `middle_plus` | A4. Канон ответа — B33 (Microsoft EXP): chi-squared goodness-of-fit; причины на стадиях Assignment / Execution / Log Processing / Analysis; частота 6–10% тестов | https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/
30. **«Как понять, что эксперимент испорчен из-за плохой рандомизации?» / «Какие sanity checks нужны перед анализом A/B теста?»** — `middle_plus` | A4
31. **«Как показать разницу между A/B-группами?» / «Как визуализировать confidence intervals для A/B test?»** — `junior` | A4 (раздел 14.6 Visualization)
32. **«Как проверить корректность итоговых таблиц по эксперименту?» / «Как понять, можно ли доверять данным эксперимента?»** — `middle` | A4
33. **«Как проверить сплит-систему на FPR через A/A: сначала на искусственных данных, затем на реальных?»** — `middle_plus` | B10 (Авито), B18 (ВК: равномерность p-value на A/A) | https://vkteam.medium.com/practitioners-guide-to-statistical-tests-ed2d580ef04f

#### A.4 Подглядывание (peeking) и sequential testing

34. **«Почему peeking в A/B-тестах опасен?»** — `middle` | A4 (раздел 14.1)
35. **«Что такое peeking problem?» / «Почему эксперимент нельзя останавливать слишком рано?»** — `middle` | A4
36. **«Что такое преждевременная остановка теста?»** — `middle` | B1 | https://habr.com/ru/articles/664512/
37. **«What would be the hazards of letting users sneak a peek at the other bucket in an A/B test?»** — `middle` | A20, вопрос №3 *(это про peek пользователя в чужую группу — родственный, но иной сюжет: контаминация)*
38. **«Что такое sequential testing?» / «Как Sequential Testing помогает в онлайн-экспериментах?»** — `middle_plus` | A4
39. **«Расскажите про границы Покока и О'Брайена–Флеминга. Чем они отличаются?»** — `middle_plus` | B17 (Учи.ру, разбор с Optimizely)
40. **«Можно ли добирать выборку, если тест "почти прокрасился"?»** — `middle` | B (карта A2: «Карпов — подглядывания: нельзя добирать выборку для подгона; срок заранее, решение в конце — фиксируем FPR») | https://raw.githubusercontent.com/kirmipt/ab_articles/main/README.md
41. **«Какие бывают критерии остановки эксперимента?»** — `middle_plus` | A4
42. **«Что такое always-valid p-value и чем group-sequential отличается от always-valid подхода?»** — `middle_plus` | A7 (конспект «Sequential-тесты и CUPED», разделы 2.2 и 2.3) | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests/4%20Sequential%20Tests%20and%20CUPED.md

#### A.5 Множественные сравнения

43. **«В A/B-тесте 5 из 100 метрик статистически значимо положительны, остальные нейтральны. Выкатываем или нет?»** — `middle_plus` | **A1, Constructor** `[A1:Senior]`
    - Ответ из источника: при 100 метриках и α=5% ожидаем ~5 ложных срабатываний просто по случайности; нужно (1) Бонферрони или FDR-контроль, (2) проверить, попали ли ключевые бизнес-метрики в эти 5, (3) посмотреть направление и величину эффекта.
44. **«Что такое multiple testing problem?» / «Как корректировать множественные сравнения?» / «Что такое Bonferroni correction?» / «Что такое false discovery rate?»** — `middle` | A4
45. **«How would you run an A/B test for many variants, say 20 or more?»** — `middle_plus` | A20, вопрос №6
46. **«I have two different experiments that both change the sign-up button to my website. I want to test them at the same time. What kinds of things should I keep in mind?»** — `middle_plus` | A20, вопрос №8
47. **«Что такое experiment collision?» / «Как избежать конфликтов между параллельными экспериментами?» / «Как multiple concurrent experiments влияют на выводы?»** — `middle_plus` | A4
48. **«Как анализировать A/B тест по сегментам без p-hacking?» / «Как бороться с p-hacking?»** — `middle_plus` | A4
49. **«Почему пост-хок поиск сегментов опасен?»** — `middle_plus` | A4

#### A.6 Снижение дисперсии: CUPED, стратификация, трансформации

50. **«Что такое CUPED и когда он полезен?»** — `middle_plus` | A4 (встречается дважды: разделы 14.9.2 и 14.10)
51. **«Как уменьшать дисперсию в онлайн-экспериментах?» / «Как уменьшить variance в A/B тесте?»** — `middle_plus` | A4
52. **«Что такое stratification в экспериментах?» / «Когда полезно использовать blocked randomization?»** — `middle_plus` | A4
53. **«CUPED vs стратификация — что выбрать и почему? Можно ли комбинировать?»** — `middle_plus` | B6 (X5 Tech: «А/Б тестирование: CUPED vs Stratification»), B11 (Авито: сравнение всех методов и их комбинаций с парной стратификацией) | https://habr.com/ru/companies/X5Tech/articles/826488/
54. **«Напишите формулу CUPED и объясните каждый член»** — `middle_plus` | A3: `Y_cuped_i = Y_i − (X_i − X_mean) · Cov(X,Y)/Var(X)`; `Var(Y_cuped) = Var(Y)·(1 − ρ(X,Y)²)`; альтернативный путь — оценить θ линейной регрессией и взять `Y − θX` | https://raw.githubusercontent.com/alselezneva/ds_mentor/main/Notion/%D0%9C%D0%B5%D0%BD%D1%82%D0%BE%D1%80%D1%81%D1%82%D0%B2%D0%BE/AB-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.md
55. **«Какие ограничения у CUPED?»** — `middle_plus` | A3 (считается только для разницы средних; неочевиден выбор предэксп. периода; иногда трансформирует данные некорректно и ведёт к неверным выводам), A7 (раздел 3.4 «Ограничения и подводные камни»)
56. **«Что такое CUPAC и чем отличается от CUPED?»** — `middle_plus` | A3
57. **«Как выбросы влияют на мощность теста и что с ними делать?»** — `middle_plus` | B10 (Авито): выбросы увеличивают дисперсию → тест менее мощный; **как не надо**: Манн–Уитни, логарифмирование метрики, выкидывание выбросов; **выкидывать выбросы по предэкспериментальному периоду можно**
58. **«Что такое winsorization и когда её используют?»** — `middle_plus` | A4
59. **«Как работать с heavy-tailed распределениями в экспериментах?» / «Почему revenue-метрики часто "шумные"?»** — `middle_plus` | A4; A6 (раздел 7.2 «Сильно правохвостые метрики (выручка)»)
60. **«Какие трансформации метрики снижают дисперсию и чем они опасны?»** — `middle_plus` | A3: корень, логарифм, Бокс-Кокс, ранжирование; опасность — смена *направленности* метрики (пример: после логарифма значения около нуля становятся отрицательными, и если там сидит большая часть выборки, лифт станет отрицательным)
61. **«Если CUPED даёт R² ≈ 0.3, на сколько упадёт требуемый N?»** — `middle_plus` | A6 (раздел 6.2: ответ — примерно на 30%)
62. **«Что такое анализ exposured (вовлечённых) пользователей и зачем он нужен?»** — `middle_plus` | A3 (пример: при тестировании нового алгоритма поиска в группы включаем только тех, кто поиском пользуется)

#### A.7 Ratio-метрики: дельта-метод, линеаризация, бутстрап, бакетизация

63. **«Чем наивный CTR отличается от global CTR? Посчитайте на примере: два пользователя с (10 просмотров, 1 клик) и (100 просмотров, 20 кликов)»** — `middle_plus` | A3: наивный `(0.1+0.2)/2 = 0.15`, global `(1+20)/(10+100) ≈ 0.27`, bias = 0.12
64. **«Какими способами корректно анализировать ratio-метрику?»** — `middle_plus` | A3: (1) бутстрап с весами по знаменателю, (2) пуассоновский бутстрап, (3) линеаризация `X − k·Y`, где `k` из регрессии числителя на знаменатель (и поверх линеаризации можно накинуть CUPED), (4) дельта-метод
65. **«Почему для ratio-метрик нужен дельта-метод? Что будет, если посчитать дисперсию наивно?»** — `middle_plus` | B28: числитель и знаменатель коррелированы; наивная оценка даёт анти-консервативные ДИ и больше ложных срабатываний | https://www.datainterview.com/blog/ab-testing-interview-questions
66. **«В чём связь между CUPED и дельта-методом?»** — `middle_plus` | B35: CUPED эквивалентен дельта-методу, если в качестве ковариаты взять знаменатель | https://srome.github.io/Connections-Between-the-Delta-Method-OLS-and-CUPED-Illustrated/
67. **«Как выбрать критерий для метрики: t-тест, Манн–Уитни, binom-Z, бутстрап, дельта-метод, бакетизация или линеаризация?»** — `middle_plus` | B18 (ВК): для `clicks` сравнивают t-тест vs Манна–Уитни; для `globalCTR` — binom-Z, bootstrap, delta-method, бакетизация, линеаризация; выбор делают сравнением FPR и мощности на искусственных данных
68. **«Когда бутстрап лучше t-теста и какие у него ограничения?»** — `middle_plus` | B9: бутстрап применяют, когда t-test не работает; минимум N≈100+; предполагает IID (для временных рядов и кластеров нужен block bootstrap); при выбросах — робастные статистики (медиана, winsorized)
69. **«Что такое пуассоновский бутстрап и зачем он нужен?»** — `middle_plus` | A3, B9: распределение Пуассона с λ=1 приближает биномиальное; позволяет считать бутстрап распределённо, когда n заранее неизвестен
70. **«Что такое бакетизация и что она даёт?»** — `middle_plus` | A2, B9: сохраняет информацию о дисперсии и среднем до трансформации и приводит распределение к нормальному
71. **«Как анализировать A/B тест с бинарной метрикой?» / «Как анализировать A/B тест с revenue-метрикой?»** — `middle` | A4
72. **«How would you run an A/B test if the observations are extremely right-skewed?»** — `middle_plus` | A20, вопрос №7
73. **«Как придумать любую метрику через числитель и знаменатель? Покажите, что любую метрику можно свести к ratio»** — `middle_plus` | A3 (раздел «Как придумать любую метрику с помощью числителей и знаменателей»)

#### A.8 Сетевые эффекты, SUTVA, switchback, interference

74. **«Что такое network effect в экспериментах?» / «Почему некоторые A/B тесты нарушают предположение независимости наблюдений?» / «Что такое interference between users?» / «Почему на маркетплейсах и в соцсетях A/B тесты сложнее?»** — `middle_plus` | A4
75. **«Почему network effects и interference особенно опасны для экспериментов с рекомендациями и соцпродуктами?»** — `middle_plus` | A4 (раздел 14.9.2)
76. **«如何 identify network effect? How to mitigate the risk?»** («Как идентифицировать сетевой эффект? Как снизить риск?») — `middle_plus` | A16
77. **«Чем A/B тест отличается от сплит-теста, multivariate test и switchback experiment?»** — `middle_plus` | A4
78. **«Что такое SUTVA и как понять, что оно нарушено? Что делать?»** — `middle_plus` | A3: SUTVA — юниты эксперимента не влияют друг на друга; spillover effect — группы влияют друг на друга; **решение — сменить единицу рандомизации** (из магазинов → в группы магазинов по округам; из пользователей → в кассы)
79. **«Что такое contamination в A/B тестировании?» / «Что такое carryover effect?»** — `middle_plus` | A4 (contamination — в обоих разделах, 14.9.2 и 14.10)
80. **«Как провести A/B тест двух execution-алгоритмов в live trading?»** — `middle` | **A1, HFT-компания (крипта/трейдинг)** `[A1:Middle]`
    - Ответ из источника — фактически switchback: рандомизировать по инструментам, раз в час/день делать switch для устранения time-of-day эффектов; метрика — slippage, нормированный на волатильность; нельзя чередовать по дням целиком (рыночная конъюнктура — confounder); paired test (Wilcoxon или t-test на разностях по инструментам); минимум неделя.
81. **«Когда классический A/B невозможен из-за сетевых эффектов — что использовать вместо него?»** — `middle_plus` | B14/B15/B16: switchback (Ситимобил, Delivery Club, Авито). Полезный факт для ответа: сетевые эффекты, измеренные классическим A/B, примерно **в 3 раза выше**, чем измеренные switchback | https://habr.com/ru/companies/deliveryclub/articles/670762/
82. **«Clustered A/B testing — когда и почему?»** — `middle_plus` | B46 (Airbnb DS: явно в списке компетенций) | https://www.interviewquery.com/interview-guides/airbnb-data-scientist
83. **«Как дизайн-эффект при кластеризации влияет на нужный размер выборки?»** — `middle_plus` | A6 (раздел 6.3 «Кластеризация (дизайн-эффект)»)

#### A.9 Novelty / primacy, сезонность, внешние шоки

84. **«Как учитывать novelty effect в A/B тесте?»** — `middle_plus` | A4 (раздел 14.9.2); «Что такое novelty effect?» — `middle` | A4 (раздел 14.10)
85. **«Как отличить novelty от primacy и как их детектить?»** — `middle_plus` | B53: строить treatment effect по времени (лифт большой на 1-й неделе и сжимается к 3-й → novelty); сегментация new vs returning; сравнение первичных пользователей control vs treatment
86. **«Как учитывать сезонность и внешние события в результатах A/B теста?» / «Как сезонность и внешние события ломают A/B тест?»** — `middle` | A4
87. **«Что делать, если во время теста произошла акция, праздник или outage?»** — `middle_plus` | A4
88. **«Как бы вы анализировали эксперимент, если в процессе изменили реализацию фичи?»** — `middle_plus` | A4
89. **«What would be some issues if blogs decide to cover one of your experimental groups?»** — `middle_plus` | A20, вопрос №4

#### A.10 Парадокс Симпсона, сегментация, HTE

90. **«Что такое парадокс Симпсона и как он ломает A/B-тест?»** — `middle_plus` | B31 (заявлено как «крайне популярная тема на интервью, часто возникает неявно»), B32 | https://bookdown.org/madinterviewllc/Product-Data-Science-Interview-The-Bar-to-Get-Hired/ab.html
    - Опорные факты для ответа (B32): для возникновения нужны **неравные сплиты** — часто следствие багованной рандомизации → selection bias; при агрегации доминируют ячейки с бо́льшим объёмом и переворачивают знак; минимальный набор проверочных сегментов — device type, traffic source, new vs returning.
91. **«Что такое heterogeneous treatment effect?» / «Как искать сегменты, в которых эффект отличается?»** — `middle_plus` | A4
92. **«Что делать, если primary metric выросла у новых пользователей, но упала у старых?»** — `middle_plus` | A4
93. **«Как бы вы анализировали результат A/B теста, если эффект положительный только на одном рынке?»** — `middle_plus` | A4
94. **«Как анализировать метрики, если пользователи очень неоднородны?»** — `middle_plus` | A4

#### A.11 Метрики: primary / secondary / guardrail и принятие решения

95. **«Что такое guardrail metrics и зачем они нужны?» / «Как выбрать guardrail metrics для эксперимента?»** — `middle` | A4 (в обоих разделах)
96. **«Зачем нужны guardrail metrics при запуске экспериментов?»** — `middle` | A4 (раздел 14.2)
97. **«Какие guardrail metrics нужны для A/B теста модели?»** — `middle` | A4 (раздел 14.9.2)
98. **«Что делать, если guardrail metrics ухудшились, а primary metric выросла?»** — `middle_plus` | A4
99. **«Как выбрать основную метрику для A/B теста?» / «Как выбрать secondary metrics?»** — `middle` | A4
100. **«Как выбрать primary metric для A/B теста модели?»** — `middle` | A4 (раздел 14.9.2)
101. **«Какие метрики вы бы использовали для recommendation system в A/B тесте?» / «…для fraud model?» / «…для ad ranking или search ranking?»** — `middle_plus` | A4 (раздел 14.9.2) — прямо релевантно MLE
102. **«Какие метрики вы бы выбрали для теста поисковой выдачи?» / «…для теста рекомендательной системы?» / «…для теста paywall?»** — `middle` | A4
103. **«Что такое leading metrics и lagging metrics?» / «Какие метрики могут улучшиться локально, но ухудшить продукт в целом?»** — `middle` | A4
104. **«After running a test, you see the desired metric, such as the click-through rate is going up while the number of impressions is decreasing. How would you make a decision?»** — `middle_plus` | B29/B30 (Emma Ding / KDnuggets) | https://medium.com/data-science/7-a-b-testing-questions-and-answers-in-data-science-interviews-eee6428a8b63
105. **«Как принимать решение по результатам A/B теста?»** — `middle` | A4
106. **«Что если в тесте новая рекомендательная система показала лучшие клики, но пользователи стали меньше времени проводить на платформе? Как интерпретировать?»** — `middle_plus` | A6-репозиторий, RecSys-силлабус (ожидаемый ответ: кликают на менее релевантное и быстро уходят → улучшение некачественное) | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/5%20Recommendations/5_syllabus.md
107. **«Какая метрика важнее — Precision@K или Recall@K — для вашего домена?»** (как разогрев перед вопросом про метрику A/B) — `middle` | тот же силлабус
108. **«Что такое north star metric?» / «Чем north star metric отличается от KPI?» / «Что такое vanity metrics и почему они опасны?»** — `junior` | A4

#### A.12 Продуктовые кейсы «спроектируйте эксперимент»

109. **«Company X has tested a new feature with the goal to increase the number of posts created per user. They assigned each user randomly to either the control or treatment group. The Test won by 1% in terms of the number of posts. What do you expect to happen after the new feature is launched to all users? Will it be the same as 1%, if not, would it be more or less?»** — `middle_plus` | B29/B30
110. **«We are launching a new feature that provides coupons to our riders. The goal is to increase the number of rides by decreasing the price for each ride. Outline a testing strategy to evaluate the effect of the new feature.»** — `middle_plus` | B29/B30
111. **«There are a few ideas to increase conversion on an e-commerce website: enabling multiple-item checkout, allowing non-registered users to checkout, changing the size and color of the "Purchase" button, etc. How do you select which idea to invest in?»** — `middle` | B29/B30
112. **«You are AirBnB and you want to test the hypothesis that a greater number of photographs increases the chances that a buyer selects the listing. How would you test this hypothesis?»** — `middle` | A20, вопрос №10
113. **«How would you design an experiment to determine the impact of latency on user engagement?»** — `middle_plus` | A20, вопрос №11
114. **«How would you conduct an A/B test on an opt-in feature?»** — `middle_plus` | A20, вопрос №5
115. **«Как бы вы провели A/B тест для изменения цены?»** — `middle_plus` | A4
116. **«Как бы вы тестировали изменение recommendation ranking?»** — `middle_plus` | A4
117. **«Как бы вы тестировали новую onboarding flow?» / «Как бы вы тестировали push-уведомления?»** — `middle` | A4
118. **«Как бы вы тестировали алгоритм антифрода, не раскрывая условия злоумышленникам?»** — `middle_plus` | A4
119. **«Составьте план A/B-теста для внедрения вашей новой рекомендательной системы: основная метрика, guardrail-метрики, длительность, процент аудитории»** — `middle` | RecSys-силлабус (A6-репозиторий): в примере — CTR как primary, average watch time как guardrail, 2 недели (чтобы захватить два выходных), 50/50 или 30% на тест
120. **«У вас новый алгоритм дал +5% офлайн precision. Будете ли вы раскатывать?»** — `middle` | тот же силлабус; ожидаемый ответ: офлайн — прокси, нужен A/B; определить метрику (например CTR), 2 недели на 10% аудитории, посмотреть значимость
121. **«Как бы вы оценивали эффект новой фичи без полноценного рандомизированного эксперимента?»** — `middle_plus` | A4 (раздел 14.1)
122. **«Как вы бы оценили влияние маркетинговой кампании, если невозможно провести A/B-тест?»** — `middle_plus` | Spirzen/it-knowledge-base, `docs/lab/questions/120.md` (найдено кодовым поиском GitHub) | https://github.com/Spirzen/it-knowledge-base/blob/main/docs/lab/questions/120.md

#### A.13 A/B для ML-моделей (специфика MLE)

123. **«Чем A/B тест модели отличается от A/B теста обычной продуктовой фичи?»** — `middle_plus` | A4 (14.9.2)
124. **«Что такое A/B тестирование и зачем оно нужно в контексте ML?»** — `junior` | A4 (14.9.2)
125. **«Как A/B тестировать ranking-модель, не сломав пользовательский опыт?» / «Как A/B тестировать search/ranking без слишком длинного цикла эксперимента?»** — `middle_plus` | A4 (14.9.2)
126. **«Как A/B тестировать fraud-модель, если ground truth приходит через месяцы?»** — `middle_plus` | A4 (14.9.2)
127. **«Как A/B тестировать модель в regulated domain, где нельзя всем пользователям показывать рискованную версию?»** — `middle_plus` | A4 (14.9.2)
128. **«Чем shadow deployment отличается от A/B теста?» / «Когда лучше использовать shadow mode, а когда A/B test?»** — `middle_plus` | A4 (14.9.2)
129. **«Как сочетать shadow mode, canary rollout и A/B test в одном релизном процессе?»** — `middle_plus` | A4 (14.9.2)
130. **«Что такое canary release и чем он отличается от A/B теста?» / «Чем feature flag отличается от эксперимента?» / «Что такое dark launch?»** — `middle` | A4
131. **«Как registry помогает A/B тестировать несколько версий моделей?» / «Как связать результаты A/B теста с model registry?»** — `middle_plus` | A4
132. **«A/B тест рекомендательной системы не показал статистически значимого улучшения. Что делать?»** — `middle_plus` | **A1, Дром.ру** `[A1:Senior]`
    - Ответ из источника: сегментация (активные, на ком учились, vs новые); просадка на новых → cold start, нужна онлайн-компонента (SASRec на последних интеракциях); проверить корреляцию офлайн и онлайн метрик; проверить методологию (длительность, размер выборки); посмотреть secondary metrics.
133. **«Расскажите про ваш опыт с A/B-тестированием»** — `middle` | **A1, Constructor** `[A1:Middle]`
    - Ожидаемый уровень для MLE (из источника): деплой сервиса на тестовую группу, стратификация групп (по регионам, возрасту), двухнедельный тест с α=5%, проверка MDE; полный статистический анализ делегируется аналитикам, MLE отвечает за feature flags и конфигурацию сплита. **Это калибровка планки для middle MLE.**
134. **«Как проводить A/B тестирование модели так, чтобы не навредить бизнесу?»** — `middle_plus` | A4
135. **«Как бы вы организовали эксперимент, чтобы сравнить несколько моделей честно?» / «Что нужно зафиксировать, чтобы результаты эксперимента были воспроизводимыми?»** — `middle` | A4 (14.8)
136. **«Почему uplift-модели не отменяют A/B-тесты?» / «Как дизайнить A/B для uplift-модели?»** — `middle_plus` | A10 (разделы 5.2 и 5.3) | https://raw.githubusercontent.com/Maha-Rossomaha/LLM_projects/main/6%20ML%20System%20Design/2%20Algorithms%20and%20Methods/1%20AB%20Tests/6%20AB%20Testing%20in%20ML%20Context.md
137. **«Почему офлайн-метрики растут, а онлайн — нет? Как связывать офлайн ↔ онлайн?»** — `middle_plus` | A10 (разделы 4.3 и 4.4)

#### A.14 Бандиты, holdout, causal inference

138. **«Бандиты vs A/B — когда что?»** — `middle_plus` | A14 (шаг 8 MLSD прямо содержит и A/B Experiments, и Bandits), B39, B63
    - Опорный ответ (B39): A/B — период чистого exploration, затем длинный exploitation; бандиты чередуют оба адаптивно; A/B нужен, когда важна оценка эффекта с ДИ и понимание treatment effect; бандиты — когда важна автоматическая максимизация метрики без промежуточной интерпретации.
139. **«Когда использовать holdout group?»** — `middle_plus` | A4
140. **«Что такое global holdout и как он устроен?»** — `middle_plus` | B40: доля пользователей изолируется от **всех** экспериментов и раскаток на уровне продукта и всех команд; так меряется кумулятивный эффект программы экспериментов; рекомендация — не более 5% трафика
141. **«Что такое causal inference и где он может быть полезен в product analytics?» / «Что такое pre-post analysis и какие у него ограничения?» / «Что такое difference-in-differences?» / «Когда можно использовать synthetic control?» / «Что такое quasi-experiments?»** — `middle_plus` | A4
142. **«В чем разница между наблюдательными данными и экспериментальными?»** — `middle` | A4 (14.1)
143. **«Чтобы доказать causation, нужен рандомизированный эксперимент или causal inference (do-оператор Пёрла, backdoor criterion). Объясните разницу»** — `middle_plus` | ST1SLE/interviews-prep-knowledge-base, `math-and-stats/applied_stats.md` (найдено кодовым поиском GitHub; raw-файл вернул 404, содержимое видел только во фрагменте кодового поиска) | https://github.com/ST1SLE/interviews-prep-knowledge-base
144. **«Как оценить новую политику (другой таргетинг или размер скидки), не разыгрывая полноценный A/B?»** — `middle_plus` | Maha-Rossomaha, `6 ML System Design/2 Algorithms and Methods/2 Uplift Modeling/8 Modern Causal Methods.md` (off-policy evaluation по логам исторической политики π₀)

#### A.15 Платформа экспериментов и процесс

145. **«Что такое experiment platform?» / «Что обычно входит в платформу экспериментов?» / «Какие проблемы возникают при масштабировании платформы A/B тестов?»** — `middle_plus` | A4
146. **«Зачем нужна платформа экспериментов, если аналитики умеют считать тесты руками?»** — `middle_plus` | A3: сфокусировать время аналитиков на важном + унификация (два аналитика могут получить разные результаты по одному тесту). Дополнительно — репозиторий метрик с явной спецификацией (пример из источника: `name: arpu; metric_type: continuous; numerator: {aggregation_function: sum, aggregation_field: revenue}; level: client_id; estimator: t_test_delta_method`)
147. **«Как вы проектируете систему логирования результатов экспериментов?» / «Как хранить метаданные эксперимента?» / «Как хранить историю экспериментов и решений о деплое?»** — `middle_plus` | A4
148. **«Как бы вы выстроили систему экспериментов в компании с нуля?»** — `middle_plus` | A4
149. **«Как бы вы организовали governance для продуктовых экспериментов?» / «Кто должен одобрять запуск эксперимента с новой моделью?»** — `middle_plus` | A4
150. **«Какие вопросы вы зададите перед тем, как запускать A/B тест?» / «Какие вопросы вы зададите после завершения A/B теста?»** — `middle` | A4
151. **«Как бы вы презентовали результаты A/B теста нетехнической аудитории?»** — `middle` | A4
152. **«Какие ошибки вы чаще всего видите в A/B тестировании?» / «Какие антипаттерны A/B тестирования моделей вы встречали?»** — `middle_plus` | A4
153. **«Какие вопросы вы бы задали кандидату, чтобы понять, что он реально запускал A/B тесты моделей, а не просто знает определения?»** — `middle_plus` | A4 — **мета-вопрос, полезен для хендбука как источник «фильтров глубины»**
154. **«Как искать прокси-метрики и оценивать их направленность?»** — `middle_plus` | A3: три способа, все требуют исторического корпуса экспериментов — (1) Label Agreement (`MAX(N⁺;N⁻)/N`, с отсылкой к Dmitriev & Wu, «Measuring metrics», CIKM 2016), (2) корреляция метрик по стат-значимым дельтам, (3) корреляция по t-статистикам. Если истории нет — начать её вести, провести обратные ухудшающие эксперименты
155. **«Как валидировать критерий через Монте-Карло симуляции?»** — `middle_plus` | A3: по очереди валидировать FPR (в каком % случаев прокрас на A/A) и TPR (домножая на лифт с шагом, например 1%→10%). Детали: для дискретных величин не домножать на лифт (0·x = 0), а генерировать биномиальные распределения с заданной p; для остальных домножать на нормальное распределение со средним x; для ratio-метрик менять только числитель; моделировать эффект константой / нормальным / равномерным / скошенным распределением
156. **«Как оценить этические риски эксперимента?» / «Какие эксперименты можно считать этически сомнительными?» / «В каких случаях вы бы запретили запуск эксперимента?»** — `middle_plus` | A4

---

### B. ML System Design

#### B.1 Формат и ожидаемая структура ответа

**Первоисточник от работодателя (Т-Банк, A18)** — дословная канва секции:
> «форматизация задачи и требований → декомпозиция на подзадачи → сбор данных → разбор ML архитектур для подзадач → деплой и тестирование итоговой системы».

**RU-схема на 60 минут с таймингом (A12):**
1. Уточнить требования (5 мин) — бизнес-цель, метрики успеха, constraints (latency, throughput, budget, regulatory).
2. Прикинуть масштаб (3 мин) — сколько пользователей, запросов, данных; на чём упрёмся.
3. Выбрать ML-формулировку (5 мин) — классификация / регрессия / ranking / generation; что предсказываем, что метрика.
4. Данные (10 мин) — источники, разметка, frequency, edge cases.
5. Модель (10 мин) — baseline → улучшение, train pipeline.
6. Eval (5 мин) — offline метрики + online A/B.
7. System (10 мин) — feature store, training, serving, monitoring.
8. Iteration (5 мин) — что мониторим, когда retrain, как ловим drift.
> Правило источника: «не молчите. Каждый шаг — обсуждайте вслух с интервьюером. Спрашивайте уточнения.»

**Развёрнутый RU-сценарий на 14 шагов (A5):** clarify the problem → functional requirements → non-functional requirements → estimate scale → product and ML metrics → data collection and labels → high-level architecture → offline training → online inference → storage and freshness → failures and degradation → monitoring and retraining → security and privacy → bottlenecks and trade-offs.
Принцип хорошего ответа оттуда же: `requirement → design decision → guarantee → cost → alternative`, и явное предупреждение, что «необоснованный список Kafka, Kubernetes и нескольких БД» — слабый ответ.

**9-шаговая англоязычная формула (A14):** Problem Formulation → Metrics (offline/online) → Architectural Components (MVP logic) → Data Collection and Preparation → Feature Engineering → Model Development and Offline Evaluation → Prediction Service → **Online Testing and Model Deployment (A/B Experiments, Bandits, Shadow deployment, Canary release)** → Scaling, Monitoring, and Updates.

**Что должно быть в «полном разборе» (A5, чек-лист):** исходная формулировка; уточняющие вопросы кандидата; предположения и оценки масштаба; product metrics и ML metrics; data generation и feedback loops; baseline и развитие модели; training pipeline; online serving; storage и caching; freshness и consistency; scaling; failure modes; observability; privacy и abuse cases; альтернативы; финальный walkthrough на 35–45 минут.

**Из RU-практики (B23, Яндекс Практикум):** первый этап всегда сбор требований — кандидат должен *сам* сформировать список требований, задавая вопросы интервьюеру; цель — не найти единственно верное решение, а показать системное мышление, работу с абстракциями, логичное построение архитектуры и обоснованный выбор технологий.

**Из RU-практики (B19, ODS):** типичный провал — прыгать между моделью, данными и деплоем, забыв спросить про бизнес.

#### B.2 Реальные кейсы, названные на собеседованиях (RU, с компанией)

Все из **A1** (`ixlander/interview-questions`), грейд источника указан в скобках:

157. **«Как бы вы спроектировали систему рекомендации видео для e-commerce платформы?»** — `middle_plus` | Самокат `[Senior]`
158. **«Как вывести ML-модель рекомендаций в продакшн?»** — `middle` | Самокат `[Middle]`
159. **«Как спроектировать систему антифрод-детекции?»** — `middle_plus` | Сбер (антифрод) `[Senior]`
160. **«Как спроектировать антифрод для банковских транзакций?»** — `middle_plus` | Т-Банк (Тинькофф) `[Senior]`
161. **«Как происходит деплой ML-модели в продакшн?»** — `middle` | Ozon `[Middle]`
162. **«Как закодировать товар с 7000 разнородными атрибутами для нейросетевой модели рекомендаций?»** — `middle_plus` | Ozon `[Senior]`
163. **«Как построить эмбеддинг пользователя на основе его последовательности действий?»** — `middle_plus` | Ozon `[Senior]`
164. **«Как объединить эмбеддинги пользователя и товара для предсказания релевантности?»** — `middle_plus` | Ozon `[Senior]`
165. **«Как оптимизировать тяжёлую модель рекомендаций для продакшн-инференса?»** — `middle` | Ozon `[Middle]`
166. **«Как бы вы строили систему генерации текстовых описаний для карточек товаров при запуске в новой стране (Китай)?»** — `middle_plus` | Яндекс (Поиск, объектные ответы) `[Senior]`
167. **«Как построить офлайн-метрику качества генерации текстов?»** — `middle` | Яндекс (Поиск, объектные ответы) `[Middle]`
168. **«Расскажите про полный ML-пайплайн от сбора данных до инференса — какие этапы и инструменты использовали?»** — `middle` | Infomedia `[Middle]`
169. **«Есть ли опыт с оптимизацией инференса — TensorRT, квантизация и т.д.?»** — `middle` | Infomedia `[Middle]`
170. **«Какие инструменты используете для логирования экспериментов и версионирования моделей?»** — `middle` | Infomedia `[Middle]`
171. **«Есть ли у вас on-call дежурство? Как организован мониторинг сервисов?»** — `middle` | Constructor `[Middle]`
172. **«Как работает индекс IVF (Inverted File Index) в библиотеке FAISS?»** — `middle` | ZinBrains `[Middle]`
173. **«Обучение модели занимает 12 часов. Как искать узкое место и ускорить процесс?»** — `middle` | ZinBrains `[Middle]`
174. **«Как обеспечить латентность inference ML-модели менее 100 мс?»** — `middle` | ZinBrains `[Middle]`
175. **«Как вы работали с ограничением размерности эмбеддингов (256) в OpenSearch?»** — `middle` | Waibee `[Middle]`
176. **«Какие тесты вы писали для ML-модели (ассистента) и как оценивали качество?»** — `middle` | Waibee `[Middle]`
177. **«Как спроектировать систему для выбора оптимального банковского продукта с помощью LLM-двойника клиента?»** — `middle_plus` | ВТБ `[Senior]`
178. **«Техническое собеседование: кодинг + ML System Design + System Design интеграции ML в highload»** — `middle` | Mayflower `[Middle]` — важен сам факт совмещения трёх форматов в одной секции
179. **«ML System Design: Спроектируйте систему предсказания задержек в портах для оптимизации скорости кораблей и экономии топлива»** — `middle_plus` | Quantum One `[Senior]`
180. **«Как вы построите таргет для модели предсказания задержки в порту? Какая гранулярность агрегации оптимальна?»** — `middle` | Quantum One `[Middle]` — **типовой follow-up: «а как вы определите таргет?»**
181. **«Какие фичи вы предложите для модели предсказания задержки в порту?»** — `middle` | Quantum One `[Middle]`
182. **«ML System Design: Оптимизируйте подбор контрольных вопросов для верификации клиентов в колл-центре банка (из 100 вопросов выбрать 5 лучших для каждого клиента)»** — `middle_plus` | Т-Банк `[Senior]`
183. **«ML System Design: Спроектируйте рекомендательную систему коротких видео (TikTok-like) с бесконечной лентой»** — `middle_plus` | VK `[Senior]`
184. **«Что такое Approximate Nearest Neighbor Search (ANN)? Какие алгоритмы знаете?»** — `middle` | VK `[Middle]` — follow-up внутри MLSD-секции
185. **«ML System Design: Спроектируйте систему подбора сочетаемой одежды (outfit recommendation) — к юбке подобрать туфли, верх и аксессуары»** — `middle_plus` | Wildberries `[Senior]`
186. **«Какие проблемы вы видите при создании LLM-агента для генерации SQL-запросов к legacy-базе?»** — `middle_plus` | PulsePoint `[Senior]`
187. **«Стоит ли интегрировать существующие отчёты компании как tool для LLM? Какие проблемы?»** — `middle` | PulsePoint `[Middle]`
188. **«System Design: спроектируйте систему ранжирования для e-commerce поиска. Сначала простое решение, затем сложнее»** — `middle_plus` | Constructor `[Senior]` — **явная инструкция «сначала baseline» прямо в постановке**
189. **«Как масштабировать ранкер при миллионе кандидатов? Пользователь не дождётся инференса бустинга»** — `middle_plus` | Constructor `[Senior]`
190. **«Был ли у вас опыт проектирования ML-архитектуры с нуля? Расскажите о таком кейсе»** — `middle` | Navi / Corsearch `[Middle]`
191. **«System Design: спроектируйте рекомендательную систему для ленты объявлений подержанных авто»** — `middle_plus` | Дром.ру `[Senior]`
192. **«Вы добавили трансформер-ранкер, и резко просела латентность и пропускная способность. Что делать?»** — `middle_plus` | Дром.ру `[Senior]` — **классический «стресс-follow-up»**
193. **«Как построить систему антифрода: rule-based + ML, что первым?»** — `middle_plus` | Сбер/Т-Банк, по разбору из A1 (двухуровневая система, дисбаланс 1:10000, adversarial drift, метрика precision@low_FPR)

**Из RU-практики, без явной привязки к грейду:**
194. **«Спроектируйте корпоративную архитектуру продукта, например Instagram»** (секция system design) — `middle_plus` | Ozon, через B26 | https://habr.com/ru/articles/926214/
195. **«Спроектируйте newsfeed твиттера»** — `middle_plus` | через B57 (личный отчёт кандидата на Senior MLE) | https://zaringleb.medium.com/как-я-готовился-к-собеседованию-на-позицию-senior-ml-engineer-f2f6d8effa50
196. **Динамическое ценообразование (surge pricing) на основе предсказательных моделей спроса** — `middle_plus` | через B55, заявлено как **новинка задач 2026 года** | https://enigmai.ru/guides/system-design-prep/system-design-common-tasks/

#### B.3 Международные формулировки MLSD (для сверки канона)

Из **A14** (`alirezadir`), полный список категорий:
- **GenAI / LLM (2026):** RAG document Q&A / «chat with your docs»; LLM-powered customer-support chatbot (с guardrails и fallback на человека); agentic workflow / AI assistant (planning, tool use, memory); enterprise / semantic search с LLM-ответами и цитатами; code assistant / coding agent (RAG по репозиторию + tool use + верификация); content generation / summarization at scale (batch + safety filtering); LLM-based recommendation / personalization (LLM как ранкер или генератор фичей).
- **RecSys:** video/movie recommendation (Netflix, YouTube); friends/follower recommendation (Facebook, Twitter, LinkedIn); event recommendation (Eventbrite); game recommendation; replacement product recommendation (Instacart); rental recommendation (Airbnb); place recommendation.
- **Search / Ranking:** newsfeed ranking; ads serving system (retrieval + ranking).
- **NLP:** named entity linking; autocompletion / typeahead; sentiment analysis; language identification; chatbot; QA.
- **Other:** ride matching system; proximity service / Yelp; food delivery time approximation; harmful content / spam detection; healthcare diagnosis.

Из **A5** (RU, план из 10 задач): Recommendation System, Search System, RAG Platform, **Feature Store**, **Model Serving Platform**, **ML Training Platform**, **Experimentation Platform**, Document Knowledge Platform, Content Moderation System, Personalization Platform.
> Важно: здесь **платформенные** задачи (feature store, serving, training, experimentation) стоят наравне с продуктовыми — это отличает MLE-трек от DS-трека.

Из **A12** (RU, 10 кейсов с разбором): (1) Рекомендации YouTube/Netflix; (2) Поиск Instagram/TikTok; (3) Fraud detection для платёжной системы; (4) LLM-чатбот для поддержки; (5) News feed ranking (Facebook/LinkedIn); (6) Image classification at scale (модерация контента); (7) Real-time speech-to-text для звонков; (8) Search autocomplete; (9) Personalized notifications; (10) On-device speech recognition (mobile).

Из **B45** (Meta / Google, процитированные формулировки): «design a personalized news ranking system»; «design a click-through rate prediction model for Google Ads»; «design an evaluation framework for ads ranking at Meta»; «design a fraud detection system for Stripe»; «design a budget pacing system for advertiser campaigns».

Из **B64**: Personalized Recommendation Systems, Ranking and Retrieval, Fraud Detection, ETA Prediction, Visual Search.

Из **B56** (русское издание книги по MLSD): визуальный поиск, рекомендации видео, предсказание кликов по рекламе.

#### B.4 Что оценивают: рубрика и разница middle vs middle+

- **Ось сеньорити №1 — problem exploration.** «Problem exploration is often an axis used to grade a candidate's seniority; more junior candidates often jump straight to feature engineering or focus exclusively on technical details without business context. More senior candidates will be asked more ambiguous problems, or be expected to navigate and find optimal formulations themselves» — B41 | https://www.tryexponent.com/courses/ml-system-design/mlsd-rubric
- **Ось сеньорити №2 — trade-offs.** «每一項回答，都想清楚背後的取捨。把 trade-off 講清楚, 是能否拿到 senior 的關鍵。**Junior pursues right or wrong; Senior looks for trade-offs**» — A16 | https://raw.githubusercontent.com/LongxingTan/Machine-learning-interview/master/02_ml/97_product_sense.md
- **Оцениваемые оси (B43):** problem framing, data-centric thinking, feature engineering depth, training-serving parity, evaluation rigor, production awareness (мониторинг, дрифт).
- **Что именно ждут (B41):** умение превратить неоднозначную бизнес-задачу в ML-решение; практический опыт с ML-системами, особенно способность найти точки наибольшего рычага; глубина знания современных техник.
- **Числовая шкала (B44):** 4.0–5.0 Strong Hire (готов к senior/staff); 3.0–3.9 Hire (mid → senior); 2.0–2.9 Lean No (нужен коучинг); 1.0–1.9 No Hire.
- **RU-специфика (B21, Авито):** развёрнутый фидбек даётся **по матрице компетенций**; на секции обсуждают целеполагание и влияние на пользователей, а не только архитектуру. По B (поиск): в конце годового буткемпа проводится техническое интервью, которое «подтвердит уровень **мидл** DS-инженера по матрице компетенций Авито» — то есть MLSD-секция официально служит инструментом присвоения грейда middle.
- **RU-специфика (B27, Т-Банк):** «Finals — системное мышление, 1.5 часа, **для middle+**, с упором на бизнес-логику». То есть **полноценная MLSD/системная секция включается именно на middle+**, а не на middle.
- **RU-специфика (B55, Яндекс):** «для Junior меньше акцент на System Design и проще алгоритмические задачи; для Senior — глубокий System Design и больше поведенческих».
- **8 финальных советов (A12), фактически анти-рубрика:** не молчите (думайте вслух); начинайте с простого (baseline → улучшения, «сначала LightGBM, потом нейросеть, если нужно»); обсуждайте trade-offs; не забывайте про данные («80% реальной работы — данные, разметка, фичи; поверхностный ответ — провал»); думайте про eval (offline + online, метрики бизнеса, не только модели); затрагивайте non-ML части (caching, sharding, fault tolerance — «это показывает зрелость»); признавайте ограничения («этот подход не сработает, если…» — сильнее, чем «всё всегда работает»); используйте опыт («я делал похожее на проекте X»).

#### B.5 Follow-up вопросы, которые прилетают внутри MLSD-секции

Это отдельная категория: у MLE их задают «поверх» дизайна, чтобы проверить глубину.

197. **«Как вы построите таргет? Какая гранулярность агрегации оптимальна?»** — `middle` | Quantum One (A1)
198. **«Какие фичи вы предложите?»** — `middle` | Quantum One (A1)
199. **«Как обеспечить латентность inference менее 100 мс?»** — `middle` | ZinBrains (A1)
200. **«Как масштабировать ранкер при миллионе кандидатов?»** — `middle_plus` | Constructor (A1)
201. **«Резко просела латентность и пропускная способность после трансформер-ранкера — что делать?»** — `middle_plus` | Дром.ру (A1)
202. **«Что делать, если операция JOIN в распределённой базе работает слишком долго?»** — `middle` | Ozon (A1, раздел SQL-DATABASES)
203. **«Какие объёмы данных и время обучения моделей? Опыт с параллелизмом?»** — `middle` | Ozon (A1)
204. **«Как искать узкое место, если обучение занимает 12 часов?»** — `middle` | ZinBrains (A1)
205. **«Как работает индекс IVF в FAISS?»** — `middle` | VK/ZinBrains (A1)
206. **«Как решить проблему холодного старта?»** — `middle` | A1, раздел ML-RECSYS

---

### C. Coding-секции для MLE

#### C.1 Что именно спрашивают и в какой пропорции

**Пропорции из A13** (`justxor/MachineLearningRoadmap`, `interview-prep/05-coding.md`):
> «Coding для ML-роли — не классический LeetCode. Это смесь:
> 1. **Алгоритмы (50%):** массивы, строки, hash maps, two pointers, BFS/DFS. Уровень **easy-medium**.
> 2. **SQL (20%):** для DS/DA позиций обязательно. Window functions, CTE, optimization.
> 3. **ML с нуля (20%):** "реализуйте kNN", "напишите gradient descent", "реализуйте softmax".
> 4. **Python data manipulation (10%):** pandas/numpy, оптимизация, профилирование.
>
> **Сениорные ML-собесы:** алгоритмы менее важны, больше — design кода, чистота, тестируемость.»

**Уровень LeetCode для MLE:** easy-medium (A13). Это же подтверждается составом топ-25 из A13 (см. C.2) — там нет hard.

**RU-контекст (B24):** ~70% компаний в России используют livecoding (Яндекс, Сбер, VK, T-Bank, Avito, OZON); Python-задачи в live-coding встречаются в Ozon, Яндексе и Kaspersky, фокус — **генераторы, декораторы и data processing**.

**RU-контекст (B4):** типовая структура собеседования аналитика/DS — 3-4 раунда: SQL live, Python live, A/B-кейс с цифрами, разбор продуктовой метрики.

**Международный контекст (B50):** основные типы интервью на MLE — LeetCode-style coding, ML System Design, ML-теория и статистика (иногда внутри MLSD), behavioral.

**Планка по pandas/numpy (B51):** «fluent data manipulation, simple model implementations, and feature processing, с pandas и NumPy настолько отточенными, чтобы думать о задаче, а не о синтаксисе».

**Универсальный подход к задаче (A13), 7 шагов:** уточнить (range входов, edge cases: empty, single element, duplicates, negatives) → brute force вслух с его сложностью → оптимизация (найти узкое место) → объяснить идею вслух → закодить чисто → прогнать тесты руками на 1-2 примерах + edge cases → назвать time/space complexity.
**Антипаттерны (A13):** молчать и сразу писать; игнорировать edge cases; не упоминать сложность.

#### C.2 Алгоритмические задачи (LeetCode-уровень)

Топ-25 из **A13**, сгруппированные как в источнике:
- *Arrays & Strings:* Two Sum (hash map, O(n)); Best Time to Buy and Sell Stock (one pass); Move Zeroes (two pointers); Container With Most Water; 3Sum (sort + two pointers); Longest Substring Without Repeating Characters (sliding window); Group Anagrams (hash map с tuple keys).
- *Hash maps & Sets:* Valid Anagram (counter); Top K Frequent Elements (heap или bucket sort); Subarray Sum Equals K (prefix sum + hash map).
- *Two Pointers & Sliding Window:* Minimum Window Substring; Longest Repeating Character Replacement.
- *Trees:* Binary Tree Level Order Traversal (BFS); Maximum Depth of Binary Tree; Validate BST; Lowest Common Ancestor.
- *Graphs:* Number of Islands (DFS/BFS на grid); Course Schedule (topological sort, cycle detection); Clone Graph.
- *DP (basics):* Climbing Stairs; House Robber; Longest Increasing Subsequence; Coin Change.
- *Heap & Priority Queue:* K Closest Points to Origin; Find Median from Data Stream (two heaps).

**Реальные алгоритмические задачи с RU/HFT-собеседований (A1, раздел CODING):**

207. **«Реализуйте алгоритм flood fill для двумерного массива»** — `junior` | Самокат Тех (Kupol Tech) `[Junior]`
208. **«Напишите класс для сэмплирования элементов с заданными вероятностями (weighted random sampling). Класс принимает массив пар (элемент, вероятность), метод `sample()` возвращает элемент согласно распределению»** — `middle` | Unknown (screening) `[Middle]`
209. **«Какова сложность вашего алгоритма сэмплирования? Можно ли улучшить до O(log n)?»** — `middle` | Unknown (screening) `[Middle]` — follow-up к №208
210. **«Реализуйте сэмплирование из дискретного распределения, заданного гистограммой (может содержать float-веса). Оптимизируйте до O(log n) на запрос»** — `middle` | Silver Mont HFT `[Middle]`
211. **«Для каждого числа из массива B найдите число из массива A, дающее максимальный XOR. Реализуйте наивное решение, затем оптимизируйте»** — `middle` | Teza Technologies `[Middle]`
212. **«Напишите функцию: зная среднее 5 чисел и одно из чисел, верните среднее оставшихся 4»** — `junior` | PulsePoint `[Junior]` — разминочная задача на скрининге
213. **«Реализуйте Bloom filter. Объясните принцип работы и напишите код»** — `middle` | Constructor `[Middle]`
214. **«Как уменьшить количество коллизий (false positive) в Bloom filter?»** — `middle` | Constructor `[Middle]`
215. **«В чём отличие Bloom filter от hash map? Зачем нужен Bloom filter?»** — `middle` | Constructor `[Middle]`
216. **«Дан CSV с биржевыми сделками (timestamp, volume). Найдите временные интервалы с наибольшим объёмом торгов. Как определить оптимальный размер окна?»** — `middle` | Wunderfund `[Middle]`
217. **«Файл с биржевыми сделками не помещается в RAM. Как найти интервал максимального объёма за один проход?»** — `middle` | Wunderfund `[Middle]` — **streaming/one-pass, очень характерно для MLE-скринов**
218. **«Есть поток биржевых пакетов с временем отправки и получения. Как обнаружить аномалии в задержках?»** — `middle` | Wunderfund `[Middle]`
219. **«Как вычислить (XᵀX)⁻¹XᵀY при ограниченной RAM? Оптимизировать число disk-to-RAM трансферов»** — `middle_plus` | Headlands Technologies (HFT) `[Senior]`
220. **«Rate Limiter через декоратор: напишите `@rate_limit(max_calls=5, period=60)`, ограничивающий количество вызовов функции»** — `middle` | Kaspersky, через B24 | https://habr.com/ru/articles/995600/

#### C.3 «Реализуйте с нуля» — ML-алгоритмы и слои

**Список из A13** (8 задач, с кодом в источнике): реализовать kNN; реализовать K-Means; реализовать linear regression с gradient descent; реализовать softmax и cross-entropy; **реализовать attention**; реализовать precision/recall/F1; реализовать train/val split; реализовать sigmoid и его производную.

**Список из A15** (`LongxingTan/Machine-learning-interview`, `02_ml/99_ml_coding.md`) — то, что реально пишут на ML-coding раунде, по разделам источника:
- *Цели и оценка:* `MSE`, `CrossEntropyLoss` (две реализации), `FocalLoss` (как `nn.Module`), **`AUC`**.
- *Статистические модели:* `TreeNode` + `DecisionTree`, `KMeansCluster`.
- *DL:* `Dense` (полносвязный слой), `Conv2D`, `image2col` / `col2image`, `conv2D(image, kernel, padding, strides)`, `conv1d`, **`scaled_dot_attention(q, k, v)`**, **`MultiHeadAttention(nn.Module)`** (с двумя вариантами: наивный и «свести к одному большому матричному умножению для ускорения»).
- *NLP:* `compute_term_frequency`, `compute_inverse_document_frequency`, `calculate_feature_vector` (TF-IDF), **BPE** (`get_stats`, `merge_vocab`), `get_positional_embedding(d_model, max_seq_len)`, `top_k_sampling(logits, k=5)`.

**Формулировки из B50/B51:**
221. **«Implement binary logistic regression using only NumPy. Include a `fit` method with gradient descent and a `predict` method»** — `middle` | B51 — проверяет одновременно сигмоиду, BCE-loss и обновление весов
222. **«Implement common model architectures from scratch: Transformers (encoder, decoder, encoder–decoder), MLP, CNN, RNN (GRU, LSTM); или traditional models — logistic regression, linear regression, KNN, K-Means, decision trees»** — `middle`/`middle_plus` | B50
223. **«Вместо импорта из `torch.nn` реализуйте строительные блоки сами: embedding lookups, projection и linear layers, layer norm, batch norm, attention (causal и bidirectional), residual connections, dropout, activations»** — `middle_plus` | B50 | https://www.yuan-meng.com/posts/mle_interviews_2.0/
224. **«Реализуйте K-Means с нуля»** (scenario-based coding) — `middle` | B51 | https://www.shadecoder.com/blogs/machine-learning-coding-interview-prep-guide-2026-skills-practice-tools

**Смежные «числовые» вопросы на понимание, которые дают вместо кода (A1):**
225. **«Случайный классификатор выдаёт 1 с вероятностью 60%. Выборка: 30 единиц, 70 нулей. Чему равны precision и recall?»** — `middle` | A1, раздел ML-GENERAL
226. **«ROC-AUC = 0.9. Продублировали каждый положительный объект 7 раз, отрицательный — 4 раза. Как изменится ROC-AUC?»** — `middle_plus` | A1, раздел ML-GENERAL
227. **«Сколько параметров в полносвязном слое с N входами и K выходами (с bias)?»** — `junior` | A1

#### C.4 pandas / numpy

Из **A13** (разделы «Pandas», «NumPy», «Memory & Performance») — темы, которые спрашивают: merge с `indicator=True` (колонка `_merge` показывает источник строки); векторизация вместо циклов (в источнике явно «Плохо / Хорошо»); память и производительность.

Из **A4** (раздел `14.4 Python / pandas для анализа данных`, ~190 вопросов) — то, что реально формирует пул pandas-вопросов:
228. **«Чем `.loc[]` отличается от `.iloc[]`?»** — `junior`
229. **«В чём разница между `&` и `and` в pandas?» / «Почему при фильтрации нужны скобки вокруг условий?»** — `junior`
230. **«Чем `concat()` отличается от `merge()`?» / «Чем `merge()` отличается от `join()`?»** — `junior`
231. **«Как понять, что merge задвоил строки?» / «Как валидировать merge?» / «Что делает параметр `validate` в `merge()`?»** — `middle` — **классический отсев: почти никто не знает про `validate`**
232. **«Чем `.agg()` отличается от `.transform()`?» / «Когда использовать `transform()`, а когда `aggregate()`?»** — `middle`
233. **«Почему `apply()` часто медленнее векторизованных операций? Когда `apply()` оправдан?»** — `middle`
234. **«Чем `.map()` отличается от `.apply()`?» / «Чем `.applymap()` отличается от `.map()`?»** — `middle`
235. **«Что такое `SettingWithCopyWarning`? Почему он возникает? Как правильно его избегать?» / «Почему важно понимать view vs copy?»** — `middle` — **очень частый отсев**
236. **«Чем `resample()` отличается от `groupby()` по дате?»** — `middle`
237. **«Что делает `rolling()` / `expanding()` / `shift()` / `pct_change()`?» / «Как посчитать day-over-day или week-over-week изменение?»** — `middle`
238. **«Как уменьшить использование памяти в pandas? Когда стоит использовать `category`, downcasting, chunking?» / «Как читать большой CSV по частям?»** — `middle`
239. **«Когда pandas уже не подходит по объёму данных?» / «Чем pandas отличается от Polars?» / «Чем pandas отличается от Spark DataFrame?» / «Когда лучше перейти с pandas на SQL / на PySpark?»** — `middle`
240. **«Чем `iterrows()` отличается от `itertuples()`? Почему `iterrows()` часто не рекомендуют?»** — `middle`
241. **«Как посчитать когорты пользователей в pandas?» / «Как посчитать retention в pandas?» / «Как посчитать funnel analysis?» / «Как посчитать ARPU, LTV, conversion rate?» / «Как построить RFM-анализ?»** — `middle` — **это ровно те же задачи, что и в SQL-раунде, но на pandas**
242. **«Как избежать data leakage при подготовке данных?» / «Как разделить train/test в Python?»** — `middle`
243. **«Как бы вы почистили "грязный" CSV-файл с разными форматами дат, пропусками и дублями?»** — `middle` — **типовая live-задача**
244. **«Как проверить гипотезу, имея только pandas и scipy?»** — `middle` — **мостик между coding-секцией и A/B-секцией**
245. **«Какие тесты вы бы написали на функцию трансформации данных? Как использовать pytest для data-пайплайнов?» / «Как инструменты вроде pandera или Great Expectations помогают в анализе данных?»** — `middle_plus`

**Python-вопросы, которые реально задавали (A1, раздел LANG-PYTHON):**
246. **«Чем генераторы отличаются от коллекций в Python?»** — `middle` | NNS `[Middle]`
247. **«Почему опасно использовать мутабельный объект как значение по умолчанию аргумента функции?»** — `middle` | NNS `[Middle]`
248. **«Как генераторы связаны с асинхронным программированием в Python?»** — `middle_plus` | NNS `[Senior]`
249. **«Что такое контекстный менеджер (with statement)?» / «Что такое dunder-методы?» / «Чем set отличается от frozenset?» / «Что можно использовать в качестве ключа словаря — set или frozenset?»** — `junior`/`middle` | NNS
250. **«Что такое async/await в Python? Что произойдёт, если поместить блокирующий HTTP-вызов в async-функцию?»** — `middle` | PulsePoint `[Middle]`

#### C.5 SQL live-coding

**Формулировки из A13 (топ-10 типов задач):** N-е максимальное значение (`ROW_NUMBER`/`DENSE_RANK`); cumulative metrics (window `SUM`); retention cohort (self-join + `date_trunc`); sessionization (gap-based session detection); median (`PERCENTILE_CONT` или руками через window); funnel analysis (multiple joins + `COUNT(DISTINCT)`); MoM/YoY growth (`LAG`); top N per group (window `RANK`); pivot/unpivot (`CASE WHEN` или `PIVOT`); time-series gaps (`generate_series` + `LEFT JOIN`).
**Подводные камни оттуда же:** NULL behaviour (`COUNT(*)` vs `COUNT(column)`, `DISTINCT` с NULL); JOINs vs UNION; index awareness; умение читать `EXPLAIN ANALYZE`.

**Реальные SQL-задачи с собеседований (A1, раздел SQL-DATABASES):**

251. **«Дана таблица логов (`user_id`, `item_id`, `action_type`, `timestamp`). Для каждого пользователя найти `item_id` последнего клика»** — `junior` | Unknown (screening) `[Junior]`
252. **«Напишите SQL-запрос для поиска аномальных дней (revenue > 3x предыдущего дня) для всех `publisher_id`»** — `middle` | PulsePoint `[Middle]`
253. **«Модифицируйте запрос: аномалия определяется как 3x среднего за 2 дня до и 2 дня после (без самого дня)»** — `middle` | PulsePoint `[Middle]` — **классическая эскалация задачи прямо в раунде: от `LAG` к оконному фрейму `ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING` с исключением текущей строки**
254. **«Есть таблица событий watchdog. Найдите периоды, когда эндпоинт действительно недоступен (2+ подряд не-OK статуса)»** — `middle_plus` | PulsePoint `[Senior]` — **gaps-and-islands**
255. **«Что делать, если операция JOIN в распределённой базе работает слишком долго?»** — `middle` | Ozon `[Middle]`
256. **«For each weekly signup cohort, compute Day-7 retention (% of users from the cohort who returned 7 days after signup) given `users(id, signup_date)` and `sessions(user_id, session_date)`»** — `middle` | B52 | https://builder.ai2sql.io/blog/sql-interview-questions-faang

**Темы SQL из A4 (раздел `14.3 SQL для аналитики`)** — карта пула вопросов; конкретные формулировки там generic, поэтому в список вопросов не выношу, но тематически покрывают ровно топ-10 из A13.

#### C.6 PyTorch и debugging

257. **«Debug and fix a PyTorch Transformer training loop»** — `middle_plus` | заявлено как вопрос **OpenAI** | https://prachub.com/interview-questions/debug-and-fix-a-pytorch-transformer-training-loop
    - Постановка: causal LM на PyTorch «обучается», но loss не улучшается и иногда становится NaN. Для каждого бага нужно назвать (a) симптом, (b) корневую причину, (c) минимальный фикс.
    - Процитированные баги: нет `optimizer.zero_grad()` перед итерацией (градиенты аккумулируются); слои создаются в `forward`, а не в `__init__` (не регистрируются в `parameters()`, пересоздаются каждый проход, не учатся); один и тот же вектор позиционного кодирования на все позиции.
258. **«Какие контекстные менеджеры используются в PyTorch?»** — `middle` | A1, раздел ML-GENERAL
259. **«Зачем отключать подсчёт градиентов при инференсе?»** — `junior` | A1
260. **«Что делает `model.eval()` в PyTorch и зачем он нужен?»** — `junior` | A1
261. **«В чём разница между `tensor.view()` и `tensor.reshape()` в PyTorch?»** — `middle` | A1, Автотехника (Sber Autonomous) `[Middle]`
262. **«Как перевести модель PyTorch в режим инференса?» / «Как перевести модель PyTorch в FP16?»** — `junior` | A1, Автотехника `[Junior]`
263. **«PyTorch: если в атрибут `nn.Module` положить обычный `Tensor` (не `Parameter`), будет ли он обучаться?»** — `middle` | A1, Точка банк (R&D) `[Middle]` — **прямой родственник бага из №257**
264. **«Как называется механизм автоматического дифференцирования в PyTorch?»** — `junior` | A1, Точка банк `[Junior]`
265. **«Умеешь ли ты собрать модель, написать training loop и корректно загрузить данные? Умеешь ли дебажить, находить bottleneck'и и ускорять обучение?»** (обобщённая формулировка того, что оценивает PyTorch-секция) — `middle` | B49

---

## Что интервьюеры ловят этими вопросами

### A/B и эксперименты

1. **Отличаешь ли ты «нет эффекта» от «не обнаружили эффект».** Вопросы №11, №43, №104 (и разбор «серых метрик» Авито, B10). Слабый кандидат говорит «эффекта нет»; сильный — «если эффект есть, он внутри [−x%, +y%], а MDE у нас был z%, поэтому мы не могли бы его увидеть».
2. **Понимаешь ли ты, что дизайн решается ДО запуска, а не после.** Вопросы №12–21. Ловят на том, что человек умеет посчитать p-value постфактум, но не умеет посчитать n и срок заранее.
3. **Знаешь ли ты, что подглядывание — это не «нетерпение», а инфляция FPR.** Вопросы №34–42. Проверяют, знает ли кандидат, что *единственный* корректный ответ — либо фиксировать горизонт заранее, либо использовать sequential-процедуру (Покок / О'Брайен-Флеминг / always-valid), а не «просто подождать ещё немножко».
4. **Умеешь ли ты работать с ratio-метрикой.** Вопросы №63–73. Это главный водораздел middle vs middle+ по A/B (прямо заявлено в B28: «senior candidates get pushed on ratio metrics, the delta method, and variance reduction»). Ловят на том, что кандидат берёт t-тест по пользователям для CTR, посчитанного как сумма кликов / сумма показов.
5. **Понимаешь ли ты, откуда берётся дисперсия и как её резать.** Вопросы №50–62. Проверяют, что CUPED — не магия, а `Var(Y)·(1−ρ²)`, и что без коррелированной ковариаты он ничего не даёт.
6. **Видишь ли ты нарушения SUTVA.** Вопросы №74–83. Проверка «продуктовой зрелости»: понимает ли кандидат, что на маркетплейсе/в соцсети/в такси юнит эксперимента — не всегда пользователь.
7. **Не путаешь ли ты «сегмент выиграл» с «сегментом, который мы нашли постфактум».** Вопросы №48, №49, №90–94. Симпсон + p-hacking + HTE — один узел.
8. **Умеешь ли ты принимать решение, а не только считать.** Вопросы №95–108. Guardrail-метрики, конфликт primary vs guardrail, конфликт новых vs старых пользователей.
9. **Понимаешь ли ты, чем ML-A/B отличается от продуктового A/B.** Вопросы №123–137. Для MLE это критично: ground truth с лагом (fraud), нельзя показывать рискованную версию (regulated), shadow vs canary vs A/B, разрыв офлайн/онлайн метрик.
10. **Есть ли у тебя реальный опыт или только теория.** Вопрос №153 — прямая формулировка этого фильтра. Индикаторы реального опыта: упоминание SRM, A/A, feature flags, стратификации сплита, длительности, репозитория метрик.

### ML System Design

11. **Задаёшь ли ты вопросы до того, как начать проектировать.** Первый шаг во всех четырёх схемах (A5, A12, A14, A18) — clarify/requirements. B23 прямо: кандидат сам формирует список требований. B19: типичный провал — прыгать между моделью, данными и деплоем, забыв про бизнес.
12. **Умеешь ли ты переводить бизнес-задачу в ML-задачу (и понимать, нужен ли вообще ML).** A14, шаг 1 содержит явный пункт «Do we need ML to solve this problem?».
13. **Начинаешь ли ты с baseline.** Формулировка Constructor (№188) прямо содержит «сначала простое решение, затем сложнее». A12: «сначала LightGBM, потом нейросеть, если нужно».
14. **Проговариваешь ли ты trade-offs.** Главный маркер сеньорити (A16, B41). Форма ответа из A5: `requirement → design decision → guarantee → cost → alternative`.
15. **Есть ли у тебя training-serving parity и понимание данных.** B43; A12: «80% реальной работы — данные, разметка, фичи; поверхностный ответ — провал».
16. **Дойдёшь ли ты до eval и мониторинга, или остановишься на архитектуре.** Все схемы содержат offline+online eval и monitoring/retrain. Практика показывает, что кандидаты выдыхаются на шаге «модель».
17. **Выдерживаешь ли ты стресс-follow-up.** №192 (просела латентность), №189 (миллион кандидатов), №174 (<100 мс), №173 (12 часов обучения). Это проверка, что ты работал в проде, а не только в ноутбуке.
18. **Признаёшь ли ты ограничения.** A12, совет №7: «"Этот подход не сработает, если…" — сильнее, чем "всё всегда работает"».

### Coding

19. **Синтаксическая беглость pandas/numpy как прокси «сколько ты реально писал кода».** B51: «pandas и NumPy настолько отточены, чтобы думать о задаче, а не о синтаксисе». Вопросы №228–245.
20. **Понимаешь ли ты, что происходит внутри библиотеки.** «Реализуйте attention / AUC / K-Means с нуля» (C.3). Проверка, что ты не только вызываешь `sklearn`.
21. **Умеешь ли ты думать вслух.** A13, антипаттерн №1: «Молчать и сразу писать → интервьюер не понимает, провал».
22. **Умеешь ли ты работать с потоком/памятью.** №217 (файл не помещается в RAM, один проход), №219 ((XᵀX)⁻¹XᵀY при ограниченной RAM). Для MLE это ключевое отличие от классического LeetCode.
23. **SQL: понимаешь ли ты оконные функции, а не только GROUP BY.** №251–256. Gaps-and-islands (№254) — верхняя планка middle+.
24. **PyTorch: понимаешь ли ты жизненный цикл градиента и регистрацию параметров.** №257, №263 — по сути один и тот же вопрос с разных сторон.
25. **Умеешь ли ты оценивать сложность и оптимизировать по требованию.** №209, №210, №211 — во всех трёх интервьюер явно просит «а теперь до O(log n)» / «а теперь оптимизируйте».

---

## Пробелы, которые чаще всего валят кандидатов

### A/B

1. **Ratio-метрики.** Считают t-тест по пользовательским CTR вместо global CTR + дельта-метода/линеаризации/бутстрапа. Не знают про bias наивного усреднения (A3 даёт готовый численный контрпример: 0.15 vs 0.27). Это **самая частая точка провала на middle+**, прямо зафиксировано в B28.
2. **MDE и sample size.** Знают формулу, но не умеют перевести её в «сколько дней тест будет идти при нашем трафике» и не различают абсолютный vs относительный MDE (A6, раздел 3).
3. **Подглядывание.** Считают проблемой «нетерпение менеджера», а не инфляцию FPR; не знают ни одной корректирующей процедуры (Покок, О'Брайен-Флеминг, always-valid p-values).
4. **SRM.** Вообще не проверяют размеры групп. Не знают про chi-squared goodness-of-fit и про то, что SRM встречается в 6–10% тестов (B33).
5. **Множественные сравнения.** «Прокрасилось 5 из 100 метрик — ура!». Вопрос №43 (Constructor) отсеивает именно это.
6. **CUPED без понимания механики.** Называют аббревиатуру, но не могут написать формулу и объяснить, почему эффект зависит от ρ² и почему ковариата должна быть предэкспериментальной и не зависящей от эксперимента.
7. **SUTVA / сетевые эффекты.** Не видят, что в маркетплейсе/такси/соцсети юзер-рандомизация даёт смещение; не знают switchback как инструмент; не могут сформулировать, что делать (сменить единицу рандомизации).
8. **Симпсон.** Не умеют объяснить *механизм* (неравные сплиты + конфаундер), путают с «просто разными сегментами».
9. **Novelty vs primacy.** Знают слово «novelty», но не умеют предложить детект (динамика эффекта по неделям, new vs returning).
10. **Guardrail-метрики.** Называют только primary. На вопрос «primary выросла, guardrail просела» отвечают «выкатываем».
11. **Разрыв офлайн/онлайн.** Для MLE это фатально: не могут объяснить, почему +5% offline precision не даёт онлайн-эффекта (вопрос №120, №132, №137).
12. **A/A и валидация критерия.** Не знают, что критерий надо валидировать симуляциями (FPR на A/A, мощность на синтетическом лифте) — это RU-канон (Авито, ВК, Карпов), и его отсутствие сразу видно.
13. **Ловушка «выкинем выбросы».** Выкидывают выбросы внутри эксперимента, ломая несмещённость. Правильный ответ (B10): фильтровать по предэкспериментальному периоду.

### ML System Design

14. **Не задают уточняющих вопросов** — сразу проектируют. Это провал шага 1 во всех схемах.
15. **Прыгают в модель, минуя формализацию задачи и метрики.** ODS (B19) описывает это как главную ошибку.
16. **Нет baseline.** Начинают с трансформера. Constructor и A12 прямо ждут обратного.
17. **Нет цифр масштаба.** Не оценивают QPS, объём данных, latency budget — а без этого нельзя обосновать ни каскад, ни ANN, ни кэш.
18. **Заканчивают на архитектуре модели.** Не доходят до serving, мониторинга, дрифта, ретрейна, деградации, rollback.
19. **Список технологий вместо обоснования.** A5 прямо называет это слабым ответом: «необоснованный список Kafka, Kubernetes и нескольких БД».
20. **Не проговаривают trade-offs** — то есть остаются на уровне junior по формулировке A16.
21. **Не умеют считать A/B внутри дизайна.** MLSD-секция почти всегда упирается в «как проверим, что стало лучше» — и там нужен весь блок A.
22. **Не знают платформенных задач** (feature store, model registry, experimentation platform, training platform) — а для MLE это половина списка A5.

### Coding

23. **Молчание в лайвкодинге.**
24. **Игнорирование edge cases и отказ назвать сложность.**
25. **pandas: `SettingWithCopyWarning`, view vs copy, `validate` в `merge`, `agg` vs `transform`** — четыре стабильных провала.
26. **Циклы вместо векторизации; `iterrows()`.**
27. **Не умеют написать метрику руками** (AUC, precision/recall) — притом что это спрашивают напрямую.
28. **Не умеют реализовать attention/softmax без фреймворка.**
29. **SQL: оконные функции.** Особенно фрейм `ROWS BETWEEN … PRECEDING AND … FOLLOWING` и gaps-and-islands.
30. **PyTorch: `optimizer.zero_grad()`, регистрация параметров, `model.eval()`, `no_grad`** — базовые вещи, на которых валятся даже те, кто «обучал модели».
31. **Не думают про память и один проход** — а именно это отличает MLE-задачи от учебного LeetCode.

---

## Рекомендации для структуры глав хендбука по этой теме

### Глава «A/B-тестирование и эксперименты» (раздел 10)

Предлагаемая последовательность — от «сдать junior-скрин» к «сдать middle+ секцию»:

1. **10.1 Зачем MLE вообще A/B.** Место A/B в жизненном цикле ML-модели (по A10): офлайн-метрика → A/B → раскатка → мониторинг. Сразу дать разницу: «A/B-тест vs просто смена модели». Ответ на вопрос-скрин №124.
2. **10.2 Статистический минимум.** H₀/H₁, ошибки I/II рода, α, мощность, p-value (что он НЕ значит), доверительный интервал, практическая vs статистическая значимость. Закрывает вопросы №1–11. Уровень: junior.
3. **10.3 Дизайн: MDE, размер выборки, длительность.** Формулы для долей и для средних, абсолютный vs относительный MDE, перевод n → дни, дизайн-эффект при кластеризации, буфер на сезонность и полный цикл пользователя. Обязательно — **готовый Python-сниппет на `statsmodels`** (шаблон из A6). Закрывает №12–21.
4. **10.4 Сплит-система и валидация.** Единица рандомизации (user/session/device/account), A/A, SRM и chi-squared, равномерность p-value на A/A, sanity checks. Закрывает №22–33. Дать чек-лист «что проверить до анализа».
5. **10.5 Подглядывание и sequential.** Демонстрация инфляции FPR на симуляции, group-sequential (Покок, О'Брайен-Флеминг), always-valid p-values, мониторинг MDE вместо мониторинга p-value. Закрывает №34–42.
6. **10.6 Множественные сравнения.** Бонферрони, Холм, FDR/BH; три источника множественности (метрики, сегменты, тритменты); почему «5 из 100» — это шум. Закрывает №43–49.
7. **10.7 Чувствительность: как ускорить тест.** Стратификация и пост-стратификация (с разложением дисперсии на меж- и внутригрупповую), CUPED (формула + алгоритм + ограничения + CUPAC), парная стратификация, работа с выбросами (что можно и чего нельзя), трансформации и ловушка направленности. Закрывает №50–62. **Это ядро middle+.**
8. **10.8 Ratio-метрики.** Наивный vs global CTR с численным контрпримером; дельта-метод (вывод через Тейлора); линеаризация; бутстрап и пуассоновский бутстрап; бакетизация; связь CUPED ↔ дельта-метод. Закрывает №63–73. **Второе ядро middle+.**
9. **10.9 Когда предпосылки ломаются.** SUTVA, spillover, interference, network effects; switchback (с RU-кейсами Ситимобил / Delivery Club / Авито и фактом «×3»); clustered A/B; carryover; contamination. Закрывает №74–83.
10. **10.10 Эффекты времени.** Novelty/primacy (детект + лечение), сезонность, внешние шоки, что делать при outage/акции. Закрывает №84–89.
11. **10.11 Сегменты и парадокс Симпсона.** Механика Симпсона, HTE, почему пост-хок сегменты опасны, как искать сегменты честно. Закрывает №90–94.
12. **10.12 Метрики и принятие решения.** Иерархия primary / secondary / guardrail; метрики под конкретные ML-задачи (recsys, search, ads, fraud); конфликтные ситуации; как докладывать результат. Закрывает №95–108.
13. **10.13 A/B для ML-моделей (специализация MLE).** Feature flags, champion/challenger, canary, shadow, dark launch, rollback; ground truth с лагом; regulated domain; разрыв офлайн/онлайн и как его закрывать; A/B + uplift. Закрывает №123–137. **Это то, чего нет в аналитических учебниках и что отличает MLE-хендбук.**
14. **10.14 Альтернативы A/B.** Бандиты (и когда они НЕ подходят), global holdout (≤5%), DiD, synthetic control, pre-post и его ограничения, off-policy evaluation, uplift. Закрывает №138–144.
15. **10.15 Платформа экспериментов и процесс.** Репозиторий метрик (с примером YAML-спеки метрики из A3), логирование, метаданные, коллизии экспериментов, governance, воспроизводимость. Закрывает №145–156.
16. **10.16 Симуляции как рабочий инструмент.** Монте-Карло валидация критерия: FPR на A/A, TPR на сетке лифтов, тонкости для дискретных/ratio-метрик. Отдельная короткая глава с кодом — это то, что отличает «читал» от «делал».
17. **10.17 Тренажёр: 30 вопросов с эталонными ответами** + 5 разборов «кейс с цифрами» (по формату B4: «A/B-кейс с цифрами» — отдельный раунд).

### Глава «ML System Design» (раздел 11)

1. **11.1 Что это за секция и кто её проходит.** Форматы в RU (Т-Банк — отдельная именованная секция; Авито — фидбек по матрице компетенций; Ozon — отдельная секция system design; Яндекс — глубина растёт с грейдом). Явно: **на middle MLSD чаще лёгкий, полноценная секция — на middle+** (B27).
2. **11.2 Единый каркас ответа.** Дать **одну** схему, а не четыре. Рекомендую 8 шагов с таймингом (A12) как рабочую, и 14-шаговую (A5) как «расширенный чек-лист для самопроверки». Обязательно — принцип `requirement → design decision → guarantee → cost → alternative`.
3. **11.3 Шаг 1: уточняющие вопросы.** Готовый список из 15–20 вопросов, которые кандидат задаёт интервьюеру (бизнес-цель, кто пользователь, где показываем, сколько объектов/юзеров/QPS, latency budget, есть ли разметка, ограничения по регуляторике, что уже есть в проде).
4. **11.4 Шаг 2: метрики.** Бизнес → продуктовые → ML-офлайн → ML-онлайн; guardrails; trade-offs между ними; как связать offline-прокси с online-целью.
5. **11.5 Шаг 3: данные и разметка.** Источники, feedback loop, position bias, delayed labels, дисбаланс, синтетика, приватность.
6. **11.6 Шаг 4: модель.** Baseline → каскад → продвинутое. Явно прописать «правило baseline».
7. **11.7 Шаг 5: инференс и инфраструктура.** Batch vs online, feature store и train/serve consistency, кэш, ANN, деградация и fallback, latency budget по компонентам.
8. **11.8 Шаг 6: eval и раскатка.** Ссылка на главу 10 + специфика: shadow, canary, interleaving, holdout.
9. **11.9 Шаг 7: мониторинг, дрифт, ретрейн.**
10. **11.10 Рубрика: что оценивают на middle vs middle+.** Таблица с осями (problem exploration, trade-offs, data-centric thinking, production awareness, scale reasoning) и явным описанием, как выглядит ответ уровня middle и уровня middle+ по каждой оси. Опереться на B41, B44, A16.
11. **11.11 Каталог кейсов.** Минимум 12 полных разборов, приоритет по частоте в RU-найме:
    (1) лента рекомендаций / бесконечная лента (VK, Дром.ру, Самокат);
    (2) ранжирование в e-commerce поиске (Constructor, Ozon);
    (3) антифрод транзакций (Сбер, Т-Банк);
    (4) CTR-предсказание для рекламы;
    (5) churn / uplift-кампания (RU-банки, ритейл);
    (6) LLM-ассистент / RAG над корпоративной базой (ВТБ, PulsePoint, Waibee);
    (7) модерация контента;
    (8) прогноз спроса / ETA / задержки (Quantum One, логистика);
    (9) динамическое ценообразование / surge (новинка 2026, B55);
    (10) матчинг / рекомендации в маркетплейсе;
    (11) поиск похожих товаров / визуальный поиск;
    (12) платформенный кейс: experimentation platform или feature store.
    Каждый разбор — по единому шаблону из 11.2, с явными «follow-up вопросами интервьюера» в конце.
12. **11.12 Стресс-follow-up'ы.** Отдельный мини-раздел: «просела латентность», «миллион кандидатов», «обучение 12 часов», «нужно <100 мс», «A/B не прокрасился». По каждому — структура ответа из 4–5 уровней решения (как в разборе Дром.ру из A1).
13. **11.13 ML System Design Doc.** Кратко: шаблон Reliable ML, чем документ отличается от секции интервью, и почему умение писать документ помогает на секции.

### Глава «Coding для MLE» (раздел 12)

1. **12.1 Что реально спрашивают.** Пропорции 50/20/20/10 (A13), уровень LeetCode easy-medium, отличия от бэкенд-собеса, RU-статистика по livecoding (~70% компаний). Уровневая карта: junior — базовый Python + easy-задачи; middle — medium + SQL + pandas + ML с нуля; middle+ — качество кода, тестируемость, память/поток.
2. **12.2 Протокол решения задачи.** 7 шагов из A13 + антипаттерны. Дать как «мышечную память».
3. **12.3 Алгоритмический минимум.** 25 задач по паттернам (A13) + отдельный блок RU/HFT-задач (№207–219): weighted sampling с оптимизацией до O(log n), Bloom filter, one-pass над файлом больше RAM, max XOR, скользящее окно по объёму торгов, flood fill.
4. **12.4 Python для MLE.** Генераторы, декораторы (с задачей `@rate_limit`), контекстные менеджеры, мутабельные дефолты, async/await и блокирующий вызов, dunder-методы. Закрывает №246–250 и покрывает RU-фокус «генераторы, декораторы, data processing» (B24).
5. **12.5 pandas/numpy: боевой минимум.** Разбить на: индексация и фильтрация; merge и его валидация; groupby/agg/transform; окна и время (`rolling`, `resample`, `shift`, `pct_change`); память и производительность; view vs copy и `SettingWithCopyWarning`; векторизация. Отдельный подраздел — **продуктовые расчёты на pandas** (когорты, retention, воронка, ARPU/LTV, RFM), потому что их спрашивают и в coding-, и в аналитическом раунде.
6. **12.6 ML с нуля.** Обязательный набор с кодом и тестами: kNN, K-Means, linear/logistic regression с GD, sigmoid + производная, softmax + cross-entropy, focal loss, precision/recall/F1, **AUC**, train/val split, decision tree (split criterion), **scaled dot-product attention + MultiHeadAttention**, positional encoding, top-k sampling, TF-IDF, BPE. Каждый — с «что проверяет интервьюер» и типовыми ошибками.
7. **12.7 SQL live-coding.** Топ-10 паттернов (A13) с решениями; отдельно — 4 реальные задачи из A1 (последний клик; аномальные дни 3x; переход к оконному фрейму ±2 дня; gaps-and-islands для watchdog) и retention-cohort из B52. Подводные камни NULL/`DISTINCT`/`COUNT`.
8. **12.8 PyTorch-секция и дебаг.** Жизненный цикл градиента; `zero_grad`, `no_grad`, `model.eval()`, `Parameter` vs `Tensor`, `view` vs `reshape`, fp16. **Отдельный практикум «найди 5 багов в training loop»** по мотивам №257 — это лучший формат для главы и он же реально встречается на интервью.
9. **12.9 Задачи «на память и поток».** One-pass алгоритмы, чанкинг, генераторы, оценка памяти. Отдельная глава, потому что это специфика MLE и её нет в LeetCode-гайдах.
10. **12.10 Чек-лист готовности к coding-этапу** (по образцу A13) + 4-недельный план.

### Сквозные рекомендации

- **Перелинковка обязательна.** Блок 11.8 (eval и раскатка) ссылается на всю главу 10; кейс «антифрод» в 11.11 ссылается на 10.13 (ground truth с лагом); pandas-когорты в 12.5 ссылаются на 10.12 (метрики).
- **Каждый вопрос из этого дампа должен где-то «приземлиться».** Полезно завести в хендбуке таблицу соответствия «вопрос → глава», чтобы не потерять покрытие.
- **Явная маркировка грейда у каждого вопроса в тренажёрах** (`junior` / `middle` / `middle_plus`) — читатель должен понимать, что ему НЕ нужно учить прямо сейчас.
- **RU-специфика — конкурентное преимущество хендбука.** Дельта-метод, линеаризация, бакетизация, пуассоновский бутстрап, парная стратификация, валидация критерия симуляциями — это канон RU-школы (Авито, ВК, X5, Karpov), которого почти нет в англоязычных гайдах. То же — switchback с российскими кейсами.
- **Не пересказывать теорию без кода.** Все три темы проверяются практикой: A/B — симуляциями и расчётом n; MLSD — устным walkthrough на 35–45 минут; coding — кодом. В каждой главе должен быть исполняемый блок.

---

*Конец research dump.*
