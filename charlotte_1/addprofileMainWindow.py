from tabs import CTkTabview as tab
from addprofileServerTab import AddServerTabFrame
import customtkinter as ctk
from PIL import Image
import os 
import globaldata


class AddProfileMainWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Добавить профиль")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_reg = ctk.CTkImage(Image.open(os.path.join(current_dir, 
                                                                                                         "img",
                                                                                                         "logo2.png")),
                                 size=(70, 70))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo_reg,
                                  text=" Charlotte",
                                  font=ctk.CTkFont(family="Mont ExtraLight DEMO",size=25),
                                  compound="left")
        self.logo.grid(row=0,
                        column=0,
                        padx=(10, 0),
                        pady=(10, 0),
                        sticky="nsw")

        self.tabview = tab(self)
        self.tabview.grid(row=1,
                          padx=5,
                          pady=(0, 5),
                          column=0,
                          sticky="nsew")
        self.tabview.add("Сервер")
        self.tabview.add("Кластер")

        #=========================================================================================

        self.add_server_frame = AddServerTabFrame(master=self.tabview.tab("Сервер"), cancel=self.cancel)
        self.add_server_frame.grid(sticky="nsew")

        #======================================================================

    
    def cancel(self):
        """Функция выхода из окна"""
        self.destroy()