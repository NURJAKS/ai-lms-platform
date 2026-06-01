import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP', timeout=60)
child.expect('assword:')
child.sendline('***REMOVED***')
child.expect('# ')

child.sendline('cat /etc/nginx/sites-available/qazaqitacademy-edu.pp.ua')
child.expect('# ')
print(child.before.decode('utf-8'))
