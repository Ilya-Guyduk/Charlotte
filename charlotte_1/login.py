from tkinter import *
from tkinter import ttk
from tkinter import font
import sqlite3
import hashlib
import test
import registration #модуль с окном регистрации
import secrets
from datetime import datetime
import db #модуль с подключением к бд
import customtkinter as ctk
from PIL import Image
import os

class loginwindow(ctk.CTk):
    #функция основного окна
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Charlotte 0.01v - Войти")
        #self.icon = PhotoImage(file = "logo2.png")
        #self.window.iconphoto(True, self.icon)
        #self.geometry(f"{1100}x{580}") 
        self.window.resizable(False, False)

        #Вставляем логотип
        #self.logo = ctk.CTkImage(Image.open(os.path.join(current_dir, "img", "logo2.png")))
        #self.label = ctk.CTkLabel(self.window, image=self.logo)
        #self.logo.grid(row=0, column=0, rowspan=7)        

        self.login_label = ctk.CTkLabel(self.window, text="Логин:")
        self.login_label.grid(row=0, column=1, sticky=W, pady=5, padx=5)
        
        
        self.login_entry = ctk.CTkEntry(self.window)
        self.login_entry.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=5)
        
        self.password_label = ctk.CTkLabel(self.window, text="Пароль:") #
        self.password_label.grid(row=2, column=1, sticky=W, pady=5, padx=5)
        
        
        self.password_entry = ctk.CTkEntry(self.window, show="*")
        self.password_entry.grid(row=3, column=1, columnspan=3, sticky="nsew", padx=5)

        self.enabled_on = "Пользователь сохранен!"
        self.enabled_off = "Сохранить пользователя"
        self.enabled = StringVar(value=self.enabled_off)

        self.checkbutton = ctk.CTkCheckBox(self.window, textvariable=self.enabled, variable=self.enabled,  offvalue=self.enabled_off, onvalue=self.enabled_on)
        self.checkbutton.grid(row=4, column=1, columnspan=3, pady=5, padx=5)
            
        self.login_button = ctk.CTkButton(self.window, text="Принять", command=self.login)
        self.login_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
            
        self.cancel_button = ctk.CTkButton(self.window, text="Отмена", command=self.cancel)
        self.cancel_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
            
        self.register_label = ctk.CTkButton(self.window, text="Зарегистрироваться", command=self.register)
        self.register_label.grid(row=6, column=1, columnspan=2, pady=5, sticky="nsew")


        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        #self.window.mainloop()

    #функция генерации токена для сесии 
    def generate_token(self):
        return secrets.token_hex(16)

    def login(self):
        # Подключение к базе данных
        conn = sqlite3.connect('charlotte')
        # Создание курсора для выполнения запросов
        cursor = conn.cursor()
        login = self.login_entry.get()
        password = self.password_entry.get()
        global state 
        state = 0
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, hashed_password))
        result = cursor.fetchone()
        if result:
            login_time = datetime.now()
            user = cursor.execute("SELECT user_id FROM users WHERE login = ? AND password = ?", (login, hashed_password)).fetchone()[0]
            token = self.generate_token()

            if self.enabled == "Пользователь сохранен!":
                state = 1
            cursor.execute("INSERT INTO sessions (user_id, token, login_time, save_user) VALUES (?, ?, ?, ?)", (user, token, login_time, state))
            conn.commit()
            # закрываем соединение с базой данных
            conn.close()
            self.window.destroy()  # закрыть окно входа
            test.App()
            

    #функция открытия окна регистрации
    def register(self):
        registration.reg_window()

    #функция закрытия окна по нажатию на кнопку "cancel"
    def cancel(self):
        window.destroy()







