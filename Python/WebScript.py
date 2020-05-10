#!/usr/bin/python3
#Using PEXPECT to configure Web Servers

import pexpect

def WebConfig(ipAddr):
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


  #Install Apache(httpd)

  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo dnf install httpd -y')
  print('Apache Installed!')
  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo systemctl start httpd.service')
  print('Apache Running!')
  child.expect('\[justincase@.*\]\$')
  child.sendline('sudo systemctl enable httpd.service')
  print('Apache set to auto-start!')

Addresses =['192.168.0.111', '192.168.0.112']
for address in Addresses:
  WebConfig(address)

