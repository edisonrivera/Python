from ntpath import join
from os import mkdir,makedirs

#TÓPICO 2) makedir

sub_path = "C:\\Users\\pc\\OneDrive - Escuela Politécnica Nacional\\Escritorio"
nombre_carpeta = "Random"

# 2.1 Se une la ubicación donde crearemos la carpeta y su nombre 
path = join(sub_path,nombre_carpeta)

# 2.2 Aquí se modificarán los permisos que la carpeta tenga
mode = 755
mkdir(path,mode)