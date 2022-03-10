#!/usr/bin/env bash

# This bash script is for downloading terraform on an EC2 instance.

# get the latest version of terraform
TERRAFORM_VER=`curl -s https://api.github.com/repos/hashicorp/terraform/releases/latest |  grep tag_name | cut -d: -f2 | tr -d \"\,\v | awk '{$1=$1};1'`

# download the latest version of terraform
wget https://releases.hashicorp.com/terraform/${TERRAFORM_VER}/terraform_${TERRAFORM_VER}_linux_amd64.zip

# install unzip so we can access the zip that we have just downloaded 
sudo yum -y install unzip

# unzip the terraform that we have just downloaded
unzip terraform_${TERRAFORM_VER}_linux_amd64.zip

# move the unzipped terraform file to the bash bin 
sudo mv terraform /usr/local/bin/

# remove the zipped file that we downloaded as we do not need it anymore
rm terraform_${TERRAFORM_VER}_linux_amd64.zip
