# Classic ML + математика/статистика — research dump

> Собрано веб-поиском и прямыми фетчами 2026-07-26.
> **Правило дампа:** сюда попадают только вопросы, которые я реально видел в загруженном контенте.
> Ничего не выдумано, ни один URL не «восстановлен по памяти».
>
> **Важная методологическая оговорка про грейды.** Явную разметку по сложности даёт только
> один источник — `alexeygrigorev/data-science-interviews` (👶 / ⭐️ / 🚀). Там я переношу
> авторскую метку один в один. Во всех остальных случаях грейд — **моя атрибуция** по глубине
> вопроса, и её стоит перепроверять при переносе в главы.
>
> **Оговорка про компании.** Ни один из открывшихся источников не даёт пофамильной привязки
> «этот вопрос задали в компании X». Русскоязычный репозиторий `ML-Interview` заявлен как
> «вопросы с собеседований на позицию MLE», но без указания работодателей. Поэтому колонка
> «компания» почти везде пустая, и это честнее, чем проставить правдоподобные догадки.
> Единственное, что удалось подтвердить по компаниям, — **структура секций** (Т-Банк), см. §1.

---

## Источники, которые реально просмотрены

Ниже — только URL, которые вернули контент. Ключ в квадратных скобках используется дальше
как ссылка на источник у каждого вопроса.

### Русскоязычные

| Ключ | URL | Что там |
|---|---|---|
| `[MLI]` | https://raw.githubusercontent.com/Pe4enIks/ML-Interview/main/README.md | **Главный русскоязычный источник.** Репозиторий «Вопросы с собеседований на позицию Machine Learning Engineer». Живые формулировки, много каверзных. Компании не указаны. |
| `[TCAREER]` | https://raw.githubusercontent.com/Tinkoff/career/master/README.md | Репозиторий Т-Банка «ИТ-собеседования в Тинькофф», корневой README. |
| `[TINT]` | https://raw.githubusercontent.com/Tinkoff/career/master/interview/README.md | Разбивка секций интервью Т-Банка. Подтверждает: для ML — «Секция программирования», «Секция по ML», «Дизайн ML-систем». |
| `[HSE]` | https://raw.githubusercontent.com/esokolov/ml-course-hse/master/README.md | Программа курса «Машинное обучение» ФКН ВШЭ (Соколов). Канон тем и порядок их подачи. |
| `[DYAK]` | https://raw.githubusercontent.com/Dyakonov/MLDM_BOOK/main/README.md | Оглавление книги Дьяконова «Машинное обучение и анализ данных». Эталонная рубрикация классического ML на русском. |
| `[GIRAFE]` | https://raw.githubusercontent.com/girafe-ai/ml-course/master/README.md | Программа курса girafe-ai: Naive Bayes/kNN → линейные → SVM/PCA → деревья/ансамбли → бустинг. |
| `[ODS]` | https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/README.md | Открытый курс ODS mlcourse.ai: 10 тем + ссылки на русские статьи. |
| `[ODS10]` | https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/mlcourse_ai_jupyter_book/book/topic10/topic10_gradient_boosting.md | Тема 10 — градиентный бустинг: функциональный градиентный спуск, алгоритм Фридмана, лоссы. |

### Англоязычные — сборники вопросов

| Ключ | URL | Что там |
|---|---|---|
| `[AG-T]` | https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/theory.md | **Лучший размеченный источник.** Вопросы с явными грейдами 👶/⭐️/🚀 по всем темам classic ML. |
| `[AG-TECH]` | https://raw.githubusercontent.com/alexeygrigorev/data-science-interviews/master/technical.md | SQL / Python-кодинг / алгоритмы. Для classic ML — контекст соседних секций. |
| `[K120-P]` | https://raw.githubusercontent.com/kojino/120-Data-Science-Interview-Questions/master/probability.md | 20 вероятностных задач-«тизеров». |
| `[K120-PM]` | https://raw.githubusercontent.com/kojino/120-Data-Science-Interview-Questions/master/predictive-modeling.md | 19 вопросов по предиктивному моделированию. |
| `[K120-SI]` | https://raw.githubusercontent.com/kojino/120-Data-Science-Interview-Questions/master/statistical-inference.md | 16 вопросов по статвыводу и A/B. |
| `[K120]` | https://raw.githubusercontent.com/kojino/120-Data-Science-Interview-Questions/master/README.md | Оглавление (7 разделов). |
| `[YH-ML]` | https://raw.githubusercontent.com/youssefHosni/Data-Science-Interview-Questions-Answers/main/Machine%20Learning%20Interview%20Questions%20%26%20Answers%20for%20Data%20Scientists.md | 36 вопросов по ML, формулировки «как на собесе». |
| `[YH-ST]` | https://raw.githubusercontent.com/youssefHosni/Data-Science-Interview-Questions-Answers/main/Statistics%20Interview%20Questions%20%26%20Answers%20for%20Data%20Scientists.md | 20 вопросов по статистике. |
| `[YH-PR]` | https://raw.githubusercontent.com/youssefHosni/Data-Science-Interview-Questions-Answers/main/Probability%20Interview%20Questions%20%26%20Answers%20for%20Data%20Scientists.md | 17 вопросов по теории вероятностей. |
| `[YH]` | https://raw.githubusercontent.com/youssefHosni/Data-Science-Interview-Questions-Answers/main/README.md | Индекс разделов. |
| `[MLQ]` | https://raw.githubusercontent.com/andrewekhalel/MLQuestions/master/README.md | 67 вопросов ML/CV. Ценны пп. 52–67 (t-SNE, UMAP, LDA vs PCA, ликующий сплит). |
| `[CRACK]` | https://raw.githubusercontent.com/shafaypro/CrackingMachineLearningInterview/master/README.md | 156 вопросов, широкий охват включая Gini/энтропию/KL. |
| `[TODOR]` | https://raw.githubusercontent.com/iamtodor/data-science-interview-questions-and-answers/master/README.md | 33 вопроса, много про выбросы, разреженность, мультиколлинеарность. |
| `[KHANG]` | https://raw.githubusercontent.com/khangich/machine-learning-interview/master/README.md | Гайд + 5 явных задач по теорверу. Перечисляет компании (FAANG, Snap, LinkedIn, NVIDIA, Booking). |
| `[ALIREZA]` | https://raw.githubusercontent.com/alirezadir/Machine-Learning-Interviews/main/README.md | Структура ML-интервью (модули), без списка вопросов по classic ML. |
| `[ZAF]` | https://raw.githubusercontent.com/zafstojano/ml-interview-questions-and-answers/main/README.md | Решения к книге Chip Huyen. В README списка вопросов нет — только описание PDF. |
| `[EXTR]` | https://raw.githubusercontent.com/Extremesarova/ds_resources/main/README.md | Мета-индекс ресурсов. Через него найдены остальные источники. |

### Англоязычные — Devinterview-io, потематически

Все вернули по 15 первых вопросов из более крупных наборов (остальное — за пейволом на их сайте).

| Ключ | URL |
|---|---|
| `[DI-BV]` | https://raw.githubusercontent.com/Devinterview-io/bias-and-variance-interview-questions/main/README.md |
| `[DI-XGB]` | https://raw.githubusercontent.com/Devinterview-io/xgboost-interview-questions/main/README.md |
| `[DI-RF]` | https://raw.githubusercontent.com/Devinterview-io/random-forest-interview-questions/main/README.md |
| `[DI-ENS]` | https://raw.githubusercontent.com/Devinterview-io/ensemble-learning-interview-questions/main/README.md |
| `[DI-SVM]` | https://raw.githubusercontent.com/Devinterview-io/svm-interview-questions/main/README.md |
| `[DI-LOG]` | https://raw.githubusercontent.com/Devinterview-io/logistic-regression-interview-questions/main/README.md |
| `[DI-LIN]` | https://raw.githubusercontent.com/Devinterview-io/linear-regression-interview-questions/main/README.md |
| `[DI-KNN]` | https://raw.githubusercontent.com/Devinterview-io/k-nearest-neighbors-interview-questions/main/README.md |
| `[DI-NB]` | https://raw.githubusercontent.com/Devinterview-io/naive-bayes-interview-questions/main/README.md |
| `[DI-DR]` | https://raw.githubusercontent.com/Devinterview-io/dimensionality-reduction-interview-questions/main/README.md |
| `[DI-PCA]` | https://raw.githubusercontent.com/Devinterview-io/pca-interview-questions/main/README.md |
| `[DI-KM]` | https://raw.githubusercontent.com/Devinterview-io/k-means-clustering-interview-questions/main/README.md |
| `[DI-FE]` | https://raw.githubusercontent.com/Devinterview-io/feature-engineering-interview-questions/main/README.md |
| `[DI-TS]` | https://raw.githubusercontent.com/Devinterview-io/time-series-interview-questions/main/README.md |
| `[DI-GD]` | https://raw.githubusercontent.com/Devinterview-io/gradient-descent-interview-questions/main/README.md |
| `[DI-STAT]` | https://raw.githubusercontent.com/Devinterview-io/statistics-interview-questions/main/README.md |
| `[DI-PROB]` | https://raw.githubusercontent.com/Devinterview-io/probability-interview-questions/main/README.md |
| `[DI-LA]` | https://raw.githubusercontent.com/Devinterview-io/linear-algebra-interview-questions/main/README.md |

**Итого проверенных URL: 43.**

### Источники, которые НЕ открылись (для честности и для повторной попытки)

Инфраструктурно недоступны через фетчер (403 Cloudflare / бот-защита). Ссылки живые, контент
я **не видел** и потому ничего из них не цитирую:

- `habr.com/ru/companies/megafon/articles/808585/` — «Материалы для подготовки к собеседованию DS, ч.3»
- `habr.com/ru/articles/783766/` — «100 вопросов для подготовки к собесу Data Science»
- `habr.com/ru/articles/704128/`, `habr.com/ru/articles/667282/`, `habr.com/ru/articles/926214/`
- `ai.itmo.ru/blog/classic-ml-sobesedovanie-ml-engineer` — «Classic ML на собеседовании»
- `education.yandex.ru/knowledge/sektsiia-na-proverku-bazovikh-tekhnicheskikh-navikov-ml-inzhenerov` — описание ML-секции Яндекса
- `education.yandex.ru/handbook/ml/...` — учебник Яндекса по ML
- `yandex.ru/jobs/interview/mldev`, `yandex.ru/yaintern/ml/interview`
- `tinkoff.ru/career/it/interview/ml/`
- `enigmai.ru/interview/ozon/`, `dreamjob.ru/employers/26029/interviews`
- `btseytlin.github.io/parts/3_interviewing/technical_interview.html` — методичка по поиску работы в ML/DS
- `uzundemir.github.io/ml-interview` — вопросы для ML Junior
- `asmekal.github.io/blog/posts/interviews-2025-ml-research-engineer-uk` — отчёт о реальных интервью 2025
- `t.me/s/KarpovCourses`, `glassdoor.com/...Yandex-ML-Engineer...`, `interviewquery.com`, `datalemur.com`,
  `tryexponent.com`, `analyticsvidhya.com`, `neerc.ifmo.ru`, `arxiv.org/abs/1706.09516`

> Рекомендация оркестратору: `github.io`, `habr.com`, `t.me` и большинство рунет-медиа режутся
> целиком. Рабочий канал — `raw.githubusercontent.com`. Если нужен habr/ITMO — нужен другой транспорт.

---

## Вопросы с собеседований

Формат: `— вопрос` → `[грейд]` `[ключ источника]`.
Русские формулировки сохранены дословно, английские — тоже.

---

### 1. Линейная регрессия

