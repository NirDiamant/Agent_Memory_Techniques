"""Shared helpers used across the Agent Memory Techniques notebooks.

Import these in any notebook to skip the boilerplate of loading API keys,
creating LLM clients, counting tokens, or computing cosine similarity.

Example
-------
    from utils.helpers import (
        load_env,
        get_openai_client,
        get_anthropic_client,
        count_tokens,
        cosine_similarity,
    )

    load_env(required=["OPENAI_API_KEY"])
    client = get_openai_client()

The functions are intentionally small and explicit. Read the source if you
want to know what they do. Nothing is hidden behind a wrapper.
"""

from __future__ import annotations

import os
import pathlib
from typing import Iterable, Sequence


def load_env(
    dotenv_path: str | pathlib.Path | None = None,
    required: Sequence[str] = (),
) -> dict[str, str | None]:
    """Load a .env file into the process environment.

    Looks for a .env file in (1) the path you pass, (2) the notebook's folder,
    (3) the current working directory, (4) parent directories up to the repo root.

    Args:
        dotenv_path: Optional explicit path to a .env file. If omitted, search.
        required: Names of env vars that must be set after loading. Raises
            RuntimeError listing the missing ones if any are absent.

    Returns:
        A dict with each name in ``required`` mapped to its value (or None if
        absent and not required).
    """
    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise RuntimeError(
            "python-dotenv is not installed. Run `pip install python-dotenv` first."
        ) from exc

    if dotenv_path is None:
        # Walk up from cwd looking for .env
        here = pathlib.Path.cwd()
        for candidate in [here, *here.parents]:
            cand = candidate / ".env"
            if cand.exists():
                dotenv_path = cand
                break

    load_dotenv(dotenv_path) if dotenv_path else load_dotenv()

    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError(
            f"Missing required env vars: {', '.join(missing)}. "
            f"Copy .env.example to .env at the repo root and set them."
        )

    return {name: os.getenv(name) for name in required}


def get_openai_client(api_key_env: str = "OPENAI_API_KEY"):
    """Return a configured `openai.OpenAI` client.

    Loads the API key from ``api_key_env`` (default: OPENAI_API_KEY). Raises
    RuntimeError with a helpful message if the key is missing or the openai
    package is not installed.
    """
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "openai is not installed. Run `pip install openai` first."
        ) from exc

    key = os.getenv(api_key_env)
    if not key:
        raise RuntimeError(
            f"{api_key_env} is not set. Run `load_env(required=['{api_key_env}'])` first."
        )
    return OpenAI(api_key=key)


def get_anthropic_client(api_key_env: str = "ANTHROPIC_API_KEY"):
    """Return a configured `anthropic.Anthropic` client.

    Loads the API key from ``api_key_env`` (default: ANTHROPIC_API_KEY). Raises
    RuntimeError if the key is missing or the anthropic package is not installed.
    """
    try:
        from anthropic import Anthropic
    except ImportError as exc:
        raise RuntimeError(
            "anthropic is not installed. Run `pip install anthropic` first."
        ) from exc

    key = os.getenv(api_key_env)
    if not key:
        raise RuntimeError(
            f"{api_key_env} is not set. Run `load_env(required=['{api_key_env}'])` first."
        )
    return Anthropic(api_key=key)


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """Count tokens in ``text`` using tiktoken's encoding for ``model``.

    Falls back to the ``cl100k_base`` encoding (GPT-4 family) if the model is
    not recognised. The fallback is close enough for budgeting, even when the
    actual model is from another provider (e.g., Claude).

    Returns the integer token count.
    """
    try:
        import tiktoken
    except ImportError as exc:
        raise RuntimeError(
            "tiktoken is not installed. Run `pip install tiktoken` first."
        ) from exc

    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    """Cosine similarity between two equal-length vectors.

    Returns a float in [-1.0, 1.0]. Uses numpy if available, else a pure-Python
    fallback. Raises ValueError if the vectors have different lengths or either
    one is zero.
    """
    if len(a) != len(b):
        raise ValueError(f"vector length mismatch: {len(a)} vs {len(b)}")

    try:
        import numpy as np

        va, vb = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
        na, nb = float(np.linalg.norm(va)), float(np.linalg.norm(vb))
        if na == 0.0 or nb == 0.0:
            raise ValueError("cosine similarity is undefined for a zero vector")
        return float(np.dot(va, vb) / (na * nb))
    except ImportError:
        dot = sum(x * y for x, y in zip(a, b))
        na = sum(x * x for x in a) ** 0.5
        nb = sum(y * y for y in b) ** 0.5
        if na == 0.0 or nb == 0.0:
            raise ValueError("cosine similarity is undefined for a zero vector")
        return dot / (na * nb)


def format_messages(turns: Iterable[dict]) -> str:
    """Render a list of message dicts as a readable transcript.

    Each turn must have ``role`` and ``content`` keys. Useful for debugging
    what the agent is about to send to the model.

    Returns a string with one ``ROLE: content`` line per turn.
    """
    lines = []
    for t in turns:
        role = str(t.get("role", "?")).upper()
        content = str(t.get("content", "")).strip()
        lines.append(f"{role}: {content}")
    return "\n".join(lines)


__all__ = [
    "load_env",
    "get_openai_client",
    "get_anthropic_client",
    "count_tokens",
    "cosine_similarity",
    "format_messages",
]
