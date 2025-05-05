from fetcher import fetch_guardian_articles
import pytest

def test_missing_query(monkeypatch):
    with pytest.raises(Exception):
        fetch_guardian_articles(api_key="fake", query=None)
