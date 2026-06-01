import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP', timeout=60)
child.expect('assword:')
child.sendline('***REMOVED***')
child.expect('# ')

child.sendline('docker compose --env-file ~/projects/lms-qit/.env.deploy -f ~/projects/lms-qit/docker-compose.vps.yml exec -T db psql -U lms education_platform -c "\\dt"')
child.expect('# ')
print("DB TABLES:")
print(child.before.decode('utf-8'))

