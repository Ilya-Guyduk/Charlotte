from tkinter import *
from tkinter import ttk

 
root = Tk()
root.title("Charlotte")
root.attributes("-fullscreen", True)




tree = ttk.Treeview(show="tree")
tree.grid(row=0, column=0)
 
# добавляем отделы
tree.insert("", END, iid=1, text="192.168.10.1")
tree.insert("", END, iid=2, text="192.168.10.1")
tree.insert("", END, iid=3, text="192.168.10.1")
tree.insert("", END, iid=4, text="192.168.10.1")
tree.insert("", END, iid=5, text="192.168.10.1")
tree.insert("", END, iid=6, text="192.168.10.1")
tree.insert("", END, iid=7, text="192.168.10.1")
tree.insert("", END, iid=8, text="192.168.10.1")
 
# добавим сотрудников отдела
tree.insert(1, index=END, text="Мониторинг")
tree.insert(1, index=END, text="Ностройки")
tree.insert(1, index=END, text="Пользователь")

tree.insert(2, index=END, text="Bob")
tree.insert(2, index=END, text="Sam")

notebook = ttk.Notebook()
#notebook.pack(expand=True)
notebook.grid(row=0, column=4, columnspan=3, rowspan=3)


# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
 
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
 
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Python")
notebook.add(frame2, text="Java")




# определяем данные для отображения
people = [
    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
    ]
 
# определяем столбцы
columns = ("name", "age", "email")
 
alerts = ttk.Treeview(columns=columns, show="headings")
#alerts.grid(row=0, column=0, sticky="nsew")
 
# определяем заголовки
alerts.heading("name", text="Имя", anchor=W)
alerts.heading("age", text="Возраст", anchor=W)
alerts.heading("email", text="Email", anchor=W)
 
alerts.column("#1", stretch=NO, width=70)
alerts.column("#2", stretch=NO, width=60)
alerts.column("#3", stretch=NO, width=100)
 
# добавляем данные
for person in people:
    alerts.insert("", END, values=person)
 
# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(orient=VERTICAL, command=alerts.yview)
alerts.configure(yscroll=scrollbar.set)
#scrollbar.grid(row=0, column=1, sticky="ns")






word_editor = Text(height=10, wrap="word")
word_editor.grid(row=10, column=4, columnspan=3, rowspan=3)

 
root.mainloop()