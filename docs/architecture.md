# Memory System Architecture Patterns

The way you organize your agent's memory affects what it remembers, how fast it finds relevant context, and how well it scales. This document describes five architecture patterns. You'll see them again and again across production agent systems. They range from a single store (the simplest) to a full cognitive architecture (the most complex, modeled on human memory research).

Each pattern includes an ASCII diagram, component descriptions, data flow, and guidance on when to choose it.

---

## 1. Single-Store Pattern

Think of a single box where you throw all your notes. Grocery lists, meeting minutes, phone numbers: everything goes in the same box. When you need something, you dig through the whole box. With 20 notes, this works fine. With 2,000, finding the right one gets slow and messy.

**This is the simplest memory architecture. One vector database holds everything.** A vector database stores text as lists of numbers (called "embeddings") and can quickly find entries with similar meaning.

You embed all memories (conversation turns, extracted facts, user preferences, episode summaries) into a single collection. "Embedding" means converting text into a number array that captures its meaning. At retrieval time, the agent runs a semantic search (finding entries by meaning, not exact keywords) over the entire store. It then injects the top-k results (the k most relevant matches) into the prompt.

```
                         ┌─────────────────────┐
                         │      LLM Agent       │
                         │                      │
                         │  system prompt       │
                         │  + retrieved context  │
                         │  + user message       │
                         └──────────┬────────────┘
                                    │
                           write ▼  │ ▲ search (top-k)
                                    │ │
                         ┌──────────▼─┴──────────┐
                         │                        │
                         │    Vector Store         │
                         │    (single collection)  │
                         │                        │
                         │  ┌──────────────────┐  │
                         │  │ memory_1  [0.2,…] │  │
                         │  │ memory_2  [0.8,…] │  │
                         │  │ memory_3  [0.1,…] │  │
                         │  │ ...               │  │
                         │  └──────────────────┘  │
                         │                        │
                         └────────────────────────┘
```

**Components:**
- A single vector collection (e.g., ChromaDB, Pinecone, Qdrant, Weaviate)
- An embedding model that converts text into number arrays (vectors)
- A retrieval query that searches by cosine similarity (a formula that scores how close two vectors are, from 0.0 to 1.0)

**Data flow:**
1. After each turn, the agent embeds its response (or a turn summary) and stores it.
2. Before each new turn, the agent queries the store with the current user message.
3. The top-k results go into the system prompt as "relevant memories."

**Strengths:**
- Quick to set up (often under 50 lines of code)
- No routing logic needed
- Works surprisingly well for single-user chatbots with moderate history

**Weaknesses:**
- No distinction between memory types (facts vs. episodes vs. procedures)
- Retrieval quality drops as the store grows. Unrelated memories pollute results.
- No temporal ordering or decay. A fact from 6 months ago carries the same weight as one from 5 minutes ago.
- No compaction (shrinking old data) or consolidation (merging related memories). The store grows without bound.

**Best for:** Prototypes, chatbots, single-session demos, learning projects.

**Real-world examples:** LangChain's `VectorStoreRetrieverMemory`, basic RAG-over-chat-history setups.

---

## 2. Dual-Store Pattern

Think of your desk and a filing cabinet. Your desk holds what you're working on right now. The filing cabinet stores older documents you might need later. Every evening, you move finished papers from the desk into the cabinet. When you need an old document, you search the cabinet and pull it back to your desk.

**A short-term buffer for recent context plus a long-term persistent store for accumulated knowledge.**

This pattern separates "what happened recently" (the conversation buffer) from "what the agent knows" (the long-term store). The buffer holds the last N messages or a running summary. The long-term store holds extracted facts, entities, and episode summaries. A flush mechanism (a process that periodically moves distilled information from the buffer to long-term storage) connects the two.

