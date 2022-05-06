def primos(*args):
    for number in args:
        acu = i = 0
        for i in range(i+1,number+1):
            if (number%i == 0):
                acu +=1
        if acu == 2:
            print(f"-> {number} es un número primo")
    
def in_dates(out_primos):
    datos = input("-> Ingresa los número separados por una coma: ")
    datos_filtrados = list(map(lambda x: int(x), datos.split(",")))
    out_primos(*datos_filtrados)

if __name__ == "__main__":
    lista = in_dates(primos)