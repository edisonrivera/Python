diccionario = {'Carro':'Azul', 'Hola':'Mundo', 'Edad':20}
print(type (diccionario))
print(diccionario['Carro']) #Se muestra el nombre que acompaña
diccionario['Carro'] = 'Rojo'
print(diccionario)
del(diccionario['Carro'])
print(diccionario)
diccionario['Edad'] += 1
print(diccionario)
for i in diccionario:
    print(i)
for i in diccionario:
    print(i,diccionario[i])
#Podemos incluir diccionarios en listas
dict = {"gato" : "gato", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    if key == dict:
        print("hola")
    print(key, "->", dict[key])

for key in sorted(dict.keys()):
    print(key, "->", dict[key])
    
dict = {"gato" : "perro", "dog" : "chien", "caballo" : "cheval"}
dict['gato'] = 'minou'
print(dict)
dict.update({"pato" : "canard"})
dict.update({"gato": "perro"})
print(dict)
del dict['dog']
print(dict)
dict.clear()
print(dict)
miDict = {"A":1, "B":2}
copyMiDict = miDict.copy()
miDict.clear()
print(copyMiDict)

diccionario["llave_extra"] = 500 #Agregar elementos
print (diccionario.keys()) #Muestra todas las llaves
print(diccionario.values()) #Ver el contenido de las llaves
print(diccionario.items()) #Separa por parentesis