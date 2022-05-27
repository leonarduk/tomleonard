module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = var.function_name
  description   = var.function_description
  handler       = var.function_handler
  runtime       = var.function_runtime

  source_path = var.function_source

  tags = {
    Name = var.tags
  }

  environment_variables = {
  }
}

