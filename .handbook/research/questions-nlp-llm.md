# NLP / LLM — research dump

> Собрано: 2026-07-26. Тема: `nlp-llm`.
> **Важное ограничение среды:** egress-политика сессии пропускает только домены GitHub
> (`github.com`, `raw.githubusercontent.com`, GitHub API). Все остальные хосты
> (habr.com, blog.deepschool.ru, medium.com, arxiv.org, datacamp, geeksforgeeks, yandex.ru, itmo.ru и т. д.)
> возвращают `403 CONNECT tunnel failed` / `403 Forbidden` при попытке загрузки.
> Поэтому источники разделены на две группы: **(A) реально скачанные целиком** и
> **(B) увиденные только через сниппеты веб-поиска** — из группы B я НЕ выписываю вопросы дословно,
> только фиксирую факт существования источника и то, что реально было видно в сниппете.

---

## Источники, которые реально просмотрены

### A. Загружены целиком (raw content прочитан)

| # | URL | Что там |
|---|-----|---------|
| A1 | https://github.com/freQuensy23-coder/ML_roadmap/blob/main/100%20questions%20NLP%20(ru).md | **«100 questions about NLP» на русском.** Каноничный русскоязычный банк вопросов по NLP, собранный тг-каналами (ds girl, Dealer.AI, «что-то на DL-ском», «Плюшевый Питон», «алиса олеговна»). Разбит по блокам: TF-IDF, метрики, word2vec, RNN/CNN, attention & transformer, типы моделей, positional encoding, pretraining, токенайзеры, training, inference, LLM + «ANALYSE questions» с явной градацией ответа по грейдам. |
| A2 | https://github.com/ixlander/interview-questions/blob/main/all-real-questions.md | **«Вопросы из реальных собеседований (274 шт.)»** — каждый вопрос помечен грейдом (`Junior`/`Middle`/`Senior`) И компанией (Ozon, Яндекс, ВТБ, VK, Avito, Точка банк, Дром.ру, Constructor, ZinBrains, PulsePoint, Quantum One, Candy.ai, Waibee, Corsearch/Navi, Infomedia, Sber Autonomous, WorldQuant, HFT-компания, NNS, Gradient, Remobby). Самый ценный источник для «asked at real screening». |
| A3 | https://github.com/justxor/MachineLearningRoadmap/blob/main/interview-prep/03-llm-rag-agents.md | «🤖 LLM, RAG и агенты: **30 вопросов с разбором**», явно позиционировано как «Вопросы для LLM / GenAI Engineer собеседований 2026. Уровень: middle/senior». |
| A4 | https://github.com/justxor/MachineLearningRoadmap/blob/main/interview-prep/02-deep-learning.md | 30 вопросов DL, из них ~8 напрямую про attention / KV-cache / positional encoding / архитектуры трансформера. |
| A5 | https://github.com/justxor/MachineLearningRoadmap/blob/main/interview-prep/04-system-design.md | 10 кейсов ML System Design, среди них «Кейс 4: LLM-чатбот для поддержки», «Кейс 8: Search autocomplete», «Кейс 7: Real-time speech-to-text». |
| A6 | https://github.com/justxor/MachineLearningRoadmap/blob/main/README.md | Roadmap ML 2026 на русском; внутри — сводный список «50 вопросов», блок «LLM и современный стек» (вопросы 21–30) и блок отладочных чеклистов. |
| A7 | https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub | **115 вопросов по LLM** (Q1–Q115) с ответами: трансформер, токенизация, инференс, decoding, prompting, fine-tuning, alignment, pretraining. |
| A8 | https://github.com/KalyanKS-NLP/RAG-Interview-Questions-and-Answers-Hub | **105 вопросов по RAG** (1–105) с ответами: chunking, embeddings, vector DB / ANN, hybrid search, rerankers, метрики retrieval (Context Precision/Recall/Relevancy, Faithfulness, Response Relevancy), latency. |
| A9 | https://github.com/llmgenai/LLMInterviewQuestions/blob/main/README.md | «100+ LLM Interview Questions for Top Companies» — заявлено, что вопросы задавались в Google, NVIDIA, Meta, Microsoft и Fortune-500. 15 категорий. |
| A10 | https://github.com/amitshekhariitbhu/ai-engineering-interview-questions/blob/main/README.md | ~400 вопросов «AI Engineering Interview» (AI/GenAI/LLM/Agentic Engineer, LLMOps). Особенность: половина — сценарные («Your X is broken. How do you fix it?»), что очень близко к реальным прод-секциям. |
| A11 | https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/interview_prep/60_gen_ai_questions.md | «60 GenAI questions»: генеративные модели, LLM, мультимодальность, эмбеддинги, training/inference/evaluation. |
| A12 | https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/interview_prep/system-design/README.md | AI System Design Case Studies: «5-layer spine» (model → wrapping layer → evals & guardrails → production & ops → optimization) + 10 разобранных кейсов (customer support agent, enterprise research assistant, text-to-SQL, coding agent, voice agent, clinical scribe …). |
| A13 | https://github.com/Pe4enIks/ML-Interview (=`epishchik/ML-Interview`) README.md | Русский банк вопросов MLE (уклон CV), но с большим разделом «Трансформеры и механизм внимания» — multi-head, self vs cross, pre/post-LN, ограничение на число токенов, квадратичная сложность, обучение BERT, задача про 2×512 vs 1×1024. |
| A14 | https://github.com/purepisces/Wenqing-Machine_Learning_Blog/blob/main/Machine-Learning-Interview-Questions/Transformer-Interview-Question.md | 15 нумерованных вопросов строго по внутренностям трансформера (в т.ч. «why scale before softmax», «why different weight matrices for Q,K,V», «why LayerNorm not BatchNorm»). |
| A15 | https://github.com/Devinterview-io/llms-interview-questions | «63 LLM interview questions» (в README раскрыты первые 15 с ответами). |
| A16 | https://github.com/Devinterview-io/nlp-interview-questions | «50 Core NLP Interview Questions in 2026» (в README раскрыты первые 15: corpus/tokenization/stopwords, morphology vs syntax, POS, лемматизация vs стемминг, NER, sentiment, dependency parsing, n-grams, BoW, Naive Bayes, HMM, SVM, RF, Decision Trees). |
| A17 | https://github.com/Maha-Rossomaha/LLM_projects/blob/main/1%20NLP%20and%20LLM/1_plan.md | «План изучения LLM + NLP (Senior, Search/RecSys)» на русском — фактически готовое оглавление раздела: Transformers → GQA/SWA → MoE → Architectures → Tokenizers (BPE/WordPiece/Unigram/byte-level BPE/SentencePiece) → Embeddings → Layers → Models → Finetuning (PEFT/LoRA/QLoRA/prompt/prefix/p-tuning/adapters) → Alignment (PPO/DPO/KTO) → Quantization → Effective training (DDP/PP/TP/ZeRO) → Long context (NTK scaling, FlashAttention) → Prompt engineering → Embeddings/contrastive → Debugging → LLM in Search & Rec. |
| A18 | https://github.com/Rakhmankulov/Interviews/blob/main/LLM%20and%20ML/README.md | Русский конспект-глоссарий под собес по LLM-инфре: Safetensors, GGUF, квантизация, KV-Cache, Chunked Prefill, offloading, RAG-стек, дрейф, метрики в проде, LLMOps-форматы, NVIDIA GPU Operator / MIG, SFT/RLHF/LoRA, vLLM vs Ollama, LiteLLM, Langfuse + раздел «Общие вопросы с собеседований». |
| A19 | https://github.com/Extremesarova/ds_resources | Русский индекс ресурсов для подготовки к DS/ML-собесам; содержит ссылки на «50 NLP interview questions», «LLM (ML) Job Interviews — Resources» и русскоязычные подборки по грейдам. |
| A20 | https://github.com/Maha-Rossomaha/LLM_projects (дерево репозитория) | Структура: `1 NLP and LLM` / `2 Search and Recs` / `3 Production and MLOps` / `4 Infra and Data Storage` / `5 Recommendations` / `6 ML System Design` / `7 Agents and MCP` — полезный шаблон разбиения материала. |

### B. Видно только через сниппеты веб-поиска (сам домен закрыт egress-политикой — страницу загрузить не удалось)

Дословные вопросы отсюда **не выписывались**; фиксирую только сам источник и то, что было в сниппете.

| URL | Что видно из сниппета |
|---|---|
| https://habr.com/ru/articles/972178/ | «Топ вопросов с NLP собеседований: трансформеры и внимание до малейших деталей». Заявлена серия с продолжениями про GPT/LLM, alignment и оптимизации, агентов. |
| https://habr.com/ru/articles/1044420/ | «Топ вопросов с NLP собеседований: обучение LLM, prompt-engineering и alignment». В сниппете: спрашивают про полный жизненный цикл LLM — pretraining, почему базовый GPT ещё не ассистент, зачем instruction tuning, как работает RLHF, что такое alignment и его подводные камни. |
| https://habr.com/ru/articles/1044418/ | «Топ вопросов по LLM: стратегии генерации текста и метрики оценки LLM». В сниппете: проверяют не термины top-k/top-p/BLEU, а понимание поведения распределения вероятностей, почему greedy decoding зацикливается, зачем температура, почему BLEU плохо оценивает ответы современных LLM. |
| https://blog.deepschool.ru/dl/attention-i-transformery-v-nlp-chto-sprashivayut-na-sobesedovaniyah/ | Гайд «Attention и трансформеры в NLP: что спрашивают на собеседованиях», ответы под спойлерами, разбит по модулям. |
| https://blog.deepschool.ru/dl/tokenizacziya-i-embeddingi-v-nlp-chto-sprashivayut-na-sobesedovaniyah/ | «Токенизация и эмбеддинги в NLP: что спрашивают на собеседованиях» — уровни токенизации (слова/символы/сабворды), BPE, WordPiece, SentencePiece, Unigram LM, позиционные эмбеддинги, static vs contextual. |
| https://anki.deepschool.ru/ | Anki-карточки «Вопросы для собеседования» (DL, LLM, Docker и др.). |
| https://yandex.ru/jobs/interview/mldev | Как Яндекс нанимает ML: 3–4 технические секции; секция «ML & Programming» — базовые понятия ML на примере алгоритма, offline-метрики, задача на алгоритмы/структуры данных. |
| https://education.yandex.ru/knowledge/sektsiia-na-proverku-bazovikh-tekhnicheskikh-navikov-ml-inzhenerov | Описание секции на проверку базовых техн. навыков ML-инженеров (массивы, хэш-таблицы, краевые случаи, тестирование решения). |
| https://ai.itmo.ru/blog/classic-ml-sobesedovanie-ml-engineer | «Classic ML на собеседовании»: тезис, что classic ML — фундамент, через который проверяют мышление, прежде чем идти в DL/LLM/агентов. |
| https://uproger.com/gajd-po-prodvinutym-voprosam-dlya-razrabotchika-llm/ | «Гайд по продвинутым вопросам для разработчика LLM»: self-attention, multi-head, Q/K/V, positional embeddings, long-range dependencies. |
| https://tproger.ru/articles/kak-gotovitsja-k-sobesedovanijam-na-machine-learning-engineer | Как готовиться к собесам на MLE (RU). |
| https://www.datainterview.com/blog/llms-and-transformers-interview-questions | «Top 32 LLMs & Transformers Interview Questions (2026)». |
| https://www.techinterview.org/post/3233474408/... | «AI/ML Interview: LLM — Inference, Fine-Tuning, RAG, Prompt Engineering, Hallucination, Evaluation, Deployment». |
| https://huru.ai/llm-engineer-interview-questions-rag-prompting-evaluation/ | «LLM Engineer Interview Questions: RAG, Prompting, and Evaluation». В сниппете: как RAG совмещает retrieval и generation; sparse vs dense trade-offs; проблемы продакшена RAG; как детектировать/митигировать галлюцинации. |
| https://letsdatascience.com/blog/50-llm-and-ai-engineer-interview-questions-for-2026 | «50 AI Engineer Interview Questions: 2026 LLM Guide». |
| https://www.aiofferly.com/career-guide/nvidia-ml-interview-questions | NVIDIA AI/ML Interview Guide 2025/2026 — в сниппете: сдвиг от архитектуры моделей к «Hardware-Software Co-Design», оптимизация LLM-инференса. |
| https://www.yuan-meng.com/posts/mle_interviews_2.0/ | «MLE Interview 2.0: Research Engineering and Scary Rounds» — в сниппете: типовые кодинг-раунды = реализовать LoRA-адаптер с нуля, Transformer encoder/decoder, KV cache, beam search. |
| https://www.teamblind.com/post/nvidia-onsite-for-ml-llm-engineer-c7w0b8qd | Отчёт об onsite в NVIDIA на ML/LLM Engineer. |
| https://skphd.medium.com/llm-system-design-interview-questions-and-answers-2a7a16212492 | «LLM System Design Interview Questions and Answers». |
| https://vllm.ai/blog/2025-09-05-anatomy-of-vllm | «Inside vLLM: Anatomy of a High-Throughput LLM Inference System» (канон для вопросов про PagedAttention/continuous batching). |
| https://rlhfbook.com/c/06-policy-gradients | RLHF Book (Nathan Lambert) — канон для PPO/GRPO/DPO. |
| https://arxiv.org/pdf/2309.00071 | YaRN: Efficient Context Window Extension (канон для вопросов про расширение контекста). |
| https://arxiv.org/pdf/2401.07872 | Survey «The What, Why, and How of Context Length Extension Techniques in LLMs». |
| https://cameronrwolfe.substack.com/p/grpo | GRPO разбор. |
| https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms | «A Guide to RL Post-Training for LLMs: PPO, DPO, GRPO, and Beyond». |
| https://www.kdnuggets.com/10-essential-agentic-ai-interview-questions-for-ai-engineers | 10 обязательных вопросов по agentic AI. |
| https://arxiv.org/pdf/2410.21819 | «Self-Preference Bias in LLM-as-a-Judge» — канон под вопрос про валидность LLM-судьи. |

