

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

variable "subnet_id" {
  description = "ID of the Subnet that we are building EC2 instances in"
  type        = string
  sensitive   = true
}

variable "state_bucket" {
    description = "The s3 bucket that is going to store the state"
    type        = string 
    sensitive   = true  
}

variable "state_key" {
    description = "The s3 key that is going to store the state"
    type        = string
    sensitive   = true
}
