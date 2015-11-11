# How to deploy Taiga.io with Ansible
This playbooks will deploy Taiga software into a server that are in the inventory file "hosts" executing the site.yml as main playbook.

## Development Server
For a development deploy, just modify the inventory file and add your node, for now we cannot make a distributd deploy, modifying the roles maybe you can, but you need deep knowledge about Ansible and Taiga itself. (only for CentOS 7, for now...)

After the inventory modification, ensure that you have the ssh-key installed in the remote node.
Also, you must check in site.yml if your group is vagrant or another one, if it's different, just change the group.
Now execute this:

```sh
$ git clone https://github.com/padajuan/taiga-deployer.git
$ cd taiga-deployer/ansible
$ ansible-playbook -i hosts -l <group_name> site.yml
```

## Production Server

## Vagrant
Here you have the Ansible playbook to deploy in a Vagrant server based on RHEL7/CentOS7 System, follow this steps to test in local:

```sh
$ git clone https://github.com/padajuan/taiga-deployer.git
$ cd taiga-deployer/ansible
$ vagrant up
```
And thats it, now you have a local Taiga server ;)
