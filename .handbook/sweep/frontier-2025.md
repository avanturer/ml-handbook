# frontier-2025 — прочёс программ

Область: что появилось в 2025–2026 и уже спрашивается на собесах, но могло не попасть в манифест
(117 глав, `.handbook/STRUCTURE.md`). Цель — не «хорошие материалы», а **программы** и **дельта тем**.

Метод: WebSearch (лимит сессии исчерпан на 200-м запросе) + WebFetch. Прямой доступ к сайтам курсов
блокируется на уровне прокси (403 на `stanford-cs336.github.io`, `llmagents-learning.org`,
`agenticai-learning.org`, `hanlab.mit.edu`, `huggingface.co/learn`, `classcentral.com`,
`genai.owasp.org`, `arxiv.org/abs`, `api.github.com`). Обход — через `raw.githubusercontent.com`
(работает стабильно), README репозиториев курсов и awesome-листы. `curl` через прокси тоже
отдаёт `CONNECT tunnel failed 403` — то есть это ограничение среды, а не сайтов.

Пометки: **[ОТКРЫЛ]** — страница реально загружена и прочитана; **[ТОЛЬКО ОПИСАНИЕ]** — состав
программы восстановлен из поисковой выдачи/сниппетов, сама страница не открылась;
**[НЕ ДОСТУПЕН]** — не получил ничего.

---

## Что реально открыл (со ссылками)

Все ссылки ниже — те, которые действительно отдали контент.

**Курсы и учебные программы**
- https://raw.githubusercontent.com/huggingface/mcp-course/main/README.md + `units/en/_toctree.yml` — HF MCP Course
- https://raw.githubusercontent.com/huggingface/agents-course/main/README.md — HF Agents Course
- https://raw.githubusercontent.com/microsoft/ai-agents-for-beginners/main/README.md — MS AI Agents for Beginners (18 уроков)
- https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/README.md — LLM Zoomcamp 2026
- https://raw.githubusercontent.com/mlabonne/llm-course/main/README.md — LLM Course (Scientist/Engineer)
- https://raw.githubusercontent.com/yandexdataschool/nlp_course/master/README.md — ШАД NLP course
- https://raw.githubusercontent.com/cmu-llms-class/cmu-llm-class-website-2025/main/syllabus.md — CMU 11-667 (открыл, но расписание лекций на странице отсутствует)

**Книги / инженерные «учебники»**
- https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md — Chip Huyen, «AI Engineering», полный ToC
- https://raw.githubusercontent.com/stas00/ml-engineering/master/README.md
- https://raw.githubusercontent.com/stas00/ml-engineering/master/inference/README.md
- https://raw.githubusercontent.com/stas00/ml-engineering/master/insights/ai-battlefield.md
- https://raw.githubusercontent.com/SylphAI-Inc/LLM-engineer-handbook/main/README.md

**Awesome-списки как «программы по теме»**
- https://raw.githubusercontent.com/opendilab/awesome-RLVR/main/README.md
- https://raw.githubusercontent.com/testtimescaling/testtimescaling.github.io/main/README.md
- https://raw.githubusercontent.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs/main/README.md
- https://raw.githubusercontent.com/atfortes/Awesome-LLM-Reasoning/main/README.md
- https://raw.githubusercontent.com/0russwest0/Awesome-Agent-RL/main/README.md
- https://raw.githubusercontent.com/xlite-dev/Awesome-LLM-Inference/main/README.md
- https://raw.githubusercontent.com/horseee/Awesome-Efficient-LLM/main/README.md
- https://raw.githubusercontent.com/hemingkx/SpeculativeDecodingPapers/main/README.md
- https://raw.githubusercontent.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling/main/README.md
- https://raw.githubusercontent.com/Meirtz/Awesome-Context-Engineering/main/README.md
- https://raw.githubusercontent.com/wasiahmad/Awesome-LLM-Synthetic-Data/main/README.md
- https://raw.githubusercontent.com/hyp1231/awesome-generative-recommendation/main/README.md
- https://raw.githubusercontent.com/dangkhoasdc/awesome-vector-database/main/README.md

**Прод-системы и стандарты (первоисточники)**
- https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/README.md
- https://raw.githubusercontent.com/a2aproject/A2A/main/README.md
- https://raw.githubusercontent.com/ai-dynamo/dynamo/main/README.md
- https://raw.githubusercontent.com/LMCache/LMCache/dev/README.md
- https://raw.githubusercontent.com/kvcache-ai/Mooncake/main/README.md
- https://raw.githubusercontent.com/sgl-project/sglang/main/README.md
- https://raw.githubusercontent.com/vllm-project/vllm/main/README.md
- https://raw.githubusercontent.com/deepseek-ai/EPLB/main/README.md
- https://raw.githubusercontent.com/mlc-ai/xgrammar/main/README.md
- https://raw.githubusercontent.com/volcengine/verl/main/README.md
- https://raw.githubusercontent.com/huggingface/open-r1/main/README.md
- https://raw.githubusercontent.com/simplescaling/s1/main/README.md
- https://raw.githubusercontent.com/sierra-research/tau-bench/main/README.md
- https://raw.githubusercontent.com/laude-institute/terminal-bench/main/README.md
- https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/README.md
- https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_ai/main/README.md
- https://raw.githubusercontent.com/NVIDIA/NeMo-Guardrails/develop/README.md
- https://raw.githubusercontent.com/guardrails-ai/guardrails/main/README.md
- https://raw.githubusercontent.com/BerriAI/litellm/main/README.md
- https://raw.githubusercontent.com/stanfordnlp/dspy/main/README.md
- https://raw.githubusercontent.com/mem0ai/mem0/main/README.md
- https://raw.githubusercontent.com/facebookresearch/generative-recommenders/main/README.md
- https://raw.githubusercontent.com/lancedb/lancedb/main/README.md
- https://raw.githubusercontent.com/open-telemetry/semantic-conventions/main/docs/gen-ai/README.md (редирект-заглушка)
- https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/README.md

---

## Программы (по каждому источнику — полный список тем)

### 1. Stanford CS336 «Language Modeling from Scratch», Spring 2025 — [ТОЛЬКО ОПИСАНИЕ]
Сайт `stanford-cs336.github.io/spring2025` — 403; репозиторий `stanford-cs336/spring2025-lectures`
README не содержит списка лекций; листинг через `api.github.com` — 403. Состав лекций восстановлен
из поисковой выдачи (плейлист YouTube + Class Central):

1. Overview and Tokenization · 2. PyTorch and Resource Accounting · 3. Architectures, Hyperparameters ·
4. **Mixture of Experts** · 5. GPUs · 6. **Kernels, Triton** · 7. Parallelism 1 · 8. Parallelism 2 ·
9. Scaling Laws 1 · 10. **Inference** · 11. Scaling Laws 2 · 12. Evaluation · 13. Data 1 · 14. Data 2 ·
15. Alignment — SFT/RLHF · 16. Alignment — RL · 17. Alignment — RL · 18–19. гостевые (Junyang Lin, Mike Lewis).

Ценность: единственный курс, где «сделай токенизатор → напиши ядро на Triton → посчитай FLOPs/бюджет →
обучи → выровняй → задеплой» проходится руками. Грейд: middle+ / senior, особенно для LLM-инфраструктуры.
Прямое пересечение с нашими 03-06, 05-01, 05-02, 05-05.

### 2. Berkeley CS294/194-196: LLM Agents (F24) → Advanced LLM Agents (Sp25) → Agentic AI (F25) — [ТОЛЬКО ОПИСАНИЕ]
`llmagents-learning.org/sp25` и `agenticai-learning.org/f25` — 403 (Cloudflare). Из выдачи:

- **Sp25 (Advanced LLM Agents, Dawn Song):** advanced inference-time techniques для reasoning;
  post-training methods for reasoning; search & planning; agentic workflow и tool use; function calling;
  математическое рассуждение и доказательство теорем (Lean, автоформализация); генерация и
  **верификация** кода; ограничения и риски.
- **F25 (Agentic AI, 12 лекций):** foundations of LLMs; reasoning; planning; агентные фреймворки и
  **инфраструктура**; прикладные домены — кодогенерация, робототехника, веб-автоматизация, научное
  открытие; **эксплуатация агентов в проде** (лекция Yangqing Jia: observability-дашборды, routing
  logic, мульти-облако, режимы отказа, backpressure, контроль стоимости); безопасность и security
  (Dawn Song); автономные агенты и обучение (Peter Stone).

