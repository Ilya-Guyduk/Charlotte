import sqlite3
import hashlib
import main
import registration #модуль с окном регистрации
from registration import RegWindow #модуль с окном регистрации
import secrets
from datetime import datetime
#import db #модуль с подключением к бд
import customtkinter as ctk
from PIL import Image
import os
import button
import tkinter.messagebox as tkmb
import test


class loginWindow(ctk.CTk):
    #функция основного окна
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))


        self.title("Charlotte 0.01v - Войти")
        
        #self.iconify("logo2.png")
        #self.iconphoto(True, self.icon)
        #self.geometry(f"{1100}x{580}") 
        self.resizable(False, False)
        #========================================================

        #Вставляем логотип
        self.logo = ctk.CTkImage(Image.open(os.path.join(current_dir, "img", "logo2.png")),
                                 size=(140, 140))
        self.label = ctk.CTkLabel(self,
                                  image=self.logo,
                                  text=" Charlotte",
                                  font=ctk.CTkFont(family="Mont ExtraLight DEMO",size=25),
                                  compound="left")
        self.label.grid(row=0,
                        column=0,
                        padx=(5, 0),
                        pady=(10, 5),
                        sticky="nsew")        
        #=========================================================

        #Вкладки авторизации, регистрации
        self.reg_window = registration.RegWindow(self)
        self.reg_window.grid(row=1,
                             padx=5,
                             pady=(0, 5),
                             column=0,
                             sticky="nsew")
        



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


    #def on_entry_change(self, event):
    #    # Проверка, заполнены ли поля
    #    if self.login_entry.get() and self.password_entry.get():
    #        self.checkbutton.config(state="normal")
    #    else:
    #        self.checkbutton.config(state="disabled")


    #функция генерации токена для сесии 
    def generate_token(self):
        return secrets.token_hex(16)

    def log_entry(self):
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()            


        self.data_entry = registration.RegWindow(self)
        login = self.data_entry.login_entry.get()
        password = self.data_entry.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print(login)
        
        self.cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, hashed_password))
        self.result = self.cursor.fetchone()
        if self.result:
            login_time = datetime.now()
            user = self.cursor.execute("SELECT user_id FROM users WHERE login = ? AND password = ?", (login, hashed_password)).fetchone()[0]
            token = self.generate_token()

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
        else:
            print(login)

    #функция закрытия окна по нажатию на кнопку "cancel"
    def cancel(self):
        self.destroy()



if __name__ == "__main__":
    app = loginWindow()
    app.mainloop()



