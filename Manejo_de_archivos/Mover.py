import os

src = r"C:\Users\pc\Python\Manejo_de_archivos\Archivos\Cubos.txt"
dst = r"C:\Users\pc\OneDrive - Escuela Politécnica Nacional\Escritorio\Cubos.txt"

# Mueve archivos o carpetas

try: 
    if os.path.exists(dst): #Comprobar si existe otro archivo con el mismo nombre en el destino
        print("Ya existe un archivo con este nombre")
    else:
        os.replace(src,dst) # (ruta de origen, ruta de destino)
except FileNotFoundError:
    print(src + "Not found !")