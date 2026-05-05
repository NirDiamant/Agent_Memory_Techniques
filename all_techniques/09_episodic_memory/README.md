# Episodic Memory

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/09_episodic_memory/episodic_memory.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

## 📖 At a Glance

| Difficulty | Time | Prerequisites |
|------------|------|---------------|
| Intermediate | ~30 min | Python 3.8+, `OPENAI_API_KEY`, understanding of 06 Vector Store Memory recommended |

This technique is for developers building agents that need to recall specific past experiences with contextual detail, similar to human autobiographical memory.

## TL;DR

- **What it is:** **Episodic Memory** captures whole conversation sessions as discrete episodes indexed by time and topic for cross-session recall.
- **When you need it:** Your agent must remember what happened in a specific past session, not isolated facts.
- **The trade-off:** Episode boundary detection can be too coarse or too fine, and storage grows with every session.
- **Closest alternative in this repo:** 10 Semantic Memory stores distilled, context-free facts rather than timestamped experiences.

## Description

You don't remember your life as a flat list of facts. You remember episodes: the meeting where you pivoted the product, the debugging session that took all afternoon. Episodic Memory brings this structure to LLM agent memory by capturing conversation sessions as discrete episodes, each indexed by time and topic. The agent searches episode summaries using semantic search and temporal indexing to find relevant past experiences. This makes it especially valuable for coaching agents, project management assistants, and multi-session chatbots where users expect recall across sessions.

Episodic Memory brings this capability to AI agents. It captures entire conversation sessions (or meaningful segments) as discrete episodes. Each episode is indexed by time, topic, and outcome. This lets the agent recall "what happened when" across sessions.

Think of it like a journal with chapters. Each chapter covers one session or topic. When you need to find something, you scan chapter titles (summaries) instead of re-reading every page. The agent does the same: it searches episode summaries to find past experiences relevant to the current question.

This matters for agents that operate across many sessions. A coaching agent needs to recall what goals were set last week. A project management agent needs to remember what was decided three days ago. Without episodic memory, each session starts from scratch.

**Keywords:** agent memory, LLM agent, episodic memory, episode boundaries, temporal indexing, semantic search, cross-session memory, conversation history, multi-session agents

## What You'll Learn

The [notebook](./episodic_memory.ipynb) walks you through a complete implementation:

1. **Episode data model**: a dataclass that stores messages, timestamps, summaries, topic tags, and embeddings.
2. **Boundary detection**: session-based (explicit `end_session()`) and topic-based (LLM detects topic shifts).
3. **Episode finalization**: LLM-generated summaries, topic extraction, and embedding computation.
4. **Retrieval**: combined scoring of recency and semantic similarity to find relevant past episodes.
5. **Prompt injection**: wiring retrieved episode summaries into the LLM system prompt.
6. **Multi-session example**: a project-coaching agent across three sessions, with a recall test.
7. **Persistence**: JSON serialization for saving and loading episodes.

## Key Concepts

- **Episode boundaries**: defining where one episode ends and another begins. Boundaries can be session-based, topic-based, or time-based.
- **Temporal indexing**: each episode is tagged with timestamps (start, end). This enables time-based queries.
- **Episode summaries**: short LLM-generated text that captures the gist of an episode. These make retrieval fast.
- **Semantic retrieval**: using embeddings and cosine similarity to find episodes related to the current query.
- **Episodic vs. semantic memory**: episodic memory stores specific experiences. Semantic memory stores generalized knowledge. Both serve different roles.

## When to Use

- Multi-session agents where users expect the agent to remember previous interactions.
- Project management or coaching agents that need to track progress over time.
- Agents that must answer "when did we..." or "what happened during..." style questions.
- Scenarios where the temporal sequence of events matters for reasoning.

## Limitations

- Episode boundary detection can produce segments that are too fine or too coarse.
- Summaries lose fine-grained detail. Specific numbers or facts may be lost.
- Retrieval adds latency (embedding call plus episode scan on every turn).
- Storage grows with every session. Long-lived agents need pruning or archival strategies.

## Architecture

