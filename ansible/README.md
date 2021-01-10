# ansible playbooks - use to configure provisioned EC2 instances by Terraform

Prerequisites:
* provisioned EC2 instances (can be deployed using Terraform template on this repo)
* Ansible
* AWS .pem key configured in /etc/ansible/ansible.cfg
* hosts file configured with added IP addresses from Terraform output in /etc/ansible/hosts
     
Run playbooks as following, using 'ansible-playbook' command: 
* deploy-users.yml
* docker-install.yml
* playbooks/clone-app.yml
* playbooks/init-app.yml