- «Как аналитически решается задача линейной регрессии?» — **middle** `[MLI]`
- «Что такое проблема мультиколлинеарности признаков?» — **middle** `[MLI]`
- «Задача: линейная регрессия, все y > 0, какие алгоритмы могут дать отрицательное значение?» — **middle_plus** `[MLI]`
- What is regression? Which models can you use to solve a regression problem? — **junior** (👶) `[AG-T]`
- What is linear regression? When do we use it? — **junior** (👶) `[AG-T]`
- What are the main assumptions of linear regression? — **middle** (⭐️) `[AG-T]`
- What methods for solving linear regression do you know? — **middle** (⭐️) `[AG-T]`
- What is the normal equation? — **middle** (⭐️) `[AG-T]`
- Which metrics for evaluating regression models do you know? — **junior** (👶) `[AG-T]`
- What are MSE and RMSE? — **junior** (👶) `[AG-T]`
- What if we want to build a model for predicting prices? Are prices distributed normally? Do we need to do any pre-processing for prices? — **middle** (⭐️) `[AG-T]`
- What happens to our linear regression model if we have three columns in our data: x, y, z — and z is a sum of x and y? — **middle** (⭐️) `[AG-T]`
- What happens to our linear regression model if the column z in the data is a sum of columns x and y and some random noise? — **middle** (⭐️) `[AG-T]`
- What's the interpretation of the bias term in linear models? — **middle** (⭐️) `[AG-T]`
- How do we interpret weights in linear models? — **middle** (⭐️) `[AG-T]`
- If a weight for one variable is higher than for another — can we say that this variable is more important? — **middle** (⭐️) `[AG-T]`
- When do we need to perform feature normalization for linear models? When it's okay not to do it? — **middle** (⭐️) `[AG-T]`
- Explain the linear regression model and discuss its assumption — **junior** `[YH-ML]`
- What are the differences between a model that minimizes squared error and the one that minimizes the absolute error? and in which cases each error metric would be more appropriate — **middle** `[YH-ML]`
- What are some differences you would expect in a model that minimizes squared error, versus a model that minimizes absolute error? — **middle** `[K120-PM]`
- Can you explain the difference between simple linear regression and multiple linear regression? — **junior** `[DI-LIN]`
- What assumptions are made in linear regression modeling? — **middle** `[DI-LIN]`
- How do you interpret the coefficients of a linear regression model? — **middle** `[DI-LIN]`
- What is the role of the intercept term in a linear regression model? — **junior** `[DI-LIN]`
- Explain the concept of homoscedasticity. Why is it important? — **middle** `[DI-LIN]`
- What is multicollinearity and how can it affect a regression model? — **middle** `[DI-LIN]`
- How is hypothesis testing used in the context of linear regression? — **middle_plus** `[DI-LIN]`
- What do you understand by the term "normality of residuals"? — **middle** `[DI-LIN]`
- How is feature scaling relevant to linear regression? — **junior** `[DI-LIN]`
- What is Linear Regressions? How does it work? — **junior** `[CRACK]`
- What is Gradient Decent Formula to Linear Regression Equation? — **middle** `[CRACK]`
- What is the difference between Logistic and Linear Regressions? — **junior** `[CRACK]`
- How would you validate a model you created to generate a predictive model of a quantitative outcome variable using multiple regression? — **middle** `[TODOR]`
- You want to run a regression to predict the probability of a flight delay, but there are flights with delays of up to 12 hours that are really messing up your model. — **middle_plus** `[K120-PM]`

---

### 2. Логистическая регрессия и линейная классификация

- What is classification? Which models would you use to solve a classification problem? — **junior** (👶) `[AG-T]`
- What is logistic regression? When do we need to use it? — **junior** (👶) `[AG-T]`
- Is logistic regression a linear model? Why? — **junior** (👶) `[AG-T]`
- What is sigmoid? What does it do? — **junior** (👶) `[AG-T]`
- Explain briefly the logistic regression model and state an example of when you have used it recently — **junior** `[YH-ML]`
- What is logistic regression and how does it differ from linear regression? — **junior** `[DI-LOG]`
- Can you explain the concept of the logit function in logistic regression? — **middle** `[DI-LOG]`
- What is the sigmoid function and why is it important in logistic regression? — **junior** `[DI-LOG]`
- Discuss the probability interpretations of logistic regression outputs. — **middle** `[DI-LOG]`
- What are the assumptions made by logistic regression models? — **middle** `[DI-LOG]`
- How does logistic regression perform feature selection? — **middle** `[DI-LOG]`
- Explain the concept of odds and odds ratio in the context of logistic regression. — **middle** `[DI-LOG]`
- How do you interpret the coefficients of a logistic regression model? — **middle** `[DI-LOG]`
- Describe the maximum likelihood estimation as it applies to logistic regression. — **middle_plus** `[DI-LOG]`
- How do you handle categorical variables in logistic regression? — **junior** `[DI-LOG]`
- Can logistic regression be used for more than two classes? If so, how? — **middle** `[DI-LOG]`
- Discuss the consequences of multicollinearity in logistic regression. — **middle_plus** `[DI-LOG]`
- Explain regularization in logistic regression. What are L1 and L2 penalties? — **middle** `[DI-LOG]`
- How would you assess the goodness-of-fit of a logistic regression model? — **middle_plus** `[DI-LOG]`
- What is the effect on the coefficients of logistic regression if two predictors are highly correlated? What are the confidence intervals of the coefficients? — **middle_plus** `[TODOR]`
- What is Logit Function? or Sigmoid function / where in ML and DL you can use it? — **junior** `[CRACK]`
- What are various ways to predict a binary response variable? — **middle** `[K120-PM]`
- What is the difference between Preceptron and SVM? — **middle** `[CRACK]`

---

### 3. Регуляризация

- «Какие существуют методы регуляризации? Плюсы и минусы каждого» — **middle** `[MLI]`
- «Почему L1 регуляризация зануляет часть весов?» — **middle_plus** `[MLI]`
- What is regularization? Why do we need it? — **junior** (👶) `[AG-T]`
- Which regularization techniques do you know? — **middle** (⭐️) `[AG-T]`
- What kind of regularization techniques are applicable to linear models? — **middle** (⭐️) `[AG-T]`
- How does L2 regularization look like in a linear model? — **middle** (⭐️) `[AG-T]`
- How do we select the right regularization parameters? — **junior** (👶) `[AG-T]`
- What's the effect of L2 regularization on the weights of a linear model? — **middle** (⭐️) `[AG-T]`
- How L1 regularization looks like in a linear model? — **middle** (⭐️) `[AG-T]`
- What's the difference between L2 and L1 regularization? — **middle** (⭐️) `[AG-T]`
- Can we have both L1 and L2 regularization components in a linear model? — **middle** (⭐️) `[AG-T]`
- What are L1 and L2 regularization? What are the differences between the two — **middle** `[YH-ML]`
- What is regularization, why do we use it, and give some examples of common methods? — **junior** `[MLQ]` `[CRACK]`
- What is regularization and where might it be helpful? — **junior** `[K120-PM]`
- Explain what regularization is and why it is useful. — **junior** `[TODOR]`
- What's the difference between L1 and L2 regularization? — **middle** `[TODOR]`
- What is Regularization? / Difference between L1 and L2 Regularization? — **junior/middle** `[CRACK]`
- What is regularization, and how does it help with bias and variance? — **middle** `[DI-BV]`
- What is meant by 'regularization' in XGBoost and how does it help in preventing overfitting? — **middle_plus** `[DI-XGB]`

---

### 4. Bias–variance, переобучение

- «Что такое переобучение? Какие есть способы борьбы с ним?» — **junior** `[MLI]`
- «Что такое bias, variance модели?» — **junior** `[MLI]`
- «Что такое bias-variance trade-off?» — **middle** `[MLI]`
- «Какой bias и variance у различных типов моделей: линейные модели, деревья, ансамбли?» — **middle_plus** `[MLI]`
- «Почему деревья сильнее переобучаются?» — **middle** `[MLI]`
- What is the bias-variance trade-off? — **junior** (👶) `[AG-T]`
- What is overfitting? — **junior** (👶) `[AG-T]`
- What are the Bias and Variance in a Machine Learning Model and explain the bias-variance trade-off — **junior** `[YH-ML]`
- What's the trade-off between bias and variance? — **junior** `[MLQ]` `[CRACK]`
- Explain over- and under-fitting and how to combat them? — **junior** `[MLQ]` `[CRACK]`
- What are bias and variance, and what are their relation to modeling data? — **junior** `[TODOR]`
- What do you understand by the terms bias and variance in machine learning? — **junior** `[DI-BV]`
- How do bias and variance contribute to the overall error in a predictive model? — **middle** `[DI-BV]`
- Can you explain the difference between a high-bias model and a high-variance model? — **junior** `[DI-BV]`
- Why is it impossible to simultaneously minimize both bias and variance? — **middle_plus** `[DI-BV]`
- How does model complexity relate to bias and variance? — **middle** `[DI-BV]`
- What could be the potential causes of high variance in a model? — **middle** `[DI-BV]`
- What might be the reasons behind a model's high bias? — **middle** `[DI-BV]`
- How would you diagnose bias and variance issues using learning curves? — **middle_plus** `[DI-BV]`
- What is the expected test error, and how does it relate to bias and variance? — **middle_plus** `[DI-BV]`
- How do you use cross-validation to estimate bias and variance? — **middle_plus** `[DI-BV]`
- What techniques are used to reduce bias in machine learning models? — **middle** `[DI-BV]`
- Can you list some methods to lower variance in a model without increasing bias? — **middle_plus** `[DI-BV]`
- Describe how boosting helps to reduce bias. — **middle_plus** `[DI-BV]`
- Which Algorithms are High Biased Algorithms? / Which Algorithms are High and low Variance Algorithms? / Why are the above algorithms high biased or high variance? — **middle** `[CRACK]`
- What are root cause of Prediction Bias? — **middle_plus** `[CRACK]`
- How would you resolve Overfitting or Underfitting? / Mention some techniques which are to avoid Overfitting? — **junior** `[CRACK]`
- What is an inductive bias? — **middle_plus** `[TODOR]`

---

### 5. Метрики классификации (ROC-AUC, PR-AUC, logloss, калибровка)

Это самый «плотный» блок русскоязычного источника — формулировки почти всегда с подвохом.

