# company-handbooks — прочёс программ

Область: инженерные хендбуки, плейбуки и систематизированные руководства компаний по ML в проде
(Google, Microsoft/ExP, Uber, Netflix, Spotify, Airbnb, Pinterest, LinkedIn, Meta, Amazon/AWS,
Booking.com, DoorDash, Etsy, Shopify).
Дата прочёса: 2026-07-27. Сверка с манифестом `/home/user/ml-handbook/.handbook/STRUCTURE.md` (117 глав).

Важное замечание о доступности: большая часть первоисточников в этой области отдаёт 403
(`developers.google.com`, `research.google.com`, `static.googleusercontent.com`, `services.google.com`,
`exp-platform.com`, `uber.com/blog`, `netflixtechblog.com`, `medium.com`, `pair.withgoogle.com`,
`docs.aws.amazon.com`, `martinfowler.com`, `arxiv.org`, `ar5iv`, `blog.acolyer.org`, `zenml.io`,
`evidentlyai.com`, `truefoundry.com`). Рабочие обходы, которые сработали: **raw.githubusercontent.com**,
**github.com/issues**, **microsoft.com/en-us/research**. Всё, что помечено [ТОЛЬКО ОПИСАНИЕ], получено
из поисковой выдачи с цитатами, но полный текст я не открывал — это честно отражено в пометках.

---

## Что реально открыл (со ссылками)

Полностью открытые документы (WebFetch вернул содержимое):

| # | Источник | Ссылка | Статус |
|---|---|---|---|
| 1 | Google, Rules of Machine Learning (M. Zinkevich) — GitHub-зеркало | https://raw.githubusercontent.com/thundergolfer/google-rules-of-machine-learning/master/README.md | [ОТКРЫЛ] |
| 2 | Microsoft ExP — Patterns of Trustworthy Experimentation: **Pre-Experiment Stage** | https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/ | [ОТКРЫЛ] |
| 3 | Microsoft ExP — Patterns of Trustworthy Experimentation: **During-Experiment Stage** | https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/ | [ОТКРЫЛ] |
| 4 | Microsoft ExP — Patterns of Trustworthy Experimentation: **Post-Experiment Stage** | https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/ | [ОТКРЫЛ] |
| 5 | Microsoft/KDD-2017 «A Dirty Dozen: 12 Metric Interpretation Pitfalls» — конспект со списком всех 12 | https://github.com/shyaginuma/papers/issues/6 | [ОТКРЫЛ] |
| 6 | Google Research — **Deep Learning Tuning Playbook** | https://raw.githubusercontent.com/google-research/tuning_playbook/main/README.md | [ОТКРЫЛ] |
| 7 | Eugene Yan, **applied-ml** — индекс инженерных публикаций компаний | https://raw.githubusercontent.com/eugeneyan/applied-ml/main/README.md | [ОТКРЫЛ] |
| 8 | DavisTrey, **ExperimentationResources** — каталог материалов по A/B-платформам компаний | https://raw.githubusercontent.com/DavisTrey/ExperimentationResources/master/README.md | [ОТКРЫЛ] |

Открыть не удалось (403), содержание получено только из поисковых сниппетов — см. пометки в разделе «Программы».

---

## Программы (по каждому источнику — полный список тем)

### 1. Google — Rules of Machine Learning: Best Practices for ML Engineering [ОТКРЫЛ]
https://raw.githubusercontent.com/thundergolfer/google-rules-of-machine-learning/master/README.md
(оригинал `developers.google.com/machine-learning/guides/rules-of-ml` и PDF `martin.zinkevich.org` — [НЕ ДОСТУПЕН], 403/DNS)

Ценность: канонический инженерный чек-лист «как не угробить ML-продукт». Грейд: **middle → middle+**,
на собеседовании по ML System Design цитируется постоянно. Полная программа — 43 правила в 8 блоках:

**Before Machine Learning**
1. Don't be afraid to launch a product without machine learning
2. First, design and implement metrics
3. Choose machine learning over complex heuristic

**ML Phase I: Your First Pipeline**
4. Keep the first model simple and get the infrastructure right
5. Test the infrastructure independently from the machine learning
6. Be careful about dropped data when copying pipelines
7. Turn heuristics into features, or handle them externally

**Monitoring**
8. Know the freshness requirements of your system
9. Detect problems before exporting models
10. Watch for silent failures
11. Give feature columns owners and documentation

**Your First Objective**
12. Don't overthink which objective you choose to directly optimize
13. Choose a simple, observable and attributable metric for your first objective
14. Starting with an interpretable model makes debugging easier
15. Separate Spam Filtering and Quality Ranking in a Policy Layer

**ML Phase II: Feature Engineering**
16. Plan to launch and iterate
17. Start with directly observed and reported features as opposed to learned features
18. Explore with features of content that generalize across contexts
19. Use very specific features when you can
20. Combine and modify existing features to create new features in human-understandable ways
21. The number of feature weights you can learn in a linear model is roughly proportional to the amount of data you have
22. Clean up features you are no longer using

**Human Analysis of the System**
23. You are not a typical end user
24. Measure the delta between models
25. When choosing models, utilitarian performance trumps predictive power
26. Look for patterns in the measured errors, and create new features
27. Try to quantify observed undesirable behavior
28. Be aware that identical short-term behavior does not imply identical long-term behavior

**Training-Serving Skew**
29. The best way to make sure that you train like you serve is to save the set of features used at serving time
30. Importance weight sampled data, don't arbitrarily drop it
31. Beware that if you join data from a table at training and serving time, the data in the table may change
32. Re-use code between your training pipeline and your serving pipeline whenever possible
33. If you produce a model based on the data until January 5th, test the model on the data from January 6th and after
34. In binary classification for filtering, make small short-term sacrifices in performance for very clean data
35. Beware of the inherent skew in ranking problems
36. Avoid feedback loops with positional features
37. Measure training/serving skew

**ML Phase III: Slow Growth, Optimization Refinement, and Complex Models**
38. Don't waste time on new features if unaligned objectives have become the issue
39. Launch decisions are a proxy for long-term product goals
40. Keep ensembles simple
41. When performance plateaus, look for qualitatively new sources of information to add
42. Don't expect diversity, personalization, or relevance to be as correlated with popularity as you think
43. Your friends tend to be the same across different products. Your interests tend not to be

Плюс разделы «Related Work» и «Acknowledgements & Appendix».

---

### 2. Google — The ML Test Score: A Rubric for ML Production Readiness [ТОЛЬКО ОПИСАНИЕ]
https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf — 403.
Восстановлено из поисковых сниппетов; блоки Model и Infra получены полностью, блок Data — частично,
блок Monitor — фрагментарно.

Ценность: рубрика production-readiness, 28 тестов в 4 группах + система баллов.
Грейд: **middle+ / senior**, прямо ложится в вопрос «как вы понимаете, что модель готова к проду».

**Tests for Features and Data** (получено частично):
- Feature expectations are captured in a schema
- All features are beneficial
- No feature's cost is too much
- Features adhere to meta-level requirements (политики/регуляторика на использование признаков)
- The data pipeline has appropriate privacy controls
- New features can be added quickly
- All input feature code is tested

**Tests for Model Development** (полный список):
- Model 1: Model specs are reviewed and submitted (код-ревью и версионирование спецификации модели)
- Model 2: Offline and online metrics correlate
- Model 3: All hyperparameters have been tuned
- Model 4: The impact of model staleness is known
- Model 5: A simpler model is not better
- Model 6: Model quality is sufficient on important data slices
- Model 7: The model is tested for considerations of inclusion (справедливость/недискриминация)

