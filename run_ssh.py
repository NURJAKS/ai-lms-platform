import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP "uptime"')
child.expect('assword:')
child.sendline('***REMOVED***')
print(child.read().decode('utf-8'))