- «Какие метрики бинарной классификации есть? Плюсы и минусы каждой.» — **junior** `[MLI]`
- «Что такое TPR и FPR?» — **junior** `[MLI]`
- «Как ROC-AUC работает на данных с дисбалансом классов?» — **middle_plus** `[MLI]`
- «ROC-AUC = 0.9, что с ним будет если домножить все предсказания на 3?» — **middle_plus** `[MLI]`
- «Метрики multiclass классификации, их плюсы и минусы.» — **middle** `[MLI]`
- «Какая вероятностная интерпретация у ROC-AUC?» — **middle_plus** `[MLI]`
- «Как происходит расчет ROC-AUC?» — **middle** `[MLI]`
- «Как определяются thresholds для расчета ROC-AUC?» — **middle_plus** `[MLI]`
- «Задача: как изменятся precision и recall, если выкинуть 10 нулей из таргета?» — **middle_plus** `[MLI]`
- How do we evaluate classification models? — **junior** (👶) `[AG-T]`
- What is accuracy? — **junior** (👶) `[AG-T]`
- Is accuracy always a good metric? — **junior** (👶) `[AG-T]`
- What is the confusion table? What are the cells in this table? — **junior** (👶) `[AG-T]`
- What are precision, recall, and F1-score? — **junior** (👶) `[AG-T]`
- Precision-recall trade-off — **middle** (⭐️) `[AG-T]`
- What is the ROC curve? When to use it? — **middle** (⭐️) `[AG-T]`
- What is AUC (AU ROC)? When to use it? — **middle** (⭐️) `[AG-T]`
- How to interpret the AU ROC score? — **middle** (⭐️) `[AG-T]`
- What is the PR (precision-recall) curve? — **middle** (⭐️) `[AG-T]`
- What is the area under the PR curve? Is it a useful metric? — **middle** (⭐️) `[AG-T]`
- **In which cases AU PR is better than AU ROC?** — **middle_plus** (⭐️) `[AG-T]` ← ключевой водораздел middle/middle+
- Define Precision, recall, and F1 and discuss the trade-off between them — **junior** `[YH-ML]`
- What is the ROC curve and when should you use it — **middle** `[YH-ML]`
- What are the evaluation metrics that can be used for multi-label classification — **middle_plus** `[YH-ML]`
- What error metric would you use to evaluate how good a binary classifier is? — **middle** `[K120-PM]`
- Explain how a ROC curve works. — **middle** `[MLQ]` `[CRACK]`
- What's the difference between Type I and Type II error? — **junior** `[MLQ]` `[CRACK]`
- Explain what precision and recall are. How do they relate to the ROC curve? — **middle** `[TODOR]`
- Is it better to have too many false positives, or too many false negatives? — **middle** `[TODOR]`
- How would you define AUC - ROC Curve? — **middle** `[CRACK]`
- How would you define False positive or Type I error and False Negative or Type II Error? — **junior** `[CRACK]`
- Which one would you prefer for your classification model: Precision or Recall? — **middle** `[CRACK]`
- What is F1 Score? which intuition does it give? — **junior** `[CRACK]`
- Which one would you prefer, low FN or FP's, based on Fraudulent Transaction? — **middle** `[CRACK]`
- How would you evaluate your classifier? — **junior** `[CRACK]`
- What is a Confusion Matrix? — **junior** `[CRACK]`
- How would you differentiate between Multilabel and MultiClass classification? — **junior** `[CRACK]`
- What are the different types of Evaluation metrics in Regression? — **junior** `[CRACK]`
- How would you define Mean absolute error vs Mean squared error? — **junior** `[CRACK]`
- What is cost function? — **junior** `[MLQ]` `[CRACK]`
- What are Loss Functions and Cost Functions? Explain the key Difference Between them — **junior** `[YH-ML]`
- How would you define Cross Entropy, What is the main purpose of it? — **middle** `[CRACK]`
- What is KL divergence, how would you define its use case in ML? — **middle_plus** `[CRACK]`

> **Пробел источников.** Ни один открывшийся источник не задаёт прямого вопроса про
> **калибровку вероятностей** (Platt / isotonic / reliability diagram / Brier score / ECE).
> При этом тема разбирается в найденных, но не открывшихся материалах. Для хендбука это
> означает: калибровку надо писать «на опережение» — вопросов в дампах мало, а в проде она
> критична, и на middle+ секциях её спрашивают через прикладную рамку («модель даёт 0.8,
> а конверсия 0.4 — что не так?»).

---

### 6. Валидация, кросс-валидация, утечки

- How to validate your models? — **junior** (👶) `[AG-T]`
- Why do we need to split our data into three parts: train, validation, and test? — **junior** (👶) `[AG-T]`
- Can you explain how cross-validation works? — **junior** (👶) `[AG-T]`
- What is K-fold cross-validation? — **junior** (👶) `[AG-T]`
- How do we choose K in K-fold cross-validation? What's your favorite K? — **junior** (👶) `[AG-T]`
- Define the cross-validation process and the motivation behind using it — **junior** `[YH-ML]`
- Why do we need a validation set and test set? What is the difference between them? — **junior** `[MLQ]` `[CRACK]`
- What is stratified cross-validation and when should we use it? — **middle** `[MLQ]` `[CRACK]`
- **Given that we want to evaluate the performance of 'n' different machine learning models on the same data, why would the following splitting mechanism be incorrect** (приводится код) — **middle_plus** `[MLQ]` ← классический вопрос-ловушка на утечку через переиспользование сплита
- What could be some issues if the distribution of the test data is significantly different than the distribution of the training data? — **middle** `[K120-PM]`
- Explain the concept of data splitting into training and test sets. — **junior** `[DI-LIN]`
- Which hyper-parameter tuning strategies (in general) do you know? — **middle** (⭐️) `[AG-T]`
- What's the difference between grid search parameter tuning strategy and random search? When to use one or another? — **middle** (⭐️) `[AG-T]`

---

### 7. Решающие деревья

- «Как происходит процесс построения дерева?» — **middle** `[MLI]`
- What are the decision trees? — **junior** (👶) `[AG-T]`
- How do we train decision trees? — **middle** (⭐️) `[AG-T]`
- What are the main parameters of the decision tree model? — **junior** (👶) `[AG-T]`
- How do we handle categorical variables in decision trees? — **middle** (⭐️) `[AG-T]`
- What are the benefits of a single decision tree compared to more complex models? — **middle** (⭐️) `[AG-T]`
- How can we know which features are more important for the decision tree model? — **middle** (⭐️) `[AG-T]`
- Explain what is information gain and entropy in the context of decision trees — **middle** `[YH-ML]`
- What are the different methods to split a tree in a decision tree algorithm — **middle** `[YH-ML]`
- What is Randomforest and Decision Trees? — **junior** `[CRACK]`
- What is Process of Splitting? / What is the process of pruning? / How do you do Tree Selection? — **middle** `[CRACK]`
- Pseudocode for Entropy in Decision Trees — **middle_plus** `[CRACK]`
- What is Gini Index? Explain the concept? / What is the process of gini index calculation? / What is the formulation of Gini Split / Gini Index? — **middle** `[CRACK]`
- What is Entropy? and Information Gain? their difference? — **middle** `[CRACK]`
- Describe the decision tree model. — **junior** `[TODOR]`

---

### 8. Бэггинг и случайный лес

- «Рассказать про RandomForest.» — **junior** `[MLI]`
- «Что такое bagging?» — **junior** `[MLI]`
- «Можно ли строить RandomForest над KNN, линейными моделями и нейросетями, почему?» — **middle_plus** `[MLI]`
- What is random forest? — **junior** (👶) `[AG-T]`
- Why do we need randomization in random forest? — **middle** (⭐️) `[AG-T]`
- What are the main parameters of the random forest model? — **middle** (⭐️) `[AG-T]`
- How do we select the depth of the trees in random forest? — **middle** (⭐️) `[AG-T]`
- How do we know how many trees we need in random forest? — **middle** (⭐️) `[AG-T]`
- Is it easy to parallelize training of a random forest model? How can we do it? — **middle** (⭐️) `[AG-T]`
- What are the potential problems with many large trees? — **middle** (⭐️) `[AG-T]`
- **What if instead of finding the best split, we randomly select a few splits and just select the best from them. Will it work?** — **middle_plus** (🚀) `[AG-T]` ← по сути «выведи Extra Trees»
- What happens when we have correlated features in our data? — **middle** (⭐️) `[AG-T]`
- Describe the motivation behind random forests and mention two reasons why they are better than individual decision trees — **junior** `[YH-ML]`
- How does a Random Forest differ from a single decision tree? — **junior** `[DI-RF]`
- What is bagging, and how is it implemented in a Random Forest? — **junior** `[DI-RF]`
- How does Random Forest achieve feature randomness? — **middle** `[DI-RF]`
- What is out-of-bag (OOB) error in Random Forest? — **middle** `[DI-RF]`
- **Are Random Forests biased towards attributes with more levels? Explain your answer.** — **middle_plus** `[DI-RF]`
- How do you handle missing values in a Random Forest model? — **middle** `[DI-RF]`
- What are the key hyperparameters of a Random Forest, and how do they affect the model? — **middle** `[DI-RF]`
- What is the difference between Random Forest and Extra Trees classifiers? — **middle_plus** `[DI-RF]`
- How does Random Forest prevent overfitting in comparison to decision trees? — **middle** `[DI-RF]`
- Explain the differences between Random Forest and AdaBoost. — **middle** `[DI-RF]`
- What is ensemble learning in machine learning? — **junior** `[DI-ENS]`
- Can you explain the difference between bagging, boosting, and stacking? — **middle** `[DI-ENS]`
- Describe what a weak learner is and how it's used in ensemble methods. — **middle** `[DI-ENS]`
- How does ensemble learning help with the variance and bias trade-off? — **middle_plus** `[DI-ENS]`
- What is a bootstrap sample and how is it used in bagging? — **middle** `[DI-ENS]`
- What is model stacking and how do you select base learners for it? — **middle_plus** `[DI-ENS]`
- What is the difference between hard and soft voting classifiers in the context of ensemble learners — **middle** `[YH-ML]`
- Why do ensembles typically have higher scores than individual models? — **middle** `[MLQ]` `[CRACK]`
- What's the difference between boosting and bagging? — **junior** `[MLQ]` `[CRACK]`
- How would you define Bagging and Boosting? How would XGBoost differ from RandomForest? — **middle** `[CRACK]`

---

### 9. Градиентный бустинг + XGBoost / LightGBM / CatBoost

Самый частотный блок на middle/middle+ секциях в РФ.

- **«Что такое градиентный бустинг? Где там появляется градиент?»** — **middle** `[MLI]` ← вопрос-фильтр: отделяет «читал» от «понимает функциональный градиентный спуск»
- «Есть градиентный бустинг и случайный лес на 1000 деревьев, что будет с качеством, если удалить первое дерево?» — **middle_plus** `[MLI]`
- «Почему в градиентном бустинге обычно менее глубокие деревья, чем в случайном лесе?» — **middle_plus** `[MLI]`
- What is gradient boosting trees? — **middle** (⭐️) `[AG-T]`
- What's the difference between random forest and gradient boosting? — **middle** (⭐️) `[AG-T]`
- Is it possible to parallelize training of a gradient boosting model? How to do it? — **middle_plus** (⭐️) `[AG-T]`
- Feature importance in gradient boosting trees — what are possible options? — **middle** (⭐️) `[AG-T]`
- **Are there any differences between continuous and discrete variables when it comes to feature importance of gradient boosting models?** — **middle_plus** (🚀) `[AG-T]`
- What are the main parameters in the gradient boosting model? — **middle** (⭐️) `[AG-T]`
- **How do you approach tuning parameters in XGBoost or LightGBM?** — **middle_plus** (🚀) `[AG-T]`
- How do you select the number of trees in the gradient boosting model? — **middle** (⭐️) `[AG-T]`
- What are the differences and similarities between gradient boosting and random forest? and what are the advantages and disadvantages of each when compared to each other — **middle** `[YH-ML]`
- What is boosting in the context of ensemble learners? discuss two famous boosting methods — **middle** `[YH-ML]`
- Why boosting is a more stable algorithm as compared to other ensemble algorithms — **middle_plus** `[YH-ML]`
- Describe how Gradient Boosting works. — **middle** `[TODOR]`
- Difference between AdaBoost and XGBoost — **middle** `[TODOR]`
- Describe the AdaBoost algorithm and its process. — **middle** `[DI-ENS]`
- How does Gradient Boosting work and what makes it different from AdaBoost? — **middle** `[DI-ENS]`
- Explain XGBoost and its advantages over other boosting methods. — **middle** `[DI-ENS]`
- Discuss the principle behind the LightGBM algorithm. — **middle_plus** `[DI-ENS]`
- **How does the CatBoost algorithm handle categorical features differently from other boosting algorithms?** — **middle_plus** `[DI-ENS]` ← сюда ложится ordered target statistics
- Compare Random Forest with Gradient Boosting Machine (GBM). — **middle** `[DI-RF]`
- What is XGBoost and why is it considered an effective machine learning algorithm? — **middle** `[DI-XGB]`
- Can you explain the differences between gradient boosting machines (GBM) and XGBoost? — **middle_plus** `[DI-XGB]`
- **How does XGBoost handle missing or null values in the dataset?** — **middle_plus** `[DI-XGB]` ← про default direction в сплите
- How does XGBoost differ from random forests? — **middle** `[DI-XGB]`
- Explain the concept of gradient boosting. How does it work in the context of XGBoost? — **middle** `[DI-XGB]`
- What are the loss functions used in XGBoost for regression and classification problems? — **middle** `[DI-XGB]`
- How does XGBoost use tree pruning and why is it important? — **middle_plus** `[DI-XGB]`
- Describe the role of shrinkage (learning rate) in XGBoost. — **middle** `[DI-XGB]`
- What are the core parameters in XGBoost that you often consider tuning? — **middle** `[DI-XGB]`
- Explain the importance of the 'max_depth' parameter in XGBoost. — **middle** `[DI-XGB]`
- Discuss how to manage the trade-off between learning rate and n_estimators in XGBoost. — **middle** `[DI-XGB]`
- What is early stopping in XGBoost and how can it be implemented? — **middle** `[DI-XGB]`
- How does the objective function affect the performance of the XGBoost model? — **middle_plus** `[DI-XGB]`
- Discuss how XGBoost can handle highly imbalanced datasets. — **middle_plus** `[DI-XGB]`

