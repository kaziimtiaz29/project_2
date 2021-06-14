#!/bin/bash

sudo apt update
sudo apt install -y curl jq

#install docker

curl https://get.docker.com | sudo bash
sudo usermod -aG docker jenkins 

# install Docker compose
# make sure jq & curl is installed
sudo apt update
sudo apt install -y curl jq
# set which version to download (latest)
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
# download to /usr/local/bin/docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# make the file executable
sudo chmod +x /usr/local/bin/docker-compose

# docker log in
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD

#ansible
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc

sudo apt install python3-pip -y

pip3 install --user ansible