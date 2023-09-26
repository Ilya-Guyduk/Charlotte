import paramiko 
import sqlite3 
import globaldata 


class SshParder():
	def add_main_data(self, svc_id=None):
		
        with sqlite3.connect('Charlotte') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ip_addr FROM SVC_CONNECTS WHERE svc_id = ?", (self.svc_id,))
            ip_addr = cursor.fetchone()[0]
            print(ip_addr)
            cursor.execute("SELECT port FROM SVC_CONNECTS WHERE svc_id = ?", (self.svc_id,))
            port = cursor.fetchone()[0]
            print(port)
            cursor.execute("SELECT svc_login FROM SVC_USERS WHERE svc_id = ?", (self.svc_id,))
            svc_login = cursor.fetchone()[0]
            print(svc_login)
            cursor.execute("SELECT svc_pass FROM SVC_USERS WHERE svc_id = ?", (self.svc_id,))
            svc_pass = cursor.fetchone()[0]
            print(svc_pass)


            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=ip_addr,
                           username=svc_login,
                               password=svc_pass,
                               port=port
                               )
            stdin, stdout, stderr = client.exec_command('hostnamectl')
            output = stdout.read().decode()

            # Распарсиваем вывод команды
            parsed_data = {}
            for line in output.split('\n'):
                if ': ' in line:
                    key, value = line.split(': ')
                    print(key, value)
                    parsed_data[key.rstrip()] = value.lstrip()
                    
            print(parsed_data)

            # Вставляем данные в таблицу
            cursor.execute('''
                INSERT INTO svc_main (svc_id, hostname, chassis, machine_id, boot_id, os, kernel, architecture)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''',(self.svc_id,
                parsed_data.get('   Static hostname', ''),
                parsed_data.get('           Chassis', ''),
                parsed_data.get('        Machine ID', ''),
                parsed_data.get('           Boot ID', ''),
                parsed_data.get('  Operating System', ''),
                parsed_data.get('            Kernel', ''),
                parsed_data.get('      Architecture', '')))