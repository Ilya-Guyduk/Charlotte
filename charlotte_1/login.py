import sqlite3
import hashlib
from tabs import CTkTabview as tab #модуль с окном регистрации
import widgets
import secrets
#from datetime import datetime
import customtkinter as ctk
from PIL import Image
import os
import button
import test
import globaldata
import pickle

#дефолтные настройки системы
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
#==========================================================================================

class loginWindow(ctk.CTk):
    '''функция основного окна'''
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.title("Charlotte")
        #self.iconify("logo2.png")
        #self.iconphoto(True, self.icon)
        self.resizable(False, False)
        #========================================================
        #Вставляем логотип
        self.logo_reg = ctk.CTkImage(Image.open(os.path.join(current_dir, 
        												 "img",
        												 "logo2.png")),
                                 size=(130, 130))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo_reg,
                                  text=" Charlotte \n 0.01v",
                                  font=ctk.CTkFont(family="Courier new",size=23),
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
        
        #login, password = self.load_credentials()
        #Блок вкладки авторизации
        self.login_entry = ctk.CTkEntry(self.reg_window.tab("Авторизация"),
                                        placeholder_text="Логин",
                                        #textvariable=ctk.StringVar(value=login),
                                        corner_radius=3)
        self.login_entry.grid(row=0,
                          pady=(30, 10)
                          )
        self.login_entry.bind('<Key>', self.on_entry_change)

        self.login_password_entry = ctk.CTkEntry(self.reg_window.tab("Авторизация"),
                                            placeholder_text="Пароль",
                                            #textvariable=ctk.StringVar(value=password),
                                            show="*",
                                            corner_radius=3)
        self.login_password_entry.grid(row=1,
                                 pady=(10, 10)
                                 )
        self.login_password_entry.bind('<Key>', self.on_entry_change)
            
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
                              pady=(10, 10)
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
                              pady=(30, 10)
                              )
        self.reg_entry.bind('<Key>', self.on_reg_entry_change)
        
        self.password_entry = ctk.CTkEntry(self.reg_window.tab("Регистрация"),
                                            placeholder_text="Пароль",
                                            show="*",
                                            corner_radius=3)
        self.password_entry.grid(row=1,
                                 column=0,
                                 pady=(10, 10)
                                 )
        self.password_entry.bind('<Key>', self.on_reg_entry_change)

        self.password_entry_retry = ctk.CTkEntry(self.reg_window.tab("Регистрация"),
                                            placeholder_text="Повторите пароль",
                                            show="*",
                                            corner_radius=3)
        self.password_entry_retry.grid(row=2,
                                 column=0,
                                 pady=(10, 10)
                                 )
        self.password_entry_retry.bind('<Key>', self.on_reg_entry_change)

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
        self.checkbutton.grid(row=3,
                              column=0,
                              columnspan=2,
                              pady=(10, 10)
                              )
        self.checkbutton.configure(state="disabled")
    
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
        self.reg_notification.grid(row=4,
                                   pady=0,
                                   padx=0,
                                     sticky="nsew",
                                     columnspan=2)
        #=========================================================
        #Фрейм окна с кнопками авторизации
        self.login_button_frame = ctk.CTkFrame(self.reg_window.tab("Авторизация"),
                                         corner_radius=0,
                                         border_width=1)
        self.login_button_frame.grid(row=5,
                               column=0,
                               sticky="nsew")
        self.login_button_frame.grid_columnconfigure((0, 1), weight=1)

        self.login_button = button.AcessButton(self.login_button_frame,
                                                text="Войти",
                                                command=self.log_entry)
        self.login_button.grid(row=0,
                               column=0,
                               pady=(6, 6),
                               padx=(6, 0),
                               sticky="nsew")
            
        self.cancel_button = button.CancelButton(self.login_button_frame,
                                                text="Отмена",
                                                command=self.cancel)
        self.cancel_button.grid(row=0,
                                column=1,
                                pady=(6, 6),
                                padx=(5, 6),
                                sticky="nsew")

        #Фрейм окна с кнопками
        self.reg_button_frame = ctk.CTkFrame(self.reg_window.tab("Регистрация"),
                                         corner_radius=0,
                                         border_width=1)
        self.reg_button_frame.grid(row=7,
                               column=0,
                               sticky="nsew")
        self.reg_button_frame.grid_columnconfigure((0, 1), weight=1)

        self.login_button = button.AcessButton(self.reg_button_frame,
                                                text="Создать",
                                                command=self.registration)
        self.login_button.grid(row=0,
                               column=0,
                               pady=(6, 6),
                               padx=(6, 0),
                               sticky="nsew")
            
        self.cancel_button = button.CancelButton(self.reg_button_frame,
                                                text="Отмена",
                                                command=self.cancel)
        self.cancel_button.grid(row=0,
                                column=1,
                                pady=(6, 6),
                                padx=(5, 6),
                                sticky="nsew")
    #===================================================================
    #===================================================================

    def load_credentials(self):
        try:
            with open('credentials.pkl', 'rb') as file:
                credentials = pickle.load(file)
                login = credentials['login']
                password = credentials['password']
        except (FileNotFoundError, pickle.UnpicklingError):
            login = ''
            password = ''
        return login, password

    def save_credentials(self, login, password):
        credentials = {'login': login, 'password': password}
        with open('credentials.pkl', 'wb') as file:
            pickle.dump(credentials, file)

    def log_entry(self):
      """функция входа в основное окно приложения"""
      self.conn = sqlite3.connect('Charlotte')
      self.cursor = self.conn.cursor()  
      login = self.login_entry.get()
      password = self.login_password_entry.get()      
      hashed_password = hashlib.sha256(password.encode()).hexdigest()
      if not login and not password:
        self.login_notification.configure(text="Укажите данные для входа!",
                                    text_color=("#FF8C00"))
        return
      self.cursor.execute("SELECT * FROM ACCOUNTS WHERE login = ? AND password = ?", (login, hashed_password))
      self.result = self.cursor.fetchone()        
      if self.result:
        globaldata.global_id = int(self.cursor.execute("SELECT account_id FROM ACCOUNTS WHERE login = ? AND password = ?", (login, hashed_password)).fetchone()[0])
        self.conn.commit()
        self.conn.close()#закрываем соединение с базой данных
        print(globaldata.global_id)
        self.destroy()  # Закройте окно входа
        app = test.App()  # Создайте экземпляр класса основного окна
        app.mainloop()  # Запустите основное окно приложения
      else:
        self.login_notification.configure(text="Не верный логин или пароль!",
                                    text_color=("#FF8C00"))
    
    def registration(self):
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor() 
        login = self.reg_entry.get()
        password = self.password_entry.get()
        password_retry = self.password_entry_retry.get()
        if not login and not password:
            self.reg_notification.configure(text="Укажите данные для регистрации!",
                                    text_color=("#FF8C00"))
        elif not login:
            self.reg_notification.configure(text="Укажите логин!",
                                    text_color=("#FF8C00"))
        elif not password:
            self.reg_notification.configure(text="Укажите пароль!",
                                    text_color=("#FF8C00"))
        elif password != password_retry:
            self.reg_notification.configure(text="Пароли не совпадают!",
                                    text_color=("#FF8C00"))
        else:    
            hashed_password = hashlib.sha256(password.code()).hexdigest()
            with sqlite3.connect('Charlotte') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO ACCOUNTS (login, password) VALUES (?, ?)", (login, hashed_password))
                self.result = cursor.fetchone()        
                self.reg_notification.configure(text="Пользователь добавлен!",
                                        text_color=("#FF8C00"))

    #функция закрытия окна по нажатию на кнопку "cancel"
    def cancel(self):
        self.destroy()

    def open_input_dialog_event():
        pass

    def on_entry_change(self, event):
        # Проверка, заполнены ли поля
        if self.login_entry.get() and self.login_password_entry.get():
            self.checkbutton_log.configure(state="normal")
        else:
            self.checkbutton_log.configure(state="disabled")


    def on_reg_entry_change(self, event):
        # Проверка, заполнены ли поля
        if self.reg_entry.get() and self.password_entry.get() and self.password_entry_retry.get():
            self.checkbutton.configure(state="normal")
        else:
            self.checkbutton.configure(state="disabled")
            

if __name__ == "__main__":
   
    log = loginWindow()   
    log.mainloop()
