ganadores = []
for i in range (0,5):
    numero = int(input(f"{i+1}) Numero de loteria: "))
    ganadores.append(numero)
ganadores.sort()
print(ganadores)