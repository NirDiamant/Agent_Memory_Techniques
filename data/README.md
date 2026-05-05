# Sample Data

Small datasets used by some notebooks as demo input. Keep files under 100 KB so the repo stays lightweight.

## Files

- `sample_conversation.json` - a 10-turn conversation between a user and an assistant. Used by techniques that need a short multi-turn conversation to demonstrate memory behavior (e.g., 03 Summary Memory, 04 Summary Buffer, 21 Cross-Session).

## Adding a new sample

1. Keep the file small (< 100 KB).
2. Prefer plain JSON or CSV.
3. Document its shape in this README.
4. Reference it from the notebook that uses it with a relative path like `../../data/file.json`.
