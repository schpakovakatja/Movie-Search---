import json
import pytest
from src.client import ask_llm

with open("data/queries.json", "r", encoding="utf-8") as f:
    data = json.load(f)


@pytest.mark.parametrize("query", data["exact"])
def test_exact_queries(query):
    answer = ask_llm(query)
    assert len(answer) > 0


@pytest.mark.parametrize("query", data["vibe"])
def test_vibe_queries(query):
    answer = ask_llm(query)
    assert len(answer) > 10


@pytest.mark.parametrize("query", data["edge"])
def test_edge_queries(query):
    answer = ask_llm(query)
    assert answer is not None


@pytest.mark.parametrize("query", data["regression"])
def test_regression_queries(query):
    answer = ask_llm(query)

    forbidden = ["ужас", "маньяк"]
    for word in forbidden:
        assert word not in answer