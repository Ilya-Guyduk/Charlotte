import sqlite3
import hashlib
from tabs import CTkTabview as tab #модуль с окном регистрации
import widgets
import secrets
import customtkinter as ctk
from PIL import Image
import os
import button
import test
import globaldata
import pickle





class LoginTabFrame(ctk.CTkFrame):
    def __init__(self, master, close_window, log_entry, **kwargs):
        super().__init__(master,
                       corner_radius=4,
                       border_width=0, #ширина рамки
                       fg_color="transparent", #цвет фона
                       **kwargs)

 		#Блок вкладки авторизации
        self.login_entry = ctk.CTkEntry(self,
                                        placeholder_text="Логин",
                                        corner_radius=3)
        self.login_entry.grid(row=0,
                          pady=(30, 10)
                          )
        self.login_entry.bind('<Key>', self.on_entry_change)
        login = self.login_entry.get()

        self.login_password_entry = ctk.CTkEntry(self,
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
        self.checkbutton_log = ctk.CTkCheckBox(self,
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
        self.login_notification = ctk.CTkLabel(self,
                                                    text="",
                                                    font=ctk.CTkFont(family="Courier new")
                                                    )
        self.login_notification.grid(row=4,
                                     sticky="nsew",
                                     columnspan=2)

        #=========================================================
        #Фрейм окна с кнопками авторизации
        self.login_button_frame = ctk.CTkFrame(self,
                                         corner_radius=0,
                                         border_width=1)
        self.login_button_frame.grid(row=5,
                               column=0,
                               sticky="nsew")
        self.login_button_frame.grid_columnconfigure((0, 1), weight=1)

        self.login_button = button.AcessButton(self.login_button_frame,
                                                text="Войти",
                                                command=log_entry)
        self.login_button.grid(row=0,
                               column=0,
                               pady=(6, 6),
                               padx=(6, 0),
                               sticky="nsew")
            
        self.cancel_button = button.CancelButton(self.login_button_frame,
                                                text="Отмена",
                                                command=close_window)
        self.cancel_button.grid(row=0,
                                column=1,
                                pady=(6, 6),
                                padx=(5, 6),
                                sticky="nsew")




    def on_entry_change(self, event):
        # Проверка, заполнены ли поля
        if self.login_entry.get() and self.login_password_entry.get():
            self.checkbutton_log.configure(state="normal")
        else:
            self.checkbutton_log.configure(state="disabled")


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

