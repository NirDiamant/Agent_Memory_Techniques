# Compare All 30 Memory Techniques

Single-table comparison across families. Skim columns to filter by your constraint, then click into the technique. Cross-linked from the main [README](../README.md#-which-technique-do-i-need).

A single table. Skim the columns to filter by your constraint, then click into the technique.

| #  | Technique | Family | Persistence | Retrieval | Token Cost vs. History | Best For |
|----|-----------|--------|-------------|-----------|------------------------|----------|
| 01 | Conversation Buffer | Short-term | None | Append-only | Linear (grows forever) | Prototypes; short chats |
| 02 | Sliding Window | Short-term | None | Last k turns | Constant (fixed window) | Bounded chat budgets |
| 03 | Summary | Short-term | None | Compressed text blob | Sub-linear (summary cap) | Long chats where gist is enough |
| 04 | Summary Buffer | Short-term | None | Summary + recent | Sub-linear | Long chats where recent detail matters |
| 05 | Token Buffer | Short-term | None | Token-trimmed history | Constant (strict budget) | Hard token caps |
| 06 | Vector Store | Long-term | Disk / DB | Semantic similarity (Top-K) | Constant per call (K items) | Recall by meaning across many turns |
| 07 | Entity | Long-term | Disk (JSON) | Entity-name lookup | Tiny (per-entity record) | Track facts about people, places, things |
| 08 | Knowledge Graph | Long-term | Graph DB | Subgraph (1-2 hop) | Tiny (subgraph) | Multi-hop relational questions |
| 09 | Episodic | Long-term | Disk / DB | Time + semantic | Tiny (episode summary) | "What happened last week?" |
| 10 | Semantic | Long-term | Disk / DB | Semantic similarity over facts | Tiny (top facts) | Stable knowledge that survives sessions |
| 11 | Procedural | Long-term | Disk / DB | Task-type matching | Tiny (one procedure) | Skip re-deriving plans |
| 12 | Working Memory | Cognitive | None | Salience-ranked window | Bounded (priority queue) | Many simultaneous attention items |
| 13 | Hierarchical Layers | Cognitive | Multi-tier | Cache fall-through | Variable | Tame unbounded memory size |
| 14 | Consolidation | Cognitive | Disk / DB | Off-path background job | One LLM job per cycle | Reduce store noise over time |
| 15 | Compaction | Cognitive | Multi-level | Level-selected | Tiny if you pick L2/L3 | Most queries do not need full detail |
| 16 | Self-Reflection | Cognitive | Disk / DB | Task-type retrieval | Tiny (1 reflection) | Improve from past failures |
| 17 | Memory Routing | Cognitive | Routes to others | Classifier-driven | Depends on target store | Decide which memory store to write/read |
| 18 | Temporal | Cognitive | Disk / DB | Time + semantic | Tiny | When facts have a "valid from / valid to" |
| 19 | Forgetting & Decay | Cognitive | Disk / DB | Strength-weighted | Shrinks over time | Bound long-running stores |
| 20 | Retrieval Patterns | Retrieval | Disk / DB | Hybrid (BM25 + dense + rerank + MMR) | Configurable | Quality retrieval at scale |
| 21 | Cross-Session | Retrieval | Disk / DB | Per-user isolated | Constant per user | Personal assistants |
| 22 | Multi-Agent Shared | Retrieval | Shared store | Permissioned | Constant | Several agents collaborate |
| 23 | Memory as Tools | Retrieval | Disk / DB | Agent invokes tools | Tool call latency | Agent decides when to read/write |
| 24 | Graphiti | Framework | Neo4j | Graph + temporal | Tiny | Production temporal knowledge graphs |
| 25 | Mem0 | Framework | Mem0 cloud | Managed retrieval | API-priced | Drop-in personalization |
| 26 | Letta / MemGPT | Framework | Letta server | Three-tier (core/recall/archival) | Bounded | Long-running self-editing agents |
| 27 | Zep | Framework | Zep cloud / OSS | Temporal KG | API-priced | Conversational memory at scale |
| 28 | Evaluation | Production | None | Methodology | None | Measure quality before shipping |
| 29 | LoCoMo Benchmarks | Production | Benchmark fixtures | Benchmark scoring | None | Compare techniques on standard data |
| 30 | Production Patterns | Production | Tiered hot/warm/cold | Tier-routed | Cost-bounded | Ship to many users reliably |

> **How to read the table.** "Token Cost vs. History" describes how cost scales with the conversation length. "Tiny" means the cost is bounded by the number of items retrieved (K), not by total history. "None" means the row is methodology, not a runtime store.
