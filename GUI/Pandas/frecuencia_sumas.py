import tkinter as tk
from tkinter import messagebox
#import PyPDF2 -> Ayuda browser
from PIL import Image,ImageTk
import pandas as pd
#from tkinter.filedialog import askopenfile -> Ayuda browser

# -> Calculas los datos ingresados
def calcular ():
    str_iteraciones = iteraciones.get()
    if str_iteraciones.isdigit():
        n_iteraciones = int(str_iteraciones)
    else:
        messagebox.showinfo(title="RESULT",message="Datos ingresados de manera incorrecta")

# -> Inicia la pantalla
def root_create():
    root = tk.Tk()
    root.title("{:>72}".format("Dados"))
    root.iconbitmap(r"GUI\Pandas\dado.ico")
    caracteristicas(root)
    elementos(root)  

# -> Caracteristicas de la pantalla
def caracteristicas(root):
    width_root = 560
    height_root = 600
    root.geometry("{}x{}".format(width_root,height_root))
    height_screen = root.winfo_screenheight() #Value about your screen
    width_screen = root.winfo_screenwidth() #Value about your screen
    x_center = int(width_screen/2 - width_root/2) 
    y_center = int(height_screen/2 - height_root/2)
    root.geometry(f"{width_root}x{height_root}+{x_center}+{y_center}") #Only allow int variables
    root.resizable(False,False)

# -> Coloca elementos en la pantalla
def elementos(root):
    instruction_one = tk.Label(root,text="{:>44}".format("Cantidad de Iteraciones: "),font="Roboto",pady=10)
    instruction_one.grid(column=0,row=0)
    iteraciones = tk.Entry(root,font ="Roboto",width=10)
    iteraciones.grid(column=1,row=0)
    instruction_two = tk.Label(root,text="{:>46}".format("Numero de dados: "),font="Roboto",pady=10,padx=1)
    instruction_two.grid(column=0,row=1)
    dados = tk.Entry(root,font ="Roboto",width=10).grid(column=1,row=1)
    button_icon = tk.PhotoImage(file=r"GUI\Pandas\calculadora.png")
    calcular_btn = tk.Button(root,text="Calcular",width=110,font="Roboto",compound=tk.LEFT,image=button_icon,padx=15,command=calcular)
    calcular_btn.place(x=380,y=20)
    
if __name__ == "__main__":
    root_create()


#
#Cargar plot creado en Pandas
#

#plot = Image.open(r"C:\Users\pc\Python\Jupyter\Graphs\first_graph.png")
#plot = ImageTk.PhotoImage(plot)
#plot_label = tk.Label(image=plot)
#plot_label.grid(column=0,row=4)
    
#
#UTILIDADES
#

#How to browse
#def open_file():
#    file = askopenfile(parent=root,mode="rb",title="Choose a file",filetype=[("Pdf file", "*.pdf")])
#    if file:
#        print("I was here")
#browse_text = tk.Button(root,font ="Raleway",text="Browse",command=lambda:open_file())
#browse_text.grid(column=1,row=2)