import numpy as np

height = ([1.73,1.68,1.71, 1.89,1.79])
weight = ([65.4,59.2,63.6,88.4,68.7])
np_height = np.array(height)
np_weight = np.array(weight)
bidimensional_list = [[1,2,3],[4,5,6]]
np_bidimensional_list = np.array(bidimensional_list)
bmi = np_weight/np_height **2
print (bmi)

print(bmi[1]) #Accediendo de manera normal
print(bmi>23) #Da valores booleanos de acuerdo con la condicion a cumplir     variable = bmi >23 guarda datos
print(bmi[bmi>23]) #Crea una matriz con valores que concuerden con la condicion establecida
print(np_bidimensional_list.shape) #Informacion acerca de las filas y columnas
print(np.mean(np_height)) #Media
print(np.median(np_weight)) #Mediana
print(np_height.max()) #Número mayor