from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo

root = Tk()
root.title("Check Widget")
root.geometry("300x300")

text = StringVar()

def get_text():
    messagebox.showinfo(title="RESULT",message=text.get())

password = Entry(root,textvariable=text,show="*").pack()
Button(root,text="Click",command=get_text).pack()
root.mainloop()