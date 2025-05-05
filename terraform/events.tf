# ======================================
# Daily EventBridge (CloudWatch) Rule
# ======================================

# =========
# CREATE
# =========


# Daily EventBridge (CloudWatch) Rule

resource "aws_cloudwatch_event_rule" "daily_trigger" {
  name                = "daily-guardian-fetch"
  description         = "Trigger Lambda every morning"
  schedule_expression = "cron(0 8 * * ? *)" # 8 AM UTC daily
}

resource "aws_cloudwatch_event_target" "invoke_lambda" {
  rule      = aws_cloudwatch_event_rule.daily_trigger.name
  target_id = "GuardianLambdaDaily"
  arn       = aws_lambda_function.guardian_fetcher.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.guardian_fetcher.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.daily_trigger.arn
}
