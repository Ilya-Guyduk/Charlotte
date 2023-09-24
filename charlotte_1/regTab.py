import customtkinter as ctk


class RegTab():
	def __init__(self, *args, **kwargs):
		self.reg_entry = ctk.CTkEntry(self,
	                                            placeholder_text="Логин",
	                                            corner_radius=3)
		self.reg_entry.grid(row=0,
	                              column=0,
	                              pady=(30, 10)
	                              )
		self.reg_entry.bind('<Key>', self.on_reg_entry_change)
	        
		self.password_entry = ctk.CTkEntry(self,
	                                            placeholder_text="Пароль",
	                                            show="*",
	                                            corner_radius=3)
		self.password_entry.grid(row=1,
	                                 column=0,
	                                 pady=(10, 10)
	                                 )
		self.password_entry.bind('<Key>', self.on_reg_entry_change)

		self.password_entry_retry = ctk.CTkEntry(self.reg_window.tab("Регистрация"),
	                                            placeholder_text="Повторите пароль",
	                                            show="*",
	                                            corner_radius=3)
		self.password_entry_retry.grid(row=2,
	                                 column=0,
	                                 pady=(10, 10)
	                                 )
		self.password_entry_retry.bind('<Key>', self.on_reg_entry_change)

		self.enabled_on = "Пользователь сохранен!"
		self.enabled_off = "Сохранить пользователя"
		self.enabled = ctk.StringVar(value=self.enabled_off)

		self.checkbutton = ctk.CTkCheckBox(self.reg_window.tab("Регистрация"),
	                                           textvariable=self.enabled,
	                                           variable=self.enabled, 
	                                           offvalue=self.enabled_off,
	                                           onvalue=self.enabled_on,
	                                           corner_radius=4,
	                                           border_width=1,
	                                           hover_color=("#FF8C00"),
	                                           font=ctk.CTkFont(family="Courier new")
	                                           )
		self.checkbutton.grid(row=3,
	                              column=0,
	                              columnspan=2,
	                              pady=(10, 10)
	                              )
		self.checkbutton.configure(state="disabled")
	    
		self.reg_window.grid(row=1,
	                             padx=5,
	                             pady=(0, 5),
	                             column=0,
	                             sticky="nsew")
	        #окно уведомлений
		self.reg_notification = ctk.CTkLabel(self.reg_window.tab("Регистрация"),
	                                                    text="",
	                                                    font=ctk.CTkFont(family="Courier new")
	                                                    )
		self.reg_notification.grid(row=4,
	                                   pady=0,
	                                   padx=0,
	                                     sticky="nsew",
	                                     columnspan=2)




	     #Фрейм окна с кнопками регистрации
		self.reg_button_frame = ctk.CTkFrame(self.reg_window.tab("Регистрация"),
	                                         corner_radius=0,
	                                         border_width=1)
		self.reg_button_frame.grid(row=7,
	                               column=0,
	                               sticky="nsew")
		self.reg_button_frame.grid_columnconfigure((0, 1), weight=1)

		self.login_button = button.AcessButton(self.reg_button_frame,
	                                                text="Создать",
	                                                command=self.log_entry)
		self.login_button.grid(row=0,
	                               column=0,
	                               pady=(6, 6),
	                               padx=(6, 0),
	                               sticky="nsew")
	            
		self.cancel_button = button.CancelButton(self.reg_button_frame,
	                                                text="Отмена",
	                                                command=self.cancel)
		self.cancel_button.grid(row=0,
	                                column=1,
	                                pady=(6, 6),
	                                padx=(5, 6),
	                                sticky="nsew")


	def log_entry(self):
		login = self.login_entry.get()
		password = self.login_password_entry.get()
		checkbox_state = self.enabled.get()
		hashed_password = hashlib.sha256(password.encode()).hexdigest()
		with sqlite3.connect('Charlotte') as conn:
			cursor = conn.cursor()
			cursor.execute("SELECT account_id FROM ACCOUNTS WHERE login = ? AND password = ?", (login, hashed_password))
			result = cursor.fetchone()
			if result:
				globaldata.global_id = int(result[0]) #переменная с user_id для формирования информации
				#if checkbox_state == self.enabled_on:
                #    save_credentials(login, password)
				self.destroy()
				app = test.App()
				app.mainloop()  
			else:
				self.login_notification.configure(text="Неверные данные для входа!", text_color=("#FF8C00"))


	def on_reg_entry_change(self, event):
		# Проверка, заполнены ли поля
		if self.reg_entry.get() and self.password_entry.get() and self.password_entry_retry.get():
			self.checkbutton.configure(state="normal")
		else:
			self.checkbutton.configure(state="disabled")