#!/bin/bash

sudo apt-get update 
#sudo apt install chromium-chromedriver -y
#sudo apt install python3-venv

sudo apt-get install python3-pip python3-venv -y 
#python3 -m venv venv
source venv/bin/activate
pip3 install -r test_requirements.txt

#pytest coverage server
cd server
python3 -m pytest --cov=app
cd ..

#pytest coverage service 2
cd service_2
python3 -m pytest --cov=app
cd ..

#pytest coverage service 3
cd service_3
python3 -m pytest --cov=app
cd ..

#pytest coverage service 4
cd service_4
python3 -m pytest --cov=app
cd ..


