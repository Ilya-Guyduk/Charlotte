from tabs import CTkTabview as tab
import customtkinter as ctk
import button 
import sqlite3
import hashlib
from PIL import Image
import os 
import time

class ServerWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.geometry("500x400")
        #self.title(title)
        self.grid_rowconfigure(0, weight=0)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_reg = ctk.CTkImage(Image.open(os.path.join(current_dir, 
                                                                                                         "img",
                                                                                                         "logo2.png")),
                                 size=(30, 30))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo_reg,
                                  text=" -> SERVER -> admin@192.168.0.1 -> V",
                                  font=ctk.CTkFont(family="Courier new",size=17),
                                  compound="left")
        self.logo.grid(row=0,
                        column=0,
                        padx=(10, 0),
                        pady=(10, 0),
                        sticky="nsw")

        #self.textbox = ctk.CTkTextbox(self,
        #                                        #width=150,
        #                                        height=50,
        #                                        corner_radius=3,
        #                                        text_color=("#5A5757")
        #                                        )
        #self.textbox.insert("0.0",
        #                    "-> " + "SERVER " + "-> " "admin@192.168.0.1 " + "-> " "V")
        #self.textbox.grid(row=0,
        #                  column=0,
        #                  padx=(10, 10),
        #                  pady=(10, 0),
        #                  sticky="nsew"
        #                  )

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
        #self.tabview.tab("Сервер").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        #self.tabview.tab("Кластер").grid_columnconfigure(0, weight=1)

        self.status_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text="Статус:",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.status_label.grid(row=0,
                             column=0)

        self.fs_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text="Файловая система:",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.fs_label.grid(row=1,
                             column=0)

        self.os_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text="Операционная система:",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.os_label.grid(row=3,
                             column=0)

        self.status_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text="АКТИВЕН",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.status_label.grid(row=0,
                             column=1)

        self.fs_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text="FHS",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.fs_label.grid(row=1,
                             column=1)

        self.os_label = ctk.CTkLabel(self.tabview.tab("Описание"),
                                                    text="LINUX",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.os_label.grid(row=3,
                             column=1)
    

        #Фрейм окна с кнопками
        self.button_frame = ctk.CTkFrame(self,
                                         corner_radius=0,
                                         border_width=1)
        self.button_frame.grid(sticky="nsew")

        self.login_button = button.AcessButton(self.button_frame,
                                                text="Создать",
                                                command=self.add_profile)
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
                                              command=self.cancel)
        self.main_button_3.grid(row=0,
                                column=3,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")


    def add_profile(self):
        # подключаемся к базе данных
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()

        #Блок с переменными для создания профиля
        name = self.alias_svc.get()
        adress = self.ip_adress.get()
        port = self.port.get()
        user = self.user.get()
        user_pass = self.password.get()
        hashed_password = hashlib.sha256(user_pass.encode()).hexdigest()

        if not name:
                name = adress
        if not port:
                port = 22
        if not adress:
            self.notification.configure(text="Не указан IP-адрес!",
                                    text_color=("#FF8C00"))
            return        
        if int(port) > 65536:
            self.notification.configure(text="Невалидное значение порта!",
                                    text_color=("#FF8C00"))
            return

        test_token = 2

        #Проверка на уже добавленный адрес-порт
        #double = self.cursor.execute("SELECT svc_id FROM SVC_CONNECTS WHERE ip_addr = ? AND port = ?", (adress, int(port))).fetchone()[0]
        #print(double)
        #if double:
        #    self.notification.configure(text="Данный адрес уже добавлен!",
        #                                text_color=("#FF8C00"))
        #    return
        

        self.cursor.execute("INSERT INTO SERVERS (account_id, desc_svc) VALUES (?, ?)", (test_token, name))
        self.conn.commit()

        server = self.cursor.execute("SELECT svc_id FROM SERVERS WHERE desc_svc = ? AND account_id = ?", (name, test_token)).fetchone()[0]

        if user and hashed_password:
            self.cursor.execute("INSERT INTO SVC_USERS (svc_id, svc_login, svc_pass) VALUES (?, ?, ?)", (server, user, hashed_password))
            self.conn.commit()
            def_user = self.cursor.execute("SELECT user_id FROM SVC_USERS WHERE svc_id = ?", (server,)).fetchone()[0]
            self.cursor.execute("INSERT INTO SVC_CONNECTS (svc_id, gefault_user, ip_addr, port) VALUES (?, ?, ?, ?)", (server, def_user, adress, port))
            def_conn = self.cursor.execute("SELECT svc_conn_id FROM SVC_CONNECTS WHERE svc_id = ?", (server,)).fetchone()[0]
            self.cursor.execute("UPDATE SERVERS SET default_connect = ? WHERE svc_id = ?", (def_conn, server))
            self.conn.commit()
        else:
            self.cursor.execute("INSERT INTO SVC_CONNECTS (svc_id, ip_addr, port) VALUES (?, ?, ?)", (server, adress, port))
            self.conn.commit()
        

        self.conn.commit()
        # закрываем соединение с базой данных
        self.conn.close()
        #Вывод информации о том, что серер добавлен
        self.notification.configure(text="Сервер добавлен",
                                   text_color=("#FF8C00"))
       
    #Функция выхода из окна
    def cancel(self):
        self.destroy()