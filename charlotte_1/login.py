from tkinter import *
from tkinter import ttk
from tkinter import font
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

class loginwindow(ctk.CTk):
    #функция основного окна
    def __init__(self):
        super().__init__()
        self.title("Charlotte 0.01v - Войти")
        #self.icon = PhotoImage(file = "logo2.png")
        #self.window.iconphoto(True, self.icon)
        #self.geometry(f"{1100}x{580}") 
        self.resizable(False, False)

        #Вставляем логотип
        #self.logo = ctk.CTkImage(Image.open(os.path.join(current_dir, "img", "logo2.png")))
        #self.label = ctk.CTkLabel(self.window, image=self.logo)
        #self.logo.grid(row=0, column=0, rowspan=7)        

        self.login_label = ctk.CTkLabel(self, text="Логин:")
        self.login_label.grid(row=0, column=1, sticky=W, pady=5, padx=5)
        
        
        self.login_entry = ctk.CTkEntry(self)
        self.login_entry.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=5)
        
        self.password_label = ctk.CTkLabel(self, text="Пароль:") #
        self.password_label.grid(row=2, column=1, sticky=W, pady=5, padx=5)
        
        
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(row=3, column=1, columnspan=3, sticky="nsew", padx=5)

        self.enabled_on = "Пользователь сохранен!"
        self.enabled_off = "Сохранить пользователя"
        self.enabled = StringVar(value=self.enabled_off)

        self.checkbutton = ctk.CTkCheckBox(self, textvariable=self.enabled, variable=self.enabled,  offvalue=self.enabled_off, onvalue=self.enabled_on)
        self.checkbutton.grid(row=4, column=1, columnspan=3, pady=5, padx=5)
            
        self.login_button = ctk.CTkButton(self, text="Принять", command=self.login)
        self.login_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
            
        self.cancel_button = ctk.CTkButton(self, text="Отмена", command=self.cancel)
        self.cancel_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
            
        self.register_label = ctk.CTkButton(self, text="Зарегистрироваться", command=self.register)
        self.register_label.grid(row=6, column=1, columnspan=2, pady=5, sticky="nsew")


        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)


    #функция генерации токена для сесии 
    def generate_token(self):
        return secrets.token_hex(16)

    def login(self):
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()            

        self.login_entry = self.login_entry.get()
        self.password_entry = self.password_entry.get()
        self.hashed_password = hashlib.sha256(self.password_entry.encode()).hexdigest()

        
        self.cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (self.login_entry, self.hashed_password))
        self.result = self.cursor.fetchone()
        if self.result:
            self.login_time = datetime.now()
            self.user = self.cursor.execute("SELECT user_id FROM users WHERE login = ? AND password = ?", (self.login_entry, self.hashed_password)).fetchone()[0]
            self.token = self.generate_token()

            self.state = 0
            if self.enabled == "Пользователь сохранен!":
                self.state = 1
            self.cursor.execute("INSERT INTO sessions (user_id, token, login_time, save_user) VALUES (?, ?, ?, ?)", (self.user, self.token, self.login_time, self.state))
            self.conn.commit()
            # закрываем соединение с базой данных
            self.conn.close()
            self.destroy()  # закрыть окно входа
            #main.Acess()
            return 6
     
            

    #функция открытия окна регистрации
    def register(self):
        registration.reg_window()

    #функция закрытия окна по нажатию на кнопку "cancel"
    def cancel(self):
        self.destroy()






if __name__ == "__main__":
    app = loginwindow()
    #login.loginwindow()
    app.mainloop()



