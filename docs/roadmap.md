# Project Roadmap

> **This is the original planning document that guided construction.** For the current state of the project, see [../ROADMAP.md](../ROADMAP.md). The phase statuses below are historical.


This document outlines the planned phases for the Agent Memory Techniques repository. Each phase builds on the previous one. We progress from foundational notebooks through cognitive architectures, framework integrations, and production-grade evaluation.

**Current status:** Phase 1 (in progress).

---

## Phase 1: Core Techniques (Techniques 01-11): Foundation Notebooks

**Status: In Progress**

The foundation phase covers the essential building blocks of agent memory. These techniques handle short-term conversation management and long-term persistent storage. They're prerequisites for everything that follows.

### Short-Term Memory (01-05)

| # | Technique | Status | Description |
|---|-----------|--------|-------------|
| 01 | Conversation Buffer Memory | Folder created | Full conversation history storage |
| 02 | Sliding Window Memory | Folder created | Last-k message windowing |
| 03 | Summary Memory | Folder created | LLM-generated conversation summaries |
| 04 | Summary Buffer Memory | Folder created | Hybrid summary + recent messages |
| 05 | Token Buffer Memory | Folder created | Token-budget-aware message trimming |

### Long-Term Memory (06-11)

| # | Technique | Status | Description |
|---|-----------|--------|-------------|
| 06 | Vector Store Memory | Folder created | Semantic retrieval with embeddings |
| 07 | Entity Memory | Folder created | Structured entity extraction and tracking |
| 08 | Knowledge Graph Memory | Folder created | Graph-based relationship modeling |
| 09 | Episodic Memory | Folder created | Temporal episode storage and recall |
| 10 | Semantic Memory | Folder created | Generalized fact extraction and storage |
| 11 | Procedural Memory | Folder created | Learned procedures and workflow storage |

### Phase 1 Deliverables

- [ ] Complete Jupyter notebook for each technique (01-11) with runnable code
- [ ] README with concept explanation, architecture diagram, and API reference for each technique
- [ ] Shared utility functions in `utils/memory_utils.py`
- [ ] Consistent notebook structure: Introduction, Concept, Implementation, Demo, Exercises
- [ ] All notebooks tested with OpenAI GPT-4o-mini and at least one open-source alternative

### Phase 1 Milestones

- **M1.1:** Techniques 01-05 (short-term memory) complete with notebooks
- **M1.2:** Techniques 06-08 (vector store, entity, knowledge graph) complete
- **M1.3:** Techniques 09-11 (episodic, semantic, procedural) complete
- **M1.4:** Phase 1 review and polish pass

---

## Phase 2: Cognitive Architectures (Techniques 12-19)

**Status: Planned**

This phase implements advanced patterns inspired by cognitive science research. These techniques build on the Phase 1 foundation. They combine multiple memory stores with intelligent management policies.

| # | Technique | Dependencies | Description |
|---|-----------|-------------|-------------|
| 12 | Working Memory & Context Window | 01, 05 | Token budget management, priority-based context curation |
| 13 | Hierarchical Memory Layers | 06, 12 | Hot/warm/cold tiering with promotion and demotion |
| 14 | Memory Consolidation | 09, 10 | Episode merging, fact strengthening, contradiction resolution |
| 15 | Memory Compaction | 03, 10, 14 | Progressive summarization, deduplication, compression |
| 16 | Self-Reflection Memory | 09, 10 | Agent-generated meta-observations about its own behavior |
| 17 | Memory Routing | 09, 10, 11 | Content classification and store-directed read/write routing |
| 18 | Temporal Memory | 09, 06 | Time-aware storage, recency weighting, temporal queries |
| 19 | Forgetting & Decay | 06, 13 | Exponential decay, access-frequency scoring, pruning |

### Phase 2 Deliverables

- [ ] Complete Jupyter notebook for each technique (12-19)
- [ ] Architecture diagrams showing how cognitive components interact
- [ ] A "mini cognitive architecture" integration notebook combining techniques 12, 14, 17, and 19
- [ ] Performance comparison: cognitive architecture vs. single vector store on multi-session conversations