```
     ┌────────────────────────────────────────────────┐
     │                   LLM Agent                     │
     │                                                │
     │  system prompt + core memory                   │
     │  + short-term buffer (recent messages)          │
     │  + retrieved long-term context                  │
     │  + user message                                │
     └───────┬──────────────────────────┬─────────────┘
             │                          │
             ▼                          ▼
     ┌───────────────┐         ┌───────────────────┐
     │  Short-Term    │  flush  │   Long-Term       │
     │  Buffer        │───────►│   Store            │
     │                │         │                   │
     │  Last k msgs   │         │  Vector DB or     │
     │  or running    │         │  Document Store    │
     │  summary       │         │                   │
     │                │         │  - Extracted facts │
     │  (in-memory)   │         │  - Entity records  │
     │                │         │  - Episode sums    │
     └───────────────┘         └───────────────────┘
```

**Components:**
- **Short-term buffer:** An in-memory list of recent messages (sliding window or summary buffer). This gives the agent immediate conversational context.
- **Long-term store:** A persistent vector database or document store. It accumulates extracted knowledge over time.
- **Flush mechanism:** A process that runs periodically (every N turns, at session end, or when memory pressure is high). It extracts durable memories from the buffer and writes them to long-term storage.

**Data flow:**
1. Each new user message goes into the short-term buffer.
2. The agent always sees the full buffer in its context window.
3. The current message also triggers a semantic search against the long-term store. Top-k results get injected.
4. Periodically, the flush mechanism processes the buffer. It extracts entities, summarizes episodes, or identifies facts, then writes results to the long-term store.
5. After flushing, older buffer entries are trimmed or summarized.

**Strengths:**
- Clear separation between recent context and accumulated knowledge
- The short-term buffer guarantees the agent always has immediate context
- The long-term store grows independently and supports semantic search
- The flush mechanism acts as a natural compaction step

**Weaknesses:**
- You must design the flush mechanism: when to flush, what to extract, how to deduplicate
- Two stores to manage and back up
- No explicit routing. The agent always searches long-term on every turn.

**Best for:** Personal assistants, customer support bots, any system that needs both immediate context and persistent memory across sessions.

**Real-world examples:** Mem0's architecture (auto-extraction to persistent store), LangChain's `ConversationSummaryBufferMemory` + `VectorStoreRetrieverMemory` combination.

---

## 3. Tiered Pattern

Think of how you organize a kitchen. Spices you use daily sit on the counter (hot tier). Less common ones live in a cabinet (warm tier). That specialty spice you bought once goes in the back of the pantry (cold tier). When you start using a spice often, you move it closer. When you stop using one, it drifts to the back.

**Hot/warm/cold memory layers with promotion and demotion policies, inspired by how CPUs organize their fast-access caches.**

CPUs use a similar idea: a small, fast layer (L1 cache) holds the most-used data, a bigger but slower layer (L2) holds the rest, and main memory holds everything. In this pattern, memories live in one of several tiers based on how often they're accessed, how recent they are, and how important they are. The hottest tier lives in-memory for instant access. Warm memories sit in a fast database. Cold memories are archived in cheap storage and only retrieved on explicit demand.

```
                          ┌──────────────────┐
                          │    LLM Agent      │
                          └────────┬─────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
           ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
           │   HOT TIER    │ │  WARM TIER    │ │  COLD TIER    │
           │   (L1 Cache)  │ │  (L2 Cache)   │ │  (Archive)    │
           │               │ │               │ │               │
           │ In-memory     │ │ Fast DB       │ │ Blob/object   │
           │ dict or Redis │ │ (Qdrant,      │ │ storage (S3,  │
           │               │ │  ChromaDB)    │ │ GCS, SQLite)  │
           │ - Current     │ │               │ │               │
           │   session     │ │ - Recent      │ │ - Historical  │
           │ - Pinned      │ │   sessions    │ │   sessions    │
           │   facts       │ │ - Active      │ │ - Archived    │
           │ - Working     │ │   entities    │ │   entities    │
           │   context     │ │ - Warm        │ │ - Compressed  │
           │               │ │   summaries   │ │   summaries   │
           │ Access: <1ms  │ │ Access: ~10ms │ │ Access: ~100ms│
           └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
                  │                │                │
                  │   promote ▲   │   promote ▲   │
                  │   demote  ▼   │   demote  ▼   │
                  └───────────────┘───────────────┘

     ┌─────────────────────────────────────────────────────┐
     │               Tier Manager / Policy Engine           │
     │                                                     │
     │  Promotion rules:                                   │
     │    - Access count > threshold  → promote to hotter  │
     │    - Explicit pin by agent     → promote to hot     │
     │    - Referenced in last N turns → stay hot           │
     │                                                     │
     │  Demotion rules:                                    │
     │    - No access for M turns     → demote to colder   │
     │    - Low relevance score       → demote or archive  │
     │    - Session ended             → demote to warm     │
     │    - Decay score below cutoff  → move to cold       │
     └─────────────────────────────────────────────────────┘
```

