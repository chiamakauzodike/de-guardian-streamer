from guardian_fetcher.source.fetcher import fetch_guardian_articles
from publisher import SQSArticlePublisher
from config import GUARDIAN_API_KEY, SQS_URL
from dotenv import load_dotenv

def run():
    query = "machine learning"
    date_from = "2024-01-01"

    articles = fetch_guardian_articles(
        api_key=GUARDIAN_API_KEY,
        query=query,
        date_from=date_from
    )

    publisher = SQSArticlePublisher(SQS_URL)
    publisher.publish_articles(articles)
    print(f"✅ Published {len(articles)} articles to SQS.")

if __name__ == "__main__":
    run()
