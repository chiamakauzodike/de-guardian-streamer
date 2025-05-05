# ==========
# CREATE
# ==========

# ==============================
# S3 BUCKET for Lambda Code
# ==============================

resource "aws_s3_object" "lambda_zip" {
  bucket = aws_s3_bucket.lambda_bucket.id
  key    = "guardian_lambda_${random_id.suffix.hex}.zip"
  source = "${path.module}/guardian_lambda.zip"
  etag   = filemd5("${path.module}/guardian_lambda.zip")
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = "guardian-lambda-bucket-${random_id.suffix.hex}"

  force_destroy = true

  tags = {
    Environment = "dev"
    Name        = "guardian_lambda_bucket"
  }
}
