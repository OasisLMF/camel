#!/bin/bash

sudo yum update -y
sudo yum install git -y
# sudo yum groupinstall "Development Tools" -y
sudo yum install cmake -y
sudo yum install tree -y
sudo yum install vim -y
sudo yum install tmux -y 

sudo amazon-linux-extras install postgresql10 vim epel -y
sudo yum install -y postgresql-server postgresql-devel -y

# 1 | curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

python3 pip install requests
