#Crear un juego pokemon
from random import randint
import os

pikachu_life = actual_pika = 80
tortuga_life = actual_tortuga = 90
string = ''
print ("                                     COMIENZA LA BATALLA ¡¡        \n")
while actual_pika > 0 or actual_tortuga > 0:
    #Vamos a dar los turnos de combate 
    #Empieza pikachu

    pika_ataque = randint (1,2)
    print ( "Pikachu Ataca \n")
    if pika_ataque == 1:
        print("    TE HA GOLPEADO UNA BOLA DE FUEGO  :(  \n")
        actual_tortuga -= 10
    if pika_ataque == 2:                                   
        print("    TE HA APLASTADO UN MAZOOOOO    :(  \n")
        actual_tortuga -= 11

    #Turno de la tortuga
    print ("----- Ya es TU TURNO , es hora de vengarte. -------\n")
    
    op = None
    while  op != 0 and op != 1 and op != 2 and op != 3:
        print ("1. ATAQUE RAPTOR")
        print ("2. ATAQUE SERPIENTE")
        print ("3. ATAQUE AGUIJON DE ABEJA.")
        print ("0. ME RINDO ...")
        op = int(input("Escoge: "))
    if op == 0:
        print("Es una lástima, pero adiós.")
        break
    else:
        if op == 1:
            print ("        !!Le propicias un ataque raptor, como gusanito¡¡     \n" )
            actual_pika -= 10
        elif op == 2:
            print ("        !!Haaaaaa, mandaste una serpiente a Pikachu¡¡       \n")
            actual_pika -= 12
        else:
            print ("        !!Le han hinchado los cachetes¡¡    \n")
            actual_pika -= 9
    
    
    #VIDA DE LOS JUGAORES
    pika = "/"* actual_pika
    tortuga = "/"* actual_tortuga
    
    #Controlar la barra de vida para no mostrar valores negativos
    if actual_pika > 0 and actual_tortuga > 0 and op != 0:
        print ("Vida Pikachu [{}]".format(pika), actual_pika, "/", pikachu_life) 
        print ("Vida Tortuga [{}]".format(tortuga), actual_tortuga, "/", tortuga_life)

    #Continuación
    input("Enter para continuar...")
    os.system("cls")
    print ("\n                   SEGUIMOS CON LA LUCHA... ")

# Parte final
if op != 0:
    if actual_pika > actual_tortuga:
        print ("\n !!!! AY, PIKACHU TE HA APLASTADO Y NO TE DEJO NI PARA RECOGER CON CUCHARITA ¡¡¡¡ ")
    else:
        print ("\n !!!! YUPI, ERES EL GRAN GANADOR, TE AMITO AMORLAIS ¡¡¡¡ ")