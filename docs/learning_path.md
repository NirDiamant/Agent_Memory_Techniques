# Detailed Learning Path Guide

This guide expands on the four learning paths outlined in the main README. For each path, you'll find prerequisites, time estimates per technique, what you'll learn, and a capstone project idea to solidify your understanding.

**Total estimated time for all four paths: 30-50 hours** (depending on depth and project work).

---

## Path 1: Beginner (Foundations)

**Goal:** Understand the core mechanics of agent memory: how conversations are stored, trimmed, summarized, and persisted.

**Techniques covered:**
```
01 Conversation Buffer → 02 Sliding Window → 03 Summary Memory →
05 Token Buffer → 06 Vector Store Memory → 21 Cross-Session Memory
```

### Prerequisites

- **Python proficiency:** You're comfortable with classes, functions, lists, dictionaries, and string manipulation. You can read and modify a 200-line Python script without difficulty.
- **Basic LLM API usage:** You've called the OpenAI or Anthropic API at least once. You understand the concept of messages, roles (system/user/assistant), and completions.
- **Jupyter notebooks:** You know how to run cells, install packages with `!pip install`, and read inline output.
- **No ML knowledge required.** You don't need to understand embeddings, vector math, or neural networks to start this path. Technique 06 teaches you what you need.

### Technique-by-Technique Breakdown

| # | Technique | Time | What You'll Learn |
|---|-----------|------|---------------------|
| 01 | Conversation Buffer Memory | 30-45 min | How to store the full conversation as a list of messages and pass it to the LLM. Why this is the simplest approach and why it breaks down with long conversations. You'll implement a `ConversationBufferMemory` class from scratch. |
| 02 | Sliding Window Memory | 30-45 min | How to keep only the last *k* messages, trading completeness for bounded context size. You'll experiment with different window sizes and observe the quality trade-off. |
| 03 | Summary Memory | 45-60 min | How to use the LLM itself to summarize conversation history, replacing old messages with a compact summary. You'll implement the summarization prompt and the replacement logic. |
| 05 | Token Buffer Memory | 30-45 min | How to count tokens (the units LLMs use to measure text length) accurately using `tiktoken` and trim messages to fit a strict token budget. You'll learn why character count isn't the same as token count. |
| 06 | Vector Store Memory | 45-60 min | How embeddings work (converting text into number arrays that capture meaning), how to store them in a vector database (ChromaDB), and how to run semantic similarity search to retrieve relevant past context. This is the gateway to all long-term memory techniques. |
| 21 | Cross-Session Memory | 45-60 min | How to save and reload agent memory state so it survives across independent sessions. You'll implement save/load logic and build a chatbot that remembers returning users. |

### Capstone Project: Chatbot with Memory

Build a command-line chatbot that:

1. Maintains a sliding window of the last 10 messages for immediate context.
2. After every 5 turns, summarizes the conversation and stores the summary in a ChromaDB collection.
3. On each new user message, searches the ChromaDB collection for relevant past summaries and injects the top 2 into the prompt.
4. Saves its full state (conversation buffer + ChromaDB path) to disk on exit and reloads it on restart.

**Success criteria:** Start a conversation, discuss several topics, exit, restart, and verify the chatbot recalls earlier topics accurately.

**Estimated time for project: 3-5 hours.**

---

## Path 2: Intermediate (Structured Memory)

**Goal:** Build richer memory systems that track entities, model relationships, and use sophisticated retrieval strategies.

**Techniques covered:**
```
07 Entity Memory → 08 Knowledge Graph → 09 Episodic Memory →
10 Semantic Memory → 20 Retrieval Patterns → 22 Multi-Agent Shared Memory
```

### Prerequisites

- **Completed Path 1** or equivalent experience with conversation buffer, summarization, and vector store basics.
- **Comfortable with data structures:** Dictionaries of dictionaries, graph representations (adjacency lists), and JSON manipulation.
- **Basic understanding of embeddings:** You know what a vector embedding is and how cosine similarity works (covered in technique 06).
- **Optional but helpful:** Familiarity with graph databases (Neo4j) or graph libraries (NetworkX).

