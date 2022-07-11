import re


"""
    TODO re.match(pattern, string, flags = 0)
    
    ? - Nos devuelve una lista de coincidencias.
    ? - Tenemos que especificarle grupos con parentesis "()"

    * Ejemplo
    * re.search("^(.+), ?(.+)$", name)
    *  group(1)~~~~^      ^~~~~group(2)

"""

if __name__ == "__main__":
    name = input("-> Nombre: ").strip()
    if matches := re.match("^(.+), *(.+)$", name):
        for name in matches.groups():
            print(name)