import customtkinter as ctk
import button
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
            cursor.execute("SELECT hostname, os, architecture, kernel, chassis, machine_id, boot_id, model_name, cpus, cores_per_socket, sockets, cpu_mhz FROM SERVERS \
                            JOIN SVC_CPU USING (svc_id) \
                            JOIN SVC_MAIN USING (svc_id) \
                            WHERE account_id = ? AND svc_id = ?", (globaldata.global_id, self.svc_id))
            serverdata = cursor.fetchone()
            svc_hostname = serverdata[0]
            svc_os = serverdata[1]
            svc_arch = serverdata[2]
            svc_kernel = serverdata[3]
            svc_chassis = serverdata[4]
            svc_machine_id = serverdata[5]
            svc_boot_id = serverdata[6]
            svc_cpu_model_name = serverdata[7]
            svc_cpus = serverdata[8]
            svc_cores_per_socket = serverdata[9]
            svc_cpu_sockets = serverdata[10]
            svc_cpu_mhz = serverdata[11]

        self.main_frame = ctk.CTkFrame(self, 
                                      corner_radius=4,
                                      border_width=1 #ширина рамки
                                      )
        self.main_frame.grid(row=0,
                             column=0,
                             padx=(5, 5),
                             pady=(5, 5)
                             )

        self.status_label = ctk.CTkLabel(self.main_frame,
                                                    text="Статус: АКТИВЕН",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="e",
                                                    justify="left"
                                                    )
        self.status_label.grid(row=0,
                             column=0)

        self.fs_label = ctk.CTkLabel(self.main_frame,
                                                    text=f"Имя хоста: {svc_hostname}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.fs_label.grid(row=1,
                             column=0)

        self.chassis_label = ctk.CTkLabel(self.main_frame,
                                                    text=f"Тип хоста: {svc_chassis}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.chassis_label.grid(row=2,
                             column=0)

        self.os_label = ctk.CTkLabel(self.main_frame,
                                                    text=f"Операционная система: {svc_os}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.os_label.grid(row=3,
                             column=0)

        self.arch_label = ctk.CTkLabel(self.main_frame,
                                                    text=f"Архитектура: {svc_arch}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.arch_label.grid(row=4,
                             column=0)

        self.arch_label = ctk.CTkLabel(self.main_frame,
                                                    text=f"Ядро: {svc_kernel}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.arch_label.grid(row=5,
                             column=0)

        self.machine_id_label = ctk.CTkLabel(self.main_frame,
                                                    text=f"Machine ID: {svc_machine_id}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.machine_id_label.grid(row=6,
                             column=0)

        self.boot_id_label = ctk.CTkLabel(self.main_frame,
                                                    text=f"Boot ID: {svc_boot_id}",
                                                    text_color=("#5A5757"),
                                                    anchor="e"
                                                    )
        self.boot_id_label.grid(row=7,
                             column=0)



        self.cpu_frame = ctk.CTkFrame(self, 
                                      corner_radius=4,
                                      border_width=1 #ширина рамки
                                      )
        self.cpu_frame.grid(row=0,
                             column=1,
                             padx=(5, 5),
                             pady=(5, 5)
                             )

        self.cpu_model_name_label = ctk.CTkLabel(self.cpu_frame,
                                                    text=f"Процессор: {svc_cpu_model_name}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.cpu_model_name_label.grid(row=0,
                             column=0)

        self.cpus_label = ctk.CTkLabel(self.cpu_frame,
                                                    text=f"Количество ядер(всего): {svc_cpus}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.cpus_label.grid(row=1,
                             column=0)

        self.cores_label = ctk.CTkLabel(self.cpu_frame,
                                                    text=f"Количество ядер(на сокет): {svc_cores_per_socket}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.cores_label.grid(row=2,
                             column=0)

        self.socket_label = ctk.CTkLabel(self.cpu_frame,
                                                    text=f"Сокеты: {svc_cpu_sockets}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.socket_label.grid(row=3,
                             column=0)

        self.mhz_label = ctk.CTkLabel(self.cpu_frame,
                                                    text=f"Тактовая частота: {svc_cpu_mhz}",
                                                    text_color=("#5A5757"),
                                                    font=ctk.CTkFont(family="Courier new"),
                                                    anchor="w"
                                                    )
        self.mhz_label.grid(row=4,
                             column=0)