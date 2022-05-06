from os import strerror
from sys import path
def conseguir_ruta():
    return path[0]
  
def escribir_archivo(ruta):
    try:
        contador_caracteres = contador_lines = 0
        for linea in open(f"{ruta}"+ "\\Archivos\\Cubos.txt","r",encoding="utf-8"):
            contador_lines += 1
            for i in linea:
                contador_caracteres += 1
        print("-> LINEAS TOTALES:",contador_lines,"\n-> CARACTERES TOTALES: ",contador_caracteres)
    except Exception as exc:
        print("!ERROR¡", strerror(exc.errno))

x = conseguir_ruta()
escribir_archivo(x)

#Otro ejemplo para leer líneas y caracteres de un archivo de una forma más legible, además
#el método close() se invocará automáticamente una vez se acabe de leer el archivo.