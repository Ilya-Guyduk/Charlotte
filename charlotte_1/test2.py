import tkinter as tk
import treeview
import notebook
import alerts
import sv_ttk



def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Пример приложения")

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

    sv_ttk.set_theme("dark")
    
    root.mainloop()

if __name__ == "__main__":
    main()