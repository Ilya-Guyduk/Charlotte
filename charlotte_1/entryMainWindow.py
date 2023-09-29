from tabs import CTkTabview as tab #модуль с окном регистрации
import customtkinter as ctk
from PIL import Image
import os
from entryRegistrationTab import RegistrationTabFrame
from entryLoginTab import LoginTabFrame
import sqlite3

#дефолтные настройки системы
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
#==========================================================================================

class EntryloginWindow(ctk.CTk):
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
        self.reg_window.grid(row=1,
                          padx=5,
                          pady=(0, 5),
                          column=0,
                          sticky="nsew")
        self.reg_window.add("Авторизация")
        self.reg_window.add("Регистрация")
        self.reg_window.tab("Авторизация").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.reg_window.tab("Регистрация").grid_columnconfigure(0, weight=1)

        self.login_frame = LoginTabFrame(master=self.reg_window.tab("Авторизация"),log_entry=self.log_entry, close_window=self.close_window)
        self.login_frame.grid(row=0,
                               column=0,
                               sticky="nsew")

        self.registration_frame = RegistrationTabFrame(master=self.reg_window.tab("Регистрация"), registration=self.registration, close_window=self.close_window)
        self.registration_frame.grid(row=0,
                               column=0,
                               sticky="nsew")

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
            hashed_password = hashlib.sha256(password.decode()).hexdigest()
            with sqlite3.connect('Charlotte') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO ACCOUNTS (login, password) VALUES (?, ?)", (login, hashed_password))
                self.result = cursor.fetchone()        
                self.reg_notification.configure(text="Пользователь добавлен!",
                                        text_color=("#FF8C00"))

    def log_entry(self):
        """функция входа в основное окно приложения"""
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()  

        login = LoginTabFrame.login
        password = login_password_entry.get()      
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
    
    def close_window(self):
        self.destroy()
           
if __name__ == "__main__":
    log = EntryloginWindow()   
    log.mainloop()