### Technique-by-Technique Breakdown

| # | Technique | Time | What You'll Learn |
|---|-----------|------|---------------------|
| 07 | Entity Memory | 45-60 min | How to extract entities (people, projects, preferences) from conversation text using LLM-based extraction. How to maintain an entity store that updates as new information arrives. You'll handle entity deduplication and attribute updates. |
| 08 | Knowledge Graph Memory | 60-90 min | How to represent entities as nodes and relationships as edges in a graph structure. How to run graph traversal queries ("Who works on Project X?"). You'll build a knowledge graph using NetworkX or a dict-based structure. |
| 09 | Episodic Memory | 45-60 min | How to store complete interaction episodes with temporal metadata (timestamps, topics, participants). How episode storage differs from raw conversation logging. You'll implement episode boundary detection and episode-level retrieval. |
| 10 | Semantic Memory | 45-60 min | How to extract generalized facts from specific conversations and store them separately from episodes. The distinction between "Alice mentioned she likes hiking on Tuesday" (episodic) vs. "Alice enjoys hiking" (semantic). You'll build an extraction pipeline that distills facts from episodes. |
| 20 | Retrieval Patterns | 60-90 min | A comparative study of retrieval strategies: pure semantic search, temporal recency weighting, hybrid scoring (semantic + recency + importance), MMR (Maximal Marginal Relevance, a technique that balances relevance with diversity), and cross-encoder re-ranking. You'll implement and benchmark each strategy. |
| 22 | Multi-Agent Shared Memory | 45-60 min | How multiple agents can share a common memory store, read each other's memories, and coordinate through shared context. You'll implement a shared memory bus and observe how agents collaborate. |

### Capstone Project: Personal Assistant with Entity Tracking

Build a personal assistant that:

1. Extracts entities (people, projects, preferences, dates) from every conversation turn and maintains an entity store.
2. Builds a knowledge graph of relationships between entities.
3. Stores each conversation session as an episode with timestamps and topic labels.
4. Uses hybrid retrieval (semantic similarity + entity match + recency) to find relevant context for each new query.
5. Can answer questions like "What did Alice say about the project last week?" by combining episodic and entity memory.

**Success criteria:** After 10+ conversation turns covering multiple people and projects, the assistant accurately answers entity-specific and temporal questions.

**Estimated time for project: 5-8 hours.**

---

## Path 3: Advanced (Cognitive Architectures)

**Goal:** Implement human-inspired memory patterns: working memory management, hierarchical storage, consolidation, reflection, and controlled forgetting.

**Techniques covered:**
```
12 Working Memory → 13 Hierarchical Layers → 14 Consolidation →
16 Self-Reflection → 17 Memory Routing → 19 Forgetting & Decay
```

### Prerequisites

- **Completed Paths 1 and 2** or equivalent experience with vector stores, entity extraction, and retrieval patterns.
- **Token counting and budget management:** You're comfortable with `tiktoken` and understand how to allocate a context window across multiple sections.
- **Comfortable with async patterns:** Some background processes (consolidation, decay) run asynchronously. Basic experience with Python `asyncio` or threading is helpful.
- **Interest in cognitive science:** Not required, but familiarity with concepts like working memory capacity, memory consolidation during sleep, and spaced repetition will deepen your understanding.

### Technique-by-Technique Breakdown

