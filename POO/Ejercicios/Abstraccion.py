# CLASES ABSTRACTAS:
#   - No las vamos a instanciar.
#   - Contiene por lo menos un método abstracto.
#   - Las vamos a usar de base para subclases más específicas
# METODOS ASBTRACTOS:
#   - Debemos sobreescribirlos en cada una de las subclases

from abc import ABC, abstractmethod


class Personaje(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self.name = name
        self.level = 0
        self.inventary = []
        self.life = 100
    
    @abstractmethod
    def attack (self, objetivo_to_attack: str):
        pass

    @abstractmethod
    def get_status(self):
        print(f"Nombre: {self.name}; Nivel: {self.level}\n")

    def level_up(self):
        self.level += 1

    def inventory(self):
        print(f"\nInventario de {self.name}")
        for object in self.inventary:
            print (f"-> {object}")
    
class Mago(Personaje):
    def __init__(self, nombre: str):
        super().__init__(nombre)
        self.life = 150
        self.hability = 200
        self.inventary = ["Life shell", "Fire Attack", "Flash Attack"]

    def attack(self, objetivo_to_attack):
        attack = self.hability*.6
        print(f"El Mago {self.name} le provocó un daño de {attack} a {objetivo_to_attack.name}")
        objetivo_to_attack.life -= attack
        return super().attack(objetivo_to_attack)

    def inventory(self):
        return super().inventory()

    def get_status(self):
        print("-- Es un Mago --")
        return super().get_status()     


class Guerrero(Personaje):
    def __init__(self, name: str):
        super().__init__(name)
        self.life = 500
        self.force = 100
        self.inventary = ["Sword", "Bow"]

    def attack(self, objetivo_to_attack: str):
        attack = self.force * 0.5
        print(f"El Guerrero {self.name} le provocó un daño de {attack} a {objetivo_to_attack.name}")
        objetivo_to_attack.life -= attack
        return super().attack(objetivo_to_attack)

    def inventory(self):
        return super().inventory() 

    def get_status(self):
        print ("-- Es un Guerrero --")
        return super().get_status()  

mago = Mago("Estela")   
guerrero = Guerrero("Edison")
mago.attack(guerrero)
guerrero.attack(mago)

mago.get_status()
guerrero.get_status()

mago.inventory()
guerrero.inventory()