class fabrica:
    def __init__(self,tiempo,nombre,accesorios):
        self.tiempo = tiempo
        self.nombre = nombre
        self.accesorios = accesorios
        print ("Se creó el auto de MARCA {}".format(self.nombre))

    def __del__(self):
        print ("Se elmininó el auto de MARCA {}".format(self.nombre))

creacion = fabrica(24,"Toyota","Muchos")

class fabrica_2:
    def __init__(self,tiempo2,nombre2,accesorios2):
        self.tiempo2 = tiempo2
        self.nombre2 = nombre2
        self.accesorios2 = accesorios2
        print ("Se creó el auto de MARCA {}".format(self.nombre2))

    def __del__(self):
        print ("Se elmininó el auto de MARCA {}".format(self.nombre2))

    def __str__(self):
        return "{} se fabricó con exito en {} con {} accesorios".format(self.nombre2,self.tiempo2, self.accesorios2)
    def __len__(self):
        return self.tiempo2

creacion_objeto2 = fabrica_2(50,"Lambo","de locos")
print(str(creacion_objeto2))
print(len(creacion_objeto2))