**Components:**
- **Hot tier:** In-memory store (Python dict, Redis) holding the agent's current working set. Always included in the prompt. Very small, typically under 20 items.
- **Warm tier:** A fast vector database or key-value store holding recently accessed or moderately important memories. Searched on demand. Hundreds to thousands of items.
- **Cold tier:** Archival storage (S3, SQLite, compressed files) holding the full history. Searched only when hot and warm tiers can't find relevant results. Can hold millions of items.
- **Tier manager:** A policy engine that runs after each turn (or on a schedule). It promotes, demotes, or evicts memories based on configurable rules.

**Data flow:**
1. New memories always enter the hot tier.
2. At the end of each turn, the tier manager checks all hot memories against demotion rules.
3. Memories that haven't been accessed recently get demoted to warm. Stale warm memories get demoted to cold.
4. When a cold memory is retrieved (because hot and warm didn't answer the query), it gets promoted back to warm or hot.
5. The agent's prompt is assembled from: system prompt + all hot-tier memories + top-k warm-tier search results.

**Strengths:**
- Efficient use of the context window. Only the most relevant memories consume tokens.
- Graceful scaling. The cold tier can hold unlimited history without hurting performance.
- Mirrors how human memory works: frequent access strengthens memories.
- Clear performance characteristics per tier.

**Weaknesses:**
- The most complex pattern to implement and tune
- Promotion/demotion policies require careful calibration
- Important memories risk getting stuck in cold storage if policies are too aggressive
- Three stores to manage

**Best for:** Long-running agents with extensive histories, production systems with strict latency requirements, enterprise assistants serving many users.

**Real-world examples:** MemGPT's archival/recall/core memory tiers, Anthropic's 7-layer memory hierarchy for Claude Code, enterprise knowledge management systems.

---

## 4. Graph-Augmented Pattern

Imagine you have a filing cabinet AND a contact book. The filing cabinet holds your notes (you search by topic). The contact book maps relationships: Alice manages Bob, Bob works on Project X, Project X uses Python. Some questions need the filing cabinet ("What did I write about databases?"). Others need the contact book ("Who works with Alice?"). The best answers often come from checking both.

**A vector store for meaning-based retrieval combined with a knowledge graph for structured relationship traversal.**

A knowledge graph is a data structure where nodes represent entities (people, projects, concepts) and edges represent relationships between them ("manages," "works_on," "uses"). This pattern recognizes that not all knowledge fits neatly into flat text. Relationships between entities are better represented as graph edges you can follow step by step.

```
                          ┌──────────────────┐
                          │    LLM Agent      │
                          └────────┬─────────┘
                                   │
                      query ┌──────┴──────┐ query
                            ▼             ▼
                   ┌──────────────┐ ┌──────────────┐
                   │ Vector Store  │ │ Knowledge    │
                   │               │ │ Graph        │
                   │ Semantic      │ │              │
                   │ search over   │ │ Entities:    │
                   │ text chunks   │ │  (Alice)──┐  │
                   │               │ │  (Bob)────┤  │
                   │ [0.2, 0.8,…] │ │  (Proj X)─┘  │
                   │ [0.1, 0.3,…] │ │              │
                   │ [0.9, 0.4,…] │ │ Edges:       │
                   │               │ │  manages     │
                   └──────┬───────┘ │  works_on    │
                          │         │  uses_tech   │
                          │         └──────┬───────┘
                          │                │
                          ▼                ▼
                   ┌─────────────────────────────┐
                   │       Result Merger          │
                   │                             │
                   │  Combine semantic results   │
                   │  with graph traversal       │
                   │  results. Deduplicate.      │
                   │  Rank by relevance.         │
                   └─────────────────────────────┘
                                   │
                          ┌────────┴─────────────┐
                          │  Entity Extractor     │
                          │  (runs after each     │
                          │   turn to update      │
                          │   both stores)        │
                          └──────────────────────┘
```

**Components:**
- **Vector store:** Holds embedded text chunks (conversation excerpts, summaries, document fragments). Supports semantic similarity search.
- **Knowledge graph:** A graph database (Neo4j, NetworkX, or even an in-memory dict of triples) holding entities as nodes and relationships as edges. Supports traversal queries like "find all people who work on Project X."
- **Entity extractor:** An LLM-based or NER-based pipeline that runs after each turn. NER (Named Entity Recognition) means automatically detecting names of people, places, organizations, and other structured items in text. The extractor identifies entities and relationships, then updates both stores.
- **Result merger:** Combines results from both stores, removes duplicates, and ranks them before injecting into the agent's context.

**Data flow:**
1. After each turn, the entity extractor processes the conversation to find new entities and relationships.
2. Text chunks go to the vector store. Entity-relationship triples go to the knowledge graph.
3. At retrieval time, the user message triggers two parallel queries: semantic search on the vector store and entity/relationship lookup on the knowledge graph.
4. The result merger combines both result sets, removes duplicates, and produces a ranked context block.
5. This context block goes into the agent's prompt.

**Strengths:**
- Best of both worlds: semantic similarity for free-text recall + structured traversal for entity questions
- Enables multi-hop reasoning ("Who manages the person who works on the project that uses Python?")
- The knowledge graph naturally supports entity deduplication and relationship updates
- Graph structure makes temporal reasoning easier (edges can carry timestamps)

**Weaknesses:**
- Entity extraction is imperfect. LLM-based extraction can miss or hallucinate entities.
- Two stores to maintain and keep in sync
- The knowledge graph requires schema design decisions
- Merger logic adds latency and complexity

**Best for:** Agents that handle entity-rich domains (CRM, project management, research), multi-user systems where relationships between entities matter, knowledge-intensive assistants.

**Real-world examples:** Zep's temporal knowledge graphs, Graphiti (episode-to-semantic graph extraction), Microsoft's GraphRAG, custom Neo4j + vector store pipelines.

---

## 5. Full Cognitive Architecture

Picture a whole office. You have a desk for active work (working memory), a filing cabinet for past events (episodic memory), a reference shelf for facts (semantic memory), a procedures manual for how-to guides (procedural memory), and an office manager who decides where to file things and what to pull out (memory router). Background staff handle cleanup: merging duplicate files, archiving old ones, and throwing out what's no longer relevant. This is the most complex setup, but it can handle any question.

**A complete memory system with specialized stores for different memory types, a memory router that directs reads and writes, and a working memory manager that curates the agent's active context.**

This is the most sophisticated pattern. Cognitive science models of human memory inspire it. The agent's memory becomes a set of cooperating subsystems, each optimized for a different kind of knowledge.

```
     ┌──────────────────────────────────────────────────────────────────┐
     │                         LLM Agent                                │
     │                                                                  │
     │  ┌────────────────────────────────────────────────────────────┐  │
     │  │                    Working Memory                          │  │
     │  │                    (Context Window)                        │  │
     │  │                                                            │  │
     │  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐ │  │
     │  │  │ System   │ │ Core     │ │ Retrieved│ │ Conversation │ │  │
     │  │  │ Prompt   │ │ Memory   │ │ Memories │ │ Buffer       │ │  │
     │  │  │          │ │ (pinned  │ │ (dynamic │ │ (last k      │ │  │
     │  │  │          │ │  facts)  │ │  per turn│ │  messages)   │ │  │
     │  │  └──────────┘ └──────────┘ └──────────┘ └──────────────┘ │  │
     │  │                                                            │  │
     │  │  Token budget manager: allocates tokens across sections    │  │
     │  └────────────────────────────────────────────────────────────┘  │
     └───────────────────────────┬──────────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │     Memory Router        │
                    │                          │
                    │  Classifies incoming     │
                    │  content and routes to   │
                    │  appropriate store(s).   │
                    │                          │
                    │  Routes queries to the   │
                    │  most relevant store(s). │
                    └─────┬──────┬──────┬──────┘
                          │      │      │
              ┌───────────┘      │      └───────────┐
              ▼                  ▼                  ▼
     ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
     │  Episodic     │  │  Semantic     │  │  Procedural   │
     │  Memory       │  │  Memory       │  │  Memory       │
     │               │  │               │  │               │
     │  "What        │  │  "What is     │  │  "How to      │
     │   happened"   │  │   true"       │  │   do things"  │
     │               │  │               │  │               │
     │  Episodes     │  │  Facts &      │  │  Workflows,   │
     │  with time-   │  │  entities,    │  │  learned       │
     │  stamps,      │  │  generaliz-   │  │  procedures,   │
     │  participants │  │  ations       │  │  tool usage    │
     │  context      │  │               │  │  patterns      │
     │               │  │  Knowledge    │  │               │
     │  Vector DB    │  │  graph +      │  │  Structured    │
     │  + metadata   │  │  vector DB    │  │  store (JSON,  │
     │               │  │               │  │  YAML, DB)     │
     └──────────────┘  └──────────────┘  └──────────────┘

     ┌─────────────────────────────────────────────────────────┐
     │                 Background Processes                     │
     │                                                         │
     │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
     │  │ Consolidation │  │ Compaction    │  │ Decay &       │  │
     │  │               │  │               │  │ Forgetting    │  │
     │  │ Merge related │  │ Summarize &   │  │               │  │
     │  │ episodes,     │  │ compress old  │  │ Reduce scores │  │
     │  │ strengthen    │  │ memories,     │  │ over time,    │  │
     │  │ repeated      │  │ deduplicate   │  │ prune below   │  │
     │  │ patterns      │  │ facts         │  │ threshold     │  │
     │  └──────────────┘  └──────────────┘  └──────────────┘  │
     │                                                         │
     │  ┌──────────────┐  ┌──────────────┐                    │
     │  │ Reflection    │  │ Entity        │                    │
     │  │               │  │ Extraction    │                    │
     │  │ Generate      │  │               │                    │
     │  │ meta-obs      │  │ NER + relation│                    │
     │  │ about past    │  │ extraction    │                    │
     │  │ behavior      │  │ pipeline      │                    │
     │  └──────────────┘  └──────────────┘                    │
     └─────────────────────────────────────────────────────────┘
```

**Components:**

- **Working memory (context window manager):** Manages the agent's limited attention. It allocates a token budget (the maximum number of tokens allowed per prompt section) across system prompt, pinned memories, retrieved memories, and conversation buffer. When the budget is exceeded, it evicts the least important content.

- **Memory router:** A classifier (rule-based or LLM-based) that examines each piece of incoming information and decides where to store it. "Alice's birthday is March 5" goes to semantic memory. "We discussed the project timeline yesterday" goes to episodic memory. "When the user asks for a CSV export, use the export_csv tool" goes to procedural memory. The router also directs retrieval queries to the most likely store(s).

- **Episodic memory:** Stores complete interaction episodes with rich metadata (timestamps, participants, topics, emotional tone, outcomes). Answers "what happened" questions. Typically a vector store with structured metadata filters.

- **Semantic memory:** Stores generalized facts, entity records, and domain knowledge distilled from interactions. Answers "what is true" questions. Often a knowledge graph augmented with a vector store (pattern 4 nested inside pattern 5).

- **Procedural memory:** Stores learned procedures, tool usage patterns, and workflows. Answers "how to do X" questions. Can be a structured store (JSON, YAML) or a specialized collection with executable templates.

- **Background processes:** Asynchronous tasks that maintain memory health:
  - **Consolidation:** Merges related episodes and strengthens frequently accessed memories.
  - **Compaction:** Summarizes verbose memories, removes duplicate facts, and prunes contradictions.
  - **Decay & forgetting:** Reduces importance scores over time. Archives or deletes memories below a threshold.
  - **Reflection:** Generates meta-observations about the agent's own behavior and outcomes.
  - **Entity extraction:** Continuously extracts entities and relationships from new interactions.

**Data flow:**
1. A user message arrives. The working memory manager calculates the current token budget.
2. The memory router classifies the query intent and selects which store(s) to search.
3. Retrieved results from relevant stores are ranked and injected into working memory.
4. The agent generates a response using the assembled context.
5. After the response, the memory router classifies the new information and writes it to the appropriate store(s).
6. Background processes run (synchronously or asynchronously) to consolidate, compact, and maintain memory health.

**Strengths:**
- The most capable and flexible architecture. Handles any memory workload.
- Each memory type is optimized for its specific access pattern.
- Background processes prevent unbounded growth and maintain quality.
- Mirrors well-studied cognitive science models. This gives you intuitive mental models for debugging.

**Weaknesses:**
- Highest implementation complexity. Many components to build and integrate.
- Memory router accuracy is critical. Misrouting degrades the entire system.
- Background processes add operational overhead.
- Over-engineering risk for simple use cases.

**Best for:** Production-grade AI assistants, long-lived agents that accumulate knowledge over months or years, research platforms exploring cognitive architectures.

**Real-world examples:** Letta/MemGPT (core memory + recall memory + archival memory + inner monologue), Anthropic's Claude Code memory layers, SOAR cognitive architecture, ACT-R cognitive architecture (adapted for LLMs).

---

## Pattern Comparison Table

| Pattern | Complexity | Stores | Best For | Retrieval | Scaling | Example Systems |
|---------|-----------|--------|----------|-----------|---------|-----------------|
| **Single-store** | Low | 1 vector DB | Prototypes, demos, learning | Semantic search only | Poor (degrades with size) | LangChain VectorStoreRetrieverMemory |
| **Dual-store** | Medium | Buffer + vector DB | Personal assistants, support bots | Buffer scan + semantic search | Moderate | Mem0, Summary Buffer + Vector Store |
| **Tiered** | High | Hot + warm + cold stores | Long-running agents, enterprise | Tiered search with promotion | Good (cold tier is cheap) | MemGPT tiers, CPU cache model |
| **Graph-augmented** | Medium-High | Vector DB + knowledge graph | Entity-rich domains, multi-hop Q&A | Semantic + graph traversal | Good (graph handles relationships) | Zep, Graphiti, GraphRAG |
| **Full cognitive** | Very High | Working + episodic + semantic + procedural | Production assistants, research | Router-directed multi-store | Excellent (each store scales independently) | Letta/MemGPT, SOAR, Claude Code |

---

## Choosing a Pattern

Use this decision flowchart:

```
Start
  │
  ├─ Is this a prototype or learning project?
  │    YES → Single-store pattern
  │
  ├─ Do you need cross-session persistence?
  │    NO  → Single-store with in-memory buffer
  │    YES ↓
  │
  ├─ Do you need entity/relationship tracking?
  │    NO  → Dual-store pattern
  │    YES ↓
  │
  ├─ Do you need multi-hop reasoning over entities?
  │    NO  → Dual-store + entity extraction
  │    YES → Graph-augmented pattern
  │
  ├─ Do you have strict latency or token budget requirements?
  │    YES → Tiered pattern (or tiered + graph)
  │
  ├─ Do you need multiple memory types (episodic + semantic + procedural)?
  │    YES → Full cognitive architecture
  │
  └─ When in doubt, start with Dual-store and evolve.
```

**General advice:** Start with the simplest pattern that meets your needs. You can always evolve to a more complex one later. The patterns nest naturally: a full cognitive architecture contains a graph-augmented pattern, which contains a dual-store pattern.

---

## Further Reading

- [Technique 06 - Vector Store Memory](../all_techniques/06_vector_store_memory/): Implements the single-store pattern
- [Technique 08 - Knowledge Graph Memory](../all_techniques/08_knowledge_graph_memory/): Implements the graph-augmented pattern
- [Technique 12 - Working Memory & Context Window](../all_techniques/12_working_memory_context_window/): Implements the working memory component
- [Technique 13 - Hierarchical Memory Layers](../all_techniques/13_hierarchical_memory_layers/): Implements the tiered pattern
- [Technique 17 - Memory Routing](../all_techniques/17_memory_routing/): Implements the memory router component
- [Technique 26 - Letta/MemGPT Patterns](../all_techniques/26_letta_memgpt_patterns/): Implements a full cognitive architecture

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=docs--architecture)
