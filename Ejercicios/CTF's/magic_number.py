from random import randrange
def get_magic_number(): #Consiguiendo el número random
    print("MINI JUEGO EN PYTHON, NUMERO MÁGICO ENTRE (0 - 100)")  
    return randrange(0,100)

def numbers (): #El usuario ingresa el número para los intentos
    while True:
        try:                                                    #Permitir que el usuario solo ingrese
            user_number = int(input("-> Ingrese su numero: "))  #números
            break
        except:
            print("Solo se permiten numeros")
    return user_number
    
def comparate_number (number,user_number): #Comparar números para guiar al usuario
    cont = 0
    while True:
        if number == user_number:
            print ("! You won this game ¡ \nAttemps: {}".format(cont))
            break
        print ("Your number is higher" if (number < user_number) else "Your number is lower")
        cont += 1    
        user_number = numbers()
    
number = get_magic_number()
user_number = numbers()
comparate_number (number,user_number)