from os import strerror
from sys import path

def original_file():
    origin = input("Nombre del archivo original:")
    try:
        first_file = open(path[0] + "\\Archivos\\" + origin,"rb")
        first_file.close()
    except IOError as err:
        print("Archivo no encontrado",strerror(err.errno)) 
        exit()
    return origin

def to_copy_file():
    copy = input("Nombre del archivo para copiar:")
    try:
        second_file = open(path[0] + "\\Archivos\\" + copy,"wb")
        second_file.close()
    except IOError as err:
        print("No se logró crear el archivo",strerror(err.errno)) 
        exit()
    return copy

def copy_files(original,copy):
    datos = bytearray(65536)
    first = open(path[0] + "\\Archivos\\" + original,"rb")
    second = open(path[0] + "\\Archivos\\" + copy,"wb")
    leido = first.readinto(datos)
    while leido != 0:
        second.write(datos[:leido])
        leido = first.readinto(datos) 
    print("¡COPIA EXITOSA!")
    first.close()
    second.close()
    
x = original_file()
y = to_copy_file()
copy_files(x,y)