import os

GUARDIAN_API_KEY = os.environ.get("GUARDIAN_API_KEY")
SQS_URL = os.environ.get("SQS_URL")

if not GUARDIAN_API_KEY:
    raise EnvironmentError("Missing GUARDIAN_API_KEY env variable.")

if not SQS_URL:
    raise EnvironmentError("Missing SQS_URL env variable.")
