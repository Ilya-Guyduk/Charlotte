import paramiko

host = '192.168.0.2'
user = 'admin'
secret = '160499'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls')
print(stdout.read().decode())
client.close()
