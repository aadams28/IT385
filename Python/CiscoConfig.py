#!/usr/bin/python3

import pexpect

switch_ip = "192.168.0.11"
switch_un = ""
switch_pw = ""
switch_port = "g02"

child = pexpect.spawn('ssh cisco@192.168.0.11')
child.timeout = 4
child.expect('Password:')
child.sendline('cisco')
child.expect('IT385-CSR1#')
child.sendline('config t')
child.expect('IT385-CSR1\(config\)#')
child.sendline('int g02')
child.expect('IT385-CSR1\(config-if\)#')
child.sendline('ip address 10.15.14.1 255.255.0.0')
child.expect('IT385-CSR1\(config-if\)#')
child.sendline('no shutdown')
child.expect('IT385-CSR1\(config-if\)#')
child.sendline('exit')
child.expect('IT385-CSR1\(config\)#')
child.sendline('wr mem')
child.expect('IT385-CSR1\(config\)#')