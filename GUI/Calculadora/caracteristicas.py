import tkinter
from tkinter.constants import LEFT
from tkinter.messagebox import showinfo
ventana = tkinter.Tk()
ventana.geometry("800x500") #Cambiar las dimensiones de la ventana
ventana.title("Hola")
def saludo ():
    print("JAJAJAJAJAJA")

def saludo2(nombre):
    print("JAJA" + nombre)

def texto ():
    salida = text1.get()
    etiqueta_salida["text"] = salida
    print(salida)

def download():
    showinfo(title="Information", message="Hello World")

etiqueta = tkinter.Label(ventana, text="Hola mundo",bg="lightblue")
#etiqueta.pack(side=tkinter.BOTTOM)#Lo colocamos y se queda estático
#etiqueta.pack(fill=tkinter.Y, expand=False) #"X o Y" estiran todo en su eje
etiqueta_salida = tkinter.Label(etiqueta)
etiqueta_salida.pack()
etiqueta.pack(fill=tkinter.BOTH, expand=True) #Cubre toda la pantalla
boton = tkinter.Button(etiqueta,text = "Click", padx=50,pady=10,command=lambda: saludo2("Python"))
boton.pack()
text1 = tkinter.Entry(etiqueta, font = "Helvetica 20")
text1.pack()
boton1 = tkinter.Button(etiqueta, text="click", command=texto)
boton1.pack()
button2_image =  tkinter.PhotoImage(file=r"C:\Users\pc\Python\GUI\Calculadora\estilos\cow.png")
boton2 = tkinter.Button(etiqueta, text="Download",compound=LEFT, command=download,image=button2_image)

boton2.pack(ipadx=5,ipady=5,expand=False)

ventana.mainloop() #Lleva el registro de  todo lo que sucede