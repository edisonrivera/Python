class Fabrica:
    def __init__(self,nombre_fabrica,maquinas,tiempo,marca, tipo = None): #coloca el None para poder omitir valores
        self.nombre_fabrica = nombre_fabrica
        self.maquinas = maquinas
        self.tiempo = tiempo
        self.marca = marca
        self.tipo = tipo

    def __str__ (self):
        return f"{self.nombre_fabrica}{self.maquinas}{self.maquinas}{self.marca}{self.tipo}"

class Agregar(Fabrica):
    pass

class Extranjero(Fabrica):
    precio = ""
    def __str__(self):
        return f"{self.nombre_fabrica}{self.precio}"

auto = Fabrica("Honda", 4,10,"Lambo", "LUJOSO")
auto_competencia = Agregar("Chevrolet", 10, 2, "Ferrari","LUJOSO")
auto_strange = Extranjero("RUSOS",10,1,"Little Big","LUJOSO EXTRA")
auto_strange.precio = 15000

print("->",auto_competencia.nombre_fabrica)
print("->",auto.nombre_fabrica)
print("->",auto_strange.nombre_fabrica, "$",auto_strange.precio)

fabrica = [auto,auto_competencia]
fabrica_strange = [auto,auto_strange]
for x in fabrica:
    print(x.nombre_fabrica,x.marca) #Podemos acceder a atributos específicos

for x in fabrica_strange:
    if (isinstance (x, Fabrica)):
        print(x.marca, x.tiempo)
    elif (isinstance(x, Extranjero)):
        print(x.marca, x.maquinas)
    elif (isinstance(x, Extranjero)):
        print(x.nombre_fabrica,x.tiempo)

def descuento_auto(t,descuento):
    t.precio = t.precio - (t.precio/100*descuento)
    print(t.precio)

descuento_auto(auto_strange,10)