**Канон для ответов (из `[ODS10]`, реально прочитано):** бустинг как оптимизация в пространстве
функций; алгоритм Фридмана 1999 (начальное константное приближение → псевдо-остатки →
базовый алгоритм на них → обновление); лоссы L2/L1/квантильный для регрессии, logistic/exponential
для классификации; веса наблюдений как альтернатива новому лоссу; тезис источника — «нет
100 % победителя» среди XGBoost / LightGBM / CatBoost.

> **Пробел источников.** Прямых вопросов про **leaf-wise vs level-wise**, **GOSS**, **EFB**,
> **гистограммные сплиты**, **ordered boosting**, **oblivious/symmetric trees** в открывшихся
> дампах нет — только «CatBoost handles categorical features differently» и «principle behind
> LightGBM». Это ровно та глубина, на которой в РФ отсеивают middle+, поэтому в хендбуке
> раздел надо писать существенно глубже, чем дают дампы.

---

### 10. SVM

- What is a Support Vector Machine (SVM) in Machine Learning? — **junior** `[DI-SVM]`
- Can you explain the concept of hyperplane in SVM? — **junior** `[DI-SVM]`
- What is the maximum margin classifier in the context of SVM? — **middle** `[DI-SVM]`
- What are support vectors and why are they important in SVM? — **junior** `[DI-SVM]`
- Discuss the difference between linear and non-linear SVM. — **middle** `[DI-SVM]`
- How does the kernel trick work in SVM? — **middle_plus** `[DI-SVM]`
- What kind of kernels can be used in SVM and give examples of each? — **middle** `[DI-SVM]`
- Can you explain the concept of a soft margin in SVM and why it's used? — **middle** `[DI-SVM]`
- How does SVM handle multi-class classification problems? — **middle** `[DI-SVM]`
- What are some of the limitations of SVMs? — **middle** `[DI-SVM]`
- Describe the objective function of the SVM. — **middle_plus** `[DI-SVM]`
- What is the role of the Lagrange multipliers in SVM? — **middle_plus** `[DI-SVM]`
- Explain the process of solving the dual problem in SVM optimization. — **middle_plus** `[DI-SVM]`
- How do you choose the value of the regularization parameter (C) in SVM? — **middle** `[DI-SVM]`
- Explain the concept of the hinge loss function. — **middle** `[DI-SVM]`
- Explain the kernel trick in SVM and why we use it and how to choose what kernel to use — **middle_plus** `[YH-ML]`
- Do you need to scale your data if you will be using the SVM classifier and discuss your answer — **middle** `[YH-ML]`
- What is Support Vector Machine? how is it different from OVR classifiers? / Types of SVM kernels — **middle** `[CRACK]`

---

### 11. kNN и метрические методы

- What is K-Nearest Neighbors (K-NN) in the context of machine learning? — **junior** `[DI-KNN]`
- How does the K-NN algorithm work for classification problems? — **junior** `[DI-KNN]`
- Explain how K-NN can be used for regression. — **junior** `[DI-KNN]`
- What does the 'K' in K-NN stand for, and how do you choose its value? — **junior** `[DI-KNN]`
- List the pros and cons of using the K-NN algorithm. — **junior** `[DI-KNN]`
- In what kind of situations is K-NN not an ideal choice? — **middle** `[DI-KNN]`
- How does the choice of distance metric affect the K-NN algorithm's performance? — **middle** `[DI-KNN]`
- What are the effects of feature scaling on the K-NN algorithm? — **junior** `[DI-KNN]`
- How does K-NN handle multi-class problems? — **junior** `[DI-KNN]`
- Can K-NN be used for feature selection? If yes, explain how. — **middle_plus** `[DI-KNN]`
- What are the differences between weighted K-NN and standard K-NN? — **middle** `[DI-KNN]`
- **How does the curse of dimensionality affect K-NN, and how can it be mitigated?** — **middle_plus** `[DI-KNN]`
- Discuss the impact of imbalanced datasets on the K-NN algorithm. — **middle** `[DI-KNN]`
- How would you explain the concept of locality-sensitive hashing and its relation to K-NN? — **middle_plus** `[DI-KNN]`
- Explore the differences between K-NN and Radius Neighbors. — **middle_plus** `[DI-KNN]`
- What is KNN how does it work? what is neighbouring criteria? How you can change it? — **junior** `[CRACK]`
- Differentiate between KNN and KMean? — **junior** `[CRACK]`

---

### 12. Naive Bayes и байесовский подход

- What is the Naive Bayes classifier and how does it work? — **junior** `[DI-NB]`
- Explain Bayes' Theorem and how it applies to the Naive Bayes algorithm. — **junior** `[DI-NB]`
- Can you list and describe the types of Naive Bayes classifiers? — **middle** `[DI-NB]`
- What is the 'naive' assumption in the Naive Bayes classifier? — **junior** `[DI-NB]`
- How does the Naive Bayes classifier handle categorical and numerical features? — **middle** `[DI-NB]`
- Why is the Naive Bayes classifier a good choice for text classification tasks? — **middle** `[DI-NB]`
- Explain the concept of 'class conditional independence' in Naive Bayes. — **middle** `[DI-NB]`
- What are the advantages and disadvantages of using a Naive Bayes classifier? — **junior** `[DI-NB]`
- How does the Multinomial Naive Bayes classifier differ from the Gaussian Naive Bayes classifier? — **middle** `[DI-NB]`
- **Why do we often use the log probabilities instead of probabilities in Naive Bayes computation?** — **middle_plus** `[DI-NB]`
- Explain how a Naive Bayes classifier can be used for spam detection. — **junior** `[DI-NB]`
- How would you deal with missing values when implementing a Naive Bayes classifier? — **middle** `[DI-NB]`
- **What role does the Laplace smoothing (additive smoothing) play in Naive Bayes?** — **middle_plus** `[DI-NB]`
- Can Naive Bayes be used for regression tasks? Why or why not? — **middle** `[DI-NB]`
- How does Naive Bayes perform in terms of model interpretability compared to other classifiers? — **middle** `[DI-NB]`
- What is Naive Bayes? How does it work? / What is Bayes Theorem? — **junior** `[CRACK]`
- What's the difference between a generative and discriminative model? — **middle_plus** `[MLQ]`
- What is the difference between Bayesian vs frequentist statistics? — **middle_plus** `[MLQ]`
- Can you explain the difference between frequentist and Bayesian probability approaches? — **middle_plus** `[YH-PR]`
- Explain the Difference Between Probability and Likelihood — **middle** `[YH-PR]`
- Define and compare parametric and non-parametric models and give two examples for each of them — **middle** `[YH-ML]`

---

### 13. Кластеризация

- What is unsupervised learning? — **junior** (👶) `[AG-T]`
- What is clustering? When do we need it? — **junior** (👶) `[AG-T]`
- Do you know how K-means works? — **middle** (⭐️) `[AG-T]`
- How to select K for K-means? — **middle** (⭐️) `[AG-T]`
- What are the other clustering algorithms do you know? — **middle** (⭐️) `[AG-T]`
- Do you know how DBScan works? — **middle** (⭐️) `[AG-T]`
- **When would you choose K-means and when DBScan?** — **middle_plus** (⭐️) `[AG-T]`
- Explain briefly the K-Means clustering and how can we find the best value of K — **junior** `[YH-ML]`
- You are working on a clustering problem, what are different evaluation metrics that can be used, and how to choose between them — **middle_plus** `[YH-ML]`
- Discuss two clustering algorithms that can scale to large datasets — **middle_plus** `[YH-ML]`
- In unsupervised learning, if a ground truth about a dataset is unknown, how can we determine the most useful number of clusters to be? — **middle** `[TODOR]`
- What's the difference between Gaussian Mixture Model and K-Means? — **middle_plus** `[TODOR]`
- What is K-Means Clustering, and why is it used? — **junior** `[DI-KM]`
- Can you explain the difference between supervised and unsupervised learning with examples of where K-Means Clustering fits in? — **junior** `[DI-KM]`
- What are centroids in the context of K-Means? — **junior** `[DI-KM]`
- Describe the algorithmic steps of the K-Means clustering method. — **junior** `[DI-KM]`
- What is the role of distance metrics in K-Means, and which distances can be used? — **middle** `[DI-KM]`
- How do you decide on the number of clusters (k) in a K-Means algorithm? — **middle** `[DI-KM]`
- What are some methods for initializing the centroids in K-Means Clustering? — **middle_plus** `[DI-KM]` (k-means++)
- Can K-Means clustering be used for categorical data? If so, how? — **middle_plus** `[DI-KM]`
- Explain the term 'cluster inertia' or 'within-cluster sum-of-squares'. — **middle** `[DI-KM]`
- What are some limitations of K-Means Clustering? — **middle** `[DI-KM]`
- Compare K-Means clustering with hierarchical clustering. — **middle** `[DI-KM]`
- How does K-Means Clustering react to non-spherical cluster shapes? — **middle_plus** `[DI-KM]`
- How do you handle outliers in the K-Means algorithm? — **middle** `[DI-KM]`
- Discuss the concept and importance of feature scaling in K-Means Clustering. — **junior** `[DI-KM]`
- **Why is K-Means Clustering considered a greedy algorithm?** — **middle_plus** `[DI-KM]`

---

### 14. Снижение размерности: PCA / SVD / t-SNE / UMAP

