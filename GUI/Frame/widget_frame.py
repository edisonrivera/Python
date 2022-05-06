from tkinter import *

def create_input_frame(container):
    frame = Frame(container)
    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(0,weight=3)
    Label(frame, text="Buscar:").grid(row=0,column=0,sticky=W)
    keyword = Entry(frame,width=30)
    keyword.focus()
    keyword.grid(row=0,column=1,sticky=W)
    Label(frame, text="Replace:").grid(row=1,column=0,sticky=W)
    replacement = Entry(frame,width=30)
    replacement.grid(row=1,column=1,sticky=W)
    match_case = IntVar()
    match_check_widget = Checkbutton(frame,text="Match case",variable=match_case,command=lambda: print(match_case.get()))
    match_check_widget.grid(row=2,column=0,sticky=W)
    wrap_around = IntVar()
    wrap_check_widget = Checkbutton(frame,variable=wrap_around,text="Wrap Around", command=lambda: print(wrap_around.get()))
    wrap_check_widget.grid(row=3,column=0,sticky=W)
    for widget in frame.winfo_children():
        widget.grid(padx=0,pady=5)
    return frame

def create_buttons(container):
    frame = Frame(container)
    frame.columnconfigure(0,weight=1)
    Button(frame,text="Find Next").grid(row=0,column=0)
    Button(frame,text="Replace").grid(row=1,column=0)
    Button(frame,text="Replace All").grid(row=2,column=0)
    Button(frame,text="Cancel").grid(row=3,column=0)
    for widget in frame.winfo_children():
        widget.grid(padx=0,pady=3)
    return frame

def create_main_window():
    root = Tk()
    root.title("Password Manager")
    root.geometry("400x150")
    root.resizable(False,False)
    root.attributes("-toolwindow",True) #Remove the minimize/maximize buttons
    root.columnconfigure(0,weight=4)
    root.columnconfigure(1,weight=1)
    input_frame = create_input_frame(root)
    input_frame.grid(column=0,row=0)
    button_frame = create_buttons(root)
    button_frame.grid(row=0,column=1)
    root.mainloop()

if __name__ == "__main__":
    create_main_window() 