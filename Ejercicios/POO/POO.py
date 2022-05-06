#Clases Objetos
class Carro: #Clase
    Rojo = False
    def __init__(self):
        print ("Se creo un auto")

    def Fabricar (self):
        self.Rojo = True
        
    def confirmar(self):
        if (self.Rojo):
            print ("Color final ROJO")
        else:
            print("Falta pintar el auto")

crear = Carro()
crear.Fabricar()
print(crear.Rojo)
crear.confirmar()
consecionaria = Carro() #Objeto creado
consecionaria.color = "Rojo"
consecionaria.puertas = "Muchas"
print ("Mi auto es de color {} y tiene {} puertas".format(consecionaria.color,consecionaria.puertas))

