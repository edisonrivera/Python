#Alinear
print ("Hola. {:20}. Curioso verdad?".format("Yo me moveré"))  # Son lo
print ("Hola. {:<20}. Curioso verdad?".format("Yo me moveré")) # MISMO

print ("Hola. {:>20}. Curioso verdad?".format("Yo me moveré"))
print ("Hola. {:^20}. Curioso verdad?".format("Yo me moveré"))  
#Números
numero = 3.14151817
miles = 2000
decimal = 1000
print("Testea con: {:.2f}".format(numero)) # .nf   n = número de decimales
print("Testea con: {:,}".format(miles)) # Incluye una coma al inicio de todos los ceros
print("Pasar a binario: {:b}".format(decimal)) # Pasa a binario el número
print("Pasar a octal: {:o}".format(decimal)) # Pasa a octal el número
print("Pasar a hexadecimal: {:X}".format(decimal)) # Pasa a hexadecimal con la variante x = minúscula y X = mayúscula
print("Pasar a notación científica: {:e}".format(decimal)) # Pasa a notación científica