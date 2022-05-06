class Animal():
    def __init__(self):
        print ("Animal Creado")

    def quien_soy(self):
        print("Soy un animal")

    def comer(self):
        print("Estoy comiendo")

class Perro(Animal): #Herencia de Animal
    def __init__(self):
        Animal.__init__(self)
        print("Perro Creado")

    def quien_soy(self):
        print("Soy un perro")