Ценность: это ровно то, из чего в 2026 собирают секцию «agents» на собесе middle+. Наша 05-08
покрывает базу, но не инфраструктуру/эксплуатацию агентов.

### 3. HF MCP Course — [ОТКРЫЛ]
Полное оглавление (из `_toctree.yml`):
- **Unit 0**: Welcome.
- **Unit 1 — Introduction to MCP**: Introduction to MCP; Key Concepts and Terminology; Architectural
  Components; Quiz 1; **The Communication Protocol**; **Understanding MCP Capabilities**; MCP SDK;
  Quiz 2; **MCP Clients**; Hugging Face MCP Server; Gradio MCP Integration; Recap; Certificate.
- **Unit 2 — End-to-End MCP Application**: Building the Gradio MCP Server; Using MCP Clients;
  MCP в AI coding assistant; Building an MCP Client with Gradio; **Tiny Agents с MCP и HF Hub**;
  локальные Tiny Agents с NPU/iGPU.
- **Unit 3 — Advanced MCP Development: Custom Workflow Servers**: сервер для Claude Code;
  Module 1 Build MCP Server; Module 2 **GitHub Actions Integration**; Module 3 Slack Notification;
  разбор решения (PR-агент).
- **Unit 3.1 — Use Case**: PR-агент на Hub: setup, MCP-сервер, MCP-клиент, **webhook listener**, квизы.

Ценность: единственная развёрнутая учебная программа по MCP. Грейд: middle+ (интеграция инструментов).

### 4. Спецификация MCP — [ОТКРЫЛ, частично]
`modelcontextprotocol/modelcontextprotocol`: репозиторий содержит спецификацию, JSON/TypeScript-схему
и доки. Актуальная ревизия схемы на момент прочёса — **2025-11-25** (schema/2025-11-25,
TypeScript + JSON Schema). Сама текстовая спека рендерится на `modelcontextprotocol.io` (Mintlify) —
недоступна из среды. То есть: **факт версионирования спеки по датам подтверждён**, детали примитивов
(tools/resources/prompts, транспорты) из первоисточника вытащить не удалось.

### 5. A2A (Agent2Agent) Protocol — [ОТКРЫЛ]
Открытый протокол взаимодействия «непрозрачных» агентов. Ключевое: **Agent Cards** (обнаружение
возможностей), **Tasks** (длительные задачи, агенты сотрудничают, не раскрывая внутреннее состояние,
память и инструменты), транспорт **JSON-RPC 2.0 поверх HTTP(S)** с синхронными вызовами, стримингом и
асинхронными уведомлениями. Позиционируется как **дополнение к MCP**: MCP — «агент↔инструменты»,
A2A — «агент↔агент».

### 6. HF Agents Course — [ОТКРЫЛ]
Unit 0 Welcome · Unit 1 Introduction to Agents (LLM, спецтокены, иерархия моделей) · Unit 2 Frameworks
(2.1 smolagents, 2.2 LlamaIndex, 2.3 LangGraph) · Unit 3 Agentic RAG · Unit 4 Final Project (автооценка +
лидерборд). Бонусы: **fine-tuning под function-calling**, **observability и evaluation**, агенты в играх.

### 7. Microsoft «AI Agents for Beginners» (18 уроков) — [ОТКРЫЛ]
1 Intro & use cases · 2 Agentic frameworks · 3 Agentic design patterns · 4 Tool use · 5 Agentic RAG ·
6 **Trustworthy agents** · 7 Planning · 8 Multi-agent · 9 **Metacognition** · 10 **AI Agents in Production** ·
11 **Agentic protocols (MCP, A2A, NLWeb)** · 12 **Context engineering** · 13 **Agentic memory** ·
14 Microsoft Agent Framework · 15 **Computer-Use Agents (CUA)** · 16 **Deploying scalable agents** ·
17 Local agents · 18 **Securing AI agents**.
Ценность: это фактически чек-лист вопросов по агентам на 2026 год. Уроки 10–18 — прод-часть, которой у
нас нет.

### 8. LLM Zoomcamp 2026 (DataTalksClub) — [ОТКРЫЛ]
Module 1 **Agentic RAG** (RAG на keyword search → agentic через function calling) · Module 2 Vector Search
(эмбеддинги, minsearch/sqlitesearch/PGVector) · Module 3 Orchestration (Kestra) · Workshop: **Data
ingestion — dlt-пайплайны для приёма и анализа LLM-трейсов**, DuckDB, marimo · Module 4 Evaluation
(offline+online, retrieval и answer quality) · Module 5 **Monitoring** (обратная связь пользователей,
health, живые дашборды) · Module 6 Best practices (LangChain, гибридный поиск, реранк) ·
Module 7 End-to-end project · Capstone.

