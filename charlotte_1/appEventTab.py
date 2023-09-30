import customtkinter as ctk
import button
from CTkToolTip import *
import sqlite3
import globaldata

class EventTabFrame(ctk.CTkFrame):
    def __init__(self, master, svc_id=None, **kwargs):
        super().__init__(master,
                       corner_radius=4,
                       border_width=0, #ширина рамки
                       fg_color="transparent", #цвет фона
                       **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.svc_id = svc_id

        # create textbox
        self.metrix_frame = ctk.CTkFrame(self, border_width=1)
        self.metrix_frame.grid(row=0,
                               column=0,
                               rowspan=3,
                               padx=(5, 0),
                               pady=(0, 5),
                               sticky="nsew")

        self.textbox = ctk.CTkTextbox(self,
                                                width=250,
                                                corner_radius=3)
        self.textbox.insert("0.0",
                            "Оповещения:\n\n" + "Подозрительные изменения в акнутом алерте Сервер: uz-ceir-geo-app2 Алерт: face-id-proxy-service_proc PROCS CRITICAL: 0 processes with args '/opt/svyazcom/bin/face-id-proxy-service' check_stat_ussd_out WARNING! Count of USSD_OUT_FULL_ALL is low or high (8 instead 30) in last 1 hours!\n\n" * 20)
        self.textbox.grid(row=0,
                          column=1,
                          padx=(5, 0),
                          pady=(0, 0),
                          sticky="nsew")

        # create radiobutton frame
        self.radiobutton_frame = ctk.CTkFrame(self)
        self.radiobutton_frame.grid(row=0,
                                    column=2,
                                    padx=(5, 5),
                                    pady=(0, 0),
                                    sticky="nsew")

        self.radio_var = ctk.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame,
                                                        text="Процессор. Нагрузка")
        self.label_radio_group.grid(row=0,
                                    column=2, 
                                    columnspan=1,
                                    padx=10,
                                    pady=10,
                                    sticky="")
        self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame,
                                                           variable=self.radio_var,
                                                           value=0,
                                                           corner_radius=3)
        self.radio_button_1.grid(row=1,
                                 column=2,
                                 pady=10,
                                 padx=20,
                                 sticky="n")

        # create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self,
                                                                 label_text="Метрики",
                                                                 corner_radius=3)
        self.scrollable_frame.grid(row=1,
                                   column=1,
                                   rowspan=2,
                                   padx=(5, 0),
                                   pady=(5, 5),
                                   sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0,
                                                   weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = ctk.CTkSwitch(self.scrollable_frame,
                                             text=f"CTkSwitch {i}",
                                             corner_radius=3)
            switch.grid(row=i,
                        column=0,
                        padx=10,
                        pady=(0, 10))
            self.scrollable_frame_switches.append(switch)
        #===================================================================================


        # create checkbox and switch frame
        self.checkbox_slider_frame = ctk.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1,
                                        column=2,
                                        rowspan=2,
                                        padx=(5, 5),
                                        pady=(5, 5),
                                        sticky="nsew")
        self.checkbox_1 = ctk.CTkCheckBox(self.checkbox_slider_frame,
                                                    corner_radius=3)
        self.checkbox_1.grid(row=1,
                             column=0,
                             pady=(20, 0),
                             padx=20,
                             sticky="n")
        self.checkbox_2 = ctk.CTkCheckBox(self.checkbox_slider_frame,
                                                    corner_radius=3)
        self.checkbox_2.grid(row=2,
                             column=0,
                             pady=(20, 0),
                             padx=20,
                             sticky="n")
        self.checkbox_3 = ctk.CTkCheckBox(self.checkbox_slider_frame,
                                                    corner_radius=3)
        self.checkbox_3.grid(row=3,
                             column=0,
                             pady=20,
                             padx=20,
                             sticky="n")
        #====================================================================

        # set default values
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()