#!/usr/bin/python3
#Using PEXPECT to configure Web Servers

import pexpect

def DbConfig(ipAddr):
  #Open connection and login
  child = pexpect.spawn('ssh justincase@' + ipAddr)
  child.expect('justincase@.* password:')
  child.sendline('Password01')
  print('Sucessfully logged in')

 #Create user

  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo adduser edgoad')
  child.expect('\[sudo\] password for justincase:')
  child.sendline('Password01')
  child.sendline('sudo passwd edgoad')
  child.expect('New password:')
  child.sendline('RubberDuck! ')
  child.expect('Retype new password:')
  child.sendline('RubberDuck!')
  print('user succesfully created')

#Install MySQL

  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo dnf -y install https://repo.mysql.com//mysql80-community-release-fc31-1.noarch.rpm')
  print('MySQL Downloaded!')
  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo dnf -y install mysql-community-server')
  print('MySQL Installed!')
  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo systemctl start mysqld.service')
  print('MySQL Started!')
  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo systemctl enable mysqld.service')
  print('MySQL set to auto-start!')

Addresses =['192.168.0.121', '192.168.0.122']
for address in Addresses:
  DbConfig(address)
