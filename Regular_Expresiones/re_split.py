"""
    TODO re.split(pattern, srting, maxsplit=0, flags=0)
    ? maxsplit=0 -> numeros de veces que se hará el patrón.
"""
import re


palabra = 'A! B. C'
lista_letras = re.split("\W+",palabra,1)

print(lista_letras)