<p align="center">
  <img src="../../images/diagrams/09_episodic_memory.svg" alt="Episodic Memory Architecture" width="720"/>
</p>

## How It Works

1. The agent collects messages into a buffer during the conversation.
2. A boundary detector decides when to close the current episode. It can split by session end or by topic shift (detected via an LLM call).
3. The agent finalizes the episode: it generates a summary, extracts topic tags, and computes an embedding (a numerical fingerprint) of the summary.
4. The finalized episode goes into persistent storage, indexed by time and topic.
5. On a new query, the agent scores stored episodes using a mix of semantic similarity and recency.
6. The top-scoring episode summaries are injected into the system prompt so the LLM can reference past experiences.

## References

- [Tulving, "Episodic Memory: From Mind to Brain," Annual Review of Psychology, 2002](https://doi.org/10.1146/annurev.psych.53.100901.135114)
- [Park et al., "Generative Agents: Interactive Simulacra of Human Behavior," UIST 2023](https://arxiv.org/abs/2304.03442)
- [Letta (MemGPT)](https://github.com/cpacker/MemGPT)
- [Conway, "Episodic Memories," Neuropsychologia, 2009](https://doi.org/10.1016/j.neuropsychologia.2009.02.003)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)

## Related Techniques

- [**10 Semantic Memory**](../10_semantic_memory/) - Stores distilled facts rather than full episodes, a natural complement to episodic memory.
- [**14 Memory Consolidation**](../14_memory_consolidation/) - Compresses and consolidates episodes over time to save storage.
- [**21 Cross-Session Memory**](../21_cross_session_memory/) - A broader pattern for persisting any memory type across sessions.
- [**18 Temporal Memory**](../18_temporal_memory/) - Focuses on time-aware retrieval and ordering, a key ingredient of episodic recall.

## FAQ

### Q: What is Episodic Memory in agent memory?

**A:** Episodic Memory captures whole conversation sessions or task executions as discrete episodes, indexed by time and topic. Each episode preserves the full context of what happened, when it happened, and what the outcome was. This mirrors human episodic memory: recalling specific experiences rather than abstract facts. Agents use it to say "Last Tuesday, when we debugged the auth issue, we found the token was expired." It stores experiences, not distilled knowledge.

### Q: When should I use Episodic Memory instead of Semantic Memory?

**A:** Use Episodic Memory when the agent needs to recall specific past interactions with full context: who said what, when, and what happened next. Semantic Memory (technique 10) strips away context to store timeless facts like "user prefers dark mode." If your agent benefits from recalling "the last time we tried approach X, it failed because of Y," that is episodic recall. Use semantic memory when you only need the extracted conclusion, not the story behind it.

### Q: What are the limits or failure modes of Episodic Memory?

**A:** Storage grows linearly with the number of episodes. Without pruning or summarization, retrieval slows as episodes accumulate into the hundreds or thousands. Retrieving the right episode depends on good indexing (time, topic tags, embeddings). If episodes are poorly segmented (too long or too short), retrieval quality drops. There is also redundancy: the same fact may appear across many episodes, wasting tokens when multiple episodes are retrieved.

### Q: Can I combine Episodic Memory with another memory technique?

**A:** Yes. The classic pairing is with technique 10 (Semantic Memory). Episodes preserve the full experience; semantic memory distills reusable facts from those episodes. Technique 14 (Memory Consolidation) can periodically process episodes to extract key facts, resolve contradictions, and archive or delete stale episodes. This episodic-to-semantic pipeline mimics how human memory consolidates experiences into long-term knowledge during sleep.

### Q: What library or framework can I use to skip the implementation work?

**A:** Letta/MemGPT (technique 26) stores conversation history as episodes in its recall memory tier. Zep (technique 27) maintains session-level episodic records with automatic fact extraction. LangChain does not have a dedicated episodic memory class, but you can build one using `ChatMessageHistory` with session IDs and a vector store for retrieval. Mem0 (technique 25) tracks user-level memories that have episodic characteristics when configured per session.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--09-episodic-memory--readme)