### 9. mlabonne/llm-course — [ОТКРЫЛ]
Fundamentals (математика, Python, NN, NLP) →
**LLM Scientist**: 1 Architecture (обзор, токенизация, attention, сэмплирование) · 2 Pre-training (данные,
распределённое обучение, оптимизация, мониторинг) · 3 **Post-training datasets** (storage & chat templates,
**synthetic data generation**, data enhancement, quality filtering) · 4 SFT · 5 Preference alignment
(**rejection sampling**, DPO, reward model, RL) · 6 Evaluation (automated benchmarks, human, model-based,
feedback signal) · 7 Quantization (GGUF/llama.cpp, GPTQ/AWQ, SmoothQuant/ZeroQuant) · 8 **New trends:
model merging, multimodal, interpretability, test-time compute** →
**LLM Engineer**: 1 Running LLMs (API, OSS, prompt engineering, **structuring outputs**) · 2 Vector storage ·
3 RAG · 4 Advanced RAG (query construction, tools, post-processing, program LLMs) · 5 **Agents (agent
fundamentals, agent protocols, vendor frameworks, other frameworks)** · 6 Inference optimization (Flash
Attention, KV-cache, speculative decoding) · 7 Deployment (local/demo/server/**edge**) · 8 Securing LLMs
(prompt hacking, **backdoors**, defensive measures).

### 10. Chip Huyen, «AI Engineering» — полный ToC — [ОТКРЫЛ]
1 Introduction (rise of AI engineering; use cases; **planning AI applications: use case evaluation,
setting expectations, milestone planning, maintenance**; AI engineering stack; AI vs ML engineering) ·
2 Understanding FM (training data, multilingual/domain-specific; modeling; post-training SFT+preference;
**sampling: fundamentals, strategies, Test Time Compute, Structured Outputs, probabilistic nature**) ·
3 Evaluation Methodology (entropy, cross-entropy, **bits-per-character/bits-per-byte**, perplexity;
exact evaluation; **AI as a Judge** + ограничения + «какие модели годятся в судьи»; **comparative
evaluation / ранжирование моделей**) · 4 Evaluate AI Systems (критерии: domain-specific, generation,
instruction-following, **cost & latency**; model selection workflow; **build vs buy**; навигация по
публичным бенчмаркам; проектирование evaluation pipeline в 3 шага) · 5 Prompt Engineering (+ **defensive
prompt engineering**: reverse prompt engineering, jailbreak/injection, information extraction, защиты) ·
6 RAG and Agents (RAG architecture, retrieval algorithms, retrieval optimization, RAG beyond text;
agents: tools, planning, **failure modes and evaluation**; **Memory**) · 7 Finetuning (когда/когда не;
memory bottlenecks; **memory math**; numerical representations; quantization; PEFT; **model merging и
multi-task finetuning**; finetuning tactics) · 8 **Dataset Engineering** (data curation: quality, coverage,
quantity, acquisition & annotation; **data augmentation and synthesis**, AI-powered synthesis, **model
distillation**; processing: inspect, dedup, clean/filter, format) · 9 Inference Optimization (метрики,
**AI accelerators**, model optimization, inference service optimization) · 10 **AI Engineering
Architecture and User Feedback** (пошагово: enhance context → guardrails → **model router and gateway** →
кэши → agent patterns → monitoring & observability → orchestration; **user feedback: извлечение
обратной связи из диалога, дизайн фидбэка, его ограничения**).

### 11. stas00/ml-engineering — [ОТКРЫЛ]
Структура: Part 1 **Insights** (The AI Battlefield Engineering; **How to Choose a Cloud Provider**;
**When Is It Worth Upgrading GPUs**) · Part 2 Hardware (Compute, Storage, Network) · Part 3 Orchestration
(SLURM) · Part 4 Training · Part 5 **Inference** · Part 6 Development (debugging, testing) · Part 7 Resources.

Глава Inference (открыл целиком): глоссарий (CLA, GQA, **ITL**, KV, LPU, MHA, **MLA**, MQA, QPS, **TPOT**,
**TTFT**); концепции — prefill/decode, **online vs offline inference**, **grounding** и input-grounded
tasks, батчинг (static, continuous/in-flight), paged attention, декодирование, температура,
**guided/structured generation**, speculative decoding, **privacy-preserving inference (FHE/MPC/PPML)**,
tensor/pipeline parallelism; метрики — системные (latency, throughput), пользовательские (TTFT, TPOT),
упрощённые (prefill/decode throughput), **utilization ускорителя**, перцентили; **анатомия памяти:
веса + KV-кэш + активации**; время загрузки модели; бенчмаркинг; сравнение фреймворков; чипы.

Глава «AI Battlefield» (открыл): формула железа — обучение (half mixed precision)
`model_size_in_B * 18 * 1.25 / gpu_size_in_GB`, инференс `model_size_in_B * 2 * 1.25 / gpu_size_in_GB`
(80B → ~23 GPU на обучение, ~3 на инференс); расчёт стоимости через TFLOPS с поправкой на **MFU ≈ 50%**;
сравнение **cloud vs HPC vs покупка железа** (3+ года окупаемости); «вам продают 80% от заявленного
объёма хранилища» — на 100 TB планируйте 125 TB; параллельные ФС (Lustre/GPFS) вместо NFS из-за
множества мелких файлов Python; узкое место — **перемещение битов, а не compute**.

### 12. SylphAI LLM-Engineer-Handbook — [ОТКРЫЛ]
Разделы: Libraries & Frameworks & Tools (Applications, Pretraining, Fine-tuning, Top Models, **Serving**,
**Prompt Management**, Datasets, Benchmarks) · Learning Resources (Applications + Agent, Modeling,
Training, Fine-tuning, Fundamentals, Books, Newsletters, **Auto-optimization**) · Understanding LLMs
(**In-context Learning**, **Reasoning & Planning**) · Community.

### 13. Test-Time Scaling: обзор «What, How, Where, How Well» — [ОТКРЫЛ]
Четырёхмерная таксономия:
- **What to scale**: Parallel (много выходов + агрегация), Sequential (следующие шаги зависят от
  промежуточных), Hybrid, **Internal** (модель сама решает, сколько считать).
- **How to scale**: *Tuning* — SFT на длинных CoT, RL; *Inference* — **Stimulation** (заставить думать
  дольше/больше сэмплов), **Verification** (оценка и отбор, критерии остановки), **Search** (MCTS,
  beam search), **Aggregation** (свод решений).
- **Where**: reasoning (математика, код, наука, игры, медицина) и general-purpose (агенты, знаниевая
  работа, open-ended, мультимодальность).
- **How well**: Performance, **Efficiency (cost-benefit)**, **Controllability** (соблюдение бюджета),
  **Scalability** (скорость роста качества от compute).

### 14. Awesome-RLVR (opendilab) — [ОТКРЫЛ]
Секции: Surveys & Tutorials · **Codebases** (open-r1, OpenRLHF, verl) · Papers по годам.
Технически: политики — **GRPO, PPO, DPO, REINFORCE-варианты**; награды — **verifiable outcome rewards
(бинарная проверка), process rewards (пошаговые), гибриды, борьба с reward hacking**; reasoning —
CoT, self-play/self-improvement, **curriculum**, test-time scaling и распределение compute.
Домены: математика (MATH/AIME/GSM8K), код (HumanEval, LiveCodeBench, Codeforces), **доказательство
теорем (Lean)**, мультимодальность, **веб-агенты и tool use**, long-context.

### 15. verl (ByteDance/volcengine) — [ОТКРЫЛ] — «RLVR в проде»
Алгоритмы: **PPO, GRPO, GSPO, ReMax, REINFORCE++, RLOO, PRIME, DAPO, Dr.GRPO**, KL_Cov & Clip_Cov, SPPO;
награды **model-based и function-based** (математика, код).
Инфраструктура: обучение на FSDP/FSDP2/Megatron-LM; rollout через **vLLM/SGLang/HF Transformers**;
FlashAttention-2, **sequence packing**, sequence parallelism (DeepSpeed Ulysses), LoRA, Liger-kernel,
**expert parallelism до 671B**, multi-GPU LoRA RL.
Кейсы: VLM/мультимодальный RL, **multi-turn с вызовом инструментов**, alignment, reasoning, код и
математика, SFT; трекинг wandb/swanlab/mlflow.

### 16. open-r1 (HF) — [ОТКРЫЛ] — «дистилляция reasoning»
План: Step 1 — воспроизвести R1-Distill **дистилляцией высококачественного корпуса из DeepSeek-R1**;
Step 2 — чистый RL-пайплайн R1-Zero; Step 3 — путь base → RL-tuned через многостадийное обучение.
Рецепты: SFT-дистилляция на `open-r1/Mixture-of-Thoughts`, **max_seq_length 32768**, 5 эпох, lr 4e-5,
bf16, gradient checkpointing; GRPO с vLLM (**режимы colocate и выделенные vLLM-ноды**); генерация
данных — маленькими R1-дистиллятами или полным R1 на кластере через **Ray + Distilabel**;
оценка через **lighteval** на AIME 2024, MATH-500, GPQA Diamond, LiveCodeBench.

### 17. s1: Simple Test-Time Scaling — [ОТКРЫЛ]
**Budget forcing**: контроль числа токенов на размышление (например, 32k) с принудительным
прерыванием/продолжением мысли. Данные — **s1K, всего 1000 примеров** с трейсами рассуждений
(в s1K-1.1 трейсы перегенерены R1). Заявка: уровень o1-preview при 1000 примерах + budget forcing.

### 18. «Stop Overthinking»: Efficient Reasoning survey — [ОТКРЫЛ]
Категории: RL с **length reward**; SFT на CoT переменной длины; сжатие шагов рассуждения в **латентные
представления**; **динамическая парадигма рассуждения на инференсе**; prompt-guided efficient reasoning;
**маршрутизация по атрибутам задачи** (какой режим рассуждения включить); перенос reasoning в
маленькие модели через дистилляцию и сжатие; бенчмарки эффективности.

### 19. Awesome-LLM-Reasoning (atfortes) — [ОТКРЫЛ]
Survey · Analysis · Technique (reasoning как emergent ability; мультимодальный reasoning;
**масштабирование reasoning на маленькие модели**) · ресурсы.

### 20. Awesome-Agent-RL — [ОТКРЫЛ]
Структура слабее (список работ + OSS-проекты: OpenManus-RL, RAGEN, Agent-R1, VAGEN). Сквозная идея —
**end-to-end многошаговый RL для агентов вместо пошаговой оптимизации**, **turn-level credit
assignment**, multi-turn RL-фреймворки, память как объект обучения (MemAgent), поисковые агенты
(ASearcher).

### 21. Awesome-LLM-Inference (xlite-dev) — [ОТКРЫЛ]
Оглавление: Trending LLM/VLM Topics · **DeepSeek/Multi-head Latent Attention (MLA)** · Multi-GPU/Multi-Node
Parallelism · **Disaggregating Prefill and Decoding** · Algorithmic/Eval Survey · Train/Inference
Framework Design · Weight/Activation Quantize · **Continuous/In-flight Batching** · IO/FLOPs-Aware/Sparse
Attention · **KV Cache Scheduling/Quantize/Dropping** · **Prompt/Context Compression** · Long Context
Attention/KV Cache Optimization · **Early-Exit/Intermediate Layer Decoding** · Parallel Decoding/Sampling ·
Structured Prune/KD/Weight Sparse · **MoE LLM Inference** · CPU/NPU/FPGA/Mobile · **Non-Transformer
Architecture** · GEMM/Tensor Cores/WMMA · VLM/Position Embed · Applications.

### 22. Awesome-Efficient-LLM (horseee) — [ОТКРЫЛ]
Pruning/Sparsity · KD · Quantization · Inference Acceleration · **Efficient MoE** · Efficient Architecture ·
**KV Cache Compression** · **Text Compression** · Low-Rank Decomposition · **Hardware/System/Serving** ·
Efficient Fine-tuning · Efficient Training · Survey/Benchmark · Reasoning Model (вынесен отдельно).

### 23. SpeculativeDecodingPapers — [ОТКРЫЛ]
Таксономия по способу драфтинга: **малая draft-модель** (SpS, SpecInfer, DistillSpec, GliDe);
**self-drafting** — layer-skipping (Draft&Verify, LayerSkip, SWIFT), early-exit (SPEED, FREE),
**Jacobi/Lookahead**, спец-головы (**Medusa**, **EAGLE**, Hydra), авторегрессионные головы (EAGLE,
Amphista); **retrieval-based** (REST, NEST, TriForce); гибриды — **token trees** (Sequoia, OPT-Tree,
EAGLE-2), multi-candidate (MCSD), графовые (GSD); n-gram-драфт (ANPD).

### 24. vLLM — [ОТКРЫЛ] — состав фич на 2026
PagedAttention; **continuous batching, chunked prefill, prefix caching**; piecewise/full CUDA-graphs;
квантизация **FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ/AWQ, GGUF, compressed-tensors, TorchAO**;
FlashAttention/FlashInfer; **speculative decoding: n-gram, suffix, EAGLE, DFlash**; **disaggregated
prefill, decode and encode**; structured outputs и tool calling; API — OpenAI-совместимый + **Anthropic
Messages API** + gRPC; параллелизм — **tensor, pipeline, data, expert, context**; 200+ архитектур;
плагины под TPU, Gaudi, Spyre, Ascend.

### 25. SGLang — [ОТКРЫЛ]
**RadixAttention для prefix caching**; zero-overhead CPU scheduler; **prefill-decode disaggregation**;
speculative decoding; continuous batching; paged attention; параллелизм tensor/pipeline/**expert**/data;
**structured outputs**; chunked prefill; квантизация FP4/FP8/INT4/AWQ/GPTQ; **multi-LoRA batching**;
языковые, эмбеддинг-, reward- и diffusion-модели.

### 26. NVIDIA Dynamo — [ОТКРЫЛ] — эталон «инференс-платформы 2026»
1) **Disaggregated prefill/decode** — независимо масштабируемые пулы GPU; 2) **KV-aware routing** —
маршрутизация по загрузке воркера и **перекрытию KV-кэша**; 3) **KV Block Manager (KVBM)** — оффлоад
KV-кэша **GPU → CPU → SSD → удалённое хранилище (S3/Azure blob)**; 4) **ModelExpress** — стриминг весов
между GPU для быстрого холодного старта; 5) **Planner** — SLA-driven автоскейлер, профилирует нагрузку
и подбирает размеры пулов; 6) **Grove** — k8s-оператор с topology-aware планированием по стойкам;
7) **AIConfigurator** — симуляция конфигураций деплоя; 8) **отказоустойчивость** — health-checks и
**миграция запросов в полёте**.

