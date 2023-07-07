from tkinter import *
from tkinter import ttk



def treeview(parent):
	tree = ttk.Treeview(parent, show="tree")
	tree.grid(sticky="nsew")	

	# добавляем отделы
	tree.insert("", END, iid=1, text="192.168.10.1")

	tree.insert(1, index=END, text="Мониторинг")
	tree.insert(1, index=END, text="Ностройки")
	tree.insert(1, index=END, text="Пользователь")
