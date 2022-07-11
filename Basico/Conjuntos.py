superSet = {1,2,3,4,5,6,7,8,9,10}
conjunto = {1,2}
 
# ? Para crear un conjunto vacío usamos conjunto.set = ()
conjunto_datos = set()

# ? Añadir datos al conjunto
conjunto.add (3)
conjunto.add (4)

conjunto_datos.add('H')
conjunto_datos.add('A')
conjunto_datos.add('Z')
print(conjunto)


# ? No nos deja tener elementos repetidos
print(5 in conjunto)

# ? Pasar de lista a conjunto
lista = [5,5,10,5]
conjunto2 = set(lista) 
print (conjunto2)

# ? Transformar cadean a conjunto
cadena = "Hola mundo por lo general es la primera linea de que condificamos"
print(set(cadena)) 


# ? Altera el conjunto inicial, elimina el arg que le demos
conjunto.discard(4)
print(conjunto)

# ? Elimina el primer elemento
conjunto.pop() 
print(conjunto)

# ? Verificar si es un super conjunto
print("(superSet) es super conjunto de (conjunto):", superSet.issuperset(conjunto))




"""  
    ! OPERACIONES EN CONJUNTOS

    ? | Une dos o más conjunto
    ? & Elementos que se repiten en los dos conjuntos
    ? - Elementos del primer conjunto que no se encuentren en el segundo conjunto.
    ? ^ Elementos que nos son comunes en los dos conjuntos
"""

print("--- OPERACIONES EN CONJUNTOS ---")

A = {1,2,3,4}
B = {2,4,6,8}

print("UNION:",A | B)

print("INTERSECCION:",A & B)

# ? Todos los elementos de A que no estén en B
print("DIFERENCIA:",A - B)

print("NO SON COMUNES:",A ^ B)