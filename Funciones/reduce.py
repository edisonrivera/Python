from functools import reduce
from operator import add
"""
? Modo de operación -> Retorna un único valor
? reduce usa los dos primeros datos iterables, se establece una operación y posterior a eso
?  hace lo mismo, es decir: [5,4,3,2,1]
TODO x, y = x*y => 5*4 = 20 [20,3,2,1] => 20*3 = 60 [60,2,1] => 60*2 [120*1] => 120*1 = 120
"""

"""
    TODO operator fuctions:
    ? - add
    ? - mul
"""

lista = [5,4,3,2,1]
valor_reducido = reduce(lambda x,y : x*y,lista)
print("Multiplicacion total:",valor_reducido)

suma_total = reduce(add, lista,10)
print("Suma total:", suma_total)


number_max = reduce(lambda a,b: a if a>b else b, lista)
print("Numero max.':",number_max)
