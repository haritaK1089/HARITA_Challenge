# HARITA_Challenge
1. Infrastructure and coding challenge

The file aws_provision.yml is used to host a simple Hello World! web application on Amazon cloud. 
Task performed by the above configuration script are:
 a. Creates an EC2 instance on AWS.
 b. Installs python, apache httpd.
 c. Creates domain name for the ip address of the EC2 instance
 d. Copies the application to /var/www/html directory
 e. Copies self signed certificates to corresponding directories.
 f. Redirects all HTTP requests to HTTPS.
The prereqisites are:
 a. Any linux machine with boto boto3 and ansible installed or run environ_setup.sh file
 b. Copy inventory file named as hosts and configuration file ansible.cfg to the project folder of your choice.
 c. Copy the secret file named aws_keys.yml to project folder.
 d. Run the cmd ansible-playbook -i hosts --ask-vault-pass aws_provision.yml. Provide password aws_keys.

2. Python coding challenge

 The program valid_crd_num.py can help to find a set 16 digit valid cards. Satisfying the following criteria:
 It must start with a 4,5 or 6. 
► It must contain exactly 16 digits. 
► It must only consist of digits (0-9). 
► It may have digits in groups of 4, separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have 4 or more consecutive repeated digits.
