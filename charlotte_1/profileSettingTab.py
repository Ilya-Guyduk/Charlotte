import customtkinter as ctk
import button
from CTkToolTip import *
import sqlite3
import globaldata

class SettingTabFrame(ctk.CTkFrame):
    def __init__(self, master, svc_id=None, **kwargs):
        super().__init__(master,
                       corner_radius=4,
                       border_width=0, #ширина рамки
                       fg_color="transparent", #цвет фона
                       **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.svc_id = svc_id