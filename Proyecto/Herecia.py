
class Marino():
    def __init__(self, nombre_especie: str):
        self.nombre_especie = nombre_especie

    def presentarse(self):
        print(f"Soy una especie marina, mi nombre es {self.nombre_especie}")
   
class Pulpo(Marino):
    def __init__(self, nombre_especie: str, color: str):
        super().__init__(nombre_especie)
        self.color = color

    def presentarse(self):
        print(f"Hola! Soy un pulpo mi nombre es {self.nombre_especie} y soy de color {self.color}")

class Medusa(Marino):
    def __init__(self, nombre_especie: str):
        super().__init__(nombre_especie)
    def presentarse(self):
        print("Soy una medusa")
        return super().presentarse()

if __name__ == "__main__":
    marino = Marino("Paco") 
    print("- Método de la clase Marino ")
    marino.presentarse();

    print("\n- Método de la clase Pulpo -")
    pulpo = Pulpo("Paul", "morado") 
    pulpo.presentarse()

    print("\n- Método de la clase Medusa -")
    medusa = Medusa("Medusita") 
    medusa.presentarse() 






