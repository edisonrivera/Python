# La HERENCIA es unidireccional.
# Cuenta siempre con una super clase o "clase padre" de la cual 
# pueden heredar subclases o "clases hijas".

class Persona():
    def __init__(self, nombre: str, edad: int, cedula: str):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    
    def presentacion(self):
        print(f"Hola !, mi nombre es {self.nombre}, tengo {self.edad} años.")


class Trabajador(Persona):
    def __init__(self, nombre: str, edad: int, cedula: str, salario: int):
        super().__init__(nombre, edad, cedula) # Los argumentos son de la super clase
        self.salario = salario
    
    def presentacion(self):
        print(f"Hola !, mi nombre es {self.nombre}, tengo {self.edad} años, gano $ {self.salario}")


persona = Persona("Estela", 20, "1752774305")
persona.presentacion()

trabajador = Trabajador("Edison", 19, "1752774305", 450)