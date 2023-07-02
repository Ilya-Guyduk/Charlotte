from tkinter import *
from tkinter import ttk
import sqlite3
import hashlib
import test
import registration






def login_window():

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
            #warning_label.config(text="Верный логин или пароль")
            window.destroy()
            test.main_window()
        else:
            warning_label.config(text="Неверный логин или пароль")

    def register():
        registration.reg_window()

    def cancel():
        window.destroy()

    window = Tk()
    window.title("Charlotte 0.01v - Войти")
    icon = PhotoImage(file = "logo2.png")
    window.iconphoto(True, icon)
    # получаем размеры экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # задаем размеры окна
    window_width = 410
    window_height = 570
    # вычисляем координаты для центрирования окна
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    # задаем расположение окна и его размеры
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    #Вставляем логотип
    logo = PhotoImage(file="logo2.png")
    label = ttk.Label(window, image=logo)
    label.pack(anchor=N, padx=5)
    frame = ttk.Frame(window, borderwidth=2, relief=SOLID, padding=8)
    frame.pack(side=BOTTOM, padx=5, pady=20)
        
    login_label = ttk.Label(frame, text="Логин:")
    login_label.grid(row=0, column=0)
    
    login_entry = ttk.Entry(frame)
    login_entry.grid(row=0, column=1)
    
    password_label = ttk.Label(frame, text="Пароль:")
    password_label.grid(row=1, column=0, padx=5, pady=5)
    
    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    warning_label = ttk.Label(frame, text="")
    warning_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    enabled_on = "Пользователь сохранен!"
    enabled_off = "Сохранить пользователя"
    enabled = StringVar(value=enabled_off)

    checkbutton = ttk.Checkbutton(frame, textvariable=enabled, variable=enabled,  offvalue=enabled_off, onvalue=enabled_on)
    checkbutton.grid(row=2, column=0, columnspan=2, padx=6, pady=6)
        
    login_button = ttk.Button(frame, text="Принять", command=login)
    login_button.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        
    cancel_button = ttk.Button(frame, text="Отмена", command=cancel)
    cancel_button.grid(row=4, column=1, padx=5, pady=5, sticky=E)
        
    register_label = ttk.Button(frame, text="Зарегистрироваться", command=register)
    register_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    window.mainloop()
login_window()