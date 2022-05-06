def verificar_k(k,*tupla_datos):
    return True if (k*2) <= len(tupla_datos) else False
    
def sacar_min_max(k,verificador,*tupla):
    lista = []
    if verificador:
        for i in range (k):
            lista.append(tupla[i])
        for i in range (len(tupla)-k,len(tupla)):
            lista.append(tupla[i])
        new_tuple = tuple(lista)
        print(new_tuple)
    else:
        print("-> El valor de k no es válido")

while True: 
    try:
        tupla = input("-> Introduzca los datos separados por comas: ")
        tupla_datos = tuple(sorted(map(lambda x: int(x),tupla.split(","))))
        k = int(input("-> k datos: "))
        condicion = verificar_k(k,*tupla_datos)
        sacar_min_max(k,condicion,*tupla_datos)
        break
    except ValueError:
        print("\'k\' tiene que se un valor entero")