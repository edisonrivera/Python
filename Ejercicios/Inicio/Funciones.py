def primera_funcion():
    print ('{:>35}'.format('Tabla de multiplicar'))
    global numero
    numero = 15
    
def segunda_funcion():
    for i in range (1,11):
        print("9 x {} = {}".format(i,i*9))

def tercera_funcion():
    return "Retorno de valor"

def cuarta_funcion():
    return 5, "Hola", [5,2,7]

def quinta_funcion(x,z):
    return x*z

def sexta_funcion(*args): #Retorna una tupla
    return print(sum(args) * 0.05)

def septima_funcion(**kwargs):
    if "fruit" in kwargs:
        print ("Mi fruta escogida es {}".format(kwargs["fruit"]))
    else:
        print ("No hay fruta :(")
        
def octava_funcion(*args,**kwargs):
    print(args)
    print(kwargs)
    print ("Me gustaría {} {}".format(args[0],kwargs["comida"]))

primera_funcion()
segunda_funcion()
print(tercera_funcion())
print(tercera_funcion()[0:8])
a,b,c = cuarta_funcion()
print ("""> Retornos de la cuarta_funcion: a) {} b) {}  c) {} """.format(a,b,c))
print(quinta_funcion(5,4))
sexta_funcion(40,50)
septima_funcion(fruit = "manzana",veggie = "lechuga")
octava_funcion(10,30,50, fruta = "naranaja", comida = "leche", animal = "perro")