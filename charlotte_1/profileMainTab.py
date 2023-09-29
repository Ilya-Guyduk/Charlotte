import customtkinter as ctk
import button
import addprofile
from CTkToolTip import *
import sqlite3
import globaldata

class MainTabFrame(ctk.CTkFrame):
    def __init__(self, master, svc_id=None, **kwargs):
        super().__init__(master,
                       corner_radius=4,
                       border_width=0, #ширина рамки
                       fg_color="transparent", #цвет фона
                       **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.svc_id = svc_id
        with sqlite3.connect('Charlotte') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT hostname, os, architecture, kernel, machine_id, boot_id FROM SERVERS \
                            JOIN SVC_CONNECTS USING (svc_id) \
                            JOIN SVC_USERS USING (svc_id) \
                            JOIN SVC_MAIN USING (svc_id) \
                            WHERE account_id = ? AND svc_id = ?", (globaldata.global_id, self.svc_id))
            serverdata = cursor.fetchone()
            svc_hostname = serverdata[0]
            svc_os = serverdata[1]
            svc_arch = serverdata[2]
            svc_kernel = serverdata[3]
            svc_machine_id = serverdata[4]
            svc_boot_id = serverdata[5]


        self.status_label = ctk.CTkLabel(self,
                                                    text="Статус: АКТИВЕН",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="e"
                                                    )
        self.status_label.grid(row=0,
                             column=0)

        self.fs_label = ctk.CTkLabel(self,
                                                    text=f"Имя хоста: {svc_hostname}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.fs_label.grid(row=1,
                             column=0)


        self.os_label = ctk.CTkLabel(self,
                                                    text=f"Операционная система: {svc_os}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.os_label.grid(row=2,
                             column=0)

        self.arch_label = ctk.CTkLabel(self,
                                                    text=f"Архитектура: {svc_arch}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.arch_label.grid(row=3,
                             column=0)

        self.arch_label = ctk.CTkLabel(self,
                                                    text=f"Ядро: {svc_kernel}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.arch_label.grid(row=4,
                             column=0)

        self.machine_id_label = ctk.CTkLabel(self,
                                                    text=f"Machine ID: {svc_machine_id}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.machine_id_label.grid(row=5,
                             column=0)

        self.boot_id_label = ctk.CTkLabel(self,
                                                    text=f"Boot ID: {svc_boot_id}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.boot_id_label.grid(row=6,
                             column=0)
