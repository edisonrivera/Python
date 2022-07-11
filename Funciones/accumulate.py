from itertools import accumulate

"""
    ? accumulate(lista, funcion)
    TODO retorna el resultado inmediato (uno a uno)
"""

lista = [1,23,3,5,8]



for number in accumulate(lista, lambda x,y: x + y):
    print(number)