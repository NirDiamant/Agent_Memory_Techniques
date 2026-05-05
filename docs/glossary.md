# Glossary of Agent Memory Terms

A reference guide to the key concepts, data structures, and techniques used in this repository. Think of it as your pocket dictionary for agent memory. Terms are listed alphabetically.

---

<a id="archival-memory"></a>
### Archival Memory

> **What is Archival Memory?**

A long-term storage layer for memories the agent doesn't need right now but may look up later. In Letta/MemGPT, archival memory is a paginated vector store. The agent searches it with explicit tool calls instead of getting results injected automatically. Archival memory can grow without limit because it lives outside the context window.

**Related techniques:** [06 - Vector Store Memory](../all_techniques/06_vector_store_memory/), [26 - Letta/MemGPT Patterns](../all_techniques/26_letta_memgpt_patterns/)

---

<a id="context-window"></a>
### Context Window

> **What is Context Window?**

The fixed-size input that a large language model (LLM) can see at once, measured in tokens. A token is roughly 3/4 of an English word. Everything the model reads when it generates a response must fit inside this window: system prompt, retrieved memories, conversation history, and the current user message. Window sizes vary by model (e.g., 4K, 32K, 128K, 200K tokens). Even the largest windows have hard limits. Managing what fills this window is the central challenge of agent memory.

**Related techniques:** [05 - Token Buffer Memory](../all_techniques/05_token_buffer_memory/), [12 - Working Memory & Context Window](../all_techniques/12_working_memory_context_window/)

---

<a id="core-memory"></a>
### Core Memory

> **What is Core Memory?**

In Letta/MemGPT, core memory is a small, always-visible block of text the agent can read and edit itself. It typically holds critical persistent information: the user's name, key preferences, the agent's persona, and essential facts. Because core memory is always in the prompt, it's the fastest to access but the most expensive in token cost. The agent modifies it through explicit tool calls (e.g., `core_memory_replace`).

**Related techniques:** 26 - Letta/MemGPT Patterns

---

<a id="cross-session-persistence"></a>
### Cross-Session Persistence

> **What is Cross-Session Persistence?**

The ability of an agent's memory to survive across independent sessions. When you return hours, days, or weeks later, the agent can recall prior context. This requires saving memory state to durable storage (database, file system, cloud) and reloading it when a new session begins. Cross-session persistence is what separates a stateless chatbot from a personal assistant.

**Related techniques:** [21 - Cross-Session Memory](../all_techniques/21_cross_session_memory/)

---

<a id="embedding"></a>
### Embedding

> **What is Embedding?**

A dense numerical vector (list of numbers) that represents the meaning of a piece of text. An embedding model (e.g., OpenAI's `text-embedding-3-small`, Cohere's `embed-v3`, open-source models like `all-MiniLM-L6-v2`) produces these vectors. Texts with similar meanings produce vectors that are close together in the number space. Agent memory systems use embeddings to store memories in vector databases and retrieve them via similarity search.

**Related techniques:** 06 - Vector Store Memory, [20 - Memory Retrieval Patterns](../all_techniques/20_memory_retrieval_patterns/)

---

<a id="entity-extraction"></a>
### Entity Extraction

> **What is Entity Extraction?**

The process of identifying structured information about named entities (people, organizations, locations, projects, dates, etc.) from unstructured conversation text. You can perform entity extraction with traditional NLP tools (like spaCy NER), LLM-based extraction (prompting the model to find entities), or hybrid approaches. Extracted entities populate entity memory stores and knowledge graphs.

**Related techniques:** [07 - Entity Memory](../all_techniques/07_entity_memory/), [08 - Knowledge Graph Memory](../all_techniques/08_knowledge_graph_memory/)

---

<a id="episodic-memory"></a>
### Episodic Memory

> **What is Episodic Memory?**