**Tests for ML Infrastructure** (полный список):
- Infra 1: Training is reproducible
- Infra 2: Model specs are unit tested
- Infra 3: The ML pipeline is integration tested
- Infra 4: Model quality is validated before serving
- Infra 5: The model is debuggable
- Infra 6: Models are canaried before serving
- Infra 7: Serving models can be rolled back

**Monitoring Tests** (получено фрагментарно):
- Monitor 3: Training and serving features compute the same values
- Monitor 7: The model has not experienced a regression in prediction quality on served data
- (остальные Monitor 1,2,4,5,6 восстановить не удалось — см. «Чего найти не удалось»)

---

### 3. Google — Practitioners Guide to MLOps (whitepaper, 2021) + MLOps levels 0/1/2 [ТОЛЬКО ОПИСАНИЕ]
`services.google.com/.../practitioners_guide_to_mlops_whitepaper.pdf` — 403;
`cloud.google.com/architecture/mlops-continuous-delivery-...` — 301 → `docs.cloud.google.com`, тоже 403;
readkong-зеркало — 403.

Ценность: словарь MLOps-возможностей, который используется как каркас ответа про зрелость платформы.
Грейд: **middle+**.

Процессы жизненного цикла MLOps: ML development → training operationalization → continuous training →
model deployment → prediction serving → continuous monitoring → data and model management.

Core capabilities (список получен из сниппетов, названия подтверждены):
experimentation; data processing; model training; model evaluation; model serving;
online experimentation; model monitoring; ML pipelines; model registry;
dataset & feature repository; ML metadata & artifact tracking.

Уровни зрелости: **MLOps level 0** (ручной процесс), **level 1** (автоматизация ML-пайплайна,
continuous training, триггеры переобучения, feature store, metadata management),
**level 2** (CI/CD для пайплайнов).

---

### 4. Google PAIR — People + AI Guidebook [ТОЛЬКО ОПИСАНИЕ]
https://pair.withgoogle.com/guidebook/chapters — 403; PDF «All Chapters» — 403.

Ценность: единственный систематизированный свод по продуктовому/человеческому слою ML-систем.
Грейд: **middle+ (продуктовая зрелость на System Design)**. Программа — 6 глав, к каждой воркшит:

1. **User Needs + Defining Success** — понять потребность, определить успех, решить, нужен ли вообще ML
2. **Data Collection + Evaluation** — какие данные нужны, откуда, как настроить на устойчивость
3. **Mental Models** — как вводить пользователя в систему и калибровать его ожидания от вероятностной модели
4. **Explainability + Trust** — как объяснять решения модели пользователю и строить доверие
5. **Feedback + Control** — дизайн механизмов обратной связи и пользовательского контроля
6. **Errors + Graceful Failure** — выявление, диагностика и коммуникация ошибок, деградация без обрыва UX

---

### 5. Google Research — Deep Learning Tuning Playbook [ОТКРЫЛ]
https://raw.githubusercontent.com/google-research/tuning_playbook/main/README.md

Ценность: методология настройки DL, а не список трюков. Грейд: **middle → middle+**.
Полная программа:

- Who is this document for? / Why a tuning playbook?
- **Guide for starting a new project**: choosing the model architecture; choosing the optimizer;
  choosing the batch size (determining feasible batch sizes and estimating training throughput;
  batch size to minimize training time; batch size to minimize resource consumption;
  changing the batch size requires re-tuning most hyperparameters; how batch norm interacts with batch size);
  choosing the initial configuration
- **A scientific approach to improving model performance**: the incremental tuning strategy;
  exploration vs exploitation; choosing the goal for the next round of experiments;
  designing the next round of experiments (identifying **scientific, nuisance, and fixed hyperparameters**;
  creating a set of studies; balance between informative and affordable experiments);
  extracting insight from experimental results (identifying bad search space boundaries;
  not sampling enough points; examining training curves; **isolation plots**; automating useful plots);
  determining whether to adopt a pipeline change or hyperparameter configuration; after exploration concludes
- **Determining the number of steps for each training run**: not compute-bound vs compute-bound;
  алгоритм выбора `max_train_steps` через LR-sweep; Round 1 / Round 2
- **Additional guidance for the training pipeline**: optimizing the input pipeline; evaluating model
  performance (evaluation settings; periodic evaluations; choosing a sample for periodic evaluation);
  saving checkpoints and retrospectively selecting the best checkpoint; setting up experiment tracking;
  batch normalization implementation details; considerations for multi-host pipelines
- **FAQs**: best LR decay schedule family; default decay; why papers have complicated schedules;
  how to tune Adam's hyperparameters; **why quasi-random search instead of Bayesian optimization
  during exploration**; where to find an implementation of quasi-random search

---

### 6. Microsoft ExP — Patterns of Trustworthy Experimentation (3 части) [ОТКРЫЛ]
Полностью открыты все три статьи (ссылки в таблице выше). Это фактически чек-лист A/B-платформы.
Грейд: **middle+ / senior** — прямые вопросы на секции про эксперименты.

**Pre-Experiment Stage**
- Forming a Hypothesis and Selecting Users
  - Formulate your Hypothesis and Success Metrics — гипотеза должна быть опровержима выбранным набором
    метрик; набор метрик: **user satisfaction, guardrail, feature/engagement, data quality**
  - Choose the Appropriate Unit of Randomization — стабильность идентификатора (cookie нестабилен →
    только короткие тесты); сетевые эффекты → кластерная рандомизация; корпоративные ограничения →
    рандомизация на уровне организации
  - Check and Account for Pre-Experiment Bias — **Retrospective-AA Analysis**; **Seedfinder**
    (перебор сидов рандомизации до старта); **Variance Reduction** на предпериодных данных
- Pre-Experiment Engineering Design Plan
  - Set Up **Counterfactual Logging** — логировать, что показал бы контроль, чтобы сравнивать
    «яблоки с яблоками» и убрать шум незатронутых пользователей
  - Have **Custom Control and Standard Control** — параллельный «стандартный» контроль ловит
    инфраструктурные ошибки
  - Review Engineering Design Choices to Avoid Bias — утечка эффекта через общие компоненты
- Pre-Validation by Progressing Through Populations
  - Gradual Rollout Across Different User Populations (dogfood → beta → прод)
  - Gradual Rollout within a User Population (1% → 5% → 10%)

**During-Experiment Stage**
- Measure Holistically and Frequently
  - Capture Unexpected Effects Early with a Complete Metric Set — таксономия метрик:
    **Data Quality Metrics, OEC Metrics, Local Feature and Diagnostic Metrics, Guardrail Metrics**
  - Measure Early and Often
- Monitor Metrics to Intervene when Needed
  - Set Up Alerts to Detect Unintended Degradations (в т.ч. алерт на **SRM**)
  - **Auto-Shutdown Egregious A/B Tests**
- Slice the Analysis with the Appropriate Segments
  - Use Segments that are **Stable during the A/B Test** (только pre-treatment сегменты:
    market, country, browser, app version)
  - Segment by Date (ловит novelty, изменения среды, дефекты данных)

**Post-Experiment Stage**
- Verify Treatment Effects do not Invalidate Metrics
  - Ensure Metric Movements Align with the Test Set-Up
  - Check for any **Telemetry-Breaking Changes** — нужны метрики надёжности самой телеметрии
  - Check for **Imbalance in Metric Observation Units** (SRM на уровне метрики, знаменатель ratio-метрик)
