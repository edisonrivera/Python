from os import path

rute = r"C:\Users\pc\Python\Manejo_de_archivos\Archivos\Cubos.txt"

if path.exists(rute):
    print("La ruta existe")
    if path.isfile(rute):
        print("Es un archivo")
    elif path.isdir(rute):
        print("Es un directorio")
else:
    print("Not found !")