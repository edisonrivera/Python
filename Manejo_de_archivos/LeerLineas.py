from os import strerror
try:
    stream = open(r"Avanzados\Manejo_de_archivos\Archivos\hola.txt","rt",encoding="UTF-8")
    #print(stream.read())
    leer_linea1 = stream.readline()
    leer_linea2 = stream.readline()
    leer_linea3 = stream.readline()
    print(leer_linea2,end="")
    print(leer_linea1)
    stream.close()
except Exception as exc:
    print("!ERROR¡",strerror(exc.errno))