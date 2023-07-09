from tkinter import *
from tkinter import ttk
from tkinter import font
import sqlite3
import hashlib
import test
import registration #модуль с окном регистрации
import secrets
from datetime import datetime
import ttkthemes 
import sv_ttk
import db #модуль с подключением к бд


#функция генерации токена для сесии 
def generate_token():
    return secrets.token_hex(16)

def login():
    # Подключение к базе данных
    conn = sqlite3.connect('charlotte')
    # Создание курсора для выполнения запросов
    cursor = conn.cursor()
    login = login_entry.get()
    password = password_entry.get()
    global state
    #state = 0
    if enabled == "Пользователь сохранен!":
        state = enabled.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, hashed_password))
    result = cursor.fetchone()
    if result:
        login_time = datetime.now()
        user = cursor.execute("SELECT user_id FROM users WHERE login = ? AND password = ?", (login, hashed_password)).fetchone()[0]
        token = generate_token()
        cursor.execute("INSERT INTO sessions (user_id, token, login_time, save_user) VALUES (?, ?, ?, ?)", (user, token, login_time, state))
        conn.commit()
        # закрываем соединение с базой данных
        conn.close()
        test.main_window()
        window.destroy()
        

#функция открытия окна регистрации
def register():
    registration.reg_window()

#функция закрытия окна по нажатию на кнопку "cancel"
def cancel():
    window.destroy()

#функция основного окна
def login_window():
    global window
    window = Tk()
    #window.style = ttkthemes.ThemedStyle(theme="equilux")
    window.title("Charlotte 0.01v - Войти")
    icon = PhotoImage(file = "logo2.png")
    window.iconphoto(True, icon)

    #custom_font = font.Font(family="Cousine")

    # получаем размеры экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # задаем размеры окна
    window_width = 400
    window_height = 230
    # вычисляем координаты для центрирования окна
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    # задаем расположение окна и его размеры
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    #запрещаем изменение размера окна 
    window.resizable(False, False)

    #Вставляем логотип
    logo = PhotoImage(file="logo2.png")
    logo = logo.subsample(2, 2)  #уменьшение в 2 раза по x и y
    label = ttk.Label(image=logo)
    label.grid(row=0, column=0, rowspan=7)        

    login_label = ttk.Label(text="Логин:")
    login_label.grid(row=0, column=1, sticky=W, pady=5, padx=5)
    
    global login_entry
    login_entry = ttk.Entry()
    login_entry.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=5)
    
    password_label = ttk.Label(text="Пароль:") #
    password_label.grid(row=2, column=1, sticky=W, pady=5, padx=5)
    
    global password_entry
    password_entry = ttk.Entry(show="*")
    password_entry.grid(row=3, column=1, columnspan=3, sticky="nsew", padx=5)

    #warning_label = ttk.Label(text="")
    #warning_label.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

    enabled_on = "Пользователь сохранен!"
    enabled_off = "Сохранить пользователя"
    global enabled
    enabled = StringVar(value=enabled_off)

    checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled,  offvalue=enabled_off, onvalue=enabled_on)
    checkbutton.grid(row=4, column=1, columnspan=3, pady=5, padx=5)
        
    login_button = ttk.Button(text="Принять", command=login)
    login_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
        
    cancel_button = ttk.Button(text="Отмена", command=cancel)
    cancel_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
        
    register_label = ttk.Button(text="Зарегистрироваться", command=register)
    register_label.grid(row=6, column=1, columnspan=2, pady=5, sticky="nsew")

    sv_ttk.set_theme("dark")

    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()



login_window()


