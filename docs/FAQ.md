# Frequently Asked Questions

> A practical reference covering agent memory concepts, technique selection, frameworks, and production concerns. Question-driven so generative search engines can quote individual answers.

## Concepts

### Q: What is agent memory?

**A:** Agent memory is any mechanism that lets an LLM-based agent retain and recall information beyond its current prompt. Without memory, every conversation turn starts from zero. Memory systems store past interactions, extracted facts, or learned procedures and inject relevant pieces back into the context window when the agent needs them. Implementations range from appending raw chat history (conversation buffer) to sophisticated knowledge graphs with temporal decay. The goal is always the same: give the agent enough context to act coherently over time without exceeding the model's token limit.

See also: [01 Conversation Buffer Memory](all_techniques/01_conversation_buffer_memory/README.md)

### Q: How is agent memory different from RAG?

**A:** RAG (Retrieval-Augmented Generation) pulls documents from a static knowledge base to answer questions. Agent memory pulls information the agent itself has gathered during conversations. RAG retrieves pre-existing knowledge; agent memory retrieves experience. In practice, the retrieval step looks similar (embed, search, inject), but the data source differs. RAG indexes documents you provide up front. Agent memory indexes facts, episodes, and procedures the agent extracted at runtime. Many production systems combine both: RAG for domain knowledge, agent memory for user-specific context.

See also: [06 Vector Store Memory](all_techniques/06_vector_store_memory/README.md)

### Q: What is the difference between short-term and long-term agent memory?

**A:** Short-term memory lives inside the current context window. It is fast but size-limited (4k to 200k tokens depending on the model). Long-term memory lives outside the context window in a database, vector store, or file. It persists across sessions but requires a retrieval step to bring relevant pieces back into the prompt. Most real agents combine both: short-term memory holds the active conversation, and long-term memory stores facts and episodes that outlive a single session.

See also: [12 Working Memory / Context Window](all_techniques/12_working_memory_context_window/README.md)

### Q: What is the difference between episodic and semantic memory in agents?

**A:** Episodic memory stores timestamped experiences: what happened during a specific session, including context and sequence. Semantic memory stores context-free facts: things the agent knows regardless of when it learned them. An episodic memory might be "On Tuesday the user asked to reschedule the demo and was frustrated." A semantic memory might be "The user prefers afternoon meetings." Episodic memory answers "What happened?" Semantic memory answers "What do we know?" Agents that need both temporal awareness and factual recall should run both stores.

See also: [09 Episodic Memory](all_techniques/09_episodic_memory/README.md), [10 Semantic Memory](all_techniques/10_semantic_memory/README.md)

### Q: What is working memory in the context of LLM agents?

**A:** Working memory is the subset of information currently loaded into the model's context window. Think of it as the agent's "desk": everything it can see right now. Managing working memory means choosing which messages, facts, and instructions stay in the prompt and which get evicted. Naive approaches use FIFO (first-in, first-out). Smarter approaches score each item by salience, recency, or task relevance and evict the lowest-scoring ones first. Good working memory management is the difference between an agent that forgets your name mid-conversation and one that keeps critical facts pinned.

See also: [12 Working Memory / Context Window](all_techniques/12_working_memory_context_window/README.md)

## Choosing a technique

### Q: I am building my first agent. Which memory technique should I start with?

**A:** Start with Conversation Buffer Memory. It stores every message and re-sends the full history on each turn. It takes about 15 minutes to implement and gives you perfect recall for short conversations (under a few thousand tokens). Once your conversations grow long enough to hit token limits or cost concerns, graduate to Sliding Window Memory (drop old messages) or Summary Memory (compress old messages). Do not reach for vector stores or knowledge graphs until you have a clear retrieval need. Start simple, measure, then add complexity.

See also: [01 Conversation Buffer Memory](all_techniques/01_conversation_buffer_memory/README.md)

### Q: How do I choose between Sliding Window Memory, Summary Memory, and Token Buffer Memory?

**A:** All three solve the same problem: conversation history that outgrows the context window. Sliding Window keeps the last K messages and drops the rest. It is the fastest and simplest, but older context vanishes completely. Summary Memory replaces old messages with an LLM-generated summary. It preserves a compressed version of everything, but summaries are lossy and cost an extra LLM call. Token Buffer Memory trims by exact token count rather than message count. Pick Sliding Window for latency-sensitive apps, Summary Memory when you need approximate recall of early turns, and Token Buffer when you want precise cost control.

