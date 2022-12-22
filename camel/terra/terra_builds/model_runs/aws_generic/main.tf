

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_access_key
  region     = var.region
}

terraform {
    backend "s3" {
    bucket = "oasislmf-terraform"
    key    = "eu-west-1/model_run/pariswindstorm/terraform.tfstate"
    region = "eu-west-1"
  }
}

module "model_server" {
  source                = "../../terraform_modules/model_server"
  server_security_group = var.server_security_group
  subnet_id             = var.subnet_id
  server_tag            = var.server_tag
  instance_type         = var.instance_type
  key_name              = var.key_name
  root_block_size       = var.root_block_size
  region                = var.region
  state_tag             = var.state_tag
#  model_server_ami      = var.model_server_ami
}

# return the IP of the server created */
output "main_server_ip" {
  value = "${module.model_server.main_server_ip}"
}
