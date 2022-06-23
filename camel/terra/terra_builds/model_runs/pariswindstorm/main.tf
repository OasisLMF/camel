

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_access_key
  region     = "eu-west-1"
}

terraform {
    backend "s3" {
    bucket = "oasislmf-terraform"
    key    = var.state_location
    region = "eu-west-1"
  }
}


resource "aws_network_interface" "network_interface" {
  subnet_id   = var.subnet_id
#   private_ips = ["172.16.10.100"]
  security_groups = [ var.server_security_group ]
  tags = {
    Name = "paris_windstorm_model_network_interface"
  }
}

resource "aws_instance" "main_server" {
  ami           = "ami-08ca3fed11864d6bb"
  instance_type = "t2.medium"
  key_name = "OasisProject"
  /* security_groups = [ var.server_security_group ] */

  network_interface {
    network_interface_id = aws_network_interface.network_interface.id
    device_index         = 0
  }

  # root disk
  root_block_device {
    volume_size           = "30"
    /* volume_type           = "gp2" */
    /* encrypted             = true */
    delete_on_termination = true
  }

  tags = {
    Name = "Paris windstorm model run"
  }

  user_data = file("./server_build.sh")
}


# # creates the EBS volume 
resource "aws_ebs_volume" "ebs_volume" {
  availability_zone = aws_instance.main_server.availability_zone
  size = 30
  tags = {
    Name = "paris windstorm model run"
  }
}

# # attach the volume to the EC2 instance 
resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdd"
  volume_id = aws_ebs_volume.ebs_volume.id
  instance_id = aws_instance.main_server.id
  force_detach = true
} 

# return the IP of the server created */
output "main_server_ip" {
  value = "${aws_instance.main_server.*.private_ip}"
}