See also: [02 Sliding Window Memory](all_techniques/02_sliding_window_memory/README.md), [03 Summary Memory](all_techniques/03_summary_memory/README.md), [05 Token Buffer Memory](all_techniques/05_token_buffer_memory/README.md)

### Q: When is agent memory overkill?

**A:** If your agent handles only single-turn requests (user asks, agent answers, done), you do not need memory. If conversations are short (under 20 turns) and context windows are large (128k+ tokens), a plain conversation buffer may be all you need. Memory infrastructure becomes worthwhile when you hit one of these triggers: conversations span multiple sessions, you need to recall facts from weeks ago, token costs are climbing, or the agent must track structured entities across interactions. Memory adds complexity. Do not add it until you feel the pain of not having it.

### Q: When should I combine multiple memory techniques?

**A:** Combine techniques when no single store covers all your recall needs. A common production stack pairs a sliding window for recent context with a vector store for long-term retrieval. Another useful combination is episodic memory (what happened) plus semantic memory (what we know) with a memory router dispatching to the right store. Start with one technique. Add a second only when you observe a specific failure: the agent forgets facts from last week, or it loses track of entities, or it re-derives procedures it already learned. Each additional store adds latency, cost, and maintenance.

See also: [17 Memory Routing](all_techniques/17_memory_routing/README.md)

### Q: At what scale do I need to move beyond simple conversation buffers?

**A:** The breakpoint depends on your model's context window and your cost tolerance. With a 4k-token window, you hit limits after roughly 10 to 20 turns. With 128k tokens, you can buffer hundreds of turns but pay for every token on every call. As a rule of thumb: if your average conversation exceeds 25% of the context window, switch to a trimming strategy (sliding window or token buffer). If you need recall across sessions or across thousands of past interactions, add a retrieval-based memory like vector store or knowledge graph. Token cost scales linearly with buffer size, so cost often forces the move before the window does.

See also: [05 Token Buffer Memory](all_techniques/05_token_buffer_memory/README.md)

## Frameworks and libraries

### Q: Mem0 vs Letta vs Zep vs Graphiti: when do I pick which?

**A:** **Mem0** is best when you want automatic fact extraction from conversations with minimal code. It provides a managed API that handles storage and retrieval by user ID. **Letta** (formerly MemGPT) is best for agents that manage their own memory through function calls, with tiered storage (core, archival, recall) for thousand-turn conversations. **Zep** is a managed service with temporal knowledge graphs, entity extraction, and asynchronous processing; pick it when you want graph-powered retrieval without self-hosting. **Graphiti** (by Zep) gives you the same temporal graph approach but self-hosted on Neo4j. Pick Mem0 for fast prototyping, Letta for self-managing agents, Zep for managed graph memory, and Graphiti for self-hosted graph memory.

See also: [25 Mem0 Patterns](all_techniques/25_mem0_patterns/README.md), [26 Letta/MemGPT Patterns](all_techniques/26_letta_memgpt_patterns/README.md), [27 Zep Memory](all_techniques/27_zep_memory/README.md), [24 Graph Memory with Graphiti](all_techniques/24_graph_memory_graphiti/README.md)

### Q: When should I use a memory framework vs build my own?

**A:** Use a framework when you want to ship fast and your use case fits the framework's assumptions. Mem0, Zep, and Letta each handle storage, retrieval, and extraction out of the box. Build your own when you need full control over extraction logic, storage schema, or retrieval ranking. Custom builds also make sense when you must comply with strict data residency rules or when your memory access patterns do not match any framework's model. A middle path: start with a framework to validate the product, then replace components you need to customize. The framework gets you to "memory works" in hours instead of weeks.

### Q: Is LangChain memory enough for production?

**A:** LangChain's built-in memory classes (`ConversationBufferMemory`, `ConversationSummaryMemory`, `VectorStoreRetrieverMemory`) are good for prototyping. They cover the basic patterns: buffer, summary, token buffer, entity, and vector retrieval. For production, you may outgrow them. LangChain memory does not natively handle multi-user isolation, TTL policies, memory consolidation, or temporal graphs. If you need those, layer a dedicated memory service (Mem0, Zep, or a custom store) behind a LangChain-compatible interface. LangChain is a good starting framework, not the final architecture.

See also: [01 Conversation Buffer Memory](all_techniques/01_conversation_buffer_memory/README.md), [06 Vector Store Memory](all_techniques/06_vector_store_memory/README.md)

