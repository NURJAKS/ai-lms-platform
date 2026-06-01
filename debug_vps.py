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

child.sendline('curl -k https://127.0.0.1 -H "Host: qazaqitacademy-edu.pp.ua"')
child.expect('# ')
print("LOCAL CURL HTTPS:")
print(child.before.decode('utf-8')[:500])

child.sendline('docker compose --env-file ~/projects/lms-qit/.env.deploy -f ~/projects/lms-qit/docker-compose.vps.yml ps')
child.expect('# ')
print("DOCKER PS:")
print(child.before.decode('utf-8'))

child.sendline('ufw status')
child.expect('# ')
print("UFW STATUS:")
print(child.before.decode('utf-8'))
