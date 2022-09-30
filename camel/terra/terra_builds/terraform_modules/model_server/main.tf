
provider "aws" {
  region = var.region
}

resource "aws_network_interface" "network_interface" {
  subnet_id   = var.subnet_id
  security_groups = [ var.server_security_group ]
  tags = {
    Name =  "${var.server_tag} interface"
  }
}

resource "aws_instance" "main_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  key_name      = var.key_name

  network_interface {
    network_interface_id = aws_network_interface.network_interface.id
    device_index         = 0
  }

  # root disk
  root_block_device {
    volume_size           = var.root_block_size
    delete_on_termination = true
  }

  tags = {
    Name = var.server_tag
  }

#  user_data = file("./server_build.sh")
}

# return the IP of the server created */
output "main_server_ip" {
  value = "${aws_instance.main_server.*.private_ip}"
}