### Q: Can I use MemGPT / Letta in production?

**A:** As of late 2025, Letta provides a server with REST APIs, persistent agent state, and tool-based memory management. It runs as a self-hosted service or through Letta Cloud. Production users report success for customer support agents and research assistants that handle hundreds of turns per session. The main operational consideration is the heartbeat mechanism: Letta agents can chain multiple internal steps per user message, which increases latency and token cost. You need to tune max heartbeat steps and monitor inner-monologue length. For high-throughput, low-latency use cases, test carefully before committing.

See also: [26 Letta/MemGPT Patterns](all_techniques/26_letta_memgpt_patterns/README.md)

### Q: What are the best open-source options for agent memory?

**A:** The main open-source options as of late 2025 are: **Mem0** (open-source core with optional managed service) for automatic fact extraction. **Letta** (open-source server) for tiered, agent-managed memory. **Graphiti** (open-source, by Zep) for temporal knowledge graphs on Neo4j. **LangChain** and **LlamaIndex** both provide memory modules for buffer, summary, and vector retrieval patterns. **Cognee** is an emerging open-source option for knowledge graph construction from unstructured data. If no single library covers your needs, the techniques in this repo show you how to build each pattern from scratch.

## Production concerns

### Q: How do I keep agent memory from leaking one user's data into another's?

**A:** Scope every memory operation by a user ID or session ID. At the storage layer, use per-user namespaces, row-level security, or separate collections. At the retrieval layer, always filter by user ID before similarity search. Never rely on the embedding model to separate users by content alone: two users discussing the same topic will have similar embeddings. In multi-tenant systems, consider encryption at rest with per-user keys. Test isolation by searching for User A's facts while authenticated as User B. If anything leaks, your scoping is broken.

See also: [30 Production Memory Patterns](all_techniques/30_production_memory_patterns/README.md)

### Q: How do I handle PII in agent memory?

**A:** Apply PII redaction at write time, not retrieval time. Before storing a memory, run it through a PII detector (spaCy, Presidio, or an LLM-based classifier) and replace sensitive fields (names, emails, phone numbers, SSNs) with tokens like `[USER_EMAIL]`. Store the mapping in a separate, access-controlled table so you can reconstruct if needed. For GDPR or CCPA compliance, implement a `forget_user(user_id)` function that deletes all memories, embeddings, and metadata for that user. Set retention TTLs so memories auto-expire if not refreshed.

See also: [30 Production Memory Patterns](all_techniques/30_production_memory_patterns/README.md)

### Q: How do I control memory costs in production?

**A:** Memory costs come from three sources: LLM calls for extraction and summarization, embedding calls for vectorization, and storage for persisting memories. To control them: (1) Batch extraction calls instead of processing every message individually. (2) Use smaller models (Haiku-class) for extraction and summarization tasks. (3) Set TTLs so stale memories get pruned automatically. (4) Compact memories periodically to reduce storage volume. (5) Track per-user memory size and set quotas. A typical memory system adds 10-30% to base LLM costs. Monitor the ratio and investigate if it exceeds 50%.

See also: [15 Memory Compaction](all_techniques/15_memory_compaction/README.md), [19 Forgetting and Decay](all_techniques/19_forgetting_and_decay/README.md)

### Q: What latency should I budget for memory retrieval?

**A:** Vector similarity search over a well-indexed store typically takes 5 to 50ms for up to 1 million entries. Cross-encoder re-ranking adds 50 to 200ms depending on the number of candidates (typically 10 to 50). Knowledge graph traversal in Neo4j adds 10 to 100ms per hop. An LLM-based routing or classification step adds 200 to 500ms. Total memory retrieval latency in a production pipeline is typically 50 to 300ms on top of the base LLM call. To stay under 500ms total memory overhead, cache frequent queries, limit re-ranking candidates, and use approximate nearest neighbor indexes.

See also: [20 Memory Retrieval Patterns](all_techniques/20_memory_retrieval_patterns/README.md)

### Q: How do I observe and debug agent memory in production?

**A:** Log every memory write, read, and delete with timestamps, user IDs, and the query or content involved. Track retrieval metrics: hit rate (how often retrieval returns useful results), precision at K, and latency per retrieval step. Instrument your memory pipeline with tracing (OpenTelemetry or LangSmith) so you can see what was retrieved for each agent turn. Build a dashboard that shows memory store size over time, extraction error rate, and cost per user. When an agent gives a wrong answer, the first debugging step is to check what memories were retrieved and whether the relevant fact was in the store at all.

