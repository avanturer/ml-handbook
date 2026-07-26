# Сводный список источников

> Собран автоматически из блоков «Что читать дальше» всех глав (`python tools/build_bibliography.py`).
> Это не список «прочитать всё» — это карта: у каждого источника указано, зачем его читать и после какой главы.

**Источников:** 982 · **глав с библиографией:** 114

## Как этим пользоваться

Читать источники до соответствующей главы обычно бесполезно: оригинальные статьи написаны для тех, кто уже знает контекст. Правильный порядок — глава, потом задачи, потом первоисточник. Тогда статья читается за полчаса вместо вечера, а в голове остаётся не пересказ, а понимание, чем работа отличается от предшественников.

---

## Старт

### [Карта собеседования MLE](../docs/00-start/03-interview-map.md)

- **Публичные матрицы компетенций** — если хотите свериться с первоисточником, а не с пересказом: `avito-tech/playbook` на GitHub (самая детальная русскоязычная, с отдельным файлом по DS-навыкам), `Tinkoff/career` (устройство секций собеседования), `DayMarket/data-skill-matrix` (редкий случай, когда «Middle+» выделен явной ступенью), `dropbox.github.io/dbx-career-framework` (западный фреймворк с ML-треком). Полезно посмотреть две-три и увидеть, что расходятся они в названиях, а сходятся — в ожиданиях.

### [Как учить, чтобы осталось в голове](../docs/00-start/04-study-method.md)

