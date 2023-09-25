import customtkinter as ctk
import button
import addprofile

class ButtonFrame(ctk.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master,
                       corner_radius=4,
                       border_width=0, #ширина рамки
                       fg_color="transparent", #цвет фона
                       **kwargs)
		self.button_1 = button.LittleAcessButton(self,
	                                                 text="+",
	                                                 command=self.open_input_dialog_event)
		self.button_1.grid(row=0,
	                           column=0)

		self.button_2 = button.LittleAcessButton(self,
	                                                 text="+c",
	                                                 command=self.open_input_dialog_event)
		self.button_2.grid(row=0,
	                           column=1)

		self.button_3 = button.LittleAcessButton(self,
	                                                 text="g",
	                                                 command=self.open_input_dialog_event)
		self.button_3.grid(row=0,
	                           column=2)

		self.button_3 = button.LittleOwnButton(self,
	                                               text="?",
	                                               command=self.open_input_dialog_event)
		self.button_3.grid(row=0,
	                           column=3)
		self.button_4 = button.LittleAcessButton(self,
	                                               text="@",
	                                               command=self.open_input_dialog_event)
		self.button_4.grid(row=0,
	                           column=4)
		self.toplevel_window = None

	def open_input_dialog_event(self):
		if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
			self.toplevel_window = addprofile.ToplevelWindow(self)  # create window if its None or destroyed
		else:
			self.toplevel_window.focus()  # if window exists focus it
		self.toplevel_window.after(100, self.toplevel_window.lift)