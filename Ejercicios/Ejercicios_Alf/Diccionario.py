def conteo (frase):
    frase = str(frase)
    palabras = {}
    lista_de_palabras = frase.split(" ")
    for i in lista_de_palabras:
        if len(i) != 0:
            palabras[i] = len(i)
    palabras_ordenado = sorted(palabras.items(),key= lambda x : x[1],reverse=True)
    for key,value in palabras_ordenado:
        print("- ",key,"->",value)

#Signos especiales
lista = ["\"","'",".","...",",","¿","?","¡"]

#Reemplazar cada signo por un espacio
x = input("-> Ingrese su frase: ")
for i in lista:
    x = x.replace(i, " ")

conteo(x)