---

## Вопросы с собеседований

Легенда грейдов:
- **junior** — ожидается определение + один пример;
- **middle** — ожидается механизм + trade-off + «когда не сработает»;
- **middle_plus** — ожидается ещё и цифра/оценка (память, латентность, сложность) либо продовый сценарий с деградацией.

Пометка `[REAL]` = источник явно указывает, что вопрос задавали на реальном скрининге/техсекции, с компанией.

---

### 0. Реальные вопросы с указанием грейда и компании `[REAL]`

Источник: A2 — https://github.com/ixlander/interview-questions/blob/main/all-real-questions.md
(грейд и компания взяты дословно из источника)

| Вопрос (verbatim RU) | Грейд (по источнику) | Компания |
|---|---|---|
| Объясните механизм Self-Attention в трансформере | Middle | **Ozon** |
| За счёт чего трансформер учитывает порядок токенов? | Middle | **Ozon** |
| В чём основная разница между BERT и GPT? | Middle | **Ozon** |
| Как агрегировать выход трансформера в единый вектор: CLS-token или pooling? | Middle | **Ozon** |
| Какие подходы к параллельному обучению нейросетей вы знаете? | Middle | **Ozon** |
| Как построить эмбеддинг пользователя на основе его последовательности действий? | Senior | **Ozon** |
| Как объединить эмбеддинги пользователя и товара для предсказания релевантности? | Senior | **Ozon** |
| Как оптимизировать тяжёлую модель рекомендаций для продакшн-инференса? | Middle | **Ozon** |
| В чём разница между SASRec и BERT4Rec? | Middle | **Ozon** |
| Почему в трансформере используется Layer Normalization вместо Batch Normalization? | Middle | **ZinBrains** |
| Опишите архитектуру трансформера (encoder) по блокам. | Middle | **ZinBrains** |
| Расскажите про реализацию трансформер-based рекомендера (SASRec): данные, обучение, результаты. | Senior | **ZinBrains** |
| Какие алгоритмы токенизации текста используются в трансформерах? | Junior | **Точка банк (R&D)** |
| Как происходит токенизация и создание эмбеддингов в трансформерах? | Junior | **Яндекс (Поиск, объектные ответы)** |
| Какую модель обучить для генерации текстовых описаний, если промтинг не работает? | Middle | **Яндекс (Поиск, объектные ответы)** |
| Как бы вы строили систему генерации текстовых описаний для карточек товаров при запуске в новой стране (Китай)? | Senior | **Яндекс (Поиск, объектные ответы)** |
| Как построить офлайн-метрику качества генерации текстов? | Middle | **Яндекс (Поиск, объектные ответы)** |
| Как применить sentiment analysis к ответам LLM для ранжирования продуктов? | Middle | **ВТБ** |
| Почему vanilla BERT недостаточен для sentiment analysis и зачем нужен fine-tuning? | Middle | **ВТБ** |
| Как спроектировать систему для выбора оптимального банковского продукта с помощью LLM-двойника клиента? | Senior | **ВТБ** |
| Расскажите про ваш опыт работы с LLM: как применяли, какие задачи решали? | Middle | **Candy.ai / AI Companion Startup** |
| Почему нельзя просто заменить основную LLM на LLM-Judge, если та даёт лучшие ответы? | Senior | **Candy.ai / AI Companion Startup** |
| Какой у вас опыт со speech-to-text и аудио-обработкой? | Middle | **Candy.ai / AI Companion Startup** |
| Как вы настраивали LLM для модерации — через System Prompt или через fine-tuning? | Middle | **Candy.ai / AI Companion Startup** |
| Расскажите подробно про ваш кейс реализации AI-агента (RAG-системы). | Middle | **Waibee (стартап)** |
| Как вы работали с ограничением размерности эмбеддингов (256) в OpenSearch? | Middle | **Waibee (стартап)** |
| Какие проблемы вы видите при создании LLM-агента для генерации SQL-запросов к legacy-базе? | Senior | **PulsePoint (AdTech, RTB)** |
| Стоит ли интегрировать существующие отчёты компании как tool для LLM? Какие проблемы? | Middle | **PulsePoint (AdTech, RTB)** |
| Вы добавили трансформер-ранкер, и резко просела латентность и пропускная способность. Что делать? | Senior | **Дром.ру** |
| Как масштабировать ранкер при миллионе кандидатов? Пользователь не дождётся инференса бустинга. | Senior | **Constructor (e-commerce search SaaS)** |
| Есть ли опыт с трансформерными моделями для ранжирования? | Middle | **Constructor** |
| System Design: спроектируйте систему ранжирования для e-commerce поиска. Сначала простое решение, затем сложнее. | Senior | **Constructor** |
| Как использовать контентные и коллаборативные embeddings для candidate generation в RecSys? | Middle | **VK** |
| Как получить embedding видео для рекомендательной системы? Какие модели и подходы? | Middle | **VK** |
| Как вы собирали датасет и обучали metric learning модель для поиска фейковых автомобилей в базе? | Middle | **VK** |
| Расскажите подробнее про обучение эмбеддинг-модели: архитектура, данные, метрики. | Middle | **Corsearch / Navi** |
| Есть ли опыт с оптимизацией инференса — TensorRT, квантизация и т.д.? | Middle | **Infomedia** |
| Как перевести модель PyTorch в режим инференса? | Junior | **Автотехника (Sber Autonomous)** |
| Зачем отключать подсчёт градиентов при инференсе? | Junior | **NNS** |
| Что делает model.eval() в PyTorch и зачем он нужен? | Middle | **NNS** |
| В чём разница между Batch Normalization и Layer Normalization? | Middle | **NNS** |
| Какие контекстные менеджеры используются в PyTorch? | Middle | **NNS** |
| Заменят ли LLM аналитиков и ML-инженеров? | Junior | **Quantum One Consulting (Abu Dhabi)** |
| Какие тренды в AI/ML будут доминировать в ближайшие 5 лет? | Junior | **Quantum One Consulting (Abu Dhabi)** |
| Описание команды монетизации Avito: broad match, profile promo, ССМ-направление (трансформеры) | Junior (HR-скрининг) | **Avito (монетизация)** |

**Вывод по этому блоку:** на российском рынке NLP/LLM-вопрос на middle почти всегда звучит либо как
«объясните механизм X внутри трансформера», либо как «вот прод-ограничение — что делаете».
Чистой теории «расскажи про word2vec» на middle уже почти нет — она уехала в junior.

---

### 1. Токенизация (BPE / WordPiece / SentencePiece / Unigram / byte-level)

