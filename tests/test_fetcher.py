import pytest
from source.fetcher import fetch_guardian_articles

def test_invalid_date():
    with pytest.raises(ValueError):
        fetch_guardian_articles("test_key", "AI", "2021-31-12")

def test_response_format(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self):
                return {"response": {"results": [{"id": "a1", "webTitle": "Test", "webUrl": "url", "webPublicationDate": "now"}]}}
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    results = fetch_guardian_articles("test_key", "AI")
    assert isinstance(results, list)
    assert "title" in results[0]
