while True:
    try:
        user_number = int(input("Ingrese su numero: "))
        break
    except:
        print ("Solo se permiten ingresar numeros")
cont = 0
for i in range (1,user_number+1):
    if (user_number%i == 0):
        cont +=1

if (cont == 2):
    print ("El numero es primo")
else:
    print("El numero no es primo")