| # | Technique | Time | What You'll Learn |
|---|-----------|------|---------------------|
| 12 | Working Memory & Context Window | 60-90 min | How to actively manage the agent's context window as a scarce resource. You'll implement a token budget allocator that distributes context space across system prompt, pinned memories, retrieved memories, and conversation buffer. You'll handle priority-based eviction when the budget is exceeded. |
| 13 | Hierarchical Memory Layers | 60-90 min | How to implement hot/warm/cold memory tiers with promotion and demotion policies. You'll build a tier manager that moves memories between layers based on access frequency, recency, and importance. This mirrors CPU cache hierarchies (small fast layers hold the most-used data). |
| 14 | Memory Consolidation | 45-60 min | How to merge related memories, strengthen frequently accessed patterns, and resolve contradictions during periodic consolidation runs. You'll implement a consolidation pipeline inspired by how the brain strengthens memories during sleep. |
| 16 | Self-Reflection Memory | 45-60 min | How to make the agent generate meta-observations about its own past behavior and outcomes. The agent examines its recent actions and generates insights like "I tend to give overly long answers. I should be more concise." These reflections are stored and influence future behavior. |
| 17 | Memory Routing | 60-90 min | How to build a memory router that classifies incoming content (fact vs. episode vs. procedure vs. preference) and directs reads and writes to the appropriate store. You'll implement both rule-based and LLM-based routers and compare their accuracy. |
| 19 | Forgetting & Decay | 45-60 min | How to implement controlled forgetting through exponential decay functions, access-frequency scoring, and relevance-based pruning. You'll observe how forgetting actually improves retrieval quality by removing noise. |

### Capstone Project: Multi-Session Agent with Reflection

Build an agent that:

1. Manages a working memory context window with explicit token budgets for each section.
2. Uses three-tier storage (hot/warm/cold) with automatic promotion and demotion.
3. Runs a consolidation process at the end of each session to merge related memories and extract durable facts.
4. Generates self-reflections every 10 turns. It stores meta-observations that influence future responses.
5. Applies exponential decay to memory scores. Accessed memories get score boosts.
6. Routes new memories to episodic, semantic, or procedural stores based on content classification.

**Success criteria:** Over 3+ sessions spanning different topics, the agent demonstrates: (a) improving response quality through self-reflection, (b) graceful handling of large memory stores through tiered storage and decay, and (c) accurate retrieval across memory types through routing.

**Estimated time for project: 8-12 hours.**

---

## Path 4: Practitioner (Frameworks & Production)

**Goal:** Integrate with production-grade memory frameworks (Mem0, Letta/MemGPT, Graphiti, Zep) and learn how to evaluate and deploy memory systems at scale.

**Techniques covered:**
```
25 Mem0 → 26 Letta/MemGPT → 24 Graphiti → 27 Zep →
28 Evaluation → 29 Benchmarks → 30 Production Patterns
```

### Prerequisites

- **Completed Paths 1-3** or significant hands-on experience building agent memory systems.
- **Docker and basic DevOps:** Some frameworks (Zep, Letta) require Docker for local deployment. You should be comfortable running `docker-compose up`.
- **API key management:** You'll need API keys for OpenAI (or compatible providers) and potentially for managed services like Pinecone or Zep Cloud.
- **Production mindset:** Familiarity with concepts like caching, TTLs (time-to-live expiration policies), sharding (splitting data across partitions), backup strategies, and privacy compliance (GDPR). This path covers real-world deployment concerns.

### Technique-by-Technique Breakdown

