import customtkinter as ctk
import widgets
import login
  
class RegWindow(ctk.CTkTabview):
  def __init__(self, master):
    super().__init__(master,
                     border_width=1,
                     corner_radius=3,
                     segmented_button_fg_color=("#5A5757"),
                     border_color=("#5A5757"),
                     segmented_button_selected_color=("#FF8C00"),
                     segmented_button_selected_hover_color=("#FF8C00")
                     )
    self.add("Авторизация")
    self.add("Регистрация")
    self.tab("Авторизация").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    self.tab("Регистрация").grid_columnconfigure(0, weight=1)
    #self.bot = self.on_tab_change.loginWindow
    #self.bind("<<NotebookTabChanged>>", self.bot.on_tab_change())

    #Блок вкладки авторизации
    self.login_entry = ctk.CTkEntry(self.tab("Авторизация"),
                                        placeholder_text="Пользователь",
                                        corner_radius=3)
    self.login_entry.grid(row=0,
                          column=0,
                          pady=(30, 0)
                          )
    self.login_entry.bind('<Key>', self.on_entry_change)

    self.login_password_entry = ctk.CTkEntry(self.tab("Авторизация"),
                                            placeholder_text="Пароль",
                                            show="*",
                                            corner_radius=3)
    self.login_password_entry.grid(row=1,
                                 column=0,
                                 pady=(10, 0)
                                 )
    self.login_password_entry.bind('<Key>', self.on_entry_change)

    self.conn_menu = widgets.SimpleMenu(self.tab("Авторизация"),
                                            values=["Value 1", "Value 2", "Value Long Long Long"],
                                            command=self.open_input_dialog_event
                                            )
    self.conn_menu.grid(row=2,
                            column=0,
                            pady=(10, 0)
                            )
    self.conn_menu.configure(state="disabled")

    self.enabled_on = "Пользователь сохранен!"
    self.enabled_off = "Сохранить пользователя"
    self.enabled = ctk.StringVar(value=self.enabled_off)

    self.checkbutton_log = ctk.CTkCheckBox(self.tab("Авторизация"),
                                           textvariable=self.enabled,
                                           variable=self.enabled, 
                                           offvalue=self.enabled_off,
                                           onvalue=self.enabled_on,
                                           corner_radius=4,
                                           border_width=1,
                                           hover_color=("#FF8C00"),
                                           font=ctk.CTkFont(family="Courier new")
                                           )
    self.checkbutton_log.grid(row=3,
                              column=0,
                              columnspan=2,
                              pady=(10, 0)
                              )
    self.checkbutton_log.configure(state="disabled")
    #========================================================================

    #Блок вкладки регистрации
    self.reg_entry = ctk.CTkEntry(self.tab("Регистрация"),
                                            placeholder_text="Логин",
                                            corner_radius=3)
    self.reg_entry.grid(row=0,
                              column=0,
                              pady=(30, 0)
                              )

    self.name_entry = ctk.CTkEntry(self.tab("Регистрация"),
                                            placeholder_text="Имя пользователя",
                                            corner_radius=3)
    self.name_entry.grid(row=1,
                              column=0,
                              pady=(10, 0)
                              )

        
    self.password_entry = ctk.CTkEntry(self.tab("Регистрация"),
                                            placeholder_text="Пароль",
                                            show="*",
                                            corner_radius=3)
    self.password_entry.grid(row=2,
                                 column=0,
                                 pady=(10, 0)
                                 )

    self.password_entry = ctk.CTkEntry(self.tab("Регистрация"),
                                            placeholder_text="Повторите пароль",
                                            show="*",
                                            corner_radius=3)
    self.password_entry.grid(row=3,
                                 column=0,
                                 pady=(10, 0)
                                 )

    self.reg_conn_menu = widgets.SimpleMenu(self.tab("Регистрация"),
                                            values=["Подключиться к базе", "Создать новое пространство"],
                                            command=self.open_input_dialog_event)
    self.reg_conn_menu.grid(row=4,
                            column=0,
                            pady=(10, 0)
                            )
    self.reg_conn_menu.configure(state="disabled")

    self.enabled_on = "Пользователь сохранен!"
    self.enabled_off = "Сохранить пользователя"
    self.enabled = ctk.StringVar(value=self.enabled_off)

    self.checkbutton = ctk.CTkCheckBox(self.tab("Регистрация"),
                                           textvariable=self.enabled,
                                           variable=self.enabled, 
                                           offvalue=self.enabled_off,
                                           onvalue=self.enabled_on,
                                           corner_radius=4,
                                           border_width=1,
                                           hover_color=("#FF8C00"),
                                           font=ctk.CTkFont(family="Courier new")
                                           )
    self.checkbutton.grid(row=5,
                              column=0,
                              columnspan=2,
                              pady=(10, 20)
                              )
    


  def open_input_dialog_event():
    pass

  def on_entry_change(self, event):
    # Проверка, заполнены ли поля
    if self.login_entry.get() and self.login_password_entry.get():
      self.checkbutton_log.configure(state="normal")
      self.conn_menu.configure(state="normal")
    else:
      self.checkbutton_log.configure(state="disabled")
      self.conn_menu.configure(state="disabled")