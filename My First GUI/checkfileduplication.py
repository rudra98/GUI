import hashlib
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("500x100")
x = ''
y = ''
def browsefunc():
    global x
    filename = filedialog.askopenfilename()
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    code1 = hash_md5.digest() 
    pathlabel.config(text=code1)
    x = code1
    


def browsefunc1():
    global y
    filename = filedialog.askopenfilename()
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    code1 = hash_md5.digest()
    pathlabel1.config(text=code1)
    y = code1
   
    
def gofunc():
    global x,y
    if x == y:
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
