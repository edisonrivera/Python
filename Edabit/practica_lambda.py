from functools import reduce


lista_inicial = [1,2,3,3,123,123,12,5,346,5,8,67,89,679]

# ? Funciones

if __name__ == "__main__":
    print("LISTA INICIAL", lista_inicial)

    # ? MAP
    lista_map = list(map(lambda x: x*2,lista_inicial))
    print("map: Fuc.(x^2)",lista_map)

    # ? FILTER
    lista_filter = list(filter(lambda x: (x > 10) and (x%2==0), lista_inicial))
    print("filter: (x > 10) y PAR:", lista_filter)

    # ? REDUCE
    suma = reduce(lambda x,y: x +y, lista_inicial)
    print("reduce: suma", suma)