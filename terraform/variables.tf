variable "aws_region" {
  type    = string
  default = "us-east-1" # Europe (Ireland)
}

variable "access_key" {}

variable "secret_key" {}

variable "service_name" {
  type    = string
  default = "ai-module"
}
variable "vpc_cidr" {
  type = string
}
variable "public_subnet_cidr" {
  type = string
}
variable "private_subnet_cidr" {
  type = string
}
variable "availability_zone" {
  type = string
}