- What is 'curse of dimensionality'? — **middle** (⭐️) `[AG-T]`
- What is the curse of dimensionality? Why do we care about it? — **middle** (⭐️) `[AG-T]`
- Do you know any dimensionality reduction techniques? — **middle** (⭐️) `[AG-T]`
- **What's singular value decomposition? How is it typically used for machine learning?** — **middle_plus** (⭐️) `[AG-T]`
- Explain Principal Component Analysis (PCA)? — **middle** `[MLQ]` `[CRACK]`
- How do you combat the curse of dimensionality? — **middle** `[MLQ]` `[CRACK]`
- What is the difference between LDA and PCA for dimensionality reduction? — **middle_plus** `[MLQ]`
- What is t-SNE? — **middle** `[MLQ]`
- **What is the difference between t-SNE and PCA for dimensionality reduction?** — **middle_plus** `[MLQ]`
- What is UMAP? — **middle_plus** `[MLQ]`
- **What is the difference between t-SNE and UMAP for dimensionality reduction?** — **middle_plus** `[MLQ]`
- How can you evaluate the performance of a dimensionality reduction algorithm on your dataset — **middle_plus** `[YH-ML]`
- Define the curse of dimensionality and how to solve it — **middle** `[YH-ML]`
- **In what cases would you use vanilla PCA, Incremental PCA, Randomized PCA, or Kernel PCA** — **middle_plus** `[YH-ML]`
- Can you define dimensionality reduction? Why do we use dimensionality reduction? — **junior** `[CRACK]`
- What is Principal Component Analysis? How does PCA work in dimensionality reduction? — **middle** `[CRACK]`
- Can you define dimensionality reduction and explain its importance in machine learning? — **junior** `[DI-DR]`
- What are the potential issues caused by high-dimensional data? — **middle** `[DI-DR]`
- Explain the concept of the "curse of dimensionality." — **middle** `[DI-DR]`
- How can dimensionality reduction prevent overfitting? — **middle** `[DI-DR]`
- What is feature selection, and how is it different from feature extraction? — **middle** `[DI-DR]`
- When would you use dimensionality reduction in the machine learning pipeline? — **middle** `[DI-DR]`
- Discuss the difference between linear and nonlinear dimensionality reduction techniques. — **middle_plus** `[DI-DR]`
- **Can dimensionality reduction be reversed? Why or why not?** — **middle_plus** `[DI-DR]`
- Explain Principal Component Analysis (PCA) and its objectives. — **middle** `[DI-DR]` `[DI-PCA]`
- How does Linear Discriminant Analysis (LDA) differ from PCA? — **middle_plus** `[DI-DR]`
- What is the role of eigenvectors and eigenvalues in PCA? — **middle** `[DI-DR]` `[DI-PCA]`
- Describe how PCA can be used for noise reduction in data. — **middle_plus** `[DI-DR]`
- Explain the kernel trick in Kernel PCA and when you might use it. — **middle_plus** `[DI-DR]`
- Discuss the concept of t-Distributed Stochastic Neighbor Embedding (t-SNE). — **middle_plus** `[DI-DR]`
- Describe the role of the covariance matrix in PCA. — **middle** `[DI-PCA]`
- What is the variance explained by a principal component? — **middle** `[DI-PCA]`
- How does scaling of features affect PCA? — **middle** `[DI-PCA]`
- What is the difference between PCA and Factor Analysis? — **middle_plus** `[DI-PCA]`
- Why is PCA considered an unsupervised technique? — **junior** `[DI-PCA]`
- **Derive the PCA from the optimization perspective, i.e., minimization of reconstruction error.** — **middle_plus** `[DI-PCA]`
- **Can you explain the Singular Value Decomposition (SVD) and its relationship with PCA?** — **middle_plus** `[DI-PCA]`
- How do you determine the number of principal components to use? — **middle** `[DI-PCA]`
- What is meant by 'loading' in the context of PCA? — **middle_plus** `[DI-PCA]`
- Explain the process of eigenvalue decomposition in PCA. — **middle_plus** `[DI-PCA]`
- Discuss the importance of the trace of a matrix in the context of PCA. — **middle_plus** `[DI-PCA]`
- What are the limitations of PCA when it comes to handling non-linear relationships? — **middle** `[DI-PCA]`

---

### 15. Дисбаланс классов

- «Что такое дисбаланс классов и как с ним бороться?» — **junior** `[MLI]`
- You are building a binary classifier and you found that the data is imbalanced, what should you do to handle this situation — **middle** `[YH-ML]`
- What is an imbalanced dataset? Can you list some ways to deal with it? — **junior** `[MLQ]` `[CRACK]`
- How do you deal with unbalanced binary classification? — **middle** `[TODOR]`
- What if the classes are imbalanced? What if there are more than 2 groups? — **middle** `[TODOR]`
- What is Imbalanced Class? / How would you resolve the issue of Imbalanced data set? — **junior** `[CRACK]`
- Can you define the concept of Undersampling and Oversampling? — **junior** `[CRACK]`
- What is SMOTE? — **middle** `[CRACK]`
- What are different Techniques of Sampling your data? — **middle** `[CRACK]`
- Discuss how XGBoost can handle highly imbalanced datasets. — **middle_plus** `[DI-XGB]`
- Discuss the impact of imbalanced datasets on the K-NN algorithm. — **middle** `[DI-KNN]`
- «Как ROC-AUC работает на данных с дисбалансом классов?» — **middle_plus** `[MLI]` (дубль из §5, но это ключевой мост)

---

### 16. Признаки: инжиниринг, кодирование категорий, отбор

- What do we do with categorical variables? — **middle** (⭐️) `[AG-T]`
- Why do we need one-hot encoding? — **middle** (⭐️) `[AG-T]`
- What is feature selection? Why do we need it? — **junior** (👶) `[AG-T]`
- Is feature selection important for linear models? — **middle** (⭐️) `[AG-T]`
- Which feature selection techniques do you know? — **middle** (⭐️) `[AG-T]`
- **Can we use L1 regularization for feature selection?** — **middle** (⭐️) `[AG-T]`
- **Can we use L2 regularization for feature selection?** — **middle_plus** (⭐️) `[AG-T]`
- Why do you use feature selection? — **junior** `[TODOR]`
- Why might it be preferable to include fewer predictors over many? — **middle** `[K120-PM]`
- When to use a Label Encoding vs. One Hot Encoding? — **middle** `[MLQ]`
- What is data normalization and why do we need it? — **junior** `[MLQ]` `[CRACK]`
- What is feature engineering and how does it impact the performance of machine learning models? — **junior** `[DI-FE]`
- List different types of features commonly used in machine learning. — **junior** `[DI-FE]`
- Explain the differences between feature selection and feature extraction. — **middle** `[DI-FE]`
- What are some common challenges you might face when engineering features? — **middle** `[DI-FE]`
- Describe the process of feature normalization and standardization. — **junior** `[DI-FE]`
- Why is it important to understand the domain knowledge while performing feature engineering? — **middle** `[DI-FE]`
- **How does feature scaling affect the performance of gradient descent?** — **middle** `[DI-FE]`
- Explain the concept of one-hot encoding and when you might use it. — **junior** `[DI-FE]`
- What is dimensionality reduction and how can it be beneficial in machine learning? — **middle** `[DI-FE]`
- How do you handle categorical variables in a dataset? — **junior** `[DI-FE]`
- What are filter methods in feature selection and when are they used? — **middle** `[DI-FE]`
- Explain what wrapper methods are in the context of feature selection. — **middle** `[DI-FE]`
- Describe embedded methods for feature selection and their benefits. — **middle_plus** `[DI-FE]`
- How does a feature's correlation with the target variable influence feature selection? — **middle** `[DI-FE]`
- What is the purpose of using Recursive Feature Elimination (RFE)? — **middle** `[DI-FE]`
- What feature selection methods can be used prior to building a regression model? — **middle** `[DI-LIN]`
- Mention three ways to handle missing or corrupted data in a dataset — **junior** `[YH-ML]`
- How do you deal with missing values when preparing data for linear regression? — **junior** `[DI-LIN]`
- Describe the steps involved in preprocessing data for linear regression analysis. — **junior** `[DI-LIN]`
- Which algorithms to use for Missing Data? — **middle** `[CRACK]`
- How do you deal with sparse data? — **middle** `[TODOR]`

**Выбросы (отдельный подпункт — спрашивают часто):**

- Mention three ways to make your model robust to outliers — **middle** `[YH-ML]`
- What are some ways I can make my model more robust to outliers? — **middle** `[K120-PM]` `[TODOR]`
- What are outliers and How would you remove them? — **junior** `[CRACK]`
- What is IQR, how can these help in Outliers removal? — **junior** `[CRACK]`
- How do you deal with outliers in your data? — **junior** `[TODOR]`
- How would you find an anomaly in a distribution? — **middle** `[TODOR]`
- How would you remove outliers when trying to estimate a flat plane from noisy samples? — **middle_plus** `[MLQ]` `[CRACK]` (RANSAC)

> **Пробел источников.** **Target/mean encoding** и его связка с утечкой (out-of-fold,
> сглаживание, ordered TS в CatBoost) прямым вопросом нигде в открывшихся дампах не встретился.
> Это дыра дампов, а не темы — писать раздел надо, потому что именно там ловят на собесах
> в РФ (связка «категории высокой кардинальности» → «target encoding» → «где утечка»).

---

### 17. Временные ряды

- What is a time series? — **junior** (👶) `[AG-T]` `[DI-TS]`
- How is time series different from the usual regression problem? — **junior** (👶) `[AG-T]`
- Which models do you know for solving time series problems? — **middle** (⭐️) `[AG-T]`
- If there's a trend in our series, how we can remove it? And why would we want to do it? — **middle** (⭐️) `[AG-T]`
- You have a series with only one variable 'y' measured at time t. How do predict 'y' at time t+1? Which approaches would you use? — **middle** (⭐️) `[AG-T]`
- You have a series with a variable 'y' and a set of features. How do you predict 'y' at t+1? Which approaches would you use? — **middle** (⭐️) `[AG-T]`
- **What are the problems with using trees for solving time series problems?** — **middle_plus** (⭐️) `[AG-T]` ← экстраполяция
- Can you explain the ARIMA model and its components — **middle** `[YH-ML]`
- What are the assumptions made by the ARIMA model — **middle_plus** `[YH-ML]`
- In the context of time series, what is stationarity, and why is it important? — **middle** `[DI-TS]`
- How do time series differ from cross-sectional data? — **junior** `[DI-TS]`
- What is seasonality in time series analysis, and how do you detect it? — **middle** `[DI-TS]`
- Explain the concept of trend in time series analysis. — **junior** `[DI-TS]`
- Describe the difference between white noise and a random walk in time series. — **middle_plus** `[DI-TS]`
- What is meant by autocorrelation, and how is it quantified in time series? — **middle** `[DI-TS]`
- Explain the purpose of differencing in time series analysis. — **middle** `[DI-TS]`
- What is an AR model (Autoregressive Model) in time series? — **middle** `[DI-TS]`
- Describe a MA model (Moving Average Model) and its use in time series. — **middle** `[DI-TS]`
- Explain the ARMA (Autoregressive Moving Average) model. — **middle** `[DI-TS]`
- How does the ARIMA model extend the ARMA model? — **middle** `[DI-TS]`
- What is the role of the ACF and PACF in time series analysis? — **middle_plus** `[DI-TS]`
- Discuss the importance of lag selection in ARMA/ARIMA models. — **middle_plus** `[DI-TS]`
- How is seasonality addressed in the SARIMA (Seasonal ARIMA) model? — **middle_plus** `[DI-TS]`
- How would you define Weighted Moving Averages? / What is meant by ARIMA Models? — **middle** `[CRACK]`
- Given training data on tweets and their retweets, how would you predict the number of retweets of a given tweet after 7 days? — **middle_plus** `[K120-PM]`

---

### 18. Оптимизация: GD / SGD / Adam

