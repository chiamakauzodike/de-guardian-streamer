# ============
# CREATE
# ============

# ==============
# SQS Queue
# ==============

resource "aws_sqs_queue" "articles_queue" {
  name                      = "guardian-articles-queue"
  message_retention_seconds = 259200  # 3 days
  visibility_timeout_seconds = 30
}
