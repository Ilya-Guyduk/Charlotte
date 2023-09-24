import customtkinter as ctk
import widgets
import serverWindow
import button

class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,
                         scrollbar_button_color=("#545353"))
        self.grid_columnconfigure(0, weight=1)
        self.label_list = []

    def add_item(self, item, srv_id, image=None):
        self.label = ctk.CTkButton(self,
                              text=f"> {item}",
                              image=image,
                              command=self.open_server_window,
                              anchor="w",
                              fg_color="transparent", #цвет фона
                            #border_width=1, #ширина рамки
                            text_color=("gray10", "#DCE4EE"), 
                            corner_radius=4, # радиус закругления
                            hover_color=("#545353"), #цвет при наведении 
                            border_color=("#5A5757"), #цвет рамки
                            border_spacing=0, #отступ от рамки
                            font=ctk.CTkFont(family="Courier new")
                                       )
        self.label.grid(row=len(self.label_list),
                   pady=(0, 0),
                   padx=2, 
                   sticky="nsew")
        self.label.bind('<Button-3>', self.open_server_window)#захват
        self.label_list.append(self.label)
        self.toplevel_window = None
        self.name_window = srv_id

    def open_server_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = serverWindow.ServerWindow(self) 
        else:
            self.toplevel_window.focus()
        self.toplevel_window.after(100, self.toplevel_window.lift)