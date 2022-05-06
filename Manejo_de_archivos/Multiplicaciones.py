#!/usr/bin/python
#from io import UnsupportedOperation hace funcionales las líneas 22 y 23
from os import strerror
from sys import path

def ruta_desktop():
    return path[0]

def verificar (ruta):
    try:
        archivo = open(f"{ruta}"+"\\Archivos\\Cubos.txt","w",encoding="utf-8")
        archivo.write("|"+"TABLAS DE EXPONENTES".center(32," ")+"|\n")
        archivo.write("----------------------------------\n")
        archivo.write("| NUMERO | OPERACION | RESULTADO |\n")
        archivo.write("----------------------------------\n")
        def rellenar():
            for i in range (11):
                archivo.write("|" + f"{i}".center(8," ") + "|" + f"{i}^3".center(11," ") + "|" + f"{i**3}".center(11," ") + "|\n")
            archivo.write("----------------------------------")
            archivo.close()
        rellenar()
    #except UnsupportedOperation: excepción lanzada cuando el archivo se abre en ("r") y se quiere escribir
    #    print("¡NOT PERMITTED!") 
    except Exception as exc:
        print("¡ERROR! :(",strerror(exc.errno))
    #except IOError as er:
    #    print("¡ERROR! :(" + strerror(er.errno))

def conteo (ruta):
    archivo = open(f"{ruta}"+"\\Archivos\\Cubos.txt","r",encoding="utf-8")
    linea = archivo.readline()
    cont_caracteres = cont_lineas = 0
    while linea != "":
        cont_lineas +=1
        for i in linea:
            cont_caracteres += 1
        linea = archivo.readline()
    archivo.close()
    print("-> LINEAS TOTALES:",cont_lineas)
    print("-> CARACTERES TOTALES:",cont_caracteres)

x = ruta_desktop()
verificar(x)
conteo(x)       