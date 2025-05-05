# grad-post-programme-projects
To run terraform
cd terraform
terraform init
terraform apply -var="guardian_api_key=your_api_key_here"

This projest is aimed at building a Python-based data ingestion tool to fetch articles from The Guardian API and send the results to a message broker (AWS SNS/SQS). The tool will be modular, production-ready (PEP-8, unit-tested, secure), and suitable for AWS deployment.

