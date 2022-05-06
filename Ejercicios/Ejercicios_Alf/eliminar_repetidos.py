lista_usuario = input("Elementos separados por comas: ")
lista =  list(set(lista_usuario.split(",")))
print(lista)