# Contributing to Agent Memory Techniques

Thank you for your interest in contributing! This project grows through community help. You can implement a new notebook, fix a bug, improve documentation, or propose a new technique.

## How to Contribute

### 1. Fork and Clone

```bash
git clone https://github.com/<your-username>/Agent_Memory_Techniques.git
cd Agent_Memory_Techniques
git remote add upstream https://github.com/NirDiamant/Agent_Memory_Techniques.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-technique-name
```

### 3. Implement Your Changes

See the notebook standards below.

### 4. Submit a Pull Request

Push your branch and open a PR against `main`. Include:
- A clear description of the changes
- Which technique(s) you changed
- Confirmation that the notebook runs end-to-end

## Notebook Standards

Every notebook should follow these guidelines.

### Structure

1. **Title cell**: Markdown H1 with the technique name
2. **Overview**: What the technique does, when to use it, and why it matters
3. **Architecture diagram**: ASCII or Mermaid diagram showing data flow
4. **Setup**: Install dependencies and load environment variables from `.env`
5. **Implementation**: Step-by-step code with explanatory markdown between cells
6. **Example usage**: Realistic demo scenarios
7. **Takeaways**: Key insights and when to use this technique
8. **References**: Papers, docs, and related techniques

### Code Standards

- **Python 3.10+** with modern features (type hints, etc.)
- **Self-contained**: Runs top-to-bottom without external state
- **Load from .env**: Never hardcode API keys. Use `python-dotenv`
- **Prefer SDKs over frameworks**: Use OpenAI or Anthropic SDKs directly when possible. When a framework fits naturally, explain the underlying pattern first.
- **Document your code**: Add docstrings and type hints
- **Keep it focused**: One technique per notebook

## Types of Contributions

### Implement a Notebook

Check the `all_techniques/` folders. Many have README outlines but no notebook yet. Pick one and implement it using the standards above.

### Improve Existing Notebooks

- Fix bugs or outdated API calls
- Add better examples or edge cases
- Improve explanations or diagrams

### Documentation

- Improve technique READMEs
- Add architecture diagrams
- Update the glossary

### Propose New Techniques

Open an issue with:
- Technique name and description
- Why it's distinct from existing techniques
- References to papers or implementations

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

Open an issue or start a discussion. We're happy to help!

---

![](https://europe-west1-amt-views-tracker.cloudfunctions.net/amt-tracker?notebook=contributing)


## Pre-PR Checklist

Before you open a pull request, confirm:

- [ ] The sub-README has all 9 sections in canonical order (Description, Key Concepts, Architecture, How It Works, When to Use, Limitations, Notebook, References, Related Techniques).
- [ ] The notebook runs top-to-bottom without errors using the current `requirements.txt`.
- [ ] No API keys or credentials are committed.
- [ ] `python3 utils/validate_style.py` reports `OK` for the files you changed.
- [ ] `python3 utils/validate_cells.py` reports `long=0 no-md=0` for the notebook.
- [ ] No em dashes anywhere. No banned marketing words from the list in [CONTENT_STANDARDS.md](../docs/CONTENT_STANDARDS.md).
- [ ] Architecture diagram exists at `images/diagrams/NN_<name>.svg` and is embedded in the sub-README.
- [ ] Install the pre-commit hooks first: `pip install pre-commit && pre-commit install`.

## Good First Issues

New to the repo? Any of these are a great starting point:

- Pick a task from [ROADMAP.md](../ROADMAP.md) and open an issue saying "I'm taking this on."
- Improve the analogy in a technique's Description section.
- Add a small dataset sample to `data/` for one of the long-term memory techniques.
- Translate one sub-README into another language (open an issue first to discuss).
- Replace a stale external link with a current one.

Look for issues labeled `good first issue` on the [Issues page](https://github.com/NirDiamant/Agent_Memory_Techniques/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

## Using utils/helpers.py in new notebooks

The repo ships a small helper module at `utils/helpers.py`. New notebooks should import from it instead of re-implementing the same boilerplate. It covers:

- `load_env(required=[...])` finds and loads a `.env`, then validates required keys.
- `get_openai_client()` and `get_anthropic_client()` return configured LLM clients.
- `count_tokens(text, model=...)` counts tokens with tiktoken.
- `cosine_similarity(a, b)` works with or without numpy installed.
- `format_messages(turns)` renders a transcript for debug output.

Import in a notebook (relative to a technique folder, the helpers live two directories up):

```python
import sys, pathlib
sys.path.append(str(pathlib.Path.cwd().parent.parent))
from utils.helpers import load_env, get_openai_client, cosine_similarity

load_env(required=["OPENAI_API_KEY"])
client = get_openai_client()
```

Existing notebooks predate this module and use inline boilerplate. Refactoring them to use the helpers is welcome but not required.
