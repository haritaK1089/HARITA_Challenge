### Installation setup to run ansible and connect to aws
#!/bin/sh
sudo apt-get update
sudo apt-get install python-pip -y
pip install boto boto3 
sudo apt-get install ansible -y
