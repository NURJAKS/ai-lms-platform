import pexpect
import sys

child = pexpect.spawn('ssh -o StrictHostKeyChecking=no root@SERVER_IP', timeout=60)
child.expect('assword:')
child.sendline('***REMOVED***')
child.expect('# ')

child.sendline('cp ~/projects/lms-qit/deploy/nginx-qazaqitacademy.example.conf /etc/nginx/sites-available/qazaqitacademy')
child.expect('# ')

child.sendline('sed -i "s/server_name qazaqitacademy-edu.pp.ua www.qazaqitacademy-edu.pp.ua;/server_name SERVER_IP;/g" /etc/nginx/sites-available/qazaqitacademy')
child.expect('# ')

child.sendline('ln -sf /etc/nginx/sites-available/qazaqitacademy /etc/nginx/sites-enabled/')
child.expect('# ')

child.sendline('nginx -t && systemctl reload nginx')
child.expect('# ')

print("NGINX DEPLOYED")
