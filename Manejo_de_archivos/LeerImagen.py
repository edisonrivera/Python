from os import strerror
from sys import path
def ruta_leer():
    return path[0]

def leer_imagen(ruta):
    try:
        imagen = open(f"{ruta}" + "\\Archivos\\icono.png","rb")
        datos = bytearray(imagen.read())
        for i in datos: 
            print(hex(i),end=" ")
        imagen.close()
    except Exception as exc:
        print("¡ERROR!", strerror(exc.errno))

x = ruta_leer()
leer_imagen(x)

#FUI AL BAÑO