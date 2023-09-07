import customtkinter

class AcessButton(customtkinter.CTkButton):
    def __init__(self, button_frame, text, command):
        super().__init__(
            button_frame,
            text=text,
            command=command,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=3,
            hover_color=("#FF8C00")
        )

class LittleAcessButton(customtkinter.CTkButton):
    def __init__(self, button_frame, text, command):
        super().__init__(
            button_frame,
            text=text,
            command=command,
            width=30,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=3,
            hover_color=("#FF8C00")
        )


class CancelButton(customtkinter.CTkButton):
    def __init__(self, button_frame, text, command):
        super().__init__(
            button_frame,
            text=text,
            command=command,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=3,
            hover_color=("#6C6C6C")
        )


class OwnButton(customtkinter.CTkButton):
    def __init__(self, button_frame, text):
        super().__init__(
            button_frame,
            text=text,
            #command=command,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=3,
            hover_color=("#2F4F4F")
        )

class LittleOwnButton(customtkinter.CTkButton):
    def __init__(self, button_frame, text):
        super().__init__(
            button_frame,
            text=text,
            #command=command,
            width=30,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "#DCE4EE"),
            corner_radius=3,
            hover_color=("#2F4F4F")
        )