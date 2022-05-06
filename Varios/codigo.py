from re import findall
from time import sleep

for linea in open("ludonusimi.html","r",encoding="utf-8"):
    if ("<b>" and "</b>") in linea:
        linea = linea.lstrip()
        sleep(2)
        encontrado = findall('^<b>([A-Za-z]*)',linea)
        if encontrado:
            print(encontrado)      