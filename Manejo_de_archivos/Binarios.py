from os import strerror
from sys import path
def conseguir_ruta():
    return path[0]
  
def escribir_archivo(ruta):
    try:
        datos = bytearray(10)
        for i in range(len(datos)):
            datos[i] = 10 + i
        archivo = open(f"{ruta}"+ "\\Archivos\\icono.png","wb")
        archivo.write(datos)
        archivo.close()
    except IOError as exc:
        print("!ERROR¡", strerror(exc.errno))

def leer_archivo(ruta):
    try:
        archivo_leer = open(f"{ruta}"+ "\\Archivos\\Archivo.bin","rb")
        datos = bytearray(archivo_leer.read())
        archivo_leer.close()
        for i in datos:
            print(hex(i), end=" ")
    except Exception as exc:
        print("!ERROR¡", strerror(exc.errno))    

x = conseguir_ruta()
escribir_archivo(x)
leer_archivo(x)