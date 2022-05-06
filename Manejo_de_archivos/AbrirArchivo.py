#try:
    # stream = open(r"C:\Users\User\Desktop\file.txt", "rt")
    # aqui se procesa el archivo
    # stream.close()
#except Exception as exc:
    #print("No se puede abrir el archivo:", exc)
try:
    stream = open(r"C:\Users\User\Desktop\file.txt", "rt") 
    stream.close()
except IOError as exc:
    print(exc.errno)