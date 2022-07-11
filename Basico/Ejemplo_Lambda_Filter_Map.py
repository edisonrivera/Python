#Funcion map es útil para pasar un lista a una
#función
numeros = [1,2,3,4,5]
def square(num):
    resultado = num**2
    return resultado

for item in map(square,numeros):
    print (item)

print(list(map(square,numeros)))

#Funcion filtro
def check_even (num):
    return num %2 == 0

for n in filter(check_even,numeros):
    print (n)

#Lambda
square = lambda num: num ** 2
print (square(5))
print(list(map(lambda num: num**2, numeros)))
print(list(filter(lambda num: num%2 == 0, numeros)))
