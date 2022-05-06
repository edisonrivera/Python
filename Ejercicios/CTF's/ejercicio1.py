def menu_principal():
    print('{:>30}'.format("MENU PRINCIPAL"))
    print("""    1) Rellenar y modificar una lista
    2) Calculo de numeros primos en una rango definido por el usuario
    3) Contador de las escondidas""")
    opcion = int (input("{:>25}".format("> Ingrese su opcion: ")))
    while (opcion<1 or opcion>3):
        print("La opcion {} no se encuentra entres las opciones presentadas".format(opcion))
        opcion = int (input("> Ingrese su opcion: "))
    return opcion

def menu_primera_opcion():
    print('{:>30}'.format("OPCIONES DE LISTA"))
    print("""    1) Insertar elemento en la lista
    2) Eliminar elemento en la lista
    3) Limpiar la lista""")
    opcion_uno = int (input("> Ingrese su opcion: "))
    while (opcion_uno<1 or opcion_uno>3):
        print("La opcion {} no se encuentra entres las opciones presentadas".format(opcion_uno))
        opcion_uno = int (input("> Ingrese su opcion: "))
    return opcion_uno

def evaluar_opcion(x):
    if (x == 1):
        opcion_uno = menu_primera_opcion()
        if (opcion_uno == 1):
            
            pass
    elif (x == 2):    
        pass
    elif (x == 3):
        pass
    elif (x == None):    
        pass

def primera_opcion():
    lista = []



opcion = menu_principal()
evaluar_opcion (opcion)