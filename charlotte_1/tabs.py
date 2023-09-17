import customtkinter as ctk

class CTkTabview(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                     border_width=1,
                     corner_radius=3,
                     segmented_button_fg_color=("#5A5757"),
                     border_color=("#5A5757"),
                     segmented_button_selected_color=("#FF8C00"),
                     segmented_button_selected_hover_color=("#FF8C00")
                     )
    


    