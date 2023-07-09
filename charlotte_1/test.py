from tkinter import *
from tkinter import ttk
import ttkthemes
import treeview
import notebook
import alerts
import sv_ttk



def main_window():
	root = Tk()
	root.title("Charlotte 0.01v")
	# set window size to full screen
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry("%dx%d+0+0" % (w, h))


    # Меняем настройки сетки
	for i in range(10):
		root.rowconfigure(i, weight=1)
	for i in range(10):
		root.columnconfigure(i, weight=1)

    # Виджет 1: левый верхний угол
	treeview.treeview(root)

    # Виджет 2: левый нижний угол
    #alerts.alerts(root)

    # Виджет 3: справа
	notebook.notebook(root)

	#sv_ttk.set_theme("dark")
    
	root.mainloop()

if __name__ == "__main__":
    main_window()