A memory store that records specific interaction episodes (complete conversations or significant events) with rich contextual metadata: timestamps, participants, topics, emotional tone, and outcomes. Episodic memory answers "what happened" questions ("What did we discuss about the project last Tuesday?"). In cognitive science, episodic memory is distinct from semantic memory. The same distinction is useful in agent architectures.

**Related techniques:** [09 - Episodic Memory](../all_techniques/09_episodic_memory/)

---

<a id="forgetting-curve"></a>
### Forgetting Curve

> **What is Forgetting Curve?**

A model of how memory retention decreases over time without reinforcement. Hermann Ebbinghaus first described it in 1885 for human memory. In agent systems, we adapt the concept as a mathematical decay function applied to memory importance scores. Memories that aren't accessed or reinforced gradually lose their scores and may eventually be pruned. A common implementation uses exponential decay: `score(t) = score(0) * e^(-lambda * t)`.

**Related techniques:** [19 - Forgetting & Decay](../all_techniques/19_forgetting_and_decay/)

---

<a id="inner-monologue"></a>
### Inner Monologue

> **What is Inner Monologue?**

A mechanism introduced by MemGPT (now Letta) where the agent produces private reasoning text. This text is visible to the agent itself but hidden from the user. The inner monologue lets the agent think through memory management decisions ("I should save the user's preference for dark mode to core memory") before taking memory actions. This is distinct from the outer monologue (the response the user sees). Inner monologue uses context window tokens but enables more deliberate memory operations.

**Related techniques:** 26 - Letta/MemGPT Patterns

---

<a id="knowledge-graph"></a>
### Knowledge Graph

> **What is Knowledge Graph?**

A graph data structure where nodes represent entities (people, concepts, objects) and edges represent relationships between them (e.g., "manages," "works_on," "is_located_in"). In agent memory, knowledge graphs enable structured reasoning about relationships. They support multi-hop queries ("Who manages the person who works on Project X?"). Knowledge graphs complement vector stores by capturing structure that flat text embeddings lose.

**Related techniques:** 08 - Knowledge Graph Memory, [24 - Graph Memory with Graphiti](../all_techniques/24_graph_memory_graphiti/)

---

<a id="locomo-long-conversation-memory"></a>
### LoCoMo (Long Conversation Memory)

> **What is LoCoMo (Long Conversation Memory)?**

A benchmark dataset and evaluation framework for testing how well memory systems handle long conversational histories. LoCoMo provides multi-session conversations with ground-truth annotations. It enables standardized evaluation of retrieval accuracy, temporal reasoning, and entity tracking across extended interactions. It tests five categories: single-hop, multi-hop, temporal, open-domain, and adversarial questions.

**Related techniques:** [29 - Memory Benchmarks (LoCoMo)](../all_techniques/29_memory_benchmarks_LoCoMo/)

---

<a id="longmemeval"></a>
### LongMemEval

> **What is LongMemEval?**

An evaluation benchmark for testing long-term memory in conversational AI systems. LongMemEval focuses on multi-session interactions over extended periods. It measures an agent's ability to recall facts, maintain consistency, handle updates to stored information, and reason about time across past interactions. It complements LoCoMo with different task formulations and evaluation criteria.

**Related techniques:** 29 - Memory Benchmarks (LoCoMo)

---

<a id="memory-benchmark"></a>
### Memory Benchmark

> **What is Memory Benchmark?**

A standardized test suite for evaluating the quality of an agent's memory system. Memory benchmarks measure dimensions like retrieval precision and recall, temporal accuracy, entity consistency, contradiction detection, and staleness handling. Benchmarks let you objectively compare different memory architectures and configurations. Key benchmarks in the field include LoCoMo and LongMemEval.

**Related techniques:** [28 - Memory Evaluation](../all_techniques/28_memory_evaluation/), 29 - Memory Benchmarks (LoCoMo)

---

<a id="memory-as-a-tool"></a>
### Memory-as-a-Tool

