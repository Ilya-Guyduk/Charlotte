import sqlite3


def сonnect():
    # Подключение к базе данных
    conn = sqlite3.connect('charlotte')
    # Создание курсора для выполнения запросов
    cursor = conn.cursor()