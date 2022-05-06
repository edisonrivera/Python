diccionario = {}
i = 0
llaves = 5
while i < llaves:
    valor = input("-> Llave: ")
    clave = input("-> Valor: ")
    diccionario[valor] = clave
    i += 1

print(diccionario)