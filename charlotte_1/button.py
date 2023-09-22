import customtkinter as ctk

class AcessButton(ctk.CTkButton):
    def __init__(self, button_frame, text, command, *args, **kwargs):
        super().__init__(
            button_frame,
            text=text, #текст кнопки
            command=command, #команда при нажатии
            fg_color="transparent", #цвет фона
            border_width=1, #ширина рамки
            text_color=("gray10", "#DCE4EE"), 
            corner_radius=4, # радиус закругления
            hover_color=("#FF8C00"), #цвет при наведении 
            border_color=("#5A5757"), #цвет рамки
            border_spacing=0, #отступ от рамки
            font=ctk.CTkFont(family="Courier new") 
        )
class LittleAcessButton(ctk.CTkButton):
    def __init__(self, button_frame, text, command):
        super().__init__(
            button_frame,
            text=text,
            command=command,
            width=30,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=4,
            hover_color=("#FF8C00"),
            border_color=("#5A5757"),
            font=ctk.CTkFont(family="Courier new")
        )


class CancelButton(ctk.CTkButton):
    def __init__(self, button_frame, text, command):
        super().__init__(
            button_frame,
            text=text,
            command=command,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=4,
            hover_color=("#6C6C6C"),
            border_color=("#5A5757"),
            font=ctk.CTkFont(family="Courier new")
        )


class OwnButton(ctk.CTkButton):
    def __init__(self, button_frame, command, text, *args, **kwargs):
        super().__init__(
            button_frame,
            text=text,
            #command=command,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=4,
            hover_color=("#2F4F4F"),
            border_color=("#5A5757"),
            font=ctk.CTkFont(family="Courier new")
        )
class LittleOwnButton(ctk.CTkButton):
    def __init__(self, button_frame, text):
        super().__init__(
            button_frame,
            text=text,
            #command=command,
            width=30,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=4,
            hover_color=("#2F4F4F"),
            border_color=("#5A5757"),
            font=ctk.CTkFont(family="Courier new")
        )