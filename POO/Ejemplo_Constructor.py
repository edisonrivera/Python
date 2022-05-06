class Fabrica:
    def __init__(self,tiempo,marcas,maquinas):
        self.tiempo = tiempo
        self.marcas = marcas
        self.maquinas = maquinas
        print("Se creó el auto: ", self.marcas)

    def __str__(self):
        return f"En {self.tiempo} horas se armó el auto {self.marcas}"

    def __len__(self):
        return self.tiempo

    def __del__(self):
        print ("Se destruyó el auto", self.marcas)

new_car = Fabrica(10,"Mazda",5)
print(str(new_car))
print(len(new_car))