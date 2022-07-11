from PIL import Image
import os


"""
    ? os.path.splitext() -> Retorna una tupla de la parte "root" y la extension de un archivo.
    TODO path = '/home/User/Desktop/file.txt'
    ! root = '/home/User/Desktop/file'
    ! extension = '.txt'
"""

# TODO Cambiar la ruta para buscar mas imagenes
path_downloads = r"C:\Users\pc\Downloads"


def init_compress() -> None:
    for file in os.listdir(path_downloads):
        namefile, extension = os.path.splitext(path_downloads + file)
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(path_downloads + file)
            # ? pictures.save([path donde guardar], [nombre para guardar], *args)
            picture.save(path_downloads, "comp_" + file, optimize = True, quality =60)


if __name__ == "__main__":
    init_compress()