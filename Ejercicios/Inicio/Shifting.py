# Bits

numero = int(input("-> NUMERO: "))
numero_right = numero >> 1 # Es como dividir para 2 >> [cantidad de veces]
numero_left = numero << 2 # Es como multiplicar para 2 << [cantidad de veces]
print(numero_right,"-",numero_left)