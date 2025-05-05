import boto3
import json
import logging
from config import GUARDIAN_API_KEY, SQS_URL


logger = logging.getLogger(__name__)

sqs = boto3.client("sqs")

class SQSArticlePublisher:
    def __init__(self, queue_url: str):
        self.queue_url = queue_url

    def publish_articles(self, articles):
        for article in articles:
            response = sqs.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(article)
            )
            logger.info(f"Sent to SQS: {article['title']} | MessageId: {response['MessageId']}")
