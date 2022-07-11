"""
    TODO re.findall(pattern, string, flags=0)
    ? - Encuentra el patrón en varias lineas de texto.
    ? - Devuelve una lista de coincidencias.
"""

import re


parrafo = """
Python will search 09981822 the regular expression pattern and 
return the first occurrence. The Python RegEx Match 120203939
"""

lista_numeros = re.findall("\d+", parrafo)
print(lista_numeros)