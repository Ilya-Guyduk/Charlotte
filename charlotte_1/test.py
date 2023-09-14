import tkinter
import customtkinter as ctk
import scrollableLabelButtonFrame as sc
import addprofile
import os
from PIL import Image
import button 
import mainMenu
import menuBar
import login
import widgets





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
        self.sidebar_frame = ctk.CTkFrame(self)
        self.sidebar_frame.grid(row=1,
                                column=0,
                                rowspan=5,
                                sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4,
                                             weight=1)
        #=====================================================
        #лого на главном экране
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_label = ctk.CTkImage(Image.open(os.path.join(current_dir, "img", "logo2.png")),
                                 size=(30, 30))
        self.logo_label = ctk.CTkLabel(self.sidebar_frame,
                                       text=" Charlotte",
                                       font=ctk.CTkFont(family="Mont ExtraLight DEMO",size=20),
                                       image=self.logo_label,
                                       compound="left")
        self.logo_label.grid(row=0,
                             column=0,
                             padx=5,
                             pady=3,
                             columnspan=2,
                             sticky="w")
        #======================================================================================
        #сайдбар с кнопками 
        self.button_frame = ctk.CTkFrame(self.sidebar_frame,
                                         corner_radius=0)
        self.button_frame.grid(row=1,
                               column=0,
                               columnspan=2,
                               sticky="nsew")
        self.button_1 = button.LittleAcessButton(self.button_frame,
                                                 text="+",
                                                 command=self.open_input_dialog_event)
        self.button_1.grid(row=1,
                           column=0)

        self.button_2 = button.LittleAcessButton(self.button_frame,
                                                 text="+c",
                                                 command=self.open_input_dialog_event)
        self.button_2.grid(row=1,
                           column=1)

        self.button_3 = button.LittleAcessButton(self.button_frame,
                                                 text="g",
                                                 command=self.open_input_dialog_event)
        self.button_3.grid(row=1,
                           column=2)

        self.button_3 = button.LittleOwnButton(self.button_frame,
                                               text="?")
        self.button_3.grid(row=1,
                           column=3)
        #=====================================================================================
        #Меню с подключениями
        self.scrollable_label_button_frame = sc.ScrollableLabelButtonFrame(self.sidebar_frame, 
                                                                           command=self.label_button_frame_event,
                                                                           corner_radius=0
                                                                           )
        self.scrollable_label_button_frame.grid(row=4,
                                                column=0,
                                                pady=3,
                                                columnspan=2,
                                                sticky="nsew")
        for i in range(40):  # цикл для добалвения профилей серверов
            self.scrollable_label_button_frame.add_item(f"Сервер {i}",
                                                        image=ctk.CTkImage(Image.open(os.path.join(current_dir,
                                                                                                             "img",
                                                                                                             "conn.png"))))
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
                        padx=(10, 0),
                        pady=(5, 10),
                        sticky="nsew")

        self.main_button_1 = button.AcessButton(self,
                                             text="Поиск",
                                             command=self.open_input_dialog_event)
        self.main_button_1.grid(row=4, 
                                column=3,
                                padx=(10, 10),
                                pady=(5, 10),
                                sticky="nsew")
        #=========================================================================================
        # create textbox
        self.textbox = ctk.CTkTextbox(self,
                                                width=250,
                                                corner_radius=3)
        self.textbox.insert("0.0",
                            "Оповещения:\n\n" + "Подозрительные изменения в акнутом алерте Сервер: uz-ceir-geo-app2 Алерт: face-id-proxy-service_proc PROCS CRITICAL: 0 processes with args '/opt/svyazcom/bin/face-id-proxy-service' check_stat_ussd_out WARNING! Count of USSD_OUT_FULL_ALL is low or high (8 instead 30) in last 1 hours!\n\n" * 20)
        self.textbox.grid(row=1,
                          column=2,
                          padx=(10, 0),
                          pady=(10, 0),
                          sticky="nsew")
        #=========================================================================================
        # create tabview
        self.tabview = ctk.CTkTabview(self,
                                                width=250,
                                                corner_radius=3)
        self.tabview.grid(row=1,
                          column=1,
                          rowspan=2,
                          padx=(10, 0),
                          pady=(0, 0),
                          sticky="nsew")
        self.tabview.add("Общие показатели")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("Общие показатели").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("Общие показатели"),
                                                        dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"],
                                                        corner_radius=3)
        self.optionmenu_1.grid(row=0,
                               column=0,
                               padx=10,
                               pady=(10, 10))
        self.combobox_1 = ctk.CTkComboBox(self.tabview.tab("Общие показатели"),
                                                    values=["Value 1", "Value 2", "Value Long....."],
                                                    corner_radius=3)
        self.combobox_1.grid(row=1,
                            column=0,
                            padx=10,
                            pady=(5, 5))
        self.string_input_button = ctk.CTkButton(self.tabview.tab("Общие показатели"),
                                                           text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event,
                                                           corner_radius=3)
        self.string_input_button.grid(row=2,
                                      column=0,
                                      padx=10,
                                      pady=(5, 5))
        self.label_tab_2 = ctk.CTkLabel(self.tabview.tab("Tab 2"),
                                                  text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0,
                              column=0,
                              padx=10,
                              pady=10)

        # create radiobutton frame
        self.radiobutton_frame = ctk.CTkFrame(self)
        self.radiobutton_frame.grid(row=1,
                                    column=3,
                                    padx=(10, 10),
                                    pady=(10, 0),
                                    sticky="nsew")

        self.radio_var = tkinter.IntVar(value=0)
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

        # create slider and progressbar frame
        #self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        #self.slider_progressbar_frame.grid(row=2, column=1, rowspan=2, padx=(10, 0), pady=(10, 0), sticky="nsew")
        #self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        #self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        #self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame, corner_radius=3)
        #self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, corner_radius=3)
        #self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, corner_radius=3)
        #self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        #self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical", corner_radius=3)
        #self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        #self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical", corner_radius=3)
        #self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self,
                                                                 label_text="Метрики",
                                                                 corner_radius=3)
        self.scrollable_frame.grid(row=2,
                                   column=2,
                                   rowspan=2,
                                   padx=(10, 0),
                                   pady=(10, 0),
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

        # create checkbox and switch frame
        self.checkbox_slider_frame = ctk.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=2,
                                        column=3,
                                        rowspan=2,
                                        padx=(10, 10),
                                        pady=(10, 0),
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

        # set default values
        #self.sidebar_button_3.configure(state="disabled")
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        self.radio_button_3.configure(state="disabled")
        self.optionmenu_1.set("CTkOptionmenu")
        self.combobox_1.set("CTkComboBox")
        #self.slider_1.configure(command=self.progressbar_2.set)
        #self.slider_2.configure(command=self.progressbar_3.set)
        #self.progressbar_1.configure(mode="indeterminnate")
        #self.progressbar_1.start()
        #self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        #self.seg_button_1.set("Value 2")
        self.toplevel_window = None

    def open_input_dialog_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = addprofile.ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
        self.toplevel_window.after(100, self.toplevel_window.lift)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")

    def search(self):
        print("search_button click")




if __name__ == "__main__":
   
    log = login.loginWindow()
    #root.log()    
    log.mainloop()