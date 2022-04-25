class Hogar(): # SuperClase
    def __init__(self, paredes: int, ventanas: int, cuarto_lavado: bool, direccion: str):
        self.paredes = paredes
        self.ventanas = ventanas
        self.cuarto_lavado = cuarto_lavado
        self.direccion = direccion
        self.pais = "Ecuador"
    
    def caracteristicas_casa(self):
        print("--- Caracteristicas de la vivienda ---")
        print("-> Numero de paredes: ", self.paredes)
        print("-> Cantidad de ventanas: ", self.ventanas)
        print("-> Tienes cuarto de lavado?", self.cuarto_lavado)
        print("-> Direccion", self.direccion)
        print("-> Pais de residencia", self.pais)


class Departamento(Hogar): # Subclase
    def mensaje(self):
        print("Estas instanciando la clase Departamento")


if __name__ == "__main__":
    departamento = Departamento(10,5,True,"Centro Historico")
    departamento.caracteristicas_casa()
    departamento.mensaje()