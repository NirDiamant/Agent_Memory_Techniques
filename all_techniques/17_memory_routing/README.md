# Memory Routing

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/17_memory_routing/memory_routing.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

## 📖 At a Glance

| Difficulty | Time | Prerequisites |
|------------|------|---------------|
| Intermediate | ~35 min | Python 3.8+, `OPENAI_API_KEY`, understanding of 06 Vector Store Memory recommended |

This technique is for developers who manage multiple memory stores and need an intelligent router to direct queries to the right backend.

## TL;DR

- **What it is:** **Memory Routing** classifies each memory operation by content type and routes it to the correct specialized store (episodic, semantic, or procedural).
- **When you need it:** You run multiple memory backends and need an intelligent dispatcher instead of querying all stores on every request.
- **The trade-off:** Every operation triggers a 200-500ms LLM classification call, and misrouting sends data to the wrong store silently.
- **Closest alternative in this repo:** 13 Hierarchical Memory Layers routes by access frequency across tiers, not by content type across stores.

## Overview

Imagine a library with separate rooms: one for history books, one for cookbooks, one for repair manuals. When a visitor asks a question, the librarian doesn't search every room. They figure out what kind of question it is, then walk to the right room. Memory Routing is the agent memory technique that gives an LLM agent this same dispatch ability. It classifies each read or write operation by content type: episodic, semantic, or procedural. Then it directs the operation to the correct specialized memory store. You'll need it when building modular memory architectures for complex agents like personal assistants or multi-domain chatbots.

Without routing, agents dump everything into a single large store and lose the benefits of specialization. Good routing enables modular memory architectures. You can add new memory types without restructuring the system.

**Keywords:** agent memory, LLM agent, memory routing, memory type classification, episodic memory, semantic memory, procedural memory, modular memory architecture, memory dispatcher

## Key Concepts

- **Memory type classification**: Sorting content into categories like episodic (events), semantic (facts), or procedural (how-to steps). This guides where to store and retrieve it.
- **Read routing**: Picking which store(s) to query based on a question's intent. "What happened yesterday?" routes to episodic. "What's our rate limit?" routes to semantic.
- **Write routing**: Directing new content to the correct store with the right formatting.
- **Fallback strategies**: Default behavior when the router is uncertain. For example: search all stores and merge results.

## Architecture

<p align="center">
  <img src="../../images/diagrams/17_memory_routing.svg" alt="Memory Routing architecture diagram" width="720"/>
</p>

---

## How It Works

1. The router sends incoming content or query text to an LLM classifier (a model that picks the right category).
2. The classifier returns one or more memory types: episodic, semantic, or procedural.
3. For writes, the router creates a memory entry and stores it in each matching specialized store.
4. For reads, the router searches only the classified store(s) and scores results by keyword overlap.
5. Results from multiple stores are merged and deduplicated (removing repeated entries) before returning.
6. For ambiguous queries, a fallback mode searches all stores at once and merges the results.

## What the Notebook Covers

The [notebook](./memory_routing.ipynb) builds a complete memory routing system from scratch:

1. **Data model**: A `MemoryType` enum and `MemoryEntry` dataclass for typed memory entries.
2. **Specialized stores**: Three `MemoryStore` instances (episodic, semantic, procedural), each with keyword-based search.
3. **LLM-powered router**: A `MemoryRouter` class that uses GPT-4o-mini to classify content and queries, then routes operations to the right store.
4. **Write pipeline**: Classifies incoming content and stores it in the matching store(s).
5. **Read pipeline**: Classifies queries, searches the relevant store(s), and returns merged results.
6. **Fallback**: A fan-out method that searches all stores for ambiguous queries.
7. **Routing log**: Every decision is recorded for debugging and classifier improvement.

## When to Use

- Agents with multiple specialized memory stores that need unified access.
- Systems where different memory types have different storage and retrieval needs.
- Architectures designed for extensibility, where new memory types may appear over time.

## Limitations

