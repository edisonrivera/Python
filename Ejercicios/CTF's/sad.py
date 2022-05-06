"""import time
print ("ESCONDIDAS")
for i in range (1,11,1):
    print(i," MISSISIPI")
    time.sleep(1)
print ("LISTOS O NO AHÍ VOY")
"""
from math import sqrt

def ecuacion(a,b,c):
    determinante = (b**2) - (4 * a * c)
    if (determinante > 0):
        x1 = -b *sqrt(+b+2-(4)*(a)*(c)) / (2*a)
        x2 = +b *sqrt(+b+2-(4)*(a)*(c)) / (2*a)
        return x1,x2
    elif (determinante == 0):
        x1= -b /(2*a)
        return x1
    else:
        return ("VALOR IMAGINARIO") 

valor1=int(input("a): "))
valor2=int(input("b): "))
valor3=int(input("c): "))
print(ecuacion(valor1,valor2,valor3))