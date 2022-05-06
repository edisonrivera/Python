#
# Sirven para modificar el comportamiento de una función.
#


# PRIMER EJEMPLO

def externa(foreing_fuction):
    def interna():
        print("-> Ejecución de la función interna... ")
        foreing_fuction()
        print("-> End of foreing_fuction <-\n")
    return interna

@externa
def saludar():
    print("Hola mundo")

@externa
def despedirse():
    print("Adios")

saludar()
despedirse()



# SEGUNDO EJEMPLO

def sumar(*args, **kwargs):
    acu = 0
    for number in args:
        acu += number
    return acu
    
def solo_pares(operacion):
    def resolv_problem(*args, **kwargs):
        pares = list(filter(lambda x: x%2 == 0, args))
        resultado = operacion(*pares, **kwargs)
        print(f"El resultado es: {resultado}")
    return resolv_problem


sumar_pares = solo_pares(sumar)
sumar_pares(2,4,5,4)

@solo_pares

def multiplicar(*args, **kwargs):
    acu = 1
    for number in args:
        acu *= number
    return acu

multiplicar(1,2,5,1,10)