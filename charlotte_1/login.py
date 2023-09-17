import sqlite3
import hashlib
from tabs import CTkTabview as tab #модуль с окном регистрации
import widgets
import secrets
from datetime import datetime
#import db #модуль с подключением к бд
import customtkinter as ctk
from PIL import Image
import os
import button
import test
import globaldata

#дефолтные настройки системы
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
#==========================================================================================

class loginWindow(ctk.CTk):
    '''функция основного окна'''
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.title("Charlotte 0.01v")
        #self.iconify("logo2.png")
        #self.iconphoto(True, self.icon)
        self.resizable(False, False)
        #========================================================
        #Вставляем логотип
        self.logo_reg = ctk.CTkImage(Image.open(os.path.join(current_dir, 
        												 "img",
        												 "logo2.png")),
                                 size=(140, 140))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo_reg,
                                  text=" Charlotte",
                                  font=ctk.CTkFont(family="Mont ExtraLight DEMO",size=25),
                                  compound="left")
        self.logo.grid(row=0,
                        column=0,
                        padx=(5, 0),
                        pady=(10, 0),
                        sticky="nsew")        
        #=========================================================
        #Вкладки авторизации, регистрации
        self.reg_window = tab(self)
        self.reg_window.add("Авторизация")
        self.reg_window.add("Регистрация")
        self.reg_window.tab("Авторизация").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.reg_window.tab("Регистрация").grid_columnconfigure(0, weight=1)
        #self.reg_window.bind('<<NotebookTabChanged>>', self.on_tab_change)

        #Блок вкладки авторизации
        self.login_entry = ctk.CTkEntry(self.reg_window.tab("Авторизация"),
                                        placeholder_text="Пользователь",
                                        corner_radius=3)
        self.login_entry.grid(row=0,
                          pady=(30, 0)
                          )
        self.login_entry.bind('<Key>', self.on_entry_change)

        self.login_password_entry = ctk.CTkEntry(self.reg_window.tab("Авторизация"),
                                            placeholder_text="Пароль",
                                            show="*",
                                            corner_radius=3)
        self.login_password_entry.grid(row=1,
                                 pady=(10, 0)
                                 )
        self.login_password_entry.bind('<Key>', self.on_entry_change)

        self.conn_menu = widgets.SimpleMenu(self.reg_window.tab("Авторизация"),
                                            values=["Value 1", "Value 2", "Value Long Long Long"],
                                            command=self.open_input_dialog_event
                                            )
        self.conn_menu.grid(row=2,
                            pady=(10, 0)
                            )
        self.conn_menu.configure(state="disabled")

        self.enabled_on = "Пользователь сохранен!"
        self.enabled_off = "Сохранить пользователя"
        self.enabled = ctk.StringVar(value=self.enabled_off)

        self.checkbutton_log = ctk.CTkCheckBox(self.reg_window.tab("Авторизация"),
                                           textvariable=self.enabled,
                                           variable=self.enabled, 
                                           offvalue=self.enabled_off,
                                           onvalue=self.enabled_on,
                                           corner_radius=4,
                                           border_width=1,
                                           hover_color=("#FF8C00"),
                                           font=ctk.CTkFont(family="Courier new")
                                           )
        self.checkbutton_log.grid(row=3,
                              column=0,
                              columnspan=2,
                              pady=(10, 0)
                              )
        self.checkbutton_log.configure(state="disabled")

        #окно уведомлений
        self.login_notification = ctk.CTkLabel(self.reg_window.tab("Авторизация"),
                                                    text="",
                                                    font=ctk.CTkFont(family="Courier new")
                                                    )
        self.login_notification.grid(row=4,
                                     sticky="nsew",
                                     columnspan=2)
        #========================================================================

        #Блок вкладки регистрации
        self.reg_entry = ctk.CTkEntry(self.reg_window.tab("Регистрация"),
                                            placeholder_text="Логин",
                                            corner_radius=3)
        self.reg_entry.grid(row=0,
                              column=0,
                              pady=(30, 0)
                              )

        self.name_entry = ctk.CTkEntry(self.reg_window.tab("Регистрация"),
                                            placeholder_text="Имя пользователя",
                                            corner_radius=3)
        self.name_entry.grid(row=1,
                              column=0,
                              pady=(10, 0)
                              )

        
        self.password_entry = ctk.CTkEntry(self.reg_window.tab("Регистрация"),
                                            placeholder_text="Пароль",
                                            show="*",
                                            corner_radius=3)
        self.password_entry.grid(row=2,
                                 column=0,
                                 pady=(10, 0)
                                 )

        self.password_entry_retry = ctk.CTkEntry(self.reg_window.tab("Регистрация"),
                                            placeholder_text="Повторите пароль",
                                            show="*",
                                            corner_radius=3)
        self.password_entry_retry.grid(row=3,
                                 column=0,
                                 pady=(10, 0)
                                 )

        self.reg_conn_menu = widgets.SimpleMenu(self.reg_window.tab("Регистрация"),
                                            values=["Подключиться к базе", "Создать новое пространство"],
                                            command=self.open_input_dialog_event)
        self.reg_conn_menu.grid(row=4,
                            column=0,
                            pady=(10, 0)
                            )
        self.reg_conn_menu.configure(state="disabled")

        self.enabled_on = "Пользователь сохранен!"
        self.enabled_off = "Сохранить пользователя"
        self.enabled = ctk.StringVar(value=self.enabled_off)

        self.checkbutton = ctk.CTkCheckBox(self.reg_window.tab("Регистрация"),
                                           textvariable=self.enabled,
                                           variable=self.enabled, 
                                           offvalue=self.enabled_off,
                                           onvalue=self.enabled_on,
                                           corner_radius=4,
                                           border_width=1,
                                           hover_color=("#FF8C00"),
                                           font=ctk.CTkFont(family="Courier new")
                                           )
        self.checkbutton.grid(row=5,
                              column=0,
                              columnspan=2,
                              pady=(10, 20)
                              )
    
        self.reg_window.grid(row=1,
                             padx=5,
                             pady=(0, 5),
                             column=0,
                             sticky="nsew")
        #окно уведомлений
        self.reg_notification = ctk.CTkLabel(self.reg_window.tab("Регистрация"),
                                                    text="",
                                                    font=ctk.CTkFont(family="Courier new")
                                                    )
        self.reg_notification.grid(row=6,
                                     sticky="nsew",
                                     columnspan=2)
        #=========================================================
        #Фрейм окна с кнопками
        self.button_frame = ctk.CTkFrame(self,
                                         corner_radius=0,
                                         border_width=1)
        self.button_frame.grid(row=2,
                               column=0,
                               sticky="nsew")
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        self.login_button = button.AcessButton(self.button_frame,
                                                text="Войти",
                                                command=self.log_entry)
        self.login_button.grid(row=1,
                               column=0,
                               pady=(10, 10),
                               padx=(10, 10),
                               sticky="nsew")
            
        self.cancel_button = button.CancelButton(self.button_frame,
                                                text="Отмена",
                                                command=self.cancel)
        self.cancel_button.grid(row=1,
                                column=1,
                                pady=(10, 10),
                                padx=(10, 10),
                                sticky="nsew")



    def log_entry(self):
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()  

        login = self.login_entry.get()
        password = self.login_password_entry.get()      
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        self.cursor.execute("SELECT * FROM ACCOUNTS WHERE login = ? AND password = ?", (login, hashed_password))
        self.result = self.cursor.fetchone()        
        
        if self.result:
            
            user = self.cursor.execute("SELECT account_id FROM ACCOUNTS WHERE login = ? AND password = ?", (login, hashed_password)).fetchone()[0]
        
            globaldata.global_id = int(user)
           
            self.conn.commit()
            self.conn.close()#закрываем соединение с базой данных
            print(globaldata.global_id)
            self.destroy()  # Закройте окно входа
            app = test.App()  # Создайте экземпляр класса основного окна
            app.mainloop()  # Запустите основное окно приложения
        else:
            self.login_notification.configure(text="Не верные данные для входа!",
                                    text_color=("#FF8C00"))
    

    def registration(self):
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()  

        login = self.reg_entry.get()
        password = self.password_entry.get()
        password_retry = self.password_entry_retry.get()
        print(login, password)
        
        if not login:
            self.login_notification.configure(text="Укажите логин!",
                                    text_color=("#FF8C00"))
        elif not password:
            self.login_notification.configure(text="Укажите пароль!",
                                    text_color=("#FF8C00"))
        elif password != password_retry:
            self.login_notification.configure(text="Пароли не совпадают!",
                                    text_color=("#FF8C00"))
        else:    
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            self.cursor.execute("INSERT INTO ACCOUNTS (login, password) VALUES (?, ?)", (login, hashed_password))
            self.result = self.cursor.fetchone()        
        
            #user = self.cursor.execute("SELECT account_id FROM ACCOUNTS WHERE login = ? AND password = ?", (login, hashed_password)).fetchone()[0]
        
            #globaldata.global_id = int(user)
           
            self.conn.commit()
            self.conn.close()#закрываем соединение с базой данных
            self.reg_notification.configure(text="Пользователь добавлен!",
                                    text_color=("#FF8C00"))



    #функция закрытия окна по нажатию на кнопку "cancel"
    def cancel(self):
        self.destroy()

    def open_input_dialog_event():
        pass

    def on_tab_change(self, event):
        selected_tab = self.reg_window.index(self.reg_window.select())
        if selected_tab == 0:
            self.login_button.configure(text='Войти', command=self.log_entry)
        elif selected_tab:
            self.login_button.configure(text='Создать', command=self.registration)



    def on_entry_change(self, event):
        # Проверка, заполнены ли поля
        if self.login_entry.get() and self.login_password_entry.get():
            self.checkbutton_log.configure(state="normal")
            self.conn_menu.configure(state="normal")
        else:
            self.checkbutton_log.configure(state="disabled")
            self.conn_menu.configure(state="disabled")




if __name__ == "__main__":
   
    log = loginWindow()
    #root.log()    
    log.mainloop()