### 27. LMCache — [ОТКРЫЛ]
**Слой управления KV-кэшем**: многоуровневый оффлоад и переиспользование (GPU→CPU RAM→SSD→удалённо);
**CacheBlend — переиспользование не-префиксного KV** с выборочным пересчётом токенов для восстановления
качества; бэкенды CPU RAM, SSD, **Redis/Valkey, S3, InfiniStore, NIXL**; **production-level KV cache
observability** (health, диагностика, метрики); работает как **отдельный демон** — кэш переживает
падение инференс-движка.

### 28. Mooncake (Moonshot AI / Kimi) — [ОТКРЫЛ]
**KVCache-centric дизагрегированная архитектура**: раздельные кластеры prefill и decode + пул KV-кэша,
собранный из **недоиспользуемых CPU, DRAM и SSD в GPU-кластере**. Компоненты: **Transfer Engine**
(единый интерфейс батчевой передачи данных, topology-aware маршрутизация, агрегация нескольких NIC;
87 GB/s на 4×200 Gbps и 190 GB/s на 8×400 Gbps RoCE); **Mooncake Store** (распределённый KV-кэш,
многоуровневая иерархия, lifecycle-управление объектами DRAM/NVMe); **Mooncake EP & Process Group**
(**отказоустойчивый expert parallelism** для MoE, детекция и восстановление после сбоев).
Прод: Kimi — **+75% обработанных запросов при соблюдении SLO**; Kimi K2 на 128×H200 с PD-дизагрегацией.
Интеграции: SGLang, vLLM.

### 29. DeepSeek EPLB — [ОТКРЫЛ] — MoE в проде
**Expert-Parallel Load Balancer**: эксперты потребляют разный объём ресурсов, поэтому вводятся
**избыточные (дублированные) эксперты** — «горячие» эксперты копируются на несколько GPU, и запросы
роутятся на реплики. Две стратегии: **hierarchical** (когда группы экспертов делятся на ноды нацело:
сначала балансируем ноды, потом дублируем внутри ноды, потом раскладываем по GPU — подходит для
**prefill с малым EP-размером**) и **global** (игнорируем группы, реплицируем глобально — для
**decode с большим EP-размером**).

### 30. XGrammar — [ОТКРЫЛ] — структурированный вывод
Constrained decoding с **100% структурной корректностью** и **near-zero overhead** на JSON. Поддержка
JSON / regex / **контекстно-свободных грамматик**; Linux/macOS/Windows, CPU/GPU/Apple Silicon/TPU;
API для Python/C++/JS/Swift. **Дефолтный бэкенд структурной генерации в vLLM, SGLang, TensorRT-LLM,
MLC-LLM**; интеграции OpenVINO GenAI, Modular MAX.

### 31. Awesome-LLM-Long-Context-Modeling — [ОТКРЫЛ]
Efficient Attention (sparse/linear/memory-aware) · **KV-Cache Optimization (eviction, quantization,
offloading)** · Recurrent Transformers · **SSM и гибриды** · Position Encoding & **length extrapolation** ·
Long-Context Training (continual pretraining) · **Long-Term Memory (диалоговая, параметрическая,
рабочая)** · RAG · **Long ICL / many-shot** · **Context Compression (token/prompt compression)** ·
Model Compression · **Long CoT** · Long Video/Image · **Long-Horizon Agents** · Long-form generation ·
**Inference Acceleration & Serving** · Benchmarks & Evaluation · Technical Reports.

### 32. Awesome-Context-Engineering — [ОТКРЫЛ]
1 Определение (контекст, **динамическая оркестрация контекста**, байесовская трактовка, сравнение с
prompt engineering) · 2 Зачем (ограничения статического промптинга, **enterprise/production
requirements**) · 3 Компоненты и архитектуры (**context scaling**, **context management in production**,
интеграция структурированных данных, self-generated context) · 4 Реализация (**agent harnesses и
runtime-системы**, RAG, **memory systems**, agent communication, tool use) · 5 Оценка (**context quality
assessment**, бенчмарки, **agent observability и телеметрия**) · 6 Применения (research-системы,
кодовые агенты) · 7 Ограничения.

### 33. mem0 — [ОТКРЫЛ] — память агентов как отдельная подсистема
Многоуровневая память (**user / session / agent state**); single-pass ADD-only извлечение одним
LLM-вызовом; **entity linking** между воспоминаниями; **multi-signal retrieval** — семантика + **BM25** +
entity matching с параллельным скорингом и слиянием; **temporal reasoning** (текущее состояние,
прошлые события, планы); факты, сгенерированные агентом, — «first-class».
Бенчмарки: **LoCoMo 92.5**, **LongMemEval 94.4**, **BEAM 1M — 64.1**, BEAM 10M — 48.6, при ~6.7–6.9K
токенов контекста и p50 < 1.1 c.

