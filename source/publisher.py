import os
import boto3
import json
from guardian_lambda.config import SQS_URL

# Initialize the SQS client
sqs_client = boto3.client("sqs")

def publish_to_sqs(message_body):
    """
    Publish a message to an SQS queue.
    
    Args:
    - message_body (dict): The message content to be sent to SQS, typically the article data.

    Returns:
    - dict: Response from the SQS service.
    """
    try:
        # To ensure the message_body is a dictionary and convert it to a JSON string
        if isinstance(message_body, dict):
            message_body = json.dumps(message_body)

        # Send the message to the SQS queue
        response = sqs_client.send_message(
            QueueUrl=SQS_URL,
            MessageBody=message_body
        )

        # Log the response and return it
        print(f"Message sent to SQS: {response}")
        return response

    except Exception as e:
        # Log any errors and raise an exception
        print(f"Error publishing to SQS: {str(e)}")
        raise Exception(f"Error publishing to SQS: {str(e)}")

def create_sqs_message(article):
    """
    Create a message structure for SQS to send the article data.
    
    Args:
    - article (dict): The article data fetched from the Guardian API.
    
    Returns:
    - dict: The message structure for SQS.
    """
    message = {
        "title": article.get("title"),
        "url": article.get("url"),
        "published": article.get("webPublicationDate"),
    }
    return message
