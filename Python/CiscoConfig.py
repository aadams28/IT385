#!/usr/bin/python3

#Importing the necessary modules needed(In this case pexpect)
import pexpect

#Establishing SSH connection to the Cisco device(for multiple devices I can add
#more pexpect.spawns and use the same commands)
child = pexpect.spawn('ssh cisco@192.168.0.11')

#Setting how long the terminal should wait before ending the session
child.timeout = 4

#Sending the commands I need to configure basic settings on the device
child.expect('Password:')
child.sendline('cisco')
child.expect('IT385-CSR1#')
child.sendline('config t')
child.expect('IT385-CSR1\(config\)#')
child.sendline('int g02')
child.expect('IT385-CSR1\(config-if\)#')
child.sendline('ip address 10.15.13.1 255.255.0.0')
child.expect('IT385-CSR1\(config-if\)#')
child.sendline('no shutdown')
child.expect('IT385-CSR1\(config-if\)#')
child.sendline('exit')
child.expect('IT385-CSR1\(config\)#')
child.sendline('no ip domain-lookup')
child.expect('IT385-CSR1\(config\)#')
child.sendline('banner motd %No Unauthorized Access!%')
child.expect('IT385-CSR1\(config\)#')
child.sendline('service password-encryption')
child.expect('IT385-CSR1\(config\)#')
child.sendline('hostname R1')
child.expect('R1\(config\)#')
child.sendline('wr mem')
child.expect('R1\(config\)#')

#This will provide visual feedback that the configuration was successful
print('Router/Switch is configured')
