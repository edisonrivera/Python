from os import strerror
from sys import path

def comprobar_archivo():
    try:
        first = open(path[0] + "\\Archivos\\lista.txt","r")   
        first.close()
    except IOError as err:
        print("¡ERROR!", strerror(err.errno))
        exit()

def leer_archivo():
    estudiantes = {}
    for linea in open(path[0] + "\\Archivos\\lista.txt","r"):
        pre_ordenador = linea.split(" ")

        if len(pre_ordenador) != 3:
            print("¡ERROR!, datos mal ingresados")
            exit()

        nombre_estudiante = " ".join(pre_ordenador[:2])
        nota = int(pre_ordenador[-1])
        estudiantes[nombre_estudiante] = nota

    return estudiantes

def compilar_resultados(**datos):
    new_file = open(path[0] + "\\Archivos\\lista_nueva.txt","w")
    new_file.write("|"+"LISTA DE ESTUDIANTES".center(34," ")+"|\n")
    new_file.write("------------------------------------\n")
    new_file.write("|     NOMBRE COMPLETO     | PUNTOS |\n")
    new_file.write("------------------------------------\n")

    for nombre,puntos in datos.items():
        new_file.write("|" + f"{nombre}".center(25," ") + "|" + f"{puntos}".center(8," ") + "|"+"\n")
    new_file.write("------------------------------------")
    new_file.close()

comprobar_archivo()
dic = leer_archivo()
compilar_resultados(**dic)