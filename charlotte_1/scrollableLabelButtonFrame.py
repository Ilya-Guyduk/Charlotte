import customtkinter as ctk
import widgets
import serverWindow

class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.label_list = []
        self.button_list = []

    def add_item(self, item, conn, image=None):
        label = ctk.CTkButton(self,
                              text=f"> {item}",
                              image=image,
                              command=self.open_server_window,
                              anchor="w",
                              fg_color="transparent", #цвет фона
                            #border_width=1, #ширина рамки
                            text_color=("gray10", "#DCE4EE"), 
                            corner_radius=0, # радиус закругления
                            hover_color=("#6C6C6C"), #цвет при наведении 
                            border_color=("#5A5757"), #цвет рамки
                            border_spacing=0, #отступ от рамки
                            font=ctk.CTkFont(family="Courier new")
                                       )
        label.grid(row=len(self.label_list),
                   column=0,
                   pady=(0, 0),
                   padx=2, 
                   sticky="nsew")
        self.label_list.append(label)

        #button = ctk.CTkButton(self,
        #                      text=item,
        #                      #image=image,
        #                      command=self.open_server_window,
        #                      anchor="w",
        #                      fg_color="transparent", #цвет фона
        #                    border_width=1, #ширина рамки
        #                    text_color=("gray10", "#DCE4EE"), 
        #                    corner_radius=0, # радиус закругления
        #                    hover_color=("#FF8C00"), #цвет при наведении 
        #                    border_color=("#5A5757"), #цвет рамки
        #                    border_spacing=0, #отступ от рамки
        #                    font=ctk.CTkFont(family="Courier new")
        #                               )
        #button.grid(row=len(self.button_list),
        #            column=1,
        #            pady=(0, 0),
        #            sticky="nsew"
        #            )
        #self.button_list.append(button)
        #button.set(conn)
        

        self.toplevel_window = None
        #if self.command is not None:
        #    button.configure(command=lambda: self.command(item))

    def open_server_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = serverWindow.ServerWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
        self.toplevel_window.after(100, self.toplevel_window.lift)