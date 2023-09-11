import customtkinter
import widgets

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        #self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self,
                                       text=item,
                                       image=image,
                                       compound="left",
                                       padx=5, 
                                       anchor="w")
        button = widgets.SimpleMenu(self, 
                                    values=["Light", "Dark", "System"],
                                    command=self.open_input_dialog_event)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list),
                   column=0, 
                   pady=(0, 10),
                   sticky="w")
        button.grid(row=len(self.button_list),
                    column=1,
                    pady=(0, 10),
                    padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    #def remove_item(self, item):
    #    for label, button in zip(self.label_list, self.button_list):
    #        if item == label.cget("text"):
    #            label.destroy()
    #            button.destroy()
    #            self.label_list.remove(label)
    #            self.button_list.remove(button)
    #            return
    def open_input_dialog_event():
        pass