import hashlib
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("500x100")
x = [0]

def browsefunc():
    filename = filedialog.askopenfilename()
    var1 = hashlib.md5(filename.encode())
    code1 = var1.digest()
    pathlabel.config(text=code1)
    x.append(code1)

def browsefunc1():
    filename = filedialog.askopenfilename()
    var1 = hashlib.md5(filename.encode())
    code1 = var1.digest()
    pathlabel1.config(text=code1)
    x.append(code1)
    
    
def gofunc():
    if x[1] == x[2]:
        pathlabel2.config(text='Both are same')
    else:
        pathlabel2.config(text='They are different')
        
        
browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack(side=LEFT)
pathlabel = Label(root)
pathlabel.pack(side=LEFT)


browsebutton1 = Button(root, text="Browse Again", command=browsefunc1)
browsebutton1.pack(side=RIGHT)
pathlabel1 = Label(root)
pathlabel1.pack(side=RIGHT)


go = Button(root, text="GO BABY GO", command=gofunc)
go.pack(side=BOTTOM)
pathlabel2 = Label(root)
pathlabel2.pack(side=BOTTOM)

root.mainloop()





















'''
import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 
'''