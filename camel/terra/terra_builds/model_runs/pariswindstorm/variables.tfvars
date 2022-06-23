

variable "aws_access_key" {
  description = "Access key for AWS access"
  type        = string
  sensitive   = true
}

variable "aws_secret_access_key" {
  description = "Secret access key for AWS access"
  type        = string
  sensitive   = true
}

variable "server_security_group" {
  description = "The security group that is applied to the main server for the platform"
  type        = string
  sensitive   = true
}

variable "subnet_id" {
  description = "ID of the Subnet that we are building EC2 instances in"
  type        = string
  sensitive   = true
}

variable "state_location" {
    description = "The position in s3 where the state is stored"
    type        = string
    sensitive   = true
    default     = "eu-west-1/model_run/pariswindstorm/terraform.tfstate"
}
