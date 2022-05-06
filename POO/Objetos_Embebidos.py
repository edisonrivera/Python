class Fabrica:
    def __init__(self,tiempo,marcas,maquinas):
        self.tiempo = tiempo
        self.marcas = marcas
        self.maquinas = maquinas
        print("Se creó el auto:",self.marcas)

    def __str__(self):
        return f"{self.tiempo},{self.marcas},{self.maquinas}"

class Listado:
    lista_autos = []
    def __init__(self,lista_autos=[]):
        self.lista_autos = lista_autos
        
    def agregar_auto(self,nuevo_auto):
        self.lista_autos.append(nuevo_auto)
    
    def inventario (self):
        i = 0
        for auto in self.lista_autos:
            print(f"{i} -> ",auto)
            i += 1

new_car = Fabrica(10,"Mazda",5)
listado = Listado([new_car])
#listado.agregar_auto(new_car)
listado.inventario()