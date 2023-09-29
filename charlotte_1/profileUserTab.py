import customtkinter as ctk
import button
from CTkToolTip import *

class UserTabFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                       corner_radius=4,
                       border_width=0, #ширина рамки
                       fg_color="transparent", #цвет фона
                       **kwargs)

        self.button_add_srv = button.LittleAcessButton(self,
                                                     text="+",
                                                     command=self.open_input_dialog_event)
        self.button_add_srv.grid(row=0,
                               column=0)
        self.tooltip_add_srv = CTkToolTip(self.button_add_srv, alpha=0, corner_radius=4, message="Добавить сервер")

        self.button_add_claster = button.LittleAcessButton(self,
                                                     text="+c",
                                                     command=self.open_input_dialog_event)
        self.button_add_claster.grid(row=0,
                               column=1)
        self.tooltip_add_claster = CTkToolTip(self.button_add_claster, message="Добавить кластер")

        self.button_3 = button.LittleAcessButton(self,
                                                     text="g",
                                                     command=self.open_input_dialog_event)
        self.button_3.grid(row=0,
                               column=2)

        self.button_3 = button.LittleOwnButton(self,
                                                   text="?",
                                                   command=self.open_input_dialog_event)
        self.button_3.grid(row=0,
                               column=3)
        self.button_4 = button.LittleAcessButton(self,
                                                   text="@",
                                                   command=self.open_input_dialog_event)
        self.button_4.grid(row=0,
                               column=4)
        self.toplevel_window = None

    def open_input_dialog_event(self):
        pass




