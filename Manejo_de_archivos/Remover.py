import os

# os.rmdir = Remueve directorios vacíos
# shutil.rmtree = Remuve directorio llenos, previamente importar shutil

try:
    os.remove(r"Avanzados\Manejo_de_archivos\Archivos\Creado.txt")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You don't have permissions to remove this file")
except OSError:
    print("The directory isn't empty")
