import customtkinter as ctk

class SimpleMenu(ctk.CTkOptionMenu):
    def __init__(self, menu_frame, values, command, **kwargs):
        super().__init__(
            menu_frame,
            dynamic_resizing=False,
            values=values,
            command=command,
            corner_radius=4,
            fg_color=("#5A5757"),
            font=ctk.CTkFont(family="Courier new"),
            dropdown_font=ctk.CTkFont(family="Courier new"),
            button_color=("#5A5757"),
            button_hover_color=("#FF8C00")
            )

