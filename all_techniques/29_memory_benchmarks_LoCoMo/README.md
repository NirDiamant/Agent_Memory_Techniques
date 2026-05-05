# Memory Benchmarks (LoCoMo & LongMemEval)

<p align="center">
  <a href="https://colab.research.google.com/github/NirDiamant/Agent_Memory_Techniques/blob/main/all_techniques/29_memory_benchmarks_LoCoMo/memory_benchmarks_locomo.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

## 📖 At a Glance

| Difficulty | Time | Prerequisites |
|------------|------|---------------|
| Advanced | ~60 min | Python 3.8+, `OPENAI_API_KEY`, understanding of 28 Memory Evaluation recommended |

This technique is for developers who want to benchmark agent memory against the LoCoMo dataset, testing long-conversation recall with standardized metrics.

## TL;DR

- **What it is:** **Memory Benchmarks (LoCoMo and LongMemEval)** tests agent memory against standardized multi-session datasets with per-category scoring.
- **When you need it:** You want to compare your memory system against published baselines using a reproducible benchmark.
- **The trade-off:** Running a full benchmark with an LLM judge costs $5-15, and the fixed conversation set may not match your domain.
- **Closest alternative in this repo:** 28 Memory Evaluation lets you build custom evaluation datasets tailored to your specific use case.

## Description

Imagine you hire a new assistant and give them a quiz after their first week. One section tests whether they remember your coffee order. Another checks if they can connect two separate conversations. A third asks when you switched from tea to coffee. Memory Benchmarks (LoCoMo & LongMemEval) work the same way for LLM agent memory. LoCoMo and LongMemEval are standardized benchmark datasets. They test how well an agent stores and retrieves information across multi-session conversations. Each benchmark produces per-category scores for single-hop retrieval, multi-hop reasoning, and temporal reasoning. This gives you concrete numbers to compare memory systems and track improvements.

LoCoMo (Long-Context Conversational Memory) and LongMemEval provide multi-session conversations paired with ground-truth questions. Each question targets a specific memory capability: single-hop retrieval, multi-hop reasoning, temporal reasoning, open-ended generation, or adversarial resistance. Running your system against these benchmarks produces per-category scores that turn "memory quality" into a number you can track and improve.

**Keywords:** agent memory, LoCoMo, LongMemEval, memory benchmark, multi-session conversation, BLEU, ROUGE, LLM agent, temporal reasoning, multi-hop reasoning

## What You'll Learn

- How to load and explore the LoCoMo benchmark dataset from HuggingFace.
- How to build a prediction pipeline that answers benchmark questions using retrieved context.
- How to score predictions with BLEU, ROUGE-L, token F1, and an LLM judge.
- How to analyze per-category results and compare against a no-memory baseline.
- How LongMemEval complements LoCoMo with user-assistant chat histories and additional question types.

## Key Concepts

- **LoCoMo benchmark**: 10 multi-session conversations with about 2,000 QA pairs across five question categories.
- **LongMemEval**: 500 instances of user-assistant chat histories testing five core memory abilities.
- **Question types**: Single-hop (direct fact recall), multi-hop (connecting facts across sessions), temporal (time-aware reasoning), open-ended (synthesis from scattered facts), and adversarial (resistance to misleading context).
- **Scoring methodology**: BLEU (n-gram overlap), ROUGE-L (longest common subsequence), token F1 (precision/recall balance), and LLM judge (semantic correctness).
- **Baseline comparison**: Running the same questions with no memory context to measure how much value retrieval adds.

## Architecture

<p align="center">
  <img src="../../images/diagrams/29_memory_benchmarks_LoCoMo.svg" alt="Memory Benchmarks Locomo architecture diagram" width="720"/>
</p>

---

## How It Works

1. You load a benchmark dataset (LoCoMo or LongMemEval) from HuggingFace. Each sample contains multi-session conversations and ground-truth question-answer pairs.
2. You convert the structured dialogue into a flat text format that your memory system can ingest.
3. For each benchmark question, your system retrieves relevant context and generates a predicted answer.
4. A scoring pipeline computes BLEU (n-gram overlap), ROUGE-L (longest common subsequence), and token F1 (precision-recall balance) against the reference answer.
5. An LLM judge checks semantic correctness for cases where wording differs but the meaning matches.
6. You group scores by question category (single-hop, multi-hop, temporal, open-ended) to pinpoint specific weaknesses.

## When to Use

- You want to objectively compare two memory architectures on the same standardized test set.
- You need per-category diagnostic scores that reveal whether your system struggles with temporal reasoning, multi-hop connections, or direct recall.
- You're iterating on a memory system and need a regression test to confirm each change helps rather than hurts.
- You want a shared, reproducible metric so your team can discuss "memory quality" with concrete numbers instead of impressions.