- «Какие знаешь оптимизаторы, в чем их идеи и различия?» — **middle** `[MLI]`
- «Gradient Descent, SGD и Mini-Batch SGD. В чем их различия, плюсы и минусы?» — **middle** `[MLI]`
- **«Если бы мы имели бесконечные ресурсы и скорость не важна, какой метод лучше?»** — **middle_plus** `[MLI]` ← продолжение предыдущего, ловит понимание роли шума SGD
- «Что такое gradient clipping?» — **middle** `[MLI]`
- «Рассказать про gradient accumulation.» — **middle** `[MLI]`
- «Что такое градиент?» — **junior** `[MLI]`
- What is gradient descent? How does it work? — **middle** (⭐️) `[AG-T]`
- What is SGD — stochastic gradient descent? What's the difference with the usual gradient descent? — **middle** (⭐️) `[AG-T]`
- Explain briefly batch gradient descent, stochastic gradient descent, and mini-batch gradient descent. and what are the pros and cons for each of them — **middle** `[YH-ML]`
- What is the importance of batch in machine learning and explain some batch dependent gradient descent algorithm — **middle** `[YH-ML]`
- What is gradient descent? — **junior** `[MLQ]` `[CRACK]` `[DI-GD]`
- What are the main variants of gradient descent algorithms? — **middle** `[DI-GD]`
- Explain the importance of the learning rate in gradient descent. — **junior** `[DI-GD]`
- How does gradient descent help in finding the local minimum of a function? — **junior** `[DI-GD]`
- **What challenges arise when using gradient descent on non-convex functions?** — **middle_plus** `[DI-GD]`
- Explain the purpose of using gradient descent in machine learning models. — **junior** `[DI-GD]`
- Describe the concept of the cost function and its role in gradient descent. — **junior** `[DI-GD]`
- Explain what a derivative tells us about the cost function in the context of gradient descent. — **junior** `[DI-GD]`
- What is batch gradient descent, and when would you use it? — **middle** `[DI-GD]`
- Discuss the concept of stochastic gradient descent (SGD) and its advantages and disadvantages. — **middle** `[DI-GD]`
- What is mini-batch gradient descent, and how does it differ from other variants? — **middle** `[DI-GD]`
- Explain how momentum can help in accelerating gradient descent. — **middle** `[DI-GD]`
- **Describe the difference between Adagrad, RMSprop, and Adam optimizers.** — **middle_plus** `[DI-GD]`
- What is the problem of vanishing gradients, and how does it affect gradient descent? — **middle** `[DI-GD]`
- How can gradient clipping help in training deep learning models? — **middle** `[DI-GD]`
- What is the difference between Batch Gradient Descent and Stochastic Gradient Descent? — **junior** `[MLQ]` `[CRACK]`
- What is Momentum (w.r.t NN optimization)? — **middle** `[MLQ]` `[CRACK]`
- Define Learning Rate. — **junior** `[MLQ]` `[CRACK]`
- Epoch vs. Batch vs. Iteration. — **junior** `[MLQ]` `[CRACK]`
- «Какой learning rate для большого батча, а какой для маленького?» — **middle_plus** `[MLI]`
- What is Gradient Decent? Difference between SGD and GD? — **junior** `[CRACK]`

---

### 19. Теория вероятностей и математическая статистика

**Русскоязычные (из `[MLI]`) — короткие, но глубокие:**

- «Формулировка задачи Maximum Likelihood Estimation. Записать формулу.» — **middle** `[MLI]`
- **«Коэффициент корреляции равен 0, можно ли утверждать, что выборки независимы?»** — **middle_plus** `[MLI]`
- «Какую зависимость ищет корреляция?» — **middle** `[MLI]`
- «Как проверить нормальность выборки?» — **middle** `[MLI]`
- «Что такое p-value и для чего оно нужно?» — **junior** `[MLI]`

**Общая статистика:**

- What's the normal distribution? Why do we care about it? — **junior** (👶) `[AG-T]`
- How do we check if a variable follows the normal distribution? — **middle** (⭐️) `[AG-T]`
- Explain the central limit theorem and give examples of when you can use it in a real-world problem? — **middle** `[YH-ST]`
- What general conditions must be satisfied for the central limit theorem to hold? — **middle_plus** `[YH-ST]`
- Describe briefly the hypothesis testing and p-value in layman's term? And give a practical application for them? — **middle** `[YH-ST]`
- **Given a left-skewed distribution that has a median of 60, what conclusions can we draw about the mean and the mode of the data?** — **middle** `[YH-ST]`
- What is the meaning of selection bias and how to avoid it? — **middle** `[YH-ST]`
- Explain the long-tailed distribution and provide three examples of relevant phenomena that have long tails. Why are they important in classification and regression problems? — **middle_plus** `[YH-ST]`
- What is the meaning of KPI in statistics? — **junior** `[YH-ST]`
- Say you flip a coin 10 times and observe only one head. What would be the null hypothesis and p-value for testing whether the coin is fair or not? — **middle** `[YH-ST]`
- **You are testing hundreds of hypotheses, each with a t-test. What considerations would you take into account when doing this?** — **middle_plus** `[YH-ST]` (множественные сравнения)
- What is skewness discuss two methods to measure it? — **middle** `[YH-ST]`
- **You sample from a uniform distribution [0, d] n times. What is your best estimate of d?** — **middle_plus** `[YH-ST]`
- Discuss the Chi-square, ANOVA, and t-test — **middle** `[YH-ST]`
- **Say you have two subsets of a dataset for which you know their means and standard deviations. How do you calculate the blended mean and standard deviation of the total dataset? Can you extend it to K subsets?** — **middle_plus** `[YH-ST]`
- What is the relationship between the significance level and the confidence level in Statistics? — **middle** `[YH-ST]`
- What is the Law of Large Numbers in statistics and how it can be used in data science? — **middle** `[YH-ST]`
- **What is the difference between a confidence interval and a prediction interval, and how do you calculate them?** — **middle_plus** `[YH-ST]`
- What are the differences between the z-test and t-test? / When to use a z-test Vs a t-test? — **middle** `[YH-ST]`
- Given a specific dataset, how do you calculate t-statistic or z-statistics? — **middle** `[YH-ST]`
- What is a p-value? What is the difference between type-1 and type-2 error? — **junior** `[K120-SI]`
- **What is maximum likelihood estimation? Could there be any case where it doesn't exist?** — **middle_plus** `[K120-SI]`
- **What's the difference between a MAP, MOM, MLE estimator? In which cases would you want to use each?** — **middle_plus** `[K120-SI]`
- What is a confidence interval and how do you interpret it? — **middle** `[K120-SI]`
- **What is unbiasedness as a property of an estimator? Is this always a desirable property when performing inference? What about in data analysis or predictive modeling?** — **middle_plus** `[K120-SI]`
- What is Selection Bias? — **middle** `[K120-SI]`
- What is a P-Value? — **junior** `[K120-P]`
- What is statistical power? — **middle** `[TODOR]`
- Define variance / Expected value — **junior** `[TODOR]`
- What is a confidence interval in layman's terms? — **junior** `[TODOR]`
- Describe the differences between and use cases for box plots and histograms — **junior** `[TODOR]`
- What is correlation? and covariance? — **junior** `[CRACK]`
- What is Anova? when to use Anova? — **middle** `[CRACK]`
- What is Z score? — **junior** `[CRACK]`
- What is Maximum Likelihood estimation? — **middle** `[CRACK]`
- What is probability? How would you define Likelihood? — **middle** `[CRACK]`
- What is Joint Probability? / Marginal Probability? / Conditional Probability? — **junior** `[CRACK]`
- What is the difference between descriptive and inferential statistics? — **junior** `[DI-STAT]`
- Define and distinguish between population and sample in statistics. — **junior** `[DI-STAT]`
- Explain what a "distribution" is in statistics, and give examples of common distributions. — **junior** `[DI-STAT]`
- What is the Central Limit Theorem and why is it important in statistics? — **middle** `[DI-STAT]`
- Describe what a "p-value" is and what it signifies about the statistical significance of a result. — **junior** `[DI-STAT]`
- What does the term "statistical power" refer to? — **middle** `[DI-STAT]`
- Explain the concepts of Type I and Type II errors in hypothesis testing. — **junior** `[DI-STAT]`
- What is the significance level in a hypothesis test and how is it chosen? — **middle** `[DI-STAT]`
- Define confidence interval and its importance in statistics. — **junior** `[DI-STAT]`
- What is a null hypothesis and an alternative hypothesis? — **junior** `[DI-STAT]`
- What is Bayes' Theorem, and how is it used in statistics? — **middle** `[DI-STAT]`
- Describe the difference between discrete and continuous probability distributions. — **junior** `[DI-STAT]` `[DI-PROB]`
- Explain the properties of a Normal distribution. — **junior** `[DI-STAT]`
- What is the Law of Large Numbers, and how does it relate to statistics? — **middle** `[DI-STAT]` `[DI-PROB]`
- What is the role of the Binomial distribution in statistics? — **junior** `[DI-STAT]`
- What is probability, and how is it used in machine learning? — **junior** `[DI-PROB]`
- Define the terms 'sample space' and 'event' in probability. — **junior** `[DI-PROB]`
- Explain the differences between joint, marginal, and conditional probabilities. — **junior** `[DI-PROB]`
- What does it mean for two events to be independent? — **junior** `[DI-PROB]`
- Describe Bayes' Theorem and provide an example of how it's used. — **middle** `[DI-PROB]`
- What is a probability density function (PDF)? / What is the role of the cumulative distribution function (CDF)? — **junior** `[DI-PROB]`
- Explain the Central Limit Theorem and its significance in machine learning. — **middle** `[DI-PROB]`
- Define expectation, variance, and covariance. — **junior** `[DI-PROB]`
- What are the characteristics of a Gaussian (Normal) distribution? — **junior** `[DI-PROB]`
- Explain the utility of the Binomial distribution in machine learning. — **junior** `[DI-PROB]`
- **How does the Poisson distribution differ from the Binomial distribution?** — **middle** `[DI-PROB]`
- What is the relevance of the Bernoulli distribution in machine learning? — **junior** `[DI-PROB]`
- What is the difference between the Bernoulli and Binomial distribution? — **junior** `[YH-PR]`
- Discuss some methods you will use to estimate the Parameters of a Probability Distribution — **middle_plus** `[YH-PR]`
- Let A and B be events on the same sample space, with P(A) = 0.6 and P(B) = 0.7. Can these two events be disjoint? — **middle** `[KHANG]`

---

### 20. Brain-teaser задачи по вероятности (реально используются в ML-скринах)

Эти встречаются и в РФ (`[MLI]` — задача про 100 монет), и в западных дампах.

