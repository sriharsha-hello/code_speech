from tkinter import *
from tkinter import filedialog
#from tkFileDialog import *
filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename,'w')
    f.write(t)
    f.close()

def saveAs():
    #def asksaveasfile()
    f= filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    t=text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        print("oops, Unable to save")

def openFile():
    #def askopenfile
    f=filedialog.askopenfile(mode ='r')
    t=f.read()
    text.delete(0.0, END)
    text.insert(0.0,t)

root=Tk()
root.title("its my editor")
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)

text=Text(root,width=400,height=400)
text.pack()

menubar=Menu(root)
filemenu=Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="open", command=openFile)
filemenu.add_command(label="save", command=saveFile)

filemenu.add_command(label="saveAs...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="file",menu=filemenu)

root.config(menu=menubar)
root.mainloop()
