import requests
from datetime import datetime
from typing import List, Optional, Dict
import logging
from config import GUARDIAN_API_KEY, SQS_URL


API_URL = "https://content.guardianapis.com/search"

logger = logging.getLogger(__name__)

def fetch_guardian_articles(api_key: str, query: str, date_from: Optional[str] = None, page_size: int = 10) -> List[Dict]:
    params = {
        "api-key": api_key,
        "q": query,
        "page-size": page_size,
        "show-fields": "headline,trailText,byline,webPublicationDate",
    }
    if date_from:
        try:
            datetime.strptime(date_from, "%Y-%m-%d")
            params["from-date"] = date_from
        except ValueError:
            raise ValueError("date_from must be in YYYY-MM-DD format")

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    articles = data.get("response", {}).get("results", [])
    return [
        {
            "id": a["id"],
            "title": a["webTitle"],
            "url": a["webUrl"],
            "publication_date": a["webPublicationDate"],
            "section": a.get("sectionName"),
        }
        for a in articles
    ]
