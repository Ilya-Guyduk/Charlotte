from tkinter import *
from tkinter import ttk
import sqlite3
import login
from datetime import datetime





def save_check():
	
	conn = sqlite3.connect('charlotte')
    # Создание курсора для выполнения запросов
    cursor = conn.cursor()
    # Находим самую последнюю запись с save_me = 1
	cursor.execute("SELECT user_id FROM session WHERE save_me = 1 ORDER BY login_time DESC LIMIT 1")
	user_id = cursor.fetchone()[0]

	# Находим запись пользователя с найденным user_id
	cursor.execute("SELECT login, password FROM users WHERE user_id = ?", (user_id,))
	result = cursor.fetchone()
	save_user = result[0]
	save_pass = result[1]

	# Закрываем соединение с базой данных
	conn.close()

	# Выводим результаты
	print("save_user: ", save_user)
	print("save_pass: ", save_pass)

	


save_check()