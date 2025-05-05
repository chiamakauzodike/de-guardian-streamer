# ==========
# CREATE
# ==========

# ==============================
# S3 BUCKET for Lambda Code
# ==============================

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = "guardian-lambda-code-${random_id.suffix.hex}"
  force_destroy = true
}

resource "random_id" "suffix" {
  byte_length = 4
}

resource "aws_s3_object" "lambda_zip" {
  bucket = aws_s3_bucket.lambda_bucket.id
  source = "${path.module}/guardian_lambda.zip"
  key    = "guardian_lambda.zip"
  etag   = filemd5("${path.module}/guardian_lambda.zip")
}

