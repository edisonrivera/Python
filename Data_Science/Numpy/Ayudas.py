import numpy as np
lista = []
for i in range (0,11):
    number = float(input(f"{i} -> "))
    lista.append(number)

np_lista = np.array(lista)
print(np.mean(np_lista))