from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo

root = Tk()
root.title("Check Widget")
root.geometry("300x300")

check= StringVar()

def agreement_changed():
    messagebox.showinfo(title="RESULT",message=check.get())

Checkbutton(root,text="Marca esta opcion",command=agreement_changed,variable=check,onvalue="agree",offvalue="disagree").pack()

root.mainloop()