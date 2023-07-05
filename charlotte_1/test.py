from tkinter import *
from tkinter import ttk
from ttkthemes import *



def main_window():
	root = ThemedTk(theme="equilux")
	root.title("Charlotte 0.01v")
	#root.attributes("-fullscreen", True)
	# set window size to full screen
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry("%dx%d+0+0" % (w, h))

	#main_menu.main_menu(root)
	# create widgets
	tree_frame = ttk.Frame(root, width=w/4, height=h*0.8, borderwidth=2, relief=SOLID, padding=8)
	tree_frame.columnconfigure(0, weight=1)
	tree_frame.rowconfigure(0, weight=1)
	tree = ttk.Treeview(tree_frame, show="tree")
	tree.grid(sticky="nsew")	

	# добавляем отделы
	tree.insert("", END, iid=1, text="192.168.10.1")
	tree.insert("", END, iid=2, text="192.168.10.1")
	tree.insert("", END, iid=3, text="192.168.10.1")
	tree.insert("", END, iid=4, text="192.168.10.1")
	tree.insert("", END, iid=5, text="192.168.10.1")
	tree.insert("", END, iid=6, text="192.168.10.1")
	tree.insert("", END, iid=7, text="192.168.10.1")
	tree.insert("", END, iid=8, text="192.168.10.1")
	 
	#подменю
	submenu = ["Мониторинг", "Настройки", "Пользователи" ]

	# добавляем данные
	for person in submenu:
	    tree.insert("", index=END, text=person)


	tree.insert(1, index=END, text="Мониторинг")
	tree.insert(1, index=END, text="Ностройки")
	tree.insert(1, index=END, text="Пользователь")

	






	notebook_frame = ttk.Frame(root, width=w*0.75, height=h*0.8, borderwidth=2, relief=SOLID, padding=8)
	notebook_frame.columnconfigure(0, weight=1)
	notebook_frame.rowconfigure(0, weight=1)
	notebook = ttk.Notebook(notebook_frame)
	notebook.grid(sticky="nsew")


	# создаем пару фреймвов
	frame1 = ttk.Frame(notebook)
	frame2 = ttk.Frame(notebook)
	frame3 = ttk.Frame(notebook)
	frame4 = ttk.Frame(notebook)
	frame5 = ttk.Frame(notebook)
	frame6 = ttk.Frame(notebook)
	 
	frame1.pack(fill=BOTH, expand=True)
	frame2.pack(fill=BOTH, expand=True)
	frame3.pack(fill=BOTH, expand=True)
	frame4.pack(fill=BOTH, expand=True)
	frame5.pack(fill=BOTH, expand=True)
	frame6.pack(fill=BOTH, expand=True)
	 
	# добавляем фреймы в качестве вкладок
	notebook.add(frame1, text="Терминал")
	notebook.add(frame2, text="Файловый менеджер")
	notebook.add(frame3, text="Процессы")
	notebook.add(frame4, text="Память")
	notebook.add(frame5, text="Нагрузка")
	notebook.add(frame6, text="RAID")




	

	listbox = ttk.Frame(root, width=w/4, height=h*0.2, borderwidth=1, relief=SOLID, padding=2)
	listbox.columnconfigure(0, weight=1)
	listbox.rowconfigure(0, weight=1)
	# определяем данные для отображения
	people = [
	    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
	    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
	    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
	    ]
 



	# определяем столбцы
	columns = ("Host", "Data", "Trigger")
	 
	alerts = ttk.Treeview(listbox, columns=columns, show="headings")
	alerts.grid(sticky="nsew")
	 
	# определяем заголовки
	alerts.heading("Host", text="Host", anchor=W)
	alerts.heading("Data", text="Data", anchor=W)
	alerts.heading("Trigger", text="Trigger", anchor=W)
	 
	alerts.column("#1", stretch=NO)
	alerts.column("#2", stretch=NO)
	alerts.column("#3", stretch=NO)
	 
	# добавляем данные
	for person in people:
	    alerts.insert("", END, values=person)
	 
	# добавляем вертикальную прокрутку
	scrollbar = ttk.Scrollbar(listbox, orient=VERTICAL, command=alerts.yview)
	alerts.configure(yscroll=scrollbar.set)
	scrollbar.grid(sticky="nse")



	# configure grid
	root.rowconfigure(0, weight=1)
	root.rowconfigure(1, weight=1)
	root.columnconfigure(0, weight=1)
	root.columnconfigure(1, weight=1)

	# place widgets in window
	tree_frame.grid(row=0, column=0, sticky='nsew')
	notebook_frame.grid(row=0, column=1, rowspan=2, sticky='nsew')
	listbox.grid(row=1, column=0, sticky='nsew')
	

	root.mainloop()

main_window()