### 34. tau-bench (Sierra) — [ОТКРЫЛ] — оценка агентов
Диалог агента с **симулированным LLM-пользователем**, доменные API-инструменты и **policy guidelines**.
Домены: **airline, retail** (в τ³-bench добавлены банкинг и голос). Метрика — **Pass^k** (не pass@k!):
доля задач, решённых **во всех k независимых прогонах** → измеряет **надёжность/воспроизводимость**
агента, а не «хотя бы раз получилось». Поддержка стратегий агента (tool-calling, ReAct, Act) и
симуляторов пользователя (LLM, ReAct, verify, reflection); **автоматический классификатор ошибок**
по типу и «виновнику».

### 35. terminal-bench — [ОТКРЫЛ]
~100 сквозных задач в **терминале в песочнице**: собрать код, обучить модель, поднять сервер. Каждая
задача = **инструкция на английском + тест-скрипт (автоматическая проверка) + oracle-решение**.
Харнесс подключает модель к sandbox-окружению; версионируемый датасет + лидерборд.

### 36. Berkeley Function Calling Leaderboard (BFCL) — [ОТКРЫЛ]
v1 — Simple / Parallel / Multiple function call через **AST-сравнение**; v2 — **Live-данные** от
энтерпрайза и OSS (борьба с протечкой); v3 — **multi-turn и multi-step**; v4 — **агентность: web search,
memory, чувствительность к формату**. Отдельно — **relevance/hallucination**-проверки (вызывать ли
функцию вообще).

### 37. Inspect (UK AI Security Institute) — [ОТКРЫЛ]
Фреймворк оценки моделей и агентов: prompt engineering, tool use, многошаговый диалог,
**model-graded evaluations**; библиотека **200+ готовых оценок**; расширяется сторонними Python-пакетами
(новые техники elicitation и скоринга). Де-факто отраслевой инструмент для safety-оценок.

### 38. NeMo Guardrails — [ОТКРЫЛ]
**Пять типов rails**: **input rails** (отклонить/изменить пользовательский ввод), **dialog rails**
(влияют на промпт и решение — звать ли LLM/выполнять ли действие, или отдать заготовленный ответ),
**retrieval rails** (отклонить извлечённый чанк в RAG), **execution rails** (проверка входов/выходов
инструментов), **output rails** (отклонить/изменить ответ). Кейсы: QA/RAG с фактчекингом и модерацией,
доменные ассистенты «на теме», защита кастомных LLM-эндпоинтов.

### 39. Guardrails AI — [ОТКРЫЛ]
Концепция **Guard** — обёртка над входом/выходом LLM, собранная из валидаторов; **Guardrails Hub**
(regex, детект конкурентов, токсичность, кастомные валидаторы); настраиваемое поведение при провале
(исключение/фильтрация); генерация структурированных данных через Pydantic; **Guardrails Server** —
отдельный сервис с REST/OpenAI-совместимым API, в проде — Docker + Gunicorn.

### 40. LiteLLM — [ОТКРЫЛ] — LLM-гейтвей как архитектурный слой
Единый OpenAI-формат для 100+ провайдеров; **Auto Router**; балансировка между деплоями; **virtual keys**,
**spend tracking по проектам/пользователям, бюджеты**; ретраи и **фолбэки между провайдерами**;
заявленные **8 ms p95 при 1k RPS**; админ-дашборд, коллбэки в Langfuse/MLflow/Lunary; **guardrails**;
кэширование; мультитенантность.

### 41. OpenTelemetry GenAI Semantic Conventions — [ОТКРЫЛ, частично]
Конвенции **вынесены в отдельный репозиторий** `open-telemetry/semantic-conventions-genai`. Область:
**спаны, метрики и события для GenAI-клиентов, для MCP и для провайдеров (OpenAI и др.)**;
человекочитаемая версия в `docs/`, YAML-модель в `model/`, эталонные реализации в `reference/`.
Конкретные имена атрибутов вытащить не удалось (файлы внутри `docs/` не перебирал — листинг каталога
через API недоступен).

### 42. Awesome-LLM-Synthetic-Data — [ОТКРЫЛ]
Surveys · Methods (**Techniques**, **Instruction Generation with High Quality/Complexity**) ·
Application Areas: **математика, кодогенерация, text-to-SQL, alignment, reward modeling, long context,
weak-to-strong, agent & tool use, vision-language, factuality** · Datasets · Tools · Blogs.

### 43. awesome-generative-recommendation (WWW-2025 tutorial) — [ОТКРЫЛ]
- **LLM-based**: LLM как последовательный рекомендер (zero-shot → выравнивание LLM под рекомендации →
  цели обучения и инференс); LLM как **диалоговый рекомендер/ассистент**; **LLM как симулятор
  пользователя**.
- **Semantic ID-based**: построение semantic ID (**квантизация, иерархическая кластеризация,
  contextual action tokenization, behavior-aware tokenization, генератор на языковой модели**);
  архитектуры (**dense + generative retrieval**, **унификация retrieval и ranking**); выравнивание с LLM.
- **Diffusion-based**: диффузия как усилитель рекомендаций, диффузия как рекомендер,
  **персонализированная генерация контента**.

### 44. Meta generative-recommenders (HSTU) — [ОТКРЫЛ]
Переформулировка рекомендаций как генеративной задачи, чтобы обойти **упор в масштабирование compute**
классических DLRM. Ключевое: **впервые продемонстрирован scaling law в развёрнутой рекомендательной
системе миллиардного масштаба**; HSTU + **M-FALCON** ускоряют обучение и инференс больших
последовательных моделей в 10x–1000x; на MovieLens-1M HSTU-large даёт +15.5% HR@10 и +18.1% NDCG@10 к
SASRec. В репозитории: CUDA/Triton-ядра, **DLRM-v3**, генерация синтетики фрактальным расширением
(до 3 млрд оценок), бенчмарки обучения и инференса.

### 45. awesome-vector-database — [ОТКРЫЛ]
Services · Libraries & Engines (векторы, тексты) · **Benchmarks & Databases** · Courses · Publications
(Survey, **Quantization**, **Graph-based**, **Tree-based**, Hashing, **Systems**, **Evaluation & Metrics**) ·
Talks. Продукты: Pinecone, Weaviate, **Vespa**, txtai, marqo, Vectara, Epsilla, Algolia, Meilisearch,
NucliaDB, OpenSearch, MyScale, Qdrant Cloud, Zilliz, **MongoDB Atlas Vector Search**, SuperDuperDB,
KDB.AI. Алгоритмы: PQ/**OPQ**/**ScaNN**/inverted multi-index; **HNSW, NSG, EFANNA, FINGER, CAGRA**;
**DiskANN**; LSH и learning-to-hash. Бенчмарки: ANN-Benchmarks, **Billion-scale ANNS**, **BEIR**,
**VectorDBBench**.

### 46. LanceDB — [ОТКРЫЛ] — «векторка нового поколения»
Построена на **колоночном формате Lance**; хранение и запросы к **петабайтам мультимодальных данных**;
векторный поиск + **full-text search** + **SQL** + **гибридный поиск** в одном движке;
**автоматическое версионирование данных с zero-copy** (версии без отдельной инфраструктуры);
**GPU-ускорение построения индекса**; open-source (локально/self-hosted) либо managed cloud;
интеграции LangChain/LlamaIndex/Arrow/Pandas/Polars/DuckDB; SDK Python/TS/Rust.

### 47. Прочие программы, открытые для сверки
- **CMU 11-667 «LLMs: Methods and Applications» (Fall 2025)** — [ОТКРЫЛ syllabus.md, расписание лекций
  на странице отсутствует]: первая половина — основы (архитектуры, обучение, инференс, оценка),
  интерпретация, выравнивание, emergent abilities, применения; вторая — масштабирование предобучения,
  эффективность обучения и деплоя, риски деплоя, фронтир. Курс переехал: с весны 2026 называется
  **«Large Language Model Applications»** (`cmu-llms.org`).
- **MIT 6.5940 EfficientML.ai** — [ТОЛЬКО ОПИСАНИЕ]: 23 лекции + гостевая, 5 лаб. Блоки: (1) лёгкие
  сети — прунинг/спарсити (2 лекции), квантизация (2), дистилляция, NAS; (2) эффективность под
  конкретные сценарии — **LLM, GAN, диффузионные модели**, MCUNet/TinyML; (3) эффективное обучение —
  распределённый параллелизм, автопараллелизация, **сжатие градиентов, on-device training**.
