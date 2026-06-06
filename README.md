# 🧠 Agent Memory Techniques

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="images/hero_dark.png">
    <img src="images/banner.png" alt="Agent Memory Techniques for LLMs: 30 runnable Jupyter notebooks covering every major memory pattern" width="100%"/>
  </picture>
</p>

**Learn every agent memory technique for LLM agents.**

> ⭐  **If you find this useful, please star the repo** so more learners can discover it.

> 🧭  **New here?** Start with [01 Conversation Buffer Memory](all_techniques/01_conversation_buffer_memory/) or pick a [Learning Path](#-learning-paths). Prefer a visual? See the [Decision Tree](#-which-technique-do-i-need) below. 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, working memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production memory patterns.

<p align="center">
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+"></a>
  <a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-Notebook-orange.svg" alt="Jupyter"></a>
  <a href="https://github.com/NirDiamant/Agent_Memory_Techniques/stargazers"><img src="https://img.shields.io/github/stars/NirDiamant/Agent_Memory_Techniques?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/NirDiamant/Agent_Memory_Techniques/issues"><img src="https://img.shields.io/github/issues/NirDiamant/Agent_Memory_Techniques" alt="Issues"></a>
  <a href=".github/CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg" alt="Contributions Welcome"></a>
</p>

---

<p align="center">
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-linkedin&target=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fnir-diamant-759323134%2F&text=LinkedIn"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue" alt="LinkedIn"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-twitter&target=https%3A%2F%2Ftwitter.com%2FNirDiamantAI&text=Twitter"><img src="https://img.shields.io/twitter/follow/NirDiamantAI?label=Follow%20%40NirDiamantAI&style=social" alt="Twitter"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-reddit&target=https%3A%2F%2Fwww.reddit.com%2Fr%2FEducationalAI%2F&text=Reddit"><img src="https://img.shields.io/badge/Reddit-Join%20our%20subreddit-FF4500?style=flat-square&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=social-discord&target=https%3A%2F%2Fdiscord.gg%2FcA6Aa4uyDX&text=Discord"><img src="https://img.shields.io/badge/Discord-Join%20our%20community-7289da?style=flat-square&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=sponsor-github&target=https%3A%2F%2Fgithub.com%2Fsponsors%2FNirDiamant&text=Sponsor"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4" alt="Sponsor"></a>
</p>

## 📖 Go deeper on RAG

<div align="center">

<a href="https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&amp;click=book-buy-gumroad-rag-image&amp;target=https%3A%2F%2Fdiamant-ai.com%2Frag-made-simple%3Fcode%3DRAGKING&amp;retarget=0&amp;text=book-buy-gumroad-rag-image"><img src="images/rag_book_best_seller.png" alt="RAG Made Simple" width="360"></a>

**[RAG Made Simple](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=book-buy-gumroad-rag-cta&target=https%3A%2F%2Fdiamant-ai.com%2Frag-made-simple%3Fcode%3DRAGKING&retarget=0&text=book-buy-gumroad-rag-cta)** - the 400-page visual guide to RAG, by the author of this repo.
Amazon Bestseller in Generative AI · 1,500+ readers · ⭐ 4.6

**[Get it - 33% off with code RAGKING →](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=book-buy-gumroad-rag-cta&target=https%3A%2F%2Fdiamant-ai.com%2Frag-made-simple%3Fcode%3DRAGKING&retarget=0&text=book-buy-gumroad-rag-cta)** · [Read Chapter 1 free](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=free-chapter&target=https%3A%2F%2Fdiamant-ai.com%2Frag-made-simple%2Fchapter-1&retarget=0&text=free-chapter)

</div>


---

## 📫 Stay Updated

<div align="center">
<table>
<tr>
<td align="center">🚀<br><b>Weekly<br>Updates</b></td>
<td align="center">💡<br><b>Expert<br>Insights</b></td>
<td align="center">🎯<br><b>Top 0.1%<br>Content</b></td>
</tr>
</table>

<a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=newsletter-subscribe-button&target=https%3A%2F%2Fdiamantai.substack.com%2F%3Fr%3D336pe4%26utm_campaign%3Dpub-share-checklist&text=Subscribe%20to%20DiamantAI%20Newsletter"><img src="images/subscribe-button.svg" alt="Subscribe to DiamantAI Newsletter"></a>

*Join over 50,000 readers getting clear AI tutorials every week.* ***Subscribers also get early access and a 33% discount on my book.***
</div>

<a href="https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme&click=newsletter-subscribe-image&target=https%3A%2F%2Fdiamantai.substack.com%2F%3Fr%3D336pe4%26utm_campaign%3Dpub-share-checklist&text=DiamantAI%20newsletter"><img src="images/substack_image.png" alt="DiamantAI newsletter"></a>

---

## 💡 Why Agent Memory Matters
> ### 💡 Quick Answer (for search engines and skimmers)
>
> **Agent memory** is the set of techniques that let an LLM-based agent (a system built around a Large Language Model) remember information across turns, sessions, and tasks. Without memory, an agent re-derives context every time and cannot personalize, learn, or maintain coherence over long interactions. This repository documents 30 distinct memory techniques, grouped into six families: short-term context management, long-term storage, cognitive architectures, retrieval and multi-agent patterns, batteries-included frameworks, and production deployment patterns.

Think about a friend who forgets every conversation you've ever had. Every morning you're strangers again. That's what most AI agents are like today.

Every AI agent eventually hits the same wall: **it forgets**.

In 2026, AI agents are everywhere. But most of them still forget what you told them yesterday. Without strong memory, an agent can't keep context across conversations. It can't learn from past chats. It can't build a lasting relationship with you.

The landscape is shifting fast:

- **Anthropic's 7 Layers of Memory** (March 2026): from conversation context to cross-project knowledge, defining the memory hierarchy for Claude Code
- **Mem0**: managed memory layer gaining rapid adoption for personalized AI
- **Letta (MemGPT)**: self-editing memory with inner/outer monologue architecture
- **Zep**: temporal knowledge graphs for long-term agent memory
- **Graphiti**: episodic-to-semantic knowledge graph extraction
- **MemOS & Memori**: memory-as-infrastructure platforms for production agents

But there's no single hands-on guide that teaches you **how each technique works, when to use it, and how to build it yourself**.

That's why this repository exists. **30 techniques. Runnable notebooks. Real code you can use today.**

---

## 🗺️ Taxonomy of Agent Memory Techniques

<p align="center">
  <img src="images/taxonomy.png" alt="Agent memory taxonomy: 30 techniques across 6 families (short-term, long-term, cognitive architectures, retrieval, frameworks, production)" width="720"/>
</p>

The 30 techniques fall into six families. Each family solves a different memory problem. Each technique lives in its own notebook.

| Family | What it solves | Techniques |
|---|---|---|
| **Short-term** | Keep recent turns in memory without filling up the context window. | 01 - 05 |
| **Long-term** | Save knowledge across sessions, users, and time. | 06 - 11 |
| **Cognitive architectures** | Working, hierarchical, and reflective memory systems. | 12 - 19 |
| **Retrieval & routing** | Choose what to recall and when. | 20 - 23 |
| **Frameworks** | Production-ready memory libraries (Mem0, Letta, Zep, Graphiti). | 24 - 27 |
| **Evaluation & production** | Measure, benchmark, and deploy memory. | 28 - 30 |

---

## 🧭 Which Technique Do I Need?

30 techniques grouped by what you are building. Pick the group that matches your goal, then open the technique inside it.

<p align="center">
  <img src="images/decision_tree.svg" alt="Decision tree: which agent memory technique do I need?" width="100%"/>
</p>

<!-- decision-tree-text-fallback -->
**Quick text version:**

- Need to manage the current chat? Start with **01-05** (short-term memory).
- Need to persist across sessions? Start with **06 Vector Store** or **21 Cross-Session Memory**.
- Building a cognitive architecture with multiple stores? See **12-19**.
- Using a framework? Go straight to **24 Graphiti**, **25 Mem0**, **26 Letta**, or **27 Zep**.
- Evaluating or shipping to production? See **28-30**.

**Still not sure?** Start with [01 Conversation Buffer](all_techniques/01_conversation_buffer_memory/). Almost every other technique builds on it.

---

## 📐 Compare Techniques at a Glance

Looking to filter by constraint (persistence, retrieval style, token cost, best-for use case)? See the [side-by-side comparison matrix](docs/comparison.md) covering all 30 techniques in one table.

---

## 📚 All 30 Techniques

<p align="center">
  <img src="images/sections/short_term.png" alt="Short-term memory techniques for LLM agents: conversation buffers, sliding window, summary, token budget" width="100%"/>
</p>

### 🔄 Short-Term Memory (Techniques 1-5)

Manage the conversation inside a single chat.

| # | Technique | Description | Notebook |
|---|-----------|-------------|----------|
| 01 | [Conversation Buffer Memory](all_techniques/01_conversation_buffer_memory/) | Save the full conversation, word for word. The simplest pattern, and the base for everything else. | ✅ [Notebook](all_techniques/01_conversation_buffer_memory/conversation_buffer_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/01_conversation_buffer_memory/conversation_buffer_memory.ipynb) |
| 02 | [Sliding Window Memory](all_techniques/02_sliding_window_memory/) | Keep only the last few messages. You limit the size, but you keep the recent parts. | ✅ [Notebook](all_techniques/02_sliding_window_memory/sliding_window_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/02_sliding_window_memory/sliding_window_memory.ipynb) |
| 03 | [Summary Memory](all_techniques/03_summary_memory/) | Replace old turns with a short summary written by the model. You lose length but keep the meaning. | ✅ [Notebook](all_techniques/03_summary_memory/summary_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/03_summary_memory/summary_memory.ipynb) |
| 04 | [Summary Buffer Memory](all_techniques/04_summary_buffer_memory/) | Summarize older turns, but keep recent messages word for word. You get both. | ✅ [Notebook](all_techniques/04_summary_buffer_memory/summary_buffer_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/04_summary_buffer_memory/summary_buffer_memory.ipynb) |
| 05 | [Token Buffer Memory](all_techniques/05_token_buffer_memory/) | Trim the history to fit a strict token budget. Drop the oldest messages first. | ✅ [Notebook](all_techniques/05_token_buffer_memory/token_buffer_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/05_token_buffer_memory/token_buffer_memory.ipynb) |

<p align="center">
  <img src="images/sections/long_term.png" alt="Long-term memory techniques for LLM agents: vector store, entity, knowledge graph, episodic, semantic, procedural" width="100%"/>
</p>

### 💾 Long-Term Memory (Techniques 6-11)

Storage that survives across sessions and users.

| # | Technique | Description | Notebook |
|---|-----------|-------------|----------|
| 06 | [Vector Store Memory](all_techniques/06_vector_store_memory/) | Turn past messages into vectors (number lists that capture meaning). Search them later by similarity. | ✅ [Notebook](all_techniques/06_vector_store_memory/vector_store_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/06_vector_store_memory/vector_store_memory.ipynb) |
| 07 | [Entity Memory](all_techniques/07_entity_memory/) | Pull out and track facts about people, projects, and preferences. Update them as the conversation grows. | ✅ [Notebook](all_techniques/07_entity_memory/entity_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/07_entity_memory/entity_memory.ipynb) |
| 08 | [Knowledge Graph Memory](all_techniques/08_knowledge_graph_memory/) | Build a graph of how entities connect. Walk the graph to reason over what the agent has learned. | ✅ [Notebook](all_techniques/08_knowledge_graph_memory/knowledge_graph_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/08_knowledge_graph_memory/knowledge_graph_memory.ipynb) |
| 09 | [Episodic Memory](all_techniques/09_episodic_memory/) | Store complete interactions with when-and-where context. Good for "what happened when" questions. | ✅ [Notebook](all_techniques/09_episodic_memory/episodic_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/09_episodic_memory/episodic_memory.ipynb) |
| 10 | [Semantic Memory](all_techniques/10_semantic_memory/) | Pull general facts out of interactions. Store them on their own, away from the raw episodes. | ✅ [Notebook](all_techniques/10_semantic_memory/semantic_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/10_semantic_memory/semantic_memory.ipynb) |
| 11 | [Procedural Memory](all_techniques/11_procedural_memory/) | Capture "how-to" knowledge: the procedures and workflows the agent picks up over time. | ✅ [Notebook](all_techniques/11_procedural_memory/procedural_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/11_procedural_memory/procedural_memory.ipynb) |

<p align="center">
  <img src="images/sections/cognitive.png" alt="Cognitive architecture memory patterns: working memory, hierarchical layers, consolidation, compaction, self-reflection, routing, temporal, forgetting" width="100%"/>
</p>

### 🧩 Cognitive Architectures (Techniques 12-19)

Patterns borrowed from how humans remember.

| # | Technique | Description | Notebook |
|---|-----------|-------------|----------|
| 12 | [Working Memory & Context Window](all_techniques/12_working_memory_context_window/) | Manage the agent's limited attention. Prioritize, pin, and evict context on the fly. | ✅ [Notebook](all_techniques/12_working_memory_context_window/working_memory_context_window.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/12_working_memory_context_window/working_memory_context_window.ipynb) |
| 13 | [Hierarchical Memory Layers](all_techniques/13_hierarchical_memory_layers/) | Tiered storage with hot, warm, and cold layers. Promote and demote items as they age. | ✅ [Notebook](all_techniques/13_hierarchical_memory_layers/hierarchical_memory_layers.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/13_hierarchical_memory_layers/hierarchical_memory_layers.ipynb) |
| 14 | [Memory Consolidation](all_techniques/14_memory_consolidation/) | Merge, deduplicate, and strengthen memories. Inspired by how the brain consolidates during sleep. | ✅ [Notebook](all_techniques/14_memory_consolidation/memory_consolidation.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/14_memory_consolidation/memory_consolidation.ipynb) |
| 15 | [Memory Compaction](all_techniques/15_memory_compaction/) | Compress stored memories with summaries, entity extraction, or distillation. Save storage and tokens. | ✅ [Notebook](all_techniques/15_memory_compaction/memory_compaction.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/15_memory_compaction/memory_compaction.ipynb) |
| 16 | [Self-Reflection Memory](all_techniques/16_self_reflection_memory/) | The agent looks back at its own actions. It writes notes on what worked, and uses them next time. | ✅ [Notebook](all_techniques/16_self_reflection_memory/self_reflection_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/16_self_reflection_memory/self_reflection_memory.ipynb) |
| 17 | [Memory Routing](all_techniques/17_memory_routing/) | Pick the right memory store to read from or write to. Route by content type and intent. | ✅ [Notebook](all_techniques/17_memory_routing/memory_routing.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/17_memory_routing/memory_routing.ipynb) |
| 18 | [Temporal Memory](all_techniques/18_temporal_memory/) | Attach timestamps to memories. Retrieve with time awareness and weight recent items higher. | ✅ [Notebook](all_techniques/18_temporal_memory/temporal_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/18_temporal_memory/temporal_memory.ipynb) |
| 19 | [Forgetting & Decay](all_techniques/19_forgetting_and_decay/) | Forget on purpose. Use decay, access counts, or relevance to prune. | ✅ [Notebook](all_techniques/19_forgetting_and_decay/forgetting_and_decay.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/19_forgetting_and_decay/forgetting_and_decay.ipynb) |

<p align="center">
  <img src="images/sections/retrieval.png" alt="Memory retrieval and multi-agent patterns: retrieval patterns, cross-session memory, multi-agent shared memory, memory as tools" width="100%"/>
</p>

### 🔍 Retrieval & Multi-Agent (Techniques 20-23)

How agents find and share memories.

| # | Technique | Description | Notebook |
|---|-----------|-------------|----------|
| 20 | [Memory Retrieval Patterns](all_techniques/20_memory_retrieval_patterns/) | Compare retrieval strategies: semantic search, recency, hybrid scoring, diversity, and re-ranking. | ✅ [Notebook](all_techniques/20_memory_retrieval_patterns/memory_retrieval_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/20_memory_retrieval_patterns/memory_retrieval_patterns.ipynb) |
| 21 | [Cross-Session Memory](all_techniques/21_cross_session_memory/) | Save and reload agent state across sessions. The user picks up where they left off. | ✅ [Notebook](all_techniques/21_cross_session_memory/cross_session_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/21_cross_session_memory/cross_session_memory.ipynb) |
| 22 | [Multi-Agent Shared Memory](all_techniques/22_multi_agent_shared_memory/) | Shared stores, message passing, and agreement protocols for multi-agent teams. | ✅ [Notebook](all_techniques/22_multi_agent_shared_memory/multi_agent_shared_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/22_multi_agent_shared_memory/multi_agent_shared_memory.ipynb) |
| 23 | [Memory with Tools](all_techniques/23_memory_with_tools/) | Give the agent memory tools it can call: save, search, forget. Treated like any other tool. | ✅ [Notebook](all_techniques/23_memory_with_tools/memory_with_tools.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/23_memory_with_tools/memory_with_tools.ipynb) |

<p align="center">
  <img src="images/sections/frameworks.png" alt="Agent memory frameworks and libraries: Graphiti, Mem0, Letta (MemGPT), Zep" width="100%"/>
</p>

### 🔧 Frameworks & Platforms (Techniques 24-27)

Work with the leading memory frameworks, hands-on.

| # | Technique | Description | Notebook |
|---|-----------|-------------|----------|
| 24 | [Graph Memory with Graphiti](all_techniques/24_graph_memory_graphiti/) | Use Zep's Graphiti to build time-aware knowledge graphs from chat. Extract episodes and general facts. | ✅ [Notebook](all_techniques/24_graph_memory_graphiti/graph_memory_graphiti.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/24_graph_memory_graphiti/graph_memory_graphiti.ipynb) |
| 25 | [Mem0 Patterns](all_techniques/25_mem0_patterns/) | Use Mem0's managed memory layer. It handles extracting, storing, and fetching user-specific memories. | ✅ [Notebook](all_techniques/25_mem0_patterns/mem0_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/25_mem0_patterns/mem0_patterns.ipynb) |
| 26 | [Letta (MemGPT) Patterns](all_techniques/26_letta_memgpt_patterns/) | Build MemGPT's self-editing memory. Covers inner monologue, heartbeat events, and memory pressure. | ✅ [Notebook](all_techniques/26_letta_memgpt_patterns/letta_memgpt_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/26_letta_memgpt_patterns/letta_memgpt_patterns.ipynb) |
| 27 | [Zep Memory](all_techniques/27_zep_memory/) | Use Zep for dialog classification, entity extraction, and time-aware graphs. Built for production. | ✅ [Notebook](all_techniques/27_zep_memory/zep_memory.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/27_zep_memory/zep_memory.ipynb) |

<p align="center">
  <img src="images/sections/evaluation.png" alt="Agent memory evaluation and production: memory evaluation, LoCoMo and LongMemEval benchmarks, production deployment patterns" width="100%"/>
</p>

### 📊 Evaluation & Production (Techniques 28-30)

Measure your memory. Then ship it.

| # | Technique | Description | Notebook |
|---|-----------|-------------|----------|
| 28 | [Memory Evaluation](all_techniques/28_memory_evaluation/) | Measure memory quality. Check retrieval precision and recall, staleness, contradictions, and user satisfaction. | ✅ [Notebook](all_techniques/28_memory_evaluation/memory_evaluation.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/28_memory_evaluation/memory_evaluation.ipynb) |
| 29 | [Memory Benchmarks (LoCoMo)](all_techniques/29_memory_benchmarks_LoCoMo/) | Run your memory against LoCoMo and LongMemEval benchmarks. See how it does over long conversations. | ✅ [Notebook](all_techniques/29_memory_benchmarks_LoCoMo/memory_benchmarks_locomo.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/29_memory_benchmarks_LoCoMo/memory_benchmarks_locomo.ipynb) |
| 30 | [Production Memory Patterns](all_techniques/30_production_memory_patterns/) | Run memory at scale. Caching, TTLs (time-to-live), sharding, backups, GDPR, and observability. | ✅ [Notebook](all_techniques/30_production_memory_patterns/production_memory_patterns.ipynb) · [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/30_production_memory_patterns/production_memory_patterns.ipynb) |

---

## 🎯 Learning Paths

### Beginner: Foundations

New to agent memory? Start here. These are the building blocks.

```
01 Conversation Buffer → 02 Sliding Window → 03 Summary Memory →
05 Token Buffer → 06 Vector Store Memory → 21 Cross-Session Memory
```

### Intermediate: Structured Memory

Ready for more? Add entities, graphs, and smarter retrieval.

```
07 Entity Memory → 08 Knowledge Graph → 09 Episodic Memory →
10 Semantic Memory → 20 Retrieval Patterns → 22 Multi-Agent Shared Memory
```

### Advanced: Cognitive Architectures

Build human-inspired memory patterns for advanced agents.

```
12 Working Memory → 13 Hierarchical Layers → 14 Consolidation →
16 Self-Reflection → 17 Memory Routing → 19 Forgetting & Decay
```

### Practitioner: Frameworks & Production

Connect to production tools and measure what you've built.

```
25 Mem0 → 26 Letta/MemGPT → 24 Graphiti → 27 Zep →
28 Evaluation → 29 Benchmarks → 30 Production Patterns
```

---

## 🚀 Quick Start

> 💡  **Prefer not to install anything?** Every notebook renders on GitHub directly. Click a technique in the table above to read it in your browser. Or use the Colab badges to run it in the cloud.

```bash
# Clone the repository
git clone https://github.com/NirDiamant/Agent_Memory_Techniques.git
cd Agent_Memory_Techniques

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your API keys
cp .env.example .env
# Edit .env with your OPENAI_API_KEY and/or ANTHROPIC_API_KEY

# Launch Jupyter and start with the first technique
jupyter notebook all_techniques/01_conversation_buffer_memory/
```

---

## 📁 Project Structure

```
Agent_Memory_Techniques/
├── README.md                           # You are here
├── ROADMAP.md                          # Current state and what's next
├── LICENSE                             # Apache 2.0
├── CITATION.cff                        # How to cite this work
├── requirements.txt                    # Python dependencies
├── .env.example                        # API key template
├── llms.txt                            # LLM-discoverability index
│
├── all_techniques/                     # 30 technique folders, each with notebook + README
│   ├── 01_conversation_buffer_memory/
│   ├── 02_sliding_window_memory/
│   ├── ...
│   └── 30_production_memory_patterns/
│
├── docs/                               # Project documentation
│   ├── architecture.md                 # Memory system design patterns
│   ├── comparison.md                   # Side-by-side comparison of all 30 techniques
│   ├── glossary.md                     # Key terms and definitions
│   ├── learning_path.md                # Detailed learning path guide
│   ├── topics.md                       # Keyword index
│   ├── roadmap.md                      # Original planning archive
│   ├── FAQ.md                          # Frequently asked questions
│   └── CONTENT_STANDARDS.md            # Writing-style rules
│
├── .github/                            # GitHub community files
│   ├── CONTRIBUTING.md                 # How to contribute
│   ├── CODE_OF_CONDUCT.md              # Community guidelines
│   ├── SECURITY.md                     # Security policy
│   ├── FUNDING.yml                     # Sponsorship config
│   ├── ISSUE_TEMPLATE/                 # Issue templates
│   ├── pull_request_template.md        # PR template
│   └── workflows/                      # CI workflows
│
├── utils/                              # Shared helpers and validators
│   ├── helpers.py                      # Env loading, LLM clients, cosine, tokens
│   ├── validate_cells.py               # Notebook cell-structure validator
│   └── validate_style.py               # Prose-style validator
│
├── tests/                              # pytest smoke tests
├── data/                               # Small sample datasets
└── images/                             # Diagrams and visuals
```

---

## 📚 More from the same author

*Run a course, newsletter, or dev community? You can [earn 25% recommending RAG Made Simple](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agent-memory-techniques--readme&click=affiliate-signup&target=https%3A%2F%2Fnirdiamant.gumroad.com%2Faffiliates&retarget=0&text=affiliate-signup) to your audience.*

## 🤝 Contributing

<a href="https://github.com/NirDiamant/Agent_Memory_Techniques/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=NirDiamant/Agent_Memory_Techniques" alt="Contributors" />
</a>

We welcome contributions. You can fill in a notebook, fix a bug, improve the docs, or propose a new technique. Every contribution helps the next reader.

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the details.

**Where we need help the most:**
- More techniques we haven't covered yet (propose one via an issue)
- Architecture diagrams (Mermaid or ASCII)
- More memory benchmarks and evaluation metrics
- Integration examples for new frameworks

---

## 💖 Sponsors

Supporting this project helps keep educational AI content free and open. If your company uses agent memory in production, consider sponsoring to get your logo below.

<a href="https://github.com/sponsors/NirDiamant"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4" alt="Become a Sponsor"/></a>

---

## 🔗 Related Work

This repo is part of a bigger collection of AI technique tutorials.

| Repository | Stars | Focus |
|-----------|-------|-------|
| [RAG Techniques](https://github.com/NirDiamant/RAG_Techniques) | 26k+ | Retrieval-Augmented Generation techniques |
| [GenAI Agents](https://github.com/NirDiamant/GenAI_Agents) | 21k+ | Generative AI agent architectures |
| [Agents Towards Production](https://github.com/NirDiamant/agents-towards-production) | 18k+ | Production-grade agent deployment |
| [Prompt Engineering](https://github.com/NirDiamant/Prompt_Engineering) | 7k+ | Prompt engineering techniques |

---

## 🏷️ Topics Covered

This repository is a practical reference for agent memory in Large Language Model (LLM) applications. For the full keyword index covering short-term, long-term, cognitive architectures, retrieval, frameworks, evaluation, and production patterns, see [docs/topics.md](docs/topics.md).

---

## ⚠️ Disclaimer

This repository is for educational purposes. The code here shows how agent memory techniques work. It is not production-ready software. Do not use it as-is for handling regulated data, medical decisions, legal advice, or any high-stakes application without a careful review. The authors accept no responsibility for how you use this material.

---

## 📄 License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

---

## 📖 Citation

If you use this repository in your research or teaching, please cite:

```bibtex
@misc{diamant2026agentmemory,
    title={Agent Memory Techniques: A Comprehensive Collection},
    author={Nir Diamant},
    year={2026},
    url={https://github.com/NirDiamant/Agent_Memory_Techniques
}
```

---

**Built with care by [Nir Diamant](https://github.com/NirDiamant)**, making advanced AI accessible to everyone.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=main-readme)