| # | Technique | Time | What You'll Learn |
|---|-----------|------|---------------------|
| 25 | Mem0 Patterns | 45-60 min | How to integrate Mem0's managed memory layer. Mem0 automatically extracts, stores, and retrieves user-specific memories. You'll explore Mem0's API for adding memories, searching, and managing user-scoped memory. You'll compare Mem0's automatic extraction with your own manual extraction pipelines. |
| 26 | Letta/MemGPT Patterns | 60-90 min | How to implement MemGPT's self-editing memory architecture: inner monologue, core/recall/archival memory tiers, heartbeat events for agentic loops, and memory pressure management. This is the most sophisticated single-framework technique in the repository. |
| 24 | Graph Memory with Graphiti | 60-90 min | How to use Zep's Graphiti library to build temporal knowledge graphs from conversations. You'll see how Graphiti extracts entities and relationships from episodes, handles temporal updates, and supports graph-based retrieval. |
| 27 | Zep Memory | 45-60 min | How to use Zep's production-ready memory service: dialog classification, entity extraction, temporal knowledge graphs, and user/session management. You'll explore Zep's API and compare it with building the same features from scratch. |
| 28 | Memory Evaluation | 60-90 min | How to measure memory quality with quantitative metrics: retrieval precision/recall at k, staleness detection accuracy, contradiction handling rate, temporal ordering accuracy, and end-to-end task performance. You'll build an evaluation harness and run it against your own memory system. |
| 29 | Memory Benchmarks (LoCoMo) | 60-90 min | How to run your memory system against standardized benchmarks. You'll download LoCoMo and LongMemEval datasets, format them for your system, run evaluations, and interpret the results. You'll learn what scores are "good" and where common architectures fail. |
| 30 | Production Memory Patterns | 60-90 min | Architecture patterns for deploying agent memory at scale: caching strategies (Redis, in-process LRU), TTL policies, memory sharding by user/tenant, backup and disaster recovery, privacy compliance (GDPR right-to-erasure, data retention policies), observability (logging, metrics, tracing for memory operations), and cost optimization. |

### Capstone Project: Production-Grade Memory System

Build a production-ready memory service that:

1. Integrates at least one framework (Mem0, Letta, or Zep) as the primary memory backend.
2. Supports multi-user isolation with per-user memory sharding.
3. Implements a caching layer (Redis or in-memory LRU) for frequently accessed memories.
4. Has an evaluation suite that measures retrieval precision, temporal accuracy, and entity consistency.
5. Includes observability: logging of all memory operations, metrics for retrieval latency and hit rates, and alerting on memory pressure.
6. Handles privacy compliance: a "forget me" endpoint that erases all memories for a given user.

**Success criteria:** The system passes a LoCoMo-style evaluation with >80% retrieval precision, handles 100+ concurrent users with <100ms retrieval latency, and correctly implements the forget-me endpoint.

**Estimated time for project: 15-25 hours.**

---

## Choosing Your Path

| If you are... | Start with | Skip to |
|---------------|------------|---------|
| New to LLM agents | Path 1 (Beginner) | (none) |
| Comfortable with LLM APIs, new to memory | Path 1, skip 01 | Path 2 after 06 |
| Built basic RAG systems | Path 2 (Intermediate) | (none) |
| Built memory systems before, want depth | Path 3 (Advanced) | (none) |
| Want to ship to production ASAP | Path 2 briefly, then Path 4 | (none) |
| Researching cognitive architectures | Path 3, then select from Path 4 | (none) |

---

## Time Investment Summary

| Path | Techniques | Study Time | Project Time | Total |
|------|-----------|------------|--------------|-------|
| Beginner | 6 techniques | 4-5 hours | 3-5 hours | 7-10 hours |
| Intermediate | 6 techniques | 5-7 hours | 5-8 hours | 10-15 hours |
| Advanced | 6 techniques | 5-7 hours | 8-12 hours | 13-19 hours |
| Practitioner | 7 techniques | 7-10 hours | 15-25 hours | 22-35 hours |
| **All paths** | **25 techniques** | **21-29 hours** | **31-50 hours** | **52-79 hours** |

Note: These are estimates for careful study, including running all notebook cells, reading the code, and experimenting with modifications. You can move faster by skimming, or slower by building extensive projects.

---

## Tips for Getting the Most Out of Each Technique

1. **Run every cell.** Don't read the notebooks passively. Execute them and examine the outputs.
2. **Break things on purpose.** Change parameters, reduce window sizes, corrupt memories, and observe what happens.
3. **Compare approaches.** After learning two techniques that solve similar problems (e.g., sliding window vs. summary memory), implement both in the same notebook and compare their outputs side by side.
4. **Build incrementally.** Each capstone project builds on the previous one. Start with Path 1's chatbot and evolve it through each path.
5. **Read the source code of frameworks.** When you reach Path 4, clone Mem0 or Letta and read their core memory management code. Seeing how production systems handle edge cases is invaluable.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=docs--learning-path)