- **Brown, Roediger, McDaniel. «Make It Stick: The Science of Successful Learning» (2014)** — лучшее популярное изложение всего, что описано в этой главе, от самих исследователей. Если читать одну книгу об обучении — эту.
- **Ericsson, Pool. «Peak: Secrets from the New Science of Expertise» (2016)** — про осознанную практику: как устроена работа над тем, что не получается.
- **Sweller, Ayres, Kalyuga. «Cognitive Load Theory» (2011)** — академическое изложение теории когнитивной нагрузки, включая эффект обращения экспертизы. Для тех, кому нужна строгость. Важно читать вместе со следующим пунктом: книга описывает трёхкомпонентную версию теории, которую авторы позже пересмотрели.
- **Sweller, van Merriënboer, Paas. «Cognitive Architecture and Instructional Design: 20 Years Later» (Educational Psychology Review, 2019)** — ревизия теории самими авторами; именно здесь germane load перестаёт быть отдельным видом нагрузки. Полезно как пример того, что и в педагогике результаты пересматриваются.
- **Мета-анализы, на которых стоят оговорки этой главы** — по перемешиванию (Brunmair & Richter, 2019), по индуцированному самообъяснению (Bisra et al., 2018), по осознанной практике (Macnamara et al., 2014). Их стоит открыть хотя бы ради разделов с ограничениями: там видно, насколько популярные пересказы сильнее исходных данных.
- **Работы Роберта Бьорка о desirable difficulties** (лаборатория Bjork Learning and Forgetting Lab, UCLA) — первоисточник по разнесению, перемешиванию и различию между обучением и сиюминутной продуктивностью.
- [Документация Anki](https://docs.ankiweb.net/) — если решите настроить систему повторений; достаточно раздела о колодах и о параметрах интервалов.

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
- **Wasserman L. «All of Statistics»** — компактно и плотно; главы 1–5 покрывают эту главу, дальше идёт [статистика](../docs/01-math/03-statistics.md). Подходит тем, кто уже знает основы и хочет систематизации, а не введения.
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

### [Оптимизация](../docs/01-math/04-optimization.md)

- [Boyd S., Vandenberghe L. «Convex Optimization» (Cambridge University Press, 2004)](https://web.stanford.edu/~boyd/cvxbook/) — бесплатный PDF на сайте Стэнфорда. Каноничный источник по выпуклости, лагранжиану, двойственности и KKT. Главы 3 (выпуклые функции), 5 (двойственность) и 9 (методы спуска) покрывают §2 и §9 этой главы полностью.
- **Nocedal J., Wright S. «Numerical Optimization» (2nd ed., Springer, 2006)** — стандартный учебник по численной оптимизации: линейный поиск, методы второго порядка, квази-Ньютон (L-BFGS), trust region. Читать, если нужно понять, что происходит за пределами методов первого порядка.
- [Bottou L., Curtis F., Nocedal J. «Optimization Methods for Large-Scale Machine Learning» (2016)](https://arxiv.org/abs/1606.04838) — обзор ровно про то, чем оптимизация в ML отличается от классической: стохастика, компромисс батча, скорости сходимости SGD. Лучший единственный источник по §5.
- [Kingma D., Ba J. «Adam: A Method for Stochastic Optimization» (2014)](https://arxiv.org/abs/1412.6980) — оригинальная статья. Раздел 3 содержит ровно тот вывод коррекции смещения, что в §7.4.
- [Loshchilov I., Hutter F. «Decoupled Weight Decay Regularization» (2017)](https://arxiv.org/abs/1711.05101) — статья про AdamW. Читать ради раздела с сравнением L2 и weight decay: там же графики, показывающие, насколько по-разному ведут себя оптимальные $\lambda$.
- [Duchi J., Hazan E., Singer Y. «Adaptive Subgradient Methods for Online Learning and Stochastic Optimization», JMLR 2011](https://jmlr.org/papers/v12/duchi11a.html) — AdaGrad. Полезен, чтобы понять, откуда вообще взялась идея покоординатного адаптивного шага и почему она так хороша для разреженных данных.
- [Reddi S., Kale S., Kumar S. «On the Convergence of Adam and Beyond» (2019)](https://arxiv.org/abs/1904.09237) — контрпример, на котором Adam расходится, и AMSGrad как починка. Читать ради понимания границ метода.
- [Dauphin Y. et al. «Identifying and Attacking the Saddle Point Problem in High-dimensional Non-convex Optimization» (2014)](https://arxiv.org/abs/1406.2572) — источник картины «сёдла, а не локальные минимумы» из §10.
- [Smith L. «Cyclical Learning Rates for Training Neural Networks» (2015)](https://arxiv.org/abs/1506.01186) — здесь описан LR range test. Короткая практическая статья, читается за полчаса.
- [Ruder S. «An Overview of Gradient Descent Optimization Algorithms» (2016)](https://arxiv.org/abs/1609.04747) — компактный обзор всех методов из §6–8 в одной нотации; удобно как шпаргалка перед собеседованием.
- [Goodfellow I., Bengio Y., Courville A. «Deep Learning», глава 8](https://www.deeplearningbook.org/) — оптимизация именно в контексте обучения сетей: плохая обусловленность, плато, выбор батча, инициализация. Бесплатная онлайн-версия.

### [Теория информации](../docs/01-math/05-information-theory.md)

- **Cover T., Thomas J. «Elements of Information Theory»** — стандартный учебник. Для этой главы достаточно глав 2 (энтропия, взаимная информация) и 5 (кодирование); там же строгие доказательства всего, что здесь выведено на пальцах. Ищется по названию, PDF широко доступен.
- **Shannon C. E. «A Mathematical Theory of Communication», Bell System Technical Journal, 1948** — оригинальная статья, из которой выросло всё. Читается на удивление легко; первые десять страниц дают интуицию лучше любого пересказа.
- **MacKay D. «Information Theory, Inference, and Learning Algorithms»** — книга бесплатно выложена автором (ищется по названию). Единственный источник, где теория информации, байесовский вывод и машинное обучение изложены как одна дисциплина, а не три.
- [Hinton G., Vinyals O., Dean J. «Distilling the Knowledge in a Neural Network» (2015)](https://arxiv.org/abs/1503.02531) — первоисточник дистилляции. Читать разделы 2 и 3: там и про температуру, и про множитель $T^2$, и про «тёмное знание».
- [Kingma D., Welling M. «Auto-Encoding Variational Bayes» (2013)](https://arxiv.org/abs/1312.6114) — VAE и вывод ELBO; раздел 2 — ровно то, что в §8.2, но подробнее, плюс репараметризационный трюк.
- [van den Oord A., Li Y., Vinyals O. «Representation Learning with Contrastive Predictive Coding» (2018)](https://arxiv.org/abs/1807.03748) — статья, где введён InfoNCE и доказана граница $I \ge \log N - \mathcal{L}$. Читать ради приложения с выводом границы: именно оно объясняет, почему в контрастивном обучении так важен размер батча.
- [Документация `scipy.stats.entropy` и `scipy.spatial.distance.jensenshannon`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html) — короткие страницы, но прочитайте внимательно: `entropy(p, q)` считает KL, а не энтропию, а `jensenshannon` возвращает корень из дивергенции. Обе детали регулярно приводят к ошибкам в мониторинге.

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

### [Бэггинг и случайный лес](../docs/02-classic-ml/06-bagging-random-forest.md)

- [Breiman L. «Random Forests», Machine Learning 45(1), 2001](https://link.springer.com/article/10.1023/A:1010933404324) — первоисточник. Читать ради двух вещей: теоремы о сходимости ошибки обобщения при $B\to\infty$ (это и есть строгий ответ на «переобучается ли лес от числа деревьев») и оценки обобщающей способности через «силу» деревьев и их корреляцию — прямой формальный аналог формулы из §4.
- **Breiman L. «Bagging Predictors», Machine Learning 24(2), 1996** — работа, где бэггинг и появился. Главное в ней — раздел про нестабильность: там прямо сказано, для каких базовых моделей бэггинг бесполезен и почему.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 15** — лучшее компактное изложение: формула $\rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$, разбор `max_features`, OOB, и честное обсуждение того, где лес проигрывает бустингу. Раздел 15.4.2 отдельно про то, как лес ведёт себя при большом числе шумовых признаков.
- **Geurts P., Ernst D., Wehenkel L. «Extremely Randomized Trees», Machine Learning 63(1), 2006** — здесь есть то, чего нет в блогах: разбор, почему случайный порог не разрушает качество, и эксперименты по зависимости от степени рандомизации.
- **Strobl C. et al. «Bias in random forest variable importance measures», BMC Bioinformatics, 2007** — почему `feature_importances_` леса нельзя показывать бизнесу без оговорок; разбор вклада бутстрапа в это смещение.
- [Документация scikit-learn: Ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html) — разделы про `RandomForest`, `ExtraTrees` и `Bagging`: точная семантика всех параметров и практические заметки о том, что sklearn делает не так, как в оригинальных статьях (в частности, усреднение вероятностей вместо голосования большинством).
- [Открытый курс ODS (mlcourse.ai)](https://mlcourse.ai/book/index.html), тема 5 — русскоязычный разбор бэггинга и случайного леса с визуализациями и кодом; хороший второй проход после этой главы.

### [Градиентный бустинг](../docs/02-classic-ml/07-gradient-boosting.md)

- [Friedman J. «Greedy Function Approximation: A Gradient Boosting Machine» (2001)](https://jerryfriedman.su.domains/ftp/trebst.pdf) — первоисточник. Читать ради разделов с выводом общей схемы и с частными случаями функций потерь; там же — обоснование shrinkage.
- [Friedman J. «Stochastic Gradient Boosting» (1999)](https://jerryfriedman.su.domains/ftp/stobst.pdf) — короткая работа про сабсэмплинг: откуда взялся `subsample` и сколько он реально даёт.
- [Chen T., Guestrin C. «XGBoost: A Scalable Tree Boosting System» (2016)](https://arxiv.org/abs/1603.02754) — раздел 2 содержит ровно тот вывод, что в §5 этой главы; раздел 3 — про алгоритм поиска сплитов и обработку разреженности. Обязательно для middle+.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 10** — наиболее аккуратное изложение бустинга как forward stagewise additive modeling и связи с AdaBoost через экспоненциальную потерю.
- [Документация LightGBM: Parameters Tuning](https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html) — практический разбор, какие параметры на что влияют; полезно как чек-лист перед тюнингом.
- [Разбор бустинга в открытом курсе ODS (mlcourse.ai), тема 10](https://mlcourse.ai/book/topic10/topic10_gradient_boosting.html) — русскоязычное изложение с кодом; хорошо заходит как второй проход после этой главы.

### [XGBoost, LightGBM, CatBoost](../docs/02-classic-ml/08-boosting-in-practice.md)

- [Chen T., Guestrin C. «XGBoost: A Scalable Tree Boosting System» (2016)](https://arxiv.org/abs/1603.02754) — раздел 3 содержит ровно то, что разобрано в §2: приближённый алгоритм, weighted quantile sketch с доказательством и sparsity-aware split finding. Раздел 4 — про блоки, кэш и out-of-core; полезен, если вас спрашивают про инженерию, а не только про математику.
- **Ke G. et al. «LightGBM: A Highly Efficient Gradient Boosting Decision Tree», NeurIPS 2017** — оригинальная статья с выводом оценки Gain для GOSS и с формулировкой EFB как задачи раскраски графа. Доступна в открытых материалах конференции NeurIPS 2017; ищите по названию.
- [Prokhorenkova L. et al. «CatBoost: unbiased boosting with categorical features» (2017/2018)](https://arxiv.org/abs/1706.09516) — главный источник по §4. Разделы про target statistics (включая контрпример с leave-one-out) и про prediction shift с оценкой порядка $O(1/n)$ — обязательное чтение для middle+.
- [Dorogush A.V., Ershov V., Gulin A. «CatBoost: gradient boosting with categorical features support» (2018)](https://arxiv.org/abs/1810.11363) — короткая инженерная статья: комбинации признаков, oblivious-деревья, устройство GPU-реализации и замеры скорости инференса.
- [Документация LightGBM: Features](https://lightgbm.readthedocs.io/en/latest/Features.html) — сжатое описание histogram-подхода, leaf-wise, EFB и режимов распределённого обучения от авторов.
- [Документация LightGBM: Parameters Tuning](https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html) — официальный чек-лист «что крутить против переобучения / за скорость»; хорошо ложится на протокол из §6.2.
- [Документация XGBoost: Categorical Data](https://xgboost.readthedocs.io/en/stable/tutorials/categorical.html) — как устроены нативные категории, что делает `max_cat_to_onehot` и какие ограничения остались.
- [Документация CatBoost](https://catboost.ai/docs/) — читайте разделы про параметры `boosting_type`, `has_time`, `max_ctr_complexity` и про CTR-типы: там детали, которых нет в статьях.
- [Grinsztajn L., Oyallon E., Varoquaux G. «Why do tree-based models still outperform deep learning on typical tabular data?» (2022)](https://arxiv.org/abs/2207.08815) — аккуратный бенчмарк с разбором причин: неровные функции, нерелевантные признаки, отсутствие инвариантности к вращению. Полезно, когда на собеседовании спрашивают «а почему не нейросеть».

### [SVM, kNN и наивный Байес](../docs/02-classic-ml/09-svm-knn-bayes.md)

- [Cortes C., Vapnik V. «Support-Vector Networks» (1995)](https://link.springer.com/article/10.1007/BF00994018) — первоисточник soft-margin SVM. Читать ради постановки и разбора двойственной задачи; изложение на удивление доступное.
- [Hsu C.-W., Chang C.-C., Lin C.-J. «A Practical Guide to Support Vector Classification»](https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf) — восемнадцать страниц от авторов LIBSVM: масштабирование, выбор ядра, сетка по $C$ и $\gamma$. Самый практичный текст про SVM, который существует.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 12 и 13** — гл. 12 даёт SVM как задачу регуляризации в RKHS (взгляд, объясняющий связь с ridge-регрессией и сплайнами), гл. 13 — kNN и прототипные методы, включая обсуждение проклятия размерности.
- **Bishop C. «Pattern Recognition and Machine Learning», гл. 6–7** — самое аккуратное изложение ядерных методов и разреженных ядерных машин; там же — вывод через RKHS и связь с гауссовскими процессами.
- **Beyer K. et al. «When Is "Nearest Neighbor" Meaningful?», ICDT 1999** — работа, в которой доказана теорема о концентрации расстояний из §8. Стоит прочитать хотя бы формулировку теоремы и условия, при которых она **не** выполняется, — это объясняет, почему kNN всё же работает на разреженных и на кластеризованных данных.
- **Ng A., Jordan M. «On Discriminative vs. Generative Classifiers: A Comparison of Logistic Regression and Naive Bayes», NIPS 2001** — про пересечение кривых обучения и про то, когда генеративная модель выигрывает.
- **Domingos P., Pazzani M. «On the Optimality of the Simple Bayesian Classifier under Zero-One Loss», Machine Learning, 1997** — формальный ответ на вопрос «почему наивный Байес работает, хотя допущение нарушено».
- [Документация scikit-learn: Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html) — раздел про сложность и про практические советы; полезно как справка по параметрам и по особенностям многоклассовой схемы.
- [Документация scikit-learn: Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html) — разбор KD-tree/Ball-tree и границ их применимости по размерности.
- [Malkov Yu., Yashunin D. «Efficient and robust approximate nearest neighbor search using HNSW graphs» (2016)](https://arxiv.org/abs/1603.09320) — то, чем на самом деле реализуют kNN в проде; читать после этой главы, если работаете с эмбеддингами.

### [Кластеризация](../docs/02-classic-ml/10-clustering.md)

- [Arthur D., Vassilvitskii S. «k-means++: The Advantages of Careful Seeding» (2007)](https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf) — первоисточник $D^2$-семплирования с доказательством оценки $8(\ln K + 2)$. Читать ради самого доказательства: оно короткое и очень поучительное.
- **Ester M., Kriegel H.-P., Sander J., Xu X. «A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise», KDD 1996** — оригинальная статья DBSCAN. Там же — исходное обоснование эвристики k-dist для выбора $\varepsilon$.
- **Campello R., Moulavi D., Sander J. «Density-Based Clustering Based on Hierarchical Density Estimates», PAKDD 2013** — статья про HDBSCAN: взаимная достижимость, дерево уплотнения, критерий устойчивости.
- **Bishop C. «Pattern Recognition and Machine Learning», гл. 9** — эталонное изложение KMeans, GMM и EM, включая вывод через ELBO и связь KMeans с GMM в пределе. Если читать одну главу по теме — эту.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 14.3** — кластеризация в контексте обучения без учителя: K-medoids, иерархические методы, gap statistic для выбора $K$.
- [Документация scikit-learn: Clustering](https://scikit-learn.org/stable/modules/clustering.html) — сравнительная таблица методов по масштабируемости и геометрии плюс знаменитая картинка «все алгоритмы на всех формах данных»; отличная шпаргалка перед выбором метода.
- [Документация HDBSCAN: How HDBSCAN Works](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html) — пошаговый разбор с иллюстрациями: взаимная достижимость, MST, сжатое дерево, отбор по устойчивости. Самое понятное объяснение метода из существующих.
- [Документация scikit-learn: Gaussian Mixture Models](https://scikit-learn.org/stable/modules/mixture.html) — про `covariance_type`, вырождение ковариаций и вариационный байесовский вариант (`BayesianGaussianMixture`), который умеет сам «выключать» лишние компоненты.

### [Снижение размерности](../docs/02-classic-ml/11-dimensionality-reduction.md)

- [van der Maaten L., Hinton G. «Visualizing Data using t-SNE», JMLR 2008](https://www.jmlr.org/papers/v9/vandermaaten08a.html) — первоисточник. Читать ради разделов 2–3: там вывод перплексии и объяснение, зачем в целевом пространстве понадобилось распределение Стьюдента (проблема скученности, crowding problem).
- [Wattenberg M., Viégas F., Johnson I. «How to Use t-SNE Effectively», Distill 2016](https://distill.pub/2016/misread-tsne/) — интерактивная статья с живыми примерами того, как t-SNE врёт: размеры кластеров, расстояния, кластеры на шуме. Обязательна к прочтению перед тем, как показывать кому-либо t-SNE-картинку.
- [McInnes L., Healy J., Melville J. «UMAP: Uniform Manifold Approximation and Projection», arXiv:1802.03426](https://arxiv.org/abs/1802.03426) — оригинал UMAP. Математическая часть тяжёлая; для практики достаточно разделов про алгоритм и параметры.
- [Understanding UMAP (Coenen, Pearce; Google PAIR)](https://pair-code.github.io/understanding-umap/) — практический аналог статьи из Distill, но про UMAP: что делают `n_neighbors` и `min_dist` на живых примерах.
- [Halko N., Martinsson P.-G., Tropp J. «Finding Structure with Randomness», arXiv:0909.4061](https://arxiv.org/abs/0909.4061) — теория рандомизированного SVD. Читать, если нужно понимать, что именно делает `svd_solver='randomized'` и когда он даёт неточный ответ.
- [Kingma D., Welling M. «Auto-Encoding Variational Bayes», arXiv:1312.6114](https://arxiv.org/abs/1312.6114) — VAE. Следующий шаг после обычного автоэнкодера: вероятностная модель латентного пространства.
- [Документация sklearn: Decomposing signals in components](https://scikit-learn.org/stable/modules/decomposition.html) — какие ещё бывают разложения (NMF, ICA, KernelPCA, SparsePCA) и в чём их постановка отличается от PCA. Полезно как карта методов.
- **Jolliffe I., Cadima J. «Principal component analysis: a review and recent developments», Philosophical Transactions of the Royal Society A, 2016** — обзорная статья от автора канонической монографии по PCA; хороша разбором вариантов (робастный, разреженный, функциональный PCA) и типичных ошибок применения.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 14.5–14.9** — PCA, PCA через SVD, нелинейные обобщения (кернел-PCA, локально-линейное вложение, ISOMAP) и многомерное шкалирование в едином изложении.
- **Kobak D., Berens P. «The art of using t-SNE for single-cell transcriptomics», Nature Communications, 2019** — самая практичная работа про настройку t-SNE: инициализация, масштабирование learning rate под размер выборки, работа с миллионами точек.

### [Дисбаланс классов и калибровка](../docs/02-classic-ml/12-imbalance-and-calibration.md)

- [Chawla N. et al. «SMOTE: Synthetic Minority Over-sampling Technique» (2002), JAIR 16](https://arxiv.org/abs/1106.1813) — первоисточник. Читать ради точной формулировки алгоритма и, что важнее, ради условий экспериментов: станет видно, на каких данных метод проверяли и почему результаты не переносятся.
- **Elor Y., Averbuch-Elor H. «To SMOTE, or not to SMOTE?» (2022)** — систематическое сравнение балансировки на десятках датасетов с сильными и слабыми моделями. Главный вывод: для сильных классификаторов после правильной настройки порога прирост исчезает. Лучший аргумент в споре «а давайте сделаем SMOTE».
- **van den Goorbergh R. et al. «The harm of class imbalance corrections for risk prediction models» (2022), JAMIA 29(9)** — та же тема со стороны медицинского прогнозирования, с акцентом на разрушение калибровки. Читать, если модель используется для оценки риска, а не только для сортировки.
- [Lin T.-Y. et al. «Focal Loss for Dense Object Detection» (2017)](https://arxiv.org/abs/1708.02002) — оригинальная статья про focal loss. Раздел 3 объясняет, почему проблема именно в лёгких примерах, а не в соотношении классов; там же — эксперименты по $\gamma$ и $\alpha$.
- **Niculescu-Mizil A., Caruana R. «Predicting Good Probabilities With Supervised Learning» (ICML 2005)** — работа, откуда пошла практика «бустинг + Платт». Содержит калибровочные кривые для десятка семейств моделей: наглядно видно, кто переуверен, кто недоуверен и почему.
- **Kull M., Silva Filho T., Flach P. «Beta calibration» (AISTATS 2017)** — про то, почему сигмоида Платта не всегда подходит по форме, и про трёхпараметрическую альтернативу. Полезно, когда Платт недокалибровывает края, а изотоническая переобучается.
- [Guo C. et al. «On Calibration of Modern Neural Networks» (2017)](https://arxiv.org/abs/1706.04599) — про то же самое в мире нейросетей: почему современные сети систематически переуверены и почему temperature scaling с одним параметром часто достаточно. Читать перед тем, как калибровать выход нейросети.
- [scikit-learn: Probability calibration](https://scikit-learn.org/stable/modules/calibration.html) — практический справочник: `CalibratedClassifierCV`, `calibration_curve`, схемы с out-of-fold и с замороженной моделью. Держать открытым при реализации.

### [Валидация и утечки](../docs/02-classic-ml/13-validation-and-leakage.md)

- [Документация sklearn: Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — полный список сплиттеров с картинками фолдов. Держите открытым при выборе схемы: там же разобраны `GroupKFold`, `StratifiedGroupKFold`, `TimeSeriesSplit` и предупреждения о i.i.d.
- [Документация sklearn: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — официальный разбор утечек через препроцессинг и правильного использования `random_state`. Короткая страница, которую стоит прочитать целиком перед первым продовым проектом.
- [Документация sklearn: Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html) — `ColumnTransformer`, вложенные пайплайны, `get_feature_names_out`. База для раздела 8.
- [Raschka S. «Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning», arXiv:1811.12808](https://arxiv.org/abs/1811.12808) — самый полный обзор темы в одном тексте: hold-out, бутстрап, .632+, вложенная CV, тесты для сравнения моделей (McNemar, 5×2cv). Читать разделы про доверительные интервалы и про сравнение алгоритмов.
- **Hastie, Tibshirani, Friedman. «The Elements of Statistical Learning», гл. 7** — разложение ошибки, оптимизм ошибки обучения, кросс-валидация. Раздел 7.10.2 «The Wrong and Right Way to Do Cross-validation» — первоисточник примера с отбором признаков из лика 7.
- **Kaufman S., Rosset S., Perlich C. «Leakage in Data Mining: Formulation, Detection, and Avoidance», ACM TKDD, 2012** — единственная академическая работа, где утечка формализована. Вводит понятие «легитимности» признака относительно момента предсказания; полезна тем, что даёт язык для разговора с командой.
- **Bengio Y., Grandvalet Y. «No Unbiased Estimator of the Variance of K-Fold Cross-Validation», JMLR, 2004** — доказательство того, почему $s/\sqrt{K}$ нельзя доверять. Короткая и важная работа.
- **Cawley G., Talbot N. «On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation», JMLR, 2010** — эксперименты, показывающие величину смещения при подборе гиперпараметров без вложенной CV. Именно эту работу цитируют, когда требуют nested CV.
- **López de Prado M. «Advances in Financial Machine Learning», гл. 7** — purged K-fold, embargo, комбинаторная purged CV. Написано про финансы, но применимо везде, где метка созревает с лагом.
- **Kapoor S., Narayanan A. «Leakage and the Reproducibility Crisis in ML-based Science», Patterns, 2023** — систематический разбор 300+ научных работ, в которых утечка привела к неверным выводам, с таксономией видов лика. Отрезвляющее чтение.

### [Работа с признаками](../docs/02-classic-ml/14-feature-engineering.md)

- [scikit-learn: Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html) — референс по всем скейлерам, `PowerTransformer`, `QuantileTransformer`, кодировщикам категорий; читать как справочник, обращая внимание на разделы про разреженные данные.
- [scikit-learn: Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html) — `SimpleImputer`, `IterativeImputer`, `KNNImputer` и `add_indicator`; там же примеры, показывающие, когда модельная импутация окупается.
- [scikit-learn: Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html) — фильтры, RFE, `SelectFromModel`; полезно прочитать целиком перед тем, как писать свой отбор.
- [Weinberger et al. «Feature Hashing for Large Scale Multitask Learning» (2009)](https://arxiv.org/abs/0902.2206) — первоисточник hashing trick; ради разбора, почему знаковое хеширование даёт несмещённые скалярные произведения и как оценивается вред коллизий.
- [Guo, Berkhahn «Entity Embeddings of Categorical Variables» (2016)](https://arxiv.org/abs/1604.06737) — как эмбеддинги категорий работают на табличных данных; читать ради части про то, что выученные векторы отражают реальную географию магазинов.
- [Prokhorenkova et al. «CatBoost: unbiased boosting with categorical features» (2018)](https://arxiv.org/abs/1706.09516) — разделы про target statistics и prediction shift: самое аккуратное объяснение, почему наивное mean encoding смещает модель и как это чинится упорядоченными статистиками.
- **Micci-Barreca D. «A Preprocessing Scheme for High-Cardinality Categorical Attributes in Classification and Prediction Problems» (SIGKDD Explorations, 2001)** — оригинальная статья про сглаженное target encoding и иерархические категории; найдётся по названию в ACM Digital Library.
- **Kursa M., Rudnicki W. «Feature Selection with the Boruta Package» (Journal of Statistical Software, 2010)** — описание алгоритма Boruta с обоснованием теневых признаков и биномиального теста; ищется по названию на сайте JSS.
- **Zheng A., Casari A. «Feature Engineering for Machine Learning» (O'Reilly, 2018)** — компактная книга-справочник по преобразованиям; лучшие главы — про биннинг, логарифмы и работу с текстом.
- [Документация LightGBM: Advanced Topics — Categorical Feature Support](https://lightgbm.readthedocs.io/en/latest/Advanced-Topics.html) — как именно библиотека разбивает категории и почему это лучше one-hot; короткий, но важный текст.
- [Документация Feast](https://docs.feast.dev/) — практическая сторона point-in-time correctness и разделения офлайн/онлайн-хранилищ признаков; читать вместе с [главой про feature store](../docs/07-mlops/03-data-and-feature-store.md).

### [Интерпретируемость](../docs/02-classic-ml/15-interpretability.md)

- [Lundberg S., Lee S.-I. «A Unified Approach to Interpreting Model Predictions» (2017)](https://arxiv.org/abs/1705.07874) — оригинальная статья SHAP. Читать ради теоремы о единственности аддитивной атрибуции, удовлетворяющей аксиомам, и ради связи SHAP с LIME и DeepLIFT как частными случаями.
- [Lundberg S. et al. «Consistent Individualized Feature Attribution for Tree Ensembles» (2018)](https://arxiv.org/abs/1802.03888) — TreeSHAP: алгоритм и доказательство несогласованности gain-важности. Обязательно для middle+, если работаете с бустингом.
- [Lundberg S. et al. «From local explanations to global understanding with explainable AI for trees» (2019)](https://arxiv.org/abs/1905.04610) — препринт статьи в Nature Machine Intelligence: как из локальных SHAP собирать глобальные выводы, взаимодействия и кластеризацию объяснений; много практических примеров из медицины.
- [Ribeiro M. et al. «Why Should I Trust You? Explaining the Predictions of Any Classifier» (2016)](https://arxiv.org/abs/1602.04938) — LIME. Читать ради постановки задачи локальной верности и ради части про доверие к модели через объяснения — она до сих пор актуальна.
- [Goldstein A. et al. «Peeking Inside the Black Box: Visualizing Statistical Learning with Plots of Individual Conditional Expectation» (2013)](https://arxiv.org/abs/1309.6392) — ICE. Короткая работа с убедительными примерами, где PDP даёт прямо неверный вывод.
- [Apley D., Zhu J. «Visualizing the Effects of Predictor Variables in Black Box Supervised Learning Models» (2016)](https://arxiv.org/abs/1612.08468) — ALE: вывод и сравнение с PDP и M-plots. Читать, если у вас коррелированные признаки и нужен честный график зависимости.
- [Wachter S. et al. «Counterfactual Explanations without Opening the Black Box» (2017)](https://arxiv.org/abs/1711.00399) — формализация контрфактических объяснений и разбор их правового контекста (GDPR).
- [Rudin C. «Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead» (2019)](https://arxiv.org/abs/1811.10154) — сильная позиция против post-hoc объяснений в ответственных задачах. Полезно как контраргумент к «прикрутим SHAP и всё» — на собеседованиях в финтехе это ценят.
- [Molnar C. «Interpretable Machine Learning»](https://christophm.github.io/interpretable-ml-book/) — бесплатная книга-справочник по всем методам главы: PDP, ICE, ALE, LIME, SHAP, counterfactual, прототипы. Лучший второй проход после этой главы.
- [Документация shap](https://shap.readthedocs.io/en/latest/) — API, разбор типов explainer'ов и галерея графиков с интерпретацией; смотреть перед тем, как писать свой код.
- [scikit-learn: Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html) — вместе с [Partial dependence and ICE](https://scikit-learn.org/stable/modules/partial_dependence.html); в обоих разделах есть явные предупреждения про коррелированные признаки и пример с иерархической кластеризацией признаков.
- [Parr T. et al. «Beware Default Random Forest Importances»](https://explained.ai/rf-importance/) — наглядный разбор смещения MDI с экспериментами; хорошо читается как дополнение к §2.

### [Временные ряды](../docs/02-classic-ml/16-time-series.md)

- [Hyndman R., Athanasopoulos G. «Forecasting: Principles and Practice» (3-е изд.)](https://otexts.com/fpp3/) — бесплатный онлайн-учебник, де-факто стандарт по теме. Главы 3 (декомпозиция), 8 (экспоненциальное сглаживание), 9 (ARIMA) и 5.8 (метрики, включая MASE) покрывают весь материал этой главы строже и с примерами. Если читать одну книгу по рядам — эту.
- [Документация statsmodels: Time Series Analysis](https://www.statsmodels.org/stable/tsa.html) — справочник по ADF/KPSS, SARIMAX, STL, ETS и диагностике остатков. Полезно как источник точных сигнатур и того, что именно возвращают тесты.
- [Prophet: документация и статья Taylor & Letham «Forecasting at Scale»](https://facebook.github.io/prophet/) — читать раздел про устройство тренда с changepoints и про то, как задаются праздники; полезно, чтобы понимать границы применимости, а не только API.
- [Oreshkin B. et al. «N-BEATS: Neural basis expansion analysis for interpretable time series forecasting» (2019)](https://arxiv.org/abs/1905.10437) — архитектура, победившая на данных M4; интересна идеей интерпретируемого базисного разложения на тренд и сезонность внутри нейросети.
- [Lim B. et al. «Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting» (2019)](https://arxiv.org/abs/1912.09363) — как правильно разделять статические, известные заранее и наблюдаемые признаки; эта таксономия полезна даже если вы делаете бустинг.
- [Salinas D. et al. «DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks» (2017)](https://arxiv.org/abs/1704.04110) — каноничный пример глобальной вероятностной модели; читать ради того, как получают предсказательные распределения, а не точки.
- [Zeng A. et al. «Are Transformers Effective for Time Series Forecasting?» (2022)](https://arxiv.org/abs/2205.13504) — отрезвляющая работа: простая линейная модель бьёт трансформеры на стандартных бенчмарках. Читать ради критики протоколов сравнения — это же умение пригодится на собеседовании.
- **Makridakis S. et al., отчёты о соревнованиях M4 (2020) и M5 (2022), International Journal of Forecasting** — эмпирическая база для утверждений «что реально работает»: победа комбинаций статистики и ML на M4 и доминирование градиентного бустинга на M5.

### [Uplift и причинность](../docs/02-classic-ml/17-uplift-and-causal.md)

- [Künzel S. et al. «Metalearners for estimating heterogeneous treatment effects using machine learning» (2017)](https://arxiv.org/abs/1706.03461) — первоисточник X-learner с аккуратным сравнением S/T/X; читать раздел про несбалансированные группы — там объяснение весов, которое мы разобрали в §5.
- [Athey S., Imbens G. «Recursive Partitioning for Heterogeneous Causal Effects» (2015)](https://arxiv.org/abs/1504.01132) — causal tree и идея honest splitting. Ключевое место — объяснение, почему без разделения выборки оценка эффекта в листе смещена.
- [Wager S., Athey S. «Estimation and Inference of Heterogeneous Treatment Effects using Random Forests» (2015)](https://arxiv.org/abs/1510.04342) — causal forest и доверительные интервалы для CATE. Единственный из перечисленных методов, дающий корректный статистический вывод.
- [Nie X., Wager S. «Quasi-Oracle Estimation of Heterogeneous Treatment Effects» (2017)](https://arxiv.org/abs/1712.04912) — R-learner и разложение Робинсона; читать, если нужно понимать, откуда берутся современные DML-подходы.
- [Chernozhukov V. et al. «Double/Debiased Machine Learning for Treatment and Structural Parameters» (2016)](https://arxiv.org/abs/1608.00060) — теоретическая база для cross-fitting и ортогонализации. Тяжёлая статья; минимум — понять, зачем нужен cross-fitting.
- [Hernán M., Robins J. «Causal Inference: What If»](https://miguelhernan.org/whatifbook) — бесплатная книга, лучший источник по допущениям, DAG, конфаундерам, коллайдерам и IV. Первая часть читается без специальной подготовки и вправляет интуицию про то, что можно и чего нельзя контролировать.
- [causalml (Uber)](https://github.com/uber/causalml) — метаобучатели, uplift-деревья и леса, метрики Qini/AUUC в одном месте; хорошая отправная точка для продовой реализации.
- [EconML (Microsoft / PyWhy)](https://github.com/py-why/EconML) — DML, DR-learner, causal forest, IV; сильнее в статистическом выводе, чем causalml.
- [scikit-uplift](https://github.com/maks-sh/scikit-uplift) — API в стиле sklearn, метрики и визуализации uplift-кривых; удобен для быстрых экспериментов и для обучения.
- **Radcliffe N. «Using control groups to target on predicted lift» (2007)** — работа, откуда происходит кривая Qini; полезна как исторический первоисточник терминологии.
- **Rzepakowski P., Jaworski S. «Decision trees for uplift modeling with single and multiple treatments» (Knowledge and Information Systems, 2012)** — критерии расщепления uplift-деревьев, разобранные в §6.

### [Поиск аномалий](../docs/02-classic-ml/18-anomaly-detection.md)

- [Документация scikit-learn: Novelty and Outlier Detection](https://scikit-learn.org/stable/modules/outlier_detection.html) — сжатое сравнение Isolation Forest, LOF, One-Class SVM и Elliptic Envelope с картинками границ решения на разных структурах данных. Лучший способ увидеть, где какой метод ломается.
- [PyOD: библиотека детекторов аномалий](https://github.com/yzhao062/pyod) — более 40 реализованных методов с единым API, включая ансамблирование и глубокие модели. Полезна не только как код, но и как каталог: по списку методов удобно понять ландшафт задачи.
- **Liu F.T., Ting K.M., Zhou Z.-H. «Isolation Forest» (ICDM 2008)** — первоисточник; читать ради вывода нормировки $c(n)$ и раздела про swamping/masking, который объясняет выбор `max_samples=256`.
- **Breunig M. et al. «LOF: Identifying Density-Based Local Outliers» (SIGMOD 2000)** — первоисточник LOF; ключевое место — обоснование reachability distance как способа стабилизировать оценку плотности.
- **Schölkopf B. et al. «Estimating the Support of a High-Dimensional Distribution» (2001)** — вывод One-Class SVM и обеих интерпретаций параметра $\nu$.
- **Chandola V., Banerjee A., Kumar V. «Anomaly Detection: A Survey» (ACM Computing Surveys, 2009)** — классический обзор; лучшая систематизация постановок и типов аномалий, из которой взята таксономия §2.
- **Ruff L. et al. «A Unifying Review of Deep and Shallow Anomaly Detection» (Proceedings of the IEEE, 2021)** — современный обзор, связывающий классические методы и глубокие; полезен, чтобы понять, что автоэнкодер и Deep SVDD решают одну задачу разными средствами.
- **Wu R., Keogh E. «Current Time Series Anomaly Detection Benchmarks are Flawed» (IEEE TKDE, 2022)** — критика стандартных бенчмарков и протокола point-adjust. Читать перед тем, как поверить любому опубликованному F1 на рядах.
- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) и [SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — не про ML, но именно здесь лучше всего сформулированы принципы «алертить на симптомы» и работа с частотой ложных срабатываний. Раздел 10 этой главы во многом опирается на них.
- [ruptures: детекция точек разладки](https://github.com/deepcharles/ruptures) и [stumpy: matrix profile](https://github.com/TDAmeritrade/stumpy) — рабочие инструменты для двух задач из §9, которых нет в scikit-learn.

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

### [Текст как данные](../docs/04-nlp/01-text-representation.md)

- [Sennrich et al. «Neural Machine Translation of Rare Words with Subword Units» (2015)](https://arxiv.org/abs/1508.07909) — первоисточник BPE в NLP. Читать ради алгоритма в разделе 3.2: он занимает полстраницы и объясняет всё.
- [Kudo «Subword Regularization: Improving NMT Models with Multiple Subword Candidates» (2018)](https://arxiv.org/abs/1804.10959) — Unigram LM и идея сэмплирования сегментаций. Раздел про EM и обрезание словаря — то, чего нет в популярных пересказах.
- [Kudo & Richardson «SentencePiece: A simple and language independent subword tokenizer» (2018)](https://arxiv.org/abs/1808.06226) — короткая инженерная статья про то, почему обратимость и отсутствие пре-токенизации важны.
- [Wu et al. «Google's Neural Machine Translation System» (2016)](https://arxiv.org/abs/1609.08144) — здесь описан WordPiece в том виде, в каком он попал в BERT (раздел 4.1), а заодно length penalty для beam search, к которой мы вернёмся в [главе про seq2seq](../docs/04-nlp/03-seq2seq-and-attention.md).
- [Provilkov et al. «BPE-Dropout: Simple and Effective Subword Regularization» (2019)](https://arxiv.org/abs/1910.13267) — как получить регуляризацию сегментации, не уходя с BPE. Полезно, если у вас мало данных.
- [Документация HuggingFace Tokenizers](https://huggingface.co/docs/tokenizers/index) и [обзор токенизаторов в Transformers](https://huggingface.co/docs/transformers/tokenizer_summary) — практика: как собрать токенизатор из нормализатора, пре-токенизатора, модели и декодера. Читать перед тем, как обучать свой.
- [Karpathy A. «minbpe»](https://github.com/karpathy/minbpe) — референсная реализация BPE и byte-level BPE на несколько сотен строк, с разбором регулярки GPT-2. Лучший способ проверить свою реализацию из задачи 2.
- [Jurafsky & Martin «Speech and Language Processing», 3rd ed.](https://web.stanford.edu/~jurafsky/slp3/) — главы 2 (регулярки, нормализация, BPE) и 6 (векторные представления, TF-IDF, PPMI). Бесплатный черновик, лучший академический учебник по классическому NLP.
- [Документация pymorphy2](https://pymorphy2.readthedocs.io/) и [проект Natasha](https://github.com/natasha/natasha) — рабочие инструменты для русской морфологии и NER. Natasha полезна как готовый пайплайн: сегментация, морфология, синтаксис, NER на одном корпусе.
- [Snowball](https://snowballstem.org/) — описание стеммеров, включая русский, с исходными правилами. Полезно посмотреть, чтобы понять, насколько это грубый инструмент.

### [Эмбеддинги](../docs/04-nlp/02-embeddings.md)

- [Mikolov et al. «Efficient Estimation of Word Representations in Vector Space» (2013)](https://arxiv.org/abs/1301.3781) — первая статья: постановка Skip-gram и CBOW, задача аналогий. Короткая, читается за вечер.
- [Mikolov et al. «Distributed Representations of Words and Phrases and their Compositionality» (2013)](https://arxiv.org/abs/1310.4546) — вторая статья, и именно её надо читать: negative sampling, иерархический softmax, прореживание частых слов, степень 3/4. Всё, что разобрано в §4–§5.
- [Goldberg Y., Levy O. «word2vec Explained» (2014)](https://arxiv.org/abs/1402.3722) — разбор оригинальных статей на трёх страницах: авторы восстанавливают выкладки, которых в статьях Миколова нет. Лучший способ проверить свой вывод из задачи 1.
- **Levy O., Goldberg Y. «Neural Word Embedding as Implicit Matrix Factorization» (NIPS 2014)** — доказательство того, что SGNS факторизует сдвинутую матрицу PMI (свёртка в §4). Ищется по названию в трудах NIPS 2014.
- [Pennington et al. «GloVe: Global Vectors for Word Representation» (2014)](https://nlp.stanford.edu/pubs/glove.pdf) — вывод целевой функции из отношений вероятностей, §7 этой главы следует ему.
- [Bojanowski et al. «Enriching Word Vectors with Subword Information» (2016)](https://arxiv.org/abs/1607.04606) — fastText. Читать ради раздела с n-граммами и экспериментов на морфологически богатых языках (там есть русский).
- [Reimers N., Gurevych I. «Sentence-BERT» (2019)](https://arxiv.org/abs/1908.10084) — почему сырой BERT плох для косинуса и как это чинится сиамской схемой. Обязательно для всех, кто делает поиск или RAG.
- [Gao et al. «SimCSE: Simple Contrastive Learning of Sentence Embeddings» (2021)](https://arxiv.org/abs/2104.08821) — контрастивное обучение без разметки через dropout; там же аккуратный разбор выравнивания и однородности пространства.
- [Ethayarajh K. «How Contextual are Contextualized Word Representations?» (2019)](https://arxiv.org/abs/1909.00512) — измерение анизотропии и контекстной специфичности по слоям. Источник фактов из §10 и §11.
- [Muennighoff et al. «MTEB: Massive Text Embedding Benchmark» (2022)](https://arxiv.org/abs/2210.07316) — как устроен современный бенчмарк эмбеддингов и почему среднее по нему мало что говорит.
- [Документация gensim](https://radimrehurek.com/gensim/) и [sentence-transformers](https://www.sbert.net/) — рабочие инструменты. У второго особенно полезен раздел Training Overview: там перечислены функции потерь и то, под какие данные каждая подходит.
- [RusVectores](https://rusvectores.org/) — предобученные word2vec и fastText для русского на разных корпусах, с онлайн-демо ближайших соседей. Удобно, чтобы быстро проверить гипотезу до того, как что-то обучать.

### [Seq2seq и машинный перевод](../docs/04-nlp/03-seq2seq-and-attention.md)

- [Sutskever, Vinyals, Le «Sequence to Sequence Learning with Neural Networks» (2014)](https://arxiv.org/abs/1409.3215) — первая работающая seq2seq-модель. Читать ради постановки и ради трюка с разворотом входа: это лучшая иллюстрация того, чем плох бутылочный вектор.
- [Cho et al. «Learning Phrase Representations using RNN Encoder-Decoder» (2014)](https://arxiv.org/abs/1406.1078) — параллельная работа, здесь же впервые появляется GRU.
- [Bahdanau, Cho, Bengio «Neural Machine Translation by Jointly Learning to Align and Translate» (2014)](https://arxiv.org/abs/1409.0473) — статья, с которой началось внимание. Обязательна: разделы 3.1 и приложение с формулами, плюс графики BLEU по длине предложения и тепловые карты выравнивания.
- [Luong, Pham, Manning «Effective Approaches to Attention-based Neural Machine Translation» (2015)](https://arxiv.org/abs/1508.04025) — систематическое сравнение вариантов скоринга, input feeding, локальное внимание. Короткая и очень плотная.
- [Vaswani et al. «Attention Is All You Need» (2017)](https://arxiv.org/abs/1706.03762) — следующий шаг: внимание без рекуррентности. Читать сразу после Luong, чтобы увидеть преемственность; разбор — в [главе о трансформере](../docs/03-deep-learning/04-attention-and-transformer.md).
- [Papineni et al. «BLEU: a Method for Automatic Evaluation of Machine Translation» (2002)](https://aclanthology.org/P02-1040/) — первоисточник метрики. Восемь страниц, читаются за час, и после них формула из §7 перестаёт быть магией.
- [Post M. «A Call for Clarity in Reporting BLEU Scores» (2018)](https://arxiv.org/abs/1804.08771) — почему числа BLEU из разных статей несравнимы и что с этим делает sacreBLEU. Прочитать до того, как сравнивать свою модель с чьей-то опубликованной.
- [Wu et al. «Google's Neural Machine Translation System» (2016)](https://arxiv.org/abs/1609.08144) — инженерная статья: length penalty, coverage penalty, квантизация, обучение на восьми GPU. Формула $\mathrm{lp}(y)$ из §6.3 отсюда.
- [Holtzman et al. «The Curious Case of Neural Text Degeneration» (2019)](https://arxiv.org/abs/1904.09751) — почему поиск моды разрушает открытую генерацию и откуда взялся nucleus sampling.
- [Bengio et al. «Scheduled Sampling for Sequence Prediction with RNN» (2015)](https://arxiv.org/abs/1506.03099) — каноническая попытка починить exposure bias; полезно прочитать вместе с критикой метода.
- **Koehn P., Knowles R. «Six Challenges for Neural Machine Translation» (2017)** — честный список того, где нейронный перевод ломается: домен, редкие слова, длинные предложения, ширина луча. Ищется по названию.

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

### [Задачи NLP и их метрики](../docs/04-nlp/05-nlp-tasks-and-metrics.md)

- [Rajpurkar et al. «SQuAD: 100,000+ Questions for Machine Comprehension of Text» (2016)](https://arxiv.org/abs/1606.05250) — постановка extractive QA и определение EM/F1 вместе с процедурой нормализации ответов.
- [Rajpurkar et al. «Know What You Don't Know: Unanswerable Questions for SQuAD» (2018)](https://arxiv.org/abs/1806.03822) — почему умение отказаться от ответа надо мерить отдельно; прямо применимо к RAG.
- [Papineni et al. «BLEU: a Method for Automatic Evaluation of Machine Translation» (2002)](https://aclanthology.org/P02-1040/) — первоисточник. Читать ради определения модифицированной точности с клиппингом и вывода BP.
- [Lin «ROUGE: A Package for Automatic Evaluation of Summaries» (2004)](https://aclanthology.org/W04-1013/) — определения ROUGE-N, ROUGE-L, ROUGE-W и ROUGE-S. Короткая и точная статья.
- [Banerjee & Lavie «METEOR: An Automatic Metric for MT Evaluation» (2005)](https://aclanthology.org/W05-0909/) — сопоставление со стеммингом и синонимами, штраф за фрагментацию.
- [Zhang et al. «BERTScore: Evaluating Text Generation with BERT» (2019)](https://arxiv.org/abs/1904.09675) — метрика на эмбеддингах, а также честный раздел про её ограничения и про baseline rescaling.
- [Post «A Call for Clarity in Reporting BLEU Scores» (2018)](https://arxiv.org/abs/1804.08771) — почему BLEU из разных статей несопоставимы и что делает sacreBLEU. Читать перед публикацией любых чисел BLEU.
- [Mathur et al. «Tangled up in BLEU» (2020)](https://arxiv.org/abs/2006.06264) — систематический разбор того, как метрики вводят в заблуждение при сравнении сильных систем.
- [Rei et al. «COMET: A Neural Framework for MT Evaluation» (2020)](https://arxiv.org/abs/2009.09022) — обучаемая метрика, предсказывающая человеческую оценку; текущий стандарт в оценке перевода.
- [Artstein & Poesio «Inter-Coder Agreement for Computational Linguistics» (2008)](https://aclanthology.org/J08-4004/) — исчерпывающий разбор каппы Коэна, каппы Фляйсса и альфы Криппендорфа с обсуждением, когда какую брать. Лучший источник по теме разметки.
- [seqeval](https://github.com/chakki-works/seqeval) — референсная реализация entity-level метрик, совместимая со скриптом CoNLL. Прочитайте исходник обработки некорректных цепочек: это объясняет расхождения в числах между командами.

### [NLP в продакшене](../docs/04-nlp/06-nlp-in-production.md)

- [DistilBERT, a distilled version of BERT (Sanh et al., 2019)](https://arxiv.org/abs/1910.01108) — каноническая рецептура дистилляции энкодера: инициализация слоями учителя, тройная функция потерь, честные замеры. Читать перед тем, как дистиллировать своё.
- [Distilling the Knowledge in a Neural Network (Hinton et al., 2015)](https://arxiv.org/abs/1503.02531) — первоисточник температуры и множителя $\tau^2$. Короткая статья, стоит прочесть целиком: почти все последующие схемы — её вариации.
- [TinyBERT (Jiao et al., 2019)](https://arxiv.org/abs/1909.10351) и [MiniLM (Wang et al., 2020)](https://arxiv.org/abs/2002.10957) — согласование не только логитов, но и внутренних представлений и матриц внимания. Отсюда берут идеи, когда двух слоёв мало.
- [Well-Read Students Learn Better (Turc et al., 2019)](https://arxiv.org/abs/1908.08962) — набор маленьких BERT-ов и разбор, что важнее: предобучение ученика или дистилляция. Полезно, когда выбираете размер ученика.
- [How to Fine-Tune BERT for Text Classification? (Sun et al., 2019)](https://arxiv.org/abs/1905.05583) — систематическое сравнение стратегий усечения (head, tail, head+tail) и режимов дообучения на длинных документах. Именно отсюда рекомендация head+tail.
- [Q8BERT: Quantized 8Bit BERT (Zafrir et al., 2019)](https://arxiv.org/abs/1910.06188) — что происходит с качеством энкодера при 8 битах и где нужен quantization-aware training.
- [Sentence-BERT (Reimers, Gurevych, 2019)](https://arxiv.org/abs/1908.10084) и [Making Monolingual Sentence Embeddings Multilingual (Reimers, Gurevych, 2020)](https://arxiv.org/abs/2004.09813) — как получать эмбеддинги предложений, которые имеет смысл кэшировать, и как перенести качественную английскую модель на русский дистилляцией.
- [Документация ONNX Runtime](https://onnxruntime.ai/docs/) и [Hugging Face Optimum](https://huggingface.co/docs/optimum/index) — практические рецепты экспорта, оптимизации графа и квантизации. Читать как справочник во время работы.
- [Padding and truncation в документации Transformers](https://huggingface.co/docs/transformers/pad_truncation) — точная семантика `padding`, `truncation`, `only_second`, `stride`. Стоит прочитать один раз внимательно: половина ошибок с длинами берётся из непонимания этих флагов.
- [UAX #15: Unicode Normalization Forms](https://www.unicode.org/reports/tr15/) и [UTS #39: Unicode Security Mechanisms](https://www.unicode.org/reports/tr39/) — чем NFC отличается от NFKC и как устроены таблицы визуально неразличимых символов. Первое читать перед выбором нормализации, второе — если делаете фильтр контента.
- [fastText: определение языка](https://fasttext.cc/docs/en/language-identification.html) — модель `lid.176`, 176 языков, микросекунды на текст. Базовый инструмент для детекции языкового дрифта.
- [Gretton et al. «A Kernel Two-Sample Test» (JMLR, 2012)](https://www.jmlr.org/papers/v13/gretton12a.html) — строгая версия того, что в §8 сделано эвристикой: как корректно проверять, что две выборки векторов пришли из разных распределений. Читать, если строите серьёзный детектор дрифта эмбеддингов.
- **Sculley et al., «Hidden Technical Debt in Machine Learning Systems» (NeurIPS, 2015)** — классическая работа Google про то, что код модели составляет малую долю системы. Разделы про glue code и про entanglement объясняют, почему препроцессинг ломается чаще модели.

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

### [Инференс LLM](../docs/05-llm/05-inference-and-serving.md)

- [Kwon et al. «Efficient Memory Management for Large Language Model Serving with PagedAttention» (2023)](https://arxiv.org/abs/2309.06180) — статья про vLLM. Читать ради разделов про фрагментацию и про copy-on-write разделение блоков; там же измерения, откуда берутся числа «20–40% полезного использования памяти».
- [Leviathan et al. «Fast Inference from Transformers via Speculative Decoding» (2022)](https://arxiv.org/abs/2211.17192) — первоисточник спекулятивного декодирования с выводом формулы ожидаемого числа принятых токенов.
- [Chen et al. «Accelerating Large Language Model Decoding with Speculative Sampling» (2023)](https://arxiv.org/abs/2302.01318) — параллельная работа DeepMind; полезна доказательством, что распределение выходов сохраняется.
- [Dao et al. «FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness» (2022)](https://arxiv.org/abs/2205.14135) и [«FlashAttention-2» (2023)](https://arxiv.org/abs/2307.08691) — почему память важнее FLOPs. Обязательно, если планируете читать профили и понимать, куда уходит время.
- [Ainslie et al. «GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints» (2023)](https://arxiv.org/abs/2305.13245) и [Shazeer «Fast Transformer Decoding: One Write-Head is All You Need» (2019)](https://arxiv.org/abs/1911.02150) — откуда взялись MQA и GQA и какой ценой они уменьшают кэш.
- [Holtzman et al. «The Curious Case of Neural Text Degeneration» (2019)](https://arxiv.org/abs/1904.09751) — введение nucleus sampling и лучшее объяснение, почему greedy и beam search вырождаются на открытой генерации.
- [Документация vLLM](https://docs.vllm.ai/) — первоисточник по `enable_chunked_prefill`, `enable_prefix_caching`, `kv_cache_dtype`, спекулятивному декодированию и встроенному бенчмарку. API меняется быстро — всегда сверяйтесь с версией, которую поднимаете.
- [Документация HuggingFace Transformers: генерация](https://huggingface.co/docs/transformers/main/en/llm_tutorial) — параметры `generate`, `GenerationConfig`, стратегии декодирования и статический KV-кэш. Полезно, чтобы понимать, что именно движки делают за вас.

### [Промптинг и структурированный вывод](../docs/05-llm/06-prompting-and-structured-output.md)

- [Brown et al. «Language Models are Few-Shot Learners» (2020)](https://arxiv.org/abs/2005.14165) — работа, где in-context learning впервые показан как явление; читать разделы про зависимость качества от числа демонстраций и размера модели.
- [Wei et al. «Chain-of-Thought Prompting Elicits Reasoning in Large Language Models» (2022)](https://arxiv.org/abs/2201.11903) — первоисточник CoT. Важна не сама идея, а графики зависимости эффекта от размера модели.
- [Kojima et al. «Large Language Models are Zero-Shot Reasoners» (2022)](https://arxiv.org/abs/2205.11916) — zero-shot CoT; полезно как пример того, насколько результат чувствителен к одной фразе.
- [Wang et al. «Self-Consistency Improves Chain of Thought Reasoning» (2022)](https://arxiv.org/abs/2203.11171) — вывод через маргинализацию и замеры зависимости качества от числа сэмплов.
- [Min et al. «Rethinking the Role of Demonstrations» (2022)](https://arxiv.org/abs/2202.12837) — эксперимент со случайными метками; обязательно к прочтению перед проектированием few-shot.
- [Lu et al. «Fantastically Ordered Prompts and Where to Find Them» (2021)](https://arxiv.org/abs/2104.08786) и [Zhao et al. «Calibrate Before Use» (2021)](https://arxiv.org/abs/2102.09690) — пара работ про чувствительность к порядку примеров и про смещения; вторая содержит метод калибровки из раздела 3.1.
- [Sclar et al. «Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design» (2023)](https://arxiv.org/abs/2310.11324) — методология измерения устойчивости; берите оттуда протокол, а не выводы.
- [Turpin et al. «Language Models Don't Always Say What They Think» (2023)](https://arxiv.org/abs/2305.04388) и [Huang et al. «Large Language Models Cannot Self-Correct Reasoning Yet» (2023)](https://arxiv.org/abs/2310.01798) — две отрезвляющие работы: цепочка не является объяснением, а самокоррекция без внешнего сигнала вредит.
- [Liu et al. «Lost in the Middle: How Language Models Use Long Contexts» (2023)](https://arxiv.org/abs/2307.03172) — почему длинный промпт не бесплатен; напрямую влияет на выбор числа few-shot-примеров.
- [Willard, Louf. «Efficient Guided Generation for Large Language Models» (2023)](https://arxiv.org/abs/2307.09702) — математика и инженерия constrained decoding: построение автомата и индексация по словарю. Основа библиотеки Outlines.
- [Zhou et al. «Least-to-Most Prompting» (2022)](https://arxiv.org/abs/2205.10625) — декомпозиция как приём; читать ради постановки, а не ради конкретных промптов.
- [Khattab et al. «DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines» (2023)](https://arxiv.org/abs/2310.03714) — взгляд на промпты как на компилируемые программы с автоматической оптимизацией; полезно даже если не будете использовать фреймворк.
- **Tam et al. «Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models» (EMNLP 2024, Industry Track)** — измерение просадки качества от жёсткого формата; найдите по названию, это прямое эмпирическое дополнение к разделу 6.3.
- [Prompt Engineering Guide (dair-ai)](https://www.promptingguide.ai/) — справочник приёмов со ссылками на первоисточники. Использовать как каталог, а не как методологию.
- [Документация OpenAI: function calling](https://platform.openai.com/docs/guides/function-calling) и [structured outputs](https://platform.openai.com/docs/guides/structured-outputs), [документация Anthropic: tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) — форматы объявления инструментов и режимы строгих схем. Сверяйтесь с версией API: детали меняются.
- [promptfoo](https://www.promptfoo.dev/) — открытый инструмент для регрессионного тестирования и A/B промптов; полезен как готовая реализация идей раздела 8.

### [RAG](../docs/05-llm/07-rag.md)

- [Lewis et al. «Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks» (2020)](https://arxiv.org/abs/2005.11401) — первоисточник термина. Читать ради постановки задачи и понимания, чем исходный RAG (обучаемый ретривер, маргинализация по документам) отличается от того, что сегодня строят в проде.
- [Karpukhin et al. «Dense Passage Retrieval for Open-Domain QA» (2020)](https://arxiv.org/abs/2004.04906) — как обучают би-энкодер для поиска: in-batch negatives, hard negatives. Основа для дообучения своего эмбеддера, а это самый выгодный рычаг качества.
- [Thakur et al. «BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of IR Models» (2021)](https://arxiv.org/abs/2104.08663) — та самая работа, где BM25 обошёл многие обученные dense-ретриверы при переносе на новый домен. Обязательна, если хотите аргументированно защищать гибридный поиск.
- [Liu et al. «Lost in the Middle: How Language Models Use Long Contexts» (2023)](https://arxiv.org/abs/2307.03172) — U-образная кривая по позиции. Читать раздел с экспериментами: там видно, при каком числе документов эффект становится заметным.
- [Gao et al. «Precise Zero-Shot Dense Retrieval without Relevance Labels» (HyDE, 2022)](https://arxiv.org/abs/2212.10496) — короткая и изящная работа; полезна как пример того, что асимметрия «запрос против документа» бывает важнее качества энкодера.
- [Es et al. «Ragas: Automated Evaluation of Retrieval Augmented Generation» (2023)](https://arxiv.org/abs/2309.15217) и [документация Ragas](https://docs.ragas.io/) — определения faithfulness, answer relevance, context precision/recall и, что важнее, то, как именно их считают. Берите как готовый каркас оценки, но валидируйте судью на своих данных.
- [Asai et al. «Self-RAG» (2023)](https://arxiv.org/abs/2310.11511) и [Yan et al. «Corrective Retrieval Augmented Generation» (2024)](https://arxiv.org/abs/2401.15884) — две схемы адаптивного поиска. Читать вместе: они решают одну задачу разной ценой, и сравнение этой цены — хороший материал для секции system design.
- [Edge et al. «From Local to Global: A Graph RAG Approach to Query-Focused Summarization» (2024)](https://arxiv.org/abs/2404.16130) — GraphRAG от Microsoft. Смотреть на раздел про стоимость индексации: там честно написано, сколько LLM-вызовов это стоит.
- [Sarthi et al. «RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval» (2024)](https://arxiv.org/abs/2401.18059) — иерархическая суммаризация как компромисс между обычным RAG и GraphRAG.
- [Anthropic. «Introducing Contextual Retrieval» (2024)](https://www.anthropic.com/news/contextual-retrieval) — инженерный разбор с числами: насколько снижается доля провалов поиска от контекстного обогащения чанков, обогащённого BM25 и реранкера. Хороший пример того, как надо измерять улучшения RAG.
- [Khattab, Zaharia. «ColBERT» (2020)](https://arxiv.org/abs/2004.12832) — late interaction, промежуточное звено между би-энкодером и cross-encoder. Читать ради понимания шкалы «когда происходит взаимодействие запроса с документом».
- **Manning, Raghavan, Schütze. «Introduction to Information Retrieval»** ([свободно доступна на сайте Стэнфорда](https://nlp.stanford.edu/IR-book/)) — главы про инвертированный индекс, оценку ранжирования и BM25. Всё, что сегодня называют «продвинутым RAG», стоит на этом фундаменте; глава про оценку особенно полезна.
- [Malkov, Yashunin. «Efficient and robust approximate nearest neighbor search using HNSW graphs» (2016)](https://arxiv.org/abs/1603.09320) — устройство основного индекса векторных БД. Разбор с параметрами `M` и `efSearch` — в главе про [ANN-поиск](../docs/06-recsys/06-two-tower-and-ann.md).
- [RAG Techniques (NirDiamant)](https://github.com/NirDiamant/RAG_Techniques) — каталог приёмов с исполняемыми ноутбуками: реранкинг, query rewriting, гибридный поиск, self-RAG. Полезен как справочник реализаций, а не как источник методологии.
- [Разборы ruMTEB и русскоязычных эмбеддингов от SberDevices](https://habr.com/ru/companies/sberdevices/articles/831150/) — как устроен бенчмарк для русского языка и что смотреть при выборе энкодера под русский RAG. Вопрос «какую модель эмбеддингов возьмёте для русского» на собеседованиях звучит регулярно.

### [Агенты и вызов инструментов](../docs/05-llm/08-agents-and-tools.md)

- [Yao et al. «ReAct: Synergizing Reasoning and Acting in Language Models» (2022)](https://arxiv.org/abs/2210.03629) — первоисточник схемы; читать ради постановки и ради разбора, почему по отдельности рассуждение и действие работают хуже.
- [Anthropic. «Building Effective Agents» (2024)](https://www.anthropic.com/engineering/building-effective-agents) — лучший короткий инженерный текст по теме: разделение workflow и агентов, каталог паттернов (chaining, routing, orchestrator-workers, evaluator-optimizer) и настойчивый совет начинать с простейшего решения.
- [Anthropic. «How we built our multi-agent research system» (2025)](https://www.anthropic.com/engineering/multi-agent-research-system) — разбор реальной мультиагентной системы с числами по расходу токенов и списком того, что ломалось. Читать вместе с предыдущим: один текст говорит «не усложняйте», другой показывает цену усложнения.
- [Shinn et al. «Reflexion: Language Agents with Verbal Reinforcement Learning» (2023)](https://arxiv.org/abs/2303.11366) и [Huang et al. «Large Language Models Cannot Self-Correct Reasoning Yet» (2023)](https://arxiv.org/abs/2310.01798) — обязательная пара: первая показывает, как рефлексия работает с внешним сигналом, вторая — как она не работает без него.
- [Yao et al. «Tree of Thoughts» (2023)](https://arxiv.org/abs/2305.10601) — поиск по дереву рассуждений; полезно понимать, чтобы осознанно от него отказываться в продуктовых задачах.
- [Schick et al. «Toolformer» (2023)](https://arxiv.org/abs/2302.04761) — как модель обучают вызывать инструменты самонадзором; объясняет, откуда вообще берётся способность к function calling.
- [Patil et al. «Gorilla: Large Language Model Connected with Massive APIs» (2023)](https://arxiv.org/abs/2305.15334) — про выбор из большого числа API и про галлюцинации в сигнатурах вызовов. Прямо относится к проблеме «50 инструментов».
- [Packer et al. «MemGPT» (2023)](https://arxiv.org/abs/2310.08560) и [Park et al. «Generative Agents» (2023)](https://arxiv.org/abs/2304.03442) — две рамочные работы по памяти агентов: иерархия контекста и ранжирование воспоминаний.
- [Wu et al. «AutoGen» (2023)](https://arxiv.org/abs/2308.08155) — мультиагентные конверсационные паттерны; читать ради систематики топологий, а не ради фреймворка.
- [Jimenez et al. «SWE-bench» (2023)](https://arxiv.org/abs/2310.06770) — образец правильной оценки агентов: критерий успеха программируемый (прохождение тестов), задачи взяты из реальных репозиториев.
- [Zhou et al. «WebArena» (2023)](https://arxiv.org/abs/2307.13854), [Liu et al. «AgentBench» (2023)](https://arxiv.org/abs/2308.03688), [Mialon et al. «GAIA» (2023)](https://arxiv.org/abs/2311.12983) — три разных подхода к бенчмаркингу агентов; смотреть на устройство критериев успеха.
- **τ-bench (Sierra AI, 2024)** — бенчмарк на взаимодействие «агент — пользователь — инструменты» с проверкой соблюдения доменных политик; найдите по названию, это редкий пример оценки, близкой к продуктовым требованиям.
- [Lilian Weng. «LLM Powered Autonomous Agents» (2023)](https://lilianweng.github.io/posts/2023-06-23-agent/) — обзорный конспект с хорошей структурой (планирование, память, инструменты); удобен как карта области перед чтением первоисточников.
- [Model Context Protocol](https://modelcontextprotocol.io/) — открытый протокол подключения инструментов и источников данных к LLM-приложениям. Полезно понимать как способ стандартизовать реестр инструментов и не писать интеграции руками под каждого провайдера.
- [Документация OpenAI: function calling](https://platform.openai.com/docs/guides/function-calling) и [документация Anthropic: tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) — точные форматы объявления инструментов, параллельные вызовы, режимы принуждения к вызову. Сверяйтесь с версией API.

### [Оценка LLM](../docs/05-llm/09-llm-evaluation.md)

- [Zheng L. et al. «Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena» (2023)](https://arxiv.org/abs/2306.05685) — базовая работа по LLM-as-a-judge: измерение позиционного смещения, verbosity bias и self-enhancement bias, а также сопоставление вердиктов судьи с человеческими предпочтениями. Обязательно к прочтению перед тем, как строить судью.
- [Chiang W.-L. et al. «Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference» (2024)](https://arxiv.org/abs/2403.04132) — как устроена краудсорсинговая арена: схема выбора пар, переход от Elo к Bradley–Terry, доверительные интервалы бутстрапом. Читать ради инженерной части, а не ради таблицы результатов.
- [Wang P. et al. «Large Language Models are not Fair Evaluators» (2023)](https://arxiv.org/abs/2305.17926) — прицельно про позиционное смещение и приёмы его калибровки; короткая и полезная.
- [Zhou et al. «Don't Make Your LLM an Evaluation Benchmark Cheater» / Yang S. et al. «Rethinking Benchmark and Contamination for Language Models with Rephrased Samples» (2023)](https://arxiv.org/abs/2311.04850) — про перефразированную протечку, которую не ловит n-граммная дедупликация.
- [Zhang H. et al. «A Careful Examination of Large Language Model Performance on Grade School Arithmetic» (2024)](https://arxiv.org/abs/2405.00332) — GSM1k: как собирают свежий параллельный набор и что он показывает про запоминание. Лучший пример методики «проверь бенчмарк новым бенчмарком».
- [Dubois Y. et al. «Length-Controlled AlpacaEval» (2024)](https://arxiv.org/abs/2404.04475) — количественная поправка на смещение к длине в лидербордах на основе судей; полезно, даже если вы не используете AlpacaEval, как образец того, как формализуют поправку на смещение.
- [Liang P. et al. «Holistic Evaluation of Language Models (HELM)» (2022)](https://arxiv.org/abs/2211.09110) — манифест многомерной оценки: почему одну модель нельзя описать одним числом. Читать введение и раздел про сценарии.
- [Chen M. et al. «Evaluating Large Language Models Trained on Code» (2021)](https://arxiv.org/abs/2107.03374) — первоисточник `pass@k` с выводом несмещённой оценки (раздел 2).
- [Es S. et al. «RAGAS: Automated Evaluation of Retrieval Augmented Generation» (2023)](https://arxiv.org/abs/2309.15217) — разложение оценки RAG на компоненты: faithfulness, answer relevance, context relevance.
- [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — де-факто стандартный инструмент прогона академических бенчмарков; полезно посмотреть, как устроены сами задачи и насколько результат зависит от деталей формата промпта.

### [Безопасность и ограничители](../docs/05-llm/10-llm-safety-and-guardrails.md)

- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — отраслевой чек-лист рисков LLM-приложений: инъекции, небезопасная обработка вывода, чрезмерные привилегии, утечки. Лучшая отправная точка для построения своей модели угроз; читать целиком.
- [Greshake K. et al. «Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection» (2023)](https://arxiv.org/abs/2302.12173) — первая систематическая работа по косвенной инъекции с рабочими сценариями атак на реальные интеграции. Обязательно, если у вас RAG или агент с доступом к внешнему контенту.
- [Perez F., Ribeiro I. «Ignore Previous Prompt: Attack Techniques For Language Models» (2022)](https://arxiv.org/abs/2211.09527) — ранняя работа по прямой инъекции и извлечению промпта; короткая, задаёт базовую терминологию.
- [Wei A. et al. «Jailbroken: How Does LLM Safety Training Fail?» (2023)](https://arxiv.org/abs/2307.02483) — та самая рамка «конкуренция целей + несовпадение обобщения» из §5.2. Лучшее объяснение, *почему* выравнивание пробивается, а не просто каталог атак.
- [Zou A. et al. «Universal and Transferable Adversarial Attacks on Aligned Language Models» (2023)](https://arxiv.org/abs/2307.15043) — оптимизированные суффиксы и их переносимость между моделями; важно для понимания, что это не проблема конкретного вендора.
- [Carlini N. et al. «Extracting Training Data from Large Language Models» (2021)](https://arxiv.org/abs/2012.07805) и [Nasr M. et al. «Scalable Extraction of Training Data from (Production) Language Models» (2023)](https://arxiv.org/abs/2311.17035) — про запоминание обучающих данных; читать перед тем, как дообучать модель на реальных диалогах.
- [Inan H. et al. «Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations» (2023)](https://arxiv.org/abs/2312.06674) — как устроен специализированный guard-классификатор и его таксономия категорий; полезно как образец для своего фильтра.
- [Bai Y. et al. «Constitutional AI: Harmlessness from AI Feedback» (2022)](https://arxiv.org/abs/2212.08073) — подход к выравниванию через явный набор принципов; полезно понимать, что именно делает провайдер вашей модели и где границы этой защиты.
- [Ji Z. et al. «Survey of Hallucination in Natural Language Generation» (2022)](https://arxiv.org/abs/2202.03629) — систематизация типов галлюцинаций и методов их измерения.
- [Microsoft Presidio](https://github.com/microsoft/presidio) — открытый инструмент детекции и анонимизации PII с расширяемыми распознавателями; удобно взять как основу вместо самописных регулярок.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — формальная рамка управления рисками ИИ; нужна, когда безопасность приходится не только делать, но и защищать перед комплаенсом.
- [Simon Willison, метка «prompt injection»](https://simonwillison.net/tags/prompt-injection/) — многолетняя подборка разборов реальных атак и паттернов защиты (включая dual-LLM); лучший источник, чтобы держать руку на пульсе.

### [LLM в продакшене](../docs/05-llm/11-llm-in-production.md)

- [Kwon W. et al. «Efficient Memory Management for Large Language Model Serving with PagedAttention» (2023)](https://arxiv.org/abs/2309.06180) — статья vLLM: почему память под KV-кэш определяет пропускную способность и как непрерывный батчинг её поднимает. Основа для оценки $s$ в формуле безубыточности.
- [Zheng L. et al. «SGLang: Efficient Execution of Structured Language Model Programs» (2023)](https://arxiv.org/abs/2312.07104) — RadixAttention: как устроено автоматическое переиспользование префиксов на стороне сервера. Читать, если хостите модель сами.
- [Leviathan Y. et al. «Fast Inference from Transformers via Speculative Decoding» (2022)](https://arxiv.org/abs/2211.17192) — спекулятивное декодирование: как ускорить генерацию без потери качества распределения.
- [Chen L. et al. «FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance» (2023)](https://arxiv.org/abs/2305.05176) — каскады и роутинг с явной оптимизацией стоимости; полезно как формализация §5.
- [Ong I. et al. «RouteLLM: Learning to Route LLMs with Preference Data» (2024)](https://arxiv.org/abs/2406.18665) — обучение роутера на данных предпочтений, с оценкой компромисса «стоимость–качество».
- [Hinton G., Vinyals O., Dean J. «Distilling the Knowledge in a Neural Network» (2015)](https://arxiv.org/abs/1503.02531) — первоисточник дистилляции; полезно понимать исходную идею мягких целей, даже если для LLM чаще используют дистилляцию по последовательностям.
- [Документация Anthropic по кэшированию промптов](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — практические детали префиксного кэша: минимальная длина, TTL, точки останова, счётчики в ответе. Механика у разных провайдеров близка, читать полезно в любом случае.
- [Документация vLLM](https://docs.vllm.ai/) — разделы про непрерывный батчинг, автоматическое префиксное кэширование и метрики; практический ориентир при замере $s$ и $u$.
- [Amazon Builders' Library: Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — каноническое изложение стратегий ретраев и джиттера; читать перед тем, как писать свой retry-слой.
- [GPTCache](https://github.com/zilliztech/GPTCache) — открытая реализация семантического кэша; полезно посмотреть на устройство и на то, какие предохранители там предусмотрены (и каких нет).

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

### [Двухбашенные модели и ANN-поиск](../docs/06-recsys/06-two-tower-and-ann.md)

- [Malkov Yu., Yashunin D. «Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs» (2016)](https://arxiv.org/abs/1603.09320) — первоисточник HNSW. Читать разделы про выбор соседей и про роль $m_L$: там объяснено, почему граф остаётся связным и откуда логарифмическая сложность.
- [Johnson J., Douze M., Jégou H. «Billion-scale similarity search with GPUs» (2017)](https://arxiv.org/abs/1702.08734) — инженерия FAISS: как IVF-PQ ложится на GPU и почему k-selection был узким местом.
- [Douze M. et al. «The Faiss library» (2024)](https://arxiv.org/abs/2401.08281) — свежий обзор всей библиотеки от авторов; лучший источник, чтобы понять логику `index_factory` и что в какой комбинации имеет смысл.
- [Guo R. et al. «Accelerating Large-Scale Inference with Anisotropic Vector Quantization» (2020)](https://arxiv.org/abs/1908.10396) — ScaNN. Ключевая идея: для скалярного произведения ошибку квантования надо штрафовать анизотропно — вдоль направления вектора она важнее, чем поперёк.
- **Jégou H., Douze M., Schmid C. «Product Quantization for Nearest Neighbor Search» (IEEE TPAMI, 2011)** — оригинал PQ. Читать ради вывода ADC и анализа ошибки квантования; статья доступна на страницах авторов и в цифровой библиотеке IEEE.
- **Yi X. et al. «Sampling-Bias-Corrected Neural Modeling for Large Corpus Item Recommendations» (RecSys 2019, Google)** — та самая работа про logQ-коррекцию в two-tower и потоковую оценку частот айтемов. Ищите по названию в публикациях Google Research.
- **Yang J. et al. «Mixed Negative Sampling for Learning Two-tower Neural Networks in Recommendations» (Google, 2020)** — про смесь in-batch и равномерных негативов; короткая и практичная.
- [Документация FAISS (wiki репозитория)](https://github.com/facebookresearch/faiss/wiki) — разделы «Guidelines to choose an index» и «Faiss indexes» стоит прочитать целиком перед тем, как выбирать индекс: там есть готовое дерево решений по размеру данных и памяти.
- [hnswlib](https://github.com/nmslib/hnswlib) — референсная реализация HNSW с понятным API; читать README ради семантики `max_elements`, `ef` и пометки удалённых элементов.
- [Документация implicit](https://benfred.github.io/implicit/) — если нужно быстро получить бейзлайн-эмбеддинги айтемов через iALS перед тем, как обучать нейросетевые башни.

### [Обучение ранжированию](../docs/06-recsys/07-learning-to-rank.md)

- [Burges C. «From RankNet to LambdaRank to LambdaMART: An Overview» (Microsoft Research, 2010)](https://www.microsoft.com/en-us/research/publication/from-ranknet-to-lambdarank-to-lambdamart-an-overview/) — первоисточник и лучший текст по теме: весь путь от вероятностной модели пары до бустинга, с выводами и с честным разбором того, почему λ работает. Читать целиком, это ~20 страниц.
- [Joachims T., Swaminathan A., Schnabel T. «Unbiased Learning-to-Rank with Biased Feedback» (WSDM 2017)](https://arxiv.org/abs/1608.04468) — каноническая работа по IPS в ранжировании: постановка, доказательство несмещённости, swap-интервенции для оценки propensity. Раздел про дисперсию особенно полезен на практике.
- **Wang X. et al. «The LambdaLoss Framework for Ranking Metric Optimization» (CIKM 2018, Google)** — теоретическое обоснование λ-градиентов через явный вероятностный лосс; ищется по названию в публикациях Google Research. Читать после §6, если хочется закрыть вопрос «а лосс-то где».
- **Wang X. et al. «Position Bias Estimation for Unbiased Learning to Rank in Personal Search» (WSDM 2018)** — regression-EM: как оценить propensity без вмешательства в выдачу. Практично для тех, кому не согласуют рандомизацию трафика.
- **Chuklin A., Markov I., de Rijke M. «Click Models for Web Search» (Morgan & Claypool, 2015)** — короткая книга обо всех моделях клика (PBM, каскадная, DBN, UBM) и о том, как их обучать. Нужна, когда PBM перестаёт объяснять ваши данные.
- [Документация LightGBM: параметры](https://lightgbm.readthedocs.io/en/latest/Parameters.html) — разделы про `lambdarank` и `label_gain`. Читать перед первым запуском, а не после.
- [MSLR: Microsoft Learning to Rank Datasets](https://www.microsoft.com/en-us/research/project/mslr/) — WEB10K/WEB30K, стандартный полигон для экспериментов из §14.
- [allRank](https://github.com/allegro/allRank) — PyTorch-библиотека LTR от Allegro с реализациями ListNet, ListMLE, ApproxNDCG, NeuralNDCG. Полезна, чтобы потрогать listwise-лоссы руками.
- [TensorFlow Ranking](https://github.com/tensorflow/ranking) — промышленная библиотека Google; ценна документацией по unbiased LTR и готовыми реализациями propensity-взвешенных лоссов.

### [Нейронное ранжирование](../docs/06-recsys/08-neural-ranking.md)

- [Naumov M. et al. «Deep Learning Recommendation Model for Personalization and Recommendation Systems» (2019)](https://arxiv.org/abs/1906.00091) — оригинал DLRM от Meta. Читать ради раздела про параллелизм: там объясняют, почему таблицы шардируют, а MLP реплицируют.
- [Zhou G. et al. «Deep Interest Network for Click-Through Rate Prediction» (KDD 2018)](https://arxiv.org/abs/1706.06978) — DIN. Кроме внимания, там есть два практичных сюжета: активация Dice и mini-batch-aware регуляризация для гигантских разреженных слоёв.
- [Zhou G. et al. «Deep Interest Evolution Network for Click-Through Rate Prediction» (AAAI 2019)](https://arxiv.org/abs/1809.03672) — DIEN: вспомогательный лосс и AUGRU. Читать после DIN, ради понимания, что даёт явное моделирование эволюции интереса и сколько это стоит.
- **Ma J. et al. «Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts» (KDD 2018, Google)** — оригинал MMoE. Ключевой для главы раздел — синтетические эксперименты с регулируемой корреляцией задач; задача 5 из §13 воспроизводит именно его.
- **Tang H. et al. «Progressive Layered Extraction (PLE)» (RecSys 2020, Tencent)** — эффект качелей и его лечение. Лучшая работа по многозадачности в рекомендациях за последние годы; ищется по названию в ACM Digital Library.
- **Zhao Z. et al. «Recommending What Video to Watch Next: A Multitask Ranking System» (RecSys 2019, Google)** — описание продовой системы YouTube: MMoE на несколько целей плюс shallow tower для позиционного биаса из [прошлой главы](../docs/06-recsys/07-learning-to-rank.md). Самый полезный текст, если нужно увидеть, как всё это собирается вместе.
- **He X. et al. «Practical Lessons from Predicting Clicks on Ads at Facebook» (ADKDD 2014)** — откуда взялись нормализованная энтропия и формула поправки после даунсэмплинга негативов. Старая, но по калибровке и по инженерии CTR не устарела.
- **McMahan H.B. et al. «Ad Click Prediction: a View from the Trenches» (KDD 2013, Google)** — FTRL-Proximal, память под признаки, вероятностное отбрасывание редких признаков, мониторинг калибровки. Читать ради инженерной части, а не ради алгоритма.
- [TorchRec](https://github.com/pytorch/torchrec) — библиотека PyTorch для рекомендательных моделей с шардированными эмбеддингами. Смотреть `EmbeddingBagCollection` и планировщик шардирования, чтобы понять, как считается размещение таблиц по устройствам.
- [DeepCTR-Torch](https://github.com/shenweichen/DeepCTR-Torch) — компактные реализации DIN, DIEN, DeepFM, MMoE в одном стиле. Удобно, чтобы за вечер сравнить архитектуры на одних данных.

### [Последовательные рекомендации](../docs/06-recsys/09-sequential-recsys.md)

- [Hidasi B. et al. «Session-based Recommendations with Recurrent Neural Networks» (2016)](https://arxiv.org/abs/1511.06939) — GRU4Rec, первоисточник. Читать ради постановки сессионной задачи, session-parallel мини-батчей и лоссов BPR/TOP1: это разделы 3.1–3.2.
- [Hidasi B., Karatzoglou A. «Recurrent Neural Networks with Top-k Gains for Session-based Recommendations» (2018)](https://arxiv.org/abs/1706.03847) — продолжение: разбор затухания градиента при большом числе негативов и вывод BPR-max. Полезно всем, кто настраивает ранжирующие лоссы, а не только в сессионных задачах.
- [Kang W.-C., McAuley J. «Self-Attentive Sequential Recommendation» (2018)](https://arxiv.org/abs/1808.09781) — SASRec. Компактная статья; смотреть раздел с архитектурой и таблицу абляций по числу блоков и длине последовательности — оттуда берутся дефолтные гиперпараметры.
- [Sun F. et al. «BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer» (2019)](https://arxiv.org/abs/1904.06690) — BERT4Rec и задача Cloze. Читать вместе со следующим пунктом, иначе картина будет неполной.
- [Ferrari Dacrema M., Cremonesi P., Jannach D. «Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches» (2019)](https://arxiv.org/abs/1907.06902) — обязательное чтение. Методология сравнения, разбор конкретных провалов, список сильных бейзлайнов, которые надо настраивать.
- **Petrov A., Macdonald C. «A Systematic Review and Replicability Study of BERT4Rec for Sequential Recommendation», RecSys 2022** — честная попытка воспроизвести BERT4Rec: сколько эпох реально нужно и что получается при равном бюджете обучения.
- **Klenitskiy A., Vasilev A. «Turning Dross Into Gold Loss: Is BERT4Rec Really Better Than SASRec?», RecSys 2023** — короткая работа с сильным выводом: замена лосса SASRec на полную кросс-энтропию убирает разрыв. Полезно как пример того, как «архитектурное» преимущество оказывается преимуществом функции потерь.
- **Krichene W., Rendle S. «On Sampled Metrics for Item Recommendation», KDD 2020** — почему нельзя оценивать на 100 негативах. Читать ради раздела с контрпримерами, где порядок моделей переворачивается.
- [Документация RecBole](https://recbole.io/) — фреймворк с реализациями GRU4Rec, SASRec, BERT4Rec и единым протоколом оценки. Удобен именно тем, что даёт одинаковые условия для всех моделей — то, чего не хватает в статьях.

### [Графовые рекомендации](../docs/06-recsys/10-graph-recsys.md)

- [Kipf T., Welling M. «Semi-Supervised Classification with Graph Convolutional Networks» (2016)](https://arxiv.org/abs/1609.02907) — исходный GCN. Читать ради вывода нормировки $D^{-1/2}AD^{-1/2}$ из спектральной свёртки: это объясняет, откуда взялся корень.
- [Hamilton W., Ying R., Leskovec J. «Inductive Representation Learning on Large Graphs» (2017)](https://arxiv.org/abs/1706.02216) — GraphSAGE. Ключевые разделы: сэмплирование соседей и сравнение агрегаторов (mean / LSTM / max-pool).
- [Ying R. et al. «Graph Convolutional Neural Networks for Web-Scale Recommender Systems» (2018)](https://arxiv.org/abs/1806.01973) — PinSage. Читать целиком как инженерный текст: раздел про curriculum с hard negatives и про MapReduce-инференс полезнее архитектурной части.
- [Wang X. et al. «Neural Graph Collaborative Filtering» (2019)](https://arxiv.org/abs/1905.08108) — NGCF. Нужна как точка отсчёта, чтобы понять, что именно удаляли в LightGCN.
- [He X. et al. «LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation» (2020)](https://arxiv.org/abs/2002.02126) — главная статья главы. Смотреть таблицу абляций: там по шагам видно, как удаление каждой компоненты влияет на метрику.
- [Li Q., Han Z., Wu X.-M. «Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning» (2018)](https://arxiv.org/abs/1801.07606) — формальный анализ over-smoothing: почему глубокие GCN вырождаются.
- [Chiang W.-L. et al. «Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks» (2019)](https://arxiv.org/abs/1905.07953) и [Zeng H. et al. «GraphSAINT: Graph Sampling Based Inductive Learning Method» (2019)](https://arxiv.org/abs/1907.04931) — два практичных способа обучать глубокие GNN на больших графах. Читать, когда упрётесь во взрыв окрестности.
- [Steck H. «Embarrassingly Shallow Autoencoders for Sparse Data» (2019)](https://arxiv.org/abs/1905.03375) — EASE. Обязательный бейзлайн: замкнутое решение без обучения, которое на многих датасетах стоит вплотную к графовым моделям. Прочитайте до того, как начнёте внедрять LightGCN.
- [Wu J. et al. «Self-supervised Graph Learning for Recommendation» (2020)](https://arxiv.org/abs/2010.10683) — SGL: контрастивная регуляризация поверх LightGCN, один из немногих приростов, который устойчиво воспроизводится.
- [Документация DGL](https://www.dgl.ai/) и [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/) — рабочие инструменты: сэмплеры соседей, разбиения графа, распределённое обучение. Начинать с их примеров, а не со своей реализации, если граф больше десятка миллионов рёбер.

### [LLM в рекомендациях](../docs/06-recsys/11-llm-recsys.md)

- [Rajput S. et al. «Recommender Systems with Generative Retrieval» (2023)](https://arxiv.org/abs/2305.05065) — TIGER. Главная статья §5. Смотреть раздел про RQ-VAE и про обработку коллизий, а также эксперименты на холодных айтемах.
- [Lee D. et al. «Autoregressive Image Generation using Residual Quantization» (2022)](https://arxiv.org/abs/2203.01941) — откуда взялась остаточная квантизация. Полезно для понимания, почему уровней несколько и как устроен лосс.
- [Hou Y. et al. «Large Language Models are Zero-Shot Rankers for Recommender Systems» (2023)](https://arxiv.org/abs/2305.08845) — систематический разбор LLM-ранкера: позиционный биас, биас популярности, проблема восприятия порядка истории, приёмы вроде бутстрапа и recency-focused промптинга.
- [Sun W. et al. «Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents» (2023)](https://arxiv.org/abs/2304.09542) — RankGPT: листовое ранжирование скользящим окном и дистилляция способности ранжировать в существенно меньшую специализированную модель. Ключевая работа для §9.
- [Geng S. et al. «Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5)» (2022)](https://arxiv.org/abs/2203.13366) — P5. Читать ради идеи единого интерфейса и ради понимания, почему id-как-токены не масштабируются.
- [Hou Y. et al. «Towards Universal Sequence Representation Learning for Recommender Systems» (2022)](https://arxiv.org/abs/2206.05941) — UniSRec: как правильно приводить текстовые представления айтемов в пространство рекомендательной модели адаптером. Прямая опора для §3.
- **Singh A. et al. «Better Generalization with Semantic IDs: A Case Study in Ranking for Recommendations», RecSys 2024** — кейс Google по использованию semantic IDs как признаков в ранжировании YouTube. Лучший аргумент в пользу «скромной» версии идеи из §5.
- **Ferrari Dacrema M. et al. «Are We Really Making Much Progress?» (2019)** и связанные работы по воспроизводимости — методологический фундамент для критической оценки любых заявленных приростов в этой области; подробнее в [главе про последовательные модели](../docs/06-recsys/09-sequential-recsys.md).

### [Холодный старт и смещения](../docs/06-recsys/12-cold-start-and-bias.md)

- [Schnabel T. et al. «Recommendations as Treatments: Debiasing Learning and Evaluation» (ICML 2016)](https://arxiv.org/abs/1602.05352) — фундамент propensity-подхода в рекомендациях: постановка MNAR, IPS-оценка риска, оценка propensity, датасет Coat. Читать вместе с §8 и §10.
- [Joachims T., Swaminathan A., Schnabel T. «Unbiased Learning-to-Rank with Biased Feedback» (WSDM 2017)](https://arxiv.org/abs/1608.04468) — каноническая работа про позиционный биас и IPS в ранжировании, включая swap-интервенцию для оценки propensity. Продолжение §7.
- [Dudík M., Langford J., Li L. «Doubly Robust Policy Evaluation and Learning» (ICML 2011)](https://arxiv.org/abs/1103.4601) — первоисточник DR-оценки; смотреть ради разбора, когда DR выигрывает у IPS, а когда нет.
- **Jiang R. et al. «Degenerate Feedback Loops in Recommender Systems» (DeepMind, AIES 2019)** — формальная модель вырождения выдачи и роль эксплорации в его замедлении. Теоретическая опора §9.
- **Chaney A., Stewart B., Engelhardt B. «How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility» (RecSys 2018)** — симуляционное исследование гомогенизации: система, обученная на собственных логах, снижает разнообразие между пользователями.
- **Abdollahpouri H. et al. — серия работ про popularity bias в рекомендациях (2019–2021)** — метрики перекоса, усиление относительно данных, влияние на группы пользователей. Полезны как источник аккуратных определений метрик из §6.
- **Steck H. «Calibrated Recommendations» (RecSys 2018)** — калибровка распределения категорий в выдаче под профиль пользователя; практичный способ бороться с вытеснением редких интересов.
- **Wang X. et al. «Position Bias Estimation for Unbiased Learning to Rank in Personal Search» (WSDM 2018, Google)** — regression-EM для оценки propensity без интервенций; способ 4 из §7.
- [Eugene Yan. «Counterfactual Evaluation for Recommendation Systems»](https://eugeneyan.com/writing/counterfactual-evaluation/) — инженерный обзор off-policy оценки: что логировать, какие оценщики брать, где ломается. Хороший мост к [следующей главе](../docs/06-recsys/13-exploration-and-bandits.md).

### [Эксплорация и бандиты](../docs/06-recsys/13-exploration-and-bandits.md)

- [Slivkins A. «Introduction to Multi-Armed Bandits»](https://arxiv.org/abs/1904.07272) — если нужен один источник, берите этот: аккуратные доказательства для UCB и Thompson sampling на уровне, который реально читается инженером. Главы 1–2 закрывают §2–§6 этой главы, глава про контекстные бандиты — §7.
- **Lattimore T., Szepesvári C. «Bandit Algorithms» (Cambridge University Press, 2020)** — полный и более тяжёлый справочник по всем видам бандитов, включая линейные и состязательные; свободно доступен на сайте первого автора. Брать как справочник, а не читать подряд.
- **Auer P., Cesa-Bianchi N., Fischer P. «Finite-time Analysis of the Multiarmed Bandit Problem» (Machine Learning, 2002)** — первоисточник UCB1 и его анализа. Вывод из §4 — оттуда.
- [Li L., Chu W., Langford J., Schapire R. «A Contextual-Bandit Approach to Personalized News Article Recommendation» (WWW 2010)](https://arxiv.org/abs/1003.0146) — LinUCB и первая крупная индустриальная проверка контекстных бандитов (Yahoo! News). Читать вместе с §7.
- **Chapelle O., Li L. «An Empirical Evaluation of Thompson Sampling» (NIPS 2011)** — работа, вернувшая TS в практику: сравнение с UCB на рекламных данных, разбор поведения при задержанной обратной связи. Прямая опора для §6 и §10.
- [Agrawal S., Goyal N. «Analysis of Thompson Sampling for the Multi-armed Bandit Problem» (2012)](https://arxiv.org/abs/1111.1797) — первое доказательство логарифмического регрета TS; там же линейная версия ([Thompson Sampling for Contextual Bandits with Linear Payoffs](https://arxiv.org/abs/1209.3352)).
- [Dudík M., Langford J., Li L. «Doubly Robust Policy Evaluation and Learning» (ICML 2011)](https://arxiv.org/abs/1103.4601) — DR-оценка для контекстных бандитов, разбор компромисса смещение/дисперсия. Основа §8.
- **Swaminathan A., Joachims T. «The Self-Normalized Estimator for Counterfactual Learning» (NIPS 2015)** — почему SNIPS устойчивее IPS и что такое propensity overfitting.
- [Open Bandit Pipeline (ZOZO)](https://github.com/st-tech/zr-obp) — библиотека и датасет с настоящими залогированными propensity: лучший способ потрогать off-policy оценку на реальных данных, а не на синтетике. Пригодится для задачи 4.
- [Vowpal Wabbit](https://vowpalwabbit.org/) — производственная реализация контекстных бандитов и off-policy обучения; полезна как референс того, как это устроено инженерно.

### [Рекомендации в продакшене](../docs/06-recsys/14-recsys-in-production.md)

- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы про feature engineering, батч/онлайн-инференс и мониторинг закрывают §4–6 этой главы на более общем материале, не только рекомендациях.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 29–32 прямо про train/serve skew и логирование признаков в момент предсказания; это ровно §5.
- [Malkov, Yashunin. «Efficient and robust approximate nearest neighbor search using HNSW» (arXiv:1603.09320)](https://arxiv.org/abs/1603.09320) — первоисточник по HNSW: параметры $M$, `efConstruction`, `efSearch` и их влияние на память и recall, из которого выведена оценка размера индекса в §7.
- [Документация Feast](https://docs.feast.dev/) — хорошая иллюстрация разделения офлайн- и онлайн-хранилищ и механики point-in-time join; читать как референс архитектуры, даже если внедрять будете не Feast.
- [Faiss wiki](https://github.com/facebookresearch/faiss/wiki) — практические рецепты выбора типа индекса под объём и память; полезно вместе с §7 при выборе между HNSW и IVF-PQ.
- [Документация k6](https://k6.io/docs/) — сценарии `ramping-arrival-rate` и пороги, на которых построен §11.
- **Covington, Adams, Sargin. «Deep Neural Networks for YouTube Recommendations» (RecSys 2016)** — классика про двухстадийность и про то, как продуктовые ограничения формируют архитектуру; ищите по названию, статья есть в свободном доступе в материалах RecSys.
- [Eugene Yan. «Applied ML»](https://github.com/eugeneyan/applied-ml) — раздел про рекомендации: десятки инженерных разборов от компаний с реальными числами по латентности, объёмам индексов и каденции обновлений.

### [Онлайн-оценка рекомендаций](../docs/06-recsys/15-recsys-online-evaluation.md)

- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments» (Cambridge University Press, 2020)** — основная книга по онлайн-экспериментам. Главы про метрики, интерференцию и долгосрочные эффекты продолжают §4, §6 и §7.
- **Radlinski, Kurup, Joachims. «How Does Clickthrough Data Reflect Retrieval Quality?» (CIKM 2008)** — первоисточник team-draft interleaving; там же разобрано, почему наивное перемешивание даёт смещение.
- **Chapelle, Joachims, Radlinski, Yue. «Large-Scale Validation and Analysis of Interleaved Search Evaluation» (ACM TOIS, 2012)** — масштабная проверка интерливинга на боевом трафике и количественные оценки выигрыша по чувствительности; ищите по названию.
- **Dmitriev, Gupta, Kim, Vaz. «A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments» (KDD 2017)** — двенадцать разобранных ошибок интерпретации, большая часть из которых встречается именно в рекомендациях.
- **Deng, Xu, Kohavi, Walker. «Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data» (WSDM 2013)** — оригинальная статья про CUPED; прямое продолжение §9, шаг «не хватило мощности». См. также [снижение дисперсии](../docs/10-ab-testing/03-variance-reduction.md).
- **Gomez-Uribe, Hunt. «The Netflix Recommender System: Algorithms, Business Value, and Innovation» (ACM TMIS, 2015)** — как рекомендательная команда связывает офлайн-оценку, A/B и долгосрочную бизнес-ценность; полезно как образец разговора о деньгах.
- [Eugene Yan. «Applied ML»](https://github.com/eugeneyan/applied-ml) — раздел про эксперименты и метрики: инженерные разборы от компаний с описанием реальных протоколов онлайн-оценки.

## Выкатка в прод / MLOps

### [Жизненный цикл ML-системы](../docs/07-mlops/01-ml-lifecycle.md)

- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — первоисточник §4. Короткая (9 страниц) и её реально спрашивают. Читать целиком, особенно разделы про CACE, glue code и configuration debt.
- [Google Cloud. «MLOps: Continuous delivery and automation pipelines in machine learning»](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — первоисточник классификации уровней 0/1/2 из §5, со схемами компонентов каждого уровня.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — 43 правила из практики. Для этой главы особенно правила 1–8 (не делайте ML, пока не нужно; сначала инфраструктура, потом модель) и 29–32 (про train/serve skew).
- **Breck et al. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (IEEE Big Data, 2017)** — 28 конкретных проверок готовности ML-системы к проду, сгруппированных по данным, модели, инфраструктуре и мониторингу. Отличный чек-лист для аудита из задачи 1; используется в главе [CI/CD для ML](../docs/07-mlops/07-ci-cd-for-ml.md).
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы 1–2 и 8–9 закрывают жизненный цикл и эксплуатацию с большим количеством практических деталей.
- **Martin Kleppmann. «Designing Data-Intensive Applications»** — не про ML, но глава про эволюцию схем и совместимость данных — обязательное чтение перед [следующей главой](../docs/07-mlops/02-reproducibility-and-tracking.md) и главой про [контракты данных](../docs/07-mlops/03-data-and-feature-store.md).

### [Воспроизводимость и трекинг](../docs/07-mlops/02-reproducibility-and-tracking.md)

- [PyTorch. «Reproducibility»](https://pytorch.org/docs/stable/notes/randomness.html) — официальная страница про детерминизм: список недетерминированных операций, `use_deterministic_algorithms`, требования cuBLAS, поведение `DataLoader`. Короткая и обязательная к прочтению.
- [DVC. Документация](https://dvc.org/doc) — разделы Data Management (как устроен кэш и remote) и Pipelines (`dvc.yaml`, `dvc.lock`, `dvc repro`). Читать после §4 этой главы.
- [MLflow. Документация](https://mlflow.org/docs/latest/) — разделы Tracking, Models и Model Registry. Обратите внимание на страницу про алиасы и депрекацию стадий: это то, что часто устарело в чужих туториалах.
- [Hydra. Документация](https://hydra.cc/docs/intro/) — композиция конфигураций, `--multirun`, структурированные конфиги. Раздел про structured configs полезен вместе с pydantic.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — раздел про configuration debt прямо описывает требования из §7.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — глава 6 (Model Development and Offline Evaluation), раздел про эксперимент-трекинг и версионирование, с обсуждением того, почему версионирование данных сложнее версионирования кода.
- [Great Expectations. Документация](https://docs.greatexpectations.io/) — пригодится для задачи 5 предыдущей главы и для [качества данных](../docs/09-monitoring/02-data-quality.md): ассерты на данные как код, версионируемые вместе с пайплайном.

### [Данные и feature store](../docs/07-mlops/03-data-and-feature-store.md)

- [Feast. Документация](https://docs.feast.dev/) — открытый feature store. Читать разделы про концепции (entity, feature view, feature service), про point-in-time joins и про материализацию: там формализовано ровно то, что разобрано в §4 и §6, включая роль второй временной метки.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 29–32 посвящены train/serve skew напрямую. Правило 29 («лучший способ добиться того, чтобы обучение соответствовало сервингу, — сохранять набор признаков, использованный во время сервинга, и подавать эти признаки в лог») — это ровно механизм из §5.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы 3–5 (Data Engineering Fundamentals, Training Data, Feature Engineering). Раздел про data leakage и про train/serve skew с большим количеством примеров из индустрии.
- [Uber Engineering. «Michelangelo: Uber's Machine Learning Platform»](https://www.uber.com/blog/michelangelo-machine-learning-platform/) — описание первой широко известной production-платформы с feature store; полезно как источник архитектурных решений и чисел.
- [Airbnb. Chronon (ранее Zipline) — открытый feature engineering framework](https://github.com/airbnb/chronon) — особенно материалы про backfill и про согласование батчевых и стриминговых определений одной фичи; это самая сложная часть темы.
- **Martin Kleppmann. «Designing Data-Intensive Applications»** — глава 4 (Encoding and Evolution) — первоисточник по режимам совместимости схем из §2, разобранный гораздо подробнее.
- [Apache Iceberg. Документация](https://iceberg.apache.org/docs/latest/) — раздел про снапшоты и time travel: механика того, как версионируется таблица, о которой шла речь в [предыдущей главе](../docs/07-mlops/02-reproducibility-and-tracking.md).
- [Great Expectations. Документация](https://docs.greatexpectations.io/) — практическая реализация проверок контракта данных как кода; см. также [качество данных](../docs/09-monitoring/02-data-quality.md).

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

### [CI/CD для ML](../docs/07-mlops/07-ci-cd-for-ml.md)

- **Breck, Cai, Nielsen, Salib, Sculley. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (IEEE Big Data, 2017)** — первоисточник рубрики из §7. Искать по названию в публикациях Google Research. Читать целиком: там на каждый из 28 пунктов есть объяснение, зачем он и что ломается без него.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — почему ML-код составляет малую часть системы и откуда берётся стоимость поддержки. Раздел про configuration debt и про «pipeline jungles» объясняет, зачем вообще нужен структурированный CI.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 1–10 про инфраструктуру и метрики, правило 29 («лучший способ убедиться, что вы обучаете так же, как сервите — логировать признаки в момент предсказания») — прямо про §4.
- [Документация GitHub Actions](https://docs.github.com/en/actions) — разделы про `concurrency`, reusable workflows, environments с required reviewers и OIDC. Это ровно те механизмы, на которых держится пайплайн из §9.
- [Документация MLflow](https://mlflow.org/docs/latest/index.html) — Model Registry, стадии и алиасы, `infer_signature`. Нужна для шага регистрации из §9.
- [pytest](https://docs.pytest.org/) — фикстуры, параметризация, маркеры. Всё в §4–5 держится на них; см. также [тесты и качество кода в ML](../docs/12-coding/07-testing-and-code-quality.md).
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы про тестирование в продакшене и про continual learning; там же хороший разбор частоты переобучения.

### [Стратегии выкатки](../docs/07-mlops/08-deployment-strategies.md)

- [Google SRE Workbook, глава «Canarying Releases»](https://sre.google/workbook/canarying-releases/) — первоисточник схемы с baseline-группой и разбор того, как выбирать метрики и длительность ступеней. Читать целиком, это 20 страниц.
- [Argo Rollouts: документация](https://argo-rollouts.readthedocs.io/en/stable/) — разделы Canary Strategy и Analysis. Практический стандарт для канареек в Kubernetes; примеры `AnalysisTemplate` там богаче, чем в этой главе.
- [Istio: Traffic Mirroring](https://istio.io/latest/docs/tasks/traffic-management/mirroring/) — как включить shadow за пять минут, если у вас есть меш.
- [Pete Hodgson. «Feature Toggles (aka Feature Flags)»](https://martinfowler.com/articles/feature-toggles.html) — классификация флагов по времени жизни и по динамичности, и главное — про то, как они превращаются в технический долг.
- [Martin Fowler. «BlueGreenDeployment»](https://martinfowler.com/bliki/BlueGreenDeployment.html) — короткая заметка-первоисточник термина; полезна разбором проблемы с состоянием и миграциями БД.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022), глава про деплой и мониторинг** — та же лестница выкатки, но с уклоном в связь с мониторингом качества.

### [Оптимизация инференса](../docs/07-mlops/09-inference-optimization.md)

- [Документация ONNX Runtime](https://onnxruntime.ai/docs/) — разделы Performance (граф-оптимизации, настройки числа потоков) и Quantization. Практический стандарт для CPU-инференса; настройки `intra_op_num_threads` там объяснены лучше, чем где-либо.
- [Документация NVIDIA TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/) — когда решите, что экономия оправдывает недели работы. Начинать с раздела про построение engine и про калибровку int8.
- [PyTorch: `torch.compile`](https://pytorch.org/docs/stable/generated/torch.compile.html) и [`torch.profiler`](https://pytorch.org/docs/stable/profiler.html) — режимы компиляции, причины рекомпиляций и как читать таблицу операторов в профайлере.
- [Hinton, Vinyals, Dean. «Distilling the Knowledge in a Neural Network» (2015)](https://arxiv.org/abs/1503.02531) — первоисточник дистилляции; там же вывод множителя $T^2$.
- [Sanh et al. «DistilBERT» (2019)](https://arxiv.org/abs/1910.01108) — рабочий рецепт дистилляции энкодера с числами по скорости и качеству; полезен как ориентир для своей задачи.
- [Dettmers et al. «LLM.int8()» (2022)](https://arxiv.org/abs/2208.07339) — про выбросы в активациях трансформеров и почему наивная int8-квантизация ломается на больших моделях.
- [Michel, Levy, Neubig. «Are Sixteen Heads Really Better than One?» (2019)](https://arxiv.org/abs/1905.10650) — сколько голов внимания можно удалить без потери качества; хорошая калибровка ожиданий от структурированного прунинга.
- [py-spy](https://github.com/benfred/py-spy) — сэмплирующий профайлер, который можно запустить на живом прод-процессе. Инструмент, который стоит освоить до всего остального.
- **Dean, Barroso. «The Tail at Scale», Communications of the ACM, 2013** — классическая статья про природу хвостов в распределённых системах и про hedged requests.

### [Стоимость и ёмкость](../docs/07-mlops/10-cost-and-capacity.md)

- [Kubernetes: Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) — как именно считается желаемое число реплик и что делают окна стабилизации; читать перед настройкой асимметричных политик из §6.
- [KEDA: документация](https://keda.sh/docs/) — скейлинг по произвольным метрикам, включая Prometheus и длину очереди Kafka. Именно то, что нужно ML-сервису вместо скейлинга по CPU.
- [FinOps Foundation](https://www.finops.org/) — фреймворк управления облачными затратами: аллокация расходов по командам, юнит-экономика, практики резервирования. Полезно, когда ваш сервис перестал быть единственным в компании.
- [Hoffmann et al. «Training Compute-Optimal Large Language Models» (Chinchilla, 2022)](https://arxiv.org/abs/2203.15556) — откуда берётся оценка $6ND$ и как соотносить бюджет обучения с размером модели и объёмом данных.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — про стоимость владения, которая не видна в смете на инфраструктуру.
- **Документация по ценам вашего облака** — скучный, но обязательный источник: соотношения цен между типами инстансов, условия committed-скидок и правила тарификации egress меняются, и считать надо по актуальному прайсу, а не по числам из учебника.

## Big Data

### [Хранение данных](../docs/08-big-data/01-storage-and-formats.md)

- [Apache Parquet — официальная документация](https://parquet.apache.org/docs/) — раздел «File Format» описывает ровно ту иерархию, что в §3, а «Encodings» — все кодировки с точными правилами. Читать после этой главы, чтобы уточнить детали.
- [Спецификация формата Parquet (репозиторий `apache/parquet-format`)](https://github.com/apache/parquet-format) — первоисточник: thrift-схема метаданных, описание column index и bloom-фильтров. Нужен, когда вы отлаживаете реальную проблему со статистиками.
- [Apache Iceberg — спецификация таблицы](https://iceberg.apache.org/spec/) — лучший текст, чтобы понять, как устроен слой метаданных: metadata.json → manifest list → manifests. После него Delta и Hudi читаются по аналогии.
- [Delta Lake — документация](https://docs.delta.io/latest/index.html) — разделы про `OPTIMIZE`, `ZORDER`, `VACUUM` и time travel; там же явно описаны параметры retention, на которых обжигаются.
- [Apache Hudi — документация](https://hudi.apache.org/docs/overview) — читать ради раздела про copy-on-write и merge-on-read: там это объяснено подробнее, чем в конкурентах, потому что это ядро продукта.
- [Apache ORC — документация](https://orc.apache.org/docs/) и [Apache Avro — документация](https://avro.apache.org/docs/) — по разделу про эволюцию схемы в Avro стоит пройтись отдельно: правила совместимости пригодятся при работе со Schema Registry.
- [Spark SQL: работа с Parquet](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html) — все опции чтения/записи, включая `mergeSchema`, pushdown и настройки компрессии.
- **Melnik et al. «Dremel: Interactive Analysis of Web-Scale Datasets» (VLDB 2010)** — статья, из которой выросла схема definition/repetition levels. Читать, если работаете с вложенными данными.
- **Armbrust et al. «Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores» (VLDB 2020)** — инженерная мотивация табличных форматов от первого лица: что именно ломалось в озере из Parquet-файлов.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)**, глава про данные — связывает форматы хранения с задачами ML: почему выбор формата влияет на скорость итераций дата-сайентиста.

### [SQL для MLE](../docs/08-big-data/02-sql-for-mle.md)

- [PostgreSQL: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — официальный разбор узлов плана и единиц стоимости. Читать целиком один раз, потом держать как справочник; после этого чужие планы перестают быть шифром.
- [PostgreSQL: Window Functions Tutorial](https://www.postgresql.org/docs/current/tutorial-window.html) и [Window Function Calls](https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-WINDOW-FUNCTIONS) — единственное место, где правила рамок и дефолтов написаны точно, а не «примерно как обычно».
- **Markus Winand. «SQL Performance Explained»** и его сайт [use-the-index-luke.com](https://use-the-index-luke.com/) — как индексы работают физически и почему предикат перестаёт быть sargable. Лучший источник по §9.
- [modern-sql.com](https://modern-sql.com/) — того же автора, про то, что появилось в стандарте после SQL-92: оконные функции, `FILTER`, `LATERAL`, рекурсивные CTE, с матрицей поддержки по СУБД. Полезно, чтобы не писать в Spark то, что есть только в Postgres.
- [Spark SQL Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — официальный список параметров: бродкаст-порог, AQE, skew join. Значения оттуда стоит помнить наизусть для собеседования.
- [ClickHouse SQL Reference](https://clickhouse.com/docs/en/sql-reference) — если работаете с аналитикой в реальном времени: `argMax`, `LIMIT 1 BY`, `uniqState`/`uniqMerge`, `windowFunnel` закрывают половину задач из §11 одной функцией.

### [Spark: как он работает](../docs/08-big-data/03-spark-fundamentals.md)

- [Официальная документация: Spark Configuration](https://spark.apache.org/docs/latest/configuration.html) — единственный источник актуальных значений по умолчанию. Прочитайте разделы Application Properties, Execution Behavior, Memory Management и Shuffle Behavior целиком: половина вопросов по производительности закрывается знанием дефолтов.
- [Официальная документация: SQL Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — бродкаст-порог, AQE, хинты джойнов, кэширование. Короткая страница, которую стоит помнить наизусть.
- [Официальная документация: Tuning Spark](https://spark.apache.org/docs/latest/tuning.html) — про сериализацию, память и уровень параллелизма; именно отсюда берётся правило «2–3 задачи на ядро» и рекомендации по GC.
- [Официальная документация: Web UI](https://spark.apache.org/docs/latest/web-ui.html) — что означает каждая колонка на вкладках Jobs, Stages, Storage, SQL. Обязательно к прочтению перед следующей главой.
- [PySpark User Guide: Apache Arrow in PySpark](https://spark.apache.org/docs/latest/api/python/user_guide/sql/arrow_pandas.html) — все формы pandas UDF с примерами, настройки Arrow и список ограничений по типам.
- **Zaharia et al. «Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing» (NSDI 2012)** — исходная статья про RDD. Читать ради понимания, почему линидж выбран вместо репликации и что такое narrow/wide зависимости в оригинальной формулировке.
- **Armbrust et al. «Spark SQL: Relational Data Processing in Spark» (SIGMOD 2015)** — статья про Catalyst: как устроены правила переписывания дерева и почему оптимизатор сделали расширяемым.
- **Chambers, Zaharia. «Spark: The Definitive Guide» (O'Reilly, 2018)** — самая полная книга по API и модели исполнения; части II и III закрывают всё содержание этой главы с примерами.
- **Karau, Warren. «High Performance Spark» (O'Reilly, 2017)** — про то, чего нет в документации: как думать о джойнах, перекосе и памяти. Местами устарела по версиям, но модель мышления верная.

### [Spark: производительность](../docs/08-big-data/04-spark-tuning.md)

- [Официальная документация: SQL Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — раздел про AQE с полным списком параметров и их дефолтов. Первоисточник для всего §9; значения оттуда стоит помнить.
- [Официальная документация: Spark Configuration](https://spark.apache.org/docs/latest/configuration.html) — разделы Memory Management, Shuffle Behavior, Dynamic Allocation, Scheduling. Все параметры из §13 описаны здесь с актуальными дефолтами.
- [Официальная документация: Tuning Spark](https://spark.apache.org/docs/latest/tuning.html) — память, сериализация, уровень параллелизма, настройка сборщика мусора.
- [Официальная документация: Web UI](https://spark.apache.org/docs/latest/web-ui.html) — описание каждой метрики на всех вкладках. Читать параллельно с §2, с открытым UI своей джобы.
- [Официальная документация: Running Spark on Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html) — если у вас k8s: специфика памяти пода, `shuffleTracking`, локальные тома под shuffle.
- **Karau, Warren. «High Performance Spark» (O'Reilly, 2017)** — главы про джойны и про перекос остаются лучшим разбором приёмов salting и разделения ключей, несмотря на возраст.
- **Damji et al. «Learning Spark, 2nd Edition» (O'Reilly, 2020)** — главы 7 и 8: оптимизация, кэширование, чтение UI; написана под Spark 3.x, поэтому AQE там уже есть.
- **Chambers, Zaharia. «Spark: The Definitive Guide» (O'Reilly, 2018)** — часть про developer/production-настройки: полезна как справочник по параметрам с объяснениями.

### [Потоковая обработка](../docs/08-big-data/05-streaming.md)

- [Официальная документация Apache Kafka](https://kafka.apache.org/documentation/) — раздел Design объясняет устройство лога, репликацию и ISR; раздел Configuration — единственный надёжный источник значений по умолчанию, которые меняются от версии к версии.
- **Gwen Shapira, Todd Palino, Rajini Sivaram, Krit Petty. «Kafka: The Definitive Guide», 2-е издание (O'Reilly, 2021)** — главы про продюсера, консьюмера и exactly-once закрывают §3–§6 этой главы с большей глубиной; лучшая книга по Kafka на сегодня.
- [Jay Kreps. «Questioning the Lambda Architecture» (O'Reilly Radar, 2014)](https://www.oreilly.com/radar/questioning-the-lambda-architecture/) — первоисточник каппа-архитектуры. Читать ради аргументации, а не ради схемы: там ровно тот довод про дублирование логики, который нужно уметь воспроизвести на собеседовании.
- [Документация Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) — разделы про watermark, output modes и восстановление из чекпоинта; читайте с оглядкой на версию своего кластера, поведение watermark менялось.
- [Документация Apache Flink: Event Time и Watermarks](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) — самое внятное объяснение event time, watermark и idleness во всей экосистеме, полезно даже если вы работаете на Spark.
- **Martin Kleppmann. «Designing Data-Intensive Applications» (O'Reilly, 2017)**, глава 11 «Stream Processing» — концептуальная рамка: логи, change data capture, время в стриминге, отказоустойчивость. Читать до всего остального, если хочется понимать, а не настраивать.

### [Оркестрация пайплайнов](../docs/08-big-data/06-orchestration.md)

- [Официальная документация Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html) — разделы DAG Runs (модель интервалов), Best Practices и Params. Читать обязательно с оглядкой на версию: между 2.x и 3.x поменялись `execution_date`, SLA и Datasets/Assets.
- [Airflow: Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — короткий официальный документ, из которого выросла половина §11; там же — про верхний уровень DAG-файла и про тестирование DAG'ов.
- **Bas Harenslak, Julian de Ruiter. «Data Pipelines with Apache Airflow» (Manning, 2021)** — единственная толковая книга по Airflow; главы про идемпотентность, backfill и про то, как встроить обучение модели в пайплайн, ложатся ровно на §7–§12.
- [Документация Dagster: Assets](https://docs.dagster.io/) — стоит прочитать, даже если работаете на Airflow: модель «пайплайн описывает не задачи, а данные, которые он производит» меняет взгляд на проектирование и напрямую отвечает на вопрос из §16 про свежесть данных.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про инфраструктуру и переобучение: полезно как аргументация того, почему автоматизировать обучение стоит, а автоматически продвигать модель в прод — нет.

### [Распределённое обучение](../docs/08-big-data/07-distributed-training.md)

- [PyTorch: Distributed Data Parallel — заметки о дизайне](https://pytorch.org/docs/stable/notes/ddp.html) — официальное описание того, что происходит внутри DDP: хуки на градиенты, бакеты, перекрытие. Первоисточник для §3.
- [PyTorch: Getting Started with Distributed Data Parallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html) — рабочий минимальный пример; с него стоит начинать первый запуск.
- [Goyal et al. «Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour» (2017)](https://arxiv.org/abs/1706.02677) — первоисточник линейного правила масштабирования LR и warmup. Читать ради §2–§3 статьи: там ровно то рассуждение, которое нужно уметь воспроизвести на собеседовании.
- [Rajbhandari et al. «ZeRO: Memory Optimizations Toward Training Trillion Parameter Models» (2019)](https://arxiv.org/abs/1910.02054) — стадии ZeRO с расчётом памяти и коммуникации для каждой. Таблицы из статьи — лучший способ запомнить, что шардируется на каждой стадии.
- [Stas Bekman. «Machine Learning Engineering Open Book»](https://github.com/stas00/ml-engineering) — практические заметки человека, который эксплуатировал большие обучающие кластеры: диагностика NCCL, отладка зависаний, реальные цифры пропускной способности, отказы железа. Самый полезный источник для §4, §10 и §12.
- [Документация NCCL](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html) — раздел про переменные окружения (`NCCL_DEBUG`, `NCCL_IB_HCA`, `NCCL_SOCKET_IFNAME`); без него отладка межузлового обучения превращается в гадание.
- **Технический отчёт Meta «The Llama 3 Herd of Models» (2024)**, раздел про инфраструктуру обучения — редкий случай, когда опубликованы реальные цифры по отказам кластера, времени восстановления и эффективности использования GPU на масштабе 16 тысяч устройств.

## Мониторинг

### [Что мониторить в ML-системе](../docs/09-monitoring/01-what-to-monitor.md)

- [Google SRE Book — «Monitoring Distributed Systems»](https://sre.google/sre-book/monitoring-distributed-systems/) — первоисточник разделения «симптомы против причин» и четырёх золотых сигналов. Читать первым, это 40 минут и ровно та база, на которой стоит вся глава.
- [Google SRE Workbook — «Alerting on SLOs»](https://sre.google/workbook/alerting-on-slos/) — подробный разбор multi-window multi-burn-rate с готовыми таблицами окон и коэффициентов. Отсюда взяты числа 14.4 / 6 / 1 из §3.
- [Prometheus: типы метрик](https://prometheus.io/docs/concepts/metric_types/) и [практика работы с гистограммами](https://prometheus.io/docs/practices/histograms/) — почему `histogram_quantile` даёт приближение и как выбирать бакеты под свой SLA.
- [Prometheus: практика инструментирования](https://prometheus.io/docs/practices/instrumentation/) и [практика алертинга](https://prometheus.io/docs/practices/alerting/) — что именно измерять в сервисе и как не завести шумное правило.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 8, 14 и особенно блок про мониторинг свежести данных и train/serve skew; короткий и очень прикладной текст.
- **Google. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (2017)** — рубрика из 28 тестов, четыре из них полностью про мониторинг. Полезно пройти по ней своим сервисом и получить честную оценку в баллах; ищется по названию.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — глава «Data Distribution Shifts and Monitoring»: систематизация того, что мониторить, и разбор задержки обратной связи.
- **Google. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)** — откуда вообще берётся мысль, что ML-система деградирует сама по себе; читать вместе с [главой про жизненный цикл](../docs/07-mlops/01-ml-lifecycle.md).

### [Качество данных](../docs/09-monitoring/02-data-quality.md)

- [Great Expectations — документация](https://docs.greatexpectations.io/) — начните с Core concepts и списка встроенных ожиданий: он сам по себе хороший чек-лист того, что вообще стоит проверять. Обязательно смотрите на версию, API 0.18 и 1.x различаются.
- [pandera — документация](https://pandera.readthedocs.io/) — типизированные схемы датафреймов, которые естественно ложатся на pytest. Хороший выбор, когда фреймворк уровня GX избыточен.
- [dbt — тесты данных](https://docs.getdbt.com/docs/build/data-tests) — `unique`, `not_null`, `accepted_values`, `relationships` одной строкой YAML и выполнение в базе. Если трансформации в dbt, проверки должны быть там же.
- [PyDeequ / Deequ (AWS Labs)](https://github.com/awslabs/deequ) — проверки качества на Spark для больших объёмов, с профилированием и детекцией аномалий в метриках данных. Читать вместе со статьёй авторов «Automating Large-Scale Data Quality Verification» (VLDB 2018).
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про мониторинг свежести данных и про train/serve skew прямо относятся к этой главе; текст короткий и очень прикладной.
- **Google. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (2017)** — блок Data Tests из семи пунктов можно взять как готовый аудит своего пайплайна; ищется по названию.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы Training Data и Data Distribution Shifts and Monitoring: систематизация проблем данных и их последствий для модели.

### [Дрифт данных](../docs/09-monitoring/03-drift-detection.md)

- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)**, глава «Data Distribution Shifts and Monitoring» — лучшая систематизация видов сдвига с продуктовой точки зрения. Читать первой, если хочется общей картины до формул.
- **«Dataset Shift in Machine Learning» под ред. Quiñonero-Candela, Sugiyama, Schwaighofer, Lawrence (MIT Press, 2009)** — академический первоисточник терминологии covariate shift / prior shift. Читать главы 1–3, если нужна строгость; остальное сильно устарело по инструментам, но не по постановкам.
- [S. Rabanser, S. Günnemann, Z. Lipton. «Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift» (arXiv:1810.11953)](https://arxiv.org/abs/1810.11953) — честное экспериментальное сравнение детекторов сдвига, включая покомпонентные тесты с поправками и классификаторные тесты. Главный вывод, ради которого стоит читать: многомерные подходы систематически выигрывают у покомпонентных.
- [D. Lopez-Paz, M. Oquab. «Revisiting Classifier Two-Sample Tests» (arXiv:1610.06545)](https://arxiv.org/abs/1610.06545) — теория за детектором-классификатором из §12: почему точность классификатора является состоятельной статистикой критерия.
- [A. Gretton et al. «A Kernel Two-Sample Test», JMLR 13 (2012)](https://jmlr.org/papers/v13/gretton12a.html) — первоисточник по MMD. Читать введение и раздел про оценки статистики; остальное нужно, только если вы собираетесь реализовывать тест сами.
- [Z. Lipton, Y.-X. Wang, A. Smola. «Detecting and Correcting for Label Shift with Black Box Predictors» (arXiv:1802.03916)](https://arxiv.org/abs/1802.03916) — метод BBSE из §4: оценка нового распределения классов без меток. Один из немногих способов измерить сдвиг приоров в проде, где меток нет.
- **Naeem Siddiqi. «Credit Risk Scorecards» (Wiley)** — источник конвенции PSI 0.1/0.25. Полезно прочитать раздел про мониторинг скоркарт, чтобы понять контекст, в котором эти пороги имели смысл, и не переносить их вслепую.
- [Great Expectations — документация](https://docs.greatexpectations.io/) — проверки контрактов данных, тот самый «шаг 0» протокола из §16. Дрифт-мониторинг без проверок качества данных даёт в основном ложные тревоги.
- [Prometheus: практика работы с гистограммами](https://prometheus.io/docs/practices/histograms/) — если метрики дрифта складываются в Prometheus, читать обязательно: выбор бакетов определяет, что вы вообще увидите на графике.
- [Evidently — документация](https://docs.evidentlyai.com/) — открытая библиотека отчётов о дрифте: полезна как каталог реализованных метрик и как быстрый способ получить первый дашборд. Смотреть на то, какие тесты по умолчанию выбираются для разных типов признаков и размеров выборки.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про train/serve skew и про логирование признаков в момент предсказания напрямую относятся к тому, чтобы дрифт вообще было чем измерять.
- **Breck et al. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (Google, IEEE Big Data 2017)** — раздел про мониторинг данных содержит чек-лист проверок, который стоит просто взять и внедрить. Ищется по названию.
- **J. Lu et al. «Learning under Concept Drift: A Review»** — обзор по терминологии форм концепт-дрифта (sudden / gradual / incremental / recurring) и по методам адаптации. Читать выборочно: разделы с таксономией.

### [Деградация модели](../docs/09-monitoring/04-model-degradation.md)

- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)**, главы про мониторинг и про continual learning — лучший разбор жизни с отложенной разметкой и natural labels. Читать первой.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про логирование признаков в момент предсказания, про train/serve skew и про измерение того, что модель на самом деле делает, напрямую относятся к этой главе. Короткий текст, который стоит перечитывать раз в год.
- **Breck et al. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (Google, IEEE Big Data 2017)** — раздел «Monitoring Tests» содержит готовый чек-лист: от проверки, что модель не устарела, до проверки инвариантов предсказаний. Ищется по названию.
- **Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)** — первоисточник про петли обратной связи (direct и hidden feedback loops) и про то, почему ML-системы деградируют без единого изменения кода. Разбирается также в [жизненном цикле ML-системы](../docs/07-mlops/01-ml-lifecycle.md).
- [C. Guo et al. «On Calibration of Modern Neural Networks» (arXiv:1706.04599)](https://arxiv.org/abs/1706.04599) — откуда взялся ECE в его нынешнем виде и почему современные глубокие сети систематически переуверены. Читать раздел про измерение калибровки.
- [Prometheus: типы метрик](https://prometheus.io/docs/concepts/metric_types/) и [практика работы с гистограммами](https://prometheus.io/docs/practices/histograms/) — как складывать прокси-метрики так, чтобы потом можно было честно считать квантили.
- [Great Expectations — документация](https://docs.greatexpectations.io/) — проверки данных как первый пункт чек-листа диагностики из §8. Половина «деградаций модели» — это непройденная проверка данных.
- **Литература по reject inference в кредитном скоринге** (главы в книгах по скоркартам, например у Naeem Siddiqi) — если работаете с задачей, где у отклонённых нет меток. Читать критически: все методы опираются на непроверяемые допущения, и случайный холдаут остаётся честнее любого из них.

### [Стек наблюдаемости](../docs/09-monitoring/05-observability-stack.md)

- [Prometheus: типы метрик](https://prometheus.io/docs/concepts/metric_types/) — короткая страница, которую надо прочитать целиком до того, как писать первую метрику.
- [Prometheus: практика работы с гистограммами и summary](https://prometheus.io/docs/practices/histograms/) — ровно про то, почему `histogram_quantile` приближённый и как выбирать бакеты. Это первоисточник ответа на вопрос «почему у меня неправильный p99».
- [Prometheus: правила именования метрик](https://prometheus.io/docs/practices/naming/) — конвенции про единицы, суффикс `_total` и что должно быть меткой, а что именем.
- [Prometheus: основы PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) и [функции](https://prometheus.io/docs/prometheus/latest/querying/functions/) — читать выборочно: `rate`, `increase`, `histogram_quantile`, `offset`, `absent`, `topk`.
- [Prometheus: алертинг и правила](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) и [конфигурация Alertmanager](https://prometheus.io/docs/alerting/latest/configuration/) — разделы про `for`, группировку и `inhibit_rules`.
- [Grafana: документация](https://grafana.com/docs/grafana/latest/) — разделы про аннотации, переменные дашборда и exemplars: три вещи, которые превращают набор графиков в инструмент.
- [OpenTelemetry: документация](https://opentelemetry.io/docs/) — концепции спанов и контекста, а также разделы про Collector и процессоры семплирования.
- **Google SRE Book, глава «Practical Alerting»** и **SRE Workbook, глава «Alerting on SLOs»** — первоисточник по бюджету ошибок и multi-window multi-burn-rate. Читается за вечер и меняет отношение к порогам навсегда.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про логирование фич в момент предсказания и про train/serve skew относятся к §11 напрямую.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — глава Monitoring and Observability: систематизация того же материала с другой стороны, полезна как второй взгляд.
- [Документация Great Expectations](https://docs.greatexpectations.io/) — если проверки качества данных из [главы 02](../docs/09-monitoring/02-data-quality.md) нужно связать с метриками и алертами этой главы.

### [Инциденты](../docs/09-monitoring/06-incidents-and-runbooks.md)

- **Google SRE Book, главы «Managing Incidents», «Effective Troubleshooting» и «Postmortem Culture: Learning from Failure»** — первоисточник по ролям в инциденте, по структуре разбора и по blameless-подходу. Читается за вечер, применимо целиком.
- **Google SRE Workbook, глава «On-Call»** — практическая часть про ротацию, нагрузку на дежурного и что делать с шумными алертами.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 29–32 про train/serve skew и про логирование фич в момент предсказания напрямую относятся к сценариям §6 и §9.
- [Google. «The ML Test Score»](https://research.google/pubs/pub46555/) — чек-лист готовности ML-системы к продакшену; раздел про мониторинг и про тесты инфраструктуры можно использовать как аудит перед тем, как заводить дежурство.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — почему ML-системы ломаются способами, которых нет у обычного софта: связанность через данные, петли обратной связи, undeclared consumers.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы Monitoring and Observability и Continual Learning: тот же материал с продуктовой стороны, полезно как второй взгляд.
- [Документация Prometheus по правилам алертов](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) и [конфигурации Alertmanager](https://prometheus.io/docs/alerting/latest/configuration/) — разделы про `for`, silence и inhibit-правила, на которые опираются §10 и §13.
- [Документация Great Expectations](https://docs.greatexpectations.io/) — если по итогам постмортема нужно закрыть класс инцидентов проверками данных на входе.

### [Переобучение моделей](../docs/09-monitoring/07-retraining.md)

- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про train/serve skew, про свежесть данных и про то, что модель надо переобучать не потому, что «пора». Короткий и очень плотный текст, читать целиком.
- [Google. «The ML Test Score»](https://research.google/pubs/pub46555/) — чек-лист готовности; разделы про тестирование инфраструктуры и мониторинга напрямую описывают, что должно быть проверено в конвейере переобучения.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — разделы про петли обратной связи и про связанность через данные объясняют, почему более частое переобучение усиливает вырождение выдачи.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — глава Continual Learning and Test in Production: систематизация режимов переобучения и стадий валидации в проде, ближайший к этой главе материал.
- [Gama et al. «A Survey on Concept Drift Adaptation» (ACM Computing Surveys, 2014)](https://dl.acm.org/doi/10.1145/2523813) — академический обзор методов адаптации к дрейфу: скользящие окна, взвешивание, ансамбли с забыванием. Полезен, чтобы увидеть, что практические приёмы этой главы имеют теоретическое основание.
- [Документация LightGBM](https://lightgbm.readthedocs.io/) — разделы про `sample_weight` и про продолжение обучения (`init_model`): практическая база для §6.
- [Документация MLflow](https://mlflow.org/docs/latest/index.html) — реестр моделей, стадии и алиасы: механика, без которой откат за минуты невозможен.
- [Документация Great Expectations](https://docs.greatexpectations.io/) — проверки данных как блокирующий шаг конвейера переобучения (§8).
- **Google SRE Workbook, глава «Canarying Releases»** — про выдержку, ступени и автоматические критерии продвижения; всё применимо к моделям, если добавить расчёт мощности из §10.

## A/B-тесты

### [Дизайн эксперимента](../docs/10-ab-testing/01-experiment-design.md)

- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing» (Cambridge University Press, 2020)** — главная книга по теме, написанная людьми, построившими экспериментальную платформу Microsoft. Главы про OEC, единицу рандомизации и институциональные памятки — прямое продолжение этой главы.
- [exp-platform.com](https://exp-platform.com/) — архив статей команды Microsoft ExP, включая «Online Controlled Experiments at Large Scale» (KDD 2013) и работы про SRM. Ценность в том, что это отчёты о реальных провалах, а не учебные примеры.
- [Evan Miller. «How Not To Run An A/B Test»](https://www.evanmiller.org/how-not-to-run-an-ab-test.html) — короткая заметка про подглядывание с наглядной симуляцией. Прочитать до того, как захочется остановить тест пораньше.
- [Evan Miller. Sample Size Calculator](https://www.evanmiller.org/ab-testing/sample-size.html) — калькулятор для долей; полезен как сверка вашей собственной реализации из задачи 1.
- **Georgi Georgiev. «Statistical Methods in Online A/B Testing» (2019)** — детальный разбор мощности, MDE и последовательных методов с инженерным уклоном.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 1–10 и раздел про метрики хорошо ложатся на §3 этой главы.

### [Статистические критерии на практике](../docs/10-ab-testing/02-statistical-criteria.md)

- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments» (Cambridge University Press, 2020)** — глава про статистику эксперимента и приложение про дельта-метод; там же приводится правило $355\gamma^2$ и обсуждение тяжёлых хвостов на реальных метриках Bing.
- **Deng, Knoblich, Lu. «Applying the Delta Method in Metric Analytics» (KDD 2018)** — базовая статья про дельта-метод в A/B: ratio-метрики, кластеризованные данные, квантили. Прямое продолжение §7.
- **Budylin, Drutsa, Katsev, Tsoy. «Consistent Transformation of Ratio Metrics for Efficient Online Controlled Experiments» (WSDM 2018)** — линеаризация ratio-метрик, работа команды Яндекса. Прямое продолжение §8.
- **Boos, Hughes-Oliver. «How Large Does n Have to Be for Z and t Intervals?» (The American Statistician, 2000)** — источник правила $n > 355\gamma^2$; полезно прочитать, чтобы понимать, откуда взялась константа и к каким интервалам она относится.
- [Документация `scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) — внимательно прочитайте описания `ttest_ind`, `mannwhitneyu`, `chi2_contingency`, `fisher_exact`: дефолтные значения параметров там как раз те, которые чаще всего приводят к ошибкам.
- **Efron, Tibshirani. «An Introduction to the Bootstrap» (1993)** — классика по бутстрапу; для практики достаточно глав про перцентильный интервал и BCa.

### [Снижение дисперсии](../docs/10-ab-testing/03-variance-reduction.md)

- **Deng, Xu, Kohavi, Walker. «Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data» (WSDM 2013)** — оригинальная статья про CUPED от команды экспериментальной платформы Microsoft. Читать ради вывода и ради раздела про выбор ковариаты; там же приводятся реальные цифры снижения дисперсии на метриках Bing.
- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments» (Cambridge University Press, 2020)** — глава про снижение дисперсии собирает все методы в одну картину: CUPED, стратификацию, триггеринг, винзоризацию, смену единицы анализа. Лучшее место, чтобы понять, как они сочетаются.
- **Lin, W. «Agnostic Notes on Regression Adjustments to Experimental Data: Reexamining Freedman's Critique» (Annals of Applied Statistics, 2013)** — почему регрессионная корректировка безопасна, если добавить взаимодействия с индикатором группы. Читать после того, как разобрались с §8.
- **Инженерный блог DoorDash про CUPAC** (Control Using Predictions As Covariates) — практическое описание схемы «предсказание ML-модели как ковариата», с числами по фактическому снижению дисперсии. Ищите по названию метода.
- **Инженерные блоги Netflix, Booking.com и Airbnb про экспериментальные платформы** — там регулярно публикуют разборы снижения дисперсии на своих метриках; полезны как источник реалистичных диапазонов $\rho$ для разных типов продуктов.

### [Ловушки A/B-тестов](../docs/10-ab-testing/04-pitfalls.md)

- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing» (Cambridge University Press, 2020)** — основная книга по теме. Главы про SRM, про закон Тваймана и про «институциональную память экспериментов» прямо соответствуют этой главе. Если читать одну книгу про A/B — эту.
- **Armitage, McPherson, Rowe. «Repeated Significance Tests on Accumulating Data» (Journal of the Royal Statistical Society, 1969)** — источник таблицы инфляции $\alpha$ из §2.2. Полезно увидеть, что проблему подглядывания решили за полвека до A/B-платформ.
- **Johari, Koomen, Pekelis, Walsh. «Peeking at A/B Tests: Why It Matters, and What to Do About It» (KDD 2017)** и их же работа про always-valid inference — самая доступная экспозиция mSPRT и последовательного тестирования в продуктовом контексте.
- **Benjamini, Hochberg. «Controlling the False Discovery Rate» (JRSS B, 1995)** — оригинальная статья про FDR. Читать ради понимания, чем FDR отличается от FWER и почему для десятков вторичных метрик нужен именно он.
- **Fabijan et al. «Diagnosing Sample Ratio Mismatch in Online Controlled Experiments» (KDD 2019)** — таксономия причин SRM и практические правила диагностики; фактически расширенная версия §5.
- **Gelman, Stern. «The Difference Between "Significant" and "Not Significant" Is Not Itself Statistically Significant» (The American Statistician, 2006)** — короткая заметка, закрывающая самую частую ошибку в анализе сегментов.
- **Инженерные блоги Netflix, Booking.com, Airbnb, Spotify про экспериментальные платформы** — публикации про последовательное тестирование, SRM-детекторы и культуру экспериментов. Полезны как источник реальных чисел и архитектурных решений.

### [Сложные схемы](../docs/10-ab-testing/05-complex-designs.md)

- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments» (Cambridge University Press, 2020)** — базовая книга по A/B; главы про нарушение независимости, интерференцию и долгосрочные эффекты закрывают §2, §3 и §8 этой главы на уровне, достаточном для собеседования.
- [Ситимобил: «Switchback-эксперименты. Эпизод 1: Скрытая сила switchback»](https://habr.com/ru/companies/citymobil/articles/560426/) — русскоязычное введение в switchback от сервиса такси: почему обычный A/B нарушает SUTVA и как устроен переход к рандомизации по времени.
- [Delivery Club: «Как мы научились A/B-тестировать алгоритмы с помощью switchback-тестов»](https://habr.com/ru/companies/deliveryclub/articles/670762/) — разбор switchback в логистике; отсюда полезное для ответа число: эффекты, измеренные обычным A/B, оказывались примерно втрое выше измеренных switchback.
- [Авито: «Switchback-тесты: инфраструктура для экспериментов в условиях сетевых эффектов»](https://habr.com/ru/companies/avito/articles/1048780/) — взгляд со стороны платформы: настройка размера окна, доли трафика и весов групп в едином семантическом слое для обычного A/B и switchback.
- **Johari, Li, Liskovich, Weintraub. «Experimental Design in Two-Sided Platforms: An Analysis of Bias» (Management Science)** — основной академический источник по двусторонней рандомизации и по анализу смещения при односторонних дизайнах на маркетплейсах.
- **Abadie, Diamond, Hainmueller — работы по synthetic control (в т.ч. «Synthetic Control Methods for Comparative Case Studies», JASA 2010)** — оригинальная постановка задачи и перестановочный вывод значимости; читать, если предстоит оценивать эффект на уровне одного региона.
- **Bertrand, Duflo, Mullainathan. «How Much Should We Trust Differences-in-Differences Estimates?» (Quarterly Journal of Economics, 2004)** — почему наивные стандартные ошибки в DiD занижены и что с этим делать; короткая и очень отрезвляющая работа.
- [Hernán, Robins. «Causal Inference: What If»](https://miguelhernan.org/whatifbook) — бесплатный учебник по причинному выводу; части про потенциальные исходы и про нарушения допущений дают язык, на котором обсуждаются §2 и §7.
- [Applied Causal Inference / CausalML book](https://causalml-book.org) — современный учебник с кодом; удобен для DiD, synthetic control и разрывного дизайна на практике.
- [Документация Statsig про holdouts](https://docs.statsig.com/holdouts) — инженерное описание того, как глобальный holdout устроен внутри экспериментальной платформы: размер, срок, изоляция от раскаток, чтение результатов.

### [Бандиты против A/B](../docs/10-ab-testing/06-bandits-vs-ab.md)

- **Lattimore, Szepesvári. «Bandit Algorithms» (Cambridge University Press, 2020)** — основной современный учебник по теме; свободная электронная версия выложена авторами. Главы про регрет, нижние границы и UCB закрывают §2 и §3 на уровне сильно глубже собеседования.
- **Lai, Robbins. «Asymptotically Efficient Adaptive Allocation Rules» (Advances in Applied Mathematics, 1985)** — работа, где выведена нижняя граница регрета. Читать ради понимания, почему логарифм и почему совсем без эксплорации нельзя.
- **Chapelle, Li. «An Empirical Evaluation of Thompson Sampling» (NIPS 2011)** — работа, вернувшая Thompson sampling в практику; там же обсуждается поведение при отложенной награде, что прямо относится к §5.2.
- [«Multi Armed Bandit vs. A/B Tests in E-commerce: Confidence Interval and Hypothesis Test Power Perspectives» (KDD 2022)](https://dl.acm.org/doi/10.1145/3534678.3539144) — прямое сравнение двух подходов именно с точки зрения ширины доверительного интервала и мощности; наиболее близкая к теме главы академическая работа.
- [Optimizely: Multi-Armed Bandit (глоссарий оптимизации)](https://www.optimizely.com/optimization-glossary/multi-armed-bandit) — короткое продуктовое изложение различия: A/B — период чистой эксплорации с последующей эксплуатацией, бандит чередует их адаптивно. Полезно как формулировка для нетехнической аудитории.
- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments» (Cambridge University Press, 2020)** — раздел про адаптивные схемы и про то, почему индустриальные платформы экспериментов построены вокруг фиксированных долей, а не вокруг бандитов.

## ML System Design

### [Как проходить ML System Design](../docs/11-system-design/01-framework.md)

- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — лучшая книга по теме на сегодня. Главы про постановку задачи, feature engineering и мониторинг закрывают шаги 1–3 и 7.
- [Google. «Rules of Machine Learning: Best Practices for ML Engineering»](https://developers.google.com/machine-learning/guides/rules-of-ml) — 43 правила, выведенных из практики. Правила 1–10 стоит выучить: они ровно про то, что проверяется на этой секции.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — почему ML-система дороже в поддержке, чем кажется. Аргументы отсюда очень уместны в шаге 8.
- [Eugene Yan. «Applied ML» (подборка инженерных разборов от компаний)](https://github.com/eugeneyan/applied-ml) — сотни реальных описаний production-систем. Лучший источник конкретных чисел и архитектур.
- **Kohavi, Tang, Xu. «Trustworthy Online Controlled Experiments»** — для шага 7; см. также [раздел про A/B](../docs/10-ab-testing/01-experiment-design.md).

### [Кейс: лента рекомендаций](../docs/11-system-design/02-case-feed-ranking.md)

- **Covington, Adams, Sargin. «Deep Neural Networks for YouTube Recommendations» (RecSys 2016)** — канонический разбор двухстадийной схемы кандидаты→ранжирование с честными инженерными деталями (сэмплирование, признак возраста видео, почему предсказывают время просмотра, а не клик). Искать по названию; статья свободно доступна на сайте исследовательской группы Google.
- **Zhao et al. «Recommending What Video to Watch Next: A Multitask Ranking System» (RecSys 2019)** — многозадачное ранжирование с MMoE и отдельной башней позиционного биаса; ровно то, что описано в §5 и §9.3 этой главы.
- [Zhou et al. «Deep Interest Network for Click-Through Rate Prediction» (2017)](https://arxiv.org/abs/1706.06978) — внимание к истории пользователя вместо усреднения эмбеддингов; читать перед переходом на вариант B из §5.
- [Kang, McAuley. «Self-Attentive Sequential Recommendation» (SASRec, 2018)](https://arxiv.org/abs/1808.09781) — сессионная модель, которая закрывает холодный старт пользователя и реактивность ленты.
- [Malkov, Yashunin. «Efficient and robust approximate nearest neighbor search using HNSW» (2016)](https://arxiv.org/abs/1603.09320) — устройство индекса, от параметров которого зависят те самые 12–18 мс из бюджета.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила 1–16 почти дословно описывают лестницу усложнения из §4.

### [Кейс: поиск и ранжирование](../docs/11-system-design/03-case-search.md)

- **Robertson, Zaragoza. «The Probabilistic Relevance Framework: BM25 and Beyond» (2009)** — откуда взялась формула BM25 и что означают её параметры; читать, если хотите отвечать на вопрос «почему именно так», а не «так принято». Искать по названию, работа свободно доступна.
- [Huang et al. «Embedding-based Retrieval in Facebook Search» (KDD 2020)](https://arxiv.org/abs/2006.11632) — лучший инженерный текст про гибрид лексики и векторов в проде: негативы, слияние ветвей, обслуживание индекса. Прямо соответствует §6 этой главы.
- [Karpukhin et al. «Dense Passage Retrieval» (2020)](https://arxiv.org/abs/2004.04906) — каноническая схема двухбашенного ретривала с in-batch и hard negatives.
- [Xiong et al. «Approximate Nearest Neighbor Negative Contrastive Learning» (ANCE, 2020)](https://arxiv.org/abs/2007.00808) — итеративная добыча hard negatives через периодическую перестройку индекса.
- [Khattab, Zaharia. «ColBERT» (2020)](https://arxiv.org/abs/2004.12832) — компромисс между двухбашенкой и кросс-энкодером; полезно, когда встанет вопрос «а можно ли качество кросс-энкодера за приемлемые деньги».
- **Joachims, Swaminathan, Schnabel. «Unbiased Learning-to-Rank with Biased Feedback» (WSDM 2017)** — формальная постановка IPS для ранжирования и оценка propensity; основа §10.4.
- **Chapelle, Chang. «Yahoo! Learning to Rank Challenge Overview» (2011)** — про то, как устроены промышленные датасеты LTR и почему LambdaMART так долго держит первое место.

### [Кейс: антифрод](../docs/11-system-design/04-case-fraud-detection.md)

- **Le Borgne, Siblini, Lebichot, Bontempi. «Reproducible Machine Learning for Credit Card Fraud Detection — Practical Handbook»** (Université Libre de Bruxelles) — свободно доступная онлайн-книга с кодом. Лучший источник именно по специфике задачи: симулятор транзакций, правильная валидация с учётом задержки метки, метрики при экстремальном дисбалансе. Ищите по названию, книга выложена авторами открыто.
- **Dal Pozzolo et al. «Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy» (IEEE Transactions on Neural Networks and Learning Systems, 2018)** — статья, в которой аккуратно разобрана задержка верификации меток и предложена схема обучения с учётом того, что часть меток приходит от аналитиков быстро, а часть — от чарджбэков поздно.
- **Dal Pozzolo, Caelen, Johnson, Bontempi. «Calibrating Probability with Undersampling for Unbalanced Classification» (IEEE SSCI, 2015)** — откуда берётся формула коррекции вероятности после прореживания негативов, использованная в §5.
- [Соревнование IEEE-CIS Fraud Detection на Kaggle](https://www.kaggle.com/c/ieee-fraud-detection) — реальный анонимизированный набор транзакций; публичные решения — хороший каталог признаков (velocity, устройственные, «псевдо-идентификаторы» клиента) и наглядная демонстрация того, как участники ловили временную утечку.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про приоритет простых эвристик и про то, почему обучение на собственных решениях системы порождает петлю, здесь особенно уместны.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы про degenerate feedback loops и про мониторинг закрывают шаги 3 и 7 этого кейса.

### [Кейс: ассистент с RAG](../docs/11-system-design/05-case-rag-assistant.md)

- [Lewis et al. «Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks» (NeurIPS 2020)](https://arxiv.org/abs/2005.11401) — работа, давшая название подходу. Читать ради постановки: почему параметрическая память модели и непараметрическая память индекса решают разные задачи.
- [Karpukhin et al. «Dense Passage Retrieval for Open-Domain Question Answering» (EMNLP 2020)](https://arxiv.org/abs/2004.04906) — базовая статья про би-энкодеры и обучение с in-batch negatives; отсюда растёт вся современная практика плотного поиска.
- [Thakur et al. «BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models» (2021)](https://arxiv.org/abs/2104.08663) — главный аргумент в пользу гибрида: показывает, что плотные модели проваливаются вне домена обучения, а BM25 остаётся сильным бейзлайном.
- [Liu et al. «Lost in the Middle: How Language Models Use Long Contexts» (2023)](https://arxiv.org/abs/2307.03172) — экспериментальное обоснование того, почему «положить побольше чанков» не работает.
- [Gao et al. «Precise Zero-Shot Dense Retrieval without Relevance Labels» (HyDE, 2022)](https://arxiv.org/abs/2212.10496) — приём с гипотетическим документом; читать, чтобы понимать, когда он помогает, а когда уводит.
- [Es et al. «RAGAS: Automated Evaluation of Retrieval Augmented Generation» (2023)](https://arxiv.org/abs/2309.15217) — формализация метрик faithfulness / answer relevance / context precision. Полезно как каталог метрик, но помните про валидацию судьи из §9.
- [Asai et al. «Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection» (2023)](https://arxiv.org/abs/2310.11511) — про обучение модели решать, когда искать и когда отказываться; прямо про §7.
- [Malkov, Yashunin. «Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs» (2016)](https://arxiv.org/abs/1603.09320) — первоисточник по HNSW; нужен, чтобы отвечать на вопросы про фильтрованный поиск не наощупь.
- [Anthropic. «Introducing Contextual Retrieval» (2024)](https://www.anthropic.com/news/contextual-retrieval) — инженерный разбор приёма с контекстуализацией чанков и связки «контекстные эмбеддинги + BM25 + реранкер», с числами по приросту recall.
- **Cormack, Clarke, Buettcher. «Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods» (SIGIR 2009)** — первоисточник по RRF. Короткая статья, ищется по названию; читать ради того, чтобы понимать, откуда взялась константа 60.
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про приоритет простых эвристик и про измеримость особенно уместны на шаге 4 этого кейса.

### [Кейс: персонализация в реальном времени](../docs/11-system-design/06-case-realtime-recsys.md)

- [Hidasi et al. «Session-based Recommendations with Recurrent Neural Networks» (GRU4Rec, ICLR 2016)](https://arxiv.org/abs/1511.06939) — работа, с которой началась сессионная постановка. Читать ради формулировки задачи и обсуждения того, что сессия — не то же самое, что пользователь.
- [Kang, McAuley. «Self-Attentive Sequential Recommendation» (SASRec, ICDM 2018)](https://arxiv.org/abs/1808.09781) — трансформер для последовательных рекомендаций; база для сессионного энкодера как источника кандидатов.
- [Zhou et al. «Deep Interest Network for Click-Through Rate Prediction» (KDD 2018)](https://arxiv.org/abs/1706.06978) — внимание кандидата к истории пользователя; вариант B из §6, с честным обсуждением вычислительной цены.
- [Ferrari Dacrema, Cremonesi, Jannach. «Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches» (RecSys 2019)](https://arxiv.org/abs/1907.06902) — почему к заявленным приростам сложных сессионных моделей стоит относиться скептически и почему бейзлайны надо настраивать честно.
- **Chip Huyen. «Designing Machine Learning Systems» (O'Reilly, 2022)** — главы про batch/streaming-признаки и про train/serve skew закрывают шаги 3 и 5 этого кейса лучше, чем что-либо ещё на русском или английском.
- **Kleppmann. «Designing Data-Intensive Applications»** — главы про потоковую обработку, логи событий и гарантии доставки; нужна, чтобы отвечать на вопросы про exactly-once и партиционирование не наощупь.
- [Apache Flink. Документация по управлению состоянием и таймерам](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/fault-tolerance/state/) — практическая часть: как устроены состояние, чекпоинты и watermark. Читать перед тем, как обещать на собеседовании «посчитаем в Flink».
- [Google. «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — правила про train/serve skew и про то, что логирование признаков в момент предсказания решает большую часть проблем, здесь особенно уместны.

### [Кейс: отток и удержание](../docs/11-system-design/07-case-churn-uplift.md)

- **Radcliffe & Surry. «Real-World Uplift Modelling with Significance-Based Uplift Trees» (Stochastic Solutions, 2011)** — работа, из которой пришли и сам термин uplift, и Qini-кривая. Читать ради постановки и ради честного обсуждения того, насколько шумны эти оценки.
- **Gutierrez & Gérardy. «Causal Inference and Uplift Modelling: A Review of the Literature» (PMLR, 2017)** — компактный обзор семейства методов: two-model, преобразование класса, uplift-деревья; хорошая карта области перед углублением.
- **Künzel, Sekhon, Bickel, Yu. «Metalearners for estimating heterogeneous treatment effects using machine learning» (PNAS, 2019)** — S/T/X-learner в одном месте, с объяснением, когда какой работает; отсюда стоит взять аргументацию про слабости T-learner.
- **Athey & Imbens. «Recursive partitioning for heterogeneous causal effects» (PNAS, 2016)** — causal tree и идея honest estimation (разные подвыборки для структуры дерева и для оценок в листьях). Объясняет, почему наивные uplift-деревья переобучаются.
- [CausalML — библиотека Uber для uplift и CATE](https://github.com/uber/causalml) — реализации метаобучателей, uplift-деревьев и метрик, включая Qini; хорошая отправная точка для практики.
- [scikit-uplift — библиотека с метриками и моделями uplift](https://github.com/maks-sh/scikit-uplift) — русскоязычное сообщество, привычный sklearn-интерфейс, реализованы Qini, uplift@k и преобразование класса.
- **Diemert et al. «A Large Scale Benchmark for Uplift Modeling» (AdKDD, 2018)** — описание открытого датасета Criteo-UPLIFT с рандомизированным воздействием; редкий случай, когда можно потренироваться на настоящих экспериментальных данных.

### [Кейс: предсказание CTR в рекламе](../docs/11-system-design/08-case-ads-ctr.md)

- **McMahan et al. «Ad Click Prediction: a View from the Trenches» (KDD 2013)** — обязательное чтение по этому кейсу. FTRL-Proximal, хеширование, прореживание негативов, калибровка, экономия памяти, метрики. Почти всё, что описано в §5–§6 этой главы, взято оттуда. Искать по названию — работа свободно доступна на сайте исследовательской группы Google.
- **He et al. «Practical Lessons from Predicting Clicks on Ads at Facebook» (ADKDD 2014)** — схема GBDT + логрег, формула коррекции прореживания негативов, влияние свежести данных. Короткая и очень плотная работа.
- **Chapelle. «Modeling Delayed Feedback in Display Advertising» (KDD 2014)** — формальная модель отложенной конверсии из §10.3, включая вывод правдоподобия.
- [Naumov et al. «Deep Learning Recommendation Model» (DLRM, 2019)](https://arxiv.org/abs/1906.00091) — устройство промышленной нейросети для CTR: таблицы эмбеддингов, взаимодействия, что упирается в память.
- [Guo et al. «DeepFM» (2017)](https://arxiv.org/abs/1703.04247) и [Wang et al. «Deep & Cross Network» (2017)](https://arxiv.org/abs/1708.05123) — два способа автоматически ловить взаимодействия признаков, часто спрашиваемые по названию.
- [Cheng et al. «Wide & Deep Learning for Recommender Systems» (2016)](https://arxiv.org/abs/1606.07792) — классическая гибридная схема «запоминание + обобщение», предшественник всего перечисленного.
- **Edelman, Ostrovsky, Schwarz. «Internet Advertising and the Generalized Second-Price Auction» (2007)** — экономика GSP: почему он не является стимулосовместимым в строгом смысле и как это влияет на поведение рекламодателей. Полезно для §10.6.

## Практика кода

### [Python, который спрашивают](../docs/12-coding/01-python-for-mle.md)

- [Python Language Reference: Data model](https://docs.python.org/3/reference/datamodel.html) — первоисточник по объектам, идентичности, `__slots__`, дандер-методам и протоколам. Читать не подряд, а как справочник, когда нужен точный ответ «как это работает на самом деле».
- **Luciano Ramalho. «Fluent Python», 2-е издание (O'Reilly, 2022)** — лучшая книга по идиоматичному Python. Главы про модель данных, последовательности, функции первого класса, итераторы и конкурентность закрывают §2–§9 этой главы с большей глубиной.
- **Micha Gorelick, Ian Ozsvald. «High Performance Python», 2-е издание (O'Reilly, 2020)** — профилирование, память, GIL, многопроцессность и переход к C. Прямое продолжение §9–§10.
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html) и [документация `itertools`](https://docs.python.org/3/library/itertools.html) — итераторы, генераторы и готовые рецепты ленивой обработки; полезно прочитать целиком один раз.
- [PEP 703: Making the Global Interpreter Lock Optional in CPython](https://peps.python.org/pep-0703/) — если хотите отвечать про GIL на уровне «понимаю, а не слышал»: там разобрано, что именно защищает блокировка и какой ценой её убирают.
- [Документация `dataclasses`](https://docs.python.org/3/library/dataclasses.html) и [PEP 484 (type hints)](https://peps.python.org/pep-0484/) — для §8; дальше стоит посмотреть `typing.Protocol` и настройку mypy в CI.
- [Документация `cProfile`/`pstats`](https://docs.python.org/3/library/profile.html), [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html), [`line_profiler`](https://github.com/pyutils/line_profiler) — рабочий набор для §10.
- [Документация pytest](https://docs.pytest.org/) — фикстуры и параметризация; продолжение темы §12 — в главе [Тесты и качество кода в ML](../docs/12-coding/07-testing-and-code-quality.md).

### [NumPy и pandas на скорость](../docs/12-coding/02-numpy-pandas.md)

- [NumPy: Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) — официальные правила из первоисточника, с картинками растяжения осей. Пять минут чтения, которые закрывают §3 навсегда.
- [NumPy: Copies and views](https://numpy.org/doc/stable/user/basics.copies.html) — точный ответ на вопрос «что вернёт эта индексация», с разбором механизма strides.
- [NumPy: Indexing on ndarrays](https://numpy.org/doc/stable/user/basics.indexing.html) — полный разбор basic vs advanced indexing, включая случаи, которые в главе не поместились (`np.ix_`, комбинации срезов и массивов).
- [Harris et al. «Array programming with NumPy» (Nature, 2020)](https://www.nature.com/articles/s41586-020-2649-2) — обзорная статья от разработчиков: устройство ndarray, история и архитектурные решения. Читать, если хочется понимать инструмент, а не только пользоваться им.
- [pandas: Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html) — главный документ по §16: что изменилось, как мигрировать, какие паттерны сломаются. Обязательно к прочтению перед переходом на pandas 3.0.
- [pandas: Scaling to large datasets](https://pandas.pydata.org/docs/user_guide/scale.html) — официальная лестница приёмов для §15, включая честный раздел «когда пора уходить из pandas».
- [pandas: Enhancing performance](https://pandas.pydata.org/docs/user_guide/enhancingperf.html) — `eval`/`query`, Numba и Cython для тех мест, где векторизация невозможна.
- **Wes McKinney. «Python for Data Analysis», 3-е изд.** — доступна бесплатно онлайн на сайте автора (wesmckinney.com/book). Книга создателя pandas; главы про groupby, reshape и временные ряды — самое подробное изложение §10–§14 на русском рынке отсутствует, читайте оригинал.
- [DuckDB](https://duckdb.org/) и [Polars](https://pola.rs/) — если после §17 захотелось попробовать. Начните с DuckDB: он читает те же parquet-файлы и говорит на SQL, так что порог входа минимальный.

### [Реализуем ML руками](../docs/12-coding/03-ml-from-scratch.md)

- **[Исходники scikit-learn](https://github.com/scikit-learn/scikit-learn)** — лучший учебник по промышленным реализациям. Начните с `sklearn/linear_model/_logistic.py` и `sklearn/metrics/_ranking.py`: там видно, сколько кода уходит на краевые случаи, которых нет в учебной версии.
- **Trevor Hastie, Robert Tibshirani, Jerome Friedman. «The Elements of Statistical Learning»** — главы 3 (линейные модели), 9 (деревья) и 10 (бустинг) содержат ровно те выводы, по которым писался код выше. Доступна бесплатно на сайте Стэнфорда.
- **Kevin Murphy. «Probabilistic Machine Learning: An Introduction» (MIT Press, 2022)** — для наивного Байеса, PCA и вероятностного взгляда на логистическую регрессию; выкладки подробнее, чем в ESL.
- [Vaswani et al. «Attention Is All You Need» (2017)](https://arxiv.org/abs/1706.03762) — оригинальная статья про attention; раздел 3.2.1 — это ровно те три строки кода из §13, включая объяснение $\sqrt{d_k}$.
- **David Arthur, Sergei Vassilvitskii. «k-means++: The Advantages of Careful Seeding» (SODA 2007)** — доказательство оценки $O(\log k)$ для инициализации из §6; PDF легко находится по названию на страницах авторов.
- [Документация NumPy: broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) — если хоть раз сомневались, почему `a[:, None] - b[None, :]` даёт матрицу, прочитайте страницу целиком; это окупается на каждой второй задаче.
- **Тренажёр [`code/README.md`](../code/README.md)** — скелеты и тесты ко всему, что разобрано выше.

### [Алгоритмы для MLE-собеса](../docs/12-coding/04-algorithms.md)

- [Python Wiki: TimeComplexity](https://wiki.python.org/moin/TimeComplexity) — официальная таблица сложности операций для `list`, `dict`, `set`, `deque`. Одна страница, которую стоит держать в закладках и просмотреть перед собеседованием.
- [Документация модуля `heapq`](https://docs.python.org/3/library/heapq.html) — в конце страницы разобраны приёмы с приоритетной очередью, tie-breaker'ами и «ленивым удалением». Ровно то, о чём спрашивают в задачах на top-k.
- [NeetCode](https://neetcode.io) — бесплатная подборка задач, сгруппированных по паттернам (раздел Roadmap), а не по темам. Для MLE достаточно веток «Arrays & Hashing», «Two Pointers», «Sliding Window», «Binary Search», «Heap», «Graphs (базовые)».
- **Gayle Laakmann McDowell. «Cracking the Coding Interview»** — не про алгоритмы, а про поведение на секции: как задавать вопросы, как думать вслух, как оценивать сложность. Главы про подход полезнее, чем задачник.
- **Кормен, Лейзерсон, Ривест, Штайн. «Алгоритмы: построение и анализ»** — справочник для случая, когда нужно разобраться в алгоритме по-настоящему, а не выучить шаблон. Читать целиком для MLE-собеса не нужно.
- [LeetCode](https://leetcode.com) — если целитесь в международный бигтех, готовьтесь по темам-паттернам, а не подряд; для российского рынка достаточно уверенного easy/medium.

### [SQL: тренировка](../docs/12-coding/05-sql-drills.md)

- [Документация PostgreSQL: оконные функции — учебник](https://www.postgresql.org/docs/current/tutorial-window.html) и [полный список функций и синтаксис рамок](https://www.postgresql.org/docs/current/functions-window.html) — самое точное описание семантики `ROWS`/`RANGE`/`GROUPS` и рамки по умолчанию. Раздел про рамки стоит прочитать целиком: там ровно те ловушки, что разобраны в задачах 15, 17 и 19.
- [Документация PostgreSQL: сравнения и `NULL`](https://www.postgresql.org/docs/current/functions-comparison.html) — формальные правила трёхзначной логики и `IS DISTINCT FROM`. Короткая страница, снимает большинство вопросов блока C.
- **Cathy Tanimura. «SQL for Data Analysis» (O'Reilly, 2021)** — лучшая книга именно про аналитический SQL: когорты, retention, воронки, текстовый анализ. Главы про когортный анализ и про временные ряды закрывают блоки E и H глубже, чем эта глава.
- **Itzik Ben-Gan. «T-SQL Window Functions»** — исчерпывающе про оконные функции, включая gaps-and-islands во всех вариантах. Синтаксис T-SQL, но идеи переносятся один в один.
- [Use The Index, Luke!](https://use-the-index-luke.com/) — про индексы и планы запросов для разработчиков, бесплатно и по делу. Читать, если задача 6 из практики вызвала затруднение.
- [pgexercises.com](https://pgexercises.com/) — интерактивные упражнения на PostgreSQL с проверкой; хороши как разминка на синтаксис.
- [LeetCode Database](https://leetcode.com/problemset/database/) — задачи в формате, близком к скринингу; уровень Medium/Hard соответствует реальной секции.
- [Документация ClickHouse](https://clickhouse.com/docs) — если целитесь в компании с аналитикой на ClickHouse (Яндекс, Авито, VK): почитайте про `QUALIFY`, комбинаторы агрегатов (`-If`, `-Merge`), `ReplacingMergeTree` и `uniqHLL12`; на собесе это часто спрашивают отдельно.

### [PyTorch: тренировка](../docs/12-coding/06-pytorch-drills.md)

- [Официальный туториал PyTorch: `torch.autograd`](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html) — как строится и уничтожается граф; читать перед задачей об утечках памяти.
- [Документация: `torch.amp` и рецепты смешанной точности](https://pytorch.org/docs/stable/amp.html) — список операций, которые autocast оставляет в fp32, и правила использования `GradScaler`. Самая полезная страница по задаче 10.
- [Документация: воспроизводимость](https://pytorch.org/docs/stable/notes/randomness.html) — исчерпывающий список источников недетерминизма и способов их подавить.
- [Документация: управление CUDA-памятью](https://pytorch.org/docs/stable/notes/cuda.html#memory-management) — кэширующий аллокатор, `PYTORCH_CUDA_ALLOC_CONF`, разница allocated/reserved.
- [`torch.profiler`: рецепт](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) — как читать вывод профайлера и находить узкое место.
- [Lin et al. «Focal Loss for Dense Object Detection» (ICCV 2017)](https://arxiv.org/abs/1708.02002) — оригинал focal loss с обоснованием выбора $\gamma$ и $\alpha$ и с разбором, почему инициализация смещения последнего слоя важна при сильном дисбалансе.
- [Vaswani et al. «Attention Is All You Need» (NeurIPS 2017)](https://arxiv.org/abs/1706.03762) — первоисточник attention; сверяйте свою реализацию с формулами из §3.2.
- [Zhang & Sennrich. «Root Mean Square Layer Normalization» (NeurIPS 2019)](https://arxiv.org/abs/1910.07467) — RMSNorm из задачи 1, с экспериментальным обоснованием отказа от центрирования.
- [Micikevicius et al. «Mixed Precision Training» (ICLR 2018)](https://arxiv.org/abs/1710.03740) — откуда взялся loss scaling и почему нужна мастер-копия весов в fp32.
- [Andrej Karpathy. «A Recipe for Training Neural Networks»](https://karpathy.github.io/2019/04/25/recipe/) — лучший текст про методику отладки обучения; тест «переобучись на одном батче» и порядок действий взяты оттуда.

### [Тесты и качество кода в ML](../docs/12-coding/07-testing-and-code-quality.md)

- [Документация pytest](https://docs.pytest.org/) — разделы про фикстуры, параметризацию и маркеры покрывают 90% того, что нужно в ML-проекте. Начните с «How-to guides → Fixtures».
- **Brian Okken. «Python Testing with pytest» (Pragmatic Bookshelf)** — лучшая книга по pytest; главы про фикстуры и про организацию тестового набора отвечают на вопрос «как не утонуть, когда тестов станет двести».
- [Документация Hypothesis](https://hypothesis.readthedocs.io/) — property-based тестирование; смотрите `hypothesis.extra.numpy` и `hypothesis.extra.pandas`, они специально про наши структуры данных.
- [Документация Ruff](https://docs.astral.sh/ruff/) — список правил с примерами; наборы `PD` (pandas-vet) и `NPY` стоят отдельного прочтения, они ловят именно ML-специфичные грабли.
- [Документация mypy](https://mypy.readthedocs.io/) — раздел «Existing code» про постепенное внедрение типов в живой проект.
- [pre-commit.com](https://pre-commit.com/) — как устроены хуки и как их писать свои.
- [Документация pandera](https://pandera.readthedocs.io/) — декларативные схемы для DataFrame; самый простой способ поставить контракт данных в пайплайн, а не только в тесты.
- **Breck, Cai, Nielsen, Salib, Sculley. «The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction» (IEEE Big Data, 2017)** — 28 конкретных проверок по четырём категориям (данные, модель, инфраструктура, мониторинг) и способ измерить зрелость проекта числом. Лучший чек-лист по теме; ищется по названию в публикациях Google Research.
- [Ribeiro et al. «Beyond Accuracy: Behavioral Testing of NLP Models with CheckList» (ACL 2020)](https://arxiv.org/abs/2005.04118) — откуда взялись инвариантность, направленное ожидание и минимальный функциональный тест; написано про NLP, но применимо к любой модели.
- [Sculley et al. «Hidden Technical Debt in Machine Learning Systems» (NeurIPS 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — почему ML-система дороже в поддержке и откуда берутся все обсуждённые здесь проблемы.
- [Made With ML: Testing](https://madewithml.com/courses/mlops/testing/) — практический разбор с кодом: тесты на код, на данные и на модель в одном проекте.

## CV, звук, мультимодальность

### [Computer Vision: необходимый минимум](../docs/13-optional/01-computer-vision.md)

- [He et al. «Deep Residual Learning for Image Recognition» (2015)](https://arxiv.org/abs/1512.03385) — оригинал ResNet. Читать ради раздела про деградацию глубоких сетей: там формулировка проблемы, из которой всё выросло.
- [Dosovitskiy et al. «An Image Is Worth 16x16 Words» (2020)](https://arxiv.org/abs/2010.11929) — ViT. Ключевая для собеседования часть — эксперименты про зависимость качества от объёма предобучения.
- [Tan, Le. «EfficientNet» (2019)](https://arxiv.org/abs/1905.11946) — про compound scaling и про то, почему FLOPs не равны латентности.
- [Ronneberger et al. «U-Net» (2015)](https://arxiv.org/abs/1505.04597) — короткая статья, читается за полчаса, объясняет skip-соединения лучше любого пересказа.
- [Lin et al. «Focal Loss for Dense Object Detection» (2017)](https://arxiv.org/abs/1708.02002) — почему одностадийные детекторы догнали двухстадийные.
- [Liu et al. «A ConvNet for the 2020s» (ConvNeXt, 2022)](https://arxiv.org/abs/2201.03545) — отрезвляющий разбор того, сколько выигрыша ViT приходилось на рецепт обучения.
- [Документация torchvision: модели и предобученные веса](https://pytorch.org/vision/stable/models.html) — практический справочник: какие веса есть, какие у них трансформации и метрики.
- [Документация Albumentations](https://albumentations.ai/docs/) — стандартная библиотека аугментаций; полезна разделом про синхронную аугментацию картинки, боксов и масок.
- [Протокол оценки COCO](https://cocodataset.org/#detection-eval) — первоисточник по mAP, описывает ровно ту процедуру, которую спрашивают на собеседовании.

### [Звук и речь: необходимый минимум](../docs/13-optional/02-audio-and-speech.md)

- [Awni Hannun. «Sequence Modeling with CTC» (Distill, 2017)](https://distill.pub/2017/ctc/) — лучшее объяснение CTC на свете, с интерактивными иллюстрациями выравниваний и разбором алгоритма вперёд-назад. Если читать по теме одну вещь — то эту.
- [Radford et al. «Robust Speech Recognition via Large-Scale Weak Supervision» (Whisper, 2022)](https://arxiv.org/abs/2212.04356) — читать ради раздела про данные и про мультизадачный формат с управляющими токенами.
- [Graves. «Sequence Transduction with Recurrent Neural Networks» (2012)](https://arxiv.org/abs/1211.3711) — оригинал RNN-T, объясняет, как снимается условная независимость CTC при сохранении потоковости.
- [Baevski et al. «wav2vec 2.0» (2020)](https://arxiv.org/abs/2006.11477) — self-supervised предобучение на сырой волне; полезно понять, почему предобучение в аудио дало такой же эффект, как в NLP.
- [Park et al. «SpecAugment» (2019)](https://arxiv.org/abs/1904.08779) — короткая статья про аугментацию прямо на спектрограмме, стандарт де-факто.
- [Gulati et al. «Conformer» (2020)](https://arxiv.org/abs/2005.08100) — типовой энкодер современных ASR: свёртки для локальных зависимостей плюс self-attention для глобальных.
- [Документация torchaudio](https://pytorch.org/audio/stable/index.html) — практический справочник: загрузка, ресемплинг, готовые спектрограммы, CTC-декодер с языковой моделью.
- [Документация librosa](https://librosa.org/doc/latest/index.html) — то же для анализа и визуализации; раздел про STFT и мел-фильтры полезно прочитать вместе с §2–3 этой главы.

### [Мультимодальность](../docs/13-optional/03-multimodal.md)

- [Radford et al. «Learning Transferable Visual Models From Natural Language Supervision» (CLIP, 2021)](https://arxiv.org/abs/2103.00020) — первоисточник. Читать разделы про функцию потерь, про инженерию подсказок и, обязательно, про ограничения — там честный разбор того, чего модель не умеет.
- [van den Oord et al. «Representation Learning with Contrastive Predictive Coding» (2018)](https://arxiv.org/abs/1807.03748) — откуда взялся InfoNCE и его связь с оценкой взаимной информации.
- [Zhai et al. «Sigmoid Loss for Language Image Pre-Training» (SigLIP, 2023)](https://arxiv.org/abs/2303.15343) — почему от softmax по батчу можно отказаться и что это даёт при обучении.
- [Li et al. «BLIP-2» (2023)](https://arxiv.org/abs/2301.12597) — Q-Former как способ соединить замороженный визуальный энкодер с замороженной LLM малой кровью.
- [Liu et al. «Visual Instruction Tuning» (LLaVA, 2023)](https://arxiv.org/abs/2304.08485) — самый простой работающий рецепт VLM: линейный проектор плюс двухстадийное обучение. Хорошая точка входа, если строите своё.
- [Alayrac et al. «Flamingo» (2022)](https://arxiv.org/abs/2204.14198) — вариант с cross-attention внутрь LLM; полезно для понимания, почему подходы различаются по расходу контекста.
- [open_clip](https://github.com/mlfoundations/open_clip) — открытые реализации и десятки чекпоинтов CLIP-подобных моделей с воспроизводимыми метриками; практический старт для любой задачи из этой главы.

## Карьера

### [Процесс найма изнутри](../docs/14-career/01-interview-process.md)

- **Публичные описания процесса найма от компаний.** Часть компаний публикует устройство своих секций и правила повторных попыток: репозитории `avito-tech/playbook` и `Tinkoff/career` на GitHub. Если вы идёте в конкретную компанию, первым делом проверьте, нет ли у неё такого документа, — он точнее любого пересказа.
- **Chip Huyen, «Machine Learning Interviews»** (открытая книга, репозиторий `chiphuyen/ml-interviews-book` на GitHub) — англоязычный взгляд на ту же воронку: как читают резюме, как устроены секции, что происходит на дебрифе. Полезна для международных процессов.

### [Поведенческая секция](../docs/14-career/02-behavioral.md)

- **Публичные принципы найма компаний.** Часть работодателей публикует, какие качества они оценивают на поведенческих секциях: например, Amazon открыто описывает свои Leadership Principles на карьерном сайте, а российские компании — в открытых репозиториях с матрицами компетенций (`avito-tech/playbook`, `Tinkoff/career` на GitHub). Если идёте в конкретную компанию, посмотрите её формулировки и подберите истории под них.

### [Рост и переговоры](../docs/14-career/03-growth-and-negotiation.md)

- **Patrick McKenzie, «Salary Negotiation: Make More Money, Be More Valued»** (эссе на kalzumeus.com) — классический разбор того, почему обсуждение компенсации не является конфликтом и как к нему готовиться.
- **Haseeb Qureshi, «Ten Rules for Negotiating a Job Offer»** (haseebq.com) — подробные скрипты переговоров в инженерном найме; учитывайте, что примеры американские, а механика универсальна.
- **Обзоры зарплат и площадки с открытыми вилками** — единственный способ говорить о рынке числами, а не ощущениями: полугодовые обзоры Хабр Карьеры, агрегаторы вилок в вакансиях, для международных позиций — levels.fyi. Смотрите медиану по своему грейду и городу, а не максимум.
- **Определение выгорания в МКБ-11 (ВОЗ)** — если хотите свериться с формулировкой из первоисточника, а не с популярными пересказами: там оно описано именно как связанное с работой явление, а не как медицинский диагноз общего характера.

---

🏠 [Оглавление хендбука](../docs/index.md)
