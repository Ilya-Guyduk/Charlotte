import sqlite3
import hashlib
import main
import registration #модуль с окном регистрации
import secrets
from datetime import datetime
#import db #модуль с подключением к бд
import customtkinter as ctk
from PIL import Image
import os
import button
import tkinter.messagebox as tkmb
import test

#дефолтные настройки системы
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
#==========================================================================================

class loginWindow(ctk.CTkToplevel):
    #функция основного окна
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))


        
        self.title("Charlotte 0.01v")
        #self.iconify("logo2.png")
        #self.iconphoto(True, self.icon)
        #self.geometry(f"{1100}x{580}") 
        self.resizable(False, False)
        #========================================================
        #Вставляем логотип
        self.logo = ctk.CTkImage(Image.open(os.path.join(current_dir, 
        												 "img",
        												 "logo2.png")),
                                 size=(140, 140))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo,
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
        self.reg_window = registration.RegWindow(self)
        self.reg_window.grid(row=1,
                             padx=5,
                             pady=(0, 5),
                             column=0,
                             sticky="nsew")
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


    #функция генерации токена для сесии 
    def generate_token(self):
        return secrets.token_hex(16)

    #функция смены названия кнопки
    def on_tab_change(self):
    	
    	selected_tab = tab_control.index(tab_control.select())
    	if selected_tab == 0:
        	self.login_button.configure(text='Войти')
    	elif selected_tab == 1:
        	self.login_button.configure(text='Создать')

    #
    def log_entry(self):
        self.login = self.reg_window.login_entry.get()
        self.password = self.reg_window.login_password_entry.get()

        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()            

        

        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        print(self.login, self.password)
        
        self.cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (self.login, hashed_password))
        self.result = self.cursor.fetchone()
        if self.result:
            login_time = datetime.now()
            user = self.cursor.execute("SELECT user_id FROM users WHERE login = ? AND password = ?", (self.login, hashed_password)).fetchone()[0]
            token = self.generate_token()

            self.enabled = self.reg_window.enabled
            state = 0
            if self.enabled == "Пользователь сохранен!":
                state = 1
            self.cursor.execute("INSERT INTO sessions (user_id, token, login_time, save_user) VALUES (?, ?, ?, ?)", (user, token, login_time, state))
            self.conn.commit()
            # закрываем соединение с базой данных
            self.conn.close()
            #tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
            self.destroy()  # закрыть окно входа
            test.App()
            return 6
        

    #функция закрытия окна по нажатию на кнопку "cancel"
    def cancel(self):
        self.destroy()





