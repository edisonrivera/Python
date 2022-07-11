from random import choice, sample, shuffle

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst)) #Escoge un numero al azar
print(sample(lst, 5)) #Escoge n números al azar
shuffle(lst) #Desordena la lista que le pasemos
print(lst)