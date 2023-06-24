from tkinter import *
from tkinter import ttk
import sqlite3
import hashlib
#import main_window
import registration


class LoginWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Charlotte 0.01v - Войти")
        icon = PhotoImage(file = "logo2.png")
        self.window.iconphoto(True, icon)
        # получаем размеры экрана
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        # задаем размеры окна
        self.window_width = 410
        self.window_height = 570
        # вычисляем координаты для центрирования окна
        x = (self.screen_width // 2) - (self.window_width // 2)
        y = (self.screen_height // 2) - (self.window_height // 2)
        # задаем расположение окна и его размеры
        self.window.geometry('{}x{}+{}+{}'.format(self.window_width, self.window_height, x, y))
        #Вставляем логотип
        self.logo = PhotoImage(file="logo2.png")
        label = ttk.Label(self.window, image=self.logo)
        label.pack(anchor=N, padx=5)


        frame = ttk.Frame(self.window, borderwidth=2, relief=SOLID, padding=8)
        frame.pack(side=BOTTOM, padx=5, pady=20)
        
        login_label = ttk.Label(frame, text="Логин:")
        login_label.grid(row=0, column=0)
        
        self.login_entry = ttk.Entry(frame)
        self.login_entry.grid(row=0, column=1)
        
        password_label = ttk.Label(frame, text="Пароль:")
        password_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.warning_label = ttk.Label(frame, text="")
        self.warning_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.enabled_on = "Пользователь сохранен!"
        self.enabled_off = "Запомнить пользователя"
        self.enabled = StringVar(value=self.enabled_off)

        checkbutton = ttk.Checkbutton(frame, textvariable=self.enabled, variable=self.enabled,  offvalue=self.enabled_off, onvalue=self.enabled_on)
        checkbutton.grid(row=2, column=0, columnspan=2, padx=6, pady=6)
        
        login_button = ttk.Button(frame, text="Принять", command=self.login)
        login_button.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        
        cancel_button = ttk.Button(frame, text="Отмена", command=self.cancel)
        cancel_button.grid(row=4, column=1, padx=5, pady=5, sticky=E)
        
        register_label = Label(frame, text="Зарегистрироваться", fg="grey")
        register_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        register_label.bind("<Button-1>", lambda event: self.register)

    def run(self):
        self.window.mainloop()

    def login(self):
        # Подключение к базе данных
        conn = sqlite3.connect('charlotte')
        # Создание курсора для выполнения запросов
        cursor = conn.cursor()
        login = self.login_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, hashed_password))
        result = cursor.fetchone()
        if result:
            self.warning_label.config(text="Верный логин или пароль")
            #self.window.destroy()
            #main_menu()
        else:
            self.warning_label.config(text="Неверный логин или пароль")


    def cancel(self):
        self.window.destroy()

    def register(self, event):
        register.RegistrationWindow()
        

#if __name__ == "__main__":
LoginWindow().run()