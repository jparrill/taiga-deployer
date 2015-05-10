# taiga-deployer
A deployer tool for Taiga.io project

The Taiga server has migrated from Ubuntu to CentOS/RHEL systems and also secured, SElinux and FirewallD activated
and with context fixed.

I hope you like it ;)

## Production Deploy
Not yet...

## Vagrant deploy
For now only in CentOS 7.X systems, soon on RHEL with correct subscriptions

To test Taiga in a VM, just do the next

```sh
git clone https://github.com/padajuan/taiga-deployer.git
cd taiga-deployer/ansible
vagrant up
```

Disclaimer: This Deployer is still in Beta and only tested in a VM


## Next steps
- RHEL 7.X Systems
- Systemd service fixed (do not work propertly)
- Better code, doc, steps to do manually
- etc...
