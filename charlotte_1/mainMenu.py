import customtkinter


class MainMenu(customtkinter.CTkOptionMenu):
  def __init__(self, master, command=None, **kwargs):
    super().__init__(master, **kwargs)

    self.frame_1 = customtkinter.CTkFrame(self)
    self.frame_1.grid(row=0, column=0, columnspan=4, sticky="new")

      self.optionmenu_1 = customtkinter.CTkOptionMenu(self.frame_1,
                                                      values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                      corner_radius=0,
                                                      fg_color=("#696969"),
                                                      button_color=("#778899"))
      self.optionmenu_1.grid(row=0, column=0)
      self.optionmenu_1.set("Файл")

  self.optionmenu_2 = customtkinter.CTkOptionMenu(self.frame_1,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#778899"))
  self.optionmenu_2.grid(row=0, column=1)
  self.optionmenu_2.set("Настройки")

  self.optionmenu_3 = customtkinter.CTkOptionMenu(self.frame_1,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#778899"))
  self.optionmenu_3.grid(row=0, column=2)
  self.optionmenu_3.set("Терминал")

  self.optionmenu_4 = customtkinter.CTkOptionMenu(self.frame_1,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#778899"))
  self.optionmenu_4.grid(row=0, column=3)
  self.optionmenu_4.set("Вид")

  self.optionmenu_5 = customtkinter.CTkOptionMenu(self.frame_1,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#778899"))
  self.optionmenu_5.grid(row=0, column=4)
  self.optionmenu_5.set("Сервисы")

  self.optionmenu_6 = customtkinter.CTkOptionMenu(self.frame_1,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#778899"))
  self.optionmenu_6.grid(row=0, column=5)
  self.optionmenu_6.set("Метрики")

  self.optionmenu_7 = customtkinter.CTkOptionMenu(self.frame_1,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#778899"))
  self.optionmenu_7.grid(row=0, column=6)
  self.optionmenu_7.set("Главный экран")

  self.optionmenu_8 = customtkinter.CTkOptionMenu(self.frame_1,
                                                values=["Option 1", "Option 2", "Option 42 long long long..."],
                                                corner_radius=0,
                                                fg_color=("#696969"),
                                                button_color=("#778899"))
  self.optionmenu_8.grid(row=0, column=7)
  self.optionmenu_8.set("Справка")