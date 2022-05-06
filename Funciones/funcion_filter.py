from random import randrange
print("["+"TITULO".center(25," ") + "]")
lista = [randrange(101) for x in range (11)]
print("> | LISTA ORIGINAL:", end=" ")
print(lista)
lista_filtrada = list(filter(lambda x: x%2 == 0,lista))
print("> | LISTA PARES:", end=" ")
print(lista_filtrada)