# Roadmap

All 30 techniques are now implemented with full notebooks, per-technique READMEs, and enforced quality gates. This page shows where the project stands today and what's next.

## At a Glance

| Area | Scope | Status |
|------|-------|--------|
| **Techniques** | 30 runnable notebooks + READMEs | Complete |
| **Writing style** | Short sentences, active voice, explained jargon | Enforced via CI (`utils/validate_style.py`) |
| **Notebook structure** | Every code cell has a markdown cell above it; no code cell over 60 lines | Enforced via CI (`utils/validate_cells.py`) |
| **Taxonomy** | Short-term, long-term, cognitive, retrieval, frameworks, production | Complete, grouped in README |
| **Learning paths** | Beginner, Intermediate, Advanced, Practitioner | Defined in `docs/learning_path.md` |
| **Licensing** | Apache 2.0 | Complete |

See [docs/roadmap.md](docs/roadmap.md) for the original planning document that guided construction. This page is the current truth.

## What's Next

The techniques themselves are done. The next wave of work makes the repo easier to find, faster to try, and easier to trust.

### 1. Executable notebooks with committed outputs
Every notebook runs top-to-bottom today, but the outputs are not committed. A fresh visitor sees code without evidence. Running each notebook end-to-end and committing the results closes this gap. Tracked as an ongoing task.

### 2. One-click try: Colab badges
Each per-technique README will link to a Colab runner so a reader can try a technique without cloning.

### 3. "Which technique do I need?" decision tree
The main README lists all 30 techniques grouped by type. A short decision tree (Mermaid) will help new readers jump straight to the right one based on their situation.

### 4. Cross-links between related techniques
Each per-technique README will end with a "see also" block pointing to the 2-3 related techniques. The graph lives in the author's head today; this codifies it.

### 5. Mermaid architecture diagrams per technique
Each technique README will include a small Mermaid diagram showing the data flow. Mermaid renders on GitHub and diffs cleanly, so contributors can update them in a PR.

### 6. Benchmarks against LoCoMo
Technique 29 implements the LoCoMo benchmark. Running it against a subset of the other techniques and committing a `BENCHMARKS.md` turns the repo from "30 recipes" into "30 recipes with evidence".

### 7. CI polish
The validate workflow runs on every push and PR. The next add is `nbqa ruff` on code cells and a weekly link checker.

### 8. Production gotchas
Each technique will gain a short "Production gotchas" section covering the failure mode that bites at scale. This is the section readers reference later.

## Contributing

Good first issues will focus on the work above. If you're looking for a specific task, see [CONTRIBUTING.md](.github/CONTRIBUTING.md) or open an issue.

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=roadmap)
