def primera_funcion(a,b):
    return a-b

def segunda_funcion(x = None, z = None):
    if (x == None and z == None):
        print ("Debes ingresar los dos parametros")
        return
    else: 
        print ("Bien hecho")
        return x*z

def tercera_funcion(*tupla): #Para mandar parametros "ilimitados"
    for tus in tupla:
        print (tus)

def cuarta_funcion(**diccionario): #Para diccionarios
    print(diccionario)

def quinta_funcion (*tupla,**diccionario):
    band = 0
    for tus in tupla:
        band +=tus
    print (band)
    for x in diccionario:
        print(x,diccionario[x])

print("Primera funcion: ",primera_funcion(b = 4,a = 2)) #Argumentos por nombre
print("Primera parte: ", segunda_funcion())
print("Segunda parte: ", segunda_funcion(4,2))
tercera_funcion("Hola", "Mundo", "Notas", 10)
cuarta_funcion(carro = "Azul", notas = "Bien", lenguaje = "Python")
quinta_funcion(10,45,10,carro = "Azul", notas = "Bien", lenguaje = "Python")