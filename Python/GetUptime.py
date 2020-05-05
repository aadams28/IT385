#!/usr/bin/python3
# Expect script using pxssh

from pexpect import pxssh

# create session and login
s = pxssh.pxssh()
s.login('192.168.0.111', 'justincase', 'Password01')
print('SSH loging succesful')

# Send command
s.sendline('uptime')
s.prompt()
print(s.before)


# logout
s.logout()

