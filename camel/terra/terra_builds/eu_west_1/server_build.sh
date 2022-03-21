#!/bin/bash

sudo apt-get update -y
sudo apt-get install git -y
sudo apt-get install cmake -y
sudo apt-get install tree -y
sudo apt-get install vim -y
sudo apt-get install tmux -y
sudo apt-get install lsb-release -y

curl -fsSL https://get.docker.com/ | sh
sudo service docker restart

sudo usermod -a -G docker ec2-user

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker

python3 pip install requests