- **ШАД YSDA NLP course** — [ОТКРЫЛ]: 12 недель (эмбеддинги; классификация; языковые модели;
  seq2seq/attention/Transformer; **structured learning**; **EM и модели выравнивания слов**;
  машинный перевод; transfer/multi-task; **domain adaptation**: instance weighting, proxy-labels,
  feature matching, distillation-like; диалоговые системы; **GAN/VAE в NLP**; суммаризация).
  Вывод: программа **не покрывает LLM-фронтир 2025–2026** — как источник дельты бесполезна,
  как источник классики (EM, domain adaptation) частично пересекается с нашими 04-*.
- **DSPy** — [ОТКРЫЛ]: «программирование вместо промптинга»; сигнатуры, модули, **оптимизаторы
  (MIPROv2, GEPA — reflective prompt evolution, BootstrapFinetune)**, DSPy Assertions.
  У нас DSPy уже упомянут в 05-06 — дельты нет.

---

## ДЕЛЬТА: темы, которых нет в нашем манифесте

Проверял двумя способами: по манифесту `.handbook/STRUCTURE.md` и `grep`-ом по готовым `docs/**.md`
(чтобы не выдать за дельту то, что уже написано в главе, но не вынесено в манифест).
**Уже есть и потому исключено из таблицы**: RLVR/GRPO/reward hacking (05-03), speculative decoding
с EAGLE/Medusa и chunked prefill, PD-дизагрегация, MFU/MBU, префиксное кэширование (05-05, 05-11),
constrained decoding + XGrammar/Outlines (05-06), MCP как факт и tau-bench/SWE-bench/pass^k (05-08),
LLM-as-a-judge (05-09), OWASP и prompt injection (05-10), semantic IDs/TIGER (06-11), MoE (05-01),
Mamba/SSM (03-03, 03-04), DSPy (05-06), синтетика для предобучения (05-02), HNSW/IVF-PQ (06-06).

