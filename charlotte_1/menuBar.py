import tkinter as tk


class OptionMenuHolder(tk.Menu):
  #
  def __init__(self, master, **kwargs):
    super().__init__(master)

	  # Menu Bar
    self.m1 = tk.Menu(self, tearoff=0)
    #self.config(menu=self)
    self.m1.add_command(label="Open File")
    self.m1.add_separator()
    self.m1.add_command(label="Save File")
    self.add_cascade(label="File",menu=self.m1)

    self.m2 = tk.Menu(self, tearoff=0)
    self.m2.add_command(label="Light theme")
    self.m2.add_command(label="Dark theme")
    self.m2.add_separator()
    self.m2.add_command(label="System theme",command=lambda : self.theme_selection(2))
    #self.config(menu=self)
    self.add_cascade(label="Setting",menu=self.m2)
        
    self.m3 = tk.Menu(self, tearoff=0)
    self.m3.add_command(label="help!",command=lambda : self.help_us())

    #self.config(menu=self)
    self.add_cascade(label="Help",menu=self.m3)
        
   
        


