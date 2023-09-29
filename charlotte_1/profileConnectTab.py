import customtkinter as ctk
import button
import addprofile
from CTkToolTip import *
import sqlite3
import globaldata

class ConnectTabFrame(ctk.CTkFrame):
    def __init__(self, master, svc_id=None, **kwargs):
        super().__init__(master,
                         corner_radius=4,
                         border_width=0,
                         fg_color="transparent",
                         **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.svc_id = svc_id
        self.entries = []  # Список для хранения созданных полей IP-адреса и порта
        self.current_row = 0

        self.connect_frame = ctk.CTkFrame(self, 
                                          corner_radius=4,
                                          border_width=1,)
        self.connect_frame.grid(row=0,
                         column=0,
                         padx=(5, 5),
                         pady=(10, 0),
                         sticky="nsew")
        self.add_entry()  # Создаем первую пару полей

        add_ip = button.LittleOwnButton(self,
                                             text="+",
                                             command=self.add_entry)
        add_ip.grid(row=0,
                         column=2,
                         padx=(5, 5),
                         pady=(10, 0),
                         sticky="new")

        save_ip = button.LittleAcessButton(self,
                                             text="✔️",
                                             command=self.add_entry)
        save_ip.grid(row=0,
                         column=4,
                         padx=(0, 10),
                         pady=(10, 0),
                         sticky="new")

    def add_entry(self):
        # Создание новых полей IP-адреса и порта
        new_ip_address = ctk.CTkEntry(self.connect_frame,
                                      placeholder_text="IP-адрес",
                                      corner_radius=3)
        new_port = ctk.CTkEntry(self.connect_frame,
                                placeholder_text="Порт(22 по умолчанию)",
                                width=90,
                                corner_radius=3)

        delete = button.LittleDeleteButton(self.connect_frame,
                                           text="❌",
                                           command=lambda: self.delete_entry(new_ip_address, new_port, delete))

        

        # Размещение новых полей в сетке
        new_ip_address.grid(row=self.current_row + 1,
                            column=0,
                            padx=(5, 5),
                            pady=(5, 5),
                            sticky="nsew")
        new_port.grid(row=self.current_row + 1,
                      column=1,
                      padx=(0, 5),
                      pady=(5, 5),
                      sticky="nsew")
        delete.grid(row=self.current_row + 1,
                    column=2,
                    padx=(0, 5),
                    pady=(5, 5),
                    sticky="nsew")

        # Добавление созданных полей в список
        self.entries.append((new_ip_address, new_port, delete))

        # Увеличение счетчика строк
        self.current_row += 1

    def delete_entry(self, ip_address, port, delete_button):
        # Удаление полей и кнопки из сетки
        ip_address.grid_remove()
        port.grid_remove()
        delete_button.grid_remove()

        # Удаление полей и кнопки из списка
        self.entries.remove((ip_address, port, delete_button))

        # Обновление окна
        self.update()
