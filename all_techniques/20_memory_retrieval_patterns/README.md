# Memory Retrieval Patterns

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/20_memory_retrieval_patterns/memory_retrieval_patterns.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

## 📖 At a Glance

| Difficulty | Time | Prerequisites |
|------------|------|---------------|
| Intermediate | ~40 min | Python 3.8+, `OPENAI_API_KEY`, understanding of 06 Vector Store Memory recommended |

This technique is for developers who want to improve memory recall accuracy using hybrid retrieval, re-ranking, and query transformation strategies.

## TL;DR

- **What it is:** **Memory Retrieval Patterns** combines semantic search, BM25 keyword matching, re-ranking, and MMR diversity filtering into a multi-stage pipeline.
- **When you need it:** Basic vector search misses keyword-dependent or diverse results and you need higher recall accuracy.
- **The trade-off:** Cross-encoder re-ranking adds 50-200ms latency, and many tunable parameters (RRF k, MMR lambda) create misconfiguration risk.
- **Closest alternative in this repo:** 06 Vector Store Memory is the single-stage semantic retrieval building block this technique extends.

## Overview

Think of a search engine. You type a query and get results. Behind the scenes, it uses many strategies at once: keyword matching, meaning analysis, popularity signals, and diversity filters. Each layer catches things the others miss. Memory Retrieval Patterns is the agent memory technique that brings this same multi-stage approach to LLM agent memory. It combines semantic search (finding memories by meaning through embeddings), BM25 keyword matching, re-ranking with cross-encoder models, and MMR diversity filtering. These components wire together into a single hybrid retrieval pipeline. You'll use these patterns in any knowledge-intensive application: research assistants, customer support agents, or long-running chatbots with large memory stores.

A memory system is only as good as its ability to surface the right information at the right time. The choice of retrieval strategy has a deep impact on agent performance.

In this notebook, you build a multi-stage retrieval pipeline from scratch. It combines semantic search (embedding-based), BM25 keyword matching, Reciprocal Rank Fusion, cross-encoder re-ranking, and MMR diversity filtering. Each component is implemented as a standalone piece, then wired together into a single `HybridRetriever` class.

**Keywords:** agent memory, LLM agent, hybrid retrieval, semantic search, BM25, re-ranking, Reciprocal Rank Fusion, MMR diversity, cross-encoder, retrieval pipeline

## Key Concepts

- **Semantic similarity**: Using embedding vectors (numerical representations of meaning) to find memories whose meaning is close to the query. Measured by cosine similarity.
- **BM25 lexical search**: A term-frequency-based ranking function that excels at exact keyword matching. It handles domain-specific terminology well.
- **Hybrid retrieval**: Combining semantic and lexical search results using Reciprocal Rank Fusion (RRF). This captures both meaning and keyword matches.
- **Maximal Marginal Relevance (MMR)**: A re-ranking strategy that balances relevance with diversity. It reduces repetitive results in the final output.
- **Cross-encoder re-ranking**: Using a model that scores (query, document) pairs together for higher precision than embedding similarity alone.
- **HyDE (Hypothetical Document Embeddings)**: A query transformation technique that generates a hypothetical answer, then searches for similar documents. This bridges the vocabulary gap between short queries and longer stored memories.

## Architecture

<p align="center">
  <img src="../../images/diagrams/20_memory_retrieval_patterns.svg" alt="Memory Retrieval Patterns architecture diagram" width="720"/>
</p>

---

## How It Works

1. The query is optionally transformed using HyDE (the LLM writes a hypothetical answer).
2. The transformed query runs through two indices in parallel: semantic search (embeddings + cosine similarity) and BM25 (keyword matching).
3. Reciprocal Rank Fusion combines both ranked lists into a single fused ranking.
4. A cross-encoder re-ranker re-scores the top candidates with higher precision.
5. MMR selects the final top-K results while maximizing diversity.
6. The results are formatted and injected into the agent's context window.

## When to Use

- Any agent system that retrieves from memory. Retrieval quality matters everywhere.
- Systems where naive semantic search returns repetitive or off-topic results.
- Domains with specialized terminology where pure embedding search underperforms keyword matching.
- Large memory stores (hundreds to thousands of entries) where a multi-stage pipeline improves precision.

## Limitations

