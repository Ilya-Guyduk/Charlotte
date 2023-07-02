from tkinter import *
 

def main_menu():
	#root = Tk()
	#root.title("Charlotte")
	#root.geometry("250x150") 
	 
	main_menu = Menu()
	 
	file_menu = Menu()
	file_menu.add_command(label="Импортировать файл конфигурации")
	file_menu.add_command(label="Экспортировать файл конфигурации")
	file_menu.add_separator()
	file_menu.add_command(label="Open")
	file_menu.add_command(label="Exit")

	set_menu = Menu()
	set_menu.add_command(label="Настройки подключений")
	set_menu.add_command(label="Настройки мониторинга")
	set_menu.add_command(label="Open")
	 
	screen_menu = Menu()
	screen_menu.add_command(label="test")
	screen_menu.add_command(label="Save")
	screen_menu.add_command(label="Open")

	main_menu.add_cascade(label="Файл", menu=file_menu)
	main_menu.add_cascade(label="Настройки", menu=set_menu)
	main_menu.add_cascade(label="Внешний вид", menu=screen_menu)
	 
	#root.config(menu=main_menu)


	#root.mainloop()







#relwidth=0.33, relheight=0.25 ширина кнопки составляет треть ширины контейнера, а высота кнопки - четверть высоты контейнера