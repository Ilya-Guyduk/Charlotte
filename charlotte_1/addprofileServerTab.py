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





class AddServerTabFrame(ctk.CTkFrame):
    def __init__(self, master, cancel, **kwargs):
        super().__init__(master,
                       corner_radius=4,
                       border_width=0, #ширина рамки
                       fg_color="transparent", #цвет фона
                       **kwargs)
        #self.grid_rowconfigure((0, 1, 2,), weight=0)

        self.alias_svc = ctk.CTkEntry(self,
                                            placeholder_text="Название(не обязательно)",
                                            corner_radius=3)
        self.alias_svc.grid(row=0,
                        column=0,
                        padx=(5, 5),
                        pady=(10, 0),
                        sticky="nsew")
        #комментарий к окну названия
        self.alias_desc = ctk.CTkLabel(self,
                                                    text="Имя по умолчанию - IP-адрес",
                                                    text_color=("#5A5757")
                                                    )
        self.alias_desc.grid(row=0,
                             column=1)
        #=============================================================================

        self.entries = []  # Список для хранения созданных полей IP-адреса и порта
        self.current_row = 0
        self.connect_frame = ctk.CTkFrame(self, 
                                          corner_radius=4,
                                          border_width=1,)
        self.connect_frame.grid(row=1,
                         column=0,
                         columnspan=2,
                         padx=(5, 5),
                         pady=(5, 0),
                         sticky="nsew"
                         )
        self.add_ip_entry()  # Создаем первую пару полей

        self.add_ip = button.LittleOwnButton(self,
                                              text="+",
                                              command=self.add_ip_entry)
        self.add_ip.grid(row=1,
                                column=2,
                                padx=(5, 5),
                                pady=(5, 5),
                                sticky="nw"
                                )
        #=============================================================================

        self.entries = []  # Список для хранения созданных полей IP-адреса и порта
        self.current_row_user = 1
        self.user_frame = ctk.CTkFrame(self, 
                                          corner_radius=4,
                                          border_width=1,)
        self.user_frame.grid(row=2,
                         column=0,
                         columnspan=2,
                         padx=(5, 5),
                         pady=(5, 0),
                         sticky="nsew"
                         )
        self.add_user_entry()  # Создаем первую пару полей

        self.add_user = button.LittleOwnButton(self,
                                              text="+",
                                              command=self.add_user_entry)
        self.add_user.grid(row=2,
                                column=2,
                                padx=(5, 5),
                                pady=(5, 5),
                                sticky="nw"
                                )


        #==================================================================

        #окно уведомлений
        self.notification = ctk.CTkLabel(self,
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
        self.button_frame.grid(columnspan=3,
        					   sticky="nsew")

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
                                                command=cancel)
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

    def add_ip_entry(self):
        # Создание новых полей IP-адреса и порта
        self.new_ip_address = ctk.CTkEntry(self.connect_frame,
                                      placeholder_text="IP-адрес",
                                      corner_radius=3)
        self.new_port = ctk.CTkEntry(self.connect_frame,
                                placeholder_text="Порт(22 по умолчанию)",
                                corner_radius=3)

        self.delete = button.LittleDeleteButton(self.connect_frame,
                                           text="❌",
                                           command=lambda: self.delete_ip_entry(new_ip_address, new_port, delete))

         # Размещение новых полей в сетке
        self.new_ip_address.grid(row=self.current_row + 1, column=0, padx=(5, 5), pady=(5, 5), sticky="new")
        self.new_port.grid(row=self.current_row + 1, column=1, padx=(0, 5), pady=(5, 5), sticky="new")
        self.delete.grid(row=self.current_row + 1, column=2, padx=(0, 5), pady=(5, 5), sticky="new")
        # Добавление созданных полей в список
        self.entries.append((self.new_ip_address, self.new_port, self.delete))

        # Увеличение счетчика строк
        self.current_row += 1

    def delete_ip_entry(self, ip_address, port, delete_button):
        # Удаление полей и кнопки из сетки
        ip_address.grid_remove()
        port.grid_remove()
        delete_button.grid_remove()

        # Удаление полей и кнопки из списка
        self.entries.remove((ip_address, port, delete_button))

        # Обновление окна
        self.update()


    def add_user_entry(self):
        # Создание новых полей IP-адреса и порта
        self.new_user = ctk.CTkEntry(self.user_frame,
                                      placeholder_text="Пользователь",
                                      corner_radius=3)
        self.new_password = ctk.CTkEntry(self.user_frame,
                                placeholder_text="Пароль",
                                corner_radius=3)

        self.delete_user = button.LittleDeleteButton(self.user_frame,
                                           text="❌",
                                           command=lambda: self.delete_user_entry(new_user, new_password, delete_user))

         # Размещение новых полей в сетке
        self.new_user.grid(row=self.current_row_user + 1, column=0, padx=(5, 5), pady=(5, 5), sticky="new")
        self.new_password.grid(row=self.current_row_user + 1, column=1, padx=(0, 5), pady=(5, 5), sticky="new")
        self.delete_user.grid(row=self.current_row_user + 1, column=2, padx=(0, 5), pady=(5, 5), sticky="new")
        # Добавление созданных полей в список
        self.entries.append((self.new_user, self.new_password, self.delete_user))

        # Увеличение счетчика строк
        self.current_row_user += 1

    def delete_user_entry(self, user, password, delete_user_button):
        # Удаление полей и кнопки из сетки
        user.grid_remove()
        password.grid_remove()
        delete_user_button.grid_remove()

        # Удаление полей и кнопки из списка
        self.entries.remove((user, password, delete_user_button))

        # Обновление окна
        self.update()




    def add_profile_with_progressbar(self):
        # Создайте новый фоновый поток для выполнения метода add_profile()
        thread = threading.Thread(target=self.add_profile)
        thread.start()

    def add_profile(self):
        """подключаемся к базе данных"""
        self.progressbar_1 = ctk.CTkProgressBar(self, corner_radius=3)
        self.progressbar_1.grid(row=3, column=0, columnspan=3, padx=(10, 10), pady=(0, 0), sticky="ew")
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()
        # получение значений полей ввода
        name = self.alias_svc.get() or self.new_ip_address.get()
        adress = self.new_ip_address.get()
        port = self.new_port.get() or 22
        user = self.new_user.get()
        user_pass = self.new_password.get()
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
        self.progressbar_1.grid_remove()

    
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