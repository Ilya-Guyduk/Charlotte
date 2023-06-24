from tkinter import *
from tkinter import ttk
import sqlite3
import hashlib
#import main_window


class RegistrationWindow:
    def __init__(self):
        
        self.register_window = Tk()
        self.register_window.title("Charlotte 0.01v")
        icon = PhotoImage(file = "logo2.png")
        self.register_window.iconphoto(True, icon)
        # получаем размеры экрана
        self.screen_width = self.register_window.winfo_screenwidth()
        self.screen_height = self.register_window.winfo_screenheight()

        # задаем размеры окна
        self.window_width = 500
        self.window_height = 400

        # вычисляем координаты для центрирования окна
        x = (self.screen_width // 2) - (self.window_width // 2)
        y = (self.screen_height // 2) - (self.window_height // 2)

        # задаем расположение окна и его размеры
        self.register_window.geometry('{}x{}+{}+{}'.format(self.window_width, self.window_height, x, y))

        login_label = ttk.Label(self.register_window, text="Регистрация", font=("Arial", 22))
        login_label.pack(side=TOP, padx=5, pady=20)

        frame = ttk.Frame(self.register_window, borderwidth=2, relief=SOLID, padding=8)
        frame.pack(side=BOTTOM, padx=5, pady=20)
        
        login_label = ttk.Label(frame, text="Логин:", font=("Arial", 16))
        login_label.grid(row=0, column=0)
        
        self.login_entry = ttk.Entry(frame)
        self.login_entry.grid(row=0, column=1)
        
        password_label = ttk.Label(frame, text="Пароль:", font=("Arial", 16))
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

    def run(self):
        self.register_window.mainloop()

    def login(self):
        # подключаемся к базе данных
        conn = sqlite3.connect('Charlotte')
        cursor = conn.cursor()
        # создаем таблицу, если она еще не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         login TEXT NOT NULL,
                         password TEXT NOT NULL)''')

        login = self.login_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()


        # добавляем новую запись в таблицу
        cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, hashed_password))
        conn.commit()

        # закрываем соединение с базой данных
        conn.close()



    def cancel(self):
        self.register_window.destroy()
        


RegistrationWindow().run()