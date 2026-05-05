# Graph Memory with Graphiti

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/24_graph_memory_graphiti/graph_memory_graphiti.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

## 📖 At a Glance

| Difficulty | Time | Prerequisites |
|------------|------|---------------|
| Advanced | ~60 min | Python 3.8+, `OPENAI_API_KEY`, Neo4j running locally (Docker recommended), understanding of 08 Knowledge Graph Memory recommended |

This technique is for developers who need multi-hop reasoning over evolving facts stored in a temporal knowledge graph backed by Neo4j.

## TL;DR

- **What it is:** **Graph Memory with Graphiti** stores agent knowledge in a Neo4j temporal knowledge graph with automatic entity and relationship extraction.
- **When you need it:** You need multi-hop reasoning over evolving facts with timestamps, like "What did the user prefer last month?"
- **The trade-off:** Requires running Neo4j, and each episode triggers multiple LLM calls for extraction that vary in quality by model.
- **Closest alternative in this repo:** 27 Zep Memory also builds temporal knowledge graphs but runs as a managed service instead of self-hosted.

## Description

Imagine a corkboard covered in index cards connected by colored strings. Each card represents a person, project, or concept. Each string represents a relationship: "manages," "depends on," "works with." Now imagine every string has a date tag. If a relationship changes, you add a new string and mark the old one as outdated. That's a temporal knowledge graph. Graph Memory with Graphiti is an agent memory technique that uses the Graphiti SDK (built by Zep) to store LLM agent knowledge in a Neo4j graph database. It captures entities, relationships, and timestamps from conversations through automatic entity extraction. You can then query with hybrid retrieval (combining semantic search and BM25 keyword matching). This is ideal for enterprise knowledge management, relationship tracking, and any agent that needs multi-hop reasoning over evolving facts.

**Keywords:** agent memory, LLM agent, Graphiti, Zep, temporal knowledge graph, Neo4j, entity extraction, relationship extraction, hybrid retrieval, knowledge graph memory

Graphiti, developed by Zep, builds temporal knowledge graphs from conversational data. A knowledge graph is a network of entities (people, projects, tools) connected by relationships ("Alice manages Bob," "Project X depends on Service Y"). "Temporal" means every relationship carries timestamps. The graph tracks when each relationship started, changed, or became invalid.

Unlike flat vector stores that treat each memory as an independent chunk, Graphiti captures the connections between concepts. This notebook covers ingesting conversation episodes into Graphiti, letting the extraction pipeline identify entities and relationships, querying the graph for multi-hop answers, exploring temporal edges, running community detection, and wiring it all into an agent loop.

## What You'll Build

A Graphiti-backed memory system that:

1. Connects to Neo4j and initializes the Graphiti knowledge graph engine.
2. Ingests six timestamped conversation episodes where facts evolve over time (team changes, job changes, new projects).
3. Searches the graph with natural-language queries using hybrid retrieval (semantic + BM25).
4. Explores temporal edges to see how facts are invalidated when they change.
5. Runs community detection with the Leiden algorithm to find knowledge clusters.
6. Powers an agent loop that answers relational and temporal questions by consulting the graph before each response.

## Key Concepts

- **Graphiti SDK**: The Python client for interacting with Graphiti's knowledge graph engine.
  It covers episode ingestion, search, and graph management.
- **Temporal knowledge graphs**: Graphs where nodes and edges carry timestamps. You can ask "what
  did we know as of last Tuesday?" and detect facts that are stale or outdated.
- **Episode ingestion**: Feeding raw conversation turns (episodes) into Graphiti. Graphiti's
  pipeline automatically extracts structured knowledge from the unstructured text.
- **Entity/relationship extraction**: Graphiti's LLM-powered pipeline that identifies named
  entities (people, projects, tools) and the relationships between them from conversation text.
- **Graph search**: Querying the knowledge graph with natural language. Graphiti combines semantic
  similarity with BM25 keyword matching for hybrid retrieval. You can retrieve entities, facts,
  and multi-hop relationship paths.
- **Community detection**: An algorithm (Leiden) that finds densely connected clusters within the
  knowledge graph. These clusters represent topic areas or knowledge domains.
- **Temporal edges**: Edges (the connections between nodes) that carry creation time, validity
  period, and invalidation markers. When a fact changes, the old edge is invalidated and a new
  one is created.

## Architecture

<p align="center">
  <img src="../../images/diagrams/24_graph_memory_graphiti.svg" alt="Graph Memory Graphiti architecture diagram" width="720"/>
</p>

---

## How It Works

1. You feed timestamped conversation episodes into Graphiti using `add_episode()`.
2. An LLM pipeline extracts entities (people, projects, tools) and relationships ("manages," "depends on") from each episode.
3. Graphiti resolves duplicates (e.g., "Alice" and "Dr. Alice Chen" merge into one node) and stores the graph in Neo4j.
4. Each relationship edge carries timestamps: when it was created and when it became invalid.
5. You query the graph with natural language. Graphiti combines semantic similarity with BM25 keyword matching.
6. Community detection (the Leiden algorithm) groups densely connected nodes into topic clusters.

## When to Use