| Тема | Где встретил | Почему важна для middle+ MLE | В какую нашу главу добавить |
|---|---|---|---|
| **Многоуровневый оффлоад KV-кэша (GPU→CPU→SSD→S3) и KV-кэш как отдельный сервис** — LMCache-демон переживает падение движка, KVBM в Dynamo, пул кэша из простаивающих CPU/DRAM/SSD | LMCache, NVIDIA Dynamo, Mooncake **(в проде: Kimi, +75% запросов при SLO)** | Прямой ответ на «как удержать TTFT при длинном контексте и не купить ещё GPU»; сейчас у нас KV-кэш только «в памяти GPU» | `05-llm/05-inference-and-serving.md` (+ ссылка из `07-mlops/09-inference-optimization.md`) |
| **KV-aware routing** — маршрутизация запроса на воркер по перекрытию KV-кэша, а не по round-robin/загрузке | NVIDIA Dynamo **(в проде)** | Классический вопрос «у вас 20 реплик vLLM, как балансировать» — ответ «round-robin» на middle+ уже слабый | `05-llm/05-inference-and-serving.md`, кейс `11-system-design/05-case-rag-assistant.md` |
| **CacheBlend / не-префиксное переиспользование KV** с выборочным пересчётом токенов | LMCache **(в проде, интеграции vLLM/SGLang)** | Префиксный кэш не срабатывает, если общий кусок в середине промпта (типично для RAG: одни и те же чанки в разном порядке) | `05-llm/07-rag.md` (раздел про контекст) + `05-llm/05-inference-and-serving.md` |
| **SLA-driven автоскейлинг инференса и раздельные пулы prefill/decode**: Planner профилирует нагрузку и «правит» размеры пулов; topology-aware планирование в k8s; **миграция запросов в полёте** при падении воркера | NVIDIA Dynamo **(в проде)** | Наш 07-05/07-10 умеет считать RPS и HPA, но не умеет масштабировать *две разные* стадии с разными узкими местами | `07-mlops/05-serving-architectures.md` и `07-mlops/10-cost-and-capacity.md` |
| **Балансировка нагрузки экспертов в MoE (EPLB): избыточные/дублированные эксперты, hierarchical vs global стратегии, разные EP-размеры для prefill и decode** | DeepSeek EPLB, Mooncake EP, SGLang/vLLM expert parallelism **(в проде)** | «MoE дешевле по FLOPs» — это половина ответа; на собесе спрашивают, почему на практике MoE упирается в перекос маршрутизации и память | `05-llm/01-llm-architecture.md` (блок MoE) + `05-llm/05-inference-and-serving.md` |
| **Отказоустойчивый expert parallelism** (детекция сбоя и восстановление при EP на сотнях GPU) | Mooncake EP **(в проде)** | Вопрос уровня middle+/senior про эксплуатацию больших MoE | `05-llm/05-inference-and-serving.md` |
| **Test-time compute как управляемый бюджет: budget forcing, принудительное прерывание/продление размышления, контроль длины CoT** | s1 (budget forcing), Test-Time Scaling survey (**Controllability**), Chip Huyen гл. 2 «Test Time Compute» | Reasoning-модели платятся токенами; «как ограничить стоимость запроса к thinking-модели» — практический вопрос 2026 | `05-llm/06-prompting-and-structured-output.md` (новый раздел про reasoning-режим) + стоимость в `05-llm/11-llm-in-production.md` |
| **Таксономия test-time scaling: parallel / sequential / hybrid / internal; stimulation–verification–search–aggregation** | «What, How, Where, How Well» survey | Даёт язык для ответа «чем self-consistency отличается от MCTS и от reasoning-модели»; у нас есть self-consistency, но нет рамки | `05-llm/06-prompting-and-structured-output.md` |
| **Overthinking / efficient reasoning: length reward в RL, SFT на CoT переменной длины, латентное сжатие шагов, маршрутизация «думать/не думать» по типу задачи** | «Stop Overthinking» survey (TMLR 2025) **(смешанное: маршрутизация — в проде, латентное сжатие — в статьях)** | Прямой продуктовый компромисс «качество↔latency↔цена» для reasoning-моделей | `05-llm/06-prompting-and-structured-output.md`, экономику — в `05-llm/11-llm-in-production.md` |
| **Дистилляция reasoning как рецепт: корпус трейсов из большой reasoning-модели → SFT (32k контекст), затем GRPO; генерация данных через Ray+Distilabel; оценка на AIME/MATH-500/GPQA/LiveCodeBench через lighteval** | open-r1, s1K **(в проде у тех, кто делает свои reasoning-модели)** | У нас дистилляция описана как «в маленькую модель» вообще; специфика reasoning (длина трейсов, качество трейсов, что мерить) отсутствует | `05-llm/04-peft-and-quantization.md` или `05-llm/03-sft-and-alignment.md`; метрики — в `05-llm/09-llm-evaluation.md` |
| **Семейство GRPO-производных: DAPO, Dr.GRPO, GSPO, RLOO, REINFORCE++, PRIME; выбор между outcome- и process-наградой** | awesome-RLVR, **verl (в проде)** | У нас в 05-03 есть GRPO и RLVR, но нет «почему появились правки к GRPO» — типичный follow-up вопрос | `05-llm/03-sft-and-alignment.md` |
| **Инфраструктура RL-обучения: rollout-движок (vLLM/SGLang) отдельно от трейнера, colocate vs выделенные ноды, sequence packing, DeepSpeed Ulysses** | verl, open-r1 **(в проде)** | Вопрос «почему RLHF/RLVR дорого и что там за архитектура» на middle+ | `03-deep-learning/06-scaling-and-efficiency.md` или `05-llm/03-sft-and-alignment.md` |
| **Многошаговый (agentic) RL: turn-level credit assignment, обучение в окружениях, награда за инструментальные вызовы** | Awesome-Agent-RL, verl (multi-turn с tool calling) **(в статьях, отдельные прод-кейсы)** | Отвечает на «как обучать агента, а не отдельный ответ»; помечать как фронтир | `05-llm/08-agents-and-tools.md` (короткий раздел «обучаемые агенты») |
| **Context engineering как дисциплина: динамическая оркестрация контекста, compaction, agent harness/runtime, деградация качества с ростом входа** | Awesome-Context-Engineering, MS AI Agents (урок 12), Awesome-LLM-Long-Context | Термин 2025-го, который уже звучит в вакансиях; у нас есть «работа с контекстом» внутри RAG, но нет самостоятельной рамки и нет тезиса «длиннее ≠ лучше» | `05-llm/06-prompting-and-structured-output.md` + врезка в `05-llm/08-agents-and-tools.md` |
| **Память агента как подсистема: уровни user/session/agent, извлечение фактов, entity linking, multi-signal retrieval (вектор+BM25+сущности), temporal reasoning** | mem0 **(в проде)**, Awesome-Context-Engineering (memory systems) | «Память» в 05-08 упомянута одним словом; на собесе просят спроектировать её | `05-llm/08-agents-and-tools.md` |
| **Бенчмарки памяти и длинного диалога: LoCoMo, LongMemEval, BEAM (1M/10M токенов)** | mem0 | Нужны, чтобы отвечать «как вы измеряете, что память работает» | `05-llm/09-llm-evaluation.md` |
| **A2A: протокол агент↔агент, Agent Cards, длительные задачи без раскрытия внутреннего состояния, JSON-RPC 2.0 + стриминг + push-уведомления; связка «MCP для инструментов, A2A для агентов»** | A2A (a2aproject) **(стандарт, внедрение в начале пути)** | Вопрос «чем MCP отличается от A2A» — типовой на 2026; у нас A2A не встречается ни разу | `05-llm/08-agents-and-tools.md` |
| **MCP глубже факта упоминания: версионирование спеки по датам (ревизия 2025-11-25), клиент/сервер/транспорты, capabilities** | HF MCP Course (unit 1), спецификация MCP | «Интеграция инструментов» стала стандартом, а не самописным function calling; ожидается понимание, что это версионируемый протокол | `05-llm/08-agents-and-tools.md` |
| **Прод-эксплуатация агентов: observability-дашборды, routing logic, backpressure, режимы отказа, контроль стоимости, деплой масштабируемых агентов** | Berkeley Agentic AI F25 (лекция Yangqing Jia), MS AI Agents уроки 10/16/18 | Наша 05-08 покрывает «надёжность и обработку ошибок», но не операционку | `05-llm/08-agents-and-tools.md` + `09-monitoring/05-observability-stack.md` |
| **Computer-Use Agents (CUA)** | MS AI Agents (урок 15), Berkeley F25 (веб-автоматизация) **(в проде ограниченно)** | Растущий класс задач; достаточно обзорного абзаца с честной оценкой надёжности | `05-llm/08-agents-and-tools.md` |
| **OpenTelemetry GenAI semantic conventions** — стандартизованные спаны/метрики/события для LLM-клиентов, **для MCP** и для провайдеров | open-telemetry/semantic-conventions-genai **(стандарт, внедряется)** | Наш 09-05 учит Prometheus/Grafana/трейсинг вообще; отраслевой стандарт именно для LLM-телеметрии не назван | `09-monitoring/05-observability-stack.md` |
| **LLM-гейтвей как отдельный компонент архитектуры: virtual keys, бюджеты и spend tracking, фолбэки между провайдерами, гейтвейные guardrails, единый формат API** | LiteLLM **(в проде)**, Chip Huyen гл. 10 («model router and gateway») | У нас есть «роутинг моделей» в 05-11, но нет гейтвея как узла с квотами/биллингом/фолбэками — а именно его рисуют в system design | `05-llm/11-llm-in-production.md` + схема в `11-system-design/05-case-rag-assistant.md` |
| **Типология guardrails по точкам применения: input / dialog / retrieval / execution (tools) / output rails** | NeMo Guardrails **(в проде)**, Guardrails AI (Guard + валидаторы + отдельный сервер) | Наша 05-10 говорит «фильтры входа/выхода»; retrieval- и execution-rails (проверка чанков и вызовов инструментов) — отдельные и важные точки | `05-llm/10-llm-safety-and-guardrails.md` |
| **OWASP Top 10 for Agentic Applications (2026) как отдельный список поверх OWASP LLM Top 10 (2025)**; из LLM-списка 2025 у нас, вероятно, не раскрыты **LLM06 Excessive Agency** (избыточная функциональность / права / автономия), **LLM07 System Prompt Leakage**, **LLM08 Vector and Embedding Weaknesses** | OWASP GenAI Security Project — [ТОЛЬКО ОПИСАНИЕ] (genai.owasp.org отдаёт 403) | Прямо ложится в вопрос «как вы ограничиваете агента»; «excessive agency» — готовая рамка ответа | `05-llm/10-llm-safety-and-guardrails.md` |
| **Оценка агентов на надёжность: Pass^k (успех во всех k прогонах) vs pass@k; автоклассификация ошибок по «виновнику»; симулированный пользователь как часть харнесса** | tau-bench / τ³-bench | Ключевое отличие агентной оценки: важна воспроизводимость, а не лучший из k. Наша 05-08 упоминает tau-bench, но не различие метрик | `05-llm/09-llm-evaluation.md` (+ ссылка из 05-08) |
| **Sandbox-бенчмарки сквозных задач (terminal-bench): инструкция + тест-скрипт + oracle-решение как единица оценки** | terminal-bench | Даёт шаблон «как построить свой агентный бенчмарк на внутренних задачах» — частый вопрос про оценку в компании | `05-llm/09-llm-evaluation.md` |
| **BFCL v3/v4: multi-turn/multi-step function calling, web search и memory как оцениваемые способности, relevance-проверка (нужно ли вообще звать функцию), чувствительность к формату** | Berkeley Function Calling Leaderboard | Function calling у нас есть, но нет «как измерить его качество», включая ложные вызовы | `05-llm/08-agents-and-tools.md` |
| **Inspect (UK AISI) как стандартный харнесс safety/capability-оценок, 200+ готовых оценок, model-graded evals** | inspect_ai | Вопрос «чем гоняете оценки» на middle+ ожидает названия инструмента, а не «скриптом» | `05-llm/09-llm-evaluation.md` |
| **Dataset engineering как отдельная дисциплина: curation (quality/coverage/quantity), acquisition & annotation, дедупликация, фильтрация, форматирование; синтетика для post-training (instruction generation высокой сложности, rejection sampling, weak-to-strong)** | Chip Huyen гл. 8, mlabonne (Post-training datasets), Awesome-LLM-Synthetic-Data | У нас синтетика есть только в контексте предобучения (05-02); отдельного «как собрать датасет для дообучения» нет | `05-llm/03-sft-and-alignment.md` (раздел «данные») или `02-classic-ml/14-feature-engineering.md` — лучше первое |
| **Обратная связь пользователя как проектируемая система: извлечение неявной обратной связи из диалога, дизайн фидбэка, его ограничения и смещения** | Chip Huyen гл. 10 | Замыкает петлю «прод → данные → дообучение» для LLM-продукта; у нас петля обратной связи описана только для рекомендаций (06-12) | `05-llm/11-llm-in-production.md` |
| **Планирование ИИ-продукта: use case evaluation, setting expectations, milestone planning, maintenance; build vs buy** | Chip Huyen гл. 1 и 4 | Секция про «продуктовое мышление» на собесе middle+; у нас частично в 11-01, но без явной рамки build-vs-buy для моделей | `00-start/03-interview-map.md` / `11-system-design/01-framework.md` |
| **Компрессия контекста и промпта (token/prompt compression) как отдельный приём экономии** | Awesome-LLM-Inference (Prompt/Context Compression), Awesome-LLM-Long-Context | Дешёвый способ снизить стоимость длинных промптов до перехода на дообучение | `05-llm/11-llm-in-production.md` или `05-llm/07-rag.md` |
| **Many-shot / long in-context learning как альтернатива дообучению при больших окнах** | Awesome-LLM-Long-Context (Long ICL) **(в статьях, но уже применимо)** | Отвечает на «у нас 1M контекст — зачем вообще fine-tuning/RAG» | `05-llm/07-rag.md` (раздел «когда RAG не нужен») |
| **Privacy-preserving inference (FHE / MPC / PPML)** | stas00 ml-engineering (глоссарий и концепции инференса) **(в статьях)** | Возникает в финтехе/медицине при вопросе «а можно ли на внешнем API»; достаточно абзаца с честным «дорого» | `05-llm/10-llm-safety-and-guardrails.md` |
| **Экономика железа в цифрах: формулы `B*18*1.25/GPU_GB` (обучение) и `B*2*1.25/GPU_GB` (инференс), пересчёт стоимости через TFLOPS с поправкой MFU≈50%, cloud vs HPC vs покупка (окупаемость 3+ года), «вам продают 80% хранилища», параллельные ФС вместо NFS** | stas00 ml-engineering (AI Battlefield) | Наша 07-10 говорит «GPU-экономика», но без готовых формул и без сравнения владения; это то, что просят посчитать вслух | `07-mlops/10-cost-and-capacity.md` |
| **Когда выгодно обновлять GPU / как выбирать облачного провайдера (чек-лист)** | stas00 ml-engineering (Insights) | Вопрос капасити-планирования на middle+ в инфра-командах | `07-mlops/10-cost-and-capacity.md` |
| **Векторное хранилище нового поколения: колоночный формат поверх объектного хранилища, версионирование данных zero-copy, единый движок «вектор + full-text + SQL», GPU-построение индекса, мультимодальные данные рядом с векторами** | LanceDB / формат Lance **(в проде)** | Наш 06-06 — про HNSW/IVF-PQ и FAISS; вопрос «как вы версионируете и переливаете индекс» решается на уровне формата хранения | `10-recsys/06-two-tower-and-ann.md` + упоминание в `05-llm/07-rag.md` |
| **VectorDBBench и методика сравнения векторных БД; фильтрованный ANN-поиск как отдельная задача** | awesome-vector-database (Benchmarks, Evaluation & Metrics) | «Как выбрать векторную БД» — частый вопрос; ответ должен быть «по бенчмарку с вашим recall/latency/фильтрами» | `10-recsys/06-two-tower-and-ann.md` |
| **HSTU / генеративные рекомендации Meta: scaling law в развёрнутой системе миллиардного масштаба, M-FALCON, DLRM-v3, ускорение 10x–1000x** | facebookresearch/generative-recommenders **(в проде, Meta)** | Наш 06-11 разбирает TIGER/P5 (в основном «в статьях»); HSTU — главный аргумент, что генеративный подход уже работает в проде и что у рекомендаций тоже есть законы масштабирования | `10-recsys/11-llm-recsys.md` и/или `10-recsys/09-sequential-recsys.md` |
| **Унификация retrieval и ranking в одной генеративной модели; behavior-aware и contextual action tokenization при построении semantic ID** | awesome-generative-recommendation (WWW-2025 tutorial), OneRec — [ТОЛЬКО ОПИСАНИЕ] | Прямо ломает нашу «многостадийную архитектуру» из 06-01 — сильный follow-up вопрос на собесе | `10-recsys/11-llm-recsys.md` (+ абзац-контрапункт в `10-recsys/01-recsys-foundations.md`) |
| **LLM как симулятор пользователя (для оценки рекомендаций и агентов)** | awesome-generative-recommendation, tau-bench (симулированный пользователь) **(в статьях + в бенчмарках)** | Способ получить офлайн-оценку там, где нет онлайна; спрашивают в связке «как тестировали до A/B» | `10-recsys/02-metrics-offline.md` или `05-llm/09-llm-evaluation.md` |
| **Диффузионные модели в рекомендациях (diffusion-enhanced rec, диффузия как рекомендер, персонализированная генерация контента)** | awesome-generative-recommendation **(в статьях)** | Обзорный абзац с честной пометкой «пока не прод» — защищает от «а вы слышали про...» | `10-recsys/11-llm-recsys.md` |
| **Triton/CUDA-ядра как инженерный навык (почему написали своё ядро и что это дало)** | CS336 лекция 6 «Kernels, Triton» — [ТОЛЬКО ОПИСАНИЕ], HSTU (CUDA/Triton-ядра), MIT 6.5940 | Для middle+ в LLM/recsys-инфре ожидается понимание, что FlashAttention — это про память, а не про формулу | `03-deep-learning/06-scaling-and-efficiency.md` (абзац) |
| **Оффлайн-инференс (batch) как отдельный режим со своими метриками против онлайн** | stas00 ml-engineering (Inference: online vs offline), vLLM | У нас батч-инференс есть в 07-05, но не в LLM-контексте (дешёвый массовый прогон, другие SLA) | `05-llm/11-llm-in-production.md` |
| **Оценка на «живых» и версионируемых данных как защита от протечки бенчмарков (BFCL Live, версии датасета terminal-bench)** | BFCL v2, terminal-bench | Наш 05-09 говорит про протечки бенчмарков; практический ответ «берите живые/версионируемые наборы» отсутствует | `05-llm/09-llm-evaluation.md` |
| **LLM-трейсы как продуктовые данные: приём и анализ пайплайном (dlt → DuckDB → дашборд)** | LLM Zoomcamp 2026 (workshop) | Соединяет 08-* (инженерия данных) с LLM-продом; вопрос «где лежат логи диалогов и как вы их анализируете» | `09-monitoring/05-observability-stack.md` |

