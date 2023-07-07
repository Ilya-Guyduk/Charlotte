from tkinter import *
from tkinter import ttk
import ttkthemes
import treeview
import notebook
import alerts



def main_window():
	root = Tk()
	root.style = ttkthemes.ThemedStyle(theme="equilux")
	root.title("Charlotte 0.01v")
	#root.attributes("-fullscreen", True)
	# set window size to full screen
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry("%dx%d+0+0" % (w, h))

	#main_menu.main_menu(root)
	# create widgets
	tree_frame = ttk.Frame(root, width=w/4, height=h*0.8, borderwidth=1, relief=SOLID, padding=8)
	tree_frame.columnconfigure(0, weight=1)
	tree_frame.rowconfigure(0, weight=1)
	treeview.treeview(tree_frame)
	


	notebook_frame = ttk.Frame(root, width=w*0.75, height=h*0.8, borderwidth=1, relief=SOLID, padding=8)
	notebook_frame.columnconfigure(0, weight=1)
	notebook_frame.rowconfigure(0, weight=1)
	notebook.notebook(notebook_frame)
	

	listbox = ttk.Frame(root, width=w/4, height=h*0.2, borderwidth=1, relief=SOLID, padding=2)
	listbox.columnconfigure(0, weight=1)
	listbox.rowconfigure(0, weight=1)
	alerts.alerts(listbox)
	

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
