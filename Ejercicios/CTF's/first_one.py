def rango ():
    while True:
        try:
            inicio = int(input("-> Inicio: "))
            final = int(input("-> Final: "))
            if (inicio < final and inicio > 0 and final > 0 and inicio != 0 and final != 0):
                break
            else: print ("El rango inicial tiene que ser menor al final")
        except:
            print ("Ingrese únicamente numeros mayores a 0")
    return inicio,final

def calcular(inicio, final):
    for x in range (inicio, final+1):
        cont = 0
        for i in range (1, final+1):
            if (x % i == 0): cont += 1
        if (cont == 2): print (x)

inicio, final = rango()
calcular (inicio,final)