foods = list()
# TODO Evalua una expresion y guarda el resultado en la misma varible para luego poder usarla.
# ! Solo guarda valores booleanos
# ? - Se la envuelve en parentesis.

# ? Se desea comparar la var (condicion) con la var (walrus)
condicion = True
walrus = True
walrus = (walrus := condicion)
print("La condicion es:", walrus)


# ? Se guardan valores hasta que se ingrese "quit"
foods = list()
while (food := input("Quit to close: ") != "quit"):
    foods.append(food)
print("Veces correctas",foods)

# ? Ejercicio Uno
lista_paises = list()
iterator = 0
while (iterator<5):
    pais = input("-> Pais: ").strip()
    lista_paises.append(pais) if (condicion := pais.startswith("E")) else print("Siguiente")
    iterator += 1
print("Lista paises:", lista_paises)