> **What is Memory-as-a-Tool?**

A design pattern where the agent interacts with its memory through explicit tool calls (functions) rather than getting memories injected automatically. The agent decides when to save, search, update, or delete memories by invoking tools like `save_memory(content)`, `search_memory(query)`, or `forget_memory(id)`. This gives the agent fine-grained control over its memory operations. The trade-off: the agent must learn when to use each tool.

**Related techniques:** [23 - Memory with Tools](../all_techniques/23_memory_with_tools/)

---

<a id="memory-compaction"></a>
### Memory Compaction

> **What is Memory Compaction?**

The process of reducing the storage size and token cost of accumulated memories without losing essential information. Compaction techniques include progressive summarization (replacing detailed episodes with shorter summaries), entity extraction (distilling facts from narratives), deduplication (merging overlapping memories), and compression (encoding memories more efficiently). Compaction runs periodically as a background maintenance process.

**Related techniques:** [15 - Memory Compaction](../all_techniques/15_memory_compaction/)

---

<a id="memory-consolidation"></a>
### Memory Consolidation

> **What is Memory Consolidation?**

Inspired by the neuroscience concept of sleep-based memory consolidation. This is the process of strengthening, reorganizing, and integrating newly acquired memories into long-term storage. In agent systems, consolidation involves merging related episodic memories, extracting generalized facts from repeated patterns, resolving contradictions, and updating entity records. Consolidation improves memory quality over time.

**Related techniques:** [14 - Memory Consolidation](../all_techniques/14_memory_consolidation/)

---

<a id="memory-decay"></a>
### Memory Decay

> **What is Memory Decay?**

The gradual reduction of a memory's importance or accessibility over time. You implement memory decay as a scoring function that reduces a memory's retrieval priority based on time since last access, time since creation, or both. Decay prevents stale or irrelevant memories from dominating retrieval results. It also naturally limits memory store size. Decay functions are typically exponential or logarithmic.

**Related techniques:** 19 - Forgetting & Decay

---

<a id="memory-pressure"></a>
### Memory Pressure

> **What is Memory Pressure?**

A condition that arises when the total size of memories the agent wants in its context exceeds the available token budget. Memory pressure forces the working memory manager to triage: which memories to keep, summarize, demote, or evict. In Letta/MemGPT, memory pressure triggers automatic compaction and archival operations. High memory pressure means the agent is accumulating information faster than it can consolidate.

**Related techniques:** 12 - Working Memory & Context Window, 26 - Letta/MemGPT Patterns

---

<a id="memory-routing"></a>
### Memory Routing

> **What is Memory Routing?**

The process of directing memory reads and writes to the appropriate store based on content type and intent. A memory router classifies incoming information. "This is a fact about a person" goes to semantic memory. "This is a procedure for exporting data" goes to procedural memory. "This is an account of a past conversation" goes to episodic memory. Routing can be rule-based, LLM-based, or hybrid.

**Related techniques:** [17 - Memory Routing](../all_techniques/17_memory_routing/)

---

<a id="memory-sharding"></a>
### Memory Sharding

> **What is Memory Sharding?**

The practice of splitting an agent's memory store across multiple shards (segments or partitions) to improve retrieval performance, enforce access control, or support multi-tenancy. Common sharding strategies include per-user sharding (each user's memories in a separate partition), per-topic sharding (memories segmented by domain), and temporal sharding (memories segmented by time period). Sharding becomes important at scale.

**Related techniques:** [30 - Production Memory Patterns](../all_techniques/30_production_memory_patterns/)

---

<a id="procedural-memory"></a>
### Procedural Memory

> **What is Procedural Memory?**

A memory store that captures learned procedures, workflows, tool usage patterns, and "how-to" knowledge the agent acquires through experience. Unlike semantic memory (facts) or episodic memory (events), procedural memory stores action sequences and decision rules. Examples: "When the user asks for a CSV export, use the export_csv tool with format='csv' and delimiter=','." Or: "To deploy to staging, first run tests, then build, then push to the staging branch."

