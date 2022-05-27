variable "function_name" {}
variable "function_description" {}
variable "tags" {}
variable "function_source" {}
variable "function_runtime" {
  default = "python3.8"
}
variable "function_handler" {
  default = "lamda_function.lambda_handler"
}

variable "environment_variables" {
  description = "A map that defines environment variables for the Lambda Function."
  type        = map(string)
  default     = {}
}