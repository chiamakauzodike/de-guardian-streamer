variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "eu-west-2"
}

variable "guardian_api_key" {
  description = "Guardian API key"
  type        = string
  sensitive   = true
}

variable "python_runtime" {
  type        = string
  default     = "python3.11"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "guardian-fetcher"
}

variable "sqs_queue_name" {
  description = "Name of the SQS queue"
  type        = string
  default     = "guardian-articles-queue"
}

variable "lambda_function_name" {
  description = "Base name for the Lambda function"
  default     = "guardian-fetcher"
}
