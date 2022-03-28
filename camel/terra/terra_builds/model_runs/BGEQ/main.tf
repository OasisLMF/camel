

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_access_key
  region     = "eu-west-1"
}

terraform {
    backend "s3" {
    bucket = "oasislmf-terraform"
    key    = "eu-west-1/model_run/bangladeshcyclone/terraform.tfstate"
    region = "eu-west-1"
  }
}


resource "aws_network_interface" "network_interface" {
  subnet_id   = var.subnet_id
#   private_ips = ["172.16.10.100"]
  security_groups = [ var.server_security_group ]
  tags = {
    Name = "bangladesh_cyclone_model_network_interface"
  }
}


# defines the policy for the aws s3 access
data "aws_iam_policy_document" "allow_access_to_model_data" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["123456789012"]
    }

    actions = [
      "s3:GetObject",
      "s3:ListBucket",
    ]

    resources = [
      var.bucket_arm,
      "${var.bucket_arm}/*",
    ]
  }
}


resource "aws_iam_policy" "bucket_policy" {
  name        = "bangladesh-model-data-access"
  path        = "/"
  description = "Allow "

  policy = data.aws_iam_policy_document.allow_access_to_model_data.json
}


resource "aws_iam_role" "s3_access_role" {

  name = "bangladesh_eq_model"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}


resource "aws_iam_role_policy_attachment" "model_data_access_policy" {
  role       = aws_iam_role.s3_access_role.name
  policy_arn = aws_iam_policy.bucket_policy.arn
}


resource "aws_iam_instance_profile" "model_data_access_profile" {
  name = "bangladesh-cyclone-model"
  role = aws_iam_role.s3_access_role.name
}


resource "aws_instance" "main_server" {
  ami           = "ami-08ca3fed11864d6bb"
  instance_type = "t2.medium"
  key_name = "OasisProject"
  iam_instance_profile = aws_iam_instance_profile.model_data_access_profile.id
  /* security_groups = [ var.server_security_group ] */

  network_interface {
    network_interface_id = aws_network_interface.network_interface.id
    device_index         = 0
  }

  # root disk
  root_block_device {
    volume_size           = "30"
    delete_on_termination = true
  }

  tags = {
    Name = "Bangladesh Cyclone model run"
  }

  user_data = file("./server_build.sh")
}


# # creates the EBS volume 
resource "aws_ebs_volume" "ebs_volume" {
  availability_zone = aws_instance.main_server.availability_zone
  size = 30
  tags = {
    Name = "Bangladesh Cyclone model run"
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