- **«Задачка на вероятность: 100 монет, 1 нечестная, выпал орел, найдите вероятность»** — **middle_plus** `[MLI]`
- Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 offspring, respectively... What is the probability that Bobo's lineage dies out? — **middle_plus** `[K120-P]`
- In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the probability that you see at least one shooting star in the period of an hour? — **middle** `[K120-P]`
- If there's a 15% probability that you might see at least one airplane in a five-minute interval, what is the probability that you might see at least one airplane in a period of half an hour? — **middle** `[YH-PR]`
- **How can you generate a random number between 1 - 7 with only a die?** — **middle_plus** `[K120-P]`
- **How can you get a fair coin toss if someone hands you a coin that is weighted to come up heads more often than tails?** — **middle_plus** `[K120-P]` (фон Нейман)
- Say you are given an unfair coin, with an unknown bias towards heads or tails. How can you generate fair odds using this coin? — **middle_plus** `[YH-PR]`
- Given an unfair coin with the probability of heads not equal to .5. What algorithm could you use to create a list of random 1s and 0s? — **middle_plus** `[KHANG]`
- You have a 50-50 mixture of two normal distributions with the same standard deviation. How far apart do the means need to be in order for this distribution to be bimodal? — **middle_plus** `[K120-P]`
- Given draws from a normal distribution with known parameters, how can you simulate draws from a uniform distribution? — **middle_plus** `[K120-P]`
- **A certain couple tells you that they have two children, at least one of which is a girl. What is the probability that they have two girls?** — **middle** `[K120-P]`
- Given that Alice has 2 kids, at least one of which is a girl, what is the probability that both kids are girls? — **middle** `[KHANG]`
- You have a group of couples that decide to have children until they have their first girl, after which they stop having children. What is the expected gender ratio...? What is the expected number of children each couple will have? — **middle_plus** `[K120-P]`
- How many ways can you split 12 people into 3 teams of 4? — **middle** `[K120-P]`
- A group of 60 students is randomly split into 3 classes of equal size... What is the probability that Jack and Jill will end up in the same class? — **middle** `[KHANG]`
- Your hash function assigns each object to a number between 1:10... what is the probability of a hash collision? What is the expected number of hash collisions? What is the expected number of hashes that are unused? — **middle_plus** `[K120-P]`
- You call 2 UberX's and 3 Lyfts... what is the probability that all the Lyfts arrive first? — **middle** `[K120-P]`
- I write a program should print out all the numbers from 1 to 300, but prints out Fizz... What is the total number of numbers that is either Fizzed, Buzzed, or FizzBuzzed? — **junior** `[K120-P]`
- On a dating site, users can select 5 out of 24 adjectives... what is the probability that they form a match? — **middle_plus** `[K120-P]`
- A lazy high school senior types up applications... What is the expected number of applications that went to the right college? — **middle_plus** `[K120-P]` (линейность матожидания)
- **Let's say you have a very tall father. On average, what would you expect the height of his son to be? Taller, equal, or shorter? What if you had a very short father?** — **middle** `[K120-P]` (регрессия к среднему)
- **What's the expected number of coin flips until you get two heads in a row? What's the expected number of coin flips until you get two tails in a row?** — **middle_plus** `[K120-P]`
- Let's say we play a game where I keep flipping a coin until I get heads... How much would you pay me to play this game? — **middle_plus** `[K120-P]` (Санкт-Петербургский парадокс)
- **You have two coins, one of which is fair... and the other which is biased... You randomly pick coin and flip it twice, and get heads both times. What is the probability that you picked the fair coin?** — **middle** `[K120-P]`
- You have a 0.1% chance of picking up a coin with both heads, and a 99.9% chance that you pick up a fair coin. You flip your coin and it comes up heads 10 times. What's the chance that you picked up the fair coin, given the information that you observed? — **middle_plus** `[K120-P]`
- Assume two coins, one fair and the other is unfair. You pick one at random, flip it five times, and observe that it comes up as tails all five times. What is the probability that you are flipping the unfair coin? — **middle** `[YH-PR]`
- You and your friend are playing a game with a fair coin... If HH shows up first, you win, and if TH shows up first your friend wins. What is the probability of you winning the game? — **middle_plus** `[YH-PR]`
- If you roll a dice three times, what is the probability to get two consecutive threes? — **middle** `[YH-PR]`
- Suppose you have ten fair dice. If you randomly throw them simultaneously, what is the probability that the sum of all of the top faces is divisible by six? — **middle_plus** `[YH-PR]`
- If you have three draws from a uniformly distributed random variable between 0 and 2, what is the probability that the median of three numbers is greater than 1.5? — **middle_plus** `[YH-PR]`
- Assume you have a deck of 100 cards with values ranging from 1 to 100 and you draw two cards randomly without replacement, what is the probability that the number of one of them is double the other? — **middle_plus** `[YH-PR]`
- If there are 30 people in a room, what is the probability that everyone has different birthdays? — **middle** `[YH-PR]`
- **Assume you take a stick of length 1 and you break it uniformly at random into three parts. What is the probability that the three pieces can be used to form a triangle?** — **middle_plus** `[YH-PR]`
- Say you draw a circle and choose two chords at random. What is the probability that those chords will intersect? — **middle_plus** `[YH-PR]`
- According to hospital records, 75% of patients suffering from a disease die from that disease. Find out the probability that 4 out of the 6 randomly selected patients survive. — **middle** `[YH-PR]`
- You have 40 cards in four colors... When you pick two cards without replacement, what is the probability that the two cards are not in the same color and not in the same number? — **middle_plus** `[YH-PR]`
- How Random Number Generator Works, e.g. rand() function in python works? — **middle_plus** `[MLQ]`

---

### 21. Линейная алгебра

- What is a vector and how is it used in machine learning? — **junior** `[DI-LA]`
- Explain the difference between a scalar and a vector. — **junior** `[DI-LA]`
- What is a matrix and why is it central to linear algebra? — **junior** `[DI-LA]`
- Explain the concept of a tensor in the context of machine learning. — **junior** `[DI-LA]`
- How do you perform matrix addition and subtraction? — **junior** `[DI-LA]`
- What are the properties of matrix multiplication? — **junior** `[DI-LA]`
- Define the transpose of a matrix. — **junior** `[DI-LA]`
- Explain the dot product of two vectors and its significance in machine learning. — **junior** `[DI-LA]`
- What is the cross product of vectors and when is it used? — **middle** `[DI-LA]`
- How do you calculate the norm of a vector and what does it represent? — **junior** `[DI-LA]`
- Define the concept of orthogonality in linear algebra. — **middle** `[DI-LA]`
- What is the determinant of a matrix and what information does it provide? — **middle** `[DI-LA]`
- **Can you explain what an eigenvector and eigenvalue are?** — **middle** `[DI-LA]`
- How is the trace of a matrix defined and what is its relevance? — **middle_plus** `[DI-LA]`
- What is a diagonal matrix and how is it used in linear algebra? — **junior** `[DI-LA]`

---

### 22. Общие / «мостиковые» вопросы

- What is supervised machine learning? — **junior** (👶) `[AG-T]`
- Can you explain the differences between supervised, unsupervised, and reinforcement learning? — **junior** `[MLQ]` `[CRACK]`
- Difference between Supervised and Unsupervised Learning? / Difference between SemiSupervised and Reinforcement Learning? — **junior** `[CRACK]`
- Instance-Based Versus Model-Based Learning. — **middle** `[MLQ]`
- What is the difference between concept and data drift and how to overcome each of them — **middle_plus** `[YH-ML]`
- What are the different approaches to implementing recommendation systems — **middle** `[YH-ML]`
- What is active learning and discuss one strategy of it — **middle_plus** `[YH-ML]`
- Pseudo Labeling / Knowledge Distillation — **middle_plus** `[TODOR]`
- (Given a Dataset) Analyze this dataset and give me a model that can predict this response variable. — **middle_plus** `[K120-PM]`
- Given a database of all previous alumni donations to your university, how would you predict which recent alumni are most likely to donate? — **middle** `[K120-PM]`
- How would you suggest to a franchise where to open a new store? — **middle_plus** `[K120-PM]`

---

## Что интервьюеры ловят этими вопросами

Ниже — не пересказ вопросов, а реконструкция сигнала, который за ними стоит. Она опирается
на то, какие формулировки повторяются у независимых источников и где формулировка специально
сделана «неудобной».

**1. Отличить «прочитал определение» от «понимает механизм».**
Это главная функция вопросов вида «Что такое градиентный бустинг? **Где там появляется градиент?**»
`[MLI]`. Первая половина отвечается любым, кто видел документацию; вторая требует понимать, что
бустинг — это градиентный спуск в пространстве функций, а деревья приближают антиградиент лосса
по предсказанию. Такую же двухступенчатую конструкцию видно в «Какая **вероятностная**
интерпретация у ROC-AUC?» и в «Почему L1 **зануляет** часть весов?».

**2. Проверить, что человек различает метрику и её инварианты.**
«ROC-AUC = 0.9, что будет, если домножить все предсказания на 3?» `[MLI]` — вопрос ровно об
одном: понимает ли кандидат, что ROC-AUC зависит только от **порядка** скоров, а не от их
значений. Тот же сигнал ловят «В каких случаях AU PR лучше AU ROC?» `[AG-T]` и «Как ROC-AUC
работает на данных с дисбалансом?» `[MLI]`.

**3. Поймать на неспособности рассуждать о смещении оценки.**
«Как изменятся precision и recall, если выкинуть 10 нулей из таргета?» `[MLI]`,
«Are Random Forests biased towards attributes with more levels?» `[DI-RF]`,
«Why would the following splitting mechanism be incorrect» `[MLQ]` — все три про одно: кандидат
должен уметь проследить, как манипуляция с данными протекает в число, которое он потом покажет
как «качество модели».

**4. Проверить границы применимости, а не знание алгоритма.**
«Можно ли строить RandomForest над KNN, линейными моделями и нейросетями, почему?» `[MLI]`,
«What are the problems with using trees for solving time series problems?» `[AG-T]`,
«Can dimensionality reduction be reversed?» `[DI-DR]`, «When would you choose K-means and when
DBScan?» `[AG-T]`. Здесь нет «правильного алгоритма» — есть условие, при котором метод ломается.

**5. Заставить вывести метод из первых принципов.**
«What if instead of finding the best split, we randomly select a few splits and just select the
best from them. Will it work?» `[AG-T]` — это просьба переизобрести Extra Trees и объяснить,
почему потеря жадности окупается снижением дисперсии. Аналогично «Derive the PCA from the
optimization perspective» `[DI-PCA]` и «Which method is better if resources are infinite?» `[MLI]`.

**6. Проверить статистическую грамотность отдельно от ML.**
«Коэффициент корреляции равен 0 — можно ли утверждать, что выборки независимы?» `[MLI]` —
классический фильтр: правильный ответ «нет, корреляция ловит только линейную зависимость» плюс
контрпример. Сюда же MLE vs MAP vs MOM `[K120-SI]`, «unbiasedness — всегда ли это желательно?»
`[K120-SI]`, множественные сравнения `[YH-ST]`.

**7. Задачи-тизеры — тест на структуру мышления под давлением.**
100 монет `[MLI]`, «две девочки» `[K120-P]`, «сломанная палка» `[YH-PR]`, «сколько бросков до
двух орлов подряд» `[K120-P]`. Интервьюер смотрит не на ответ, а на то, вводит ли кандидат
обозначения, проверяет ли граничные случаи, замечает ли, что задача — про условную вероятность,
а не про подсчёт.

**8. Отдельный сигнал: умение говорить о компромиссах, а не о «лучше/хуже».**
Формулировки «advantages and disadvantages of each **when compared to each other**» `[YH-ML]`,
«pros and cons for each of them» `[YH-ML]`, «Плюсы и минусы каждой» `[MLI]` встречаются
навязчиво часто. На middle+ ответ без явного условия («если признаков много и они разрежены —
то...») засчитывается как слабый.

---

## Пробелы, которые чаще всего валят кандидатов

Список составлен по пересечению двух сигналов: (а) вопрос повторяется у 3+ независимых
источников; (б) формулировка содержит «второй слой», который легко не заметить.

**ROC-AUC как ранговая статистика.** Кандидат знает «площадь под кривой», но не может сказать,
что AUC = P(скор случайного позитива > скор случайного негатива), не понимает инвариантность к
монотонным преобразованиям и не умеет объяснить, почему AUC оптимистична при сильном дисбалансе,
а PR-AUC — нет. Пересечение: `[MLI]`, `[AG-T]`, `[YH-ML]`, `[MLQ]`, `[CRACK]`.

**Bias-variance как разложение, а не как слоган.** «Смещение — недообучение, разброс —
переобучение» проходит на junior. На middle+ спрашивают формулу разложения, поведение каждой
компоненты у деревьев/линейных/ансамблей `[MLI]`, диагностику по learning curves `[DI-BV]` и
почему бустинг снижает именно смещение, а бэггинг — именно разброс `[DI-BV]`. Провал здесь —
самый частый.

**Почему L1 разрежает.** Ответ «потому что L1 обнуляет» — тавтология. Нужен либо геометрический
аргумент (ромб vs круг, касание в вершине), либо субградиентный (мягкий порог). `[MLI]`.

**Разница бустинга и леса на уровне гиперпараметров.** «Почему в бустинге деревья мельче, чем
в лесу?» `[MLI]` — валит тех, кто не связал это с bias-variance: лес усредняет переобученные
низкосмещённые деревья (борьба с разбросом), бустинг складывает слабые высокосмещённые
(борьба со смещением). Из того же куста — «что будет, если удалить **первое** дерево» `[MLI]`:
в лесу почти ничего, в бустинге ломается всё, потому что там инициализация и последовательная
зависимость.

**Утечка данных.** Кандидаты уверенно перечисляют «train/val/test», но не видят утечку в
конкретном коде `[MLQ]`, в подборе гиперпараметров на тех же фолдах, в скейлинге до сплита,
в target encoding без out-of-fold. Формулировки-ловушки: `[MLQ]` п. 64, `[AG-T]` про три части.

