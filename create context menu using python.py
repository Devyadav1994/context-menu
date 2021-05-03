import tkinter
from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Context Menu")

text = Text(root, font=("haveltica 15 bold"), bd=2)
text.focus()
text.pack()

def cut_text():
    text.event_generate(("<<Cut>>"))

def copy_text():
    text.event_generate(("<<Copy>>"))

def paste_text():
    text.event_generate(("<<paste>>"))


#Create a menubar

menu = Menu(root, tearoff = 0)
menu.add_command(label="Cut", command=cut_text)
menu.add_command(label="Copy", command=copy_text)
menu.add_command(label="Paste", command=paste_text)
menu.add_separator()
menu.add_command(label="Exit", command=root.destroy)

#define functions to popup the
#context menu on right button click

def context_menu(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()

root.bind("<Button-3>", context_menu)
root.mainloop()

