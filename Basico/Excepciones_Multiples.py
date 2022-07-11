#try:
#    a = int(input("Ingrese un numero:"))
#except Exception as a:
#    print(type(a).__name__)

try:
    a = int(input("Ingrese un numero:"))
    10/a
except TypeError:
    print ("Ingresaste el dato de manera incorrecta")
except ValueError:
    print("Tienes que ingresar un numero")
except ZeroDivisionError: #"PADRE" ArithmeticError
    print ("M A T H   E R R O R")

def profesor (estudiante = None):
    if estudiante is None:
        print ("Está vacío")
    else:
        print ("Todo bien")

profesor()

"""
def probar (x = None):
    if x is None:
        raise ValueError("Está vacío")
probar()
"""

#if (0 < 1): #Despliega un mensaje al usuario para que sea "más" amigable
#    raise Exception ("Numero menor a 0")