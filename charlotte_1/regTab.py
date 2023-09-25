import customtkinter as ctk
import sqlite3
import button 
class RegTab(ctk.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)
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

		self.password_entry_retry = ctk.CTkEntry(self,
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

		self.checkbutton = ctk.CTkCheckBox(self,
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
	    
		#self.reg_window.grid(row=1,
	    #                         padx=5,
	    #                         pady=(0, 5),
	    #                         column=0,
	    #                         sticky="nsew")
	        #окно уведомлений
		self.reg_notification = ctk.CTkLabel(self,
	                                                    text="",
	                                                    font=ctk.CTkFont(family="Courier new")
	                                                    )
		self.reg_notification.grid(row=4,
	                                   pady=0,
	                                   padx=0,
	                                     sticky="nsew",
	                                     columnspan=2)




	     #Фрейм окна с кнопками регистрации
		self.reg_button_frame = ctk.CTkFrame(self,
	                                         corner_radius=0,
	                                         border_width=1)
		self.reg_button_frame.grid(row=7,
	                               column=0,
	                               sticky="nsew")
		self.reg_button_frame.grid_columnconfigure((0, 1), weight=1)

		self.login_button = button.AcessButton(self.reg_button_frame,
	                                                text="Создать",
	                                                command=self.registration)
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


	def registration(self):
		self.conn = sqlite3.connect('Charlotte')
		self.cursor = self.conn.cursor() 
		login = self.reg_entry.get()
		password = self.password_entry.get()
		password_retry = self.password_entry_retry.get()
		if not login and not password:
			self.reg_notification.configure(text="Укажите данные для регистрации!",
                                    text_color=("#FF8C00"))
		elif not login:
			self.reg_notification.configure(text="Укажите логин!",
                                    text_color=("#FF8C00"))
		elif not password:
			self.reg_notification.configure(text="Укажите пароль!",
                                    text_color=("#FF8C00"))
		elif password != password_retry:
			self.reg_notification.configure(text="Пароли не совпадают!",
                                    text_color=("#FF8C00"))
		else:    
			hashed_password = hashlib.sha256(password.decode()).hexdigest()
			with sqlite3.connect('Charlotte') as conn:
				cursor = conn.cursor()
				cursor.execute("INSERT INTO ACCOUNTS (login, password) VALUES (?, ?)", (login, hashed_password))
				self.result = cursor.fetchone()        
				self.reg_notification.configure(text="Пользователь добавлен!",
                                        text_color=("#FF8C00"))

	#функция закрытия окна по нажатию на кнопку "cancel"
	def cancel(self):
		self.destroy()

	def on_reg_entry_change(self, event):
		# Проверка, заполнены ли поля
		if self.reg_entry.get() and self.password_entry.get() and self.password_entry_retry.get():
			self.checkbutton.configure(state="normal")
		else:
			self.checkbutton.configure(state="disabled")