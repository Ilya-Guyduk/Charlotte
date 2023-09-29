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
import ssh_parser_module
import threading

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Добавить профиль")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_reg = ctk.CTkImage(Image.open(os.path.join(current_dir, 
                                                                                                         "img",
                                                                                                         "logo2.png")),
                                 size=(70, 70))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo_reg,
                                  text=" Charlotte",
                                  font=ctk.CTkFont(family="Mont ExtraLight DEMO",size=25),
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
        self.tabview.add("Сервер")
        self.tabview.add("Кластер")

        self.alias_svc = ctk.CTkEntry(self.tabview.tab("Сервер"),
                                            placeholder_text="Название(не обязательно)",
                                            corner_radius=3)
        self.alias_svc.grid(row=0,
                        column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")
        #комментарий к окну названия
        self.alias_desc = ctk.CTkLabel(self.tabview.tab("Сервер"),
                                                    text="Имя по умолчанию - IP-адрес",
                                                    text_color=("#5A5757")
                                                    )
        self.alias_desc.grid(row=0,
                             column=1)

        self.ip_adress = ctk.CTkEntry(self.tabview.tab("Сервер"),
                                               placeholder_text="IP-адрес",
                                               corner_radius=3)
        self.ip_adress.grid(row=1,
                        column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")
        self.port = ctk.CTkEntry(self.tabview.tab("Сервер"),
                                               placeholder_text="Порт(22 по умолчанию)",
                                               corner_radius=3)
        self.port.grid(row=1,
                        column=1,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")
        self.add_ip = button.LittleOwnButton(self.tabview.tab("Сервер"),
                                              text="+",
                                              command=self.add_entry)
        self.add_ip.grid(row=1,
                                column=2,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")

        self.user = ctk.CTkEntry(self.tabview.tab("Сервер"), 
                                           placeholder_text="Пользователь",
                                           corner_radius=3)
        self.user.grid(row=2,
                        column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")

        self.password = ctk.CTkEntry(self.tabview.tab("Сервер"),
                                               placeholder_text="Пароль",
                                               show="*",
                                               corner_radius=3)
        self.password.grid(row=2,
                           column=1,
                           padx=(10, 10),
                           pady=(10, 10),
                           sticky="nsew")

        self.add_connect = button.LittleOwnButton(self.tabview.tab("Сервер"),
                                              text="+",
                                              command=self.add_entry)
        self.add_connect.grid(row=2,
                                column=2,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")
        #==================================================================

        self.progressbar_1 = ctk.CTkProgressBar(self.tabview.tab("Сервер"), corner_radius=3)
        self.progressbar_1.grid(row=3, column=0, columnspan=2, padx=(10, 10), pady=(0, 0), sticky="ew")
        self.progressbar_1.configure(mode="indeterminnate")
        #self.progressbar_1.start()

        #окно уведомлений
        self.notification = ctk.CTkLabel(self.tabview.tab("Сервер"),
                                                    text="",
                                                    font=ctk.CTkFont(family="Courier new")
                                                    )
        self.notification.grid(sticky="nsew",
                               columnspan=2)
        #==================================================================

        #Фрейм окна с кнопками  
        self.button_frame = ctk.CTkFrame(self,
                                         corner_radius=0,
                                         border_width=1)
        self.button_frame.grid(sticky="nsew")

        self.login_button = button.AcessButton(self.button_frame,
                                                text="Создать",
                                                command=self.add_profile_with_progressbar)
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
                                                command=self.test_conf)
        self.main_button_3.grid(row=0,
                                column=3,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")

    def add_entry(self):
        self.user = ctk.CTkEntry(self.tabview.tab("Сервер"), 
                                           placeholder_text="Пользователь",
                                           corner_radius=3)
        self.user.grid(column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")

        self.password = ctk.CTkEntry(self.tabview.tab("Сервер"),
                                               placeholder_text="Пароль",
                                               show="*",
                                               corner_radius=3)
        self.password.grid(column=1,
                           padx=(10, 10),
                           pady=(10, 10),
                           sticky="nsew")

    def add_profile_with_progressbar(self):
        # Создайте новый фоновый поток для выполнения метода add_profile()
        thread = threading.Thread(target=self.add_profile)
        thread.start()

    def add_profile(self):
        """подключаемся к базе данных"""
        self.progressbar_1.start()
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()
        # получение значений полей ввода
        name = self.alias_svc.get() or self.ip_adress.get()
        adress = self.ip_adress.get()
        port = self.port.get() or 22
        user = self.user.get()
        user_pass = self.password.get()
        # валидация IP-адреса и порта
        if not adress:
            self.notification.configure(text="Не указан IP-адрес!", text_color=("#FF8C00"))
            return
        if int(port) > 65536:
            self.notification.configure(text="Невалидное значение порта!", text_color=("#FF8C00"))
            return
        # вставка данных в таблицу SVC_USERS, SVC_CONNECTS и обновление SERVERS
        if user and user_pass:
            # вставка данных в таблицу SERVERS
            self.cursor.execute("INSERT INTO SERVERS (account_id, desc_svc) VALUES (?, ?)", (globaldata.global_id, name))
            server_id = self.cursor.lastrowid
            self.cursor.execute("INSERT INTO SVC_USERS (svc_id, svc_login, svc_pass) VALUES (?, ?, ?)", (server_id, user, user_pass))
            default_user_id = self.cursor.lastrowid
            self.cursor.execute("INSERT INTO SVC_CONNECTS (svc_id, gefault_user, ip_addr, port) \
                            VALUES (?, ?, ?, ?)", (server_id, default_user_id, adress, port))
            self.cursor.execute("UPDATE SERVERS SET default_connect = ? WHERE svc_id = ?", (self.cursor.lastrowid, server_id))
            self.conn.commit()
            self.conn.close()#закрываем соединение с базой данных
            parser = ssh_parser_module.SshParser()
            parser.add_main_data(svc_id=server_id, adress=adress, port=port, user=user, user_pass=user_pass)
        else:
            self.cursor.execute("INSERT INTO SVC_CONNECTS (svc_id, ip_addr, port) VALUES (?, ?, ?)", (server_id, adress, port))
        # вывод информации о том, что сервер добавлен
        self.notification.configure(text="Сервер добавлен", text_color=("#FF8C00"))
        self.progressbar_1.stop()

    
    def test_conf(self):
        self.progressbar_1.start()
        test_name = self.alias_svc.get()
        test_adress = self.ip_adress.get()
        test_port = self.port.get()
        test_user = self.user.get()
        test_user_pass = self.password.get()
        if not test_name:
                test_name = test_adress
        if not test_port:
                test_port = 22
        if not test_adress:
            self.notification.configure(text="Не указан IP-адрес!",
                                    text_color=("#FF8C00"))
            return        
        if int(test_port) > 65536:
            self.notification.configure(text="Невалидное значение порта!",
                                    text_color=("#FF8C00"))
            return
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=test_adress,
                       username=test_user,
                       password=test_user_pass,
                       port=test_port
                       )
        stdin, stdout, stderr = client.exec_command('hostname')
        data = stdout.read().decode()
        print(data)
        client.close()
        self.progressbar_1.stop()
        test_window = ctk.CTkToplevel()
        test_window.title(test_name)
        label = ctk.CTkLabel(test_window, text=f"{data} доступен!")
        label.grid(row=0, padx=20, pady=20)
        test_window.after(100, test_window.lift)
        
    
    def cancel(self):
        """Функция выхода из окна"""
        self.destroy()