| Вопрос | Грейд | Источник |
|---|---|---|
| Какие виды **токенайзеров** вы знаете? Сравните их. | junior | A1 (#64) |
| Как обучается токенизатор? Объясните на примерах **WordPiece** и **BPE**. | middle | A1 (#68) |
| Какой токенизатор используется в BERT, а какой в GPT? | junior | A1 (#70) |
| Объясните как современные токенизаторы обрабатывают out-of-vocabulary words? | middle | A1 (#71) |
| На что влияет tokenizer vocab size? Как вы будете его выбирать в случае нового обучения? | middle_plus | A1 (#72) |
| Можете ли вы расширять токенайзер? Если да, то в каком случае? Когда вы будете переобучать токенайзер? Что необходимо сделать при добавлении новых токенов? | middle_plus | A1 (#65) |
| Чем обычные токены отличаются от **специальных** токенов? | junior | A1 (#66) |
| Почему в трансформерах не используется лемматизация? И зачем нам нужны токены? | middle | A1 (#67) |
| На какой позиции стоит CLS вектор? Почему? | junior | A1 (#69) |
| Какие алгоритмы токенизации текста используются в трансформерах? `[REAL]` | junior | A2, **Точка банк** |
| Как происходит токенизация и создание эмбеддингов в трансформерах? `[REAL]` | junior | A2, **Яндекс** |
| Что такое токенизация и почему BPE стал стандартом? | middle | A3 (#1) |
| Что такое токенизация (BPE, WordPiece, SentencePiece)? | junior | A6 (#21) |
| What is a token in the language model? | junior | A9 |
| What is tokenization, and why is it necessary in LLMs? | junior | A7 (Q12) |
| Explain why subword tokenization is preferred over word-level tokenization in the Transformer model. | middle | A7 (Q7) |
| Explain the trade-offs in using a large vocabulary in LLMs. | middle_plus | A7 (Q8) |
| If I have a vocabulary of 100K words/tokens, how can I optimize transformer architecture? | middle_plus | A9 |
| A large vocabulary can cause computation issues and a small vocabulary can cause OOV issues, what approach you would use to find the best balance of vocabulary? | middle_plus | A9 |
| How do LLMs handle out-of-vocabulary (OOV) words? | middle | A7 (Q111) |
| Your tokenizer splits important domain terms into meaningless subword pieces. How do you fix it? | middle_plus | A10 |
| Как работают различные токенизаторы текста? | middle | A13 |

**Что реально хотят услышать:** merge-правила BPE vs likelihood-критерий WordPiece vs вероятностная модель Unigram;
почему SentencePiece работает на сыром тексте без пре-токенизации (важно для языков без пробелов);
почему byte-level BPE не имеет `<UNK>`; что расширение словаря требует resize эмбеддингов + lm_head
и что новые строки эмбеддингов надо инициализировать не случайно, а средним/по сабтокенам;
что для русского языка fertility (токенов на слово) в англоцентричных токенайзерах в 2–3 раза выше — это прямые деньги.

---

### 2. Эмбеддинги, word2vec, fastText, GloVe, contextual

| Вопрос | Грейд | Источник |
|---|---|---|
| Объясните как учится **Word2Vec**? Какая функция потерь? Что максимизируется? | middle | A1 (#16) |
| Какие две основные архитектуры вы знаете и какая из них учится быстрее? (CBOW / Skip-gram) | junior | A1 (#19) |
| Что такое negative sampling и зачем он нужен? Какие ещё трюки у word2vec знаете? | middle | A1 (#21) |
| В чём разница между GloVe, ELMo, FastText и Word2Vec? | middle | A1 (#20) |
| В чём отличие между static и contextual эмбеддингами? | junior | A1 (#18) |
| Что такое dense и sparse эмбеддинги? Приведите примеры. | junior | A1 (#22) |
| Почему может быть важна размерность эмбеддинга? | middle | A1 (#23) |
| Какие проблемы могут возникнуть при обучении Word2Vec на коротких текстовых данных, и как с ними справиться? | middle | A1 (#24) |
| Какие способы получения эмбеддингов знаете? Когда какие будут лучше? | middle | A1 (#17) |
| Почему эмбеддинги называются контекстуальными? Как это работает? | middle | A1 (#40) |
| Что такое sentence embedding? Какими способами вы можете его получить? | middle | A1 (#90) |
| Объясните концепции metric learning. Какие подходы вам известны? | middle | A1 (#86) |
| Какие метрики для близости текстов вы знаете? | junior | A1 (#7) |
| Объясните разницу между косинусной близостью и косинусным расстоянием. Какое может быть негативным? | junior | A1 (#8) |
| Как агрегировать выход трансформера в единый вектор: CLS-token или pooling? `[REAL]` | middle | A2, **Ozon** |
| Как вы работали с ограничением размерности эмбеддингов (256) в OpenSearch? `[REAL]` | middle | A2, **Waibee** |
| Расскажите подробнее про обучение эмбеддинг-модели: архитектура, данные, метрики. `[REAL]` | middle | A2, **Corsearch/Navi** |
| Compare and contrast word embeddings and sentence embeddings. How do their applications differ? | middle | A11 |
| When training word embeddings, how can models be designed to effectively capture representations for rare words? | middle_plus | A11 |
| Propose metrics for quantitatively evaluating the quality of embeddings generated by an LLM. | middle_plus | A11 |
| In loss functions like triplet loss or contrastive loss, what is the significance of the margin parameter? | middle | A11 |
| What is quantization in the context of embeddings, and how does it reduce memory footprint while preserving quality? | middle_plus | A11 |
| How do you handle embedding drift when the embedding model is updated? | middle_plus | A10 |
| Your new embedding model has different dimensions from the existing vectors in production. How do you handle the mismatch? | middle_plus | A10 |
| You deployed a new embedding model, and search quality crashed overnight. How do you handle embedding drift? | middle_plus | A10 |
| How do you fine-tune an embedding model for a specific domain? | middle_plus | A10 |
| Your semantic search fails for short queries. How do you improve it? | middle | A10 |
| Walk me through steps of improving sentence transformer model used for embedding? | middle_plus | A9 |
| What is the difference between embedding short and long content? | middle | A9 |
| How to benchmark embedding models on your data? | middle_plus | A9 |
| После бенчмарка точность OpenAI-эмбеддера низкая — как дальше улучшать точность embedding-поиска? | middle_plus | A9 |
| After tokenization, how are tokens converted into embeddings in the Transformer model? | junior | A7 (Q6) |
| Какая размерность у эмбеддингового слоя в трансформере? | junior | A1 (#39) |

---

### 3. Классический NLP, RNN, seq2seq (что ещё спрашивают на junior)

| Вопрос | Грейд | Источник |
|---|---|---|
| Напишите **TF-IDF** с нуля. | junior | A1 (#1) |
| Что такое нормализация в TF-IDF? | junior | A1 (#2) |
| Зачем вы вообще знаете про TF-IDF в наше время и как можете использовать в сложных моделях? | middle | A1 (#3) |
| Объясните возможные методы предобработки текста (лемматизацию и стемминг). Какие алгоритмы знаете и когда используете? | junior | A1 (#6) |
| Объясните, как работает Наивный Байес? Для чего вы можете его использовать? | junior | A1 (#4) |
| Что такое perplexity? С чем мы можем её считать? | middle | A1 (#12) |
| Что такое метрика BLEU? | junior | A1 (#13) |
| Объясните разницу между разными видами ROUGE метрики? | middle | A1 (#14) |
| В чём отличие BLEU от ROUGE? | junior | A1 (#15) |
| Сколько обучающих параметров в простой 1-слойной RNN? | middle | A1 (#25) |
| Как обучается RNN? Какие проблемы есть в RNN? | junior | A1 (#26–27) |
| Какие виды RNN сетей вы знаете? Объясните разницу между GRU и LSTM. | junior | A1 (#28) |
| Что такое затухающие градиенты для RNN? И как вы решаете эту проблему? | middle | A1 (#30) |
| Зачем в NLP CNN и как вы можете его использовать? С чем сравните CNN в рамках парадигмы attention? | middle | A1 (#31) |
| Как работает teacher forcing, приведите примеры? | middle | A1 (#83) |
| In a transformer-based seq2seq model, what are the primary functions of the encoder and decoder? How does information flow between them during training vs inference? | middle | A11 |
| What problems of RNNs do transformer models solve? | junior | A11 |
| Compare Transformers and RNNs in terms of handling long-range dependencies. | middle | A7 (Q31) |
| What are some of the advantages of using a transformer instead of LSTM? | junior | A9 |
| What do you understand by the terms 'corpus', 'tokenization', and 'stopwords' in NLP? | junior | A16 (#2) |
| Describe lemmatization and stemming. When would you use one over the other? | junior | A16 (#5) |
| What are n-grams, and how do they contribute to language modeling? | junior | A16 (#9) |
| Describe what a 'bag of words' model is and its limitations. | junior | A16 (#10) |
| How does a dependency parser work, and what information does it provide? | junior | A16 (#8) |
| What is a 'named entity' and how is NER useful in NLP tasks? | junior | A16 (#6) |
| How are Hidden Markov Models (HMMs) applied in NLP tasks? | junior | A16 (#12) |

---

### 4. Attention и внутренности трансформера

| Вопрос | Грейд | Источник |
|---|---|---|
| Как считаете attention? | junior | A1 (#32) |
| Напишите attention с нуля. | middle | A1 (#35) |
| Сложность attention? Сравните со сложностью в RNN. | middle | A1 (#33) |
| Сравните RNN и attention. В каком случае будете использовать attention, а когда RNN? | middle | A1 (#34) |
| Объясните маскирование в attention. | middle | A1 (#36) |
| Какая размерность у матриц self-attention? | middle | A1 (#37) |
| В чём разница между BERT и GPT в рамках подсчёта attention? | middle | A1 (#38) |
| Что используется в трансформере layer norm или batch norm и почему? | middle | A1 (#41) |
| Зачем в трансформерах PreNorm и PostNorm? | middle_plus | A1 (#42) |
| Объясните разницу между soft и hard (local/global) attention? | middle | A1 (#43) |
| Объясните multihead attention. | middle | A1 (#44) |
| Какие другие виды механизмов внимания вы знаете? На что направлены эти модификации? | middle_plus | A1 (#45) |
| Насколько усложнится self-attention при увеличении числа голов? | middle_plus | A1 (#46) |
| Объясните разницу между головами и слоями в трансформер-моделях. | junior | A1 (#53) |
| Объясните механизм Self-Attention в трансформере `[REAL]` | middle | A2, **Ozon** |
| Опишите архитектуру трансформера (encoder) по блокам. `[REAL]` | middle | A2, **ZinBrains** |
| Почему в трансформере используется Layer Normalization вместо Batch Normalization? `[REAL]` | middle | A2, **ZinBrains** |
| Рассказать про multi-head attention в деталях. | middle | A13 |
| В чём разница self-attention и cross-attention, для чего используется каждый? | middle | A13 |
| Pre-layer norm vs post-layer norm — в чём разница, какие где используются и почему? | middle_plus | A13 |
| Почему в трансформерах есть ограничения на количество токенов? | middle | A13 |
| Как борются с квадратичной сложностью механизма внимания? | middle_plus | A13 |
| Задача: что будет эффективнее по скорости — подать 2 входа по 512 токенов по отдельности (2×512) или объединить и подать сразу (1×1024)? | middle_plus | A13 |
| Why does the Transformer scale the attention score before softmax? (`/√d_k`) | middle | A14 (#4) |
| Why does the Transformer use different weight matrices to create Q, K and V? | middle | A14 (#5) |
| Why does the transformer block use LayerNorm instead of BatchNorm? | middle | A14 (#8) |
| Why does the Transformer use Multi-head Attention? | middle | A14 (#3) |
| What are the aspects of Transformer parallelization? | middle | A14 (#9) |
| Introduce residual connections in Transformer and their significance. | junior | A14 (#6) |
| What are the differences between Transformer Encoder and Decoder? | junior | A14 (#10) |
| Why do we scale the dot product attention by √dₖ in the Transformer architecture? | middle | A10 |
| What is causal masking? | junior | A10 |
| What is Cross Attention in Transformers? | junior | A10 |
| What are Feed-Forward Networks in LLMs? / What is the purpose of the position-wise feed-forward sublayer? | junior | A10 / A7 (Q35) |
| What is Grouped-Query Attention (GQA), and how does it differ from Multi-Head Attention (MHA)? | middle_plus | A10 |
| What is Flash Attention? | middle_plus | A10 |
| What is the computational complexity of self-attention in the Transformer model? | junior | A7 (Q10) |
| How do Transformer models address the vanishing gradient problem? | middle | A7 (Q11) |
| Explain how self-attention is computed in the Transformer model step by step. | junior | A7 (Q9) |
| What is the purpose of scaling in the self-attention mechanism in the Transformer model? | middle | A7 (Q19) |
| Why does the Transformer model use multiple self-attention heads instead of a single head? | middle | A7 (Q20) |
| How are the outputs of multiple heads combined and projected back in multi-head attention? | middle | A7 (Q21) |
| How does masked self-attention differ from regular self-attention, and where is it used? | middle | A7 (Q22) |
| Explain why self-attention in the decoder is referred to as cross-attention. How does it differ from self-attention in the encoder? | middle | A7 (Q26) |
| Discuss the pros and cons of the self-attention mechanism in the Transformer model. | middle | A7 (Q23) |
| What are the fundamental limitations of the Transformer model? | middle_plus | A7 (Q32) |
| Explain the disadvantages of the self-attention mechanism and how can you overcome it. | middle_plus | A9 |
| What is the difference between local attention and global attention? | middle | A9 |
| What makes transformers heavy on computation and memory, and how can we address this? | middle_plus | A9 |
| Explain dimension of each layer in multi headed transformation attention block | middle_plus | A9 |
| How do you make sure that attention layer focuses on the right part of the input? | middle_plus | A9 |
| Объясните attention на пальцах / Что такое multi-head attention и зачем? | junior/middle | A4 (#14, #15) |
| Your Transformer runs out of memory on long documents due to quadratic self-attention. How do you scale it? | middle_plus | A10 |
| What is Mixture of Experts (MoE), and how does it work in models like Mixtral? | middle_plus | A10 |
| Объясните технологию, которая стоит за MixTral, в чём её плюсы и минусы? | middle_plus | A1 (#99) |
| What is the difference between dense and sparse models? | middle | A10 |

---

### 5. Позиционное кодирование (sinusoidal / learned / relative / RoPE / ALiBi)

| Вопрос | Грейд | Источник |
|---|---|---|
| Почему в эмбеддингах transformer-моделей с attention теряется информация о позициях? | junior | A1 (#54) |
| Объясните подходы для позициональных эмбеддингов и их плюсы и минусы. | middle | A1 (#55) |
| Почему нельзя просто добавить эмбеддинг с индексом токена? | middle | A1 (#56) |
| Почему мы не учим positional embeddings? | middle_plus | A1 (#57) |
| Что такое relative и absolute positional encoding? | middle | A1 (#58) |
| Подробно объясните принцип работы rotary positional embeddings (RoPE). | middle_plus | A1 (#59) |
| За счёт чего трансформер учитывает порядок токенов? `[REAL]` | middle | A2, **Ozon** |
| Что такое позиционные эмбеддинги и для чего они нужны? Какие есть виды и для чего каждый нужен? | middle | A13 |
| Можно ли использовать двумерное позиционное кодирование в трансформерах для изображений? Какие проблемы у одномерного в этом случае? | middle_plus | A13 |
| Объясните positional encoding (sinusoidal, RoPE, ALiBi). | middle | A6 (#22) |
| CNNs and RNNs don't use positional embeddings. Why do transformers use positional embeddings? | junior | A7 (Q1) |
| How does Rotary Position Embedding (RoPE) work, and why is it preferred over learned positional embeddings? | middle_plus | A10 |
| Why is positional encoding crucial in transformer models, and what issue does it address in the context of self-attention operations? | junior | A11 |
| A brief introduction to Transformer's position encoding, its pros and cons | middle | A14 (#12) |
| What is positional encoding? | junior | A9 |

**Отдельно (канон, встречается как follow-up):** почему RoPE — это абсолютное кодирование, дающее относительный эффект;
почему `theta_base = 10000` и что происходит при его увеличении (NTK-aware scaling);
почему ALiBi экстраполируется лучше, но плохо генерализуется далеко за пределы обучающей длины;
почему bfloat16 ломает RoPE на длинном контексте (см. arXiv 2411.13476 из выдачи).

---

### 6. Архитектуры: BERT vs GPT vs T5, MLM vs CLM

| Вопрос | Грейд | Источник |
|---|---|---|
| В чём основная разница между BERT и GPT? `[REAL]` | middle | A2, **Ozon** |
| Объясните transformer модели, сравнивая BERT, GPT и T5. | middle | A1 (#50) |
| Почему BERT во многом проигрывает RoBERTa и что вы можете взять у RoBERTa? | middle_plus | A1 (#47) |
| Что такое T5 и BART модели? Чем они отличаются? | middle | A1 (#48) |
| Что такое task-agnostic модели? Приведите примеры. | middle | A1 (#49) |
| Какая большая проблема есть в моделях BERT, GPT и т.д. относительно знаний модели? Как это можно решать? | middle_plus | A1 (#51) |
| Как работает decoder-like а-ля GPT на обучении и на инференсе? В чём разница? | middle | A1 (#52) |
| Как обучается causal language modelling? | junior | A1 (#60) |
| Какие модели кроме BERT и GPT по различным задачам предобучения вы знаете? | middle | A1 (#63) |
| Как обучался BERT? | junior | A13 |
| Чем encoder-only, decoder-only и encoder-decoder трансформеры отличаются? | junior | A6 / A4 (#17) |
| What is the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures? | junior | A10 |
| What is the difference between causal language modeling and masked language modeling? | junior | A7 (Q110) |
| Explain different types of LLM architecture and which type of architecture is best for which task? | middle | A9 |
| Highlight the key differences between models like GPT and BERT? | junior | A11 |
| Почему vanilla BERT недостаточен для sentiment analysis и зачем нужен fine-tuning? `[REAL]` | middle | A2, **ВТБ** |
| What is the purpose of the encoder / decoder in a Transformer model? | junior | A7 (Q16–Q18) |
| What are Autoregressive Models? | junior | A10 |
| How do Diffusion Language Models (DLMs) work? / Explain how DLMs differ from LLMs. | middle_plus | A10 / A7 (Q58) |
| Do you prefer DLMs or LLMs for latency-sensitive applications? | middle_plus | A7 (Q59) |

---

### 7. Претрейн, scaling laws, распределённое обучение

| Вопрос | Грейд | Источник |
|---|---|---|
| Объясните scaling law. | middle | A1 (#93) |
| Объясните все этапы обучения LLM. От какого из этапов мы можем отказаться и в каких случаях? | middle_plus | A1 (#94) |
| Как обучить transformer с нуля? Объясните свой пайплайн и в каком случае вы будете этим заниматься. | middle_plus | A1 (#62) |
| Когда мы используем предобученную модель? | junior | A1 (#61) |
| In the context of LLM pretraining, what is scaling law? | middle | A7 (Q112) |
| Explain the pretraining objective used in LLM pretraining. | junior | A7 (Q109) |
| What is the significance of self-supervised learning in LLM pretraining? | junior | A7 (Q115) |
| Explain the concept of Mixture-of-Experts (MoE) architecture and its role in LLM pretraining. | middle_plus | A7 (Q113) |
| What is model parallelism, and how is it used in LLM pre-training? | middle_plus | A7 (Q114) |
| What are the different phases in LLM development? | junior | A7 (Q88) |
| Какие подходы к параллельному обучению нейросетей вы знаете? `[REAL]` | middle | A2, **Ozon** |
| Какие знаете способы распределённого обучения? | middle | A1 (#78) |
| Как оптимизировать потребление ресурсов при обучении? | middle_plus | A1 (#77) |
| Как изменятся потребляемые ресурсы при gradient accumulation? | middle | A1 (#76) |
| Что такое DDP и FSDP? | middle_plus | A4 (#22) |
| What is FSDP (Fully Sharded Data Parallel), and how does it differ from DeepSpeed ZeRO? | middle_plus | A10 |
| What is tensor parallelism / pipeline parallelism, and how does it help serve large models? | middle_plus | A10 |
| What is model parallelism vs data parallelism in distributed training? | middle | A10 |
| Mixed precision training: что и зачем? / Gradient checkpointing: что и зачем? | middle | A4 (#19, #20) |
| Объясните как работает warm-up? | middle | A1 (#81) |
| Объясните концепцию gradient clipping. | junior | A1 (#82) |
| В чём отличие оптимизатора Adam от AdamW? | middle | A1 (#75) |
| Почему стал реже использоваться паддинг? Что делают вместо этого? (packing / sequence bucketing) | middle_plus | A1 (#80) |
| Что такое текстовые аугментации? Назовите все методы, что знаете. | middle | A1 (#79) |
| Можно ли использовать на инференсе dropout и почему? | middle | A1 (#74) |
| How to train LLM with low precision training without compromising on accuracy? | middle_plus | A9 |
| What is FP8 variable and what are its advantages? | middle_plus | A9 |
| Large Language Models often require careful tuning of learning rates. How do you adapt learning rates during training to ensure stable convergence? | middle_plus | A11 |
| Discuss challenges related to overfitting in LLMs during training. What strategies and regularization techniques are effective? | middle | A11 |

---

### 8. Fine-tuning, PEFT, LoRA/QLoRA

| Вопрос | Грейд | Источник |
|---|---|---|
| Как работает LoRA? Как вы будете выбирать параметры? Представьте, что мы хотим дообучить большую языковую модель, делаем LoRA с маленьким r, но модель всё равно не лезет по памяти — что ещё можно сделать? | middle_plus | A1 (#91) |
| В чём отличие prefix tuning от p-tuning и от prompt tuning? | middle_plus | A1 (#92) |
| Что такое адаптеры? Где и как мы можем их использовать? | middle | A1 (#85) |
| Как вы сможете предотвращать катастрофическое забывание у LLM? | middle_plus | A1 (#97) |
| Что такое LoRA / QLoRA / PEFT? | junior | A6 (#24) |
| LoRA vs full fine-tuning: trade-offs | middle | A3 (#15) |
| Когда fine-tuning реально нужен? | middle | A3 (#14) |
| Как вы настраивали LLM для модерации — через System Prompt или через fine-tuning? `[REAL]` | middle | A2, **Candy.ai** |
| What is LoRA (Low-Rank Adaptation), and how does it work? | junior | A10 / A7 (Q101) |
| Explain the key ingredient behind the effectiveness of the LoRA technique. (низкий внутренний ранг апдейта) | middle_plus | A7 (Q102) |
| What is QLoRA, and how does it enable fine-tuning on consumer hardware? | middle | A10 / A7 (Q103) |
| When would you use QLoRA instead of standard LoRA? | middle | A7 (Q104) |
| How would you handle LLM fine-tuning on consumer hardware with limited GPU memory? | middle_plus | A7 (Q105) |
| How do you fine-tune LLM on consumer hardware? | middle_plus | A9 |
| What are the different categories of the PEFT method? | middle | A9 |
| What are different re-parameterized methods for fine-tuning? | middle_plus | A9 |
| Explain Prefix Tuning and Prompt Tuning. How are they different from LoRA? | middle_plus | A10 |
| What is adapter-based fine-tuning? | middle | A10 |
| How do you merge multiple LoRA adapters? | middle_plus | A10 |
| What is continual pre-training, and when would you use it? | middle_plus | A10 |
| What are the key hyperparameters for fine-tuning (learning rate, epochs, batch size, LoRA rank)? | middle | A10 |
| How to set hyperparameters for fine-tuning? / How to estimate infrastructure requirements for fine-tuning LLM? | middle_plus | A9 |
| How do you prepare a dataset for fine-tuning an LLM? / How to create fine-tuning datasets for Q&A? | middle | A10 / A9 |
| What is catastrophic forgetting, and how do you prevent it during fine-tuning? | middle | A10 / A7 (Q93) / A9 |
| When should you choose fine-tuning over RAG over prompt engineering? | middle | A10 |
| What is the difference between SFT (Supervised Fine-Tuning) and alignment training? | middle | A10 |
| What is instruction tuning, and why is it important for chat models? | junior | A10 |
| What role does instruction tuning play in improving an LLM's usability? | middle | A7 (Q90) |
| What is synthetic data generation, and how do you use it for fine-tuning? | middle_plus | A10 |
| What is knowledge distillation for fine-tuning, and what are the legal considerations? | middle_plus | A10 |
| You must choose between LoRA and full fine-tuning for a domain-specific assistant. How do you decide? | middle_plus | A10 |
| Your fine-tuned LLM forgot its general capabilities after domain-specific fine-tuning. How do you fix catastrophic forgetting? | middle_plus | A10 |
| Your fine-tuned model memorized training data verbatim instead of learning patterns. How do you fix overfitting? | middle_plus | A10 |
| Your fine-tuned LLM produces factually wrong outputs due to training data quality issues. How do you fix it? | middle_plus | A10 |
| How do you improve the model to answer only if there is sufficient context for doing so? | middle_plus | A9 |
| What are the strengths and limitations of full fine-tuning? | middle | A7 (Q94) |
| Explain how parameter efficient fine-tuning addresses the limitations of full fine-tuning. | middle | A7 (Q95) |
| What are the possible options to speed up LLM fine-tuning? | middle_plus | A7 (Q108) |
| Допустим, надо обучить классификатор на k классов, из разметки есть по 10 примеров на каждый — как учить? | middle | A1 (ANALYSE) |
| Что такое дисбаланс классов? Как это можно увидеть? Назовите все подходы к решению. | junior | A1 (#73) |

---

### 9. Alignment: RLHF / DPO / GRPO / Constitutional AI

| Вопрос | Грейд | Источник |
|---|---|---|
| Pre-training vs SFT vs RLHF vs DPO — что и зачем? | middle | A3 (#4) |
| Чем pre-training, SFT, RLHF, DPO отличаются? | junior | A6 (#23) |
| В чём математическая разница между PPO и DPO? | middle_plus | A6 (deep-dive блок) |
| Почему DPO теоретически эквивалентен PPO при определённых условиях? | middle_plus | A6 (deep-dive блок) |
| What is RLHF, and how is it used to align LLMs? | junior | A10 / A9 / A11 |
| What is the reward hacking issue in RLHF? | middle_plus | A9 |
| Your RLHF-trained LLM is gaming the reward model instead of being genuinely helpful. How do you fix reward hacking? | middle_plus | A10 |
| At which stage will you decide to go for preference alignment rather than SFT? | middle_plus | A9 |
| Explain different preference alignment methods and their trade-offs. | middle_plus | A9 / A7 (Q106) |
| What is RLAIF (RL from AI Feedback), and how does it differ from RLHF? | middle_plus | A10 |
| After RLHF alignment, your LLM became safer but lost capability on hard tasks. How do you manage the alignment tax? | middle_plus | A10 |
| Your RLHF preference data has low annotator agreement. How do you ensure data quality? | middle_plus | A10 |
| What role does alignment tuning play in improving an LLM's usability? | middle | A7 (Q91) |
| Что такое Constitutional AI? | middle_plus | A3 (#24) |
| What is AI alignment, and why is it important? | junior | A10 |
| How can reinforcement learning be integrated into the training of LLMs, and what challenges might arise in selecting suitable loss functions for RL-based approaches? | middle_plus | A11 |
| Генеративная decoder-only модель выучила «плохие» паттерны в данных и иногда генерирует «плохие» тексты. Как сделать, чтобы она их не генерировала? *(источник прямо говорит: от стажёра/джуна — 1–2 гипотезы, от мидла — 2–3 подхода, от сеньора — 4–5 подходов с разбором достоинств и недостатков)* | junior / middle / senior — **эталонная градация** | A1 (ANALYSE) |

---

### 10. Декодирование и контроль генерации

| Вопрос | Грейд | Источник |
|---|---|---|
| За что отвечает температура в softmax? Какую вы будете выставлять? | junior | A1 (#87) |
| Объясните виды sampling при генерации: top-k, top-p, nucleus sampling. | junior | A1 (#88) |
| Какая сложность у beam search и как он работает? | middle | A1 (#89) |
| Объясните temperature, top_p, top_k | junior | A3 (#3) |
| Explain the role of decoding strategy in LLM text generation. | junior | A7 (Q42) |
| What are the different decoding strategies in LLMs? | junior | A7 (Q43) |
| Explain the impact of the decoding strategy on LLM-generated output quality and latency. | middle | A7 (Q44) |
| Explain the greedy search decoding strategy and its main drawback. | junior | A7 (Q45) |
| How does Beam Search improve upon Greedy Search, and what is the role of the beam width parameter? | middle | A7 (Q46) |
| When is a deterministic strategy (like Beam Search) preferable to a stochastic strategy? Provide a specific use case. | middle | A7 (Q47) |
| Discuss the primary trade-off between computational cost and output quality: Greedy vs Beam Search. | middle | A7 (Q48) |
| When you set the temperature to 0.0, which decoding strategy are you using? | junior | A7 (Q49) |
| How is Beam Search fundamentally different from a BFS or DFS? | middle | A7 (Q50) |
| Compare deterministic and stochastic decoding methods in LLMs. | middle | A7 (Q52) |
| What are different ways you can define stopping criteria in large language model? / How to use stop sequences in LLMs? | junior | A9 |
| What is autoregressive generation in the context of LLMs? Strengths and limitations. | junior | A7 (Q56–57) |
| Explain the concept of token streaming during inference. | middle | A7 (Q60) |
| What is temperature in the context of LLMs, and how does it affect output? | junior | A10 |
| Explain Top-p (nucleus) sampling and Top-k sampling. How do they differ? | junior | A10 |
| What are logits, and how are they used in text generation? | junior | A10 |
| Your text generation repeats phrases in long outputs. How do you fix repetition? | middle | A10 |
| Your LLM generates responses that are too verbose. How do you control response length? | middle | A10 |
| Nucleus (Top-p) and Min-P Sampling / Contrastive Search | middle_plus | A15 |

---

### 11. Инференс и оптимизация: KV-cache, GQA/MQA, PagedAttention/vLLM, speculative decoding, batching, квантизация

| Вопрос | Грейд | Источник |
|---|---|---|
| Объясните принцип работы KV cache, Grouped-Query Attention и Multi-Query Attention. | middle_plus | A1 (#98) |
| Какие методы квантизации вы знаете? Можем ли мы тюнить квантизованные модели? | middle_plus | A1 (#96) |
| Объясните KV-cache. Как он влияет на latency и память? | middle | A6 / A4 (#16) |
| Объясните, почему KV-cache важен для инференса. | middle | A6 (#29) |
| Чем quantization (INT8, INT4, GPTQ, AWQ) помогает в проде? | middle | A6 (#30) |
| Объясните vLLM и PagedAttention | middle_plus | A3 (#20) |
| Что такое quantization и какие виды? | middle | A3 (#21) |
| Что такое speculative decoding? / Как реализовать speculative decoding с нуля? | middle_plus / senior | A3 (#29) / A6 |
| Какие есть способы снизить cost и latency LLM? | middle_plus | A3 (#19) |
| Что такое prompt caching и почему важно? | middle_plus | A3 (#26) |
| Когда self-host LLM, а когда API? | middle | A3 (#22) |
| Опишите архитектуру LLM-приложения в проде на 1000 RPS | senior | A3 (#30) |
| Explain how KV Cache accelerates LLM inference. | middle | A7 (Q3) |
| How do you handle the large memory requirements of KV cache in LLM inference? | middle_plus | A7 (Q5) |
| How to calculate size of KV cache | middle_plus | A9 |
| Your Transformer's KV cache grows too large during long sequence generation. How do you manage memory? | middle_plus | A10 |
| How does quantization affect inference speed and memory requirements? | middle | A7 (Q4) |
| Tell me the basic steps involved in running an inference query on an LLM. | junior | A7 (Q2) |
| Can you briefly explain the difference between LLM training and inference? | junior | A7 (Q36) |
| What is latency in LLM inference, and why is it important? | junior | A7 (Q37) |
| Why is the first token slower than the rest in an LLM? (prefill vs decode) | middle | A10 |
| What is batch inference, and how does it differ from single-query inference? | middle | A7 (Q38) |
| Explain the trade-offs between batching and latency in LLM serving. | middle_plus | A7 (Q40) |
| What is continuous batching, and how does it differ from static batching? | middle_plus | A7 (Q65) / A10 |
| What is Paged Attention? | middle_plus | A10 |
| How does vLLM work? / How does SGLang work? | middle_plus | A10 |
| Explain the role of Flash Attention in reducing memory bottlenecks. | middle_plus | A7 (Q64) |
| What is speculative decoding, and when would you use it? | middle_plus | A7 (Q61) / A10 |
| What are the challenges in performing distributed inference across multiple GPUs? | middle_plus | A7 (Q62) |
| How would you design a scalable LLM inference system for real-time applications? | senior | A7 (Q63) |
| What is mixed precision, and why is it used during inference? | middle | A7 (Q66) |
| Differentiate between online and offline LLM inference deployment scenarios. | middle | A7 (Q67) |
| Explain the throughput vs latency trade-off in LLM inference. | middle_plus | A7 (Q68) |
| What are the various bottlenecks in a typical LLM inference pipeline on a modern GPU? (memory-bound vs compute-bound) | middle_plus | A7 (Q69) |
| How do you measure LLM inference performance? (TTFT, ITL/TPOT, throughput) | middle_plus | A7 (Q70) / A10 |
| What are the different LLM inference engines available? Which one do you prefer? | middle | A7 (Q71) |
| What are the possible options for accelerating LLM inference? | middle_plus | A7 (Q73) |
| How can techniques like mixture-of-experts (MoE) optimize inference efficiency? | middle_plus | A7 (Q41) |
| Why does quantization not decrease the accuracy of LLM? | middle_plus | A9 |
| What are the techniques by which you can optimize the inference of LLM for higher throughput? | middle_plus | A9 |
| How to accelerate response time of model without attention approximation like GQA? | senior | A9 |
| What is model quantization (INT8, INT4, FP16, BF16), and how does it affect quality? | middle | A10 |
| You quantized your LLM, but accuracy dropped significantly. How do you minimize quantization loss? | middle_plus | A10 |
| How does GGUF work? | middle | A10 |
| How do you select GPUs for LLM inference? | middle_plus | A10 |
| How do you manage GPU memory for serving multiple models? | middle_plus | A10 |
| What is model sharding, and when would you use it? | middle_plus | A10 |
| How do you optimize inference for edge and mobile deployment? | middle_plus | A10 |
| How do you implement request queuing and priority scheduling for AI services? | senior | A10 |
| How do you handle cold start latency for serverless AI deployments? | middle_plus | A10 |
| What is model routing at the infrastructure level, and how do you route requests based on complexity and cost? | senior | A10 |
| What is semantic routing, and how do you implement it in a multi-model system? | middle_plus | A10 |
| How does Prompt Caching work? / How do you handle long contexts efficiently in production (context compression, prefix caching)? | middle_plus | A10 |
| Есть ли опыт с оптимизацией инференса — TensorRT, квантизация и т.д.? `[REAL]` | middle | A2, **Infomedia** |
| Как оптимизировать тяжёлую модель рекомендаций для продакшн-инференса? `[REAL]` | middle | A2, **Ozon** |
| Вы добавили трансформер-ранкер, и резко просела латентность и пропускная способность. Что делать? `[REAL]` | senior | A2, **Дром.ру** |
| Что такое Chunked Prefill? Что такое offloading в контексте LLM? | middle_plus | A18 |
| Что такое GGUF / Safetensors? Что хранится в config.json и generation_config.json? | junior | A18 |
| Какую платформу или фреймворк можно использовать для сервинга моделей? | middle | A18 |
| vLLM vs Ollama: ключевые особенности, плюсы, минусы, типовые use-cases | middle | A18 |

---

### 12. Длинный контекст

| Вопрос | Грейд | Источник |
|---|---|---|
| Что такое context window и почему он ограничен? | junior | A3 (#2) |
| Что такое context rot? | middle_plus | A3 (#25) |
| What is the context window in LLMs, and why does it matter? / Why is the context window limited in LLMs? | junior | A10 |
| How can you increase the context length of an LLM? | middle_plus | A9 |
| Why is naively increasing context length not a straightforward solution? What computational and memory challenges does it pose? | middle_plus | A11 |
| What challenges arise from the fixed and limited attention span in the vanilla Transformer? How does this affect capturing long-term dependencies? | middle | A11 |
| What is the "lost in the middle" problem in long-context prompting? | middle_plus | A10 |
| What is the role of the context window during LLM inference? Pros and cons of large vs small context windows. | middle | A7 (Q53–54) |
| Your LLM-powered tool hits the context window limit on long documents. How do you handle it? | middle_plus | A10 |
| Your chatbot loses context after 10 turns in a conversation. How do you maintain a long conversation context? | middle | A10 |
| How does context compaction work? | middle_plus | A10 |
| How do LLMs handle context and long-term dependencies in text? (Ring Attention, FlashAttention-3, SSM-гибриды, KV-cache compression) | senior | A15 |
| NTK scaling / Flash Attention — как расширяют контекст | middle_plus | A17 (раздел «Long context») |

---

### 13. RAG (chunking, hybrid search, rerankers, метрики)

**Базовое / архитектура**

| Вопрос | Грейд | Источник |
|---|---|---|
| Как работает RAG? Чем он отличается от few-shot KNN? | middle | A1 (#95) |
| Что такое RAG и когда он лучше fine-tuning? | junior | A3 (#5) |
| Объясните RAG end-to-end. | middle | A6 (#25) |
| Опишите архитектуру боевого RAG end-to-end | middle_plus | A3 (#6) |
| Какие основные проблемы RAG в проде? | middle_plus | A3 (#7) |
| Что такое hybrid search и RRF? | middle | A3 (#8) |
| Зачем нужен reranking и какой выбрать? | middle | A3 (#9) |
| Расскажите подробно про ваш кейс реализации AI-агента (RAG-системы). `[REAL]` | middle | A2, **Waibee** |
| Explain the requirement of RAG when LLMs are already powerful. | junior | A8 (#1) |
| Is RAG still relevant in the era of long context LLMs? | middle_plus | A8 (#2) |
| What are the fundamental challenges of RAG systems? | middle | A8 (#3) |
| What are effective strategies to reduce latency in RAG systems? | middle_plus | A8 (#4) |
| How does RAG help reduce hallucinations in LLM generated responses? | junior | A8 (#6) |
| Explain the steps in the indexing process in a RAG pipeline. | junior | A8 (#11) |
| Explain the retrieval process step-by-step in a RAG pipeline. | junior | A8 (#15) |
| What are the key hyperparameters in a RAG pipeline? | middle | A8 (#18) |
| Explain the influence of LLM context window size on RAG hyperparameters. | middle_plus | A8 (#20) |
| Compare reasoning vs non-reasoning LLMs for RAG systems. | middle_plus | A8 (#22) |
| What happens with a weak generator LLM in a RAG system? / with a weak retriever? | middle | A8 (#23, #39) |
| What are the architecture patterns for customizing LLM with proprietary data? | middle_plus | A9 |
| How to build production grade RAG system, explain each component in detail? | senior | A9 |
| Compare RAG vs fine-tuning. When would you use each? | middle | A10 |
| Explain Self-RAG. How does the model decide when to retrieve? | middle_plus | A10 |
| What is GraphRAG, and when would you use it over traditional RAG? | middle_plus | A10 |

**Chunking**

| Вопрос | Грейд | Источник |
|---|---|---|
| What is chunking, and why do we chunk our data? / Explain the importance of chunking in RAG. | junior | A9 / A8 (#12) |
| What factors influence chunk size? / How do you choose the chunk size for a RAG system? | middle | A9 / A8 (#13) |
| What are the potential consequences of having chunks that are too large versus too small? | middle | A8 (#14) |
| What is the purpose of character overlap during chunking in a RAG pipeline? | junior | A8 (#8) |
| What are some common chunking methods used in RAG? Criteria to choose a specific one? | middle | A8 (#34–35) |
| Explain the pros and cons of semantic chunking. | middle_plus | A8 (#36) |
| How does the chunking strategy differ for structured documents (PDFs with tables/figures) vs plain text? | middle_plus | A8 (#37) |
| What is parent-child chunking, and how does it improve retrieval? | middle_plus | A10 |
| What are the different chunk enhancement techniques in RAG? Pros and cons? | middle_plus | A8 (#31–32) |
| Explain how the contextual chunk header technique enhances RAG retrieval. | middle_plus | A8 (#33) |
| How to handle tables during chunking? How do you handle very large table for better retrieval? How to handle list item during chunking? | middle_plus | A9 |
| What is the best method to digitize and chunk complex documents like annual reports? | senior | A9 |
| How to handle graphs & charts in RAG | middle_plus | A9 |
| Your RAG system struggles with PDF documents containing tables and layouts. How do you fix PDF parsing? | middle_plus | A10 |
| Your RAG chunk overlap causes redundant results. How do you reduce redundancy? | middle | A10 |

**Retrieval / vector DB / hybrid**

| Вопрос | Грейд | Источник |
|---|---|---|
| What are the common retrieval approaches used in RAG systems? | junior | A8 (#40) |
| Compare keyword-based retrieval and semantic retrieval in RAG systems. | middle | A8 (#50) |
| How does hybrid search work in the context of RAG retrieval? When do you opt for hybrid instead of semantic? | middle | A8 (#51–52) |
| If you have search results from multiple methods, how would you merge and homogenize the rankings into a single result set? (RRF) | middle_plus | A9 |
| How do sparse embeddings differ from dense embeddings in terms of keyword matching and retrieval interpretability? | middle | A8 (#54) |
| Explain the role of ANN search algorithms in RAG retrieval. Step-by-step working. | middle_plus | A8 (#46–47) |
| Explain Random projection index / LSH indexing / product quantization (PQ) indexing method. | middle_plus | A9 |
| Explain vector search strategies like clustering and Locality-Sensitive Hashing. How does clustering reduce search space? When does it fail? | middle_plus | A9 |
| Compare different Vector index and given a scenario, which vector index you would use? | middle_plus | A9 |
| Explain difference between vector index, vector DB & vector plugins? | middle | A9 |
| What are the typical distance metrics used for similarity search in vector databases, and why? Why is cosine similarity preferred? | middle | A8 (#48–49) |
| How would you decide ideal search similarity metrics for the use case? | middle | A9 |
| Explain different types and challenges associated with filtering in vector DB? | middle_plus | A9 |
| What is the role of metadata filtering in RAG systems? | middle | A10 |
| How to decide the best vector database for your needs? | middle | A9 |
| Discuss the strategies to scale embeddings in RAG retrieval. Quantization vs dimensionality reduction? Scalar vs binary quantization? | middle_plus | A8 (#57–60) |
| How do you balance relevance and diversity when retrieving document chunks for RAG? (MMR) | middle_plus | A8 (#53) |
| Design a retrieval strategy for a RAG system handling both structured (knowledge graphs) and unstructured (text) data simultaneously. | senior | A8 (#56) |
| How can fine-tuning embedding models improve the retriever's performance in RAG? | middle_plus | A8 (#55) |
| What are the possible reasons for the poor performance of a RAG retriever? | middle_plus | A8 (#38) |
| Consider a scenario where a client has built a RAG system that is not giving accurate results; investigation shows the retrieval system is inaccurate. What steps will you take to improve it? | senior | A9 |
| How do you scale a RAG system to millions of documents? | senior | A10 |
| Your RAG retrieval is too slow with a large knowledge base. How do you speed it up? | middle_plus | A10 |
| Your vector database cannot scale to millions of embeddings. How do you fix the bottleneck? | senior | A10 |
| Your RAG system needs per-user access control on internal documents. How do you implement it? | middle_plus | A10 |
| Your RAG system returns duplicate results. How do you deduplicate? | middle | A10 |

**Query transformation / reranking**

| Вопрос | Грейд | Источник |
|---|---|---|
| How do you handle ambiguous or vague user queries in RAG systems? | middle | A8 (#24) |
| What are the different query transformation techniques that enhance user queries in RAG? Pros and cons? | middle_plus | A8 (#25–26) |
| Explain how the HyDE query transformation technique works. / HyPE? / Compare HyPE and HyDE. | middle_plus | A8 (#27–29) |
| To minimize RAG system latency, which pre-retrieval enhancement technique will you choose? | middle_plus | A8 (#30) |
| What is query transformation in RAG (HyDE, query decomposition, step-back prompting)? | middle_plus | A10 |
| Why is re-ranking important in the RAG pipeline after initial document retrieval? | middle | A8 (#7) |
| How does re-ranking differ from the initial retrieval process in RAG? Pros and cons of using re-rankers? | middle | A8 (#61–62) |
| What are the different types of re-ranker models? Compare general vs instruction-following re-rankers. | middle_plus | A8 (#63–64) |
| Why is the cross-encoder typically used as the re-ranker rather than the bi-encoder? | middle | A8 (#65) |
| Describe the vector pre-computation and storage strategy in a bi-encoder + cross-encoder pipeline. Why can't cross-encoders pre-compute text representations? | middle_plus | A8 (#69) |
| A RAG system retrieves 20 candidate chunks but can only fit 5 in the context window. Without re-ranking, how might this affect response quality, and what problems would a re-ranker solve? | middle_plus | A8 (#66) |
| Describe a scenario where BM25 retrieval returns relevant chunks but in poor ranking order. How would a neural re-ranker address this? | middle_plus | A8 (#67) |
| If your RAG system serves both simple factual queries and complex analytical questions, how would you decide when to bypass the re-ranker for efficiency? | senior | A8 (#68) |
| Compare noise reduction capabilities of re-rankers versus simply increasing the similarity threshold in initial retrieval. | middle_plus | A8 (#70) |
| What challenges do re-rankers face regarding computational overhead and latency? In real-time apps with strict latency SLAs, name two optimizations. | senior | A8 (#71–72) |
| How to fine-tune re-ranking models? | middle_plus | A9 |

**Метрики RAG**

| Вопрос | Грейд | Источник |
|---|---|---|
| What are the key metrics for evaluating retrieval quality in RAG? | middle | A8 (#42) |
| How would you evaluate the effectiveness of a reranker? Which metrics (MRR, MAP, NDCG) would you prioritize and why? | middle_plus | A8 (#73) |
| Explain the difference between Precision@k and Recall@k in the context of RAG. When might you prefer one? | middle | A8 (#74) |
| Why is MRR unsuitable when there are multiple relevant chunks per query, and how does MAP address this? | middle_plus | A8 (#75) |
| Given a retrieval result, manually calculate MAP@5. What does MAP reveal that raw Precision does not? | middle_plus | A8 (#76) |
| If all relevant chunks are at the very bottom, how would this affect MRR, MAP, and NDCG? | middle_plus | A8 (#77) |
| Suppose your RAG retriever gets perfect Recall@10 but low Precision@10. What problems for the downstream generator? | middle_plus | A8 (#78) |
| Compare "order-aware" and "order-unaware" retrieval metrics in RAG. | middle | A8 (#79) |
| How would NDCG@k change if all relevant chunks are retrieved but in reverse order? | middle_plus | A8 (#80) |
| What is Context Precision@K and how does it differ from standard Precision@k in traditional IR? | middle_plus | A8 (#81–83) |
| A RAG system achieves Context Precision@5 = 0.8. What scenarios could lead to this score? | middle_plus | A8 (#84) |
| Explain the possible reasons for a RAG retrieval system with consistently low context precision. | middle_plus | A8 (#85) |
| Compare Context Recall with traditional IR recall. Why is Context Recall computed using "ground truth claims"? | middle_plus | A8 (#86) |
| If your retriever achieves high context precision but low context recall, what types of user queries would suffer most? | middle_plus | A8 (#89) |
| If your RAG retriever consistently shows Context Recall below 0.6, what are three potential root causes? | senior | A8 (#92) |
| Why is it important to optimize both context precision and recall simultaneously? What trade-offs occur? | middle_plus | A8 (#93) |
| Explain why Context Relevancy is "reference-free" while Context Precision/Recall are "reference-dependent". | middle_plus | A8 (#94) |
| How does the Faithfulness metric assess the quality of a RAG generator? | middle | A8 (#97) |
| Distinguish between Faithfulness and Context Precision. Why might a system have high Context Precision but low Faithfulness? | middle_plus | A8 (#98) |
| A RAG system has high context precision but low faithfulness. How would you address this? | senior | A8 (#99) |
| How does Response Relevancy differ from Context Relevancy, and why do you need both? | middle_plus | A8 (#102) |
| The generator's response mentions facts not present in the retrieved context. How are faithfulness and response relevancy impacted? | middle_plus | A8 (#103) |
| What are the risks of relying solely on response relevancy? | middle_plus | A8 (#105) |
| How do you evaluate a RAG system end-to-end? | middle_plus | A10 |
| How to evaluate RAG-based systems? | middle | A9 |

**RAG-инциденты (сценарные)**

| Вопрос | Грейд | Источник |
|---|---|---|
| Что вы сделаете, если у RAG-сервиса вдруг упало качество в проде? | senior | A6 |
| Your RAG system is hallucinating despite having the right context. How do you fix it? | middle_plus | A10 |
| Your RAG system fails on multi-hop questions that require combining multiple facts. How do you fix it? | middle_plus | A10 |
| Your enterprise RAG system returns contradictory answers from different source documents. How do you resolve conflicts? | senior | A10 |
| Your RAG system returns outdated answers from an evolving knowledge base. How do you keep it current? | middle_plus | A10 |
| Your RAG knowledge base gets updated frequently and needs versioning. How do you manage it? | middle_plus | A10 |
| Your RAG system fails on domain-specific jargon. How do you fix it? | middle_plus | A10 |
| Your text-only RAG system now needs to handle images and tables. How do you extend it? | middle_plus | A10 |
| Your vector search returns irrelevant results despite high similarity scores. How do you fix it? | middle_plus | A10 |
| How do you implement citation and source attribution in RAG? | middle_plus | A10 |
| How do you handle document updates and maintain freshness in a RAG system? | middle | A10 |
| How do you handle structured data (tables, SQL databases) in a RAG pipeline? | middle_plus | A10 |
| What is multi-modal RAG, and how does it differ from text-only RAG? | middle_plus | A10 |
| How to handle multi-hop/multifaceted queries? | middle_plus | A9 |
| How do you build production grade document processing and indexing pipeline? | senior | A9 |

---

### 14. Агенты, tool-calling, MCP

| Вопрос | Грейд | Источник |
|---|---|---|
| Объясните function calling | middle | A3 (#10) |
| Что такое ReAct и зачем? | middle | A3 (#11) |
| Когда multi-agent оправдан и когда — overkill? | middle_plus | A3 (#12) |
| Что такое MCP (Model Context Protocol)? | middle | A3 (#13) |
| Чем DSPy отличается от LangChain? | middle_plus | A3 (#28) |
| Что такое function calling / tool use? | junior | A6 (#28) |
| Расскажите подробно про ваш кейс реализации AI-агента (RAG-системы). `[REAL]` | middle | A2, **Waibee** |
| Какие проблемы вы видите при создании LLM-агента для генерации SQL-запросов к legacy-базе? `[REAL]` | senior | A2, **PulsePoint** |
| Стоит ли интегрировать существующие отчёты компании как tool для LLM? Какие проблемы? `[REAL]` | middle | A2, **PulsePoint** |
| What is an AI agent, and how does it differ from a simple LLM call? | junior | A10 |
| What is tool use (function calling) in LLMs, and how does it enable agents? | junior | A10 |
| How do you design and define tools for an AI agent? | middle_plus | A10 |
| What is the Plan-and-Execute agent pattern? / Explain Plan and Execute prompting strategy | middle | A10 / A9 |
| Explain ReAct prompting with a code example and its advantages | middle | A9 |
| Explain the difference between OpenAI functions vs LangChain Agents | middle | A9 |
| What is the difference between single-agent and multi-agent systems? | middle | A10 |
| What are the different types of agent memory (short-term, long-term, episodic)? | middle | A10 |
| What is an agent loop, and how does it decide when to stop? | middle_plus | A10 |
| How do you handle agent failures and implement error recovery? | middle_plus | A10 |
| How do you evaluate and test AI agents? / How do you evaluate the quality of AI agents? | middle_plus | A10 |
| What are the security risks of agentic systems, and how do you mitigate them? | senior | A10 |
| How do you manage token consumption and cost in long-running agent workflows? | middle_plus | A10 |
| What is the human-in-the-loop pattern for agents, and when is it needed? | middle | A10 |
| How do you implement guardrails for AI agents to prevent harmful actions? | middle_plus | A10 |
| What is agent reflection, and how does it improve agent performance? | middle | A10 |
| What is agent orchestration, and how do you implement it? | senior | A10 |
| How do you build a code execution agent safely using sandboxed environments? | senior | A10 |
| Your AI agent is stuck in an infinite loop. How do you detect and break the cycle? | middle_plus | A10 |
| Your AI agent gets conflicting answers from different tools. How does it reconcile them? | middle_plus | A10 |
| Your AI agent burns too many tokens per task. How do you reduce token consumption? | middle_plus | A10 |
| Your AI agent keeps exceeding its budget per task. How do you enforce budget limits? | middle_plus | A10 |
| Your AI agent hallucinates tool capabilities and passes wrong inputs. How do you fix it? | middle_plus | A10 |
| Your AI agent deleted a production database. How do you prevent irreversible actions? | senior | A10 |
| Your AI agent has many tools, but keeps picking the wrong one. How do you improve tool selection? | middle_plus | A10 |
| Your LLM selects the right tool but extracts the wrong parameters. How do you fix parameter extraction? | middle_plus | A10 |
| Your AI agent takes too long to complete a task. How do you speed it up? | middle_plus | A10 |
| How do you build a customer support agent with escalation logic? | senior | A10 |
| How do Computer-Use Agents work? | middle_plus | A10 |
| How AI Agents Communicate? / What are AI SubAgents? | middle | A10 |

---

### 15. Prompt engineering и in-context learning

| Вопрос | Грейд | Источник |
|---|---|---|
| Explain the basic structure prompt engineering. / Explain type of prompt engineering. | junior | A9 |
| Explain in-context learning | junior | A9 |
| What are some aspects to keep in mind while using few-shot prompting? | middle | A9 |
| What are certain strategies to write good prompt? | junior | A9 |
| How to improve the reasoning ability of LLM through prompt engineering? / How to improve LLM reasoning if your CoT prompt fails? | middle_plus | A9 |
| What is Chain-of-Thought prompting, and when is it useful? Explain the reason behind its effectiveness. Trade-offs? | middle | A7 (Q74–76) |
| What is In-Context Learning (ICL), and how is few-shot prompting related? | junior | A7 (Q82) |
| What is self-consistency prompting, and how does it improve reasoning? | middle_plus | A7 (Q83) |
| What is the difference between zero-shot and few-shot prompting? What are the different approaches for choosing examples? | junior/middle | A7 (Q78–79) |
| What is a system prompt, and how does it differ from a user prompt? | junior | A7 (Q81) |
| How would you structure a prompt to ensure the LLM output is in a specific format, like JSON? | middle | A7 (Q86) |
| Describe a strategy for reducing hallucinations via prompt design. | middle | A7 (Q85) |
| Explain the purpose of ReAct prompting in AI agents. | middle | A7 (Q87) |
| What is tree-of-thought prompting? | middle_plus | A10 |
| What is prompt chaining, and how do you design a chain of prompts for complex tasks? | middle_plus | A10 |
| What is the difference between prompt engineering and prompt tuning? | middle | A10 |
| What is a prompt template, and how do you design one for production use? | middle | A10 |
| How do you version and manage prompts in production? | middle_plus | A10 |
| How do you evaluate and iterate on prompt quality? | middle_plus | A10 |
| What are meta-prompts, and how can they be used to generate prompts? | middle_plus | A10 |
| What are the common failure modes in prompting, and how do you debug them? | middle_plus | A10 |
| Your few-shot prompting gives inconsistent results across similar inputs. How do you stabilize it? | middle_plus | A10 |
| Your LLM classification system is too sensitive to prompt wording changes. How do you reduce prompt sensitivity? | middle_plus | A10 |
| Your chain-of-thought prompting is not improving LLM accuracy on reasoning tasks. What do you fix? | middle_plus | A10 |
| Your LLM keeps ignoring your instructions. How do you make it follow structured output formats? | middle | A10 |
| What are output parsers, and why are they needed for production applications? | middle | A10 |
| How do you handle multi-language prompting effectively? / Your AI system works in English but fails for other languages. | middle_plus | A10 |
| How do you optimize prompts for cost and latency? | middle_plus | A10 |
| Какую модель обучить для генерации текстовых описаний, если промтинг не работает? `[REAL]` | middle | A2, **Яндекс** |

---

### 16. Галлюцинации

| Вопрос | Грейд | Источник |
|---|---|---|
| Что такое hallucinations и как с ними бороться? | junior | A6 (#26) |
| Как избежать hallucinations? | middle | A3 (#23) |
| What is hallucination, and how can it be controlled using prompt engineering? | middle | A9 |
| What are different forms of hallucinations? / How to control hallucinations at various levels? | middle_plus | A9 |
| Hallucination in LLMs is a known issue — how can you evaluate and mitigate it? | middle_plus | A11 |
| What are hallucinations in LLMs, and how do you mitigate them? | junior | A10 |
| How do you detect and measure hallucinations in LLM outputs? | middle_plus | A10 |
| How do you measure factual consistency in LLM outputs? | middle_plus | A10 |
| Explain the Chain of Verification. | middle_plus | A9 |
| Your LLM does not admit when it does not know the answer. How do you make it say "I don't know"? | middle_plus | A10 |
| Your QA system always generates an answer even when no answer exists in the context. How do you detect unanswerable questions? | middle_plus | A10 |
| Your summarization system hallucinated facts not in the original article. How do you fix it? | middle_plus | A10 |
| How do you handle hallucinations when they occur in a production AI system? | senior | A10 |
| Может ли быть такое, что модель даёт вероятность какого-то класса 90+%, но при этом всё равно ошибается? (калибровка) | middle | A1 (ANALYSE) |
| Как искать и диагностировать ошибки и галлюцинации (разделы Debugging / Robustness) | middle_plus | A17 |

---

### 17. Оценка LLM: бенчмарки, метрики, LLM-as-judge

| Вопрос | Грейд | Источник |
|---|---|---|
| Какие есть метрики качества для LLM (BLEU, ROUGE, BERTScore, LLM-as-judge)? | junior | A6 (#27) |
| Как мерять качество LLM-приложения? | middle | A3 (#17) |
| Что такое LLM-as-a-judge? | middle | A3 (#18) |
| Что такое evaluation в CI для LLM? | middle_plus | A3 (#27) |
| Как бы вы построили eval для чат-бота поддержки без human annotators? | senior | A6 |
| Как построить офлайн-метрику качества генерации текстов? `[REAL]` | middle | A2, **Яндекс** |
| Почему нельзя просто заменить основную LLM на LLM-Judge, если та даёт лучшие ответы? `[REAL]` | senior | A2, **Candy.ai** |
| How do you evaluate the best LLM model for your use case? | middle | A9 |
| What are different metrics for evaluating LLMs? | middle | A9 |
| How do you evaluate LLM outputs? What metrics do you use? | middle | A10 |
| Explain BLEU, ROUGE, and BERTScore. When would you use each? | middle | A10 |
| What is G-Eval, and how does it use LLMs for evaluation? | middle_plus | A10 |
| What is LLM-as-a-judge evaluation, and what are its limitations? | middle_plus | A10 |
| What are benchmark suites (MMLU, HumanEval, GSM8K), and how do you interpret them? | middle | A10 |
| What is the difference between offline and online evaluation for AI systems? | middle | A10 |
| How do you build a regression test suite for AI applications? | middle_plus | A10 |
| How do you implement continuous evaluation for production AI systems? | senior | A10 |
| What is the role of golden datasets in AI evaluation? | middle | A10 |
| How do you compare two models or prompts in a statistically rigorous way? | senior | A10 |
| How do you evaluate the robustness of an LLM application across input variations? | middle_plus | A10 |
| What are the key differences between evaluating traditional ML vs LLM applications? | middle | A10 |
| How do you set up an evaluation framework from scratch for a new LLM application? | senior | A10 |
| How do you evaluate multi-turn conversation quality? | middle_plus | A10 |
| What is evaluation-driven development for AI applications? | middle | A10 |
| Why might over-reliance on perplexity as a metric be problematic in evaluating LLMs? | middle_plus | A11 |
| How do you conduct human evaluation for AI systems? | middle_plus | A10 |
| How do you implement A/B testing for LLM systems? | senior | A10 |
| How do you evaluate a fine-tuned model's performance? | middle | A10 |

---

### 18. Безопасность: prompt injection, jailbreak, guardrails, PII

| Вопрос | Грейд | Источник |
|---|---|---|
| Что такое prompt injection и как защищаться? | middle | A3 (#16) |
| What is prompt injection, and what are the different types (direct, indirect)? | middle | A10 |
| What is prompt hacking and why should we bother about it? / types / defense tactics | middle | A9 |
| What is jailbreaking in LLMs, and what are common jailbreak techniques? | middle | A10 |
| How do you implement input and output guardrails for AI systems? | middle_plus | A10 |
| What are guardrails for LLMs, and how do you implement them? | middle | A10 |
| Your chatbot's system prompt containing proprietary business logic is being leaked by users. How do you prevent it? | middle_plus | A10 |
| Your LLM agent is vulnerable to prompt injection that reveals the system prompt. How do you defend it? | middle_plus | A10 |
| Your LLM memorized proprietary training data and leaks it in responses. How do you prevent this? | senior | A10 |
| How do you handle PII and sensitive data in LLM inputs and outputs? | middle_plus | A10 |
| What is red teaming, and how do you red team an LLM application? | middle_plus | A10 |
| How do you structure red teaming for an LLM chatbot before launch? | senior | A10 |
| What is adversarial testing for AI systems? | middle_plus | A10 |
| What is data poisoning, and how can it affect AI models? | middle_plus | A10 |
| Your LLM's training data was deliberately poisoned by an adversary. How do you respond? | senior | A10 |
| A pre-trained model from an open-source repo may contain a hidden backdoor. How do you detect it? | senior | A10 |
| How do you implement content filtering for AI outputs? / content safety filters | middle | A10 |
| Your healthcare chatbot gives medical diagnoses it should not make. How do you add safety guardrails? | senior | A10 |
| A user invokes the right to be forgotten, but their data is in your model weights. How do you comply? | senior | A10 |
| Your AI system is reproducing copyrighted material verbatim. How do you prevent this? | senior | A10 |

---

### 19. Прод, LLMOps, стоимость, мониторинг

| Вопрос | Грейд | Источник |
|---|---|---|
| Что такое LLMOps, и how does it differ from traditional MLOps? | middle | A10 |
| How do you serve LLMs in production? | middle | A10 |
| How do you monitor LLM applications in production? / What is LLM observability? | middle_plus | A10 |
| За какими метриками и параметрами модели нужно следить в продакшене? Как следить за качеством ответов и дрифтом? | middle_plus | A18 |
| Что такое дрейф (drifting) в контексте LLM? | middle | A18 |
| How do you estimate the cost of running an AI-powered feature in production? | middle_plus | A10 |
| How do you optimize LLM inference costs in production? / How to optimize cost of overall LLM System? | middle_plus | A10 / A9 |
| How to estimate the cost of running SaaS-based and Open Source LLM models? | middle | A9 |
| Your LLM costs are too high in production. How do you reduce costs without degrading quality? | middle_plus | A10 |
| Your LLM API has latency spikes during peak hours. How do you stabilize it? | senior | A10 |
| Your application is hitting LLM provider rate limits during peak hours. How do you handle it? | middle_plus | A10 |
| Your application depends on one LLM provider. How do you switch providers without downtime? | senior | A10 |
| One LLM provider outage took down your entire system. How do you eliminate single points of failure? | senior | A10 |
| Your AI system handles 100 requests/sec but crashes at 5000. How do you scale for concurrent requests? | senior | A10 |
| Your multi-LLM pipeline fails when one model in the chain breaks. How do you handle orchestration failure? | senior | A10 |
| Your AI pipeline has zero visibility into which step is failing. How do you add observability? | middle_plus | A10 |
| One failing AI component can take down your entire platform. How do you design graceful degradation? | senior | A10 |
| What is CI/CD for AI applications, and how does it differ from traditional CI/CD? | middle_plus | A10 |
| What is a gateway pattern for LLM API management? | middle_plus | A10 |
| How do you implement caching strategies for LLM applications? | middle_plus | A10 |
| How do you implement streaming responses / token streaming for real-time AI applications? | middle | A10 |
| How do you implement structured output from LLMs reliably in production? | middle_plus | A10 |
| What are the key SLAs and metrics for production AI systems (latency, throughput, availability)? | middle_plus | A10 |
| How do you decide between using an LLM API vs self-hosting an open-source model? | middle | A10 |
| Что такое NVIDIA Device Plugin в Kubernetes? Что такое NVIDIA GPU Operator / MIG Profiles? | middle_plus | A18 |
| Минусы и ограничения локальных LLM | middle | A18 |

---

### 20. LLM system design / «как сделать под ограничением X»

| Задача | Грейд | Источник |
|---|---|---|
| Опишите архитектуру LLM-приложения в проде на 1000 RPS | senior | A3 (#30) |
| Кейс: LLM-чатбот для поддержки (ML System Design) | senior | A5 |
| Кейс: Search autocomplete | middle_plus | A5 |
| Кейс: Real-time speech-to-text для звонков | senior | A5 |
| Как спроектировать систему для выбора оптимального банковского продукта с помощью LLM-двойника клиента? `[REAL]` | senior | A2, **ВТБ** |
| Как бы вы строили систему генерации текстовых описаний для карточек товаров при запуске в новой стране (Китай)? `[REAL]` | senior | A2, **Яндекс** |
| System Design: спроектируйте систему ранжирования для e-commerce поиска. Сначала простое решение, затем сложнее. `[REAL]` | senior | A2, **Constructor** |
| Как масштабировать ранкер при миллионе кандидатов? Пользователь не дождётся инференса бустинга. `[REAL]` | senior | A2, **Constructor** |
| Вы добавили трансформер-ранкер, и резко просела латентность и пропускная способность. Что делать? `[REAL]` | senior | A2, **Дром.ру** |
| AI System Design «5-layer spine»: model → wrapping layer (RAG/tools/memory) → evals & guardrails → production & ops → optimization | senior | A12 |
| Кейсы A12: customer support agent (tools + escalation), enterprise research assistant (multi-source retrieval + permissions), text-to-SQL copilot, financial/ops decisioning (evals + audit), security & compliance agent (real-time guardrails, low FP budget), coding agent (context compaction, verification loops), document decisioning, real-time voice agent (streaming, turn-taking), SDR sales agent, clinical scribe (faithfulness safety) | senior | A12 |
| You need to choose between a complex agentic system that scores 15% better on benchmarks, or a simpler RAG pipeline that is easier to maintain. How do you decide? | senior | A10 |
| How do you design for latency vs quality trade-offs in AI systems? | senior | A10 |
| How do you approach capacity planning for an AI system? | senior | A10 |
| How would you approach building an AI feature with limited labeled data? | middle_plus | A10 |
| Your PM wants to ship an AI feature with a 15% hallucination rate on edge cases. How do you communicate the risk? | senior | A10 |
| Design a RAG system that handles conflicting information across sources. | senior | A10 |
| Case Study: LLM Chat Assistant with dynamic context based on query | senior | A9 |

---

### 21. Кодинг-секции по NLP/LLM

| Задача | Грейд | Источник |
|---|---|---|
| Напишите TF-IDF с нуля. | junior | A1 (#1) |
| Напишите attention с нуля. | middle | A1 (#35) |
| Реализуйте LoRA-адаптер с нуля. | middle_plus | B (yuan-meng.com — сниппет) |
| Реализуйте KV cache / beam search / Transformer encoder-decoder. | middle_plus | B (yuan-meng.com — сниппет) |
| Как реализовать speculative decoding с нуля? | senior | A6 |
| Перцептрон на NumPy: forward, BCE loss, backward. Обучите на AND, OR, XOR. Почему XOR не решается одним нейроном? | junior | A6 |
| На собеседовании могут дать готовый код обучения языковой модели с расписанным трансформер-блоком и attention, и просить его разобрать/починить. | middle | B (habr 704128 — сниппет) |
| Coding and Practical Implementation (раздел) | middle | A10 |

---

## Что интервьюеры ловят этими вопросами

1. **Понимание, а не заучивание формулы.** Классический маркер — `/√d_k`. Кандидат, который говорит «так в статье», проваливает.
   Ожидаемый ответ: дисперсия скалярного произведения растёт как `d_k`; деление на `√d_k` возвращает std ≈ 1;
   без этого софтмакс насыщается и градиент занулится. Follow-up-ловушка: «а почему не делить на `d_k`?» —
   потому что тогда дисперсия станет `1/d_k`, распределение внимания станет почти равномерным.
2. **Различение «что» и «зачем» в позиционном кодировании.** Ловят на вопросе «почему нельзя просто прибавить индекс токена»
   (A1 #56) и «почему мы не учим positional embeddings» (A1 #57) — тут проверяют понимание экстраполяции за пределы обучающей длины.
3. **Память и цифры.** Вопросы «How to calculate size of KV cache» (A9), «Как изменятся ресурсы при gradient accumulation» (A1 #76),
   «Что делать, если LoRA с маленьким r всё равно не лезет по памяти» (A1 #91) — проверяют, умеет ли кандидат считать VRAM,
   а не перечислять техники. Формула KV-cache (`2 · n_layers · n_kv_heads · d_head · seq_len · batch · bytes`) — must-have.
4. **Умение отличать похожие сущности.** BERT vs GPT (Ozon), MLM vs CLM, LoRA vs prefix/prompt/p-tuning,
   GPTQ vs AWQ vs bitsandbytes, PPO vs DPO vs GRPO, bi-encoder vs cross-encoder, sparse vs dense.
   Почти всегда следующий вопрос — «когда что выбрать» с конкретным ограничением.
5. **Прод-мышление вместо «сделаю RAG».** Ozon/Дром.ру/Constructor спрашивают ровно про деградацию:
   «добавили трансформер-ранкер — упала латентность, что делать», «миллион кандидатов — юзер не дождётся».
   Ожидают каскад (retrieval → лёгкий ранкер → тяжёлый ранкер на топ-K), кэш, дистилляцию, батчинг, квантизацию — с числами.
6. **Осознанность в метриках.** Больше всего вопросов в RAG-банке (A8) — про метрики ретривала и генерации,
   с ручным подсчётом MAP@5 / Context Precision@10. Это фильтр на тех, кто «померил через RAGAS и всё».
7. **Способность признать границы метода.** «Почему нельзя просто заменить основную LLM на LLM-Judge?» (Candy.ai, senior),
   «What are the limitations of LLM-as-a-judge?», «Why is over-reliance on perplexity problematic?» —
   проверяют, знает ли кандидат про position bias / verbosity bias / self-preference bias и про то,
   что судья дороже и медленнее целевой модели, а его качество надо самому валидировать против human labels.
8. **Градация глубины по грейду напрямую.** A1 явно формулирует эталон: на вопрос про «плохие» генерации
   от стажёра ждут 1–2 гипотезы, от мидла — 2–3 подхода, от сеньора — 4–5 подходов с разбором достоинств и недостатков.
   Это надо воспроизвести в хендбуке как формат ответа.
9. **Умение задать уточняющие вопросы.** В system-design-кейсах (A5, A12) первым делом смотрят,
   уточнит ли кандидат SLA по латентности, объём корпуса, требования к цитируемости, приватность, бюджет.

---

## Пробелы, которые чаще всего валят кандидатов

1. **Токенизация «на уровне слова “BPE”».** Не могут объяснить, чем WordPiece отличается от BPE по критерию слияния,
   что делает Unigram LM, зачем byte-level, что происходит при добавлении токенов в словарь (resize эмбеддингов + tied lm_head,
   инициализация новых строк). Отдельная дыра — fertility на русском и её влияние на стоимость.
2. **Позиционное кодирование дальше «синусоид».** RoPE объясняют как «поворот», но не могут показать,
   почему из абсолютного поворота получается относительная зависимость `q_m · k_n` от `m − n`.
   Про ALiBi, position interpolation, NTK-aware, YaRN — молчание.
3. **KV-cache без цифр.** Знают, что «кэшируем K и V», но не считают размер, не знают, почему кэшируется K/V, а не Q,
   не связывают это с MQA/GQA и с тем, что decode-фаза memory-bound, а prefill — compute-bound.
   Отсюда же провал вопроса «почему первый токен медленнее остальных».
4. **PagedAttention/continuous batching путают с обычным батчингом.** Не могут сказать, что PagedAttention —
   это виртуальная память для KV-кэша (блоки + таблица трансляции), убирающая внутреннюю фрагментацию,
   а continuous batching — это планирование на уровне токена, а не запроса.
5. **Квантизация как одно слово.** Не различают weight-only vs weight+activation, PTQ vs QAT,
   GPTQ (послойный least-squares по гессиану, нужна калибровка) vs AWQ (защита salient-каналов по статистике активаций)
   vs bitsandbytes (квантизация на лету при загрузке, без калибровки, лучше под QLoRA-тюнинг) vs GGUF (формат + k-quants под CPU/llama.cpp).
6. **Alignment: «RLHF = обучение с подкреплением».** Не могут объяснить три стадии, зачем нужна KL-регуляризация к SFT-референсу,
   почему DPO убирает reward-модель и critic, чем GRPO отличается (нет critic, baseline = среднее по группе сэмплов на один промпт,
   KL как отдельный член лосса, а не внутри reward), что такое reward hacking и alignment tax.
7. **RAG на уровне «эмбеддинги + косинус».** Нет hybrid search, нет RRF, нет реранкера, нет query transformation,
   нет метрик ретривала отдельно от метрик генерации. Классический провал: система галлюцинирует при правильном контексте —
   кандидат идёт чинить ретривал вместо промпта/faithfulness-гардрейла.
8. **Chunking без учёта структуры документа.** Fixed-size splitting на всё, включая таблицы и PDF с колонками.
   Не знают про parent-child / contextual chunk headers / semantic chunking и их цену.
9. **Оценка LLM.** BLEU/ROUGE применяют к свободной генерации, не понимая, что они меряют n-gram overlap.
   Не умеют строить golden set и не знают про офлайн/онлайн разделение и про регрессионные наборы в CI.
10. **LLM-as-judge без валидации судьи.** Не знают про position/verbosity/self-preference bias
    и про то, что судью надо калибровать против человеческой разметки и рандомизировать порядок.
11. **Prompt injection ≠ jailbreak.** Не различают direct и indirect (инъекция через документ в RAG-контексте),
    не предлагают runtime-guardrails на уровне действий (а не только фильтр текста).
12. **Long context «просто увеличим окно».** Не видят, что это квадрат по attention и линейный рост KV-cache,
    не знают про «lost in the middle», не знают ни одного метода расширения окна.
13. **Fine-tuning vs RAG vs prompting — нет решающего дерева.** Отвечают «зависит», но не формулируют критерии:
    новые знания vs новый формат/стиль/домен, частота обновления данных, требование цитируемости, бюджет, латентность.
14. **Практика по памяти при обучении.** Не знают, из чего складывается память при обучении
    (веса + градиенты + состояния оптимизатора + активации) и почему это ~16 байт/параметр для AdamW fp32,
    и как это чинится (LoRA, QLoRA, gradient checkpointing, ZeRO/FSDP, offloading, gradient accumulation).
15. **Классика NLP забыта.** На junior-собесах в РФ TF-IDF, наивный Байес, word2vec, negative sampling
    и разница BLEU/ROUGE спрашиваются регулярно (A1, A16) — кандидаты «с LLM-бэкграундом» на этом сыпятся.

---

## Рекомендации для структуры глав хендбука по этой теме

Опираюсь на реальную частотность вопросов в собранном корпусе + на структуру A17 (RU senior-план) и A20.

### Раздел «04-nlp» (классика + трансформер)

1. **04.1 Предобработка и классический NLP** — токен/корпус/стоп-слова, стемминг vs лемматизация, POS, NER,
   n-граммы, BoW, TF-IDF (с выводом и кодом с нуля), наивный Байес, метрики близости текстов, косинус vs косинусное расстояние.
   *Уровень: junior. Обязательно, потому что это до сих пор спрашивают (A1, A16, Точка банк).*
2. **04.2 Эмбеддинги** — word2vec (CBOW/Skip-gram, полный вывод лосса, negative sampling, subsampling),
   GloVe, fastText (n-граммы символов → OOV), ELMo; static vs contextual; dense vs sparse;
   выбор размерности; sentence embeddings и пулинг (CLS vs mean vs max) — с явным ответом на вопрос Ozon.
3. **04.3 Метрики генерации и языкового моделирования** — perplexity (и на чём она считается),
   BLEU, ROUGE-1/2/L, METEOR, BERTScore, chrF; когда каждая ломается.
4. **04.4 RNN/LSTM/GRU и seq2seq** — коротко, но с ответом на «сколько параметров в 1-слойной RNN»,
   затухающие градиенты, teacher forcing, bottleneck фиксированного контекстного вектора → мотивация attention.
5. **04.5 Attention** — Bahdanau/Luong → scaled dot-product; полный вывод `/√d_k`;
   маскирование (padding mask vs causal mask); multi-head (зачем несколько голов, что меняется по FLOPs и по памяти);
   self vs cross; сложность O(n²d) и сравнение с RNN; реализация с нуля на PyTorch/NumPy.
6. **04.6 Блок трансформера целиком** — Q/K/V (почему разные матрицы), FFN/SwiGLU, residual,
   LayerNorm vs BatchNorm (почему LN в NLP), Pre-LN vs Post-LN (и почему современные модели Pre-LN),
   dropout, инициализация; разбор архитектуры по блокам «как на доске» (вопрос ZinBrains).
7. **04.7 Позиционное кодирование** — sinusoidal → learned → relative → RoPE (полный вывод) → ALiBi;
   почему теряется порядок; почему нельзя просто индекс; экстраполяция; 2D-варианты для картинок.
8. **04.8 Токенизация** — уровни; BPE, WordPiece, Unigram LM, byte-level BPE, SentencePiece;
   обучение токенайзера; vocab size trade-off; спец-токены; расширение словаря и что при этом ломается;
   fertility для русского; OOV.
9. **04.9 Семейства моделей** — BERT/RoBERTa (MLM+NSP и что убрала RoBERTa), GPT (CLM),
   T5/BART (denoising), encoder-only vs decoder-only vs encoder-decoder;
   почему decoder-only победил; обучение vs инференс у decoder-like.
10. **04.10 Обучение NLP-моделей** — дисбаланс классов, текстовые аугментации, warm-up, gradient clipping,
    Adam vs AdamW, gradient accumulation, packing вместо padding, mixed precision, checkpointing, DDP/FSDP/ZeRO.

### Раздел «05-llm»

1. **05.1 Жизненный цикл LLM** — pretraining → SFT/instruction tuning → alignment → (опц.) domain adaptation.
   Явно: от какого этапа и когда можно отказаться (вопрос A1 #94).
2. **05.2 Scaling laws и MoE** — Kaplan vs Chinchilla, compute-optimal;
   MoE (router, top-k эксперты, load balancing loss), Mixtral; dense vs sparse; плюсы/минусы для инференса.
3. **05.3 Эффективное внимание и память** — MHA → MQA → GQA → MLA; FlashAttention (почему это IO-aware, а не аппроксимация);
   sliding window attention; линейные/разреженные attention.
4. **05.4 Длинный контекст** — почему окно ограничено; position interpolation, NTK-aware scaling, YaRN;
   ALiBi; «lost in the middle»; context rot; компрессия контекста; когда длинный контекст дешевле RAG и когда нет.
5. **05.5 PEFT и файнтюнинг** — full FT vs LoRA vs QLoRA vs adapters vs prompt/prefix/p-tuning;
   выбор r, alpha, target modules; merge адаптеров; катастрофическое забывание и как лечить;
   расчёт памяти для обучения; «LoRA с маленьким r не лезет — что дальше» (сценарий-эталон);
   подготовка датасета и синтетика.
6. **05.6 Alignment** — reward model, PPO с KL к SFT-референсу, DPO (вывод и почему нет reward-модели),
   GRPO/RLVR, KTO, RLAIF, Constitutional AI; reward hacking; alignment tax; качество preference-разметки.
7. **05.7 Декодирование** — greedy, beam search (сложность, где оправдан), temperature, top-k, top-p, min-p,
   repetition/frequency penalty, contrastive search, self-consistency; почему greedy зацикливается;
   что делает `temperature=0`; streaming.
8. **05.8 Инференс и сервинг** — prefill vs decode; KV-cache (расчёт размера, почему не кэшируем Q);
   PagedAttention и vLLM; continuous batching vs static; speculative decoding (draft+verify, medusa/eagle);
   prefix/prompt caching; chunked prefill; TTFT/ITL/throughput; memory-bound vs compute-bound;
   TP/PP/EP; vLLM vs TGI vs SGLang vs Ollama vs llama.cpp.
9. **05.9 Квантизация и компрессия** — INT8/INT4/FP8/BF16; PTQ vs QAT; weight-only vs W+A;
   GPTQ / AWQ / bitsandbytes / GGUF+k-quants / SmoothQuant; калибровка; выбросы;
   когда квантизация ломает качество и как это ловить; дистилляция; прунинг.
10. **05.10 RAG** — индексация, chunking-стратегии (fixed/recursive/semantic/parent-child/contextual headers),
    эмбеддеры и их выбор, vector DB и ANN (HNSW/IVF/PQ/LSH), hybrid search + RRF,
    query transformation (HyDE, decomposition, step-back), reranking (bi- vs cross-encoder, когда пропускать),
    метрики ретривала (Precision@k/Recall@k/MRR/MAP/NDCG) и метрики RAG (Context Precision/Recall/Relevancy, Faithfulness, Answer Relevancy),
    цитирование и attribution, ACL/permissions, freshness и версионирование, latency-бюджет.
    **Отдельный подраздел «Диагностика RAG»**: дерево «что чинить, если …» — 10 сценариев из A10.
11. **05.11 Агенты и tool-calling** — function calling и дизайн схем инструментов, ReAct, Plan-and-Execute,
    reflection, память (short/long/episodic), MCP, multi-agent (когда оправдан), sandbox для code-execution,
    бюджет токенов, обрыв бесконечных циклов, HITL, guardrails на действия, оценка агентов.
12. **05.12 Оценка LLM** — бенчмарки (MMLU/GSM8K/HumanEval) и их ограничения; golden set;
    LLM-as-judge (G-Eval, rubric-based) и три биаса судьи + как валидировать;
    офлайн vs онлайн; регрессионные тесты в CI; A/B для LLM; human eval.
13. **05.13 Галлюцинации** — таксономия (intrinsic/extrinsic, faithfulness vs factuality);
    детекция (self-consistency, NLI-entailment к контексту, uncertainty/logprob-сигналы);
    митигация на всех уровнях (данные → обучение → промпт → RAG → декодирование → post-hoc проверка → guardrail).
14. **05.14 Безопасность** — prompt injection (direct/indirect), jailbreak, утечка system prompt,
    PII, data poisoning/backdoor, guardrails на вход/выход/runtime, red teaming.
15. **05.15 LLMOps** — сервинг, автоскейлинг, роутинг по сложности/цене, кэш, rate limiting,
    фолбэк на второго провайдера, graceful degradation, observability и трейсинг (Langfuse),
    версионирование промптов, дрейф и мониторинг качества ответов, расчёт стоимости фичи.
16. **05.16 LLM System Design** — шаблон ответа по «5-layer spine» (A12) + 6–8 разобранных кейсов:
    саппорт-бот, поиск по внутренней базе с правами, text-to-SQL, генерация описаний товаров,
    модерация, голосовой агент, coding agent, 1000 RPS.
17. **05.17 Кодинг-секция** — attention с нуля, KV-cache с нуля, LoRA-адаптер с нуля,
    beam search, top-p sampling, BPE-трейнер, chunker, RRF-мердж.

### Сквозные правила оформления глав

- Каждый вопрос — с **пометкой грейда** и, где известно, **компанией** (использовать блок §0 как источник «real»).
- Формат ответа по грейдам воспроизвести явно (эталон из A1): junior — 1–2 тезиса, middle — механизм + trade-off,
  middle+/senior — 4–5 подходов с разбором достоинств и недостатков + цифры.
- В каждую главу — блок **«Follow-up, которым добивают»** (например, после `/√d_k` → «а почему не `/d_k`?»).
- В каждую главу — блок **«Красные флаги в ответе»** (что интервьюер слышит как незнание).
- Мини-калькуляторы: память при обучении, размер KV-cache, стоимость токенов, latency-бюджет RAG.
- Русскоязычная терминология с указанием английского оригинала в скобках — вопросы на собесах звучат смешанно.

---

## Сводка по объёму собранного

- Уникальных вопросов, выписанных в этот файл: **≈ 470**.
- Из них с явной пометкой грейда и компании из источника (`[REAL]`): **46**.
- Полностью загруженных и прочитанных источников (группа A): **20**.
- Источников, зафиксированных по сниппетам поиска (группа B): **27**.
- Поисковых запросов выполнено: **18** (RU + EN).
- Общий пул вопросов в исходниках (включая невыписанные дубли и смежные темы): **> 1100**.