See also: [28 Memory Evaluation](all_techniques/28_memory_evaluation/README.md)

## Evaluation

### Q: How do I know my agent's memory is actually working?

**A:** Measure three things: retrieval precision (did the right memories come back?), retrieval recall (were relevant memories missed?), and downstream answer quality (did the agent use the memories correctly?). Build a test dataset of 50 to 100 question-answer pairs where the answer depends on a past interaction. Run the memory pipeline end to end and score results with an LLM-as-judge or human evaluators. Compare against a no-memory baseline. If your memory system does not measurably beat the baseline, something in your pipeline is broken: extraction, storage, retrieval, or injection.

See also: [28 Memory Evaluation](all_techniques/28_memory_evaluation/README.md)

### Q: What is LoCoMo and how do I use it to benchmark agent memory?

**A:** LoCoMo (Long Conversation Memory) is an academic benchmark that tests memory systems against multi-session conversation datasets. It includes 10 long conversations with 300+ turns each and evaluates five question categories: single-session, multi-session, temporal reasoning, knowledge graph, and open-domain. To use it: load the dataset from Hugging Face, feed conversations into your memory system, then answer the benchmark questions and score with the provided LLM judge. A full run costs $5 to $15 in API calls. LoCoMo gives you a standardized score you can compare against published baselines.

See also: [29 Memory Benchmarks / LoCoMo](all_techniques/29_memory_benchmarks_LoCoMo/README.md)

### Q: What metrics should I track for agent memory quality?

**A:** Track these core metrics: **Retrieval Precision@K** (what fraction of top-K retrieved memories are relevant, typical target above 0.7). **Retrieval Recall** (what fraction of all relevant memories were retrieved, target above 0.8). **Staleness rate** (how often the top result contains outdated information). **Answer accuracy** on memory-dependent questions (measure with LLM-as-judge or human eval). **Latency** per retrieval call. **Memory store growth rate** per user per day. Start by measuring precision and recall on a golden test set of 50+ queries. These two numbers tell you if your retrieval pipeline is fundamentally healthy.

See also: [28 Memory Evaluation](all_techniques/28_memory_evaluation/README.md)

### Q: How do I A/B test different memory configurations?

**A:** Run two memory pipelines in parallel with the same input conversations. Route a random subset of users (or conversations) to each pipeline. Measure answer quality on memory-dependent questions using an LLM judge or user satisfaction scores. Compare retrieval precision, latency, and cost between the two groups. You need at least 100 to 200 test queries per group for statistically meaningful results. Common things to A/B test: retrieval top-K values, re-ranking vs no re-ranking, different chunking strategies, and decay half-life settings. Change one variable at a time.

See also: [28 Memory Evaluation](all_techniques/28_memory_evaluation/README.md)

### Q: When is memory the bottleneck vs the model itself?

**A:** Memory is the bottleneck when: (1) the agent has access to the right facts but retrieval fails to surface them, (2) the agent's answers degrade on older topics even though those facts exist in the store, or (3) latency spikes come from retrieval, not generation. The model itself is the bottleneck when: the right memories are injected into the context but the model still produces wrong answers, or the model ignores relevant context in long prompts. To tell the difference, log what was retrieved for each wrong answer. If the relevant memory was retrieved but the answer is still wrong, the model is the bottleneck. If it was not retrieved, memory is.

## Long-tail questions

### Q: What is the difference between entity memory and knowledge graph memory?

**A:** Entity memory maintains a flat dictionary: each entity (person, org, project) maps to a text block of known facts. Knowledge graph memory builds a directed graph where entities are nodes connected by typed relationships (subject-predicate-object triples). Entity memory answers "What do we know about Alice?" Knowledge graph memory also answers "Who manages Alice's team lead?" by traversing relationship edges. Use entity memory for simple fact lookup. Use knowledge graph memory when your agent needs multi-hop reasoning across connected facts. Knowledge graphs are more powerful but harder to maintain.

See also: [07 Entity Memory](all_techniques/07_entity_memory/README.md), [08 Knowledge Graph Memory](all_techniques/08_knowledge_graph_memory/README.md)

### Q: How does memory consolidation differ from memory compaction?

