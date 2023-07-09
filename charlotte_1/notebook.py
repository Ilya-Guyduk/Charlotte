from tkinter import *
from tkinter import ttk
from ttkthemes import *



def notebook(parent):
	notebook = ttk.Notebook(parent)
	notebook.grid(row=0, column=2, rowspan=10, columnspan=8, sticky="nsew")


	# создаем пару фреймвов
	frame1 = ttk.Frame(notebook)
	frame2 = ttk.Frame(notebook)
	frame3 = ttk.Frame(notebook)
	frame4 = ttk.Frame(notebook)
	frame5 = ttk.Frame(notebook)
	frame6 = ttk.Frame(notebook)
	frame7 = ttk.Frame(notebook)
	 
	frame1.pack(fill=BOTH, expand=True)
	frame2.pack(fill=BOTH, expand=True)
	frame3.pack(fill=BOTH, expand=True)
	frame4.pack(fill=BOTH, expand=True)
	frame5.pack(fill=BOTH, expand=True)
	frame6.pack(fill=BOTH, expand=True)
	frame7.pack(fill=BOTH, expand=True)

	 
	# добавляем фреймы в качестве вкладок
	notebook.add(frame1, text="Дашборд")
	notebook.add(frame2, text="Файловый менеджер")
	notebook.add(frame3, text="Процессы")
	notebook.add(frame4, text="Память")
	notebook.add(frame5, text="Нагрузка")
	notebook.add(frame6, text="RAID")
	notebook.add(frame7, text="Терминал")