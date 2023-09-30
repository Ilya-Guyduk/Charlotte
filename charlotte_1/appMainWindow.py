import customtkinter as ctk
from appScrollableLabelButtonFrame import ScrollableLabelButtonFrame as sc
import os
from PIL import Image
import button 
from appMenuBar import OptionMenuHolder
import globaldata
import widgets
import sqlite3
from tabs import CTkTabview as tab
from buttonFrame import ButtonFrame
from appEventTab import EventTabFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #настройки основного окна
        self.title("Charlotte v0.01")
        self.geometry(f"{1100}x{580}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        #верхнее меню
        self.option_menu = OptionMenuHolder(self)
        self.option_menu.grid(row=0,
                            column=0,
                            columnspan=4,
                            sticky="nsew")
        self.option_menu.grid_columnconfigure(0, weight=0)
        #====================================================

        #фрейм сайдбара с виджетами
        self.sidebar_frame = ctk.CTkFrame(self,
                                          corner_radius=0
                                          )
        self.sidebar_frame.grid(row=1,
                                column=0,
                                rowspan=5,
                                sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
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
        self.scrollable_label_button_frame = sc(self.sidebar_frame, 
                                                corner_radius=0, 
                                                scrollbar_button_hover_color=("#5A5757"),
                                                border_width=1)
        self.scrollable_label_button_frame.grid(row=4, 
                                                column=0, 
                                                pady=0, 
                                                padx=(0, 0), 
                                                columnspan=2, 
                                                sticky="nsew")
        
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
        self.tabview.tab("Общие показатели").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Общие показатели").grid_rowconfigure(0,weight=1)
        self.tabview.add("Tab 2")
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        #=========================================================================================

        self.event_frame = EventTabFrame(master=self.tabview.tab("Общие показатели"))
        self.event_frame.grid(sticky="nsew")


        #======================================================================
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