from abc import ABC, abstractmethod

class Personaje(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 500

    @abstractmethod
    def atack (self, enemy):
        pass

    @abstractmethod    
    def get_status(self):
        print(f"{self.nombre}. Nivel {self.nivel}")

    def level_up(self):
        self.nivel += 1

    def inventory(self):
        print(f"Inventario de {self.nombre}")
        for objecto in self.inventario:
            print(objecto)   

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 250
        self.inteligencia = 95
        self.inventario = ["Piedra filosofal", "Varita mágica"]

    def get_status(self):
        print("Es un mago ahora !")
        super().get_status()

    def atack(self, enemy):
        enemy.vida -= self.inteligencia*0.6
        print(f"Vida del enemigo {enemy.nombre} a bajado a {enemy.vida} después del ataque de {self.nombre}")
        return super().atack(enemy)

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 400
        self.fuerza = 80
        self.inventario = ["Espada", "Escudo", "Arco"]

    def get_status(self):
        print ("Es un guerrero ahora !")
        return super().get_status()

    def atack(self, enemy):
        enemy.vida -= self.fuerza*0.8
        print(f"Vida del enemigo {enemy.nombre} a bajado a {enemy.vida} después del ataque de {self.nombre}")
        return super().atack(enemy)

guerrero = Guerrero("Kaladin")
mago = Mago("Yuno")

guerrero.get_status()
mago.get_status()

guerrero.inventory()
mago.inventory()

mago.atack(guerrero)
guerrero.atack(mago)