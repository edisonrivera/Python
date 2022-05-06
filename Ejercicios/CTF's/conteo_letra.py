def conteo (letra,parrafo):
    contador = 0
    for i in parrafo:
        if i == letra:
            contador += 1
    return contador

x = input("-> Letra/Simbolo: ")
y = input("-> Texto: ")
print("-> Resultado:",conteo(x,y))