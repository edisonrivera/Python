class Fabrica:
    def __init__(self,tiempo,tipo):
        self.tiempo = tiempo
        self.tipo = tipo
        print ("Auto por procesar... -> ", self.tipo)
    
    def __str__(self):
        return "{} ({})".format(self.tiempo,self.tipo)
    #def __len__(self):
    #    return self.tiempo
    
    #def __del__(self):
    #    print ("Auto inexistente",self.tipo)s
class Listado_de_autos_creados:
    autos = []
    def __init__(self,autos=[]):
        self.autos = autos
    
    def agregar_auto(self,newcar):
        self.autos.append(newcar)
    
    def inventario(self):
        for i in self.autos:
            print ("->",i)

auto = Fabrica(2,"Honda")
#print(len(auto))
#print(str(auto))
lista = Listado_de_autos_creados([auto])
lista.agregar_auto(Fabrica(15,"Lambo"))
lista.inventario()