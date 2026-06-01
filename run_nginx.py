import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP', timeout=60)
child.expect('assword:')
child.sendline('***REMOVED***')
child.expect('# ')

child.sendline('systemctl status nginx --no-pager')
child.expect('# ')
print("NGINX STATUS:")
print(child.before.decode('utf-8'))

