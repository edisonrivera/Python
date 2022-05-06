class Areas:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def areas (self):
        print("-> Cuadrado: ",self.base**self.base)
        print("-> TRIANGULO: ",(self.base*self.altura)/2)
        print("-> PENTAGONO: ",((self.base*self.altura)/2)*5)

base = int(input("-> BASE: "))
altura = int(input("-> ALTURA: "))
figura = Areas(abs(base),abs(altura))
figura.areas()