from tkinter import *
from tkinter import ttk
from ttkthemes import *




def alerts(parent):
	# определяем данные для отображения
	people = [
	    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
	    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
	    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
	    ]
 

	# определяем столбцы
	columns = ("Host", "Data", "Trigger")
	 
	alerts = ttk.Treeview(parent, columns=columns, show="headings")
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
	scrollbar = ttk.Scrollbar(parent, orient=VERTICAL, command=alerts.yview)
	alerts.configure(yscroll=scrollbar.set)
	scrollbar.grid(sticky="nse")