- Estimate the Final Impact of the Treatment
  - **Segment By Triggered/Non-Triggered Users**
  - **Dilute Gains to Reflect the Trigger Rate** (разбавление эффекта до общей популяции)
  - Tradeoff the Observed Metric Movements (заранее согласованные веса конфликтующих метрик)
- Close the Loop on Experiment Results
  - When in Doubt, Reproduce Results (перезапуск на пересэмплированных пользователях)
  - Regularly Share Experiment Results
  - **Archive Hypothesis, Tests, and Metric Movements** (institutional memory, мета-анализ)

---

### 7. Microsoft/KDD-2017 — «A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls» [ОТКРЫЛ конспект]
https://github.com/shyaginuma/papers/issues/6 (оригинал `exp-platform.com` — 403).
Полный список 12 ловушек:

1. Metric Sample Ratio Mismatch — расхождение знаменателей между вариантами
2. Misinterpretation of Ratio Metrics — падение CTR при росте кликов из-за роста знаменателя
3. Telemetry Loss Bias — потеря телеметрии по-разному в вариантах
4. Assuming Underpowered Metrics had no Change — «незначимо» ≠ «нет эффекта»
5. Claiming Success with a Borderline p-value
6. Continuous Monitoring and Early Stopping
7. Assuming the Metric Movement is Homogeneous
8. Segment Interpretation — смещённая сегментация раздувает FPR
9. Impact of Outliers
10. Novelty and Primacy Effects
11. Incomplete Funnel Metrics — не отслеживаются все шаги воронки
12. Failure to Apply **Twyman's Law** — слишком хороший результат почти всегда баг

---

### 8. Kohavi / Tang / Xu — «Trustworthy Online Controlled Experiments» (книга) [ТОЛЬКО ОПИСАНИЕ]
Оглавление восстановлено из выдачи. Грейд: **middle+ / senior**. Главы:
Introduction and motivation; Running and analyzing experiments (end-to-end example);
**Twyman's law and experimentation trustworthiness**; Experimentation platform and culture;
Speed matters (case study); Organizational metrics; Metrics for experimentation and the **OEC**;
**Institutional memory and meta-analysis**; **Ethics in controlled experiments**;
Complementary techniques; Observational causal studies; Client-side experiments;
**Instrumentation**; Choosing a randomization unit; **Ramping experiment exposure**;
Scaling experiment analyses; The statistics behind online controlled experiments;
Variance estimation and improved sensitivity; The A/A test; **Triggering for improved sensitivity**;
**Guardrail metrics**.

Сопутствующая работа тех же авторов — KDD-2014 «Seven Rules of Thumb for Web Site Experimenters»
(`ai.stanford.edu` и `exp-platform.com` — [НЕ ДОСТУПЕН], 403). Из подтверждённых цитат: скорость
имеет значение и её влияние измеряют экспериментом с искусственной задержкой; изменения редко дают
большой положительный эффект; **carryover effects** между экспериментами на одних и тех же бакетах.

---

### 9. Google — Overlapping Experiment Infrastructure (KDD-2010, Tang et al.) [ТОЛЬКО ОПИСАНИЕ]
`research.google.com/pubs/archive/36500.pdf` — 403. Из подтверждённых цитат:
архитектура A/B-платформы из **layers / domains**, которые вкладываются друг в друга
(домены содержат слои, слои содержат эксперименты, слои могут содержать домены);
отдельный **launch domain / launch layer** для постепенного ramp-up выкаток;
свойства инфраструктуры: простота использования, скорость, масштабируемость, гибкость, устойчивость.
Противопоставляется «одному слою», где запрос может быть максимум в одном эксперименте.

---

### 10. Booking.com — «150 Successful ML Models: 6 Lessons Learned» (KDD-2019) [ТОЛЬКО ОПИСАНИЕ]
`kevinhu.me`-зеркало PDF, `blog.acolyer.org`, `queirozf.com` — все 403.
Шесть уроков (по подтверждённым цитатам):
1. ML-модели дают ощутимую бизнес-ценность
2. Качество модели ≠ бизнес-эффект: **отсутствует корреляция не между офлайн и онлайн качеством,
   а между приростом офлайн-метрики и приростом бизнес-ценности**; офлайн-метрика — только health check
3. Чётко формулируй решаемую задачу
4. **Латентность обслуживания имеет значение**: эксперимент с синтетической задержкой —
   рост латентности на ~30% стоил ~0.5% конверсии
5. Ранняя обратная связь о качестве модели — **Response Distribution Analysis (RDA)**:
   анализ распределения выходов модели позволяет ловить дефекты очень рано, без разметки
6. Бизнес-эффект проверяется рандомизированными контролируемыми испытаниями

Общий вывод: итеративный, гипотезо-ориентированный процесс, интегрированный с другими дисциплинами.

---

### 11. Netflix — серия по экспериментам + платформа [ТОЛЬКО ОПИСАНИЕ]
`netflixtechblog.com` — 403 на всех URL. Структура серии «Decision Making at Netflix» (подтверждена):
Part 1 Decision Making at Netflix → Part 2 What is an A/B Test? → Part 3 Interpreting A/B test results:
false positives and statistical significance → Part 4 Interpreting A/B test results: false negatives and
power → Part 5 How to build confidence in decisions based on A/B test results → финальный пост о культуре
экспериментирования.

Отдельные систематизированные материалы Netflix (из индекса ExperimentationResources):
Interleaving in Online Controlled Experiments; Quasi Experimentation at Netflix + Key Challenges with
Quasi Experiments; Sequential A/B Testing (Part 1: Continuous Data); Reimagining Experimentation Analysis;
Streaming Video Experimentation: Visualizing Practical and Statistical Significance;
Data Compression for Large-Scale Streaming Experimentation; It's All A/Bout Testing (платформа);
Improving the Sensitivity of Online Controlled Experiments: Case Studies at Netflix (KDD-2016).
Платформа поддерживает: interleaving, quantile bootstrapping, quasi experiments, quantile regression,
heterogeneous treatment effects.

---

### 12. Каталог DavisTrey/ExperimentationResources [ОТКРЫЛ]
https://raw.githubusercontent.com/DavisTrey/ExperimentationResources/master/README.md
Это не курс, а полный каталог инженерных материалов компаний по экспериментам. Разделы и состав:

