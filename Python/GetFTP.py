#!/usr/bin/python3
# Downloads a file from FTP

import pexpect

# Open connection and login
child = pexpect.spawn('ftp ftp.redhat.com')
child.expect('Name .*:')
child.sendline('ftp')
child.expect('Password:')
child.sendline('ftp')

# Change directory and download file
child.expect('ftp> ')
child.sendline('cd /pub/redhat/linux/enterprise/7Server/en/Ansible')
child.expect('ftp>')
child.sendline('get ansible-2.5.7-1.el7ae.src.rpm')

# logout
child.expect('ftp>')
child.sendline('quit')


