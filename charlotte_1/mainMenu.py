import customtkinter as ctk


class OptionMenuHolder(ctk.CTkOptionMenu):
  #
  def __init__(self, master):
    super().__init__(master)

    self.frame_mainmenu = ctk.CTkFrame(self)
    self.frame_mainmenu.grid(row=0,
                      column=0,
                      columnspan=4,
                      sticky="new")

    self.optionmenu_1 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                          values=["Option 1", "Option 2", "Option 42 long long long..."],
                                          corner_radius=0,
                                          fg_color=("#696969"),
                                          button_color=("#696969"),
                                          dropdown_hover_color=("#FF8C00"))
    self.optionmenu_1.grid(row=0,
                           column=0)
    self.optionmenu_1.set("Настройки")

    self.optionmenu_2 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#696969"),
                                                dropdown_hover_color=("#FF8C00"))
    self.optionmenu_2.grid(row=0,
                           column=1)
    self.optionmenu_2.set("Файл")

    self.optionmenu_3 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#696969"),
                                                dropdown_hover_color=("#FF8C00"))
    self.optionmenu_3.grid(row=0,
                           column=2)
    self.optionmenu_3.set("Терминал")

    self.optionmenu_4 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#696969"),
                                                dropdown_hover_color=("#FF8C00"))
    self.optionmenu_4.grid(row=0,
                           column=3)
    self.optionmenu_4.set("Вид")

    self.optionmenu_5 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#696969"),
                                                dropdown_hover_color=("#FF8C00"))
    self.optionmenu_5.grid(row=0,
                           column=4)
    self.optionmenu_5.set("Сервисы")

    self.optionmenu_6 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#696969"),
                                                dropdown_hover_color=("#FF8C00"))
    self.optionmenu_6.grid(row=0,
                           column=5)
    self.optionmenu_6.set("Метрики")

    self.optionmenu_7 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#696969"),
                                                dropdown_hover_color=("#FF8C00"))
    self.optionmenu_7.grid(row=0,
                           column=6)
    self.optionmenu_7.set("Главный экран")

    self.optionmenu_7 = ctk.CTkOptionMenu(self.frame_mainmenu,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#696969"),
                                                dropdown_hover_color=("#FF8C00"))
    self.optionmenu_7.grid(row=0,
                           column=7)
    self.optionmenu_7.set("Справка")
