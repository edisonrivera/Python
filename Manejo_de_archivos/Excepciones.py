from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    s.close()
except Exception as exc:
    print("El archivo no se pudo abrir:", strerror(exc.errno))