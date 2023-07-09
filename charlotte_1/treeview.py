from tkinter import *
from tkinter import ttk
import sqlite3




def treeview(parent):

	conn = sqlite3.connect('charlotte')
	cursor = conn.cursor()

	# Получить данные из таблицы servers
	cursor.execute("SELECT alias FROM servers")
	rows = cursor.fetchall()
	conn.close()


	tree = ttk.Treeview(parent, show="tree")
	tree.grid(row=0, column=0, rowspan=7, columnspan=2, sticky="nsew")

	# Полученные данные из таблицы servers
	for i, row in enumerate(rows):
		alias = row[0]
		iid = i + 1

		# Вставить строки в ttk.Treeview
		tree.insert("", END, iid=iid, text=alias)


	#tree.insert(1, index=END, text="Мониторинг")
	#tree.insert(1, index=END, text="Ностройки")
	#tree.insert(1, index=END, text="Пользователь")
