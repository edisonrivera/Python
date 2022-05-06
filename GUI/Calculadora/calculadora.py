from tkinter import *
from ctypes import windll #Librería para más nitidez
#Crear ventana
ancho_ventana = 230
largo_ventana = 240

windll.shcore.SetProcessDpiAwareness(1) #Línes para nitidez
venta_principal = Tk()
#venta_principal.maxsize(ancho_ventana,largo_ventana) #Máximo que se podrá dimensionar la ventana
venta_principal.resizable(False,False) #El usuario no puede cambiar la dimensión
venta_principal.title("Calculadora Básica")
venta_principal.attributes("-alpha", 0.9) #Transparencia (0 a 1)
pantalla = Entry(venta_principal, font="Calibri 15") #Vista de calculadora
pantalla.grid(row=0,column=0,columnspan=4,padx=10,pady=5)
venta_principal.attributes("-topmost",1) #Jerarquía de ventanas
venta_principal.iconbitmap(r"C:\Users\pc\Python\GUI\Calculadora\estilos\icono.ico") #Cambia el icono por defecto
i = 0
"""
window.lift()               Funcion al igual que "-topmost"
window.lift(another_window)

window.lower()
window.lower(another_window)
"""
#Centrar la pantalla

ancho_pantalla = venta_principal.winfo_screenwidth()
largo_pantalla = venta_principal.winfo_screenheight()

centro_x = int(ancho_pantalla/2 - ancho_ventana/2)
centro_y = int(largo_pantalla/2 - ancho_ventana/2)
venta_principal.geometry(f"{ancho_ventana}x{largo_ventana}+{centro_x}+{centro_y}")
#Funciones
def entrada(valor):
    global i
    pantalla.insert(i,valor)
    i += 1

def limpiar ():
    pantalla.delete(0,END)
    i = 0

def resultado():
    ecuacion = pantalla.get()
    resultado = eval(ecuacion)
    limpiar()
    pantalla.insert(0,resultado)

#Botones
boton1 = Button(venta_principal,text="1", width=4,height=1, command= lambda:entrada(1))
boton2 = Button(venta_principal,text="2", width=4,height=1, command= lambda:entrada(2))
boton3 = Button(venta_principal,text="3", width=4,height=1, command= lambda:entrada(3))
boton4 = Button(venta_principal,text="4", width=4,height=1, command= lambda:entrada(4))
boton5 = Button(venta_principal,text="5", width=4,height=1, command= lambda:entrada(5))
boton6 = Button(venta_principal,text="6", width=4,height=1, command= lambda:entrada(6))
boton7 = Button(venta_principal,text="7", width=4,height=1, command= lambda:entrada(7))
boton8 = Button(venta_principal,text="8", width=4,height=1, command= lambda:entrada(8))
boton9 = Button(venta_principal,text="9", width=4,height=1, command= lambda:entrada(9))
boton0 = Button(venta_principal,text="0", width=4,height=1, command= lambda:entrada(0))

#Botones_funciones
boton_limpiar = Button(venta_principal,text="AC", width=4,height=1, command=limpiar)
boton_multiplicacion = Button(venta_principal,text="x", width=4,height=1, command= lambda:entrada("*"))
boton_dividir = Button(venta_principal,text="/", width=4,height=1, command= lambda:entrada("/"))
boton_restar = Button(venta_principal,text="-", width=4,height=1, command= lambda:entrada("-"))
boton_sumar = Button(venta_principal,text="+", width=4,height=1, command= lambda:entrada("+"))
boton_calcular = Button(venta_principal,text="=", width=12,height=1, command=resultado)
boton_parentesis_abrir = Button(venta_principal,text="(", width=4,height=1, command= lambda:entrada("("))
boton_parentesis_cerrar = Button(venta_principal,text=")", width=4,height=1, command= lambda:entrada(")"))
boton_decimal = Button(venta_principal,text=",", width=4,height=1, command=lambda:entrada(","))

#Agregar los botones
boton_limpiar.grid(row=1,column=2)
boton_parentesis_cerrar.grid(row=1,column=1)
boton_parentesis_abrir.grid(row=1,column=0)
boton_sumar.grid(row=1,column=3, pady=5)
boton1.grid(row=2,column=0)
boton2.grid(row=2,column=1)
boton3.grid(row=2,column=2)
boton_restar.grid(row=2,column=3, pady=5)
boton4.grid(row=3,column=0,)
boton5.grid(row=3,column=1)
boton6.grid(row=3,column=2)
boton_multiplicacion.grid(row=3,column=3, pady=5)
boton7.grid(row=4,column=0)
boton8.grid(row=4,column=1)
boton9.grid(row=4,column=2)
boton_dividir.grid(row=4,column=3, pady=5)
boton_decimal.grid(row=5, column=0)
boton0.grid(row=5,column=1)
boton_calcular.grid(row=5,column=2,columnspan=2,pady=5)

venta_principal.mainloop()