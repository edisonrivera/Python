from random import randint
lista = [randint(0,101) for i in range (0,10)]
print(lista)
print([x**2 for x in lista])