import customtkinter as ctk
from CTkMenuBar import *

class OptionMenuHolder(CTkMenuBar):
  #
  def __init__(self, master, **kwargs):
    super().__init__(master)

    #menu = CTkMenuBar(root)
    button_1 = self.add_cascade("Файл")
    button_2 = self.add_cascade("Edit")
    button_3 = self.add_cascade("Settings")
    button_4 = self.add_cascade("About")

    dropdown1 = CustomDropdownMenu(widget=button_1)
    dropdown1.add_option(option="Open", command=lambda: print("Open"))
    dropdown1.add_option(option="Save")
    dropdown1.add_separator()

    self.sub_menu = dropdown1.add_submenu("Export As")
    self.sub_menu.add_option(option=".TXT")
    self.sub_menu.add_option(option=".PDF")

    self.dropdown2 = CustomDropdownMenu(widget=button_2)
    self.dropdown2.add_option(option="Cut")
    self.dropdown2.add_option(option="Copy")
    self.dropdown2.add_option(option="Paste")

    self.dropdown3 = CustomDropdownMenu(widget=button_3)
    self.dropdown3.add_option(option="Preferences")
    self.dropdown3.add_option(option="Update")

    self.dropdown4 = CustomDropdownMenu(widget=button_4)
    self.dropdown4.add_option(option="Hello World")
