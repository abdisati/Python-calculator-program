from tkinter import *
def button_press(num):
    pass


def equals():
    pass


def clear():
    pass

window = Tk()


window.title("Calculator Program") #set the title
window.geometry("500x500") #set the geometry of the window

equation_text = ""   #set the an empty string

equation_label = StringVar()

label = Label(window,textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()





window.mainloop()