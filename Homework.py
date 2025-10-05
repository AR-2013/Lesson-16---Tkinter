from tkinter import *

window = Tk()
window.geometry = ('600x600')
window.title = ('Homework')

greeting = Label(text="Hello!", fg='blue', bg='white')
greeting.pack()

button = Button(text="CLICK ME!", fg='yellow', bg='red')
button.pack()
        
window.mainloop()