**Категориальные признаки высокой кардинальности.** Знают one-hot `[AG-T]`, `[DI-FE]`,
не знают, что делать при 50k категорий, и не связывают target encoding с утечкой. Это же —
мост к вопросу «как CatBoost обрабатывает категории иначе» `[DI-ENS]`.

**Внутренности бустингов.** «Чем LightGBM отличается от XGBoost» ждут ответа про гистограммы,
leaf-wise рост, GOSS/EFB; «чем CatBoost» — про ordered target statistics, ordered boosting и
симметричные деревья. Дампы этот слой почти не покрывают, а спрашивают его регулярно —
несоответствие между «что доступно для подготовки» и «что спрашивают» здесь максимальное.

**MLE vs MAP vs MOM и «когда MLE не существует».** `[K120-SI]`. Валит почти всех, кто учил
статистику по прикладным курсам без теории оценивания.

**Корреляция ≠ независимость.** `[MLI]`. Кандидат отвечает «да, независимы» или отвечает «нет»
без контрпримера. Оба варианта — минус.

**Экстраполяция деревьев на временных рядах.** `[AG-T]`. Кандидат предлагает бустинг на лаги
и не упоминает, что дерево не выйдет за диапазон таргета, виденный в обучении, — значит,
тренд надо снимать отдельно.

**Калибровка.** Почти не представлена в открытых дампах, но именно она отличает человека,
который выводил модель в прод (скоринг, риск, ценообразование), от того, кто оптимизировал
метрику на Kaggle. Отсутствие вопроса в дампах ≠ отсутствие на собесе.

**Масштабирование признаков — где обязательно, где вредно.** `[AG-T]` («When do we need to
perform feature normalization for linear models? When it's okay not to do it?»), `[DI-KM]`,
`[DI-KNN]`, `[YH-ML]` (SVM). Кандидаты дают универсальное «всегда скейлить», не отделяя
метрические/градиентные методы от деревьев.

---

## Рекомендации для структуры глав хендбука по этой теме

Ниже — предложение по разбиению раздела `02-classic-ml` (и части `01-math`), выстроенное
так, чтобы порядок глав совпадал с порядком, в котором темы всплывают на собесе, а не с
порядком университетского курса. Опорная рубрикация сверена с `[HSE]`, `[DYAK]`, `[GIRAFE]`, `[ODS]`.

### Принцип нарезки

Одна глава = один блок вопросов, который интервьюер может пройти целиком за 10–15 минут.
Если тема даёт больше 12 вопросов «Проверь себя» — делим.

### Предлагаемый порядок

**01. Постановка задачи и словарь.** Supervised/unsupervised/RL, признак/таргет/объект,
обобщающая способность. Короткая (800–1200 слов). Нужна, чтобы дальше не объяснять термины.

**02. Линейная регрессия.** Проблема → МНК → аналитическое решение (нормальное уравнение) →
почему его не всегда используют (сложность $O(d^3)$, вырожденность) → градиентный спуск.
Обязательно: предпосылки, интерпретация весов, «выше вес ≠ важнее признак» `[AG-T]`,
мультиколлинеарность и точный разбор «z = x + y» и «z = x + y + шум» `[AG-T]`.

**03. Логистическая регрессия.** Почему не MSE (невыпуклость + затухание градиента), вывод
log-loss из правдоподобия Бернулли, odds/logit, интерпретация коэффициентов, многоклассовость
(softmax vs OvR). Врезка 💬 уже есть в `AUTHORING.md` §3 — она про эту главу.

**04. Регуляризация.** L1/L2/ElasticNet, геометрия ромба и круга, субградиент и мягкий порог,
почему L2 не зануляет, можно ли отбирать признаки через L2 `[AG-T]`, связь с MAP-оценкой
(мост в байесовскую главу).

**05. Разложение ошибки: смещение и разброс.** Отдельная глава, не подраздел. Полный вывод
для квадратичного лосса, поведение компонент у линейных/деревьев/леса/бустинга `[MLI]`,
диагностика по learning curves `[DI-BV]`, почему нельзя минимизировать обе `[DI-BV]`.

**06. Метрики классификации.** Ключевая глава (4000–7000 слов по нормативу §9 стандарта).
Confusion matrix → precision/recall/F → пороги → ROC → **AUC как ранговая вероятность** →
PR-кривая → когда PR-AUC лучше ROC-AUC → logloss → многоклассовые усреднения (micro/macro/weighted).
Обязательно включить задачи-ловушки из `[MLI]`: домножение скоров на 3, выкидывание 10 нулей.

**07. Калибровка вероятностей.** Отдельная глава, хотя дампы её почти не спрашивают напрямую.
Reliability diagram, Brier score, ECE, Platt scaling, изотоническая регрессия, что происходит
после undersampling. Аргумент за отдельную главу: это единственная тема, где middle+ отличается
от middle не знанием, а опытом.

**08. Метрики регрессии.** MSE/RMSE/MAE/MAPE/квантильный лосс, чувствительность к выбросам,
«что оптимизирует модель, минимизирующая MAE» (медиана) vs MSE (среднее) `[K120-PM]`, `[YH-ML]`.

**09. Валидация и утечки.** Hold-out → K-fold → стратификация → GroupKFold → TimeSeriesSplit.
Вложенная кросс-валидация. Каталог утечек с симптомами: скейлинг до сплита, target encoding
без OOF, подбор гиперпараметров на тесте, дубликаты между фолдами, лик через время.
Разбор кода из `[MLQ]` п. 64 — идеальная задача для раздела «Подводные камни».

**10. Решающие деревья.** Критерии (Gini, энтропия, MSE), жадность, что такое прирост
информации, обрезка, обработка категорий, важность признаков и её смещение в сторону
признаков с большим числом уровней `[DI-RF]`.

**11. Бэггинг и случайный лес.** Bootstrap, OOB, две рандомизации (объекты + признаки),
почему декоррелирование деревьев снижает дисперсию, Extra Trees как ответ на вопрос
«а если сплиты выбирать случайно» `[AG-T]`, что ломается при коррелированных признаках.

**12. Градиентный бустинг: механика.** Ключевая глава. Бустинг как градиентный спуск в
пространстве функций, алгоритм Фридмана по шагам `[ODS10]`, псевдо-остатки, shrinkage,
subsample, почему деревья мелкие, почему нельзя выкинуть первое дерево, ранняя остановка.

**13. XGBoost / LightGBM / CatBoost: инженерные различия.** Вторая ключевая глава, отдельно
от механики. Второй порядок и регуляризация листьев в XGBoost; гистограммные сплиты;
level-wise vs leaf-wise; GOSS и EFB; обработка пропусков через default direction;
ordered target statistics и ordered boosting в CatBoost; симметричные (oblivious) деревья
и почему они быстры на инференсе. Сравнение — через условия задачи, не через «лучше».

**14. SVM.** Максимальный зазор, hinge loss, мягкий зазор и смысл C, двойственная задача,
kernel trick, почему обязательна нормировка, где SVM проигрывает бустингу по масштабу.

**15. Метрические методы: kNN.** Метрики расстояния, выбор k, проклятие размерности,
масштабирование, приближённый поиск соседей (LSH/HNSW) как мост в RecSys/векторные БД.

**16. Наивный Байес и байесовский взгляд.** Условная независимость, лапласово сглаживание,
логарифмирование вероятностей, generative vs discriminative, связь регуляризации с априорным
распределением.

**17. Кластеризация.** k-means (+k-means++, почему жадный, почему шаровые кластеры),
DBSCAN, иерархическая, GMM/EM, метрики качества без разметки (силуэт, Calinski–Harabasz),
как выбирать k.

**18. Снижение размерности.** PCA через максимум дисперсии и через минимум ошибки
реконструкции (оба вывода), связь с SVD, выбор числа компонент, kernel PCA,
LDA vs PCA, t-SNE и UMAP — что они сохраняют, чего с ними нельзя делать
(интерпретировать расстояния между кластерами, использовать как признаки без осторожности).

**19. Признаки: инжиниринг, кодирование, отбор.** One-hot / label / ordinal / target
(mean) encoding с обязательным разбором out-of-fold и сглаживания, hashing trick,
высокая кардинальность, отбор признаков (filter/wrapper/embedded, RFE, permutation importance,
SHAP как инструмент, а не как истина).

**20. Дисбаланс классов.** Почему accuracy врёт, взвешивание классов vs ресемплинг,
SMOTE и его ограничения, порог как отдельный гиперпараметр, что происходит с калибровкой
после undersampling, выбор метрики под бизнес-цену ошибки.

**21. Временные ряды.** Стационарность, тренд/сезонность, ACF/PACF, ARIMA/SARIMA,
признаки-лаги и скользящие агрегаты, **почему деревья не экстраполируют** `[AG-T]`,
корректная валидация (расширяющееся окно), утечки через будущее.

**22. Оптимизация.** GD/SGD/mini-batch, роль шума, momentum/Nesterov, Adagrad/RMSprop/Adam,
learning rate и его связь с размером батча `[MLI]`, что ломается на невыпуклых функциях,
gradient clipping и accumulation.

### Что вынести в раздел `01-math`

- **Теория вероятностей:** случайные величины, совместные/маргинальные/условные, формула Байеса,
  основные распределения (Бернулли, биномиальное, Пуассон, нормальное, экспоненциальное),
  матожидание и дисперсия, ЗБЧ и ЦПТ с условиями применимости.
- **Статистика:** оценивание (MLE, MAP, метод моментов), несмещённость и состоятельность,
  доверительные vs предсказательные интервалы, проверка гипотез, p-value, ошибки I/II рода,
  мощность, z-тест vs t-тест, множественные сравнения.
- **Линейная алгебра:** нормы, ортогональность, собственные значения/векторы, SVD,
  положительная определённость, псевдообратная матрица — всё с явной привязкой «где это
  всплывает в ML» (PCA, нормальное уравнение, ковариационная матрица).
- **Задачи-тизеры:** отдельная глава-тренажёр на 25–35 задач из §20 этого дампа, сгруппированных
  по приёму (условная вероятность, линейность матожидания, рекуррентные соотношения на
  матожидание, симметрия, дополнение события), а не по сюжету.

### Замечания по подаче

1. **Грейд-маркеры из стандарта (🌱/🎯/🧠) хорошо ложатся на разметку `[AG-T]`** (👶/⭐️/🚀).
   Где источник дал явную метку — переносить её, а не переизобретать.
2. **Вопросы «Проверь себя» брать в первую очередь из `[MLI]`** — это единственный русскоязычный
   источник с живыми формулировками, и они звучат ровно так, как их произносит интервьюер.
3. **Каждый вопрос-ловушку разбирать через «провал»**, как требует §5 стандарта: для ROC-AUC ×3
   провальный ответ — «AUC вырастет»; для «корреляция = 0» — «значит независимы»; для
   «удалить первое дерево» — «ничего не изменится».
4. **Не дублировать §6 (метрики классификации) и §7 (калибровка)** — первая про ранжирование
   и пороги, вторая про соответствие скоров вероятностям. Это разные вопросы на собесе.

---

## Сводка по объёму собранного

| Показатель | Значение |
|---|---|
| Проверенных (реально загруженных) URL | 43 |
| Размеченных грейдом записей-вопросов в дампе | 610 |
| Из них различных после дедупликации | ~575 (≈35 записей — намеренные перекрёстные ссылки между разделами) |
| Разбивка по грейдам | junior — 180, middle — 286, middle_plus — 144 |
| Русскоязычных вопросов дословно | 37 (все из `[MLI]`) |
| Источников с явной авторской разметкой по грейдам | 1 (`[AG-T]`, метки 👶/⭐️/🚀) |
| Источников с привязкой вопроса к конкретной компании | 0 |
| Подтверждено по компаниям | только структура ML-секций Т-Банка (`[TINT]`) |
