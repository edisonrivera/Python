class Fabrica:
    def __init__(self,llantas,color,precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def poner_color(self):
        pass

    def __str__(self):
        return f"->LLANTAS: {self.llantas}\n->COLOR: {self.color}\n->PRECIO: {self.precio}"

class Moto(Fabrica):
    pass
class Carro(Fabrica):
    pass

llantas_moto = int(input("-> LLANTAS: "))
color_moto = input("-> COLOR: ")
precio_moto = float(input("-> PRECIO: "))
moto = Moto(llantas_moto,color_moto,precio_moto)
print(str(moto))

llantas_carro = int(input("-> LLANTAS: "))
color_carro = input("-> COLOR: ")
precio_carro = float(input("-> PRECIO: "))
carro = Carro(llantas_carro,color_carro,precio_carro)
print(str(carro))