from tkinter import *

window = Tk()
window.title('tkinter window')
window.geometry('300x300')

greeting = Label(text="Hello user", fg='black', bg='white')
button = Button(text="Click me", fg='black', bg='white')
entry = Entry(fg='yellow', bg='blue', width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Frame')
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()