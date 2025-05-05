variable "aws_region" {
  default = "eu-west-2"
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
