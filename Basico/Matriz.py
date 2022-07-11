filas = columnas = 3
matriz = []
for i in range (filas):
    matriz.append([])
    for j in range (columnas):
        a = int(input(f"-> [{i+1}][{j+1}] NUMERO: "))
        matriz[i].append(a)

for j in range (columnas):
    print(matriz[j])