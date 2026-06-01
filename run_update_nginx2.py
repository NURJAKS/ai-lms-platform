import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP', timeout=60)
child.expect('assword:')
child.sendline('***REMOVED***')
child.expect('# ')

child.sendline('rm /etc/nginx/sites-enabled/default')
child.expect('# ')

child.sendline('nginx -t && systemctl reload nginx')
child.expect('# ')

print("NGINX RELOADED")
