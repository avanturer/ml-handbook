# Сводный список источников

> Собран автоматически из блоков «Что читать дальше» всех глав (`python tools/build_bibliography.py`).
> Это не список «прочитать всё» — это карта: у каждого источника указано, зачем его читать и после какой главы.

**Источников:** 334 · **глав с библиографией:** 41

## Как этим пользоваться

Читать источники до соответствующей главы обычно бесполезно: оригинальные статьи написаны для тех, кто уже знает контекст. Правильный порядок — глава, потом задачи, потом первоисточник. Тогда статья читается за полчаса вместо вечера, а в голове остаётся не пересказ, а понимание, чем работа отличается от предшественников.

---

## Старт

### [Как пользоваться хендбуком](../docs/00-start/01-how-to-use.md)

- [Треки обучения](02-tracks.md) — выберите маршрут под свою ситуацию. **Начните отсюда.**
- [Карта собеседования MLE](03-interview-map.md) — из чего состоит воронка и что спрашивают на каждом грейде.
- [Как учить, чтобы осталось в голове](04-study-method.md) — обоснование протокола из §5 и подробный разбор методики.
- [Глоссарий](05-glossary.md) — если по ходу встретился незнакомый термин.

### [Треки обучения](../docs/00-start/02-tracks.md)

- [Карта собеседования MLE](03-interview-map.md) — что именно спрашивают на каждой секции и каждом грейде.
- [Как учить, чтобы осталось в голове](04-study-method.md) — методика, на которой построены правила выше.
- [Оглавление](../index.md) — полная карта хендбука, если хотите собрать свой маршрут.

### [Карта собеседования MLE](../docs/00-start/03-interview-map.md)

- [Треки обучения](02-tracks.md) — выберите маршрут под свою ситуацию и приступайте.
- [Как учить, чтобы осталось в голове](04-study-method.md) — протокол работы с материалом.
- [Каркас ответа на ML System Design](../11-system-design/01-framework.md) — секция с наибольшим весом на middle+.
- [Процесс найма изнутри](../14-career/01-interview-process.md) — резюме, проекты, что делать между этапами и после отказа.

### [Как учить, чтобы осталось в голове](../docs/00-start/04-study-method.md)

