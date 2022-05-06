class Empleado ():
    def __init__(self, nombre: str, sueldo: float):
        self.sueldo = sueldo
        self.nombre = nombre
    
    def calcular_sueldo(self):
        sueldo_anual = 12*self.sueldo*(1 + 1/100)
        print(f"Empleado: {self.nombre}, gana ${sueldo_anual}")


class Ingeniero(Empleado):
    def __init__(self, nombre: str, sueldo: float):
        super().__init__(nombre, sueldo)
        
    def calcular_sueldo(self):
        sueldo_anual = 12*self.sueldo*(1 + 4/100)
        print(f"Empleado: {self.nombre}, gana ${sueldo_anual}")


class Medico (Empleado):
    def __init__(self, nombre: str, sueldo: float):
        super().__init__(nombre, sueldo)
    
    def calcular_sueldo(self):
        sueldo_anual = 12*self.sueldo*(1 + 5/100)
        print(f"Empleado: {self.nombre}, gana ${sueldo_anual}")

empleados = [
    Empleado("Edison", 450),
    Ingeniero("Estela", 550.90),
    Medico("Juan", 1000.85)
]

for empleo in empleados:
    empleo.calcular_sueldo()
