# Memory with Tools (Memory-as-a-Tool)

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/23_memory_with_tools/memory_with_tools.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

## 📖 At a Glance

| Difficulty | Time | Prerequisites |
|------------|------|---------------|
| Intermediate | ~35 min | Python 3.8+, `ANTHROPIC_API_KEY`, understanding of 06 Vector Store Memory recommended |

This technique is for developers building tool-using agents that persist tool results and use stored knowledge to inform future tool calls.

## TL;DR

- **What it is:** **Memory with Tools** exposes memory CRUD operations as callable tools so the agent decides when to save, search, update, or delete memories.
- **When you need it:** You want the agent itself to control what gets remembered rather than using automatic extraction.
- **The trade-off:** Each tool call adds an API round trip, and the agent may forget to save important facts if not prompted.
- **Closest alternative in this repo:** 25 Mem0 Patterns automates extraction instead of relying on the agent to call tools explicitly.

## Description

Think of a librarian who decides what books to shelve, which ones to look up for you, and which outdated ones to discard. The librarian doesn't follow a fixed routine. They use their judgment based on what you ask. Memory with Tools (also called Memory-as-a-Tool) gives an LLM agent the same kind of control over its own agent memory. Instead of managing memory behind the scenes, you expose CRUD operations (create, read, update, delete) as callable tools in the agent's tool-use loop. The agent decides when to save, search, update, or delete memories through semantic search. This approach works well for autonomous agents, conversational assistants, and any system where the model should actively curate its own knowledge base.

**Keywords:** agent memory, LLM agent, memory-as-a-tool, tool-use, memory CRUD, semantic search, agent-driven memory, save memory, search memory, Anthropic tool use

Instead of managing memory behind the scenes through prompt engineering or framework-level code, this technique gives the agent explicit, callable memory tools. The four tools are `save_memory`, `search_memory`, `update_memory`, and `delete_memory`. The agent calls them through the standard tool-use loop, the same way it might call a web search or run code.

The agent decides when and what to remember, what to look up, and what to forget. This makes memory management a first-class part of the agent's reasoning. The approach uses Anthropic's `tool_use` pattern. A "tool_use pattern" means the agent can request a tool call during generation, and the system executes it and returns the result. Memory operations appear alongside other tools in the agent's action space.

The result is an agent that actively curates its own knowledge base. It saves important facts after a user mentions them. It searches for relevant context before answering. It prunes outdated information when corrections arrive.

## Key Concepts

- **Tool schema**: A structured description of a callable function. It includes the tool's name, what it does, and what inputs it expects as a JSON Schema.
- **Memory CRUD**: The four core operations (Create, Read, Update, Delete) exposed as individual tools: `save_memory`, `search_memory`, `update_memory`, `delete_memory`.
- **Agentic tool-use loop**: The cycle where the LLM generates a response, optionally requests a tool call, receives the result, and continues. This repeats until the model produces a final text response.
- **`tool_use` / `tool_result` blocks**: Anthropic's content block types for tool calls. The model emits `tool_use` to request a call. Your code returns `tool_result` with the output.
- **Semantic search**: Finding stored items by meaning rather than exact keyword match. We embed the query and find memories with the highest cosine similarity.
- **Agent-driven memory**: The LLM decides on its own when to store, retrieve, modify, or discard information based on the conversation context.

## Notebook

The [implemented notebook](./memory_with_tools.ipynb) covers:

1. **Tool definitions**: Four Anthropic-compatible tool schemas for memory CRUD.
2. **Memory store**: A `MemoryStore` class with hash-based embeddings and cosine similarity search.
3. **Tool dispatcher**: A function that routes tool calls to the correct memory operation.
4. **System prompt**: Instructions that guide the model on when to save, search, update, and delete.
5. **Agentic loop**: The full `chat_with_memory` function that drives multi-turn conversations with tool-use.
6. **Example run**: A realistic conversation that exercises all four operations, including tool chaining.

## Architecture

<p align="center">
  <img src="../../images/diagrams/23_memory_with_tools.svg" alt="Memory with Tools architecture diagram" width="720"/>
</p>

## How It Works

