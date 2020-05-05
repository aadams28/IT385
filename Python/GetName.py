#!/usr/bin/python3
# Logs in to remote system and runs the hostname command

import pexpect

def GetHostName(ipAddr):
# Open connection and login
  child = pexpect.spawn('ssh justincase@' + ipAddr)
  child.expect('justincase@.* password:')
  child.sendline('Password01')
  print('Logged into system')

# Send hostname command
  child.expect('\[justincase@.*\]\$')
  child.sendline('hostname')
  print('Got hostname')


#logout
  child.expect('\[justincase@.*\]\$')
  print(child.before)
  child.sendline('exit')
  print('Logged out')

Addresses = ['192.168.0.111', '192.168.0.112', '192.168.0.121', '192.168.0.122']
for address in Addresses:
  GetHostName(address)


