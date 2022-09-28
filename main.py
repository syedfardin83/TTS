from cgitb import enable
from distutils.cmd import Command
from faulthandler import disable
from logging import PlaceHolder
from operator import index, indexOf
from tkinter import *
from turtle import width
import pyttsx3
import random
import threading


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].name)
engine.setProperty ("rate", 178)

def clearHistory():
    print('Clearing')
    TextBox.config(state=NORMAL)
    TextBox.delete("1.0", "end")
    # root.update()
    TextBox.config(state=DISABLED)
    historyUpdate('HISTORY: ')
    # historyUpdate('HISTORY:')

def clearText():
    Texts.set('')

def resetSpeed():
    s1.set(133)

def getIdFromName(name):
    for x in voices:
        if(x.name==name):
            return x.id

def historyUpdate(text):
    TextBox.config(state=NORMAL)
    TextBox.insert(END, "\n"+text)
    TextBox.see(END)
    TextBox.config(state=DISABLED)

def speakReal():
    # enteredText = TextBox.get("1.0", "end-1c")
    enteredText = Texts.get()

    historyUpdate(f'Spoke: {enteredText}')
    TextBox.see(END)

    engine.say(enteredText)
    engine.runAndWait()

def speak():
    global t1
    t1 = threading.Thread(target=speakReal)
    t1.start()

# def stopVoice():
#     t1.join()
    # pass

def changeVoice(e):
    newName = str(clicked.get())
    newId = getIdFromName(newName)
    engine.setProperty('voice',newId)
    historyUpdate(f'Changed voice to {newName}')
    print("Voice changed to "+newName)
    
def changeSpeed(e):
    newSpeed = int(voice_speed.get())+50
    engine.setProperty ("rate", newSpeed)
    # historyUpdate(f'Changed voice speed to {newSpeed-60}')

def saveVoice():
    string = Texts.get()
    fileName = './'+str(random.randint(1,1000))+'.mp3'
    engine.save_to_file(string, fileName)
    engine.runAndWait()
    historyUpdate(f'Saved to file as {fileName}')

window_height = "240"
window_width = "850"
window_size = window_width+"x"+window_height

root = Tk()
root.title("Text To Speech")
# root.iconbitmap("logo.ico")
root.iconbitmap("C:\\Users\\DELL\\Desktop\\Coding\\Python\\Text To Speech\\logo.ico")
root.geometry(window_size)
# root.maxsize("750x400")
# root.minsize("750x400")
root.resizable(False,False)

TextBox = Text(root, height=12, width=60, padx=10, xscrollcommand=SCROLL)
TextBox.insert(END, "\nHISTORY: ")
TextBox.config(state=DISABLED)
TextBox.place(x=2, y=0)

Texts = StringVar()
Entered = Entry(root,width=83, textvariable=Texts)
# Entered.place(y=-500, x=-10)
Entered.place(x=2, y=200)

b1 = Button(root, text="Speak", command=speak)
# b1.grid(row=1,column=1)
b1.place(x=510,y=197)

options = []

for voice in voices:
    options.append(voice.name)


l1 = Label(text="Voice: ", font="Arial 10")
l1.place(x=530, y=0)

clicked = StringVar()
clicked.set( "Select Voice" )
drop = OptionMenu( root , clicked , *options, command=changeVoice)
# drop.grid(row=0, column=1)
drop.place(x=530,y=20)

l2 = Label(text="Voice Speed", font="Arial 10")
l2.place(x=530, y=70)

voice_speed = IntVar()
s1 = Scale( root, variable = voice_speed, from_ = 1, to = 300, orient = HORIZONTAL, command=changeSpeed)
s1.set(133)
s1.place(x=530, y=90)

b3 = Button(root, text="Default", command=resetSpeed)
b3.place(x=635, y=107)

b2 = Button(root, text='Save Voice',state=DISABLED, command=saveVoice)
b2.place(x=550, y=150)

b4 = Button(root, text='Clear',command=clearText)
b4.place(x=562, y=197)

b5 = Button(root, text='Clear',command=clearHistory)
b5.place(x=468,y=0)

# b6 = Button(root, text='Stop',command=stopVoice)
# b6.place(x=610,y=197)

root.mainloop()