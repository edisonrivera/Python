class Persona():
    def __init__(self,nombre: str, edad: int, dni: int):
        self.nombre = nombre 
        self.edad = edad 
        self.dni = dni 
        
    def presentacion(self):
        print(f"Hola! Soy {self.nombre}, tengo {self.edad}.")

class Trabajador(Persona):
    def __init__(self, nombre: str, edad: int, dni: int, sueldo: int, cargo: str, empresa: str):
        super().__init__(nombre, edad, dni)
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa
    
    def job_presentation(self):
        print(f"""Hola! Soy {self.nombre}, tengo {self.edad}.
        Trabajo de {self.cargo}, en {self.empresa} y gano ${self.sueldo}
        """)
        
class Estudiante (Persona):
    def __init__(self, nombre: str, edad: int, dni: int, universidad: str, carrera: str):
        super().__init__(nombre, edad, dni)
        self.universidad = universidad
        self.carrera = carrera
    
    def presentacion(self):
        return super().presentacion()

persona = Persona("Edison", 19, "175897846")
persona.presentacion()

trabajador = Trabajador("Paul",19,"123457987", 20, "soporte", "anonima")
trabajador.job_presentation()

estudiante = Estudiante("Juan",20, "dwadawdaw", "EPN", "Sistemas")
estudiante.presentacion()