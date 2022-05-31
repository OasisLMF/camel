#!/bin/bash

# install modules needed to run oasislmf models
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

# install and configure docker
curl -fsSL https://get.docker.com/ | sh
sudo service docker restart

sudo usermod -a -G docker ec2-user

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker

cd /home/ubuntu
PATH=$PATH:~/.local/bin

# install oasislmf
pip3 install oasislmf
pip3 install numba

# add your own python configuration for your model run below


# adding github to known hosts for github cloning
ssh-keyscan -H "github.com" >> ~/.ssh/known_hosts


# add your file configurations below. For example cloning open source github repos however, reserve password protected
# files like s3 or github repos for the run_model.py script



# write a finished flag to signal that the server build is complete. You will run into concurrency issues if you do
# not block other scripts until the flag below is present
echo FINISHED > output.txt
