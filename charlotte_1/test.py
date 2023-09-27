import customtkinter as ctk
import scrollableLabelButtonFrame as sc
import os
from PIL import Image
import button 
import mainMenu
import globaldata
import widgets
import sqlite3
from tabs import CTkTabview as tab
from buttonFrame import ButtonFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #настройки основного окна
        self.title("Charlotte v0.01")
        self.geometry(f"{1100}x{580}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1,
                                  weight=1)
        self.grid_columnconfigure((2, 3),
                                  weight=0)
        self.grid_rowconfigure((1, 2),
                               weight=1)

        #верхнее меню
        self.optionmenu = mainMenu.OptionMenuHolder(self)
        self.optionmenu.grid(row=0,
                            column=0,
                            columnspan=4,
                            sticky="nsew")
        self.optionmenu.grid_columnconfigure(0,
                                             weight=0)
        #====================================================
        #фрейм сайдбара с виджетами
        self.sidebar_frame = ctk.CTkFrame(self,
                                          corner_radius=0
                                          )
        self.sidebar_frame.grid(row=1,
                                column=0,
                                rowspan=5,
                                sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4,
                                             weight=1)
        #=====================================================
        #лого на главном экране
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_main = ctk.CTkImage(Image.open(os.path.join(current_dir, "img", "logo2.png")),
                                 size=(30, 30))
        self.logo_label = ctk.CTkLabel(self.sidebar_frame,
                                       text=" Charlotte",
                                       font=ctk.CTkFont(family="Mont ExtraLight DEMO",size=20),
                                       image=logo_main,
                                       compound="left")
        self.logo_label.grid(row=0,
                             column=0,
                             padx=5,
                             pady=3,
                             columnspan=2,
                             sticky="w")
        #======================================================================================
        #сайдбар с кнопками 
        self.button_frame = ButtonFrame(master=self.sidebar_frame)
        self.button_frame.grid(row=1,
                               column=0,
                               columnspan=2,
                               pady=(0, 2),
                               padx=1,
                               sticky="nsew")
        #=====================================================================================
        self.scrollable_label_button_frame = sc.ScrollableLabelButtonFrame(self.sidebar_frame, 
                                                                   corner_radius=0, 
                                                                   scrollbar_button_hover_color=("#5A5757"),
                                                                   border_width=1)
        self.scrollable_label_button_frame.grid(row=4, column=0, pady=0, padx=(0, 0), columnspan=2, sticky="nsew")
        
        with sqlite3.connect('Charlotte') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT desc_svc, svc_id FROM SERVERS WHERE account_id = ?", (globaldata.global_id,))
            server_data = cursor.fetchall()
            
        for desc_name, srv_id in server_data:
            self.scrollable_label_button_frame.add_item(desc_name,
                                                        srv_id=srv_id,
                                                        image=ctk.CTkImage(Image.open(os.path.join(current_dir, "img", "conn.png")))
                                                        )

        # Создаем отдельный поток для обновления записей
        #self.update_thread = threading.Thread(target=self.update_records)
        #self.update_thread.start()
        #======================================================================================================================
        #доп опции
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame,
                                                            text="Оформление:"
                                                            )
        self.appearance_mode_label.grid(row=5,
                                        column=0
                                        )
        self.appearance_mode_optionemenu = widgets.SimpleMenu(self.sidebar_frame,
                                            values=(["Dark", "Light", "System"]),
                                            command=self.change_appearance_mode_event,)
        self.appearance_mode_optionemenu.grid(row=6,
                                              column=0,
                                              padx=(10, 2),
                                              pady=(0, 10))
        self.appearance_mode_optionemenu.set("Dark")

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame,
                                                    text="Масштаб:"
                                                    )
        self.scaling_label.grid(row=5,
                                column=1
                                )
        self.scaling_optionemenu = widgets.SimpleMenu(self.sidebar_frame,
                                                      values=["80%", "90%", "100%", "110%", "120%"],
                                                      command=self.change_scaling_event
                                                      )
        self.scaling_optionemenu.grid(row=6,
                                      column=1,
                                      padx=(2, 10),
                                      pady=(0, 10))
        self.scaling_optionemenu.set("100%")
        #==========================================================================================
        # поисковая строка и кнопка
        self.entry = ctk.CTkEntry(self,
                                  placeholder_text="Поиск",
                                  corner_radius=4,
                                  font=ctk.CTkFont(family="Courier new"))
        self.entry.grid(row=4,
                        column=1,
                        columnspan=2,
                        padx=(5, 0),
                        pady=(5, 10),
                        sticky="nsew")

        self.main_button_1 = button.AcessButton(self,
                                             text="Поиск",
                                             command=self.search)
        self.main_button_1.grid(row=4, 
                                column=3,
                                padx=(5, 5),
                                pady=(5, 10),
                                sticky="nsew")
        #=========================================================================================
        # create tabview
        self.tabview = tab(self)
        self.tabview.grid(row=1,
                          column=1,
                          rowspan=2,
                          columnspan=3,
                          padx=(5, 5),
                          pady=(0, 0),
                          sticky="nsew")
        self.tabview.add("Общие показатели")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("Общие показатели").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Общие показатели").grid_rowconfigure((0, 1),weight=1)
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        #=========================================================================================
        # create textbox
        self.metrix_frame = ctk.CTkFrame(self.tabview.tab("Общие показатели"))
        self.metrix_frame.grid(row=0,
                               column=0,
                               rowspan=3,
                               padx=(5, 0),
                               pady=(0, 5),
                               sticky="nsew")

        self.textbox = ctk.CTkTextbox(self.tabview.tab("Общие показатели"),
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
        self.radiobutton_frame = ctk.CTkFrame(self.tabview.tab("Общие показатели"))
        self.radiobutton_frame.grid(row=0,
                                    column=2,
                                    padx=(5, 5),
                                    pady=(0, 0),
                                    sticky="nsew")

        self.radio_var = ctk.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame,
                                                        text="CTkRadioButton Group:")
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
        self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame,
                                                           variable=self.radio_var,
                                                           value=1,
                                                           corner_radius=3)
        self.radio_button_2.grid(row=2,
                                 column=2,
                                 pady=10,
                                 padx=20,
                                 sticky="n")
        self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame,
                                                           variable=self.radio_var,
                                                           value=2,
                                                           corner_radius=3)
        self.radio_button_3.grid(row=3,
                                 column=2,
                                 pady=10,
                                 padx=20,
                                 sticky="n")

        # create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.tabview.tab("Общие показатели"),
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
        self.checkbox_slider_frame = ctk.CTkFrame(self.tabview.tab("Общие показатели"))
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
        self.radio_button_3.configure(state="disabled")
        self.toplevel_window = None
        #======================================================================
        #======================================================================


    #def update_records(self):
    #    conn = sqlite3.connect('Charlotte')
    #    cursor = conn.cursor()
    #    while True:
            # Выполняем запрос SELECT
    #        cursor.execute("SELECT desc_svc FROM SERVERS")
    #        results = cursor.fetchall()
            # Обновляем интерфейс в главном потоке
    #        self.after(1000, self.update_interface, results)
            # Задержка перед следующей проверкой
            #time.sleep(1)  # Настройте нужное вам время задержки
    #    cursor.close()
    #    conn.close()

    #def update_interface(results):
    #    conn = sqlite3.connect('Charlotte')
    #    cursor = conn.cursor()
    #    cursor.execute("SELECT desc_svc FROM SERVERS")
    #    results = cursor.fetchall()
    #    for i, result in enumerate(results):  # цикл для добалвения профилей серверов
    #        self.scrollable_label_button_frame.add_item(result[0],
    #                                                    image=ctk.CTkImage(Image.open(os.path.join(current_dir,
    #                                                                                                         "img",
    #                                                                                                         "conn.png")))
    #                                                                  )


    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


    def search(self):
        print("search_button click")




if __name__ == '__main__':
    app = App()
    app.mainloop()