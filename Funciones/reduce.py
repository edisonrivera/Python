from functools import reduce

# Modo de operación
# reduce usa los dos primeros datos iterables, se establece una operación y posterior a eso
# hace lo mismo, es decir: [5,4,3,2,1]
# x, y = x*y => 5*4 = 20 [20,3,2,1] => 20*3 = 60 [60,2,1] => 60*2 [120*1] => 120*1 = 120

lista = [5,4,3,2,1]
factorial = reduce(lambda x,y : x*y,lista)
print(factorial)