lista_inicial = [x for x in range(11)]

# ? 1) Uso basico de lambda
lista_map_uno = list(map(lambda x: x**2,lista_inicial))
print(lista_map_uno)

# ? 2) Uso con for
for x in map(lambda x : x / 2,lista_map_uno):
    print(f"[{x}]", end = " ")


lista_uno = [1,5,3,5,6,6]
lista_dos = [15,6,6,2,33,1]

# ? 3) Usar con mas de una lista
lista_suma = list(map(lambda x,y : x +y, lista_uno,lista_dos))
print("\nLista de sumas:", lista_suma)

# ? 4) Otro uso
lista_palabras = ["gato", "perro", "conejo"]
lista_lista_palabras = list(map(list, lista_palabras))
print(lista_lista_palabras)