- Your agent needs to answer multi-hop questions like "Who manages Alice, and what tools does her team use?"
- Facts change over time, and you need to track both current state and history (e.g., job changes, team transfers).
- You're building enterprise knowledge management where relationships between people, projects, and tools matter.
- A flat vector store isn't enough because your queries require traversing connections between entities.

## Limitations

- Requires a running Neo4j instance. That means extra infrastructure, monitoring, and backup compared to a vector store.
- Each `add_episode()` triggers multiple LLM calls. This adds seconds of latency and dollars of cost per episode.
- Extraction quality depends on the LLM. The pipeline can miss entities, hallucinate relationships, or fail to merge duplicates.
- For direct fact lookup ("What did the user say about X?"), a vector store is faster and cheaper. Graph memory adds unnecessary overhead for flat recall.

## Notebook

See the [full notebook](./graph_memory_graphiti.ipynb) for the implementation, architecture diagram, and interactive examples.

## Prerequisites

- A running Neo4j instance (Docker is the easiest path: `docker run -d -p 7687:7687 -p 7474:7474 -e NEO4J_AUTH=neo4j/password neo4j:latest`)
- An OpenAI API key (Graphiti uses OpenAI for extraction and embeddings by default)
- Python packages: `graphiti-core`, `neo4j`, `openai`, `python-dotenv`

## FAQ

### Q: What is Graph Memory with Graphiti in agent memory?

**A:** Graphiti is an open-source library that stores agent knowledge in a Neo4j temporal knowledge graph. It automatically extracts entities and relationships from conversations, assigns timestamps to every edge, and supports multi-hop traversal queries. Unlike static knowledge graphs, Graphiti tracks how facts change over time. You can query "What did we know about Project X in January?" versus "What do we know now?" Built by the Zep team, it is available as a self-hosted Python library.

### Q: When should I use Graph Memory with Graphiti instead of Zep Memory?

**A:** Use Graphiti when you want full control over your graph infrastructure and can self-host Neo4j. Zep (technique 27) offers similar temporal graph capabilities as a managed cloud service. Graphiti gives you direct access to the graph database, custom Cypher queries, and no vendor lock-in. Choose Zep when you prefer a managed service with less operational burden. Choose Graphiti when you need to run on-premises, customize the graph schema, or avoid sending data to a third-party service.

### Q: What are the limits or failure modes of Graph Memory with Graphiti?

**A:** Graphiti requires a running Neo4j instance, adding infrastructure complexity. Entity extraction quality depends on the LLM. Duplicate entities with slightly different names ("John Smith" vs. "J. Smith") need entity resolution, which Graphiti handles but not perfectly. Graph queries can become slow on large graphs (100k+ nodes) without proper indexing. The library is relatively new (2024), so the API may change across versions. Community support is growing but smaller than established frameworks.

### Q: Can I combine Graph Memory with Graphiti with another memory technique?

**A:** Yes. Graphiti works well alongside technique 09 (Episodic Memory): use episodic memory for raw session records and Graphiti for the distilled knowledge graph. Pair it with technique 20 (Memory Retrieval Patterns) to add hybrid search (vector + graph traversal) for richer retrieval. Graphiti already combines with technique 18 (Temporal Memory) natively, since all edges carry timestamps and support temporal queries out of the box.

### Q: What library or framework can I use to skip the implementation work?

**A:** Graphiti itself is the library. Install it via `pip install graphiti-core` and connect to Neo4j. For a managed alternative that uses the same temporal graph technology, use Zep (technique 27). LangChain has Neo4j graph integrations for basic graph memory, but Graphiti adds automatic entity extraction, temporal tracking, and entity resolution on top. For simpler graph memory without Neo4j, LangChain's `ConversationKGMemory` (technique 08) uses NetworkX for lightweight in-memory graphs.

## References

- [Graphiti GitHub Repository](https://github.com/getzep/graphiti): Open-source code, API reference, and examples.
- [Zep Documentation](https://docs.getzep.com?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques): Production deployment guides for Graphiti.
- [Neo4j Graph Database Documentation](https://neo4j.com/docs/?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques): The graph database backend. Covers Cypher queries, indexing, and graph algorithms.
- [Ji et al., "A Survey on Knowledge Graphs," IEEE TNNLS, 2021](https://ieeexplore.ieee.org/document/9416312): Knowledge graph construction and applications.
- [Kang et al., "Zep: A Temporal Knowledge Graph Architecture for Agent Memory," 2025 (arXiv:2501.13956)](https://arxiv.org/abs/2501.13956): The paper behind Graphiti's design.

## Related Techniques

- [**08 Knowledge Graph Memory**](../08_knowledge_graph_memory/) - The foundational pattern for graph-based memory. Graphiti builds on these ideas with temporal tracking and hybrid retrieval.
- [**27 Zep Memory**](../27_zep_memory/) - The broader Zep platform that hosts Graphiti, adding session management and user-scoped memory on top.
- [**07 Entity Memory**](../07_entity_memory/) - Tracks individual entities across conversations. Graphiti extends this to full entity-relationship graphs.
- [**20 Memory Retrieval Patterns**](../20_memory_retrieval_patterns/) - Covers hybrid retrieval strategies like the semantic + BM25 combination that Graphiti uses.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--24-graph-memory-graphiti--readme)