**Related techniques:** [11 - Procedural Memory](../all_techniques/11_procedural_memory/)

---

<a id="recall-memory"></a>
### Recall Memory

> **What is Recall Memory?**

In Letta/MemGPT, recall memory is the searchable log of all past conversation messages. Unlike core memory (always visible) or archival memory (extracted knowledge), recall memory stores the raw conversation history. It supports both recency-based and keyword-based retrieval. The agent searches recall memory with explicit tool calls to find specific past conversations.

**Related techniques:** 26 - Letta/MemGPT Patterns

---

<a id="retrieval"></a>
### Retrieval

> **What is Retrieval?**

The process of finding and returning relevant memories from a store in response to a query. Retrieval strategies include: semantic search (cosine similarity over embeddings), keyword search (BM25, TF-IDF), metadata filtering (by timestamp, entity, topic), graph traversal (following relationship edges), hybrid scoring (combining multiple signals), and re-ranking (using a cross-encoder model or LLM to reorder initial results). Retrieval quality directly determines how useful stored memories are.

**Related techniques:** 20 - Memory Retrieval Patterns

---

<a id="semantic-memory"></a>
### Semantic Memory

> **What is Semantic Memory?**

A memory store that holds generalized facts, domain knowledge, and entity information distilled from specific interactions. While episodic memory records "what happened in conversation #42," semantic memory extracts and stores the durable fact: "The user prefers Python over JavaScript." Semantic memory is updated through extraction and consolidation. It forms the agent's general knowledge base.

**Related techniques:** [10 - Semantic Memory](../all_techniques/10_semantic_memory/)

---

<a id="temporal-memory"></a>
### Temporal Memory

> **What is Temporal Memory?**

A memory capability that attaches time information to stored memories and uses it during retrieval. Temporal memory enables time-aware queries ("What did we discuss last week?"), recency-weighted retrieval (recent memories rank higher), time-range filtering (only search a specific period), and temporal reasoning ("Has the user's preference changed over time?"). Temporal metadata includes creation timestamps, last-access timestamps, and expiration dates.

**Related techniques:** [18 - Temporal Memory](../all_techniques/18_temporal_memory/)

---

<a id="token-budget"></a>
### Token Budget

> **What is Token Budget?**

The maximum number of tokens allocated for a specific section of the agent's context window. In a well-designed memory system, the total context window is divided into budgets: system prompt (fixed), core memory (fixed), retrieved memories (variable), conversation buffer (variable), and the current turn (variable). Token budgets ensure no single section monopolizes the context window. They force the system to prioritize the most relevant content.

**Related techniques:** 05 - Token Buffer Memory, 12 - Working Memory & Context Window

---

<a id="vector-store"></a>
### Vector Store

> **What is Vector Store?**

A database optimized for storing, indexing, and querying high-dimensional vectors (embeddings). Vector stores support similarity search: given a query vector, find the k nearest neighbors by cosine similarity, dot product, or Euclidean distance. Popular vector stores for agent memory include ChromaDB (local, lightweight), Pinecone (managed, scalable), Qdrant (open-source, feature-rich), Weaviate (open-source, hybrid search), and FAISS (in-memory, Facebook research).

**Related techniques:** 06 - Vector Store Memory

---

<a id="working-memory"></a>
### Working Memory

> **What is Working Memory?**

The agent's active, limited-capacity "attention space." It's the subset of all stored memories currently loaded into the context window. Working memory is analogous to human working memory: it holds the information the agent is actively using to reason about the current task. A working memory manager decides what to load, what to evict, and how to allocate the token budget across competing demands. Effective working memory management is what makes agents feel intelligent and responsive.

**Related techniques:** 12 - Working Memory & Context Window

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=docs--glossary)