- Each pipeline stage adds latency. The cross-encoder re-ranker adds 50-200ms, and HyDE (Hypothetical Document Embeddings) adds a full LLM call. Real-time chat may need to skip stages.
- HyDE can mislead retrieval when the LLM generates an incorrect hypothetical answer. The search then finds documents similar to the wrong answer instead of the right one.
- Small memory stores (fewer than 50 entries) see little benefit from the full pipeline. A basic cosine similarity search works well enough at that scale.
- The system has many tunable parameters: RRF's k constant, MMR's lambda, candidate counts at each stage. More parameters mean more opportunities for misconfiguration.

## Notebook

See the [implemented notebook](./memory_retrieval_patterns.ipynb) for the full walkthrough, code, and example queries.

## FAQ

### Q: What is Memory Retrieval Patterns in agent memory?

**A:** Memory Retrieval Patterns describes a multi-stage hybrid retrieval pipeline that combines semantic search, BM25 keyword matching, cross-encoder re-ranking, and MMR (Maximal Marginal Relevance) diversity filtering. Instead of relying on a single retrieval method, you run multiple retrievers in parallel, fuse their results using Reciprocal Rank Fusion (RRF), then re-rank and deduplicate. This consistently outperforms single-method retrieval, improving recall by 15-30% in typical benchmarks.

### Q: When should I use Memory Retrieval Patterns instead of Vector Store Memory?

**A:** Use the full retrieval pipeline when basic vector search misses relevant memories. Vector Store Memory (technique 06) uses cosine similarity on embeddings, which can miss keyword-exact matches ("Python 3.11" vs. "latest Python"). Adding BM25 catches these. Use re-ranking when your top-K results contain false positives. Use MMR when results are too similar (returning 5 near-duplicate memories). Start with basic vector search and add pipeline stages as retrieval quality problems appear.

### Q: What are the limits or failure modes of Memory Retrieval Patterns?

**A:** Each pipeline stage adds latency. A full pipeline (vector search + BM25 + re-ranking + MMR) can take 200-500ms compared to 20-50ms for vector search alone. Cross-encoder re-ranking is the most expensive step, running the query against each candidate pair. Over-engineering the pipeline for a small memory store (under 100 entries) adds complexity without measurable improvement. You also need to tune fusion weights and re-ranker thresholds per domain.

### Q: Can I combine Memory Retrieval Patterns with another memory technique?

**A:** Yes. Apply these patterns as the retrieval layer for technique 06 (Vector Store Memory), technique 10 (Semantic Memory), or technique 09 (Episodic Memory). Pair with technique 18 (Temporal Memory) by adding a time-decay multiplier after the re-ranking stage. Combine with technique 12 (Working Memory) to feed the top results into the context window with priority scoring. The retrieval pipeline is infrastructure that improves any storage-based memory technique.

### Q: What library or framework can I use to skip the implementation work?

**A:** LangChain provides `EnsembleRetriever` for BM25+vector fusion and supports cross-encoder re-rankers through the `CrossEncoderReranker` class. LlamaIndex has `QueryFusionRetriever` for multi-source fusion. Zep (technique 27) applies hybrid retrieval internally. For standalone components, rank-bm25 handles BM25 scoring, sentence-transformers provides cross-encoder models, and FAISS or Chroma handles the vector search layer. You can assemble a full pipeline in roughly 50-100 lines using these libraries.

## References

- Robertson, S., & Zaragoza, H. (2009). ["The Probabilistic Relevance Framework: BM25 and Beyond."](https://doi.org/10.1561/1500000019) *Foundations and Trends in Information Retrieval*, 3(4), 333-389.
- Carbonell, J., & Goldstein, J. (1998). ["The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries."](https://doi.org/10.1145/290941.291025) *ACM SIGIR*, 335-336.
- Gao, L., et al. (2022). ["Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)."](https://arxiv.org/abs/2212.10496)
- Ma, X., et al. (2023). ["Fine-Tuning LLaMA for Multi-Stage Text Retrieval."](https://arxiv.org/abs/2310.08319)

## Related Techniques

- [**06 Vector Store Memory**](../06_vector_store_memory/) - The basic semantic retrieval building block. This technique extends it with keyword search, fusion, and re-ranking.
- [**21 Cross-Session Memory**](../21_cross_session_memory/) - Applies retrieval patterns across user sessions so the agent remembers past conversations.
- [**18 Temporal Memory**](../18_temporal_memory/) - Adds time-weighted scoring to the retrieval pipeline for environments where recency matters.
- [**25 Mem0 Patterns**](../25_mem0_patterns/) - A framework that implements hybrid retrieval for agent memory out of the box.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--20-memory-retrieval-patterns--readme)
