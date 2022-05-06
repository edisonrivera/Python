class Figure():
    def __init__(self,alto,ancho):
        self.alto = alto
        self.ancho = ancho

class Cuadrado(Figure):
    def __init__(self,alto,ancho):
        super().__init__(alto,ancho)
    
    def area(self):
        return self.alto * self.ancho

class Cubo(Figure):
    def __init__(self,alto,ancho,largo):
        super().__init__(alto,ancho)
        self.largo = largo
    
    def area(self):
        return self.alto * self.ancho * self.largo

cuadrado = Cuadrado(10,20)
cubo = Cubo(20,40,50)
print(cuadrado.area())
print(cubo.area())