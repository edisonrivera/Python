conjunto = {5,4,3}
print (conjunto)
conjunto.add (2)
print (conjunto)
conjunto.add (6)
print (conjunto)
conjunto.add('H')
conjunto.add('A')
conjunto.add('Z')
print(conjunto)
#Para crear un conjunto vacío usamos conjunto.set = {}
#No nos deja tener elementos repetidos
print(5 in conjunto)
lista = [5,5,10,5]
conjunto2 = set(lista) # Pasar de lista a conjunto
print (conjunto2)
cadena = "Hola mundo por lo general es la primera linea de que condificamos"
print(set(cadena)) #Eliminamos los caracteres repetidos