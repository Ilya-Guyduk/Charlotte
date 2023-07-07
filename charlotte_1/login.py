from tkinter import *
from tkinter import ttk
import sqlite3
import hashlib
import test
import registration
import secrets
from datetime import datetime
import ttkthemes 



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
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, hashed_password))
    result = cursor.fetchone()
    if result:
        login_time = datetime.now()
        user = cursor.execute("SELECT user_id FROM users WHERE login = ? AND password = ?", (login, hashed_password)).fetchone()[0]
        token = generate_token()
        cursor.execute("INSERT INTO sessions (user_id, token, login_time) VALUES (?, ?, ?)", (user, token, login_time))
        conn.commit()
        window.destroy()
        test.main_window()

#функция открытия окна регистрации
def register():
    registration.reg_window()

#функция закрытия окна по нажатию на кнопку "cancel"
def cancel():
    window.destroy()

#функция основного окна
def login_window():
    window = Tk()
    window.style = ttkthemes.ThemedStyle()
    window.title("Charlotte 0.01v - Войти")
    icon = PhotoImage(file = "./img/logo2.png")
    window.iconphoto(True, icon)

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

    #Вставляем логотип
    logo = PhotoImage(file="logo2.png")
    logo = logo.subsample(1.9, 1.9)  #уменьшение в 2 раза по x и y
    label = ttk.Label(image=logo)
    label.grid(row=0, column=0, rowspan=7)        

    login_label = ttk.Label(text="Логин:")
    login_label.grid(row=0, column=1)
    
    login_entry = ttk.Entry()
    login_entry.grid(row=1, column=1, columnspan=3)
    
    password_label = ttk.Label(text="Пароль:")
    password_label.grid(row=2, column=1)
    
    password_entry = ttk.Entry(show="*")
    password_entry.grid(row=3, column=1, columnspan=3)

    #warning_label = ttk.Label(text="")
    #warning_label.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

    enabled_on = "Пользователь сохранен!"
    enabled_off = "Сохранить пользователя"
    enabled = StringVar(value=enabled_off)

    checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled,  offvalue=enabled_off, onvalue=enabled_on)
    checkbutton.grid(row=4, column=1, columnspan=3, padx=6, pady=6)
        
    login_button = ttk.Button(text="Принять", command=login)
    login_button.grid(row=5, column=1, padx=5, pady=5, sticky=W)
        
    cancel_button = ttk.Button(text="Отмена", command=cancel)
    cancel_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)
        
    register_label = ttk.Button(text="Зарегистрироваться", command=register)
    register_label.grid(row=6, column=1, columnspan=2, padx=5, pady=5)

    window.mainloop()



login_window()


