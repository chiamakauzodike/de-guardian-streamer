from fetcher import fetch_guardian_articles
from publisher import SQSArticlePublisher
from config import GUARDIAN_API_KEY, SQS_URL
import os

def lambda_handler(event, context):
    query = event.get("query")
    date_from = event.get("date_from")

    if not query:
        return {
            "statusCode": 400,
            "body": "Missing required parameter: 'query'"
        }

    try:
        articles = fetch_guardian_articles(
            api_key=GUARDIAN_API_KEY,
            query=query,
            date_from=date_from
        )

        publisher = SQSArticlePublisher(SQS_URL)
        publisher.publish_articles(articles)

        return {
            "statusCode": 200,
            "body": f"Published {len(articles)} articles to SQS"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Internal error: {str(e)}"
        }