## Limitations

- LoCoMo conversations are between friends chatting about daily life. If your system handles technical support or enterprise workflows, benchmark scores may not reflect real performance.
- Running all 2,000 LoCoMo questions through an LLM judge costs real API money (roughly $5-15 per full run with GPT-4o-mini).
- Text overlap metrics (BLEU, ROUGE, F1) penalize correct answers that use different wording. The LLM judge helps, but it isn't perfect either.
- These benchmarks test a fixed set of conversations. They can't capture every edge case your system will encounter in production. Treat them as a floor, not a ceiling.

## Notebook

See the [implemented notebook](./memory_benchmarks_locomo.ipynb) for a complete walkthrough with code.

## FAQ

### Q: What is LoCoMo in agent memory benchmarks?

**A:** LoCoMo (Long Conversation Memory) is a standardized benchmark dataset for testing agent memory systems. It contains multi-session conversations with ground-truth questions spanning single-hop retrieval, multi-hop reasoning, temporal reasoning, and open-ended generation. Each question has a verified answer, enabling automated scoring. LoCoMo was introduced in 2024 and has become a standard benchmark for comparing memory architectures. LongMemEval is a complementary benchmark that tests long-term memory across even longer conversation spans.

### Q: When should I use LoCoMo benchmarks instead of custom Memory Evaluation?

**A:** Use LoCoMo and LongMemEval when you want to compare your memory system against published baselines or other systems on common ground. Custom evaluation (technique 28) tests your specific domain requirements but cannot be compared across teams. LoCoMo gives you standardized scores that you can report in papers or use to pick between memory frameworks. Use LoCoMo for system selection and external comparison. Use custom evaluation for domain-specific tuning and production monitoring.

### Q: What are the limits or failure modes of LoCoMo?

**A:** LoCoMo tests a specific conversation distribution that may not match your domain. High LoCoMo scores do not guarantee good performance on medical, legal, or technical conversations. The dataset is relatively small (around 600 QA pairs across sessions), so overfitting is possible. Temporal reasoning questions assume specific time formats. The benchmark does not test write performance, latency, or cost, only retrieval and answer quality. Use it as one signal among many, not as the sole quality metric.

### Q: Can I combine Memory Benchmarks with another memory technique?

**A:** Yes. Run LoCoMo against different memory configurations to find the best setup. For example, test technique 06 (Vector Store Memory) alone, then add technique 20 (Memory Retrieval Patterns) and measure the improvement. Compare technique 03 (Summary Memory) versus technique 04 (Summary Buffer Memory) on LoCoMo's multi-hop questions. The benchmark is a tool for systematic comparison. Use it with technique 28 (Memory Evaluation) to build a complete evaluation suite covering both standard and domain-specific tests.

### Q: What library or framework can I use to skip the implementation work?

**A:** The LoCoMo dataset is available on GitHub and HuggingFace. LongMemEval is also publicly available. Both come with evaluation scripts. RAGAS can compute retrieval metrics on LoCoMo results. DeepEval supports custom benchmark evaluation pipelines. The evaluation code in this repo (technique 28) includes a harness that runs memory systems against LoCoMo questions and scores the results. You can set up a complete benchmark pipeline in under an hour using these tools.

## References

- Maharana, A., Lee, D., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024).
  "Evaluating Very Long-Term Conversational Memory of LLM Agents." arXiv:2402.17753.
- LoCoMo GitHub:
  [https://github.com/snap-research/LoCoMo](https://github.com/snap-research/LoCoMo)
- Wu, D., et al. (2024). "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive
  Memory." arXiv:2410.10813.
- LongMemEval GitHub:
  [https://github.com/xiaowu0162/LongMemEval](https://github.com/xiaowu0162/LongMemEval)
- HuggingFace evaluate library (BLEU/ROUGE):
  [https://huggingface.co/docs/evaluate](https://huggingface.co/docs/evaluate?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques)

## Related Techniques

- [**28 Memory Evaluation**](../28_memory_evaluation/) - The general evaluation framework. Benchmarks give you standard datasets to plug into it.
- [**30 Production Memory Patterns**](../30_production_memory_patterns/) - Benchmark results help you choose the right patterns before deploying to production.
- [**21 Cross-Session Memory**](../21_cross_session_memory/) - Both LoCoMo and LongMemEval test cross-session recall abilities.
- [**09 Episodic Memory**](../09_episodic_memory/) - Episodic recall is one of the core abilities these benchmarks measure.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=all-techniques--29-memory-benchmarks-locomo--readme)