- **Brown, Roediger, McDaniel. «Make It Stick: The Science of Successful Learning» (2014)** — лучшее популярное изложение всего, что описано в этой главе, от самих исследователей. Если читать одну книгу об обучении — эту.
- **Ericsson, Pool. «Peak: Secrets from the New Science of Expertise» (2016)** — про осознанную практику: как устроена работа над тем, что не получается.
- **Sweller, Ayres, Kalyuga. «Cognitive Load Theory» (2011)** — академическое изложение теории когнитивной нагрузки, включая эффект обращения экспертизы. Для тех, кому нужна строгость.
- **Работы Роберта Бьорка о desirable difficulties** (лаборатория Bjork Learning and Forgetting Lab, UCLA) — первоисточник по разнесению, перемешиванию и различию между обучением и сиюминутной продуктивностью.
- [Документация Anki](https://docs.ankiweb.net/) — если решите настроить систему повторений; достаточно раздела о колодах и о параметрах интервалов.

### [Глоссарий](../docs/00-start/05-glossary.md)

- [Оглавление](../index.md) — полная карта хендбука.
- [Треки обучения](02-tracks.md) — если непонятно, с какой стороны подступиться.

## Математика

### [Линейная алгебра для ML](../docs/01-math/01-linear-algebra.md)

- **Deisenroth M., Faisal A., Ong C. «Mathematics for Machine Learning»** — [mml-book.github.io](https://mml-book.github.io/), книга бесплатна в PDF. Главы 2–4 — ровно та линейная алгебра, что нужна MLE, с честными выводами и без физико-математической избыточности. Лучший «второй проход» после этой главы.
- **Strang G. «Linear Algebra and Learning from Data» (2019)** — книга специально про то, как линейная алгебра работает в ML: SVD, малоранговые приближения, рандомизированные методы. Читать после того, как базовые вещи уложились.
- [MIT 18.06 Linear Algebra (OpenCourseWare)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — курс Стрэнга целиком, с видео и задачами. Если геометрическая интуиция не появилась, лекции про четыре фундаментальных подпространства и про SVD закрывают этот пробел.
- **«The Matrix Cookbook» (Petersen, Pedersen)** — справочник матричных тождеств и производных, свободно доступен в PDF (ищется по названию). Не для чтения подряд: держать открытым, когда выводите формулу. Раздел 2 — производные, раздел 9 — специальные матрицы.
- [Hu E. et al. «LoRA: Low-Rank Adaptation of Large Language Models» (2021)](https://arxiv.org/abs/2106.09685) — первоисточник по низкоранговым адаптерам. Читать раздел 4 и эксперименты про выбор ранга: там же авторы измеряют, насколько «низкоранговым» на самом деле оказывается обновление.
- [Halko N., Martinsson P.-G., Tropp J. «Finding Structure with Randomness» (2009)](https://arxiv.org/abs/0909.4061) — рандомизированное SVD: как считать топ-$k$ компонент матрицы, которая не помещается в память. Это то, что стоит за `randomized_svd` в sklearn.
- [Документация `numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html) — прочитайте страницы `lstsq`, `cond`, `matrix_rank`, `pinv` целиком, включая раздел про `rcond`. Это пятнадцать минут, которые избавят от целого класса багов.

### [Теория вероятностей](../docs/01-math/02-probability.md)

- **Blitzstein J., Hwang J. «Introduction to Probability»** и сопровождающий её бесплатный курс Гарварда **Stat 110** (лекции и задачники выложены в открытый доступ, ищутся по названию курса). Лучший баланс строгости и интуиции; глава про условную вероятность и раздел с задачами-тизерами закрывают половину математической секции собеседования.
- **Bertsekas D., Tsitsiklis J. «Introduction to Probability»** (курс MIT 6.041) — более инженерный стиль, много про пуассоновские и марковские процессы. Брать, если нужна прикладная сторона: очереди, потоки событий, времена ожидания.
- **Wasserman L. «All of Statistics»** — компактно и плотно; главы 1–5 покрывают эту главу, дальше идёт [статистика](03-statistics.md). Подходит тем, кто уже знает основы и хочет систематизации, а не введения.
- [Документация `scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) — прочитайте раздел про интерфейс `rv_continuous`/`rv_discrete` и список распределений. Пятнадцать минут, после которых вы перестанете писать руками формулы плотностей и квантилей.
- **Kohavi R., Tang D., Xu Y. «Trustworthy Online Controlled Experiments» (2020)** — книга про A/B-тесты от людей, запускавших их в Microsoft и Amazon. Для этой главы важны разделы про зависимость наблюдений, про тяжёлые хвосты и про то, почему единица рандомизации и единица анализа должны совпадать.
- **Gigerenzer G. о натуральных частотах** — серия работ о том, что задачи вида «тест на редкую болезнь» решаются людьми в разы точнее, если переформулировать их в частотах вместо вероятностей. Полезно не как математика, а как приём коммуникации: так вы объясните продукту, почему у модели низкая precision.

### [Статистика и вывод](../docs/01-math/03-statistics.md)

- **Wasserman L. «All of Statistics» (Springer, 2004)** — компактный справочник по всему, что в этой главе: оценивание, MLE, бутстрап, проверка гипотез. Главы 6–10. Лучший вариант, если нужен один учебник и мало времени.
- **Casella G., Berger R. «Statistical Inference» (2nd ed.)** — если нужна строгость: полные доказательства свойств MLE, достаточные статистики, теория оптимальных критериев. Читать выборочно, главы 7 и 8.
- **Efron B., Tibshirani R. «An Introduction to the Bootstrap» (1993)** — первоисточник по бутстрапу от его автора; там же вывод BCa и честный разбор случаев, когда метод не работает.
- [Wasserstein R., Lazar N. «The ASA Statement on p-Values: Context, Process, and Purpose», *The American Statistician*, 2016](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108) — официальная позиция Американской статистической ассоциации: шесть принципов о том, чем p-value является и чем нет. Две страницы, которые стоит прочитать перед собеседованием.
- [Ioannidis J. «Why Most Published Research Findings Are False», *PLoS Medicine*, 2005](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124) — разбор того, как малая мощность, множественные сравнения и свобода в анализе превращают статистическую значимость в шум. Прямо переносится на A/B-тесты в продукте.
- **Kohavi R., Tang D., Xu Y. «Trustworthy Online Controlled Experiments» (Cambridge University Press, 2020)** — практический стандарт индустрии по A/B-тестам: дизайн, мощность, SRM, ловушки, культура принятия решений. Главы 17–19 — про статистику, остальное — про организацию процесса.
- **Deng A., Xu Y., Kohavi R., Walker T. «Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data» (WSDM 2013, Microsoft)** — статья про CUPED. Ищется по названию на сайте Microsoft Research; читать после того, как формула $n \propto \sigma^2$ станет для вас очевидной.
- **Benjamini Y., Hochberg Y. «Controlling the False Discovery Rate», *JRSS Series B*, 1995** — оригинальная статья про FDR. Стоит прочитать введение, чтобы понять, зачем вообще понадобилась величина, отличная от FWER.
- [Документация `scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) — список критериев с точными формулировками нулевых гипотез. Читать не как справочник функций, а как справочник **гипотез**: в описании каждой функции написано, что именно она проверяет.
- [Документация `statsmodels`: статистические тесты и поправки](https://www.statsmodels.org/stable/stats.html) — здесь живут `multipletests` (все поправки на множественность), тесты пропорций и расчёты мощности, которых нет в scipy.

## Классический ML

### [Постановка задачи обучения](../docs/02-classic-ml/01-learning-theory.md)

- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning»** — [сайт книги с бесплатным PDF](https://hastie.su.domains/ElemStatLearn/). Глава 2 — постановка задачи, байесовский предсказатель, проклятие размерности с теми самыми оценками про долю данных в окрестности; глава 7 — bias-variance, эффективное число степеней свободы, оценка обобщения. Основной источник для этой главы, читать обязательно на уровне middle+.
- **James, Witten, Hastie, Tibshirani. «An Introduction to Statistical Learning»** — [statlearning.com](https://www.statlearning.com/). Главы 2 и 5 — то же самое, но существенно мягче и с картинками. Если ESL идёт тяжело, начинайте отсюда.
- **Shalev-Shwartz S., Ben-David S. «Understanding Machine Learning: From Theory to Algorithms» (2014), главы 2–6** — аккуратное построение PAC-обучаемости, ERM, равномерной сходимости и VC-размерности. Для тех, кому нужны доказательства, а не пересказ.
- **Wolpert D. «The Lack of A Priori Distinctions Between Learning Algorithms», Neural Computation, 1996** — первоисточник no free lunch. Полезно прочитать хотя бы введение, чтобы видеть, насколько узки условия теоремы и как часто её пересказывают неверно.
- [Belkin M. et al. «Reconciling modern machine learning practice and the bias-variance trade-off» (2019)](https://arxiv.org/abs/1812.11118) — работа, зафиксировавшая двойной спуск. Читать после того, как разложение bias-variance уложилось: иначе легко сделать неверный вывод, что «классическая теория неверна».
- [scikit-learn: Validation curves и learning curves](https://scikit-learn.org/stable/modules/learning_curve.html) — практическая часть: как построить кривые обучения и как по ним ставить диагноз. Нужный инструмент для §8.
- [scikit-learn: Underfitting vs. Overfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html) — минимальный воспроизводимый пример с полиномами; хорошая отправная точка для задачи 1.

### [Линейная регрессия и регуляризация](../docs/02-classic-ml/02-linear-models.md)

- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», глава 3** — [сайт книги с бесплатным PDF](https://hastie.su.domains/ElemStatLearn/). Эталонное изложение: геометрия МНК, ридж через SVD и эффективные степени свободы, Lasso, LARS, сравнение методов сжатия. Именно на неё опирается эта глава; читать обязательно.
- **James, Witten, Hastie, Tibshirani. «An Introduction to Statistical Learning», глава 6** — [statlearning.com](https://www.statlearning.com/). Тот же материал без матричного анализа, с хорошими картинками ромба и круга. Если §8.1 не сложилась в голове — идите сюда.
- **Tibshirani R. «Regression Shrinkage and Selection via the Lasso», JRSS Series B, 1996** — первоисточник Lasso. Полезно ради постановки в форме ограничения и обсуждения, почему вершины ромба дают отбор признаков.
- **Zou H., Hastie T. «Regularization and Variable Selection via the Elastic Net», JRSS Series B, 2005** — откуда взялся ElasticNet и что такое эффект группировки; там же разбор ограничения Lasso «не больше $n$ признаков».
- **Friedman J., Hastie T., Tibshirani R. «Regularization Paths for Generalized Linear Models via Coordinate Descent», Journal of Statistical Software, 2010** — статья про glmnet. Содержит ровно тот координатный спуск, что реализован в §8.3, плюс приёмы вроде тёплого старта и активного множества. Читать, если хотите понимать, что происходит внутри `sklearn.linear_model`.
- [scikit-learn: Linear Models (User Guide)](https://scikit-learn.org/stable/modules/linear_model.html) — точные формулировки минимизируемых функционалов для `Ridge`, `Lasso`, `ElasticNet`. Обязательно свериться перед переносом гиперпараметров между библиотеками.
- [numpy.linalg.lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) — что именно возвращает функция при вырожденной матрице (решение минимальной нормы) и как работает параметр `rcond`. Мелочь, о которой спрашивают на практических секциях.

### [Логистическая регрессия](../docs/02-classic-ml/03-logistic-regression.md)

- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», раздел 4.4** — [сайт книги с бесплатным PDF](https://hastie.su.domains/ElemStatLearn/). Логистическая регрессия, вывод IRLS, сравнение с LDA и обсуждение того, когда порождающая модель выигрывает у различающей. Глава 18 — регуляризованная логистическая регрессия при $d \gg n$.
- **James, Witten, Hastie, Tibshirani. «An Introduction to Statistical Learning», глава 4** — [statlearning.com](https://www.statlearning.com/). Мягкое введение с примерами интерпретации коэффициентов через odds ratio; удачные иллюстрации того, почему линейная регрессия на метках плоха.
- **Bishop C. «Pattern Recognition and Machine Learning», разделы 4.3–4.5** — вывод IRLS во всех подробностях, softmax-регрессия, байесовская логистическая регрессия с лапласовским приближением. Лучший источник, если хочется полной математики.
- **Murphy K. «Probabilistic Machine Learning: An Introduction» (2022), глава 10** — современное изложение: связь с GLM, разбор нескольких оптимизаторов, разделимость и роль регуляризации.
- **Hosmer D., Lemeshow S., Sturdivant R. «Applied Logistic Regression»** — книга не про ML, а про статистическую практику: диагностика модели, интерпретация, проверка адекватности, работа с взаимодействиями. Полезна тем, кто строит скоринговые модели.
- **McMahan H. B. et al. «Ad Click Prediction: a View from the Trenches», KDD 2013** — как логистическую регрессию обучают в промышленных рекламных системах: FTRL-Proximal, разреженность, хеширование признаков, экономия памяти, калибровка. Лучший ответ на вопрос «зачем линейная модель в 2020-х».
- [scikit-learn: LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) — точная формула минимизируемого функционала (обратите внимание на `C` при **сумме** потерь), таблица солверов и поддерживаемых ими штрафов. Сверяйтесь перед подбором гиперпараметров.

### [Метрики качества](../docs/02-classic-ml/04-metrics.md)

- **Fawcett T. «An Introduction to ROC Analysis» (2006), Pattern Recognition Letters, 27(8)** — самое аккуратное изложение ROC-анализа: свойства кривой, выпуклая оболочка, изокосты, работа с несколькими классами. Читать, если хотите понимать ROC глубже, чем «площадь под кривой».
- **Davis J., Goadrich M. «The Relationship Between Precision-Recall and ROC Curves» (ICML 2006)** — доказывает, что доминирование по ROC эквивалентно доминированию по PR, и объясняет, почему при этом *площади* ведут себя по-разному. Ключевая работа для понимания раздела 4.
- **Saito T., Rehmsmeier M. «The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets» (PLOS ONE, 2015)** — много численных экспериментов ровно на тему §4.1; полезно тем, кому нужны аргументы в споре с командой.
- [scikit-learn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) — справочник по всем реализованным метрикам с точными определениями и оговорками про усреднения. Держать открытым при написании кода: половина расхождений в отчётах берётся из разных дефолтов `average`.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 7** — оценка качества и выбор модели: связь функции потерь, ожидаемого риска и метрик, а также почему оценка на данных, использованных для настройки, смещена.
- [Hyndman R., Athanasopoulos G. «Forecasting: Principles and Practice»](https://otexts.com/fpp3/) — глава про оценку точности прогнозов: там разобраны MAPE, sMAPE, MASE и приведены аргументы, почему авторы рекомендуют именно MASE. Обязательно для тех, кто работает с временными рядами.
- [Manning C., Raghavan P., Schütze H. «Introduction to Information Retrieval»](https://nlp.stanford.edu/IR-book/) — глава 8 «Evaluation in information retrieval»: MAP, MRR, NDCG, устройство асессорской разметки и пулинг. Первоисточник для всего раздела 8.
- **Järvelin K., Kekäläinen J. «Cumulated Gain-Based Evaluation of IR Techniques» (2002), ACM TOIS 20(4)** — статья, в которой введён DCG/NDCG. Читать ради обоснования выбора логарифмического дисконта: это не единственный возможный выбор, и авторы объясняют, какой моделью поведения пользователя он мотивирован.

### [Решающие деревья](../docs/02-classic-ml/05-decision-trees.md)

- **Breiman, Friedman, Olshen, Stone. «Classification and Regression Trees» (CART), 1984** — первоисточник. Читать ради двух вещей, которых нет нигде больше в таком объёме: суррогатные сплиты с мерой предсказательной связи и полный разбор cost-complexity pruning с доказательством вложенности поддеревьев.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 9.2** — самое аккуратное короткое изложение: критерии, пример «400/400» из раздела 3.5, обсуждение категориальных признаков и нестабильности. 15 страниц, читаются за вечер.
- **Hyafil L., Rivest R. «Constructing Optimal Binary Decision Trees is NP-complete», Information Processing Letters, 1976** — двухстраничная работа, ради которой стоит понять, почему жадность здесь не лень, а необходимость.
- **Strobl C. et al. «Bias in random forest variable importance measures: Illustrations, sources and a solution», BMC Bioinformatics, 2007** — систематический разбор смещения MDI: откуда берётся, как зависит от мощности признака и от бутстрапа, что с этим делать. Обязательно тем, кто принимает решения по важностям.
- [Документация scikit-learn: Decision Trees](https://scikit-learn.org/stable/modules/tree.html) — раздел «Tips on practical use» и «Minimal Cost-Complexity Pruning» содержат ровно те практические детали, которые чаще всего спрашивают: что делают параметры, как sklearn обрабатывает пропуски, чем `min_samples_leaf` отличается от `min_samples_split`.
- [Документация scikit-learn: Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html) — короткий текст с честным разбором того, где permutation importance тоже ломается (коррелированные признаки). Читать сразу после раздела 8 этой главы.
- [Открытый курс ODS (mlcourse.ai)](https://mlcourse.ai/book/index.html), тема 3 — русскоязычное изложение деревьев и kNN с кодом и визуализациями разделяющих поверхностей; хорошо заходит как второй проход для тех, кому не хватает картинок.

### [Градиентный бустинг](../docs/02-classic-ml/07-gradient-boosting.md)

- [Friedman J. «Greedy Function Approximation: A Gradient Boosting Machine» (2001)](https://jerryfriedman.su.domains/ftp/trebst.pdf) — первоисточник. Читать ради разделов с выводом общей схемы и с частными случаями функций потерь; там же — обоснование shrinkage.
- [Friedman J. «Stochastic Gradient Boosting» (1999)](https://jerryfriedman.su.domains/ftp/stobst.pdf) — короткая работа про сабсэмплинг: откуда взялся `subsample` и сколько он реально даёт.
- [Chen T., Guestrin C. «XGBoost: A Scalable Tree Boosting System» (2016)](https://arxiv.org/abs/1603.02754) — раздел 2 содержит ровно тот вывод, что в §5 этой главы; раздел 3 — про алгоритм поиска сплитов и обработку разреженности. Обязательно для middle+.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 10** — наиболее аккуратное изложение бустинга как forward stagewise additive modeling и связи с AdaBoost через экспоненциальную потерю.
- [Документация LightGBM: Parameters Tuning](https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html) — практический разбор, какие параметры на что влияют; полезно как чек-лист перед тюнингом.
- [Разбор бустинга в открытом курсе ODS (mlcourse.ai), тема 10](https://mlcourse.ai/book/topic10/topic10_gradient_boosting.html) — русскоязычное изложение с кодом; хорошо заходит как второй проход после этой главы.

## Deep Learning

### [Нейросети и обратное распространение](../docs/03-deep-learning/01-neural-nets-and-backprop.md)

- [Goodfellow I., Bengio Y., Courville A. «Deep Learning»](https://www.deeplearningbook.org) — главы 6 (глубокие сети прямого распространения) и 8 (оптимизация). Каноничный вывод backprop и обсуждение универсальной аппроксимации. Читать, если нужна строгость.
- [Nielsen M. «Neural Networks and Deep Learning»](http://neuralnetworksanddeeplearning.com) — глава 2 — самое понятное словесное объяснение backprop из существующих, с той же нотацией $\delta^{(l)}$, что и здесь. Первый выбор, если вывод в §5 показался тяжёлым.
- [CS231n. Backpropagation, Intuitions](https://cs231n.github.io/optimization-2/) — разбор через вычислительный граф и «маршрутизацию» градиента. Лучший источник интуиции «сложение копирует, умножение меняет местами».
- [Baydin et al. «Automatic Differentiation in Machine Learning: a Survey» (2018)](https://arxiv.org/abs/1502.05767) — строгое разделение численного, символьного и автоматического дифференцирования, forward против reverse. Читать, чтобы перестать путать термины.
- [Karpathy A. «micrograd»](https://github.com/karpathy/micrograd) — скалярный autograd на ~150 строк, из которого вырос `Value` в §7. Сравните со своей реализацией из задачи 3.
- [He et al. «Delving Deep into Rectifiers» (2015)](https://arxiv.org/abs/1502.01852) — PReLU и инициализация под ReLU; здесь же аккуратный анализ дисперсии активаций по слоям.
- [Hendrycks D., Gimpel K. «Gaussian Error Linear Units (GELUs)» (2016)](https://arxiv.org/abs/1606.08415) — откуда взялась GELU и почему её интерпретируют как стохастический вентиль.
- [Ramachandran et al. «Searching for Activation Functions» (2017)](https://arxiv.org/abs/1710.05941) — Swish/SiLU, найденная автоматическим поиском; полезно как пример честного сравнения активаций.
- [Документация PyTorch: Autograd mechanics](https://pytorch.org/docs/stable/notes/autograd.html) — как устроен граф, что такое `requires_grad`, `detach`, in-place операции и почему они ломают обратный проход. Читать перед первым серьёзным проектом.
- Rumelhart D., Hinton G., Williams R. «Learning representations by back-propagating errors» (Nature, 1986) — статья, с которой backprop вошёл в обиход. Историческая ценность; математика там ровно та же, что в §5.

### [Как на самом деле обучается сеть](../docs/03-deep-learning/02-training-dynamics.md)

- [Glorot X., Bengio Y. «Understanding the difficulty of training deep feedforward neural networks» (2010)](http://proceedings.mlr.press/v9/glorot10a.html) — первоисточник Xavier-инициализации. Читать ради самого анализа дисперсий: это образец того, как рассуждать о масштабах в глубоких сетях.
- [He et al. «Delving Deep into Rectifiers» (2015)](https://arxiv.org/abs/1502.01852) — вывод He-инициализации и разбор развилки fan_in / fan_out.
- [Ioffe S., Szegedy C. «Batch Normalization» (2015)](https://arxiv.org/abs/1502.03167) — оригинальная статья. Читать вместе со следующей, чтобы увидеть, как менялось объяснение.
- [Santurkar et al. «How Does Batch Normalization Help Optimization?» (2018)](https://arxiv.org/abs/1805.11604) — экспериментальное опровержение объяснения через internal covariate shift и анализ сглаживания ландшафта. Обязательно к прочтению перед собеседованием.
- [Ba et al. «Layer Normalization» (2016)](https://arxiv.org/abs/1607.06450) и [Zhang, Sennrich «Root Mean Square Layer Normalization» (2019)](https://arxiv.org/abs/1910.07467) — LayerNorm и RMSNorm из первых рук; во второй есть аккуратная абляция, показывающая, что центрирование почти ничего не даёт.
- [Wu Y., He K. «Group Normalization» (2018)](https://arxiv.org/abs/1803.08494) — почему при батче 2 нужна другая нормализация, с хорошими графиками зависимости от $B$.
- [Kingma D., Ba J. «Adam: A Method for Stochastic Optimization» (2014)](https://arxiv.org/abs/1412.6980) — вывод bias correction в разделе 3; ровно то, что разобрано в §4.6.
- [Loshchilov I., Hutter F. «Decoupled Weight Decay Regularization» (2017)](https://arxiv.org/abs/1711.05101) — AdamW. Читать раздел с разбором, почему L2 и weight decay расходятся в адаптивных методах.
- [Loshchilov I., Hutter F. «SGDR: Stochastic Gradient Descent with Warm Restarts» (2016)](https://arxiv.org/abs/1608.03983) — косинусное расписание и рестарты.
- [Smith L. «Super-Convergence: Very Fast Training Using Large Learning Rates» (2017)](https://arxiv.org/abs/1708.07120) — one-cycle; там же практика LR range test.
- [Goyal et al. «Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour» (2017)](https://arxiv.org/abs/1706.02677) — линейное правило масштабирования и warmup, с честным разбором границ применимости.
- [Srivastava et al. «Dropout: A Simple Way to Prevent Neural Networks from Overfitting» (2014)](https://jmlr.org/papers/v15/srivastava14a.html) — первоисточник, включая интерпретацию через ансамбль подсетей.
- [Müller et al. «When Does Label Smoothing Help?» (2019)](https://arxiv.org/abs/1906.02629) — польза для калибровки и вред для дистилляции, с наглядными визуализациями представлений.
- [Pascanu et al. «On the difficulty of training recurrent neural networks» (2012)](https://arxiv.org/abs/1211.5063) — откуда взялся градиентный клиппинг и почему он по норме, а не по значению.
- [Karpathy A. «A Recipe for Training Neural Networks» (2019)](http://karpathy.github.io/2019/04/25/recipe/) — лучший практический текст про порядок действий и санитарные проверки. Прочитать целиком до первого серьёзного проекта.
- [Документация PyTorch: torch.optim](https://pytorch.org/docs/stable/optim.html) — точные формулы всех оптимизаторов и расписаний в том виде, в каком они реализованы. Смотреть, когда нужно понять, чем `Adam(weight_decay=)` отличается от `AdamW`.

### [Свёрточные и рекуррентные сети](../docs/03-deep-learning/03-cnn-and-rnn.md)

- [He et al. «Deep Residual Learning for Image Recognition» (2015)](https://arxiv.org/abs/1512.03385) — первоисточник ResNet. Читать ради раздела 3.1: там тот самый эксперимент с деградацией, который все пересказывают неверно.
- [He et al. «Identity Mappings in Deep Residual Networks» (2016)](https://arxiv.org/abs/1603.05027) — продолжение с аккуратным анализом того, почему остаточный путь должен быть чистым. Прямая параллель с pre-LN в трансформере.
- [Dumoulin & Visin. «A guide to convolution arithmetic for deep learning» (2016)](https://arxiv.org/abs/1603.07285) — все формулы размеров, включая транспонированную свёртку, с анимациями. Держите под рукой как справочник.
- [Distill. «Computing Receptive Fields of Convolutional Neural Networks» (2019)](https://distill.pub/2019/computing-receptive-fields/) — строгий вывод формул рецептивного поля, в том числе для сетей со сложной топологией.
- [Lin et al. «Network In Network» (2013)](https://arxiv.org/abs/1312.4400) — откуда взялись свёртки 1×1 и глобальный average pooling.
- [Howard et al. «MobileNets» (2017)](https://arxiv.org/abs/1704.04861) — depthwise separable свёртки и честный разбор компромисса «точность против латентности».
- [Pascanu et al. «On the difficulty of training recurrent neural networks» (2012)](https://arxiv.org/abs/1211.5063) — формальный анализ затухания и взрыва градиента в RNN плюс обоснование клиппинга. Это первоисточник для §9.
- [Cho et al. «Learning Phrase Representations using RNN Encoder–Decoder» (2014)](https://arxiv.org/abs/1406.1078) — статья, в которой появился GRU (и заодно постановка seq2seq).
- [Greff et al. «LSTM: A Search Space Odyssey» (2015)](https://arxiv.org/abs/1503.04069) — систематическая абляция всех компонентов LSTM: какие гейты действительно нужны. Лучший ответ на вопрос «что будет, если убрать forget gate».
- [Bai et al. «An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling» (2018)](https://arxiv.org/abs/1803.01271) — временные свёрточные сети (TCN); полезно как напоминание, что свёртка — полноценная альтернатива рекуррентности для последовательностей.
- [Gu & Dao. «Mamba: Linear-Time Sequence Modeling with Selective State Spaces» (2023)](https://arxiv.org/abs/2312.00752) — куда ушла рекуррентная идея. Читать после того, как разберётесь с §9 и §12.
- [Karpathy A. «The Unreasonable Effectiveness of Recurrent Neural Networks» (2015)](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) — классический пост с интуицией и примерами генерации. Хорошее «мягкое» дополнение к формулам.
- Оригинальная статья Hochreiter & Schmidhuber «Long Short-Term Memory» (Neural Computation, 1997) и LeCun et al. «Gradient-Based Learning Applied to Document Recognition» (Proceedings of the IEEE, 1998) — первоисточники LSTM и свёрточных сетей соответственно; ищите по названию, читать необязательно, но полезно понимать, насколько давно всё это придумано.

### [Внимание и трансформер](../docs/03-deep-learning/04-attention-and-transformer.md)

- [Vaswani et al. «Attention Is All You Need» (2017)](https://arxiv.org/abs/1706.03762) — первоисточник. Читать ради разделов 3.2 (attention) и 3.5 (позиционные кодировки); сноска про $\sqrt{d_k}$ — ровно то, что разобрано в §4.
- [Su et al. «RoFormer: Enhanced Transformer with Rotary Position Embedding» (2021)](https://arxiv.org/abs/2104.09864) — вывод RoPE. Раздел с доказательством свойства относительности стоит прочитать целиком.
- [Press et al. «Train Short, Test Long: Attention with Linear Biases» (2021)](https://arxiv.org/abs/2108.12409) — ALiBi и вообще хорошее обсуждение экстраполяции по длине.
- [Dao et al. «FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness» (2022)](https://arxiv.org/abs/2205.14135) — почему память важнее FLOPs. Обязательно для тех, кто идёт в инференс.
- [Xiong et al. «On Layer Normalization in the Transformer Architecture» (2020)](https://arxiv.org/abs/2002.04745) — строгий разбор pre-LN против post-LN и объяснение, почему post-LN требует warmup.
- [Ainslie et al. «GQA: Training Generalized Multi-Query Transformer Models» (2023)](https://arxiv.org/abs/2305.13245) — мотивация GQA и компромисс качество/память.
- [Jay Alammar. «The Illustrated Transformer»](https://jalammar.github.io/illustrated-transformer/) — визуальное объяснение. Полезно как *первый* проход, если тема совсем новая; после этой главы добавит немного.
- [Karpathy A. «nanoGPT»](https://github.com/karpathy/nanoGPT) — компактная референсная реализация decoder-only модели. Стоит прочитать целиком после того, как напишете свою: сравнение вашего кода с чужим — лучший способ найти собственные заблуждения.

### [PyTorch на практике](../docs/03-deep-learning/05-pytorch-in-practice.md)

- [PyTorch: Autograd mechanics](https://pytorch.org/docs/stable/notes/autograd.html) — официальная заметка о том, как устроен граф, что такое leaf-тензоры и как работают in-place операции. Короткая и обязательная.
- [PyTorch: Broadcasting semantics](https://pytorch.org/docs/stable/notes/broadcasting.html) — формальные правила из §3. Прочитать один раз внимательно дешевле, чем неделю искать баг.
- [PyTorch: CUDA semantics](https://pytorch.org/docs/stable/notes/cuda.html) — асинхронность, потоки, закреплённая память, кэширующий аллокатор. Это фундамент для §8 и §11.
- [PyTorch: Reproducibility](https://pytorch.org/docs/stable/notes/randomness.html) — первоисточник для §12, включая полный список недетерминированных операций.
- [PyTorch: Performance Tuning Guide](https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html) — чек-лист ускорения обучения: от `channels_last` до слияния операций. Прогоняйте по нему каждый новый проект.
- [PyTorch Profiler recipe](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) — практическое руководство по `torch.profiler` с разбором вывода.
- [Karpathy A. «A Recipe for Training Neural Networks» (2019)](https://karpathy.github.io/2019/04/25/recipe/) — лучший текст о методологии отладки обучения: почему начинать надо с переобучения одного батча и почему нельзя менять пять вещей сразу. Читать целиком, желательно дважды.
- [Karpathy A. «nanoGPT»](https://github.com/karpathy/nanoGPT) — референсный обучающий цикл на 300 строк со всеми практиками из этой главы: AMP, gradient accumulation, DDP, компиляция. Отличный образец того, как выглядит production-grade учебный код.
- [PyTorch Examples](https://github.com/pytorch/examples) — официальные примеры (ImageNet, языковая модель, DDP). Полезны как эталон структуры проекта.

### [Масштабирование обучения](../docs/03-deep-learning/06-scaling-and-efficiency.md)

- [Micikevicius et al. «Mixed Precision Training» (2017)](https://arxiv.org/abs/1710.03740) — первоисточник: loss scaling, мастер-копия весов fp32, список операций, требующих полной точности. Раздел 3 — ровно материал §3.
- [Chen et al. «Training Deep Nets with Sublinear Memory Cost» (2016)](https://arxiv.org/abs/1604.06174) — откуда взялся gradient checkpointing и оценка $O(\sqrt{L})$.
- [Korthikanti et al. «Reducing Activation Recomputation in Large Transformer Models» (2022)](https://arxiv.org/abs/2205.05198) — точные формулы памяти активаций (использованы в §2) и идея селективного пересчёта. Самая полезная статья для практических расчётов памяти.
- [Rajbhandari et al. «ZeRO: Memory Optimizations Toward Training Trillion Parameter Models» (2019)](https://arxiv.org/abs/1910.02054) — первоисточник трёх стадий с полным разбором памяти и коммуникации. Таблица из §7 — оттуда.
- [Zhao et al. «PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel» (2023)](https://arxiv.org/abs/2304.11277) — как ZeRO-3 реализован в PyTorch, включая политики оборачивания и перекрытие коммуникации.
- [Li et al. «PyTorch Distributed: Experiences on Accelerating Data Parallel Training» (2020)](https://arxiv.org/abs/2006.15704) — внутреннее устройство DDP: бакетинг градиентов, перекрытие all-reduce с обратным проходом. Читать перед вопросами про DDP на собеседовании.
- [Shoeybi et al. «Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism» (2019)](https://arxiv.org/abs/1909.08053) — тензорный параллелизм: почему первую матрицу режут по столбцам, а вторую по строкам.
- [Huang et al. «GPipe» (2018)](https://arxiv.org/abs/1811.06965) — пайплайн-параллелизм и формула пузыря.
- [Narayanan et al. «Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM» (2021)](https://arxiv.org/abs/2104.04473) — как комбинируют TP, PP и DP, откуда берутся правила «TP внутри узла» и метрика MFU.
- [Kaplan et al. «Scaling Laws for Neural Language Models» (2020)](https://arxiv.org/abs/2001.08361) — здесь появляется оценка $C \approx 6ND$ (приложение с подсчётом FLOPs) и первые законы масштабирования.
- [Hoffmann et al. «Training Compute-Optimal Large Language Models» (Chinchilla, 2022)](https://arxiv.org/abs/2203.15556) — пересмотр оптимального соотношения $N$ и $D$. Читать вместе с предыдущей.
- [PyTorch: Automatic Mixed Precision](https://pytorch.org/docs/stable/amp.html) и [рецепт AMP](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html) — актуальный API `autocast` и `GradScaler`, включая список операций, которые autocast оставляет в fp32.
- [PyTorch: Distributed Data Parallel notes](https://pytorch.org/docs/stable/notes/ddp.html) — практические детали DDP, включая `no_sync` и работу с неравномерными входами.
- [Karpathy A. «nanoGPT»](https://github.com/karpathy/nanoGPT) — компактный обучающий цикл, где AMP, накопление градиента, DDP и `torch.compile` собраны вместе на 300 строках. Лучший образец для копирования практик.

## NLP

### [BERT и семейство энкодеров](../docs/04-nlp/04-bert-and-encoders.md)

- [Devlin et al. «BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding» (2018)](https://arxiv.org/abs/1810.04805) — первоисточник. Читать ради раздела 3.1 (постановка MLM и обоснование 80/10/10) и приложения C.2 с абляциями; там же рекомендованные гиперпараметры дообучения.
- [Liu et al. «RoBERTa: A Robustly Optimized BERT Pretraining Approach» (2019)](https://arxiv.org/abs/1907.11692) — образцовое исследование абляций. Читать целиком: это лучший в NLP пример того, как отделять вклад рецепта обучения от вклада архитектуры.
- [Lan et al. «ALBERT: A Lite BERT for Self-supervised Learning of Language Representations» (2019)](https://arxiv.org/abs/1909.11942) — факторизация эмбеддингов, разделение параметров и обоснование SOP против NSP.
- [Clark et al. «ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators» (2020)](https://arxiv.org/abs/2003.10555) — разбор compute-эффективности предобучения. Раздел с абляциями по размеру генератора объясняет, почему он должен быть маленьким.
- [He et al. «DeBERTa: Decoding-enhanced BERT with Disentangled Attention» (2020)](https://arxiv.org/abs/2006.03654) — вывод разложения логита внимания на три слагаемых и обоснование множителя $\sqrt{3d}$.
- [Sanh et al. «DistilBERT, a distilled version of BERT» (2019)](https://arxiv.org/abs/1910.01108) — компактная статья про тройной лосс дистилляции; читать перед тем, как дистиллировать своё.
- [Reimers & Gurevych «Sentence-BERT» (2019)](https://arxiv.org/abs/1908.10084) — почему `[CLS]` плох как эмбеддинг и как обучать сиамскую схему. Обязательно, если делаете поиск.
- [Gao et al. «SimCSE: Simple Contrastive Learning of Sentence Embeddings» (2021)](https://arxiv.org/abs/2104.08821) — contrastive без разметки и хорошее обсуждение анизотропии (alignment и uniformity).
- [Wettig et al. «Should You Mask 15% in Masked Language Modeling?» (2022)](https://arxiv.org/abs/2202.08005) — прямая проверка канонической цифры; читать, если собираетесь предобучать свою модель.
- [Kuratov & Arkhipov «Adaptation of Deep Bidirectional Multilingual Transformers for Russian Language» (2019)](https://arxiv.org/abs/1905.07213) — как делали ruBERT: перенос из mBERT, пересборка словаря под русский.
- [Документация sentence-transformers](https://www.sbert.net/) — практический референс по лоссам (MultipleNegativesRankingLoss, TripletLoss), pooling-стратегиям и обучению своей модели. Начинать с раздела Training Overview.
- [Документация HuggingFace Transformers](https://huggingface.co/docs/transformers) — разделы про `AutoModelFor*`, `Trainer` и `DataCollatorForLanguageModeling` (в нём как раз реализована схема 80/10/10 — полезно сравнить со своей реализацией из задачи 1).

## LLM

### [Устройство современной LLM](../docs/05-llm/01-llm-architecture.md)

- [Touvron et al. «LLaMA: Open and Efficient Foundation Language Models» (2023)](https://arxiv.org/abs/2302.13971) — раздел 2 читать как чек-лист современного блока: там прямо перечислено, что и у кого позаимствовано (RMSNorm из GPT-3-подобных практик, SwiGLU из PaLM, RoPE из GPTNeo).
- [Grattafiori et al. «The Llama 3 Herd of Models» (2024)](https://arxiv.org/abs/2407.21783) — самый подробный публичный отчёт о том, как реально принимаются архитектурные решения: конфиги 8B/70B/405B, обоснование GQA, стадия расширения контекста.
- [Ainslie et al. «GQA: Training Generalized Multi-Query Transformer Models» (2023)](https://arxiv.org/abs/2305.13245) — замеры качество/память для разного числа KV-групп; отсюда «магическая» восьмёрка.
- [Shazeer «GLU Variants Improve Transformer» (2020)](https://arxiv.org/abs/2002.05202) — двухстраничная статья, из которой вырос SwiGLU. Полезна честностью: автор прямо пишет, что объяснения эффекту нет, есть только замеры.
- [Zhang, Sennrich «Root Mean Square Layer Normalization» (2019)](https://arxiv.org/abs/1910.07467) — почему центрирование можно выбросить.
- [Fedus et al. «Switch Transformers» (2021)](https://arxiv.org/abs/2101.03961) — канон по MoE: балансировочный лосс, capacity factor, инженерия роутинга.
- [Jiang et al. «Mixtral of Experts» (2024)](https://arxiv.org/abs/2401.04088) и [DeepSeek-AI «DeepSeek-V3 Technical Report» (2024)](https://arxiv.org/abs/2412.19437) — два разных подхода к MoE: 8 крупных экспертов top-2 против 256 мелких + общий, top-8. Второй отчёт стоит читать целиком ради раздела про экономику обучения.
- [Wang et al. «What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot Generalization?» (2022)](https://arxiv.org/abs/2204.05832) — контролируемое сравнение архитектур; эмпирическая основа для ответа «почему decoder-only».
- [Документация HuggingFace Transformers по LLaMA](https://huggingface.co/docs/transformers/model_doc/llama) — сверять свои реализации RoPE и GQA с рабочим кодом; там же смысл всех полей `config.json`.

### [Предобучение и законы масштабирования](../docs/05-llm/02-pretraining-and-scaling.md)

- [Kaplan et al. «Scaling Laws for Neural Language Models» (2020)](https://arxiv.org/abs/2001.08361) — первая работа, показавшая предсказуемость. Читать ради самой идеи и ради приложения с оценкой FLOPs, откуда растёт $6ND$.
- [Hoffmann et al. «Training Compute-Optimal Large Language Models» (2022)](https://arxiv.org/abs/2203.15556) — Chinchilla. Три подхода к оценке оптимума и эксперимент против Gopher; читать целиком, это самая цитируемая работа темы.
- [Besiroglu et al. «Chinchilla Scaling: A replication attempt» (2024)](https://arxiv.org/abs/2404.10102) — что не сходится в параметрическом фите Chinchilla. Хорошая прививка от веры в цифры из чужих статей.
- [Sardana & Frankle «Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws» (2024)](https://arxiv.org/abs/2401.00448) — формализация того, почему модели сегодня перетренировывают.
- [Lee et al. «Deduplicating Training Data Makes Language Models Better» (2021)](https://arxiv.org/abs/2107.06499) — дедупликация, MinHash, эффекты на запоминание и на загрязнение валидации.
- [Muennighoff et al. «Scaling Data-Constrained Language Models» (2023)](https://arxiv.org/abs/2305.16264) — сколько эпох можно повторять данные; ответ «до четырёх» родом отсюда.
- [Penedo et al. «The RefinedWeb Dataset for Falcon LLM» (2023)](https://arxiv.org/abs/2306.01116) — подробный разбор конвейера фильтрации веба с абляциями; лучший вход в тему «как чистят данные».
- [Wei et al. «Emergent Abilities of Large Language Models» (2022)](https://arxiv.org/abs/2206.07682) и [Schaeffer et al. «Are Emergent Abilities of Large Language Models a Mirage?» (2023)](https://arxiv.org/abs/2304.15004) — читать строго парой, в этом порядке. Отличный пример того, как выбор метрики меняет вывод.
- [Rae et al. «Scaling Language Models: Methods, Analysis & Insights from Training Gopher» (2021)](https://arxiv.org/abs/2112.11446) — приложение с правилами фильтрации MassiveText; те самые эвристики, которые с тех пор копируют все.

### [SFT и выравнивание](../docs/05-llm/03-sft-and-alignment.md)

- [Ouyang et al. «Training language models to follow instructions with human feedback» (2022)](https://arxiv.org/abs/2203.02155) — InstructGPT, каноническое описание трёхстадийного конвейера. Читать разделы 3.5 (модели и лоссы) и приложение с объёмами данных: именно оттуда цифры 13k/33k/31k.
- [Rafailov et al. «Direct Preference Optimization: Your Language Model is Secretly a Reward Model» (2023)](https://arxiv.org/abs/2305.18290) — DPO. Раздел 4 и приложение A.1 — тот самый вывод, который разобран в §9; стоит пройти по нему с карандашом ещё раз после этой главы.
- [Schulman et al. «Proximal Policy Optimization Algorithms» (2017)](https://arxiv.org/abs/1707.06347) — первоисточник PPO. Нужен, если будете реально запускать RLHF: там обрезанный суррогат и GAE.
- [Stiennon et al. «Learning to summarize from human feedback» (2020)](https://arxiv.org/abs/2009.01325) — самая понятная работа про RLHF-конвейер до InstructGPT, с честным разбором того, как модель переигрывает reward-модель.
- [Christiano et al. «Deep Reinforcement Learning from Human Preferences» (2017)](https://arxiv.org/abs/1706.03741) — откуда всё пошло. Читать ради постановки задачи обучения на сравнениях.
- [Gao, Schulman, Hilton. «Scaling Laws for Reward Model Overoptimization» (2022)](https://arxiv.org/abs/2210.10760) — количественная картина reward hacking: как истинное качество ведёт себя в зависимости от KL. Обязательно, если отвечаете за качество выравнивания.
- [Bai et al. «Constitutional AI: Harmlessness from AI Feedback» (2022)](https://arxiv.org/abs/2212.08073) — self-critique и RLAIF по принципам.
- [Lee et al. «RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback» (2023)](https://arxiv.org/abs/2309.00267) — прямое сравнение AI-разметки с человеческой.
- [Zhou et al. «LIMA: Less Is More for Alignment» (2023)](https://arxiv.org/abs/2305.11206) — аргумент «разнообразие важнее объёма» на 1000 примерах.
- [Shao et al. «DeepSeekMath» (2024)](https://arxiv.org/abs/2402.03300) — описание GRPO (раздел про RL). Читать ради формулы group-relative advantage.
- [Ethayarajh et al. «KTO: Model Alignment as Prospect Theoretic Optimization» (2024)](https://arxiv.org/abs/2402.01306) — что делать, когда у вас не пары, а просто метки «хорошо/плохо» на отдельных ответах.
- [Документация TRL (HuggingFace)](https://huggingface.co/docs/trl) — рабочие реализации `SFTTrainer`, `DPOTrainer`, `PPOTrainer`, `GRPOTrainer`. API меняется довольно быстро, поэтому сверяйтесь с версией, а не с постами в блогах.
- [RLHF Book (Nathan Lambert)](https://rlhfbook.com/) — свободная книга про post-training целиком: policy gradients, PPO, GRPO, DPO, практики. Лучший источник, если после этой главы хочется углубиться в RL-часть.

### [PEFT и квантизация](../docs/05-llm/04-peft-and-quantization.md)

- [Hu et al. «LoRA: Low-Rank Adaptation of Large Language Models» (2021)](https://arxiv.org/abs/2106.09685) — первоисточник. Читать разделы 4 (метод) и 7 (какие матрицы адаптировать и какой ранг реально нужен) — там же эмпирика про то, что $r=1{-}4$ часто достаточно.
- [Aghajanyan et al. «Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning» (2020)](https://arxiv.org/abs/2012.13255) — почему низкоранговое обновление вообще работает. Это ответ на маркерный вопрос собеседования.
- [Dettmers et al. «QLoRA: Efficient Finetuning of Quantized LLMs» (2023)](https://arxiv.org/abs/2305.14314) — NF4, двойная квантизация, paged optimizers, и — важное — раздел про то, что адаптеры нужны на всех линейных слоях.
- [Dettmers et al. «LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale» (2022)](https://arxiv.org/abs/2208.07339) — открытие выбросных каналов активаций и почему они ломают наивную квантизацию.
- [Frantar et al. «GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers» (2022)](https://arxiv.org/abs/2210.17323) — послойная реконструкция и коррекция через обратный гессиан.
- [Lin et al. «AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration» (2023)](https://arxiv.org/abs/2306.00978) — идея защиты важных каналов через масштабирование. Читать раздел 3: там показано, что важность определяется активациями, а не величиной весов.
- [Xiao et al. «SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models» (2022)](https://arxiv.org/abs/2211.10438) — как перенести «сложность» из активаций в веса, чтобы стала возможна W8A8.
- [Dettmers & Zettlemoyer. «The case for 4-bit precision: k-bit Inference Scaling Laws» (2022)](https://arxiv.org/abs/2212.09720) — количественный ответ на вопрос «модель побольше в 4 битах или поменьше в 16».
- [Houlsby et al. «Parameter-Efficient Transfer Learning for NLP» (2019)](https://arxiv.org/abs/1902.00751) — адаптеры, исторический контекст PEFT.
- [Li & Liang. «Prefix-Tuning: Optimizing Continuous Prompts for Generation» (2021)](https://arxiv.org/abs/2101.00190) и [Lester et al. «The Power of Scale for Parameter-Efficient Prompt Tuning» (2021)](https://arxiv.org/abs/2104.08691) — два метода, которые постоянно путают на собеседовании.
- [Liu et al. «Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning» (2022)](https://arxiv.org/abs/2205.05638) — IA³ и сравнение PEFT с few-shot-промптингом.
- [Sheng et al. «S-LoRA: Serving Thousands of Concurrent LoRA Adapters» (2023)](https://arxiv.org/abs/2311.03285) — как устроен мультиадаптерный сервинг.
- [Документация PEFT (HuggingFace)](https://huggingface.co/docs/peft) — актуальные конфиги LoRA, DoRA, rsLoRA, IA³, слияние адаптеров. Сверяйтесь с версией: API активно развивается.
- [Документация bitsandbytes](https://huggingface.co/docs/bitsandbytes) — NF4, 8-битные оптимизаторы, paged optimizers.
- [Документация vLLM](https://docs.vllm.ai/) — поддержка GPTQ/AWQ, мультиадаптерный LoRA-сервинг, квантизация KV-кэша. Первоисточник по тому, что реально работает в проде.
- [llama.cpp (репозиторий)](https://github.com/ggml-org/llama.cpp) — GGUF и k-quants; в документации репозитория есть таблицы «размер против перплексии» для всех схем, полезные для выбора.

## Рекомендательные системы

### [Постановка задачи рекомендаций](../docs/06-recsys/01-recsys-foundations.md)

- **Hu Y., Koren Y., Volinsky C. «Collaborative Filtering for Implicit Feedback Datasets» (ICDM 2008)** — работа, задавшая схему «предпочтение + уверенность» и алгоритм iALS. Читать ради разделов 3–4: там формально показано, почему нельзя просто выбросить ненаблюдённые ячейки. Ищите по названию, PDF доступен на сайте Yifan Hu.
- [Rendle S. et al. «BPR: Bayesian Personalized Ranking from Implicit Feedback» (2009/2012)](https://arxiv.org/abs/1205.2618) — вторая базовая постановка для implicit: попарное ранжирование вместо поточечной регрессии. В контексте этой главы важна мотивационная часть — разбор, почему поточечная постановка на неявных данных концептуально неверна.
- **Covington P., Adams J., Sargin E. «Deep Neural Networks for YouTube Recommendations» (RecSys 2016)** — каноническое описание двухстадийной архитектуры «candidate generation → ranking» с реальными числами и честным разбором инженерных решений (включая знаменитый трюк с обучением на «следующем просмотре» вместо случайного holdout). Есть в открытом доступе на research.google.
- [Ferrari Dacrema M., Cremonesi P., Jannach D. «Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches» (2019)](https://arxiv.org/abs/1907.06902) — обязательное чтение перед тем, как поверить любой статье с новой архитектурой. Показывает, что аккуратно настроенные простые бейзлайны бьют большинство «нейросетевых прорывов».
- [Документация библиотеки `implicit`](https://implicit.readthedocs.io/) — практический инструмент для iALS/BPR на разреженных матрицах; полезно посмотреть на API, чтобы понять, в каком виде данные вообще подаются в такие модели.
- **Netflix Technology Blog** (`netflixtechblog.com`) — серия постов про рекомендации, калибровку и переход от предсказания оценок к ранжированию; лучший источник по продуктовой стороне вопроса. Искать по тегу recommendations.

### [Офлайн-метрики рекомендаций](../docs/06-recsys/02-metrics-offline.md)

- **Järvelin K., Kekäläinen J. «Cumulated Gain-Based Evaluation of IR Techniques» (ACM TOIS, 2002)** — первоисточник DCG и NDCG. Читать ради мотивации дисконта и обсуждения градуированной релевантности; там же разобрано, почему бинарной релевантности недостаточно. Ищите по названию, статья широко доступна.
- **Krichene W., Rendle S. «On Sampled Metrics for Item Recommendation» (KDD 2020)** — ключевая работа раздела 8. Содержит доказательство, что сэмплированные метрики несогласованы с полными, и корректирующие оценки. Обязательно, если вы читаете статьи по рекомендациям и сравниваете числа.
- [Ferrari Dacrema M., Cremonesi P., Jannach D. «Are We Really Making Much Progress?» (2019)](https://arxiv.org/abs/1907.06902) — про воспроизводимость: при равном бюджете тюнинга простые бейзлайны бьют большинство нейросетевых моделей. Читать как прививку от доверия к таблицам без описания протокола.
- [Rendle S., Krichene W., Zhang L., Anderson J. «Neural Collaborative Filtering vs. Matrix Factorization Revisited» (2020)](https://arxiv.org/abs/2005.09683) — прямое продолжение темы: как выбор протокола оценки и настройка бейзлайна меняют выводы на противоположные.
- [Joachims T., Swaminathan A., Schnabel T. «Unbiased Learning-to-Rank with Biased Feedback» (2016)](https://arxiv.org/abs/1608.04468) — формальная постановка задачи позиционного биаса и IPS-коррекции; основа для раздела 9 и для главы про LTR.
- **Shani G., Gunawardana A. «Evaluating Recommendation Systems»** (глава в *Recommender Systems Handbook*) — самый полный обзор метрик и протоколов, включая метрики за пределами точности. Полезен как справочник, когда нужно быстро вспомнить формулу.
- [Документация библиотеки `implicit`](https://implicit.readthedocs.io/) — там же реализованы `precision_at_k`, `ndcg_at_k`, `AUC_at_k` для разреженных матриц; удобно сверять свою реализацию с чужой конвенцией.

### [Коллаборативная фильтрация](../docs/06-recsys/03-collaborative-filtering.md)

- [Simon Funk. «Netflix Update: Try This at Home» (2006)](https://sifter.org/~simon/journal/20061211.html) — тот самый блог-пост, с которого началась FunkSVD. Читать ради интонации: видно, как метод придумывается из практических соображений, а не выводится из теории. Заодно навсегда запоминается, почему «SVD» в рекомендациях — не SVD.
- **Koren Y., Bell R., Volinsky C. «Matrix Factorization Techniques for Recommender Systems», IEEE Computer, 2009** — каноническая обзорная статья по MF со смещениями, SVD++ и временной динамике. Если читать что-то одно по этой главе — читайте её.
- **Koren Y. «Factorization Meets the Neighborhood: a Multifaceted Collaborative Filtering Model», KDD 2008** — первоисточник SVD++ и объединённой модели «соседи + факторы». Полезен разбором, как соседские веса обучаются, а не постулируются.
- **Sarwar B. et al. «Item-Based Collaborative Filtering Recommendation Algorithms», WWW 2001** — работа, которая ввела item-based схему и скорректированный косинус. Короткая, читается за час.
- **Linden G., Smith B., York J. «Amazon.com Recommendations: Item-to-Item Collaborative Filtering», IEEE Internet Computing, 2003** — инженерный взгляд: почему item-to-item масштабируется и как это работало в проде Amazon. Ровно те аргументы, что в разделе 3.
- [Rendle S. et al. «Neural Collaborative Filtering vs. Matrix Factorization Revisited» (2020)](https://arxiv.org/abs/2005.09683) — отрезвляющая работа: аккуратно настроенное скалярное произведение обыгрывает нейросетевые замены. Обязательна, чтобы не переоценивать сложность моделей.
- [Документация Surprise](https://surprise.readthedocs.io/en/stable/) — библиотека для explicit-CF с готовыми `SVD`, `SVD++`, `KNNBaseline` и опубликованными бенчмарками на MovieLens; удобна, чтобы быстро получить точку отсчёта перед своей реализацией.

### [Неявная обратная связь](../docs/06-recsys/04-implicit-feedback.md)

- **Hu Y., Koren Y., Volinsky C. «Collaborative Filtering for Implicit Feedback Datasets», ICDM 2008** — первоисточник iALS. Раздел с выводом ALS-шага — ровно то, что разобрано в §3; читать обязательно, если собираетесь отвечать на вопрос про $Q^\top Q$.
- [Rendle S. et al. «BPR: Bayesian Personalized Ranking from Implicit Feedback» (2009)](https://arxiv.org/abs/1205.2618) — первоисточник BPR. Ценность не только в функции потерь, но и в общей постановке: там же показано, что BPR — это фреймворк, в который можно подставить любую модель скора, включая kNN и tensor factorization.
- **Weston J., Bengio S., Usunier N. «WSABIE: Scaling Up To Large Vocabulary Image Annotation», IJCAI 2011** — откуда взялся WARP. Задача другая (аннотация изображений), но механика «сэмплируй до нарушения, взвесь по оценённому рангу» — та же.
- **Johnson C. «Logistic Matrix Factorization for Implicit Feedback Data», NIPS 2014 workshop** — короткая работа из Spotify; полезна разбором того, почему кросс-энтропия уместнее квадратичной потери на бинарной цели.
- [Rendle S. et al. «Neural Collaborative Filtering vs. Matrix Factorization Revisited» (2020)](https://arxiv.org/abs/2005.09683) — экспериментальное опровержение популярного тезиса «MLP лучше скалярного произведения». Читать ради методологии сравнения бейзлайнов.
- [Dacrema M. F., Cremonesi P., Jannach D. «Are We Really Making Much Progress?» (2019)](https://arxiv.org/abs/1907.06902) — воспроизводимость в RecSys: из 18 нейросетевых методов 11 не удалось воспроизвести, а большинство остальных проигрывают аккуратно настроенным простым бейзлайнам. Лучшая прививка от гонки за архитектурами.
- [Документация implicit](https://implicit.readthedocs.io/en/latest/) — реализации ALS, BPR и Logistic MF на C++/CUDA, `bm25_weight`, готовые методы `recommend` и `similar_items`. Основной рабочий инструмент для этой главы.
- [Документация LightFM](https://making.lyst.com/lightfm/docs/home.html) — BPR и WARP с поддержкой признаков; удобна, чтобы сравнить функции потерь на одинаковой модели.

### [Факторизационные машины и гибриды](../docs/06-recsys/05-factorization-machines.md)

- **Rendle S. «Factorization Machines», ICDM 2010** — первоисточник. Раздел с выводом свёртки квадратичного члена — ровно то, что разобрано в §4; там же показано, как MF, SVD++ и ещё несколько моделей получаются выбором структуры признаков.
- **Rendle S. «Factorization Machines with libFM», ACM TIST, 2012** — практическая версия той же работы: обучение через SGD, ALS и MCMC, разбор гиперпараметров. Полезна, если будете реализовывать FM сами.
- **Juan Y. et al. «Field-aware Factorization Machines for CTR Prediction», RecSys 2016** — FFM и опыт победы в CTR-соревнованиях. Ценно разделом про регуляризацию и раннюю остановку: там честно написано, насколько модель капризна.
- [Cheng H.-T. et al. «Wide & Deep Learning for Recommender Systems» (2016)](https://arxiv.org/abs/1606.07792) — первоисточник пары «memorization / generalization». Читать ради постановки вопроса и инженерных деталей (два оптимизатора, размеры эмбеддингов, конвейер обучения в Google Play).
- [Guo H. et al. «DeepFM: A Factorization-Machine based Neural Network for CTR Prediction» (2017)](https://arxiv.org/abs/1703.04247) — как убрать ручные кроссы, разделив эмбеддинги между FM и MLP. Короткая и понятная.
- [Wang R. et al. «Deep & Cross Network for Ad Click Predictions» (2017)](https://arxiv.org/abs/1708.05123) — явные взаимодействия высоких порядков через cross-слои; полезно как продолжение линии «не надейся, что MLP выучит произведения».
- [Naumov M. et al. «Deep Learning Recommendation Model for Personalization and Recommendation Systems» (2019)](https://arxiv.org/abs/1906.00091) — DLRM от Meta: как та же идея (эмбеддинги категорий + явные попарные взаимодействия + MLP) выглядит в промышленном масштабе, включая обсуждение памяти под таблицы эмбеддингов.
- [Kula M. «Metadata Embeddings for User and Item Cold-start Recommendations» (2015)](https://arxiv.org/abs/1507.08439) и [документация LightFM](https://making.lyst.com/lightfm/docs/home.html) — модель из §7 и её реализация; в документации есть готовый пример эксперимента на холодный старт.

## Выкатка в прод / MLOps

### [Жизненный цикл ML-системы](../docs/07-mlops/01-ml-lifecycle.md)

- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — первоисточник §4. Короткая (9 страниц) и её реально спрашивают. Читать целиком, особенно разделы про CACE, glue code и configuration debt.
- [Google Cloud. «MLOps: Continuous delivery and automation pipelines in machine learning»](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — первоисточник классификации уровней 0/1/2 из §5, со схемами компонентов каждого уровня.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — 43 правила из практики. Для этой главы особенно правила 1–8 (не делайте ML, пока не нужно; сначала инфраструктура, потом модель) и 29–32 (про train/serve skew).
- **Breck et al. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (IEEE Big Data, 2017)** — 28 конкретных проверок готовности ML-системы к проду, сгруппированных по данным, модели, инфраструктуре и мониторингу. Отличный чек-лист для аудита из задачи 1; используется в главе [CI/CD для ML](07-ci-cd-for-ml.md).
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы 1–2 и 8–9 закрывают жизненный цикл и эксплуатацию с большим количеством практических деталей.
- **Martin Kleppmann. «Designing Data-Intensive Applications»** — не про ML, но глава про эволюцию схем и совместимость данных — обязательное чтение перед [следующей главой](02-reproducibility-and-tracking.md) и главой про [контракты данных](03-data-and-feature-store.md).

### [Воспроизводимость и трекинг](../docs/07-mlops/02-reproducibility-and-tracking.md)

- [PyTorch. «Reproducibility»](https://pytorch.org/docs/stable/notes/randomness.html) — официальная страница про детерминизм: список недетерминированных операций, `use_deterministic_algorithms`, требования cuBLAS, поведение `DataLoader`. Короткая и обязательная к прочтению.
- [DVC. Документация](https://dvc.org/doc) — разделы Data Management (как устроен кэш и remote) и Pipelines (`dvc.yaml`, `dvc.lock`, `dvc repro`). Читать после §4 этой главы.
- [MLflow. Документация](https://mlflow.org/docs/latest/) — разделы Tracking, Models и Model Registry. Обратите внимание на страницу про алиасы и депрекацию стадий: это то, что часто устарело в чужих туториалах.
- [Hydra. Документация](https://hydra.cc/docs/intro/) — композиция конфигураций, `--multirun`, структурированные конфиги. Раздел про structured configs полезен вместе с pydantic.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — раздел про configuration debt прямо описывает требования из §7.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — глава 6 (Model Development and Offline Evaluation), раздел про эксперимент-трекинг и версионирование, с обсуждением того, почему версионирование данных сложнее версионирования кода.
- [Great Expectations. Документация](https://docs.greatexpectations.io/) — пригодится для задачи 5 предыдущей главы и для [качества данных](../09-monitoring/02-data-quality.md): ассерты на данные как код, версионируемые вместе с пайплайном.

### [Данные и feature store](../docs/07-mlops/03-data-and-feature-store.md)

- [Feast. Документация](https://docs.feast.dev/) — открытый feature store. Читать разделы про концепции (entity, feature view, feature service), про point-in-time joins и про материализацию: там формализовано ровно то, что разобрано в §4 и §6, включая роль второй временной метки.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 29–32 посвящены train/serve skew напрямую. Правило 29 («лучший способ добиться того, чтобы обучение соответствовало сервингу, — сохранять набор признаков, использованный во время сервинга, и подавать эти признаки в лог») — это ровно механизм из §5.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы 3–5 (Data Engineering Fundamentals, Training Data, Feature Engineering). Раздел про data leakage и про train/serve skew с большим количеством примеров из индустрии.
- [Uber Engineering. «Michelangelo: Uber's Machine Learning Platform»](https://www.uber.com/blog/michelangelo-machine-learning-platform/) — описание первой широко известной production-платформы с feature store; полезно как источник архитектурных решений и чисел.
- [Airbnb. Chronon (ранее Zipline) — открытый feature engineering framework](https://github.com/airbnb/chronon) — особенно материалы про backfill и про согласование батчевых и стриминговых определений одной фичи; это самая сложная часть темы.
- **Martin Kleppmann. «Designing Data-Intensive Applications»** — глава 4 (Encoding and Evolution) — первоисточник по режимам совместимости схем из §2, разобранный гораздо подробнее.
- [Apache Iceberg. Документация](https://iceberg.apache.org/docs/latest/) — раздел про снапшоты и time travel: механика того, как версионируется таблица, о которой шла речь в [предыдущей главе](02-reproducibility-and-tracking.md).
- [Great Expectations. Документация](https://docs.greatexpectations.io/) — практическая реализация проверок контракта данных как кода; см. также [качество данных](../09-monitoring/02-data-quality.md).

### [Упаковка модели](../docs/07-mlops/04-model-packaging.md)

- [Документация модуля `pickle` (python.org)](https://docs.python.org/3/library/pickle.html) — раздел про безопасность и описание протокола. Читать, чтобы увидеть предупреждение в первоисточнике и понять механизм `__reduce__`.
- [ONNX: документация по версионированию и операторам (репозиторий onnx/onnx, папка docs)](https://github.com/onnx/onnx/blob/main/docs/Versioning.md) — как устроены IR version и opset, что означает совместимость. Обязательно перед первой конверсией в прод.
- [ONNX Runtime — официальный сайт и документация](https://onnxruntime.ai/) — провайдеры исполнения, квантизация, оптимизации графа. Смотреть, когда конверсия уже работает и надо ускоряться.
- [safetensors (документация Hugging Face)](https://huggingface.co/docs/safetensors/index) — описание формата на одной странице. Полезно прочитать целиком: формат простой, и понимание его устройства снимает вопросы о том, откуда берётся zero-copy.
- [TorchScript (документация PyTorch)](https://pytorch.org/docs/stable/jit.html) — разница `trace` и `script`, ограничения поддерживаемого подмножества Python.
- [Mitchell et al. «Model Cards for Model Reporting» (2019)](https://arxiv.org/abs/1810.03993) — откуда взялась идея карточки модели и что в ней должно быть. Полезно для аргументации, зачем нужны поля limitations и разбивка метрик по сегментам.
- [MLflow — официальная документация](https://mlflow.org/docs/latest/) — разделы Model Registry и Models. Обратите внимание на переход от стадий к алиасам и на формат `MLmodel` как на готовый пример метаданных артефакта.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — глава про деплой и про model store: хорошая систематизация того, что должно храниться рядом с моделью.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — раздел про configuration debt и entanglement объясняет, почему артефакт без метаданных превращается в невоспроизводимый чёрный ящик.

### [Архитектуры сервинга](../docs/07-mlops/05-serving-architectures.md)

- [FastAPI — официальная документация](https://fastapi.tiangolo.com/) — разделы про lifespan, зависимости и фоновые задачи. Читать перед тем, как писать свой сервис.
- [Uvicorn — документация](https://www.uvicorn.org/) — раздел про деплой: воркеры, graceful shutdown, работа за прокси.
- [NVIDIA Triton Inference Server (репозиторий и документация)](https://github.com/triton-inference-server/server) — начните с раздела Model Configuration: dynamic batching и instance groups объясняют, как выжимать GPU.
- [TorchServe — документация PyTorch](https://pytorch.org/serve/) — более простая альтернатива Triton для чисто-PyTorch стека.
- [gRPC — «Introduction to gRPC»](https://grpc.io/docs/what-is-grpc/introduction/) — устройство протокола, дедлайны, стриминг. Обязательно прочитать про балансировку.
- [Prometheus: типы метрик](https://prometheus.io/docs/concepts/metric_types/) и [практика работы с гистограммами](https://prometheus.io/docs/practices/histograms/) — почему `histogram_quantile` даёт приближение и как выбирать бакеты. Это ровно та деталь, из-за которой у людей «неправильный p99».
- [Pydantic — документация](https://docs.pydantic.dev/latest/) — валидаторы и настройки модели: `extra="forbid"`, `field_validator`, работа с типами.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — глава Model Deployment and Prediction Service: систематизация батч/онлайн и разбор компромиссов.
- **Google SRE Book, главы «Handling Overload» и «Addressing Cascading Failures»** — первоисточник по ретрай-бюджетам, деградации и каскадным отказам. Читается быстро и полностью применимо к ML-сервисам.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про train/serve skew и логирование фич в момент предсказания напрямую относятся к дизайну сервиса.

### [Docker и Kubernetes для MLE](../docs/07-mlops/06-docker-and-k8s.md)

- [Dockerfile reference (docs.docker.com)](https://docs.docker.com/reference/dockerfile/) — справочник по инструкциям. Читать целиком не нужно; нужны разделы про `RUN`, `COPY`, `CMD`/`ENTRYPOINT` (особенно разница exec- и shell-формы) и про `--mount`.
- [Docker build cache (docs.docker.com)](https://docs.docker.com/build/cache/) — как именно инвалидируется кэш и как им управлять. Прямо отвечает на §2.
- [Docker Compose (docs.docker.com)](https://docs.docker.com/compose/) — раздел про `healthcheck` и `depends_on: condition` для корректного порядка запуска зависимостей.
- [Kubernetes: управление ресурсами контейнеров](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) — первоисточник по requests/limits, QoS-классам и поведению при превышении.
- [Kubernetes: liveness, readiness и startup probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) — все параметры и их семантика. Обратите внимание на то, что startupProbe отключает остальные до своего успеха.
- [Kubernetes: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — раздел про стратегии обновления, `maxSurge`/`maxUnavailable` и `rollout undo`.
- [Kubernetes: Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) — формула расчёта реплик, `behavior`, окна стабилизации.
- [Kubernetes: планирование GPU](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) — device plugin, целочисленность расширенных ресурсов, ограничения совместного использования.
- [NVIDIA k8s-device-plugin (репозиторий)](https://github.com/NVIDIA/k8s-device-plugin) — конфигурация time-slicing и MIG. Читать перед тем, как обещать «поделим карту».
- [KEDA](https://keda.sh/) — скейлинг по внешним метрикам (лаг Kafka, длина очереди), включая scale-to-zero. Полезно для стримингового и батчевого инференса.
- **Kubernetes Patterns (Ibryam, Huß, O'Reilly)** — паттерны Health Probe, Managed Lifecycle, Predictable Demands изложены ровно на том уровне абстракции, который нужен прикладному инженеру.

## ML System Design

### [Как проходить ML System Design](../docs/11-system-design/01-framework.md)

- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — лучшая книга по теме на сегодня. Главы про постановку задачи, feature engineering и мониторинг закрывают шаги 1–3 и 7.
- [Google. «Rules of Machine Learning: Best Practices for ML Engineering»](https://developers.google.com/machine-learning/guides/rules-of-ml) — 43 правила, выведенных из практики. Правила 1–10 стоит выучить: они ровно про то, что проверяется на этой секции.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — почему ML-система дороже в поддержке, чем кажется. Аргументы отсюда очень уместны в шаге 8.
- [Eugene Yan. «Applied ML» (подборка инженерных разборов от компаний)](https://github.com/eugeneyan/applied-ml) — сотни реальных описаний production-систем. Лучший источник конкретных чисел и архитектур.
- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments»** — для шага 7; см. также [раздел про A/B](../10-ab-testing/01-experiment-design.md).

### [Кейс: лента рекомендаций](../docs/11-system-design/02-case-feed-ranking.md)

- **Covington, Adams, Sargin. «Deep Neural Networks for YouTube Recommendations» (RecSys 2016)** — канонический разбор двухстадийной схемы кандидаты→ранжирование с честными инженерными деталями (сэмплирование, признак возраста видео, почему предсказывают время просмотра, а не клик). Искать по названию; статья свободно доступна на сайте исследовательской группы Google.
- **Zhao et al. «Recommending What Video to Watch Next: A Multitask Ranking System» (RecSys 2019)** — многозадачное ранжирование с MMoE и отдельной башней позиционного биаса; ровно то, что описано в §5 и §9.3 этой главы.
- [Zhou et al. «Deep Interest Network for Click-Through Rate Prediction» (2017)](https://arxiv.org/abs/1706.06978) — внимание к истории пользователя вместо усреднения эмбеддингов; читать перед переходом на вариант B из §5.
- [Kang, McAuley. «Self-Attentive Sequential Recommendation» (SASRec, 2018)](https://arxiv.org/abs/1808.09781) — сессионная модель, которая закрывает холодный старт пользователя и реактивность ленты.
- [Malkov, Yashunin. «Efficient and robust approximate nearest neighbor search using HNSW» (2016)](https://arxiv.org/abs/1603.09320) — устройство индекса, от параметров которого зависят те самые 12–18 мс из бюджета.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 1–16 почти дословно описывают лестницу усложнения из §4.
- Смежные главы хендбука: [холодный старт и смещения](../06-recsys/12-cold-start-and-bias.md), [эксплорация и бандиты](../06-recsys/13-exploration-and-bandits.md), [рекомендации в продакшене](../06-recsys/14-recsys-in-production.md), [онлайн-оценка рекомендаций](../06-recsys/15-recsys-online-evaluation.md).

### [Кейс: поиск и ранжирование](../docs/11-system-design/03-case-search.md)

- **Robertson, Zaragoza. «The Probabilistic Relevance Framework: BM25 and Beyond» (2009)** — откуда взялась формула BM25 и что означают её параметры; читать, если хотите отвечать на вопрос «почему именно так», а не «так принято». Искать по названию, работа свободно доступна.
- [Huang et al. «Embedding-based Retrieval in Facebook Search» (KDD 2020)](https://arxiv.org/abs/2006.11632) — лучший инженерный текст про гибрид лексики и векторов в проде: негативы, слияние ветвей, обслуживание индекса. Прямо соответствует §6 этой главы.
- [Karpukhin et al. «Dense Passage Retrieval» (2020)](https://arxiv.org/abs/2004.04906) — каноническая схема двухбашенного ретривала с in-batch и hard negatives.
- [Xiong et al. «Approximate Nearest Neighbor Negative Contrastive Learning» (ANCE, 2020)](https://arxiv.org/abs/2007.00808) — итеративная добыча hard negatives через периодическую перестройку индекса.
- [Khattab, Zaharia. «ColBERT» (2020)](https://arxiv.org/abs/2004.12832) — компромисс между двухбашенкой и кросс-энкодером; полезно, когда встанет вопрос «а можно ли качество кросс-энкодера за приемлемые деньги».
- **Joachims, Swaminathan, Schnabel. «Unbiased Learning-to-Rank with Biased Feedback» (WSDM 2017)** — формальная постановка IPS для ранжирования и оценка propensity; основа §10.4.
- **Chapelle, Chang. «Yahoo! Learning to Rank Challenge Overview» (2011)** — про то, как устроены промышленные датасеты LTR и почему LambdaMART так долго держит первое место.
- Смежные главы: [обучение ранжированию](../06-recsys/07-learning-to-rank.md), [двухбашенные модели и ANN](../06-recsys/06-two-tower-and-ann.md), [RAG](../05-llm/07-rag.md) — там же разбирается гибридный поиск, но под задачу генерации.

### [Кейс: антифрод](../docs/11-system-design/04-case-fraud-detection.md)

- **Le Borgne, Siblini, Lebichot, Bontempi. «Reproducible Machine Learning for Credit Card Fraud Detection — Practical Handbook»** (Université Libre de Bruxelles) — свободно доступная онлайн-книга с кодом. Лучший источник именно по специфике задачи: симулятор транзакций, правильная валидация с учётом задержки метки, метрики при экстремальном дисбалансе. Ищите по названию, книга выложена авторами открыто.
- **Dal Pozzolo et al. «Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy» (IEEE Transactions on Neural Networks and Learning Systems, 2018)** — статья, в которой аккуратно разобрана задержка верификации меток и предложена схема обучения с учётом того, что часть меток приходит от аналитиков быстро, а часть — от чарджбэков поздно.
- **Dal Pozzolo, Caelen, Johnson, Bontempi. «Calibrating Probability with Undersampling for Unbalanced Classification» (IEEE SSCI, 2015)** — откуда берётся формула коррекции вероятности после прореживания негативов, использованная в §5.
- [Соревнование IEEE-CIS Fraud Detection на Kaggle](https://www.kaggle.com/c/ieee-fraud-detection) — реальный анонимизированный набор транзакций; публичные решения — хороший каталог признаков (velocity, устройственные, «псевдо-идентификаторы» клиента) и наглядная демонстрация того, как участники ловили временную утечку.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про приоритет простых эвристик и про то, почему обучение на собственных решениях системы порождает петлю, здесь особенно уместны.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы про degenerate feedback loops и про мониторинг закрывают шаги 3 и 7 этого кейса.
- Для внутренней математики: [дисбаланс и калибровка](../02-classic-ml/12-imbalance-and-calibration.md), [валидация и утечки](../02-classic-ml/13-validation-and-leakage.md), [интерпретируемость](../02-classic-ml/15-interpretability.md), [деградация модели](../09-monitoring/04-model-degradation.md).

### [Кейс: отток и удержание](../docs/11-system-design/07-case-churn-uplift.md)

- **Radcliffe & Surry. «Real-World Uplift Modelling with Significance-Based Uplift Trees» (Stochastic Solutions, 2011)** — работа, из которой пришли и сам термин uplift, и Qini-кривая. Читать ради постановки и ради честного обсуждения того, насколько шумны эти оценки.
- **Gutierrez & Gérardy. «Causal Inference and Uplift Modelling: A Review of the Literature» (PMLR, 2017)** — компактный обзор семейства методов: two-model, преобразование класса, uplift-деревья; хорошая карта области перед углублением.
- **Künzel, Sekhon, Bickel, Yu. «Metalearners for estimating heterogeneous treatment effects using machine learning» (PNAS, 2019)** — S/T/X-learner в одном месте, с объяснением, когда какой работает; отсюда стоит взять аргументацию про слабости T-learner.
- **Athey & Imbens. «Recursive partitioning for heterogeneous causal effects» (PNAS, 2016)** — causal tree и идея honest estimation (разные подвыборки для структуры дерева и для оценок в листьях). Объясняет, почему наивные uplift-деревья переобучаются.
- [CausalML — библиотека Uber для uplift и CATE](https://github.com/uber/causalml) — реализации метаобучателей, uplift-деревьев и метрик, включая Qini; хорошая отправная точка для практики.
- [scikit-uplift — библиотека с метриками и моделями uplift](https://github.com/maks-sh/scikit-uplift) — русскоязычное сообщество, привычный sklearn-интерфейс, реализованы Qini, uplift@k и преобразование класса.
- **Diemert et al. «A Large Scale Benchmark for Uplift Modeling» (AdKDD, 2018)** — описание открытого датасета Criteo-UPLIFT с рандомизированным воздействием; редкий случай, когда можно потренироваться на настоящих экспериментальных данных.
- Для внутренней теории: [uplift и причинность](../02-classic-ml/17-uplift-and-causal.md), [дизайн эксперимента](../10-ab-testing/01-experiment-design.md), [снижение дисперсии](../10-ab-testing/03-variance-reduction.md), [сложные схемы экспериментов](../10-ab-testing/05-complex-designs.md).

---

🏠 [Оглавление хендбука](../docs/index.md)
