import random
lista = [5,9,10]
print(len(lista))
lista.append(11)
print (lista)
lista.insert (0,2.5)
print (lista)
print (lista[1:3]) #[inclusive : exclusive]
cuadrados = [x**2 for x in range(11)]
print (cuadrados)
# Compresión de lista [rellenar_termino  manera de llenar]
ajedrez = ["Peon" for i in range(8)]
print (ajedrez)
#Ejemplo 2
pares = [x for x in cuadrados if x%2 == 0] 
print (pares) #Podemos recorrer la lista de "cuadrados" añadiendo la sentencia "if" solo
              #desplegamos los numeros pares de la lista "cuadrados"

#Crear una lista bidimensional
tablero = [["Pieza" for i in range (8)] for j in range (8)]
print (tablero)

#Elije un elemento al azar
print(random.choice(lista))
lista.pop() #Elimina el último elemento o podemos mandar una parámetro
print (list(range(0,11,2))) #Crea un lista con la palabra reservada "list"