- Every read or write triggers an LLM classification call. This adds 200-500ms of latency per operation, which accumulates in high-throughput systems.
- If the classifier picks the wrong memory type, data lands in the wrong store. You get no results because the system never searches where the data actually lives.
- Content that spans multiple types (like "In yesterday's meeting, we set the refund window to 14 days") needs multi-label classification. Without it, the router misses relevant results.
- The LLM classifier has no confidence score. It makes hard routing decisions without signaling when it's uncertain, so you can't tell when to trigger the fallback.
- The fallback mode (searching all stores) gets expensive as the number of stores and entries grows.

## FAQ

### Q: What is Memory Routing in agent memory?

**A:** Memory Routing classifies each memory operation by content type and routes it to the correct specialized store. Instead of putting everything in one memory, a router decides: "this is a fact" (send to semantic memory), "this is an experience" (send to episodic memory), "this is a procedure" (send to procedural memory). The router can use an LLM classifier, keyword rules, or embedding-based clustering. It acts as the traffic controller for a multi-store memory architecture.

### Q: When should I use Memory Routing instead of Hierarchical Memory Layers?

**A:** Use Memory Routing when you have multiple memory stores organized by content type (semantic, episodic, procedural). Hierarchical Memory Layers (technique 13) routes by access frequency across hot/warm/cold tiers within a single store. Routing is about "what kind of memory is this?" while hierarchy is about "how often do we access this?" If your agent has distinct memory types that need different storage and retrieval strategies, routing is the right pattern. Many production systems use both.

### Q: What are the limits or failure modes of Memory Routing?

**A:** The router can misclassify content, sending a fact to episodic memory or a procedure to semantic memory. LLM-based routing adds latency (100-300ms) per operation. Rule-based routing is faster but brittle and misses edge cases. Ambiguous content (a fact embedded in a story) may not have a clear single destination. If the router fails silently, memories end up in the wrong store and become unretrievable through the expected query path. Testing coverage for routing logic is essential.

### Q: Can I combine Memory Routing with another memory technique?

**A:** Yes. Memory Routing is inherently a composition pattern. It sits in front of techniques 09 (Episodic Memory), 10 (Semantic Memory), and 11 (Procedural Memory), routing content to each. On the retrieval side, it decides which stores to query for a given request. Add technique 13 (Hierarchical Memory Layers) within each store for access-frequency optimization. This creates a two-dimensional organization: by content type (routing) and by access pattern (hierarchy).

### Q: What library or framework can I use to skip the implementation work?

**A:** Letta/MemGPT (technique 26) implements routing between core, recall, and archival memory through the agent's own function calls. Zep (technique 27) routes between conversation history and knowledge graph storage automatically. No major framework provides a standalone routing class. For custom builds, implement a classifier (LLM-based or rule-based) that tags each memory operation and dispatches it to the appropriate store. The routing logic typically requires 50-150 lines of Python.

## References

- Packer, C., et al. (2023). ["MemGPT: Towards LLMs as Operating Systems."](https://arxiv.org/abs/2310.08560) arXiv:2310.08560.
- Zhang, Z., et al. (2024). ["A Survey on the Memory Mechanism of Large Language Model Based Agents."](https://arxiv.org/abs/2404.13501) arXiv:2404.13501.
- Lewis, P., et al. (2020). ["Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."](https://arxiv.org/abs/2005.11401) arXiv:2005.11401.
- Weston, J., Chopra, S., & Bordes, A. (2015). ["Memory Networks."](https://arxiv.org/abs/1410.3916) arXiv:1410.3916.
- Park, J. S., et al. (2023). ["Generative Agents: Interactive Simulacra of Human Behavior."](https://arxiv.org/abs/2304.03442) arXiv:2304.03442.

## Related Techniques

- [**13 Hierarchical Memory Layers**](../13_hierarchical_memory_layers/) - Routing directs by content type. Hierarchical layers add a second axis: routing across hot, warm, and cold storage tiers.
- [**09 Episodic Memory**](../09_episodic_memory/) - One of the three specialized stores a router dispatches to. Stores event-based "what happened" memories.
- [**10 Semantic Memory**](../10_semantic_memory/) - The factual knowledge store in a routed architecture. Handles "what is true" queries.
- [**26 Letta/MemGPT Patterns**](../26_letta_memgpt_patterns/) - Implements built-in memory routing between core memory and archival storage.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--17-memory-routing--readme)
