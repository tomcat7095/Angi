#!/usr/bin/python
import os
from getpass import getpass

import paramiko

def deploy_key(key, server, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=username, password=password)
    client.exec_command('mkdir -p ~/.ssh/')
    client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % key)
    client.exec_command('chmod 644 ~/.ssh/authorized_keys')
    client.exec_command('chmod 700 ~/.ssh/')

key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
#username = os.getlogin()
username="dannyf"
password = getpass()
hosts = ["mysql-master01.Angi.com", 
"mysql-master02.Angi.com", 
"mysql-p-slave01.Angi.com", 
"mysql-p-slave02.Angi.com", 
"mysql-read01.Angi.com",
"mysql-lb-slave01.Angi.com",
"nagios.Angi.com",
"solr101.internal.east1c.aws.Angi.com",
"solr102.internal.east1c.aws.Angi.com",
"solr201.internal.east1d.aws.Angi.com",
"solr202.internal.east1d.aws.Angi.com",
"solr301.internal.east1d.aws.Angi.com",
"172.24.122.54",
"172.24.62.73",
"172.24.22.212"
]
for host in hosts:
    deploy_key(key, host, username, password)
    