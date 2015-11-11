# taiga-deployer
A deployer tool for Taiga.io project

The Taiga server has migrated from Ubuntu to CentOS/RHEL systems and also secured, SElinux and FirewallD activated
and with context fixed.

I hope you like it ;)

## Vagrant deploy for testing 
For now only in CentOS 7.X systems, soon on RHEL with correct subscriptions

To test Taiga in a VM, just do the next

```sh
# Add to hosts file in /etc/hosts an alias for 127.0.0.1 called taiga.localdomain
git clone https://github.com/padajuan/taiga-deployer.git
cd taiga-deployer/ansible
vagrant up
```

Now open your browser and call for http://taiga.localdomain:8080

The username and password from fixtures are
- User: admin
- Pass: 123123

Disclaimer: This Deployer is still in Beta and only tested in a VM


## Next steps
- RHEL 7.X Systems
- Https
- Systemd service fixed (do not work propertly)
- Better code, doc, steps to do manually
- etc...
