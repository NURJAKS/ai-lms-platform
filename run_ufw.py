import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP', timeout=60)
child.expect('assword:')
child.sendline('***REMOVED***')
child.expect('# ')

child.sendline('ufw allow 80/tcp && ufw allow 443/tcp && ufw reload')
child.expect('# ')
print("UFW STATUS:")
print(child.before.decode('utf-8'))