---

## Чего найти не удалось

1. **Первичные страницы курсов** — все главные (`stanford-cs336.github.io/spring2025`,
   `llmagents-learning.org/sp25`, `agenticai-learning.org/f25`, `hanlab.mit.edu`, `huggingface.co/learn`,
   `classcentral.com`) отдают 403 и через WebFetch, и через `curl` (прокси: `CONNECT tunnel failed 403`).
   Списки лекций CS336, Berkeley Agentic AI и MIT 6.5940 приведены **со слов поисковой выдачи**
   и помечены [ТОЛЬКО ОПИСАНИЕ] — их стоит перепроверить перед цитированием.
2. **Полный текст спецификации MCP** (примитивы tools/resources/prompts, транспорты stdio/Streamable
   HTTP, sampling/elicitation, модель безопасности: confused deputy, tool poisoning). Подтверждена лишь
   ревизия схемы **2025-11-25**. Следствие: специфические **MCP-риски безопасности** в дельту не внесены —
   нет открытого первоисточника, а выдумывать нельзя.
3. **Конкретные имена атрибутов OpenTelemetry GenAI** (`gen_ai.*`): подтверждён факт выделения в
   отдельный репозиторий и область охвата (GenAI-клиенты, MCP, провайдеры), содержимое `docs/` не
   перебрано (листинг каталогов через `api.github.com` — 403).
4. **Официальный текст OWASP Top 10 for LLM Apps 2025 и Agentic Apps 2026** — `genai.owasp.org` 403,
   README проекта на GitHub списка не содержит. Коды/названия взяты из поисковых сниппетов.
5. **Таксономия обзора по MoE** (`A-Survey-on-Mixture-of-Experts`) — в README только картинка
   `moe_taxonomy.jpg`, текстовой структуры нет; arXiv недоступен. Дельта по MoE опирается на EPLB,
   Mooncake, SGLang/vLLM — то есть на код, а не на обзор.
6. **arXiv** (`arxiv.org/abs/*`) недоступен полностью — все ссылки на статьи в отчёте даны только
   как «упомянуто в открытом источнике», ни одна статья не прочитана.
7. **Расписание лекций CMU 11-667 Fall 2025** — `syllabus.md` открыт, но раздел с расписанием пуст;
   `2025.cmu-llms.org` не проверял (лимит поиска).
8. **Российские программы 2025–2026 по фронтир-темам** отдельно прочесать не удалось: лимит WebSearch
   закончился, а прямые домены (Karpov, Yandex Practicum, ODS) недоступны через прокси. Единственный
   открытый российский источник — YSDA NLP course, и он по составу **не содержит фронтир-тем 2025–2026**.
   Смежные прочёсы у нас уже есть: `.handbook/sweep/ru-industry.md`, `.handbook/sweep/ru-universities.md`.
9. **Явно не подтверждено практикой (оставляю как «в статьях», в дельту не тащу отдельными строками)**:
   агентный RL в продовых рекомендательных/поисковых системах; латентное сжатие цепочек рассуждений;
   диффузия как основной рекомендер; non-transformer архитектуры в массовом проде (в awesome-листах
   раздел есть, продовых подтверждений в открытых источниках не нашёл).
