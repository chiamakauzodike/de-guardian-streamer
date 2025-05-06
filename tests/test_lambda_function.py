import os
import json
import pytest
import requests
from unittest.mock import patch
import boto3
from moto import mock_aws

# Set required environment variables
os.environ['GUARDIAN_API_KEY'] = 'test-api-key'
os.environ['SQS_URL'] = 'https://sqs.eu-west-2.amazonaws.com/123456789012/test-queue'

# Now import the functions to test
from guardian_lambda.lambda_function import fetch_guardian_articles, publish_to_sqs

@pytest.fixture
def sample_articles():
    return [
        {
            "id": "tech/2024/jun/01/machine-learning-success",
            "webTitle": "Machine Learning Success",
            "webUrl": "https://www.theguardian.com/tech/2024/jun/01/machine-learning-success",
        }
    ]

@mock_aws
def test_publish_to_sqs(sample_articles):
    sqs = boto3.client("sqs", region_name="eu-west-2")
    queue = sqs.create_queue(QueueName="test-queue")
    queue_url = queue["QueueUrl"]

    publish_to_sqs(sample_articles, queue_url)

    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    messages = response.get("Messages", [])
    
    assert len(messages) == 1
    body = json.loads(messages[0]["Body"])
    assert body["id"] == sample_articles[0]["id"]

@patch("requests.get")  # Mock the requests.get function
def test_fetch_articles(mock_get):
    dummy_key = "test-api-key"
    dummy_query = "latest news"
    # Set up the mock to simulate a successful API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {       
        "response": {
            "results": [
                {"title": "Article 1", "url": "https://example.com/article1"},
                {"title": "Article 2", "url": "https://example.com/article2"}
            ]
        }
    }
    articles = fetch_guardian_articles(dummy_key, dummy_query)
    assert articles["response"]["results"][0]["title"] == "Article 1"
    assert articles["response"]["results"][1]["title"] == "Article 2"
   
