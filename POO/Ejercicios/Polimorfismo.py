#
# Nos permite redifinir o modificar un método heredado 
#

class Empleado():
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario
        
    def calcular_sueldo_anual(self):
        print(f"{self.nombre} gana $ {(self.salario*12)} al año")

class Abogado(Empleado):
    def __init__(self, nombre: str, salario: float, bono: int):
        super().__init__(nombre, salario)
        self.bono = bono
        
    def calcular_sueldo_anual(self):
        print(f"{self.nombre} gana $ {(self.salario*12) + (5000)} al año")

class Programador(Empleado):
    def __init__(self, nombre: str, salario: float):
        super().__init__(nombre, salario)
    
    def calcular_sueldo_anual(self):
        print(f"{self.nombre} gana $ {self.salario*13} al año")


profesiones = [
    Abogado("Joaquin", 500.50),
    Programador("Estela", 750)
]

for profesion in profesiones:
    profesion.calcular_sueldo_anual()