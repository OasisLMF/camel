#!/bin/bash

sudo apt-get update -y
sudo apt-get install git -y
sudo apt-get install vim -y
sudo apt-get install tmux -y 
sudo apt-get install ca-certificates -y
sudo apt-get install curl -y 
sudo apt-get install gnupg -y 
sudo apt-get install lsb-release -y
sudo apt install python3.8-venv -y
sudo apt install python3-pip -y
sudo apt install awscli -y

curl -fsSL https://get.docker.com/ | sh
sudo service docker restart

sudo usermod -a -G docker ec2-user

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker

cd /home/ubuntu
PATH=$PATH:~/.local/bin

pip3 install oasislmf
pip3 install numba


sudo -u ubuntu git clone https://github.com/OasisLMF/BangladeshCyclone.git

# aws s3 cp --recursive s3://oasislmf-model-library-iki-bgwtcss1 /home/ubuntu/BangladeshCyclone/BGWTCSS1/

echo FINISHED > output.txt
