# Públicos: Accedidos desde cualquier punto del código.
# Protegidos: La misma clase y subclases. (_variable)
# Privados: Únicamente desde la misma clase. (__variable)

# La encapsulación en Python ! NO EXISTE ¡, lo anterior escrito es 
# una convención entre programadores

# La sintaxis para poder acceder a un "atributo privado" es
# [nombre_del_objeto]._[Nombre_de_la_clase]__[nombre_del_atributo]


class Circulo():
    def __init__(self, diametro: float):
        self._diametro = diametro
        self.__pi = 3.1415
    
    def calcular_perimetro(self):
        return round(self._diametro * self.__pi,2)
    
    def calcular_area(self):
        return round(self.__pi * (self._diametro/2) ** 2,2)
    
    def return_pi(self):
        return self.__pi 

circulo = Circulo(15.2)
print(circulo._Circulo__pi) # Accedemos a "diametro"
print(circulo.calcular_perimetro())
print(circulo.calcular_area())
print("La constante PI tiene un valor de:", circulo.return_pi()) # Le permitimos acceder a un valor sin "mucho esfuerzo"