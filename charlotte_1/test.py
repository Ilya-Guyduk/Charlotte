import tkinter
import tkinter.messagebox
import customtkinter
import scrollableLabelButtonFrame as sc
#import login
import os
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #настройки основного окна
        self.title("Charlotte v0.01")
        self.geometry(f"{1100}x{580}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        #фрейм сайдбара с виджетами
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)





        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.grid(row=0, column=0, columnspan=4, pady=10, padx=0)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
        self.optionmenu_1.grid(row=0, column=0, pady=10, padx=10)
        self.optionmenu_1.set("CTk Option Menu")

        self.combobox_1 = customtkinter.CTkComboBox(self.frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
        self.combobox_1.grid(row=0, column=1, pady=10, padx=0)
        self.combobox_1.set("CTk Combo Box")

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_1, values=["Light", "Dark", "System"])
        self.appearance_mode_optionemenu.grid(row=0, column=2, padx=0, pady=10)

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.frame_1, values=["80%", "90%", "100%", "110%", "120%"])
        self.scaling_optionemenu.grid(row=0, column=3, padx=0, pady=10)

        





        #лого на главном экране
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Charlotte", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=3, columnspan=2, sticky="w")
        

        #self.button_frame = customtkinter.CTkFrame(self.sidebar_frame)
        #self.button_frame.grid(row=1, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")
        self.sidebar_buttons = customtkinter.CTkSegmentedButton(self.sidebar_frame, values=["+", "-", "Group", "Node", "Value"],command=self.open_input_dialog_event)
        self.sidebar_buttons.grid(row=1, column=0, padx=5, pady=3, columnspan=2, sticky="nsew")
        #self.sidebar_button_1 = customtkinter.CTkButton(self.button_frame, width=30, text="+", command=self.open_input_dialog_event)
        #self.sidebar_button_1.grid(row=1, column=0, padx=3, pady=3)
        #self.sidebar_button_2 = customtkinter.CTkButton(self.button_frame, width=30, text="+c", command=self.open_input_dialog_event)
        #self.sidebar_button_2.grid(row=1, column=1, padx=3, pady=3)
        #self.sidebar_button_3 = customtkinter.CTkButton(self.button_frame, width=30, text="G", command=self.sidebar_button_event)
        #self.sidebar_button_3.grid(row=1, column=2, padx=3, pady=3)
        
        #Меню с подключениями
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = sc.ScrollableLabelButtonFrame(master=self.sidebar_frame, width=300, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=4, column=0, padx=5, pady=3, columnspan=2, sticky="nsew")
        for i in range(40):  # add items with images
            self.scrollable_label_button_frame.add_item(f"Сервер {i}", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "img", "logo2.png"))))


        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Оформление:", anchor="w", width=50)
        self.appearance_mode_label.grid(row=5, column=0, padx=5, pady=3)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=5, pady=3)

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Масштаб:", anchor="w", width=50)
        self.scaling_label.grid(row=5, column=1, padx=5, pady=3)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=6, column=1, padx=5, pady=3)



        # поисковая строка и кнопка
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Поиск")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(10, 0), pady=(10, 10), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Поиск", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")



        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=10, pady=(10, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=10, pady=(5, 5))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=10, pady=(5, 5))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=10, pady=10)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, rowspan=2, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Метрики")
        self.scrollable_frame.grid(row=1, column=2, rowspan=2, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 10))
            self.scrollable_frame_switches.append(switch)

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, rowspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        #self.sidebar_button_3.configure(state="disabled")
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("CTkOptionmenu")
        self.combobox_1.set("CTkComboBox")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "Оповещения:\n\n" + "Подозрительные изменения в акнутом алерте Сервер: uz-ceir-geo-app2 Алерт: face-id-proxy-service_proc PROCS CRITICAL: 0 processes with args '/opt/svyazcom/bin/face-id-proxy-service' check_stat_ussd_out WARNING! Count of USSD_OUT_FULL_ALL is low or high (8 instead 30) in last 1 hours!\n\n" * 20)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Введите данные:", title="Добавить сервер")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")



if __name__ == "__main__":
    app = App()
    #login.loginwindow()
    app.mainloop()