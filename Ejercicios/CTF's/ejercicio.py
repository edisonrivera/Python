from random import randrange

def values():
    try:
        beggin = int(input("-> INICIO: "))
        end = int(input("-> FIN: "))
        n = int(input("-> CANTIDAD DE VALORES: "))
        n = abs(n)
        if beggin > end:
            print ("¡ RANGOS INCOHERENTES!")
    except:
        print("¡ INGRESE VALORES VÁLIDOS !")
    return beggin,end,n

def random_values(beggin,end,n):
    i = 0
    while i < n:
        print(randrange(beggin,end+1))
        i += 1

a,b,c = values()
random_values(a,b,c)