tupla = ('Hola', 'Mundo', 10, [1,2,3],10)
print (tupla) #Las tuplas no se pueden modificar
print (tupla[3][0])
print("Longitud: ",len(tupla))
print("Posicion de palabra a encontrar: ",tupla.index('Mundo'))
print ("Cantidad de elementos repetidos: ",tupla.count(10))
miTupla = (1, 10, 100)
t1 = miTupla + (1000, 10000)
t2 = miTupla * 3
print(len(t2))
print(t1)
print(t2)
print(10 in miTupla)
print(-10 not in miTupla)