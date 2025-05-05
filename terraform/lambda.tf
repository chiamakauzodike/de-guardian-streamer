# ==================
# CREATE
# ==================

# ==============================
# Lambda Function
# ==============================

resource "aws_lambda_function" "guardian_fetcher" {
  function_name = "guardian-fetcher"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = var.python_runtime
  memory_size   = 128
  timeout       = 30

  s3_bucket     = aws_s3_bucket.lambda_bucket.id
  s3_key        = aws_s3_object.lambda_zip.key

  environment {
    variables = {
      GUARDIAN_API_KEY = var.guardian_api_key
      SQS_URL          = aws_sqs_queue.articles_queue.id
    }
  }
}
