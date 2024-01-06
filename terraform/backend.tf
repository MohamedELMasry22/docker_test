terraform {
  backend "s3" {
    bucket = "ai2-sandbox-tfstate"
    key    = "ai-tfstate"
    region = "us-east-1" # Europe (Ireland)
  }
}