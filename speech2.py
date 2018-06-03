import speech_recognition as sr
import os
# get audio from the microphone
from cffi.setuptools_ext import execfile
from prompt_toolkit.output import Output
import sys

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
    #print("Speak:")
    #audio = r.listen(source)
try:
    txt = r.recognize_google(audio)
    with open("output.txt","w") as fo:
        txt =fo.write(txt)
        import os
        os.system("start notepad.exe output.txt")
        fo.close()

        #print(txt)
    """text=r.recognize_google(audio)
    print(text)
    text_file = open("Output.txt", "r")
    text_file.write(text)
    text_file.close()
    sys.argv  = text
    file= notepad.exeoutput.txt
    os.system(file)
    #execfile('./myowntext.py')
    #exec(open("./myowntext.py").read())"""

    print("Done listening!")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))