### Phase 2 Milestones

- **M2.1:** Techniques 12-13 (working memory, hierarchical layers) complete
- **M2.2:** Techniques 14-15 (consolidation, compaction) complete
- **M2.3:** Techniques 16-17 (reflection, routing) complete
- **M2.4:** Techniques 18-19 (temporal, forgetting) complete
- **M2.5:** Integration notebook and phase review

---

## Phase 3: Framework Integrations (Techniques 24-27)

**Status: Planned**

This phase provides hands-on integration guides for the leading agent memory frameworks. Each notebook walks through setup and core usage patterns. It also compares the framework approach with the from-scratch implementations from Phases 1 and 2.

| # | Technique | Framework | Key Features Covered |
|---|-----------|-----------|---------------------|
| 24 | Graph Memory with Graphiti | Zep Graphiti | Episode ingestion, temporal knowledge graphs, entity resolution, graph-based retrieval |
| 25 | Mem0 Patterns | Mem0 | Automatic memory extraction, user-scoped storage, search API, memory lifecycle |
| 26 | Letta (MemGPT) Patterns | Letta | Core/recall/archival memory, inner monologue, heartbeat loop, self-editing memory, memory pressure |
| 27 | Zep Memory | Zep | Dialog classification, entity extraction, temporal knowledge graph, session management |

### Phase 3 Deliverables

- [ ] Complete Jupyter notebook for each framework integration (24-27)
- [ ] Docker Compose files for local framework deployment where applicable
- [ ] Feature comparison matrix: Mem0 vs. Letta vs. Zep vs. Graphiti
- [ ] Migration guide: how to move from a from-scratch implementation to a managed framework
- [ ] Cost analysis: self-hosted vs. managed service for each framework

### Phase 3 Milestones

- **M3.1:** Technique 25 (Mem0) complete (chosen first because it has the simplest setup)
- **M3.2:** Technique 26 (Letta/MemGPT) complete
- **M3.3:** Techniques 24, 27 (Graphiti, Zep) complete
- **M3.4:** Comparison matrix and migration guide published

---

## Phase 4: Evaluation & Production (Techniques 28-30)

**Status: Planned**

This phase covers memory quality measurement and production deployment. It also includes the retrieval, cross-session, multi-agent, and tool-use techniques (20-23). These bridge the gap between individual techniques and production systems.

### Retrieval & Multi-Agent (20-23)

| # | Technique | Description |
|---|-----------|-------------|
| 20 | Memory Retrieval Patterns | Semantic, temporal, hybrid, MMR, re-ranking comparison |
| 21 | Cross-Session Memory | State serialization, session management, returning user handling |
| 22 | Multi-Agent Shared Memory | Shared stores, message passing, consensus protocols |
| 23 | Memory with Tools | Memory-as-a-tool pattern with save/search/forget functions |

### Evaluation & Production (28-30)

| # | Technique | Description |
|---|-----------|-------------|
| 28 | Memory Evaluation | Retrieval precision/recall, staleness, contradictions, temporal accuracy |
| 29 | Memory Benchmarks (LoCoMo) | Running LoCoMo and LongMemEval benchmarks against your system |
| 30 | Production Memory Patterns | Caching, TTLs, sharding, backup, GDPR, observability, cost optimization |

### Phase 4 Deliverables

- [ ] Complete Jupyter notebooks for techniques 20-23 and 28-30
- [ ] Reusable evaluation harness that can benchmark any memory implementation
- [ ] LoCoMo and LongMemEval runner scripts with result visualization
- [ ] Production deployment guide with Docker Compose templates
- [ ] Cost modeling spreadsheet for different memory architectures at various scales
- [ ] Privacy compliance checklist (GDPR, CCPA, SOC 2 considerations)

### Phase 4 Milestones

