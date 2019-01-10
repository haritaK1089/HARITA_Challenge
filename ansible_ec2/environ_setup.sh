### Installation setup to run ansible and connect to aws
#!/bin/sh
sudo apt update
sudo apt install python-pip -y
pip install boto boto3 
sudo apt install ansible -y
