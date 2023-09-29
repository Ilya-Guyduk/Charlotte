from tabs import CTkTabview as tab
import customtkinter as ctk 
import sqlite3
from PIL import Image
import os 
import globaldata
import paramiko
from profileUserTab import UserTabFrame
from profileMainTab import MainTabFrame
from profileConnectTab import ConnectTabFrame
from profileSettingTab import SettingTabFrame


class ProfileMainWindow(ctk.CTkToplevel):
    """Класс основного окна конфигурации сервера"""
    def __init__(self, master, svc_id=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.svc_id = svc_id
        with sqlite3.connect('Charlotte') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT desc_svc, ip_addr, svc_login FROM SERVERS \
                            JOIN SVC_CONNECTS USING (svc_id) \
                            JOIN SVC_USERS USING (svc_id) \
                            JOIN SVC_MAIN USING (svc_id) \
                            WHERE account_id = ? AND svc_id = ?", (globaldata.global_id, self.svc_id))
            serverdata = cursor.fetchone()
            server_name = serverdata[0]
            ip_addr = serverdata[1]
            svc_login = serverdata[2]
            
        self.title(server_name)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_reg = ctk.CTkImage(Image.open(os.path.join(current_dir, 
                                                                                                         "img",
                                                                                                         "logo2.png")),
                                 size=(30, 30))
        self.logo = ctk.CTkLabel(self,
                                  image=self.logo_reg,
                                  text=f"->{server_name}->{svc_login}@{ip_addr}->✔",
                                  font=ctk.CTkFont(family="Courier new",size=17),
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
        self.tabview.add("Описание")
        self.tabview.tab("Описание").grid_columnconfigure(0, weight=1)
        self.tabview.add("Подключения")
        self.tabview.add("Юзеры")
        self.tabview.add("Настройки")

        self.main_frame = MainTabFrame(master=self.tabview.tab("Описание"), svc_id=self.svc_id)
        self.main_frame.grid(row=0,
                               column=0,
                               sticky="nsew")

        self.connect_frame = ConnectTabFrame(master=self.tabview.tab("Подключения"), svc_id=self.svc_id)
        self.connect_frame.grid(row=0,
                               column=0,
                               sticky="nsew")

        self.user_frame = UserTabFrame(master=self.tabview.tab("Юзеры"))
        self.user_frame.grid(row=0,
                               column=0,
                               sticky="nsew")

        self.setting_frame = SettingTabFrame(master=self.tabview.tab("Настройки"), svc_id=self.svc_id)
        self.setting_frame.grid(row=0,
                               column=0,
                               sticky="nsew")



