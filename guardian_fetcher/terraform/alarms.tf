# =========
# CREATE
# =========

# ====================================
# CloudWatch Alarm for Lambda Errors
# ====================================

resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/${aws_lambda_function.guardian_fetcher.function_name}"
  retention_in_days = 7
}

resource "aws_cloudwatch_metric_alarm" "lambda_errors" {
  alarm_name          = "guardian-lambda-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
  alarm_description   = "Triggers if Lambda errors occur"
  dimensions = {
    FunctionName = aws_lambda_function.guardian_fetcher.function_name
  }
}
