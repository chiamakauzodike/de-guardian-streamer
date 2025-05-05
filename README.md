# grad-post-programme-projects
To run terraform
cd terraform
terraform init
terraform apply -var="guardian_api_key=your_api_key_here"

This projest is aimed at building a Python-based data ingestion tool to fetch articles from The Guardian API and send the results to a message broker (AWS SNS/SQS). The tool will be modular, production-ready (PEP-8, unit-tested, secure), and suitable for AWS deployment.

Guardian Article Fetcher
A serverless Python application that retrieves relevant articles from the Guardian Open Platform API based on a search term, and publishes them to an AWS SQS queue for downstream processing by marketing, careers, or data analysis teams.

This tool is designed with extensibility, CI/CD, and AWS cloud deployment in mind. It uses AWS Lambda, SQS, and Terraform, and includes GitHub Actions for continuous integration and deployment.

Features
- Fetch up to 10 articles from the Guardian API per query
- Publish article metadata to an AWS SQS queue
- Supports optional date_from for time-bounded searches
- Python codebase with unit tests and security checks
- PEP8-compliant and production-ready
- Configurable via environment variables
- Automatically deployed via GitHub Actions CI/CD
- Terraform-managed infrastructure
- Compliant with Guardian API free tier rate limits (max 50 requests/day)
- SQS message TTL set to 3 days

Architecture
+-------------+           +---------------------------+           +-----------------+
| User Input  |  ----->   | Lambda (Guardian Fetcher) |  ----->   | AWS SQS Queue   |
+-------------+           +---------------------------+           +-----------------+
        ↑                         | Terraform Deployment                    ↓
        └──────────── GitHub Actions CI/CD Workflow ────────────────────────┘

Tech Stack
- Python 3.9+
- AWS Lambda
- AWS SQS
- Terraform (v1.5.7)
- GitHub Actions (CI/CD)
- Guardian API

Configure Secrets in GitHub
Go to your GitHub repo → Settings → Secrets and variables → Actions, and add:

. GUARDIAN_API_KEY – your free-tier API key from The Guardian
. AWS_ACCESS_KEY_ID – AWS access key
. AWS_SECRET_ACCESS_KEY – AWS secret key

Trigger Lambda
The Lambda is triggered manually via event testing or via SQS integrations.

Input JSON example:
{
  "search_term": "machine learning",
  "date_from": "2024-01-01"
}

CI/CD via GitHub Actions
A workflow at .github/workflows/deploy.yml automatically:

- Packages the Lambda function
- Initializes and applies Terraform
- Deploys updates to AWS

This runs on push to main and can be triggered manually.

Project Structure
.
├── .github/workflows/deploy.yml     # CI/CD Workflow
├── terraform/                       # Infrastructure as Code
│   ├── main.tf
│   ├── lambda.tf
│   ├── iam.tf
│   ├── sqs.tf
│   └── outputs.tf
├── lambda/
│   ├── lambda_function.py           # AWS Lambda handler
│   ├── config.py                    # Config (env parsing)
│   ├── requirements.txt             # Python dependencies
│   └── package/                     # Optional: Dependencies ZIP
├── guardian_lambda.zip              # Deployment package (ignored in .gitignore)
└── README.md
