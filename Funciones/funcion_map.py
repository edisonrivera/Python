lista_inicial = [x for x in range(11)]
lista_map_uno = list(map(lambda x: x**2,lista_inicial))
print(lista_map_uno)

for x in map(lambda x : x / 2,lista_map_uno):
    print(f"[{x}]", end = " ")