- **Experimentation Platforms**: Stitch Fix (Building our Centralized Experimental Platform);
  Netflix (Reimagining Experimental Analysis); Airbnb (Scaling Airbnb's Experimentation Platform / ERF);
  Hulu (How We Scaled Experimentation at Hulu); DoorDash (Supporting Rapid Product Iteration with an
  Experimentation Analysis Platform); Squarespace (How we Reimagined A/B Testing)
- **Experimentation Culture**: Booking (Democratizing Online Experiments); HBR (Building a Culture of
  Experimentation); Microsoft (It takes a Flywheel to Fly); Netflix (A Culture of Learning);
  SIGKDD (Top Challenges from the first Practical Online Controlled Experiments Summit);
  VistaPrint; HelloFresh
- **Peeking and Sequential Testing**: Etsy (How Etsy Handles Peeking in A/B Testing); GoPractice
- **Variance Reduction and Experiment Throughput**: Faire (How to speed up your AB test, ч.1 и ч.2 —
  outlier capping + CUPED); **DoorDash (CUPAC — Control Using Predictions As Covariate)**;
  Facebook (Increasing sensitivity by utilizing variance estimates of experimental units);
  DoorDash (Improving Online Experiment Capacity by 4X with Parallelization);
  DoorDash (The 4 Principles to Increase Logistics Experiment Capacity by 1000%);
  Booking (Increasing the Power of Online Experiments with CUPED); TripAdvisor (Reducing variance by 30%)
- **Multi Arm Bandits**: Stitch Fix (Bandits and the Experimentation Platform); Booking (There's More to
  Experimentation Than A/B); VWO
- **Quasi Experiments**: Netflix ×2; Shopify (Quasi-experiments and Counterfactuals); NeurIPS-2018
- **Randomization and Assignment**: Microsoft (Tenant-Randomized A/B Test / tenant pairing);
  Netflix (Interleaving); **DoorDash (Switchback Tests under Network Effects; Analyzing Switchback
  Experiments by Cluster Robust Standard Error; Experiment Rigor for Switchback Analysis)**;
  Lyft (Experimentation in a Ridesharing Marketplace, части 1–3, включая симуляцию маркетплейса)
- **Statistical Tests and Measures**: Netflix (practical vs statistical significance; data compression);
  Convoy (**The Power of Bayesian A/B Testing**; **Cracking Correlated Observations with Mixed Effect
  Models**); Evan Miller (Formulas for Bayesian A/B Testing); Variance Explained (Is Bayesian A/B Testing
  Immune to Peeking?); Chris Stucchio (Decision Rules in Bayesian A/B testing); Wix (×2 по байесу);
  Twitter (Detecting and Avoiding Bucket Imbalance in A/B Tests)
- **Other Resources**: Evan Miller (How not to run an A/B Test); Reforge (Airbnb Growth Principles;
  Good Experiment, Bad Experiment); Twitter (The What and Why of Experimentation);
  Microsoft (Patterns of Trustworthy Experiments); Booking (**Leaky Abstractions in Online
  Experimentation Platforms**)
- **Causal Modeling**: Google CausalImpact; Lyft (Causal Models in Practice); Booking (Estimating
  Mechanisms of Change); Uber CausalML; Microsoft EconML
- **Experimentation Research**: Microsoft (A Dirty Dozen); Microsoft (Novelty/Primacy Effect Detection);
  Netflix/KDD (Improving Sensitivity); Microsoft (CUPED, оригинал); Optimizely/KDD (Peeking at A/B Tests);
  Facebook (Graph cluster randomization); ML for Variance Reduction in Online Experiments
- **Tools**: Eppo, StatSig, A/B Smartly, Split, Optimizely, Amplitude, VWO, LaunchDarkly, JetLab, GrowthBook

---

### 13. Индекс eugeneyan/applied-ml [ОТКРЫЛ]
https://raw.githubusercontent.com/eugeneyan/applied-ml/main/README.md
31 раздел: Data Quality; Data Engineering; Data Discovery; Feature Stores; Classification; Regression;
Forecasting; Recommendation; Search & Ranking; Embeddings; NLP; Sequence Modelling; Computer Vision;
Reinforcement Learning; Anomaly Detection; Graph; Optimization; Information Extraction; Weak Supervision;
Generation; Audio; Privacy-Preserving ML; Validation and A/B Testing; Model Management; Efficiency;
Ethics; Infra; MLOps Platforms; **Practices**; **Team Structure**; **Fails**.

Ключевые записи:
- Practices: Google (High-Interest Credit Card of Technical Debt; Rules of ML);
  Booking (ML in Production: The Booking.com Approach; 150 Successful ML Models);
  Cambridge (Challenges in Deploying Machine Learning)
- Data Quality: Airbnb (Reliable and Scalable Data Ingestion); Uber (Monitoring Data Quality at Scale
  with Statistical Modeling); Google (Data Management Challenges in Production ML; **Data Validation
  for Machine Learning**); Gojek (Hodor)
- Feature Stores: Netflix (Distributed Time Travel for Feature Generation); Gojek (Feast);
  Uber (Michelangelo Palette); DoorDash (Building Scalable ML Feature Store with Redis; **Riviera —
  Declarative Real-Time Feature Engineering**)
- Validation and A/B Testing: Google (Overlapping Experiment Infrastructure); Netflix; Pinterest
  (Building Pinterest's A/B Testing Platform); Airbnb (Scaling Experimentation Platform);
  Uber (Under the Hood of Uber's Experimentation Platform)
- MLOps Platforms: Uber (Michelangelo); Netflix (Metaflow); Instagram (Core Modeling);
  Lyft (Flyte); Shopify (Merlin)

Разделы **Team Structure** и **Fails** (разбор провалов ML-проектов) — самостоятельные срезы,
которых нет ни в одном учебном курсе.

---

### 14. Uber — Michelangelo [ТОЛЬКО ОПИСАНИЕ]
`uber.com/blog/michelangelo-machine-learning-platform` — 403; ZenML-зеркало — 403.
Шестишаговый workflow платформы (подтверждён цитатами):
**manage data → train models → evaluate models → deploy models → make predictions → monitor predictions**.
Компоненты: **Palette** (feature store; иерархия «сущность → группа фич → имя фичи → join key»),
model registry, workflow-система для оркестрации батч-пайплайнов/обучения/батч-предсказаний/деплоя,
**Model Excellence Score** (автоматическая оценка качества модели и данных в проде),
онлайн- и офлайн-режимы предсказаний, real-time проверки качества данных по логам предсказаний,
постепенный rollout с автоматическим откатом. Масштаб: ~400 активных ML-проектов, >5000 моделей,
до 10 млн предсказаний/сек.

---

### 15. DoorDash — ML-платформа и эксперименты [ТОЛЬКО ОПИСАНИЕ]
`doordash.engineering` / `careersatdoordash.com` — не открывал напрямую (403 на сопутствующих).
Компоненты: **Sibyl** (централизованный real-time inference service; gRPC, Redis как feature store,
in-memory кэш моделей; ~900k предсказаний/сек на пике; разделение inference, вычисления фич и обучения);
clusterless feature store (>130M HMGET/сек для 1.6 млрд фич, цель p999 = 50 мс; client-side caching дал +70%);
**Fabricator** (декларативный фреймворк описания фич с автогенерацией E2E-пайплайнов);
**Riviera** (декларативный real-time feature engineering).
Эксперименты: **CUPAC**, switchback + cluster-robust standard errors, параллелизация экспериментов.

---

### 16. Airbnb / Spotify / LinkedIn / Pinterest / Shopify / Etsy [ТОЛЬКО ОПИСАНИЕ]
- **Airbnb**: ERF (Experiment Reporting Framework), переписан на Python поверх Airflow;
  **метрический слой / metric consistency at scale** (единые определения метрик);
  **Bighead** — ML-платформа (Redspot — управляемые Jupyter; Deep Thought — real-time inference;
  **Zipline** — feature store с декларативным описанием фич на Python, автогенерацией
  offline-backfill и online-serving, point-in-time корректностью).
- **Spotify**: Experimentation Platform (Part 1 и Part 2). Part 1 — переход от ABBA к EP:
  замена feature flags на **properties** (Remote Configuration), **Metrics Catalog** вместо ноутбуков,
  **Experiment Planner**. Part 2 — координация множества одновременных экспериментов с сохранением
  **эксклюзивности и holdback'ов**, **«salt machine»** — автоматическая переперемешивание пользователей
  через дерево «солей» без остановки всех экспериментов. Далее — Confidence (внешний продукт).
- **LinkedIn**: **Feathr** — feature store с общим неймспейсом для определения/вычисления/сервинга фич,
  модель «producer/consumer» как в пакетном менеджере; десятки приложений (Search, Feed, Ads),
  сотни воркфлоу, петабайты фич; сокращение времени добавления фичи с недель до дней,
  до +50% производительности против кастомных пайплайнов; явная цель — снижение train/serve skew.
- **Pinterest**: Pinnability (ранжирование Homefeed по паре <user, pin>), типы сигналов
  (pinner / user / pin / context), realtime user sequence signals с sequence-модулем,
  **лайфлонг-последовательности пользовательских действий (16k+ действий)**,
  отбор действий по близости к кандидату в пространстве PinSage-эмбеддингов,
  модернизация **pre-ranking стадии**, LinkSage (GNN для внешнего контента),
  Building Pinterest's A/B Testing Platform.
- **Shopify**: **Merlin** — ML-платформа на **Ray**; Merlin Online Inference; Merlin Pipelines;
  **Pano Feature Store** на базе Feast; model registry и трекинг экспериментов на Comet ML.
  Отдельно — материал по квазиэкспериментам и контрфактуалам.
- **Etsy**: блог Code as Craft; систематизированный материал — «How Etsy Handles Peeking in A/B Testing»;
  «Building a Platform for Serving Recommendations at Etsy»; ML observability.

---

### 17. Meta — Embedding-based Retrieval in Facebook Search (KDD-2020) [ТОЛЬКО ОПИСАНИЕ]
`arxiv.org/pdf/2006.11632`, `ar5iv` — 403. Подтверждённые темы:
unified embedding framework для персонализированного поиска; интеграция embedding-based retrieval
**в существующий инвертированный индекс** (а не отдельным сервисом);
**hard negative mining** (лёгкие случайные негативы недостаточны; онлайн- и офлайн-варианты,
офлайн-HNM требует эффективной генерации top-K, ANN по одному случайному шарду достаточно);
**ANN tuning** (recall против числа просканированных документов, сравнение алгоритмов
грубого квантования); **full-stack / later-stage optimization** — сквозная оптимизация всей
системы, включая переобучение поздних стадий ранжирования под новый источник кандидатов.

---

### 18. AWS — Well-Architected Framework: Machine Learning Lens [ТОЛЬКО ОПИСАНИЕ]
`docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/` — 403.
Структура: **6 столпов** (Operational Excellence, Security, Reliability, Performance Efficiency,
Cost Optimization, **Sustainability**) × **фазы жизненного цикла ML**
(defining your business goal → framing your ML problem → preparing your data sources →
building your ML model → deployment → monitoring). Для каждой фазы — best practices по каждому
столбу, cloud-agnostic, плюс реализация на AWS.

---

### 19. Google — Data Validation for Machine Learning (MLSys/SysML 2019, TFX) [ТОЛЬКО ОПИСАНИЕ]
Подтверждённая программа: схема как версионируемый артефакт данных;
**single-batch anomalies** (проверка батча против схемы) vs **inter-batch anomalies**;
таксономия train/serve skew из трёх видов — **feature skew** (фича принимает разные значения
на обучении и на сервинге), **distribution skew** (расходятся распределения),
**scoring/serving skew** (то, как результаты показываются пользователю, возвращается в обучающие данные);
**model unit testing** на фиктивных данных, сгенерированных из схемы (6% прогонов ловят ошибку);
эксплуатация — сотни продуктовых команд, петабайты данных в сутки.

---

### 20. Model Cards / Datasheets for Datasets [ТОЛЬКО ОПИСАНИЕ]
Model Cards for Model Reporting (FAccT-2019, Google): стандартные разделы — Model Details;
Intended Use; Factors; Metrics; **Evaluation Data**; **Training Data**;
**Quantitative Analyses (unitary и intersectional разбивка качества по подгруппам)**;
**Ethical Considerations**; **Caveats and Recommendations**.
Datasheets for Datasets — документация мотивации, состава, процесса сбора и рекомендуемого
использования датасета. Комплементарны друг другу.

---

## ДЕЛЬТА: темы, которых нет в нашем манифесте

Только то, чего в `STRUCTURE.md` нет вовсе или что там есть лишь в виде общего слова, тогда как
источники дают именованную практику. Отсортировано по убыванию ценности.

### A. Эксперименты и A/B-платформа (самый плотный пробел)

| Тема | Где встретил | Почему важна для middle+ MLE | Куда добавить |
|---|---|---|---|
| **Триггерный анализ (triggered analysis) и разбавление эффекта (dilution) до общей популяции** | Microsoft ExP Post-Experiment [ОТКРЫЛ]; Kohavi, гл. «Triggering for improved sensitivity» | Базовый приём повышения чувствительности: анализируем только затронутых, потом честно пересчитываем эффект на всю аудиторию через trigger rate. Без него любой эксперимент над узкой фичей выглядит «незначимым». Спрашивают прямо | `docs/06-ab-testing/01-experiment-design.md` (дизайн) + `02-statistical-criteria.md` (пересчёт и дисперсия разбавленной метрики) |
| **Counterfactual logging** — логирование того, что показал бы контроль | Microsoft ExP Pre-Experiment [ОТКРЫЛ] | Единственный корректный способ определить триггерную популяцию в ML-системах, где treatment меняет выдачу. Прямо связан с recsys/поиском | `docs/06-ab-testing/01-experiment-design.md` |
| **Архитектура A/B-платформы: слои и домены (layers/domains), взаимоисключающие группы, launch layer, holdback, хеш-бакетирование по «соли»** | Google Overlapping Experiment Infrastructure [ТОЛЬКО ОПИСАНИЕ]; Spotify «salt machine» + эксклюзивность/holdback [ТОЛЬКО ОПИСАНИЕ] | На middle+ спрашивают «как запустить 200 экспериментов одновременно и не получить кашу». В манифесте нет ни одной строки про устройство платформы | `docs/06-ab-testing/01-experiment-design.md` (новый подраздел «инфраструктура экспериментов») или `05-complex-designs.md` |
| **Carryover effects и повторная рандомизация (reshuffle) бакетов** | Kohavi «Seven Rules of Thumb» [ТОЛЬКО ОПИСАНИЕ]; Spotify salt machine [ТОЛЬКО ОПИСАНИЕ] | Остаточный эффект прошлого эксперимента на тех же пользователях — источник систематических ложных выводов; лечится перемешиванием. У нас в pitfalls этого нет | `docs/06-ab-testing/04-pitfalls.md` |
| **Twyman's law: подозрительно хороший результат — почти всегда дефект** | Dirty Dozen п.12 [ОТКРЫЛ]; Kohavi (отдельная глава книги) [ТОЛЬКО ОПИСАНИЕ] | Практический фильтр здравого смысла + связка с проверками SRM/телеметрии. Часто звучит как вопрос «эксперимент дал +30% выручки, ваши действия?» | `docs/06-ab-testing/04-pitfalls.md` |
| **Bias телеметрии: telemetry loss и telemetry-breaking changes; метрики надёжности логирования** | Dirty Dozen п.3 [ОТКРЫЛ]; MS Post-Experiment [ОТКРЫЛ] | Классический источник ложного эффекта в мобильных/клиентских экспериментах: вариант чаще падает → его плохие сессии не долетают в логи | `docs/06-ab-testing/04-pitfalls.md` |
| **Metric-level SRM (дисбаланс единиц наблюдения в знаменателе ratio-метрик)** | MS Post-Experiment [ОТКРЫЛ]; Dirty Dozen п.1–2 [ОТКРЫЛ] | У нас SRM есть только на уровне распределения пользователей. Дисбаланс знаменателя ratio-метрики ловит другой класс багов | `docs/06-ab-testing/04-pitfalls.md` |
| **Правило «сегментировать только по pre-treatment (стабильным) признакам»** | MS During-Experiment [ОТКРЫЛ]; Dirty Dozen п.8 [ОТКРЫЛ] | Сегментация по признаку, на который влияет treatment, — это post-treatment bias, гарантированно ложные выводы. У нас есть «победа на подгруппах», но не сформулировано правило | `docs/06-ab-testing/04-pitfalls.md` |
| **Байесовский A/B-тест** | Convoy, Evan Miller, Wix, Variance Explained (каталог ExperimentationResources) [ОТКРЫЛ каталог] | В манифесте раздел 10 полностью частотный. Байесовский подход, его отношение к подглядыванию и правила принятия решений — стандартный вопрос на middle+ | Новый подраздел в `docs/06-ab-testing/02-statistical-criteria.md` |
| **CUPAC (Control Using Predictions As Covariate)** | DoorDash (каталог) [ОТКРЫЛ каталог] | Естественное развитие CUPED: ковариата — предсказание ML-модели по предпериодным данным. У нас CUPED и «регрессионная корректировка» есть, CUPAC как приём — нет | `docs/06-ab-testing/03-variance-reduction.md` |
| **Seedfinder и ретроспективный A/A на предпериоде** | MS Pre-Experiment [ОТКРЫЛ] | Проверка и устранение предэкспериментального смещения ещё до старта. У нас A/A есть, но только как «прогнать A/A» | `docs/06-ab-testing/01-experiment-design.md` |
| **Класс метрик «data quality metrics» в наборе эксперимента; полная таксономия метрик (OEC / guardrail / local & diagnostic / data quality)** | MS During-Experiment [ОТКРЫЛ] | У нас «ключевая, прокси, guardrail». Отсутствует класс метрик качества данных самого эксперимента и диагностических метрик фичи | `docs/06-ab-testing/01-experiment-design.md` |
| **OEC как формально взвешенная композиция + заранее согласованный trade-off между конфликтующими метриками** | MS Post-Experiment [ОТКРЫЛ]; Kohavi гл. «Metrics for experimentation and the OEC» [ТОЛЬКО ОПИСАНИЕ]; Rules of ML #39 | Ответ на «метрика A выросла, B упала — шипим?». У нас есть «ключевая метрика», но нет механики свёртки | `docs/06-ab-testing/01-experiment-design.md` |
| **Автоматическое отключение эксперимента (auto-shutdown) и алерты на guardrail во время теста** | MS During-Experiment [ОТКРЫЛ] | Эксплуатационная часть эксперимента: тест — тоже прод, у него нужен kill-switch | `docs/06-ab-testing/01-experiment-design.md` или `docs/07-mlops/08-deployment-strategies.md` |
| **Institutional memory: архив гипотез/тестов/движений метрик и мета-анализ накопленных экспериментов** | MS Post-Experiment [ОТКРЫЛ]; Kohavi гл. «Institutional memory and meta-analysis» [ТОЛЬКО ОПИСАНИЕ] | Отвечает на «как понять, что ваша команда учится»; база для калибровки априорных ожиданий и для оценки доли успешных идей | `docs/06-ab-testing/04-pitfalls.md` (блок про культуру) |
| **Воспроизведение удивительных результатов (re-run на пересэмплированных пользователях)** | MS Post-Experiment [ОТКРЫЛ] | Дешёвая защита от ложноположительных решений о запуске | `docs/06-ab-testing/04-pitfalls.md` |
| **Incomplete funnel metrics — обязательный мониторинг всех шагов воронки** | Dirty Dozen п.11 [ОТКРЫЛ] | Метрика последнего шага растёт, а верх воронки просел — типовая ловушка | `docs/06-ab-testing/01-experiment-design.md` |
| **Квантильные метрики и квантильный бутстрап / квантильная регрессия в экспериментах** | Netflix (платформа поддерживает quantile bootstrapping и quantile regression) [ТОЛЬКО ОПИСАНИЕ] | Для метрик латентности/качества стрима среднее бессмысленно; нужен эффект на p95. У нас бутстрап есть, квантильные эффекты — нет | `docs/06-ab-testing/02-statistical-criteria.md` |
| **Cluster-robust standard errors при анализе switchback-экспериментов** | DoorDash (3 статьи в каталоге) [ОТКРЫЛ каталог] | У нас switchback упомянут как дизайн, но не сказано, что наивный анализ даёт ложноположительные результаты и нужны кластерные ошибки | `docs/06-ab-testing/05-complex-designs.md` |
| **Симуляция маркетплейса как способ проверки дизайна эксперимента** | Lyft, «Experimentation in a Ridesharing Marketplace» ч.1–3 [ОТКРЫЛ каталог] | Когда сетевые эффекты не дают честного A/B, симуляция — рабочая альтернатива. У нас в 05 есть маркетплейсы, но симуляции нет | `docs/06-ab-testing/05-complex-designs.md` |
| **Ёмкость экспериментов как метрика платформы (параллелизация, переиспользование трафика)** | DoorDash «4X capacity», «1000% capacity» [ОТКРЫЛ каталог] | Организационно-инженерный ответ на «как ускорить продуктовые итерации» | `docs/06-ab-testing/01-experiment-design.md` |
| **Этика экспериментов** | Kohavi, отдельная глава [ТОЛЬКО ОПИСАНИЕ] | Вопрос «какие эксперименты нельзя запускать» реально задают на middle+ в продуктовых компаниях | `docs/06-ab-testing/04-pitfalls.md` |
| **Единый слой определений метрик (metrics store / metric consistency at scale)** | Airbnb (metric consistency, ERF) [ТОЛЬКО ОПИСАНИЕ]; Spotify Metrics Catalog [ТОЛЬКО ОПИСАНИЕ] | Одна и та же «конверсия» в трёх дашбордах = три разных числа. Инженерное решение — общий каталог метрик; у нас нигде не упоминается | `docs/06-ab-testing/01-experiment-design.md` или `docs/09-monitoring/01-what-to-monitor.md` |

### B. Продакшн-практики ML (MLOps / мониторинг)

| Тема | Где встретил | Почему важна для middle+ MLE | Куда добавить |
|---|---|---|---|
| **Измерение цены латентности экспериментом с синтетической задержкой** | Booking.com, урок 4 (+30% latency → −0.5% конверсии) [ТОЛЬКО ОПИСАНИЕ]; Kohavi «Speed matters» [ТОЛЬКО ОПИСАНИЕ] | Единственный способ обосновать бюджет латентности деньгами, а не «ну хочется быстрее». Прямо усиливает наш разговор о p95/p99 | `docs/07-mlops/05-serving-architectures.md` (бюджет латентности) со ссылкой из `09-inference-optimization.md` |
| **Response Distribution Analysis (RDA)** — диагностика модели по распределению её выходов без разметки | Booking.com, урок 5 [ТОЛЬКО ОПИСАНИЕ] | Именованный приём: бимодальность = модель различает, спайк/вырождение = дефект. У нас есть «мониторинг распределения предсказаний», но не как метод ранней диагностики дефектов до выката | `docs/09-monitoring/04-model-degradation.md` |
| **Rule #24: измерять дельту предсказаний между старой и новой моделью до A/B** | Rules of ML #24 [ОТКРЫЛ] | Дешёвый предвыкатной gate: если модели предсказывают почти одинаково, A/B бессмысленен; если слишком по-разному — ищи баг. У нас в 08-deployment-strategies этого нет | `docs/07-mlops/08-deployment-strategies.md` |
| **Measure model staleness: эксперимент «обучить на данных N дней назад и померить деградацию»** | Rules of ML #8 [ОТКРЫЛ]; ML Test Score Model 4 [ТОЛЬКО ОПИСАНИЕ] | Превращает вопрос «как часто переобучать» из мнения в измерение. У нас глава про переобучение есть, но методики измерения свежести нет | `docs/09-monitoring/07-retraining.md` |
| **Тихие отказы (silent failures) и обязательные sanity-проверки модели ПЕРЕД экспортом** | Rules of ML #9, #10 [ОТКРЫЛ] | Данные перестали обновляться, а все метрики модели в норме — самый частый и самый долгий инцидент. У нас есть gate-метрики, но не сформулирован класс «тихих» отказов | `docs/09-monitoring/02-data-quality.md` + `docs/09-monitoring/06-incidents-and-runbooks.md` |
| **Тестирование инфраструктуры отдельно от ML (сквозной прогон пайплайна с фиктивной моделью)** | Rules of ML #4, #5 [ОТКРЫЛ]; ML Test Score Infra 3 [ТОЛЬКО ОПИСАНИЕ] | «Сначала инфраструктура, потом качество» — принцип, который отличает middle от middle+ на System Design | `docs/07-mlops/07-ci-cd-for-ml.md` |
| **Model unit testing на данных, сгенерированных из схемы (fuzz по схеме)** | Google Data Validation (TFX) [ТОЛЬКО ОПИСАНИЕ]; ML Test Score Infra 2 [ТОЛЬКО ОПИСАНИЕ] | Конкретная техника тестирования ML-кода, которой нет в нашей главе о тестах | `docs/12-coding/07-testing-and-code-quality.md` |
| **Таксономия skew из трёх видов: feature skew / distribution skew / scoring-serving skew** | Google Data Validation [ТОЛЬКО ОПИСАНИЕ] | У нас train/serve skew — одно общее понятие. Разделение задаёт разные способы обнаружения и лечения | `docs/07-mlops/03-data-and-feature-store.md` |
| **Схема данных как эволюционирующий версионируемый артефакт (автогенерация схемы, предложение правок)** | Google Data Validation [ТОЛЬКО ОПИСАНИЕ]; ML Test Score Data 1 [ТОЛЬКО ОПИСАНИЕ] | У нас «схема и контракты» упомянуты, но не как версионируемый артефакт с жизненным циклом | `docs/09-monitoring/02-data-quality.md` |
| **Стоимость признака как критерий отбора (latency + инфра + поддержка)** | ML Test Score «No feature's cost is too much» [ТОЛЬКО ОПИСАНИЕ]; Rules of ML #22 | У нас отбор признаков — только про качество. Признак, стоящий 30 мс на запрос, отбирается по другим правилам | `docs/02-classic-ml/14-feature-engineering.md` |
| **Meta-level требования к признакам: политические/регуляторные ограничения на использование фич** | ML Test Score «Features adhere to meta-level requirements» [ТОЛЬКО ОПИСАНИЕ] | Нельзя использовать возраст/пол/геолокацию в скоринге — инженерное ограничение, а не юридическая сноска | `docs/07-mlops/03-data-and-feature-store.md` |
| **Privacy controls в ML-пайплайне: PII в фичах, логах предсказаний и обучающих данных** | ML Test Score «The data pipeline has appropriate privacy controls» [ТОЛЬКО ОПИСАНИЕ]; AWS ML Lens (Security pillar) [ТОЛЬКО ОПИСАНИЕ] | У нас PII разобран только в `05-llm/10`. Для классических ML-пайплайнов темы нет вообще | `docs/07-mlops/03-data-and-feature-store.md` |
| **Security-контур ML-системы (доступ к модели и фичам, шифрование, изоляция инференса)** | AWS Well-Architected ML Lens, столб Security [ТОЛЬКО ОПИСАНИЕ] | Столб, которого у нас нет ни в одной главе 07-mlops | `docs/07-mlops/06-docker-and-k8s.md` или `04-model-packaging.md` |
| **Model Cards и Datasheets for Datasets как стандарт документации модели/датасета** | Model Cards (FAccT-2019) [ТОЛЬКО ОПИСАНИЕ] | Артефакт, который на middle+ требуют в регулируемых доменах; естественно ложится к реестру моделей | `docs/07-mlops/04-model-packaging.md` |
| **Тестирование модели на справедливость / недискриминацию (inclusion): метрики по защищённым подгруппам** | ML Test Score Model 7 [ТОЛЬКО ОПИСАНИЕ]; PAIR Guidebook [ТОЛЬКО ОПИСАНИЕ] | Целого раздела fairness в манифесте нет. Минимум — demographic parity / equalized odds и разбивка качества по подгруппам как gate | `docs/02-classic-ml/04-metrics.md` (метрики) + `docs/07-mlops/07-ci-cd-for-ml.md` (gate) |
| **«A simpler model is not better» как обязательный формальный тест перед выкатом** | ML Test Score Model 5 [ТОЛЬКО ОПИСАНИЕ] | У нас бейзлайн — методическая рекомендация; здесь это формализованный пункт чек-листа готовности | `docs/07-mlops/07-ci-cd-for-ml.md` |
| **Debuggability модели (прогон одного примера по шагам)** | ML Test Score Infra 5 [ТОЛЬКО ОПИСАНИЕ] | Требование к архитектуре сервиса, которое приходится закладывать заранее | `docs/07-mlops/05-serving-architectures.md` |
| **Декларативное описание фич с автогенерацией offline-backfill и online-serving из одного определения** | Airbnb Zipline, DoorDash Fabricator/Riviera, LinkedIn Feathr, Uber Palette [ТОЛЬКО ОПИСАНИЕ] | Это ключевой архитектурный приём современных feature store, а не деталь. У нас feature store описан через материализацию/TTL/backfill, но не через «одно определение → два пайплайна» | `docs/07-mlops/03-data-and-feature-store.md` |
| **Ray как исполнительный слой ML-платформы** | Shopify Merlin на Ray [ТОЛЬКО ОПИСАНИЕ] | В манифесте распределённое обучение — только DDP/FSDP/Spark. Ray отсутствует, а он стал стандартом в платформенных стеках | `docs/08-big-data/07-distributed-training.md` |

### C. Моделирование и продуктовый слой

| Тема | Где встретил | Почему важна для middle+ MLE | Куда добавить |
|---|---|---|---|
| **Importance weighting сэмплированных данных (Rule #30: не выбрасывай, а взвешивай)** | Rules of ML #30 [ОТКРЫЛ] | Даунсэмплинг негативов ломает калибровку; корректный приём — взвешивание. У нас в главе про дисбаланс есть веса классов, но не восстановление калибровки после сэмплирования | `docs/02-classic-ml/13-imbalance-and-calibration.md` |
| **Эксплорация в фильтрующих системах (Rule #34: держать нефильтруемый срез трафика ради чистых данных)** | Rules of ML #34 [ОТКРЫЛ] | Антифрод/спам-фильтр не видит, что происходит с тем, что он заблокировал → данные вырождаются. Ключевой вопрос на кейсе про антифрод | `docs/11-system-design/04-case-fraud-detection.md` + ссылка из `docs/10-recsys/13-exploration-and-bandits.md` |
| **Later-stage optimization: при замене источника кандидатов надо переобучать ранжирование** | Meta EBR (full-stack optimization) [ТОЛЬКО ОПИСАНИЕ] | Классический провал: внедрили embedding-retrieval, метрики упали, потому что ранкер не умеет оценивать новый тип кандидатов. Не отражено ни в 10-recsys/01, ни в кейсе поиска | `docs/10-recsys/01-recsys-foundations.md` + `docs/11-system-design/03-case-search.md` |
| **Embedding-based retrieval внутри инвертированного индекса (гибрид на уровне индекса, а не двух сервисов)** | Meta EBR [ТОЛЬКО ОПИСАНИЕ] | У нас гибридный поиск описан как BM25 + dense с последующим слиянием. Вариант «ANN как оператор индекса» — другой архитектурный класс | `docs/10-recsys/06-two-tower-and-ann.md` |
| **Rule #40: ансамбли держать простыми (модель либо только потребляет выход другой, либо базовая)** | Rules of ML #40 [ОТКРЫЛ] | Правило против связности моделей в стеке, из-за которой ничего нельзя обновлять независимо | `docs/02-classic-ml/07-bagging-random-forest.md` или `docs/11-system-design/01-framework.md` |
| **Heuristics-first: запускать без ML, эвристика → фича, ML только когда эвристика стала неуправляемой (Rules #1, #3, #7)** | Rules of ML #1, #3, #7 [ОТКРЫЛ] | На System Design ожидают вопроса «а нужен ли здесь вообще ML» и корректного пути миграции эвристики в фичу | `docs/11-system-design/01-framework.md` |
| **Error analysis как метод: разбор ошибок руками, поиск паттернов, квантификация нежелательного поведения (Rules #23, #26, #27)** | Rules of ML #23, #26, #27 [ОТКРЫЛ] | «Ты не типичный пользователь» + систематический разбор ошибок → новые фичи. У нас есть сегментный анализ, но не метод работы с ошибками | `docs/02-classic-ml/04-metrics.md` или `docs/09-monitoring/04-model-degradation.md` |
| **Rule #37: измерение train/serve skew послойно (обучение vs holdout, holdout vs следующий день, следующий день vs живой трафик)** | Rules of ML #37 [ОТКРЫЛ] | Даёт диагностическую лестницу: по тому, на каком стыке расходится, сразу понятно, что сломано | `docs/07-mlops/03-data-and-feature-store.md` |
| **Продуктовый слой ML: ментальные модели пользователя, объяснения ДЛЯ пользователя, дизайн обратной связи и контроля, graceful failure UX** | Google PAIR People + AI Guidebook, гл. 3–6 [ТОЛЬКО ОПИСАНИЕ] | У нас `02-classic-ml/15-interpretability` — про SHAP/LIME для инженера, не про объяснение пользователю. Продуктовая деградация и дизайн сбора фидбека не отражены нигде, а на System Design это отдельный балл | `docs/11-system-design/01-framework.md` (шаг «продуктовые требования и деградация») + `docs/09-monitoring/06-incidents-and-runbooks.md` (фолбэк как продуктовый сценарий) |
| **Научный подход к тюнингу: разделение гиперпараметров на scientific / nuisance / fixed; isolation plots; квазислучайный поиск вместо байесовской оптимизации на фазе исследования** | Google Deep Learning Tuning Playbook [ОТКРЫЛ] | В `03-deep-learning/02-training-dynamics` есть диагностика по графикам, но нет методологии постановки серии экспериментов. Это ровно то, что отличает «покрутил параметры» от «провёл исследование» | `docs/03-deep-learning/02-training-dynamics.md` |
| **Ретроспективный выбор лучшего чекпоинта + протокол периодических оценок (какая выборка, как часто)** | Google Deep Learning Tuning Playbook [ОТКРЫЛ] | Практика, которую спрашивают в связке с «как понять, что пора останавливать обучение» | `docs/03-deep-learning/02-training-dynamics.md` |
| **Team Structure и Fails (разборы провалившихся ML-проектов) как отдельные срезы знания** | eugeneyan/applied-ml, разделы «Team Structure» и «Fails» [ОТКРЫЛ] | Поведенческая секция middle+ строится вокруг «расскажи о провале проекта»; систематизированные чужие провалы — материал для этих историй | `docs/14-career/02-behavioral.md` (истории) + `docs/07-mlops/01-ml-lifecycle.md` (что ломается на каждом этапе) |

---

## Чего найти не удалось

**Заблокировано (403 / DNS), содержание восстановлено лишь частично:**
- Полный список 28 тестов ML Test Score. Блоки **Model 1–7** и **Infra 1–7** получены целиком,
  **Data** — 7 пунктов, но без гарантии полноты и точности формулировок,
  **Monitor** — только 2 из 7 (Monitor 3 и Monitor 7). Первоисточники:
  `research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf`,
  `static.googleusercontent.com/.../45742.pdf` — оба 403. GitHub-зеркала полного списка не нашёл.
- Полный текст семи правил Kohavi «Seven Rules of Thumb for Web Site Experimenters»
  (`ai.stanford.edu`, `exp-platform.com`, `researchgate` — 403). Подтверждены только 3 из 7 по смыслу.
- Полное оглавление Google MLOps whitepaper «Practitioners Guide to MLOps»
  (`services.google.com`, `cloud.google.com` → `docs.cloud.google.com`, readkong — все 403).
  Список core capabilities получен из сниппетов, структура разделов — нет.
- Подразделы глав People + AI Guidebook (`pair.withgoogle.com` — 403). Есть только 6 названий глав.
- Полная структура AWS Well-Architected ML Lens по фазам (`docs.aws.amazon.com` — 403).
  Есть 6 столпов и общее описание фаз.
- Полный текст Meta «Embedding-based Retrieval in Facebook Search» (arXiv, ar5iv, dl.acm — 403).
  Нумерованная структура разделов не получена.
- Оригинальные посты Uber (`uber.com/blog`), Netflix (`netflixtechblog.com`), Airbnb/Spotify/Pinterest
  (`medium.com`, `engineering.atspotify.com`) — 403 повсеместно. Восстановлено только из сниппетов.
- «Continuous Delivery for Machine Learning» (CD4ML, Martin Fowler / ThoughtWorks) —
  `martinfowler.com/articles/cd4ml.html` 403, обойти не удалось. Программа не собрана.

**Не нашёл вовсе (отсутствие находки — тоже результат):**
- **Систематизированного открытого ML-хендбука у Etsy, Shopify, Pinterest, LinkedIn и Amazon.**
  У всех — набор разрозненных инженерных постов и отдельные статьи, но ни одного документа
  формата «руководство/чек-лист/плейбук» уровня Rules of ML или Patterns of Trustworthy Experimentation.
  Единственное исключение по Amazon — AWS Well-Architected ML Lens, но это документ AWS
  (архитектурный фреймворк для клиентов), а не внутренняя инженерная практика Amazon.
- **Публичного «ML handbook» у Meta.** Есть сильные статьи (DLRM, EBR) — но это research papers,
  не руководства.
- Открытого аналога ML Test Score от других компаний (ближайшее — Uber Model Excellence Score,
  но публичной спецификации критериев я не нашёл).
- Русскоязычных инженерных хендбуков компаний по ML в проде такого формата — искал,
  систематизированных материалов уровня перечисленных выше не обнаружил.
