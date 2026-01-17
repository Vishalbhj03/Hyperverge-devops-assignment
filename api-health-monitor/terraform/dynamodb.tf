resource "aws_dynamodb_table" "api_config" {
  name         = "api_config"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "api_id"

  attribute {
    name = "api_id"
    type = "S"
  }
}

resource "aws_dynamodb_table" "api_state" {
  name         = "api_state"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "api_id"

  attribute {
    name = "api_id"
    type = "S"
  }
}

