<!-- validate-style: ignore-file -->

# Content Quality Standards

Every notebook, README, and doc in this repository follows these standards. If you contribute, please adhere to them. If you spot something that does not, open an issue or a PR.

## Writing style

Our readers come from all over the world. Many of them don't speak English as a first language. Write so they can read you easily.

- **Short sentences.** If a sentence runs over 20 words, break it in two.
- **Active voice.** Write "the agent stores the memory", not "the memory is stored by the agent".
- **Use "you" and "we".** Talk to the reader. "You'll notice" beats "the user will notice".
- **Contractions are fine.** "You'll", "don't", "it's" sound more natural.
- **Explain every technical term the first time you use it.** Don't assume the reader knows "boilerplate", "scaffold", "refactor", "abstraction", "embedding", "chunking", "RAG", "MMR", or "TTL". Define it in plain words, then use it.
- **Analogy first.** Before you introduce a concept, ground it in something the reader already knows. Cooking, driving, organizing a closet, a conversation with a friend. Keep the analogy to 2 to 4 sentences. Say where the analogy breaks down.

### Words to avoid

| Instead of | Use |
|---|---|
| "simply", "just" | Delete the word. Nothing is simple to a beginner. |
| "obviously" | Delete. If it were obvious, you wouldn't be teaching it. |
| "as you already know" | "Let's recall" or "Remember when we..." |
| "trivial" | "Straightforward" or "quick to set up" |
| "it's easy" | "This is one of the more approachable parts" |
| "leverage", "utilize" | "Use" |
| "paradigm" | "Approach" or "way of thinking" |
| "robust" | "Reliable" or "strong" |
| "no fluff", "no BS" | Delete. It's marketing posture, not teaching. |

### Punctuation

- No em dashes ( — ). Use a period, a colon, or parentheses instead.
- Use hyphens for number ranges (1-5, not 1–5).

## Overview and motivation

Every notebook opens with a substantial introduction that explains:

- **What** the technique is, in plain terms.
- **Why** it exists, what problem it solves, and when it is the right tool.
- **How** it works conceptually, independent of any specific framework.
- **What the reader will build** in this notebook, and what they will understand by the end.

Readers should finish reading the notebook, without running a single cell, and walk away with a working mental model. The code is there to make the idea concrete, not to substitute for the idea.

Implementations shown are specific illustrations of general ideas. Always name the general idea first, then the specific example.

## Code quality

- Code is broken into small cells, each doing one thing.
- Every code cell is preceded by a markdown cell that explains what the cell does and why, in natural language. Never drop a code cell on the reader with no context.
- No pip install logs, no `--verbose` output, no debug prints left in the notebook. Use `pip install -q` and clear outputs before committing.
- Comments inside code explain the non-obvious. Do not narrate line-by-line what the code already says. Do explain the edge cases, the invariants, the constants.
- Variable names are descriptive. No one-letter names outside of short loops.
- Prefer the SDK directly over wrapper frameworks when the technique does not require them. Framework lock-in hides the underlying pattern.

## Content structure

- Notebooks are focused. One technique per notebook. No appendices of loosely related ideas.
- Sections follow: Motivation, Key Concepts, Architecture, Setup, Implementation, Example Run, Tradeoffs, Further Reading.
- Remove anything that does not move the reader toward understanding the technique. If a section is not pulling its weight, cut it.
- Prose is dense, not verbose. One clean sentence beats three flowery ones.

## Links and references

- Each link appears exactly once per notebook or README. If the same source is relevant in two places, pick the more natural place.
- External links use UTM parameters for attribution:

  ```
  ?utm_source=nirdiamant&utm_medium=github&utm_campaign=agent_memory_techniques
  ```

  Applied to: documentation links, repo links to non-official projects, tool landing pages, author-owned content.
  Not applied to: academic papers (arxiv, DOI), official framework documentation under the vendor's top-level domain when they strip query strings, and plain GitHub repo roots unless there is a marketing reason.

- No external blog references (Medium, Substack, Dev.to, company blogs) unless they are the single authoritative source for a technique. Prefer papers, official docs, and reference implementations instead.
- Focus on high-value references. A reader should learn something from every link.

## Visual elements

- Every fully implemented notebook includes at least one architectural diagram rendered as an image, not a raw mermaid code block (Jupyter does not render mermaid natively).
- Only include logos that are directly relevant and authorised for use.
- Images live under `images/` at the repo root, never inlined as base64 in notebooks.
- Consistent palette across diagrams: indigo, emerald, amber, rose, slate.

## Per-notebook checklist

Before opening a PR, check:

- [ ] Opens with Motivation section covering what, why, how, what-you-will-build.
- [ ] Every code cell has an explanatory markdown cell before it.
- [ ] No pip install noise, no debug prints, all outputs cleared.
- [ ] Architecture diagram present and rendered as an image.
- [ ] All external links UTM-tagged where applicable; each link appears once.
- [ ] No external blog references.
- [ ] Closes with Tradeoffs and Further Reading.

## Per-README checklist

- [ ] Reads cleanly as a standalone document.
- [ ] Links deduplicated.
- [ ] External links UTM-tagged where applicable.
- [ ] Images optimised and relatively sized.
- [ ] Consistent tone with the rest of the repo.

## Reviewer tips

- Read the notebook top to bottom once without running it. If you cannot explain the technique to someone afterward, the motivation is not strong enough.
- Run every cell from a fresh kernel. Verify there are no silent dependencies on earlier state.
- Skim for boilerplate that could be cut.
- Treat the reader's attention as the scarcest resource in the repo.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=content-standards)
