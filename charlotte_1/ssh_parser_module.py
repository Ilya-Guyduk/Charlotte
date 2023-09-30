import paramiko 
import sqlite3 
import globaldata 


class SshParser():
    def add_main_data(self, svc_id=None, adress=None, port=None, user=None, user_pass=None):
        self.svc_id = svc_id
        self.adress = adress
        self.port = port
        self.user = user
        self.user_pass = user_pass
        print("Принято в парсер:", self.svc_id, self.adress, self.port, self.user, self.user_pass)
        client = paramiko.SSHClient()
        print("подключение")
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.adress,
                        username=self.user,
                        password=self.user_pass,
                        port=self.port
                        )
        print("передача команды hostnamectl")
        stdin, stdout, stderr = client.exec_command('hostnamectl')
        output_hostname = stdout.read().decode()

        print("передача команды lscpu")
        stdin, stdout, stderr = client.exec_command('lscpu')
        output_lscpu = stdout.read().decode()

        # Распарсиваем вывод команды hostnamectl
        parsed_data_hostname = {}
        for line in output_hostname.split('\n'):
            if ': ' in line:
                key, value = line.split(': ')
                print("Ключи:", key, "значения:", value)
                parsed_data_hostname[key.rstrip()] = value.lstrip()
                    
        print(parsed_data_hostname)

        # Распарсиваем вывод команды lscpu
        parsed_data_lscpu = {}
        for line in output_lscpu.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                print("Ключи:", key, "значения:", value)
                parsed_data_lscpu[key.strip()] = value.strip()
                    
        print(parsed_data_lscpu)

        # Вставляем данные в таблицу
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            INSERT INTO SVC_MAIN (svc_id, hostname, chassis, machine_id, boot_id, os, kernel, architecture)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',(self.svc_id,
            parsed_data_hostname.get('   Static hostname', ''),
            parsed_data_hostname.get('           Chassis', ''),
            parsed_data_hostname.get('        Machine ID', ''),
            parsed_data_hostname.get('           Boot ID', ''),
            parsed_data_hostname.get('  Operating System', ''),
            parsed_data_hostname.get('            Kernel', ''),
            parsed_data_hostname.get('      Architecture', '')))
        self.cursor.execute('''
            INSERT INTO SVC_CPU (svc_id, model_name, cpus, cores_per_socket, sockets, cpu_mhz)
            VALUES(?, ?, ?, ?, ?, ?)
        ''',(self.svc_id,
            parsed_data_lscpu.get('Model name', ''),
            parsed_data_lscpu.get('CPU(s)', ''),
            parsed_data_lscpu.get('Core(s) per socket', ''),
            parsed_data_lscpu.get('Socket(s)', ''),
            parsed_data_lscpu.get('CPU MHz', ''),
                                 ))
        self.conn.commit()
        self.conn.close()  # Закрываем соединение с базой данных

    def add_addr(self, svc_id=None, adress=None, port=None, user=None, user_pass=None):
        self.svc_id = svc_id
        self.adress = adress
        self.port = port
        self.user = user
        self.user_pass = user_pass
        print("Принято в парсер:", self.svc_id, self.adress, self.port, self.user, self.user_pass)
        client = paramiko.SSHClient()
        print("подключение")
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.adress,
                       username=self.user,
                       password=self.user_pass,
                       port=self.port
                       )
        print("передача команды")
        stdin, stdout, stderr = client.exec_command('ip addr show')
        output = stdout.read().decode()

            # Обрабатываем результат и извлекаем IP-адреса и интерфейсы
        ip_addresses = []
        interfaces = []
        for line in output.split('\n'):
            if 'inet ' in line:
                parts = line.split(' ')
                ip_address = parts[5]
                interface = parts[-1]
                ip_addresses.append(ip_address)
                interfaces.append(interface)
                print(ip_address, interface)
        # Закрываем соединение SSH
        client.close()

            
        # Добавляем IP-адреса и интерфейсы в базу данных
        for i in range(len(ip_addresses)):
            cursor.execute("INSERT INTO SVC_ADDR (svc_id, ip_addr, interface) VALUES (?, ?, ?)", (self.svc_id, ip_addresses[i], interfaces[i]))