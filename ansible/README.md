# How to deploy Taiga.io with Ansible
This playbooks will deploy Taiga software into a server that are in the inventory file "hosts" executing the site.yml as main playbook.

## Development Server

## Production Server

## Vagrant
Here you have the Ansible playbook to deploy in a Vagrant server based on RHEL7/CentOS7 System, follow this steps to test in local:

```sh
$ git clone https://github.com/padajuan/taiga-deployer.git
$ cd taiga-deployer/ansible
$ vagrant up
```
And thats it, now you have a local Taiga server ;)
