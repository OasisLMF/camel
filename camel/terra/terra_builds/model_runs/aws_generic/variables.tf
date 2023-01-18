

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

variable "server_tag" {
  description = "the tag that will stay on the server when built"
  type        = string
  default     = "paris windstorm model"
}

variable "instance_type" {
  description = "the type of EC2 instance that the model is going to run on"
  type        = string
  default     = "t2.medium"
}

variable "key_name" {
  description = "the name of the key that the model server will accept to SSH into"
  type        = string
  default     = "OasisProject"
}

variable "root_block_size" {
  description = "the size of the root hard drive for the model server"
  type        = string
  default     = "30"
}

variable "region" {
  description = "the AWS region where the model server is going to run"
  type        = string
  default     = "eu-west-1"
}

variable "state_tag" {
  description = "name of the path to the terraform state to tether the EC2 to the build"
  type        = string
}

#variable "model_server_ami" {
#  description = "the AMI of the model server"
#  type        = string
#  default     = data.aws_ami.ubuntu.id
#}
