from random import shuffle, randint

cadena = r'\nombres\Hola'
print (cadena)
print (cadena*3)
profesor = "Hola profe"
i = 0
for i in range (0,len(profesor),1):
    print (profesor[i])

print(profesor.endswith("e")) #Letra con que termina
print(profesor.startswith("H")) # letra con que empieza
print(profesor.isupper()) #Si toda la cadena es MAYUSCULA
print(profesor.islower()) # Si toda la cadena es minuscula

decimal = 100/888
#Formato de float "{valor:width.precisionf}"
print("{r:1.3f}".format(r = decimal))

for index,letter in enumerate(profesor):
    print (index, " - ",letter)


lista1 = [1,2,3]
lista2 = ["a","b","c"]

for item in zip(lista1,lista2): # "zip" empareja elemento de una lista
    print(item)

print(list(zip(lista1,lista2)))

print(min(lista1)) # Halla el valor mínimo
print(max(lista1)) # Halla el valor máximo
shuffle(lista1) # Desordena la lista de manera random
print(lista1)

randint(0,100) # Elemento aleatorio
print('[' + 'gamma'.center(20, '*') + ']')

if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# Ejemplo 1: Demostración del método isapha()
print("----->","Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostración del método isdigit()
    
print("| -----> ",'2018'.isdigit())
print("Año2019".isdigit())

def misplit(strng):
    strng = strng.strip(" ")
    return strng.split(" ")
    

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))


# Ejemplo 1: Demostración del método islower()
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper() 
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demostración del método swapcase()
print("Yo sé que no sé nada.".swapcase())

print()

# Demostración del método title()
print("Yo sé que no sé nada. Parte 1.".title())

print()

# Demostración del método upper()
print("Yo sé que no sé nada. Parte 2.".upper())