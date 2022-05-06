from os import strerror
from sys import path

def comprobar_archivo():
    try:
        leer = open(path[0] + "\\Archivos\\Hola.txt","r")
        leer.close()
    except Exception as exc:
        print("!ERROR¡", strerror(exc.errno))
        exit()

def contar_letras():
    vocales = {}

    for i in range (97,123):
        vocales[f"{chr(i)}"] = 0

    for linea in open(path[0] + "\\Archivos\\Hola.txt","r"):
        for letter in linea:
            letter = letter.lower()
            for key_letra in vocales.keys():
                if letter == key_letra:
                    vocales[letter] += 1

    for key in vocales.keys():
        if vocales[key] != 0:
            print(key,"->",vocales[key])
    return vocales

def escribir_en_archivo(**diccionario):
    new = open(path[0] + "\\Archivos\\resultados.hist","w")
    sortedDict = sorted(diccionario.items(),key=lambda x: x[1],reverse=True)
    for i,o in sortedDict:
        new.write(f"{i} -> {o}\n")   

comprobar_archivo()
diccionario_contador = contar_letras()
escribir_en_archivo (**diccionario_contador)