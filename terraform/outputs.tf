output "lambda_function_name" {
  value = aws_lambda_function.guardian_fetcher.function_name
}

output "sqs_queue_url" {
  description = "URL of the Guardian SQS queue"
  value       = aws_sqs_queue.articles_queue.id
}

output "s3_code_bucket" {
    value = aws_s3_bucket.lambda_bucket.bucket
}

output "lambda_iam_role_name" {
  value = aws_iam_role.lambda_exec_role.name
}