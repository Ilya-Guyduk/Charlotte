from tkinter import *
from tkinter import ttk
import sqlite3
import hashlib
#import main_window
import secrets


        


def generate_token():
    return secrets.token_hex(16)

def login():
    # подключаемся к базе данных
    conn = sqlite3.connect('Charlotte')
    cursor = conn.cursor()

    

    login = login_entry.get()
    password = password_entry.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()


        # добавляем новую запись в таблицу
    cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, hashed_password))

    token = generate_token()
    cursor.execute("INSERT INTO sessions (token) VALUES (?)", (token))
    conn.commit()

    # закрываем соединение с базой данных
    conn.close()
    register_window.destroy()


def cancel():
    register_window.destroy()

def reg_window():
    global register_window
    register_window = Toplevel()
    register_window.title("Charlotte 0.01v")
    icon = PhotoImage(file = "logo2.png")
    register_window.iconphoto(True, icon)
    # получаем размеры экрана
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()
        # задаем размеры окна
    window_width = 500
    window_height = 400
    # вычисляем координаты для центрирования окна
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # задаем расположение окна и его размеры
    register_window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

    #login_label = ttk.Label(text="Регистрация", font=("Arial", 22))
    #login_label.pack(side=TOP, padx=5, pady=20)

        
    login_label = ttk.Label(register_window, text="Логин:", font=("Arial", 16))
    login_label.grid(row=0, column=0)
        
    login_entry = ttk.Entry(register_window)
    login_entry.grid(row=0, column=1)
    
    password_label = ttk.Label(register_window, text="Пароль:", font=("Arial", 16))
    password_label.grid(row=1, column=0, padx=5, pady=5)
        
    password_entry = ttk.Entry(register_window, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)
    
    warning_label = ttk.Label(register_window, text="")
    warning_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    login_label = ttk.Label(register_window, text="Импорт конфигурации", font=("Arial", 16))
    login_label.grid(row=2, column=0, columnspan=2, padx=6, pady=6)

    #enabled_on = "Пользователь сохранен!"
    #enabled_off = "Запомнить пользователя"
    #enabled = StringVar(register_windowm, value=enabled_off)

    #checkbutton = ttk.Checkbutton(register_windowm, textvariable=enabled, variable=enabled,  offvalue=enabled_off, onvalue=enabled_on)
    #checkbutton.grid(row=2, column=0, columnspan=2, padx=6, pady=6)
        
    login_button = ttk.Button(register_window, text="Создать", command=login)
    login_button.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        
    cancel_button = ttk.Button(register_window, text="Отмена", command=cancel)
    cancel_button.grid(row=4, column=1, padx=5, pady=5, sticky=E)

    register_window.mainloop()


