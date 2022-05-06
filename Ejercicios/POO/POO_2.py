class Carro: #Clase
    Rojo = False
    def __init__(self,puertas,color):
        self.puertas = puertas
        self.color = color
        print("Se creo un auto con puertas {} y color {}".format(self.puertas,self.color))

    def Fabricar (self):
        self.Rojo = True
        
    def confirmar(self):
        if (self.Rojo):
            print ("Color final ROJO")
        else:
            print("Falta pintar el auto")

crear = Carro(2, "Negro")