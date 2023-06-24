from tkinter import *
from tkinter import ttk

root = Tk()
root.attributes("-fullscreen", True)
# set window size to full screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# create widgets
tree_frame = ttk.Frame(root, width=w/4, height=h*0.8, borderwidth=2, relief=SOLID, padding=8)
tree = ttk.Treeview(tree_frame, show="tree")
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



notebook_frame = ttk.Frame(root, width=w*0.75, height=h*0.8, borderwidth=2, relief=SOLID, padding=8)
notebook = ttk.Notebook(notebook_frame)
notebook.pack(expand=True)
#notebook.pack()


# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
 
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
 
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Первая страница")
notebook.add(frame2, text="Вторая страница")




listbox = ttk.Frame(root, width=w/4, height=h*0.2, borderwidth=2, relief=SOLID, padding=8)
text_entry = ttk.Frame(root, width=w*0.75, height=h*0.2, borderwidth=2, relief=SOLID, padding=8)

# place widgets in window
tree_frame.grid(row=0, column=0, sticky='nsew')
notebook_frame.grid(row=0, column=1, sticky='nsew')
listbox.grid(row=1, column=0, sticky='nsew')
text_entry.grid(row=1, column=1, sticky='nsew')

# configure grid
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()