**A:** Memory consolidation clusters related memories, merges duplicates, and resolves contradictions. It reduces the number of memory entries. Memory compaction compresses individual memories to multiple fidelity levels (full text, summary, keywords, tags) without deleting any. Consolidation is destructive: merged memories cannot be un-merged. Compaction is progressive: you choose the detail level at retrieval time. Use consolidation when your store has many near-duplicate entries that confuse retrieval. Use compaction when you need to fit more knowledge into a limited token budget at query time.

See also: [14 Memory Consolidation](all_techniques/14_memory_consolidation/README.md), [15 Memory Compaction](all_techniques/15_memory_compaction/README.md)

### Q: What is memory routing and when do I need it?

**A:** Memory routing classifies each incoming memory operation (save or query) by content type and sends it to the correct specialized store. For example, an experience gets routed to episodic memory, a fact to semantic memory, and a procedure to procedural memory. You need routing when you run multiple memory backends and do not want to query all of them on every request. Without routing, you either duplicate writes to all stores (wasteful) or search all stores and merge results (slow). Routing adds 200 to 500ms per operation for the LLM classification call. It pays off when you have three or more specialized stores.

See also: [17 Memory Routing](all_techniques/17_memory_routing/README.md)

### Q: Can agents learn and improve over time using memory?

**A:** Yes, through two mechanisms. First, **procedural memory** stores successful workflows as reusable templates. When the agent encounters a similar task, it retrieves the proven procedure instead of reasoning from scratch. Second, **self-reflection memory** has the agent analyze its own performance after each task and store lessons learned. On future tasks, it retrieves relevant lessons and avoids past mistakes. Both require explicit implementation. Agents do not improve automatically by accumulating memories. You need extraction logic that identifies what is worth learning and retrieval logic that surfaces lessons at the right time.

See also: [11 Procedural Memory](all_techniques/11_procedural_memory/README.md), [16 Self-Reflection Memory](all_techniques/16_self_reflection_memory/README.md)

### Q: How do I handle contradictions in agent memory?

**A:** Contradictions arise when new facts conflict with stored ones ("User prefers morning meetings" vs "User said they hate mornings"). You have three strategies: (1) **Timestamp-based**: always prefer the newer fact. This works well for user preferences that change over time. (2) **Confidence-based**: score each memory by extraction confidence and prefer higher-confidence entries. (3) **Explicit resolution**: when a contradiction is detected during consolidation, generate a merged entry that acknowledges the change ("User previously preferred mornings but now prefers afternoons"). Whichever strategy you pick, log contradictions for debugging.

See also: [14 Memory Consolidation](all_techniques/14_memory_consolidation/README.md), [18 Temporal Memory](all_techniques/18_temporal_memory/README.md)

### Q: What is the Summary Buffer Memory pattern and when does it beat pure summarization?

**A:** Summary Buffer Memory keeps the last N messages verbatim in a buffer while compressing everything older into a running summary. Pure Summary Memory compresses all past messages. Summary Buffer wins when you need exact recall of recent turns (names, numbers, code snippets) but also need approximate recall of earlier conversation. The verbatim buffer prevents lossy compression from corrupting recent details. The tradeoff is more complexity: you must tune buffer size, summary refresh rate, and total token budget. Use Summary Buffer when both precision on recent turns and recall on older turns matter.

See also: [04 Summary Buffer Memory](all_techniques/04_summary_buffer_memory/README.md)

### Q: How do I implement cross-session memory for a chatbot?

**A:** At minimum, you need three things: (1) A user identifier (login, cookie, or API key) so you know who is returning. (2) A storage backend (database, file system, or managed service) that persists memory between sessions. (3) A load/save cycle that retrieves the user's memory at session start and updates it at session end or after each turn. For simple use cases, serialize the conversation buffer to JSON keyed by user ID. For richer memory, persist extracted facts or embeddings to a vector store with user-scoped collections. Test the cold-start path: what happens when a returning user's memory is large?

See also: [21 Cross-Session Memory](all_techniques/21_cross_session_memory/README.md)

### Q: How does multi-agent shared memory work?

**A:** Multiple agents read from and write to a shared memory store with namespace scoping. Each agent typically has a private namespace for its own working state and read access to a shared namespace for cross-agent communication. Conflict resolution is needed when two agents update the same memory entry. Strategies include last-write-wins, version vectors, or a coordinator agent that merges updates. Shared memory enables patterns like a research agent writing findings that a writing agent reads, without passing everything through the orchestrator. The main challenge is access control and namespace design.

