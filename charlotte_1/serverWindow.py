from tabs import CTkTabview as tab
import customtkinter as ctk
import button 
import sqlite3
import hashlib
from PIL import Image
import os 
import time
import globaldata
import paramiko



class ServerWindow(ctk.CTkToplevel):
    def __init__(self, master, svc_id=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.svc_id = svc_id
        with sqlite3.connect('Charlotte') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT desc_svc FROM SERVERS WHERE account_id = ? AND svc_id = ?", (globaldata.global_id, self.svc_id))
            server_name = cursor.fetchone()[0]

            cursor.execute("SELECT ip_addr FROM SVC_CONNECTS WHERE svc_id = ?", (self.svc_id,))
            ip_addr = cursor.fetchone()[0]
            
            cursor.execute("SELECT port FROM SVC_CONNECTS WHERE svc_id = ?", (self.svc_id,))
            port = cursor.fetchone()[0]
            
            cursor.execute("SELECT svc_login FROM SVC_USERS WHERE svc_id = ?", (self.svc_id,))
            svc_login = cursor.fetchone()[0]
           
            cursor.execute("SELECT svc_pass FROM SVC_USERS WHERE svc_id = ?", (self.svc_id,))
            svc_pass = cursor.fetchone()[0]

            cursor.execute("SELECT hostname FROM SVC_MAIN WHERE svc_id = ?", (self.svc_id,))
            svc_hostname = cursor.fetchone()[0]

            cursor.execute("SELECT os FROM SVC_MAIN WHERE svc_id = ?", (self.svc_id,))
            svc_os = cursor.fetchone()[0]

            cursor.execute("SELECT architecture FROM SVC_MAIN WHERE svc_id = ?", (self.svc_id,))
            svc_arch = cursor.fetchone()[0]

            cursor.execute("SELECT kernel FROM SVC_MAIN WHERE svc_id = ?", (self.svc_id,))
            svc_kernel = cursor.fetchone()[0]
            

        self.title(server_name)
        self.grid_rowconfigure(0, weight=0)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_reg = ctk.CTkImage(Image.open(os.path.join(current_dir, 
                                                                                                         "img",
                                                                                                         "logo2.png")),
                                 size=(30, 30))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo_reg,
                                  text=f" -> SERVER -> {svc_login}@{ip_addr} -> ✔",
                                  font=ctk.CTkFont(family="Courier new",size=17),
                                  compound="left")
        self.logo.grid(row=0,
                        column=0,
                        padx=(10, 0),
                        pady=(10, 0),
                        sticky="nsw")

        self.tabview = tab(self)
        self.tabview.grid(row=1,
                          padx=5,
                          pady=(0, 5),
                          column=0,
                          sticky="nsew")
        self.tabview.add("Описание")
        self.tabview.add("Подключения")
        self.tabview.add("Юзеры")
        self.tabview.add("Настройки")

        self.status_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text="Статус: АКТИВЕН",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.status_label.grid(row=0,
                             column=0)

        self.fs_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text=f"Имя хоста: {svc_hostname}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.fs_label.grid(row=1,
                             column=0)


        self.os_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text=f"Операционная система: {svc_os}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.os_label.grid(row=2,
                             column=0)

        self.arch_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text=f"Архитектура: {svc_arch}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.arch_label.grid(row=3,
                             column=0)

        self.arch_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text=f"Ядро: {svc_kernel}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.arch_label.grid(row=4,
                             column=0)

        #===================================================================


        self.ip_adress = ctk.CTkEntry(self.tabview.tab("Подключения"),
                                               placeholder_text="IP-адрес",
                                               corner_radius=3)
        self.ip_adress.grid(row=0,
                        column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")
        self.port = ctk.CTkEntry(self.tabview.tab("Подключения"),
                                               placeholder_text="Порт(22 по умолчанию)",
                                               corner_radius=3)
        self.port.grid(row=0,
                        column=1,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")
        self.add_ip = button.LittleOwnButton(self.tabview.tab("Подключения"),
                                              text="+",
                                              command=self.add_ip)
        self.add_ip.grid(row=0,
                                column=2,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")
        #==================================================================


        #Фрейм окна с кнопками
        self.button_frame = ctk.CTkFrame(self.tabview.tab("Описание"),
                                         corner_radius=0,
                                         border_width=1)
        self.button_frame.grid(row=7, sticky="sew", columnspan=3)

        self.login_button = button.AcessButton(self.button_frame,
                                                text="Создать",
                                                command=self.cancel)
        self.login_button.grid(row=0,
                               column=0,
                               pady=(10, 10),
                               padx=(10, 10),
                               sticky="nsew")
            
        self.cancel_button = button.CancelButton(self.button_frame,
                                                text="Назад",
                                                command=self.cancel)
        self.cancel_button.grid(row=0,
                                column=1,
                                pady=(10, 10),
                                padx=(10, 10),
                                sticky="nsew")

        self.main_button_3 = button.OwnButton(self.button_frame,
                                              text="Тест",
                                              command=self.add_main_data)
        self.main_button_3.grid(row=0,
                                column=3,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")
        #=========================================================
        #Фрейм окна с кнопками
        self.button_frame = ctk.CTkFrame(self.tabview.tab("Подключения"),
                                         corner_radius=0,
                                         border_width=1)
        self.button_frame.grid(sticky="sew", columnspan=3)

        self.login_button = button.AcessButton(self.button_frame,
                                                text="Создать",
                                                command=self.cancel)
        self.login_button.grid(row=0,
                               column=0,
                               pady=(10, 10),
                               padx=(10, 10),
                               sticky="nsew")
            
        self.cancel_button = button.CancelButton(self.button_frame,
                                                text="Назад",
                                                command=self.cancel)
        self.cancel_button.grid(row=0,
                                column=1,
                                pady=(10, 10),
                                padx=(10, 10),
                                sticky="nsew")

        self.main_button_3 = button.OwnButton(self.button_frame,
                                              text="Собрать адреса",
                                              command=self.add_addr)
        self.main_button_3.grid(row=0,
                                column=3,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")
        #=========================================================

    def add_ip(self):
        pass

    def test_conf(self):
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
            stdin, stdout, stderr = client.exec_command('hostname')
            data = stdout.read().decode()
            client.close()
            test_window = ctk.CTkToplevel()
            test_window.title(self.svc_id)
            label = ctk.CTkLabel(test_window, text=data)
            label.grid(row=0, padx=20, pady=20)
            test_window.after(100, test_window.lift)
        

    def add_addr(self):
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

    def add_main_data(self):
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

       
    #Функция выхода из окна
    def cancel(self):
        self.destroy()