- **M4.1:** Techniques 20-23 (retrieval, cross-session, multi-agent, tools) complete
- **M4.2:** Technique 28 (evaluation harness) complete
- **M4.3:** Technique 29 (benchmarks) complete
- **M4.4:** Technique 30 (production patterns) complete
- **M4.5:** End-to-end integration test: build, evaluate, and deploy a complete memory system

---

## Phase 5: Community Contributions and Advanced Topics

**Status: Future**

This phase opens the repository to community contributions. It also explores emerging topics in agent memory.

### Community Contribution Areas

- **New technique implementations:** Community members implement notebooks for techniques from Phases 1-4.
- **Alternative framework integrations:** LlamaIndex memory modules, AutoGen memory, CrewAI memory, custom solutions.
- **Language ports:** Implementations in TypeScript/JavaScript, Rust, Go for non-Python ecosystems.
- **Benchmark contributions:** New evaluation datasets, domain-specific benchmarks, adversarial memory tests.
- **Case studies:** Real-world production memory systems, lessons learned, failure modes.

### Advanced Topics Under Consideration

We may add these topics as notebooks beyond the initial 30, depending on community interest and the evolving landscape.

| Topic | Description | Why It Matters |
|-------|-------------|---------------|
| **Memory for multimodal agents** | Storing and retrieving image, audio, and video memories alongside text. Multimodal embeddings, vision-language memory stores, cross-modal retrieval. | As agents become multimodal, memory systems need to handle non-text data natively. |
| **Memory in agentic coding assistants** | How tools like Claude Code, Cursor, GitHub Copilot Workspace, and Devin manage memory across coding sessions. Project context, code understanding, user preference learning, cross-file reasoning. | Coding assistants are the most widely deployed agents in 2026. Their memory needs are unique. |
| **Federated memory across organizations** | Sharing memory patterns across organizational boundaries while preserving privacy. Federated learning for memory models, differential privacy in memory stores, secure multi-party computation for shared entities. | Enterprise agents increasingly need to collaborate across company boundaries. |
| **Memory for autonomous agents** | Long-horizon memory for agents that run for hours or days without human interaction. Self-monitoring, drift detection, memory corruption recovery, autonomous consolidation. | As agents become more autonomous, their memory systems must be self-maintaining. |
| **Neuromorphic memory patterns** | Bio-inspired memory architectures: Hebbian learning ("neurons that fire together wire together"), sparse distributed memory, complementary learning systems (hippocampus + neocortex model). | These patterns may unlock more efficient and reliable memory systems. |
| **Memory-aware fine-tuning** | Using memory interaction logs to fine-tune the base model for better memory operations. Learning to summarize, extract, route, and retrieve through training rather than prompting. | Prompting-based memory has limits. Fine-tuning may break through performance ceilings. |
| **Memory security and adversarial resilience** | Protecting memory from prompt injection attacks that attempt to poison stored memories, extract private information, or manipulate entity records. | As agents handle sensitive data, memory security becomes a critical concern. |

---

## Timeline (Estimated)

This timeline assumes one primary author plus community contributions. Dates are approximate.

```
2026 Q2:  Phase 1 - Core techniques (01-11)
2026 Q3:  Phase 2 - Cognitive architectures (12-19)
2026 Q3:  Phase 3 - Framework integrations (24-27)
2026 Q4:  Phase 4 - Evaluation & production (20-23, 28-30)
2027 Q1+: Phase 5 - Community contributions and advanced topics
```

---

## How to Contribute

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines. The highest-impact contributions right now are:

1. **Implement a Phase 1 notebook.** Pick any technique from 01-11, follow the README outline in its folder, and submit a PR with a complete Jupyter notebook.
2. **Review existing notebooks.** Test them, find bugs, suggest improvements.
3. **Add architecture diagrams.** Mermaid or ASCII diagrams that show memory data flow for each technique.
4. **Propose new techniques.** Open an issue describing a memory technique not covered in the current 30, with references to papers or implementations.

---

## Versioning

This roadmap is a living document. We track major updates here:

| Date | Change |
|------|--------|
| 2026-04-19 | Initial roadmap created with 5 phases |

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=docs--roadmap)
