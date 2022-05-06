import shutil

#copyfile() = copia el contenido de una archivo
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy + copia la metadata del archivo

src_file = r"C:\Users\pc\Python\Manejo_de_archivos\Archivos\resultados.hist"

shutil.copy(src_file,"Copia.txt") #(ruta archivo original,ruta archivo destino)