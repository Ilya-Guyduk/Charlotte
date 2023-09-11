from customtkinter import CustomTkinter as ctk

def settings_menu():
    # Функция, вызываемая при выборе элемента меню
    def on_menu_select(option):
        print("Option selected:", option)

    # Создаем объект CustomTkinter
    ct = ctk()

    # Создаем кнопку
    button = ct.Button(text="...", command=lambda: ct.show_menu(button, options, on_menu_select))

    # Создаем список опций для меню
    options = ["Option 1", "Option 2", "Option 3"]

    # Добавляем кнопку на форму
    ct.add_widget(button)
    
    # Запускаем основной цикл обработки событий
    ct.start()


# Запускаем функцию создания кнопки с выпадающим меню
settings_menu()
