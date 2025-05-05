# ========
# CREATE
# ========

# =============================
# IAM Role & Permissions
# =============================

# Generate a unique suffix for naming resources
resource "random_id" "suffix" {
  byte_length = 4
}

# IAM Role for Lambda execution
resource "aws_iam_role" "lambda_exec_role" {
  name = "guardian_lambda_exec_role-${random_id.suffix.hex}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# IAM Policy to allow publishing to SQS
resource "aws_iam_policy" "lambda_permissions" {
  name = "lambda-sqs-send-${random_id.suffix.hex}"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = "sqs:SendMessage",
        Resource = aws_sqs_queue.articles_queue.arn
      }
    ]
  })
}

# Attach the policy to the role
resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = aws_iam_policy.lambda_permissions.arn
}
