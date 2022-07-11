"""
    Las tuplas NO se pueden modificar. (Son inmutables)
"""

tupla = ('Hola', 'Mundo', 10, [1,2,3],10)
print ("Tupla:",tupla) 
print ("Acceder a elemnto en (tupla):", tupla[3][0])
print("Longitud (tupla):",len(tupla))
print("Posicion de \"Mundo\":",tupla.index('Mundo'))
print ("Veces elementos (10) en (tupla):",tupla.count(10))
miTupla = (1, 10, 100)
t1 = miTupla + (1000, 10000)

# Duplica n veces la tupla
t2 = miTupla * 3
print("La tupla (t2):",t2)
print("Longitud (t2):",len(t2))

# Comprobar la existencia de elementos
print("10 está (miTupla):",10 in miTupla)
print("-10 no está (miTupla):",-10 not in miTupla)


lista = [1, 10, 100]
miTupla = tuple(lista)
print(miTupla)