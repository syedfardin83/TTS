from logging import PlaceHolder
from operator import index, indexOf
from tkinter import *
from turtle import width
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak():
    enteredText = TextBox.get("1.0", "end-1c")
    engine.say(enteredText)
    engine.runAndWait()

def changeVoice(a):
    new = (clicked.get())
    engine.setProperty('voice',voices[int(new)].id)
    

window_height = "500"
window_width = "200"
window_size = window_height+"x"+window_width

root = Tk()
root.title("Text To Speech")
# root.geometry(window_size)
# root.maxsize("750x400")
# root.minsize("750x400")
root.resizable(False,False)

Texts = StringVar()
TextBox = Text(root, height=10, width=60)
TextBox.grid(row=0, column=0)

b1 = Button(root, text="Speak", command=speak)
b1.grid(row=0,column=1)

options = []

for voice in voices:
    options.append(voice.name)

clicked = StringVar()
clicked.set( "Select Voice" )
drop = OptionMenu( root , clicked , *options, command=changeVoice)
drop.grid(row=1, column=1)
root.mainloop()