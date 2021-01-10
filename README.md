# arcusteam-test dockerized application

Prerequisites:
* local deployment: docker, docker-compose
* cloud deployment: terraform, ansible, AWSCLI

To use app locally: 
* clone this repo / extract zip
* change to cloned/extracted directory
* run 'docker-compose up -d --build'
* to print ArangoDB Collection data to output, run 'print.py', or visit 'http://localhost:5000' to view dumped output as html on flask app

To deploy app:
* cd terraform/elb
* terraform init
* terraform apply - approve and wait for infrastructure to be provisioned
* take note of ELB IP address, to be accessed after configuring EC2 instances using Ansible
* add EC2 IP addresses from output to ansible hosts - further deployment instructions are inside 'ansible' directory
* once all playbooks have been executed, access ELB IP address on port 5000 to view app's output