See also: [22 Multi-Agent Shared Memory](all_techniques/22_multi_agent_shared_memory/README.md)

### Q: What is temporal memory and how does it differ from forgetting/decay?

**A:** Temporal memory attaches timestamps to every memory and uses recency-weighted scoring during retrieval. Newer memories get higher scores. Older memories are still retrievable but rank lower. Forgetting and decay goes further: it reduces importance scores over time and permanently deletes memories that fall below a threshold. The key difference is that temporal memory is non-destructive (old memories stay in the store), while forgetting and decay is destructive (old memories get pruned). Use temporal memory when you want recency bias without data loss. Use forgetting and decay when unbounded growth is a problem and you need automatic cleanup.

See also: [18 Temporal Memory](all_techniques/18_temporal_memory/README.md), [19 Forgetting and Decay](all_techniques/19_forgetting_and_decay/README.md)

### Q: What is hierarchical memory and when do I need multiple tiers?

**A:** Hierarchical memory organizes data into hot (in-context), warm (fast retrieval from cache or small index), and cold (archival storage for rarely accessed memories) tiers. Memories are promoted to hotter tiers on access and demoted when idle. You need multiple tiers when your total memory exceeds what a single store can serve at low latency. For example, if you have 10 million memories but only 10k are accessed regularly, keeping all of them in a high-performance index wastes resources. Tiering lets you optimize cost and latency per access frequency band. Most agents with under 100k total memories do not need tiers.

See also: [13 Hierarchical Memory Layers](all_techniques/13_hierarchical_memory_layers/README.md)

### Q: How do I use memory with tool-calling agents?

**A:** Expose memory operations (save, search, update, delete) as tools the agent can call. The agent decides when to save a fact, when to search for past information, and when to update or delete stale entries. This gives the agent full control over its memory lifecycle. The risk is that the agent may forget to save important facts or may over-save noisy details. Mitigate this by adding a system prompt instruction like "After learning a new user preference, always call the save_memory tool." You can also run automatic extraction in parallel as a safety net for facts the agent misses.

See also: [23 Memory with Tools](all_techniques/23_memory_with_tools/README.md)

### Q: What is the best way to chunk conversations for memory storage?

**A:** Three common strategies: (1) **Per-turn**: store each user-assistant exchange as one memory. Simple but creates many small entries. (2) **Per-topic**: detect topic shifts and group consecutive turns into topic-based chunks. Better for retrieval but requires a topic detector. (3) **Fixed token window**: split the conversation into chunks of N tokens (typically 200 to 500) with overlap. Predictable sizing but may split mid-thought. For vector store memory, per-turn or per-topic chunking with 200 to 500 tokens per chunk works well. For episodic memory, session-level or topic-level boundaries are more natural. Test retrieval quality with each strategy on your data.

See also: [06 Vector Store Memory](all_techniques/06_vector_store_memory/README.md), [09 Episodic Memory](all_techniques/09_episodic_memory/README.md)

### Q: Can I use agent memory with non-chat use cases like code generation or data analysis?

**A:** Yes. Memory is useful any time an agent performs multi-step tasks where later steps depend on earlier ones. A code-generation agent can use procedural memory to recall successful code patterns and self-reflection memory to avoid past bugs. A data-analysis agent can use entity memory to track dataset schemas and semantic memory to remember insights from previous queries. The techniques are the same. The content changes: instead of storing chat messages, you store code snippets, query results, schema definitions, or analysis conclusions. Memory-augmented agents outperform memoryless ones on multi-step tasks that span many turns.

See also: [11 Procedural Memory](all_techniques/11_procedural_memory/README.md), [16 Self-Reflection Memory](all_techniques/16_self_reflection_memory/README.md)

### Q: What is LongMemEval and how does it compare to LoCoMo?

**A:** LongMemEval is a benchmark that tests long-term memory with 500+ questions across five categories: information extraction, multi-session reasoning, temporal reasoning, knowledge update, and abstention (knowing when to say "I don't know"). LoCoMo focuses on conversation memory with 10 long dialogues. LongMemEval covers a broader range of memory tasks. LoCoMo is better for testing conversation-specific memory patterns. Use both if you want a comprehensive evaluation. LoCoMo is cheaper to run ($5 to $15 per full eval). LongMemEval can cost more depending on the number of test cases you evaluate.

See also: [29 Memory Benchmarks / LoCoMo](all_techniques/29_memory_benchmarks_LoCoMo/README.md)
