"""Smoke tests for utils/helpers.py"""
import math
import pytest


def test_cosine_similarity_basic():
    from utils.helpers import cosine_similarity
    assert cosine_similarity([1.0, 0.0], [1.0, 0.0]) == pytest.approx(1.0)
    assert cosine_similarity([1.0, 0.0], [0.0, 1.0]) == pytest.approx(0.0)
    assert cosine_similarity([1.0, 0.0], [-1.0, 0.0]) == pytest.approx(-1.0)


def test_cosine_similarity_length_mismatch():
    from utils.helpers import cosine_similarity
    with pytest.raises(ValueError, match="length mismatch"):
        cosine_similarity([1.0, 2.0], [1.0])


def test_cosine_similarity_zero_vector():
    from utils.helpers import cosine_similarity
    with pytest.raises(ValueError, match="zero vector"):
        cosine_similarity([0.0, 0.0], [1.0, 1.0])


def test_format_messages():
    from utils.helpers import format_messages
    out = format_messages([
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "hello"},
    ])
    assert "USER: hi" in out
    assert "ASSISTANT: hello" in out


def test_load_env_missing_required(tmp_path, monkeypatch):
    """When required keys are absent the function raises a clear error."""
    from utils.helpers import load_env
    monkeypatch.delenv("AMT_HELPERS_TEST_KEY", raising=False)
    monkeypatch.chdir(tmp_path)
    # No .env file in tmp_path; require a key that isn't set
    with pytest.raises(RuntimeError, match="Missing required env vars"):
        load_env(required=["AMT_HELPERS_TEST_KEY"])


def test_load_env_returns_present(tmp_path, monkeypatch):
    from utils.helpers import load_env
    monkeypatch.setenv("AMT_HELPERS_TEST_KEY", "test-value")
    monkeypatch.chdir(tmp_path)
    result = load_env(required=["AMT_HELPERS_TEST_KEY"])
    assert result["AMT_HELPERS_TEST_KEY"] == "test-value"
