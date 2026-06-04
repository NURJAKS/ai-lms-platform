import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP', timeout=600)
child.expect('assword:')
child.sendline('***REMOVED***')
child.expect('# ')

print("Pulling changes from GitHub...")
child.sendline('cd ~/projects/lms-qit && git pull origin main')
child.expect('# ')
print(child.before.decode('utf-8'))

print("Rebuilding frontend & backend containers...")
child.sendline('cd ~/projects/lms-qit && docker compose --env-file .env.deploy -f docker-compose.vps.yml up -d --build frontend backend')
for line in child:
    sys.stdout.write(line.decode('utf-8'))
    if "Started" in line.decode('utf-8') or "Running" in line.decode('utf-8') or "Healthy" in line.decode('utf-8') or "Created" in line.decode('utf-8') or "up" in line.decode('utf-8'):
        pass
