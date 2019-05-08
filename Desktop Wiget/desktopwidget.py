import os
import psutil

var = str(psutil.virtual_memory())
var2 = var.split(',')

from tkinter import *
root = Tk()
root.geometry("100x100")
root.attributes('-alpha', 0.5)
pathlabel = Label(root)
pathlabel.pack(side=TOP)
pathlabel.config(text=var2[2])
root.mainloop()


