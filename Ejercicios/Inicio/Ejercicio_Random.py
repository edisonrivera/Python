from random import sample
lista = []
lista_primos = []
cantidad = int(input("-> NUMERO: "))
for i in range (cantidad):
    x = int(input(f"{i+1} -> CANTIDAD: "))
    lista.append(x)
cantidad = int(input("-> NUMEROS AL AZAR: "))
lista_azar = sample(lista,cantidad)
verificar = 0
for i in lista_azar:
    for x in range(1,i+1):
        if (i % x == 0): verificar += 1
    if verificar == 2:
        lista_primos.append(i) 
    verificar = 0
print(lista_primos)