1. You define four tool schemas (save, search, update, delete) and register them with the LLM.
2. A `MemoryStore` holds memories as text with vector embeddings for semantic search (finding items by meaning, not exact keywords).
3. During conversation, the LLM decides when to call a memory tool based on context.
4. A dispatcher routes each tool call to the correct `MemoryStore` method and returns the result.
5. The LLM receives the tool result and continues generating. It may chain more tool calls in the same turn.
6. The loop repeats until the LLM produces a final text response with no further tool requests.

## When to Use

- You want the agent to decide what's worth remembering, rather than saving everything automatically.
- Your agent needs to correct or delete outdated memories when users provide updates.
- You're building an autonomous agent that combines memory tools with other tools (web search, code execution).
- You need transparent, auditable memory operations where every save and delete appears in the conversation log.

## Limitations

- The agent may forget to save important facts or save too much noise. Quality depends on the model's judgment.
- Each tool call adds an API round trip. Chaining multiple operations (search, then update, then delete) increases latency.
- Tool schemas consume 500-800 tokens in every request. That overhead exists even when no memory operations happen.
- Memory management only runs during active turns. The agent won't consolidate or clean up memories between conversations.

## FAQ

### Q: What is Memory with Tools in agent memory?

**A:** Memory with Tools (also called Memory-as-a-Tool) exposes memory CRUD operations as callable tools that the agent invokes through its tool-use interface. Instead of automatic memory management, the agent decides when to call `save_memory`, `search_memory`, `update_memory`, or `delete_memory`. This gives the agent full control over what gets stored and retrieved. The pattern works with any tool-calling LLM (GPT-4, Claude, Gemini) and any storage backend behind the tool interface.

### Q: When should I use Memory with Tools instead of Mem0 Patterns?

**A:** Use Memory with Tools when you want the agent to make explicit, auditable decisions about what to remember. Mem0 (technique 25) extracts and stores facts automatically, which is easier to set up but gives you less control. The tool-based approach lets the agent choose precisely what to save and when to search. If you need transparency about why the agent stored a fact or auditability for compliance, explicit tool calls are preferable to automatic extraction.

### Q: What are the limits or failure modes of Memory with Tools?

**A:** The agent may forget to call the save tool, losing important information. It may over-save, storing noise that pollutes future retrievals. Tool-calling adds latency per operation (100-300ms). The agent must learn when to use each tool, which requires good tool descriptions and sometimes few-shot examples. If the LLM's tool-calling ability is weak, memory operations may fail or return unexpected formats. Prompt engineering for tool descriptions is critical for reliability.

### Q: Can I combine Memory with Tools with another memory technique?

**A:** Yes. The tool interface is a wrapper that can connect to any storage technique. Wire `save_memory` to technique 10 (Semantic Memory) for fact storage, `search_memory` to technique 06 (Vector Store Memory) for retrieval, and `delete_memory` to technique 19 (Forgetting and Decay) for cleanup. Add technique 17 (Memory Routing) behind the tools so the save operation automatically routes to the right store. The tool pattern is a control interface, not a storage technique.

### Q: What library or framework can I use to skip the implementation work?

**A:** LangChain supports custom tools through its `Tool` or `StructuredTool` classes, making it easy to wrap any memory backend as a callable tool. OpenAI function calling and Claude tool use both support this pattern natively. Mem0 (technique 25) provides a tool-friendly API that you can wrap in 10 lines of code. Letta/MemGPT (technique 26) is built entirely around the tool-based memory pattern, with built-in memory management functions the agent calls directly.

## References

- [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)
- [Packer et al. (2023). "MemGPT: Towards LLMs as Operating Systems."](https://arxiv.org/abs/2310.08560)
- [Anthropic: Building Effective Agents (2025)](https://www.anthropic.com/engineering/building-effective-agents?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)
- [Zep Memory Tools Integration](https://docs.getzep.com?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)

## Related Techniques

- [**06 Vector Store Memory**](../06_vector_store_memory/) - The underlying storage approach that many memory tools use for semantic search.
- [**25 Mem0 Integration Patterns**](../25_mem0_patterns/) - A managed service that automates the same save/search/update/delete cycle this technique builds by hand.
- [**26 Letta (MemGPT) Patterns**](../26_letta_memgpt_patterns/) - A framework where the agent manages its own memory through tool calls, similar to this approach but with tiered storage.
- [**16 Self-Reflection Memory**](../16_self_reflection_memory/) - Adds a reflection step where the agent evaluates what to remember, complementing tool-based memory control.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--23-memory-with-tools--readme)
