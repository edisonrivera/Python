from time import perf_counter


def calculos(numero: int) -> int:
    return  (numero * numero) / (numero**2)

lista = [1,2,3,4,5,3,4,5,6,7,8,89,9,3,3,45,1,
        12,3,3,4,45,6,45,6,45,2,3,4,45,3,4,3,
        3,4,2,34,3,4,4,23,3,4,4,45,5,3,2,3,4,
        5,34,6,4,4,23,3,4,4,42,1,1,2,6,43,6,
        3,4,1,3,4,5,6,7,67,8,9,3,3,3,5,4,67]

otra_lista = []

inicio = perf_counter()
for i in range(100000):
    for numero in lista:
        otra_lista.append(calculos(numero))

fin = perf_counter()

print("Time: ", round((fin-inicio),4),"s")