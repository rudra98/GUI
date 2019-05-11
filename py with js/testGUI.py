
import hashlib
import eel

eel.init('Index')
x = ''
y = ''

@eel.expose
def browsefunc(path):
    global x
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    code1 = hash_md5.digest()
    x = code1
    
@eel.expose
def browsefunc1(path2):
    global y
    hash_md5 = hashlib.md5()
    with open(path2, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    code1 = hash_md5.digest()
    y = code1
   
@eel.expose    
def gofunc():
    global x,y
    if x == y:
        return "Both are same"
    else:
        return "They are different"
        
        
eel.start('index.html')    