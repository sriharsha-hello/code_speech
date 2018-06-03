from tkinter import *
from tkinter import filedialog
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
try:
    text= r.recognize_google(audio)
    print(text)
    add(text)
    #print("you said :\n"+ r.recognize_google(audio))
    #print(text)
    #exec(open("./myowntext.py").read())
    print("Done listening!")
#except Exception as e:
 #   print("error",type(e).__name__)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
except :
    pass
filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
    #label :check

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
def add(text):
    root=Tk()
    root.title("its my editor")
    root.minsize(width=400,height=400)
    root.maxsize(width=400,height=400)

    text=Text(root,width=400,height=400)
    text.pack()

    menubar=Menu(root)
    filemenu=Menu(menubar)
    print(text,filemenu.add_command(label="New", command=newFile))
    filemenu.add_command(label="open", command=openFile)
    filemenu.add_command(label="save", command=saveFile)


    filemenu.add_command(label="saveAs...", command=saveAs)
    filemenu.add_separator()
    filemenu.add_command(label="Quit",command=root.quit)
    menubar.add_cascade(label="file",menu=filemenu)

    root.config(menu=menubar)
    root.mainloop()
